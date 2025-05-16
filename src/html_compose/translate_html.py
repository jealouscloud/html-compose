import inspect
import re
from typing import Any, Optional, Union

from bs4 import BeautifulSoup, NavigableString, Tag
from bs4.element import Doctype

from . import elements as el_list
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


def translate(html: str, import_module: Optional[str] = None) -> str:
    """
    Translate HTML string into Python code representing a similar HTML structure

    We try to strip aesthetic line breaks from original HTML in this process.
    """
    soup = BeautifulSoup(html, features="html.parser")

    tags: dict[str, Any] = {}
    prefix = ""
    if import_module is not None:
        prefix = import_module + ("." if import_module else "")

    def process_element(element) -> Union[str, None]:
        if isinstance(element, Doctype):
            dt: Doctype = element
            tags["doctype"] = None
            return f"doctype({repr(dt)})"
        elif isinstance(element, NavigableString):
            return read_string(element)

        assert isinstance(element, Tag)
        safe_tag_name = safe_name(element.name)
        if safe_tag_name not in tags:
            tags[safe_tag_name] = getattr(el_list, safe_tag_name)
        tag_cls = tags[safe_tag_name]

        result = [f"{prefix}{safe_tag_name}"]
        if element.attrs:
            param_attrs = {}
            dict_attrs = {}
            tag_keys = inspect.signature(tag_cls.__init__).parameters.keys()

            for key, value in element.attrs.items():
                if key in ("attrs", "self", "children"):
                    # These are params of the constructor but the HTML given
                    # clashes with them
                    dict_attrs[key] = value
                    continue

                safe_attr_name = safe_name(key)

                if safe_attr_name in tag_keys:
                    param_attrs[safe_attr_name] = value
                else:
                    # This is an unknown attribute,
                    # let's include it as a dictionary key/value
                    dict_attrs[key] = value

            # Build element constructor call
            result.append("(")

            # Dict attributes first positionally
            if dict_attrs:
                result.append(repr(dict_attrs))

            # Matching keyword args
            if param_attrs:
                if dict_attrs:
                    result.append(", ")
                params = []
                for key, value in param_attrs.items():
                    params.append(f"{key}={repr(value)}")
                result.append(", ".join(params))

            result.append(")")
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

    if not tags:
        return "No HTML tags found"

    return "\n\n".join(
        [f"from html_compose import {', '.join(tags.keys())}"]
        + [e for e in elements if e]
    )
