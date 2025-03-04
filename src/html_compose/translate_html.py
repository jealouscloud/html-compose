import re
from typing import Union

from bs4 import (
    BeautifulSoup,
    NavigableString,
    Tag,
)
from bs4.element import Doctype

from .util_funcs import safe_name


def read_string(input_str: NavigableString) -> Union[str, None]:
    """
    Helper to sort of 'auto-translate' HTML formatted strings into what
    they would be viewed as in a browser, which can then be represented in
    Python

    Remove leading and trailing whitespace, and replace multiple spaces with a single space.

    """
    result = re.sub(r"\s+", " ", str(input_str), flags=re.MULTILINE)
    result = (
        result.lstrip()
    )  # Leading and trailing whitespace typically ignored
    if not result:
        return None
    return repr(result)


def read_pre_string(input_str: NavigableString) -> Union[str, None]:
    """
    pre elements do the same as above, but remove the first newline
    """
    result = re.sub("^\n", "", input_str)
    if not result:
        return None
    return repr(result)


def translate(html: str) -> str:
    """
    Translate HTML string into Python code representing a similar HTML structure

    We try to strip aesthetic line breaks from original HTML in this process.
    """
    soup = BeautifulSoup(html, features="html.parser")

    tags = set()

    def process_element(element) -> Union[str, None]:
        if isinstance(element, Doctype):
            dt: Doctype = element
            tags.add("doctype")
            return f"doctype({repr(dt)})"
        elif isinstance(element, NavigableString):
            return read_string(element)

        assert isinstance(element, Tag)
        safe_tag_name = safe_name(element.name)

        tags.add(safe_tag_name)
        result = [safe_tag_name]
        if element.attrs:
            result.extend(["(", repr(element.attrs), ")"])
        else:
            result.append("()")

        children: list[str] = []
        for child in element.children:
            if element.name == "pre" and isinstance(child, NavigableString):
                processed = read_pre_string(child)
                if processed:
                    children.append(processed)
            else:
                processed = process_element(child)
                if processed:
                    children.append(processed)
        if children:
            result.append("[")
            result.append(", ".join(children))
            result.append("]")
        return "".join(result)

    elements = [process_element(child) for child in soup.children]
    return "\n\n".join(
        [f"from html_compose import {', '.join(tags)}"]
        + [e for e in elements if e]
    )
