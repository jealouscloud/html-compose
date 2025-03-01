import re

from bs4 import BeautifulSoup, NavigableString, Tag
from bs4.element import Doctype

from .util_funcs import safe_name


def read_string(e: NavigableString):
    """
    Helper to sort of 'auto-translate' HTML formatted strings into what
    they would be viewed as in a browser, which can then be represented in
    Python

    Remove leading and trailing whitespace, and replace multiple spaces with a single space.

    """
    e = re.sub(r"\s+", " ", str(e), flags=re.MULTILINE)
    e = e.lstrip()  # Leading and trailing whitespace typically ignored
    if not e:
        return None
    return repr(e)


def read_pre_string(e: NavigableString):
    """
    pre elements do the same as above, but remove the first newline
    """
    e = re.sub("^\n", "", e)
    if not e:
        return None
    return repr(e)


def translate(html: str):
    """
    Translate HTML string into Python code representing a similar HTML structure

    We try to strip aesthetic line breaks from original HTML in this process.
    """
    soup = BeautifulSoup(html, features="html.parser")

    tags = set()

    def process_element(element):
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

        children = []
        for child in element.children:
            if element.name == "pre" and isinstance(child, NavigableString):
                children.append(read_pre_string(child))
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
    return "\n".join(
        [f"from html_compose import {', '.join(tags)}"]
        + [e for e in elements if e]
    )
