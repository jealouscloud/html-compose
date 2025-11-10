"""
# html-compose

A library for natural HTML composition directly in Python.

Focused on fast, flexible, extensible document generation,
its goal is to make the web platform fun to work with while using
modern browser technologies.

## Quick Start

All HTML elements from the [living spec](https://html.spec.whatwg.org/multipage/)
are available to use with full type hinting:

```python
from html_compose import a

element = a(href="/logout")["Log out"]
print(element.render())
# <a href="/logout">Log out</a>
```

The `[]` syntax provides a natural way to define child elements, making the code
resemble the HTML structure it represents.

Behind the scenes, this is `.base_element.BaseElement.append`, which accepts text,
elements, lists, nested lists, and callables. It returns self for chaining.

Think of it as:
* `()` sets attributes
* `[]` adds children

Set non-constructor attributes with a dict:

```python
a({"@click": "alert(1)"}, href="#")["Click me"]
```

**Security**: The children of HTML elements are always HTML escaped,
so XSS directly in the HTML is not possible.

JavaScript within HTML attribute values is always escaped.
Just don't pass user input into JavaScript attributes.

Use `.unsafe_text()` when you need unescaped content.

All HTML nodes treat their children as if they contain HTML.
This means if you have a `<script>` or `<style>` element or something
else that isn't read as HTML, you may need to handle escaping yourself before
passing to `.unsafe_text()`.

### Imports

You can import elements from this module or `html_compose.elements`:

- `from html_compose import a, div, span`
- `from html_compose.elements import a, div, span`
- `import html_compose.elements as el`

### Building Documents

Use `document_generator` for complete HTML5 documents with optimized resource management:

```python
from html_compose import p
from html_compose.document import document_generator
from html_compose.resource import js_import, css_import

# Local module with cache-busting
admin_script = js_import(
    "./static/admin.js",
    name="admin",
    cache_bust=True,
    preload=True
)

# Remote library
alpine = js_import(
    'https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js',
    defer=True
)

# CSS with integrity checking and preload
bootstrap_css = css_import(
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css",
    preload=True,
    hash="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM",
    crossorigin="anonymous"
)

doc: str = document_generator(
    title="My App",
    css=[bootstrap_css],
    js=[admin_script, alpine],
    head_extra=[],  # anything you want to add to head
    body_content=[
        p(class_="container")["Hello, world!"]
    ]
)
```

Generates HTML with correct `<link>`, `<script>`, `importmap`, and preload tags
in the optimal order.

For streaming responses, use `document_streamer` to send the `<head>` early.

### Basic Document API

If you prefer simpler boilerplate generation, `HTML5Document` returns a complete
document string:

```python
from html_compose import HTML5Document, p, script, link

doc: str = HTML5Document(
    "Site Title",
    lang="en",
    head=[
        script(src="/public/bundle.js"),
        link(rel="stylesheet", href="/public/style.css"),
    ],
    body=[p["Hello, world!"]],
)
```

### Composing Elements

The constructor for an element defines attributes, so if it has none the call
to the constructor can be skipped like the `p` and `strong` elements below:

```python
from html_compose import div, strong, a

user = "github wanderer"
content = div(class_="profile")[
    p["Welcome, ", strong[user], "!"],
    a(href="/logout")["Log out"]
]

print(content.render())
# <div class="profile"><p>Welcome, <strong>github wanderer</strong>!</p><a href="/logout">Log out</a></div>
```

## More Features

### Custom Elements

Create custom elements with `CustomElement.create` or `create_element`:

```python
from html_compose.custom_element import CustomElement

foo = CustomElement.create("foo")
foo["Hello world"].render()  # <foo>Hello world</foo>

# Or use the shorthand
from html_compose import create_element

bar = create_element("bar")
bar()["Hello world"].render()  # <bar>Hello world</bar>
```

### Type Hints

All elements and attributes are fully type-hinted for IDE support. Your editor
can complete element names and attributes.

### Flexible Attributes

Attributes support multiple input formats:

```python
img([img.hint.src("..."), {"@click": "..."}, onmouseleave="..."])
```

### Extensions

Custom attributes for frameworks can be packaged as reusable modules:

```python
from pretend_extensions import htmx
from html_compose import button, div

button([htmx.get('/url'), htmx.target('#result')])
# <button hx-get="/url" hx-target="#result"></button>
```

## Command-line Interface

Convert HTML to html-compose syntax—useful when starting from tutorials or templates:

```sh
html-compose convert {filename or empty for stdin}
html-compose convert --noimport el  # produces el.div() style references
```

`html-convert` provides access to this tool as shorthand.

# Core Ideas
We are going to dive into the technicals and core ideas of the library.

.. include:: ../../doc/ideas/01_iterator.md
.. include:: ../../doc/ideas/02_base_element.md
.. include:: ../../doc/ideas/03_code_generator.md
.. include:: ../../doc/ideas/04_attrs.md
.. include:: ../../doc/ideas/05_livereload.md
.. include:: ../../doc/ideas/06_resource_imports.md
"""

from markupsafe import Markup, escape


def escape_text(value) -> Markup:
    """
    Escape unsafe text to be inserted into HTML

    Optionally casting to string
    """
    if isinstance(value, str):
        return escape(value)
    else:
        return escape(str(value))


def unsafe_text(value: str | Markup) -> Markup:
    """
    Return input string as Markup

    If input is already markup, it needs no further casting
    """
    if isinstance(value, Markup):
        return value

    return Markup(str(value))


def pretty_print(html_str: str, features="html.parser") -> str:
    """
    Pretty print HTML.  
    DO NOT do this for production since it introduces whitespace and may
    affect your output.

    :param html_str: HTML string to print
    :param features: BeautifulSoup tree builder to print with
    :return: Pretty printed HTML string
    """  # fmt: skip
    # Production instances probably don't use this
    # so we lazy load bs4
    from bs4 import BeautifulSoup  # type: ignore[import-untyped]

    return BeautifulSoup(html_str, features=features).prettify(
        formatter="html5"
    )


def doctype(dtype: str = "html"):
    """
    Return doctype tag
    """
    return unsafe_text(f"<!DOCTYPE {dtype}>")


# The imports are organized to avoid circular dependencies
# The import x as x pattern is interpreted by some tools as "public export"

# ruff: noqa: E402

# Library primitives
from .base_attribute import BaseAttribute as BaseAttribute
from .base_element import BaseElement as BaseElement
from .custom_element import CustomElement as CustomElement

create_element = CustomElement.create
# Document features
from .document import HTML5Document as HTML5Document
from .document import document_generator as document_generator
from .document import document_streamer as document_streamer

# Elements
from .elements import a as a
from .elements import abbr as abbr
from .elements import address as address
from .elements import area as area
from .elements import article as article
from .elements import aside as aside
from .elements import audio as audio
from .elements import b as b
from .elements import base as base
from .elements import bdi as bdi
from .elements import bdo as bdo
from .elements import blockquote as blockquote
from .elements import body as body
from .elements import br as br
from .elements import button as button
from .elements import canvas as canvas
from .elements import caption as caption
from .elements import cite as cite
from .elements import code as code
from .elements import col as col
from .elements import colgroup as colgroup
from .elements import data as data
from .elements import datalist as datalist
from .elements import dd as dd
from .elements import del_ as del_
from .elements import details as details
from .elements import dfn as dfn
from .elements import dialog as dialog
from .elements import div as div
from .elements import dl as dl
from .elements import dt as dt
from .elements import em as em
from .elements import embed as embed
from .elements import fieldset as fieldset
from .elements import figcaption as figcaption
from .elements import figure as figure
from .elements import footer as footer
from .elements import form as form
from .elements import h1 as h1
from .elements import h2 as h2
from .elements import h3 as h3
from .elements import h4 as h4
from .elements import h5 as h5
from .elements import h6 as h6
from .elements import head as head
from .elements import header as header
from .elements import hgroup as hgroup
from .elements import hr as hr
from .elements import html as html
from .elements import i as i
from .elements import iframe as iframe
from .elements import img as img
from .elements import input as input
from .elements import ins as ins
from .elements import kbd as kbd
from .elements import label as label
from .elements import legend as legend
from .elements import li as li
from .elements import link as link
from .elements import main as main
from .elements import map as map
from .elements import mark as mark
from .elements import menu as menu
from .elements import meta as meta
from .elements import meter as meter
from .elements import nav as nav
from .elements import noscript as noscript
from .elements import object as object
from .elements import ol as ol
from .elements import optgroup as optgroup
from .elements import option as option
from .elements import output as output
from .elements import p as p
from .elements import picture as picture
from .elements import pre as pre
from .elements import progress as progress
from .elements import q as q
from .elements import rp as rp
from .elements import rt as rt
from .elements import ruby as ruby
from .elements import s as s
from .elements import samp as samp
from .elements import script as script
from .elements import search as search
from .elements import section as section
from .elements import select as select
from .elements import slot as slot
from .elements import small as small
from .elements import source as source
from .elements import span as span
from .elements import strong as strong
from .elements import style as style
from .elements import sub as sub
from .elements import summary as summary
from .elements import sup as sup
from .elements import svg as svg
from .elements import table as table
from .elements import tbody as tbody
from .elements import td as td
from .elements import template as template
from .elements import textarea as textarea
from .elements import tfoot as tfoot
from .elements import th as th
from .elements import thead as thead
from .elements import time as time
from .elements import title as title
from .elements import tr as tr
from .elements import track as track
from .elements import u as u
from .elements import ul as ul
from .elements import var as var
from .elements import video as video
from .elements import wbr as wbr

# Resource features
from .resource import css_import as css_import
from .resource import font_import_manual as font_import_manual
from .resource import font_import_provider as font_import_provider
from .resource import js_import as js_import
