---
title: Editing the Wiki - Math Expressions
section: Help:Editing the Wiki
---

This page demonstrates how to include mathematical expressions.

This site supports mathematical notation using
[MathJax](https://www.mathjax.org/), so that you can write expressions with
{% include wikipedia title="LaTeX" %} syntax, either inline or as a block.

Expressions are delineated by `$$` tags before and after the expression.

## Block equation example

{% capture block-equation-code %}
{% raw %}$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}$${% endraw %}
{% endcapture %}
{% capture block-equation-result %}
$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}$$
{% endcapture %}
{% include example code=block-equation-code result=block-equation-result %}

## Inline equation example

{% capture inline-equation-code %}
{% raw %}When $$a \ne 0$$, there are two solutions
to $$(ax^2 + bx + c = 0)$$.{% endraw %}
{% endcapture %}
{% capture inline-equation-result %}
When $$a \ne 0$$ , there are two solutions to $$(ax^2 + bx + c = 0)$$.
{% endcapture %}
{% include example code=inline-equation-code result=inline-equation-result %}

## Further reading

See [this excellent guide](https://math.meta.stackexchange.com/q/5020) for a
comprehensive introduction to MathJax with lots of examples.
