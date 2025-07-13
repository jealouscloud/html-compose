"""
This module contains HTML elements.

Each element is a class that inherits from BaseElement.

The classes are generated from the WhatWG HTML specification.
We do not generate deprecated elements.

Each class has a hint class that provides type hints for the attributes.

## Construction
#### `[]` syntax
1. There is special syntax for constructed elements which will append
  any given parameters to the elements children. Internally this is simply
  `BaseElement.append(...)`
2. There is a special syntax for _unconstructed_ elements which will create
  an element with no parameters and append the children.

Example:
```python
from html_compose import p, strong
# Internally, this is what we're doing
# e1 = p()
# e2 = strong()
# e2.append("world!")
# e1.append("Hello ", e2)

# Syntax 1.
link = a()["Hello ", strong()["world!"]]

# Syntax 2.
link = a["Hello ", strong["world!"]]
```

#### Basic usage
Most hints are available right in the constructor signature.

This was done because it makes the constructor hint too heavy.

```python
from html_compose import a

link = a(href="https://example.com", target="_blank")["Click here"]
link.render()  # '<a href="https://example.com" target="_blank">Click here</a>'
```
#### Attributes that aren't in the constructor signature
**Note that events like .onclick are _not_ available in the constructor.**

We do however provide the type hint via `<element>.hint`

The first positional argument is `attrs=` which can be a list of attributes.
We generate many of these for type hints under `<element>.hint or `<element>._`

```python
# attrs can also be a list of BaseAttribute objects
link = a([a.hint.onclick("alert(1)")],
         href="https://example.com", target="_blank")["Click here"]
```

#### With attributes that aren't built-in
The first positional argument is `attrs=` which can also be a dictionary.

```python
from html_compose import a
# You can simply define any attribute in the attrs dict
link = a({"href": "https://example.com",
          "target": "_blank"})["Click here"]
link.render()  # '<a href="https://example.com" target="_blank">Click here</a>'

# attrs can also be a list of BaseAttribute objects
link = a([a.hint.onclick("alert(1)")],
         href="https://example.com", target="_blank")["Click here"]
```
#### Framework Attributes
Some attributes are not part of the HTML specification, but are
commonly used in web frameworks. You can make your own hint class to wrap these

```python
from html_compose.base_attribute import BaseAttribute
from html_compose import button
class htmx:
    '''
    Attributes for the HTMX framework.
    '''

    @staticmethod
    def hx_get(value: str) -> BaseAttribute:
        '''
        htmx attribute: hx-get
            The hx-get attribute will cause an element to issue a
            GET to the specified URL and swap the HTML into the DOM
            using a swap strategy

        :param value: URI to GET when the element is activated
        :return: An hx-get attribute to be added to your element
        '''

        return BaseAttribute("hx-get", value)

btn = button([htmx.hx_get("/api/data")])["Click me!"]
btn.render()  # '<button hx-get="/api/data">Click me!</button>'
```

Publish your own to make someone elses development experience better!

"""

from .a_element import a
from .abbr_element import abbr
from .address_element import address
from .area_element import area
from .article_element import article
from .aside_element import aside
from .audio_element import audio
from .b_element import b
from .base_element import base
from .bdi_element import bdi
from .bdo_element import bdo
from .blockquote_element import blockquote
from .body_element import body
from .br_element import br
from .button_element import button
from .canvas_element import canvas
from .caption_element import caption
from .cite_element import cite
from .code_element import code
from .col_element import col
from .colgroup_element import colgroup
from .data_element import data
from .datalist_element import datalist
from .dd_element import dd
from .del__element import del_
from .details_element import details
from .dfn_element import dfn
from .dialog_element import dialog
from .div_element import div
from .dl_element import dl
from .dt_element import dt
from .em_element import em
from .embed_element import embed
from .fieldset_element import fieldset
from .figcaption_element import figcaption
from .figure_element import figure
from .footer_element import footer
from .form_element import form
from .h1_element import h1
from .h2_element import h2
from .h3_element import h3
from .h4_element import h4
from .h5_element import h5
from .h6_element import h6
from .head_element import head
from .header_element import header
from .hgroup_element import hgroup
from .hr_element import hr
from .html_element import html
from .i_element import i
from .iframe_element import iframe
from .img_element import img
from .input_element import input
from .ins_element import ins
from .kbd_element import kbd
from .label_element import label
from .legend_element import legend
from .li_element import li
from .link_element import link
from .main_element import main
from .map_element import map
from .mark_element import mark
from .menu_element import menu
from .meta_element import meta
from .meter_element import meter
from .nav_element import nav
from .noscript_element import noscript
from .object_element import object
from .ol_element import ol
from .optgroup_element import optgroup
from .option_element import option
from .output_element import output
from .p_element import p
from .picture_element import picture
from .pre_element import pre
from .progress_element import progress
from .q_element import q
from .rp_element import rp
from .rt_element import rt
from .ruby_element import ruby
from .s_element import s
from .samp_element import samp
from .script_element import script
from .search_element import search
from .section_element import section
from .select_element import select
from .slot_element import slot
from .small_element import small
from .source_element import source
from .span_element import span
from .strong_element import strong
from .style_element import style
from .sub_element import sub
from .summary_element import summary
from .sup_element import sup
from .svg_element import svg
from .table_element import table
from .tbody_element import tbody
from .td_element import td
from .template_element import template
from .textarea_element import textarea
from .tfoot_element import tfoot
from .th_element import th
from .thead_element import thead
from .time_element import time
from .title_element import title
from .tr_element import tr
from .track_element import track
from .u_element import u
from .ul_element import ul
from .var_element import var
from .video_element import video
from .wbr_element import wbr

import os

# hack: force PDOC to treat elements as submodules
if not os.environ.get("PDOC_GENERATING", False):
    __all__ = [
        "a",
        "abbr",
        "address",
        "area",
        "article",
        "aside",
        "audio",
        "b",
        "base",
        "bdi",
        "bdo",
        "blockquote",
        "body",
        "br",
        "button",
        "canvas",
        "caption",
        "cite",
        "code",
        "col",
        "colgroup",
        "data",
        "datalist",
        "dd",
        "del_",
        "details",
        "dfn",
        "dialog",
        "div",
        "dl",
        "dt",
        "em",
        "embed",
        "fieldset",
        "figcaption",
        "figure",
        "footer",
        "form",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "head",
        "header",
        "hgroup",
        "hr",
        "html",
        "i",
        "iframe",
        "img",
        "input",
        "ins",
        "kbd",
        "label",
        "legend",
        "li",
        "link",
        "main",
        "map",
        "mark",
        "menu",
        "meta",
        "meter",
        "nav",
        "noscript",
        "object",
        "ol",
        "optgroup",
        "option",
        "output",
        "p",
        "picture",
        "pre",
        "progress",
        "q",
        "rp",
        "rt",
        "ruby",
        "s",
        "samp",
        "script",
        "search",
        "section",
        "select",
        "slot",
        "small",
        "source",
        "span",
        "strong",
        "style",
        "sub",
        "summary",
        "sup",
        "svg",
        "table",
        "tbody",
        "td",
        "template",
        "textarea",
        "tfoot",
        "th",
        "thead",
        "time",
        "title",
        "tr",
        "track",
        "u",
        "ul",
        "var",
        "video",
        "wbr",
    ]
