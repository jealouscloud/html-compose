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
    def get(value: str) -> BaseAttribute:
        '''
        htmx attribute: hx-get
            The hx-get attribute will cause an element to issue a
            GET to the specified URL and swap the HTML into the DOM
            using a swap strategy

        :param value: URI to GET when the element is activated
        :return: An hx-get attribute to be added to your element
        '''

        return BaseAttribute("hx-get", value)

btn = button([htmx.get("/api/data")])["Click me!"]
btn.render()  # '<button hx-get="/api/data">Click me!</button>'
```

Publish your own to make someone elses development experience better!

"""

import os

from .a_element import a as a
from .abbr_element import abbr as abbr
from .address_element import address as address
from .area_element import area as area
from .article_element import article as article
from .aside_element import aside as aside
from .audio_element import audio as audio
from .b_element import b as b
from .base_element import base as base
from .bdi_element import bdi as bdi
from .bdo_element import bdo as bdo
from .blockquote_element import blockquote as blockquote
from .body_element import body as body
from .br_element import br as br
from .button_element import button as button
from .canvas_element import canvas as canvas
from .caption_element import caption as caption
from .cite_element import cite as cite
from .code_element import code as code
from .col_element import col as col
from .colgroup_element import colgroup as colgroup
from .data_element import data as data
from .datalist_element import datalist as datalist
from .dd_element import dd as dd
from .del__element import del_ as del_
from .details_element import details as details
from .dfn_element import dfn as dfn
from .dialog_element import dialog as dialog
from .div_element import div as div
from .dl_element import dl as dl
from .dt_element import dt as dt
from .em_element import em as em
from .embed_element import embed as embed
from .fieldset_element import fieldset as fieldset
from .figcaption_element import figcaption as figcaption
from .figure_element import figure as figure
from .footer_element import footer as footer
from .form_element import form as form
from .h1_element import h1 as h1
from .h2_element import h2 as h2
from .h3_element import h3 as h3
from .h4_element import h4 as h4
from .h5_element import h5 as h5
from .h6_element import h6 as h6
from .head_element import head as head
from .header_element import header as header
from .hgroup_element import hgroup as hgroup
from .hr_element import hr as hr
from .html_element import html as html
from .i_element import i as i
from .iframe_element import iframe as iframe
from .img_element import img as img
from .input_element import input as input
from .ins_element import ins as ins
from .kbd_element import kbd as kbd
from .label_element import label as label
from .legend_element import legend as legend
from .li_element import li as li
from .link_element import link as link
from .main_element import main as main
from .map_element import map as map
from .mark_element import mark as mark
from .menu_element import menu as menu
from .meta_element import meta as meta
from .meter_element import meter as meter
from .nav_element import nav as nav
from .noscript_element import noscript as noscript
from .object_element import object as object
from .ol_element import ol as ol
from .optgroup_element import optgroup as optgroup
from .option_element import option as option
from .output_element import output as output
from .p_element import p as p
from .picture_element import picture as picture
from .pre_element import pre as pre
from .progress_element import progress as progress
from .q_element import q as q
from .rp_element import rp as rp
from .rt_element import rt as rt
from .ruby_element import ruby as ruby
from .s_element import s as s
from .samp_element import samp as samp
from .script_element import script as script
from .search_element import search as search
from .section_element import section as section
from .select_element import select as select
from .slot_element import slot as slot
from .small_element import small as small
from .source_element import source as source
from .span_element import span as span
from .strong_element import strong as strong
from .style_element import style as style
from .sub_element import sub as sub
from .summary_element import summary as summary
from .sup_element import sup as sup
from .svg_element import svg as svg
from .table_element import table as table
from .tbody_element import tbody as tbody
from .td_element import td as td
from .template_element import template as template
from .textarea_element import textarea as textarea
from .tfoot_element import tfoot as tfoot
from .th_element import th as th
from .thead_element import thead as thead
from .time_element import time as time
from .title_element import title as title
from .tr_element import tr as tr
from .track_element import track as track
from .u_element import u as u
from .ul_element import ul as ul
from .var_element import var as var
from .video_element import video as video
from .wbr_element import wbr as wbr

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
