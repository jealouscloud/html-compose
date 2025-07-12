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
