from typing import Union

from markupsafe import Markup, escape


def escape_text(value) -> Markup:
    """
    Escape unsafe text to be inserted to HTML

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


def doctype(dtype: str = "html"):
    """
    Return doctype tag
    """
    return unsafe_text(f"<!DOCTYPE {dtype}>")


def from_html():
    """
    Command-line tool to translate HTML to Python code using html_compose

    This function reads from stdin by default, but accepts an optional filename as argument
    """
    import argparse
    import fileinput

    from . import translate_html

    parser = argparse.ArgumentParser(description="HTML to Markdown translator")
    parser.add_argument(
        "html",
        default="-",
        nargs="?",
        help="HTML file to translate (default: stdin)",
    )
    args = parser.parse_args()
    is_stdin = args.html == "-"
    if is_stdin:
        print("Reading from stdin. Press Ctrl+D to finish.")

    html_content = "\n".join(
        [line for line in fileinput.input(files=args.html, encoding="utf-8")]
    )
    if is_stdin:
        print("---\n")
    print(translate_html.translate(html_content))


from .base_element import BaseElement
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
