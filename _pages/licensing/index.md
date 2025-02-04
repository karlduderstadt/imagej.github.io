---
title: Licensing
section: About:Licensing
---

{% include info-box content='This page describes the *legal* structure of [SciJava](SciJava) projects.

-   For information on their *technical* structure, see [Architecture](/develop/architecture).
-   For information on their *social* structure, see [Governance](/about/governance).' %}


The [ImageJ](/about) project, and related projects in the [SciJava](SciJava) component collection, are licensed as [open source](Open_source) software (OSS) projects.

For an introduction to OSS licensing, see [http://choosealicense.com/](http://choosealicense.com/).

The table below summarizes the dominant license of each project's components.

## Exceptions

Since each project consists of many components, some may be licensed differently. You can always find the license of each project in a `LICENSE.txt` or similar file of the relevant repository on [GitHub](/develop/github). That said, in general, the table below is accurate with very few exceptions. When there *is* an exception, it is often licensed more permissively than the rest of the project—for example, the core of [Bio-Formats](/formats/bio-formats) is licensed under [BSD-2](/licensing/bsd) ([1](https://github.com/openmicroscopy/bioformats/blob/develop/components/formats-bsd/LICENSE.txt)), and the [ImageJ](/about) and [SCIFIO](/libs/scifio) tutorials are licensed under [CC0](/licensing/public-domain) ([1](https://github.com/imagej/tutorials/blob/master/README.md), [2](https://github.com/scifio/scifio-tutorials/blob/master/README.md)), waiving all copyright interest as allowed by law.

## Project summary

{::nomarkdown}
<table>
  <tbody>
    <tr class="odd">
      <td style="background-color: white">
        <p><strong>Basics</strong></p>
      </td>
      <td></td>
      <td></td>
      <td></td>
      <td>
        <p><strong>Required*</strong></p>
      </td>
      <td></td>
      <td></td>
      <td>
        <p><strong>Permitted*</strong></p>
      </td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr class="even">
      <td>
        <p><strong>Logo</strong></p>
      </td>
      <td style="background-color: white">
        <p><strong>Project</strong></p>
      </td>
      <td style="background-color: white">
        <p><strong>License</strong></p>
      </td>
      <td style="background-color: white">
        <p><strong>Type</strong></p>
      </td>
      <td style="vertical-align: middle">
        <p><a href="|alt=Disclose%20source"><img src="/media/licensing-disclose-source.png" width="10px"></a></p>
      </td>
      <td>
        <p><a href="|alt=License%20and%20copyright%20notice"><img src="/media/licensing-license-and-copyright-notice.png" width="22px"></a></p>
      </td>
      <td>
        <p><a href="|alt=State%20changes"><img src="/media/licensing-state-changes.png" width="10px"></a></p>
      </td>
      <td>
        <p><a href="|alt=Commercial%20use"><img src="/media/licensing-commercial-use.png" width="10px"></a></p>
      </td>
      <td>
        <p><a href="|alt=Distribution"><img src="/media/licensing-distribution.png" width="10px"></a></p>
      </td>
      <td>
        <p><a href="|alt=Modification"><img src="/media/licensing-modification.png" width="10px"></a></p>
      </td>
      <td>
        <p><a href="|alt=Patent%20grant"><img src="/media/licensing-patent-grant.png" width="10px"></a></p>
      </td>
      <td>
        <p><a href="|alt=Private%20use"><img src="/media/licensing-private-use.png" width="10px"></a></p>
      </td>
      <td>
        <p><a href="|alt=Hold%20liable"><img src="/media/licensing-hold-liable.png" width="10px"></a></p>
      </td>
      <td>
        <p><a href="|alt=Sublicensing"><img src="/media/licensing-sublicensing.png" width="10px"></a></p>
      </td>
    </tr>
    <tr class="odd">
      <td>
        <p><a href="/software/imagej1">ImageJ 1.x</a></p>
      </td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr class="even">
      <td>
        <p><img src="/media/imagej1-icon.png" width="48"></p>
      </td>
      <td>
        <p><strong><a href="/software/imagej1">ImageJ1</a></strong></p>
      </td>
      <td>
        <p><a href="/ij/disclaimer.html">Disclaimer</a></p>
      </td>
      <td>
        <p><a href="/licensing/public-domain">Public</a><br>
        <a href="/licensing/public-domain">Domain</a><sup>†</sup></p>
      </td>
      <td>
        <p>❌</p>
      </td>
      <td>
        <p>❌</p>
      </td>
      <td>
        <p>❌</p>
      </td>
      <td>
        <p>✅</p>
      </td>
      <td>
        <p>✅</p>
      </td>
      <td>
        <p>✅</p>
      </td>
      <td>
        <p>-</p>
      </td>
      <td>
        <p>✅</p>
      </td>
      <td>
        <p>❌</p>
      </td>
      <td>
        <p>✅</p>
      </td>
    </tr>
    <tr class="odd">
      <td>
        <p><a href="/develop/architecture">ImageJ software stack</a></p>
      </td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr class="even">
      <td>
        <p><img src="/media/scijava-icon.png" width="48"></p>
      </td>
      <td>
        <p><strong><a href="SciJava">SciJava</a></strong></p>
      </td>
      <td>
        <p><a href="https://github.com/scijava/scijava-common/blob/master/LICENSE.txt">License</a></p>
      </td>
      <td>
        <p><a href="/licensing/bsd">BSD-2</a></p>
      </td>
      <td rowspan="4" class="yesno">
        <p>❌</p>
      </td>
      <td rowspan="4" class="yesno">
        <p>✅</p>
      </td>
      <td rowspan="4" class="yesno">
        <p>❌</p>
      </td>
      <td rowspan="4" class="yesno">
        <p>✅</p>
      </td>
      <td rowspan="4" class="yesno">
        <p>✅</p>
      </td>
      <td rowspan="4" class="yesno">
        <p>✅</p>
      </td>
      <td>
        <p>-</p>
      </td>
      <td rowspan="4" class="yesno">
        <p>✅</p>
      </td>
      <td rowspan="4" class="yesno">
        <p>❌</p>
      </td>
      <td>
        <p>-</p>
      </td>
    </tr>
    <tr class="odd">
      <td>
        <p><img src="/media/imglib2-icon.png" width="48"></p>
      </td>
      <td>
        <p><strong><a href="/libs/imglib2">ImgLib2</a></strong></p>
      </td>
      <td>
        <p><a href="https://github.com/imglib/imglib2/blob/master/LICENSE.txt">License</a></p>
      </td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr class="even">
      <td>
        <p><img src="/media/imagej2-icon.png" width="48"></p>
      </td>
      <td>
        <p><strong><a href="/software/imagej2">ImageJ2</a></strong></p>
      </td>
      <td>
        <p><a href="https://github.com/imagej/imagej/blob/master/LICENSE.txt">License</a></p>
      </td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr class="odd">
      <td>
        <p><img src="/media/scifio-icon.png" width="48"></p>
      </td>
      <td>
        <p><strong><a href="/libs/scifio">SCIFIO</a></strong></p>
      </td>
      <td>
        <p><a href="https://github.com/scifio/scifio/blob/master/LICENSE.txt">License</a></p>
      </td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr class="even">
      <td>
        <p><a href="/software/fiji">Fiji projects</a></p>
      </td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr class="odd">
      <td>
        <p><img src="/media/fiji-icon.png" width="48"></p>
      </td>
      <td>
        <p><strong><a href="/software/fiji">Fiji</a></strong></p>
      </td>
      <td>
        <p><a href="https://github.com/fiji/fiji/blob/master/LICENSES">Licenses</a></p>
      </td>
      <td>
        <p><a href="/licensing/gpl">GPL</a></p>
      </td>
      <td rowspan="3" class="yesno">
        <p>✅</p>
      </td>
      <td rowspan="3" class="yesno">
        <p>✅</p>
      </td>
      <td rowspan="3" class="yesno">
        <p>✅</p>
      </td>
      <td rowspan="3" class="yesno">
        <p>✅</p>
      </td>
      <td rowspan="3" class="yesno">
        <p>✅</p>
      </td>
      <td rowspan="3" class="yesno">
        <p>✅</p>
      </td>
      <td rowspan="3" class="yesno">
        <p>✅</p>
      </td>
      <td rowspan="3" class="yesno">
        <p>✅</p>
      </td>
      <td rowspan="3" class="yesno">
        <p>❌</p>
      </td>
      <td rowspan="3" class="yesno">
        <p>❌</p>
      </td>
    </tr>
    <tr class="even">
      <td>
        <p><strong><a href="/plugins/bdv">BigDataViewer</a></strong></p>
      </td>
      <td></td>
      <td>
        <p><a href="https://github.com/bigdataviewer/bigdataviewer-core/blob/master/LICENSE.txt">License</a></p>
      </td>
      <td></td>
      <td></td>
    </tr>
    <tr class="odd">
      <td>
        <p><strong><a href="/plugins/trakem2">TrakEM2</a></strong></p>
      </td>
      <td>
        <p><a href="https://github.com/trakem2/plugins/trakem2/blob/master/README">Readme</a></p>
      </td>
      <td></td>
      <td></td>
    </tr>
    <tr class="even">
      <td>
        <p><a href="SciJava">SciJava consortium</a></p>
      </td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr class="odd">
      <td>
        <p><img src="/media/cellprofiler-icon.png" width="48"></p>
      </td>
      <td>
        <p><strong><a href="/software/cellprofiler">CellProfiler</a></strong></p>
      </td>
      <td>
        <p><a href="https://github.com/CellProfiler/CellProfiler/blob/master/LICENSE">License</a></p>
      </td>
      <td>
        <p><a href="/licensing/bsd">BSD-3</a></p>
      </td>
      <td rowspan="1" class="yesno">
        <p>❌</p>
      </td>
      <td rowspan="1" class="yesno">
        <p>✅</p>
      </td>
      <td rowspan="1" class="yesno">
        <p>❌</p>
      </td>
      <td rowspan="1" class="yesno">
        <p>✅</p>
      </td>
      <td rowspan="1" class="yesno">
        <p>✅</p>
      </td>
      <td rowspan="1" class="yesno">
        <p>✅</p>
      </td>
      <td>
        <p>-</p>
      </td>
      <td rowspan="1" class="yesno">
        <p>✅</p>
      </td>
      <td rowspan="1" class="yesno">
        <p>❌</p>
      </td>
      <td>
        <p>-</p>
      </td>
    </tr>
    <tr class="even">
      <td>
        <p><img src="/media/bio-formats-icon.png" width="48"></p>
      </td>
      <td>
        <p><strong><a href="/formats/bio-formats">Bio-Formats</a></strong></p>
      </td>
      <td>
        <p><a href="https://github.com/openmicroscopy/bioformats/blob/develop/LICENSE.txt">License</a><br>
        <a href="http://openmicroscopy.org/site/about/licensing-attribution">Info</a></p>
      </td>
      <td>
        <p><a href="/licensing/gpl">GPL</a></p>
      </td>
      <td rowspan="3" class="yesno">
        <p>✅</p>
      </td>
      <td rowspan="3" class="yesno">
        <p>✅</p>
      </td>
      <td rowspan="3" class="yesno">
        <p>✅</p>
      </td>
      <td rowspan="3" class="yesno">
        <p>✅</p>
      </td>
      <td rowspan="3" class="yesno">
        <p>✅</p>
      </td>
      <td rowspan="3" class="yesno">
        <p>✅</p>
      </td>
      <td rowspan="3" class="yesno">
        <p>✅</p>
      </td>
      <td rowspan="3" class="yesno">
        <p>✅</p>
      </td>
      <td rowspan="3" class="yesno">
        <p>❌</p>
      </td>
      <td rowspan="3" class="yesno">
        <p>❌</p>
      </td>
    </tr>
    <tr class="odd">
      <td>
        <p><img src="/media/omero-icon.png" width="48"></p>
      </td>
      <td>
        <p><strong><a href="/software/omero">OMERO</a></strong></p>
      </td>
      <td>
        <p><a href="https://github.com/openmicroscopy/openmicroscopy/blob/develop/LICENSE.txt">License</a><br>
        <a href="http://openmicroscopy.org/site/about/licensing-attribution">Info</a></p>
      </td>
    </tr>
    <tr class="even">
      <td>
        <p><img src="/media/knime-icon.png" width="48"></p>
      </td>
      <td>
        <p><strong><a href="/software/knime">KNIME</a></strong></p>
      </td>
      <td>
        <p><a href="http://www.knime.org/downloads/full-license">License</a></p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

<span>\*</span> See [choosealicense.com](http://choosealicense.com/) for details.  
<sup>†</sup> See note below for details.

## A note about ImageJ1

The [ImageJ 1.x](/software/imagej1) project is developed at the National Institutes of Health, a United States government organization. Hence, pursuant to [U.S. copyright law Title 17, Section 105](http://www.copyright.gov/title17/92chap1.html#105), no copyright applies. However, that waiver of copyright applies only to U.S. law, and does not apply to other countries. Furthermore, the ImageJ1 project includes substantial effort and code from individuals who are not U.S. government employees, making the legal status of ImageJ1 as a whole decidedly unclear. For further reading, see the {% include wikipedia title='Copyright status of work by the U.S. government' text='Wikipedia article "Copyright status of work by the U.S. government"'%}.

## Developers: How to use this page

If you will be creating and/or consuming open source code, you should familiarize yourself with the options for [managing copyright information](http://softwarefreedom.org/resources/2012/ManagingCopyrightInformation.html). There are numerous tools for assisting in license management; in ImageJ projects, for example, the [license-maven-plugin](https://www.mojohaus.org/license-maven-plugin/) is used to maintain file-scope copyright notices.

### Linking to these libraries

If you are writing code (open source or not) that will use one or more of these libraries, you should first familiarize yourself with the type of license(s) used by your library(ies) of interest to determine the compatibility with the licensing of your own project. Then follow the corresponding *License text* column entry links to the actual document (if any) that needs to be distributed with your code.

### Applying these licenses

If you are writing open source code and aren't sure how to license it, you can use this page to get a feel for how other ImageJ software layers are licensed, and thus what might be appropriate for your project. You can follow [general tutorials](http://opensource.org/faq#apply-license) on applying open source licenses, or use the fantastic [choosealicense.com](http://choosealicense.com/licenses/) to guide your choice (which also includes *How to apply this license* instructions for each license).
