#!/bin/env python

import os, re, sys, traceback
import typesense
import yaml


def debug(s):
    pass

def info(s):
    print(f'[INFO] {s}')

def error(s):
    sys.stderr.write(f'[ERROR] {s}\n')


def first_sentence(lines):
    def good(line):
        if line.startswith('#'): return False      # ignore headers
        if re.match('^[=-]+$', line): return False # ignore section dividers
        return True

    s = ''.join(line for line in lines if good(line))
    s = re.sub('<[^>]*>', '', s)                   # strip HTML
    s = re.sub('{%[^%]*%}', '', s)                 # strip Liquid tags
    s = re.sub('\[([^]]*)\]\([^\)]*\)', '\\1', s)  # strip Markdown links
    s = re.sub('\*+\\s*([^\*]*)\\s*\*+', '\\1', s) # strip emphasis
    s = re.sub('\\s\\s*', ' ', s)                  # unify whitespace
    dot = s.find('. ')
    if dot >= 0: s = s[:dot+1]                     # cut down to first sentence
    return s.strip()


def connect():
    """
    Open a connection to the typesense server.
    """
    with open('/etc/typesense/typesense-server.ini') as f:
        lines = f.readlines()

    api_key = [line[10:] for line in lines if line.startswith('api-key = ')][0].rstrip()

    return typesense.Client({
      'nodes': [{
        'host': 'search.imagej.net',
        'port': '8108',
        'protocol': 'https'
      }],
      'api_key': api_key,
      'connection_timeout_seconds': 2,
    })


def summary(client, name):
    summary = client.collections.retrieve()
    for item in summary:
        if item['name'] == name:
            return item


def drop(client):
    """
    Delete the ImageJ wiki collection.
    """
    client.collections['imagej-wiki'].delete()
    info('Deleted existing collection')


def create(client, documents, force=False):
    """
    Create the ImageJ wiki collection, if it doesn't already exist.

    :return: True if newly created; False if collection already exists.
    """
    if summary(client, 'imagej-wiki'):
        # already exists
        if force: drop(client)
        else: return False

    # Typesense allows you to index the following types of fields:
    #   string, int32 int64, float, bool
    #   string[], int32[], int64[], float[], bool[]

    # Make a schema out of all the fields present across all the documents:
    # a union of all the observed YAML keys, plus the three required fields.
    fieldset = set()
    for doc in documents:
        fieldset.update(doc)
    fieldset -= {'id', 'score', 'title', 'content'}
    fields = [
        {'name': 'score',   'type': 'int32'}, # for tie-breaking
        {'name': 'title',   'type': 'string'}, # required field
        {'name': 'content', 'type': 'string'}, # required field
    ]
    fields.extend({'name': key, 'type': 'string', 'optional': True} for key in fieldset)

    schema = {
        'name': 'imagej-wiki',
        'fields': fields,
        'default_sorting_field': 'score',
    }
    client.collections.create(schema)
    return True


def parse_document(docroot, path):
    debug(f'Parsing {path}...')
    with open(path) as f:
        lines = f.readlines()

    if len(lines) == 0 or not lines[0].strip() == '---':
        # missing front matter indicator -- assume it's not a Jekyll document.
        return None

    for i in range(1, len(lines)):
        line = lines[i].strip()
        if line == '---':
            # conclusion of front matter; treat the rest as content
            break

    content = lines[i+1:]
    debug(f'--> Content is {len(content)} lines')
    front_matter = lines[1:i]
    doc = yaml.safe_load(''.join(front_matter))
    debug(f'--> Front matter is {len(doc)} items')

    # Coerce YAML content to strings only. Sad but necessary.
    for key in doc:
        doc[key] = str(doc[key])

    # Set required field values.
    doc['id'] = path[len(docroot):path.rindex('.')]
    doc['score'] = 100 # a constant value, at least for now
    if not 'title' in doc: doc['title'] = doc['id']
    doc['content'] = ''.join(content)

    if not 'description' in doc:
        description = first_sentence(content)
        debug(f'--> Inferred description: {description}')
        doc['description'] = description

    return doc


def load_jekyll_site(docroot):
    """
    Loads the Jekyll content from the given docroot folder.
    """
    documents = []
    for root, dirs, files in os.walk(docroot):
        for name in files:
            path = os.path.join(root, name)
            try:
                doc = parse_document(docroot, path)
                if doc: documents.append(doc)
            except:
                error(f'Failed to parse {path}:')
                traceback.print_exc()
    return documents


def update_index(client, documents):
    """
    Update the ImageJ wiki collection to match the given documents.
    """
    client.collections['imagej-wiki'].documents.import_(documents, {'action': 'upsert'})


pathname = os.path.dirname(sys.argv[0])
docroot = os.path.join(pathname, '..', '..', '_pages')
if not os.path.isdir(docroot):
    error('Cannot find the _pages directory!')
    sys.exit(1)

info('Loading content...')
documents = load_jekyll_site(docroot)
info(f'Loaded {len(documents)} documents')

client = connect()
info('Connected to typesense')
created = create(client, documents, force=True)
info('Created new collection' if created else 'Updating existing collection')
info(f'Indexing {len(documents)} documents...')
update_index(client, documents)
info('Done!')
