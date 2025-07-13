"""

`html-compose` is a library for natural HTML composition directly in Python.

## Quick Start Guide

For user comfort, the `[]` syntax provides a natural way to define child
elements which makes the code look more like the HTML structure it represents and
less like a list of procedures.

Behind the scenes, this is just the .base_element.BaseElement.append method.

Text is always escaped, so XSS directly in the HTML is not possible.
Via this mechanism, JavaScript within HTML attributes is always escaped.

Just don't pass user input into JavaScript attributes.

If you want to insert unsafe text, use the `unsafe_text(...)` function.

You can import elements directly from this module or .elements i.e.
* `from html_compose import a, div, span` or
* `from html_compose.elements import a, div, span` or
* `import html_compose.elements as e`

If you think HTML frame boilerplate is no fun, you can use the `HTML5Document` function
to generate a complete HTML5 document with a title, language, and body content.

It will return a string you can send directly to the client.

```python
from html_compose import HTML5Document, p, script, link

doc = HTML5Document(
    "Site Title",
    lang="en",
    head=[
            script(src="/public/bundle.js"),
            link(rel="stylesheet", href="/public/style.css"),
    ],
    body=[p["Hello, world!"]],
)
```

Custom elements can be created with `CustomElement.create` / `create_element`.

```python
from html_compose.custom_element import CustomElement
foo = CustomElement.create("foo")
foo["Hello world"].render() # <foo>Hello world</foo>

from html_compose import create_element
bar = create_element("bar")
bar()["Hello world"].render() # <bar>Hello world</bar>
```

## Type hints
Type hints are given wherever possible, so you can use your IDE to
complete element names and attributes.

Read more about these in the [elements documentation](html_compose/elements).

## Command-line Interface
An `html-compose` command-line interface is available which can be used to
convert native HTML into html-compose syntax.
This is useful when starting from a tutorial or template.

```
$ html-compose convert {filename or empty for stdin}
```

## Core Ideas
We are going to dive into the technicals and core ideas of the library.

.. include:: ../../doc/ideas/01_iterator.md
.. include:: ../../doc/ideas/02_base_element.md
.. include:: ../../doc/ideas/03_code_generator.md
.. include:: ../../doc/ideas/04_attrs.md
.. include:: ../../doc/ideas/05_livereload.md
"""

from typing import Union

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


def unsafe_text(value: Union[str, Markup]) -> Markup:
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

    return BeautifulSoup(html_str, features="html.parser").prettify(
        formatter="html5"
    )


def doctype(dtype: str = "html"):
    """
    Return doctype tag
    """
    return unsafe_text(f"<!DOCTYPE {dtype}>")


from .base_attribute import BaseAttribute
from .base_element import BaseElement
from .custom_element import CustomElement

create_element = CustomElement.create

from .document import HTML5Document

# ruff: noqa: F401, E402
from .elements import (
    a,
    abbr,
    address,
    area,
    article,
    aside,
    audio,
    b,
    base,
    bdi,
    bdo,
    blockquote,
    body,
    br,
    button,
    canvas,
    caption,
    cite,
    code,
    col,
    colgroup,
    data,
    datalist,
    dd,
    del_,
    details,
    dfn,
    dialog,
    div,
    dl,
    dt,
    em,
    embed,
    fieldset,
    figcaption,
    figure,
    footer,
    form,
    h1,
    h2,
    h3,
    h4,
    h5,
    h6,
    head,
    header,
    hgroup,
    hr,
    html,
    i,
    iframe,
    img,
    input,
    ins,
    kbd,
    label,
    legend,
    li,
    link,
    main,
    map,
    mark,
    menu,
    meta,
    meter,
    nav,
    noscript,
    object,
    ol,
    optgroup,
    option,
    output,
    p,
    picture,
    pre,
    progress,
    q,
    rp,
    rt,
    ruby,
    s,
    samp,
    script,
    search,
    section,
    select,
    slot,
    small,
    source,
    span,
    strong,
    style,
    sub,
    summary,
    sup,
    svg,
    table,
    tbody,
    td,
    template,
    textarea,
    tfoot,
    th,
    thead,
    time,
    title,
    tr,
    track,
    u,
    ul,
    var,
    video,
    wbr,
)
