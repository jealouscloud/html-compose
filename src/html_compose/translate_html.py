import inspect
import re
from functools import cache
from typing import Any, Optional, Union, cast

from bs4 import BeautifulSoup, NavigableString, Tag
from bs4.element import Doctype

from . import elements as el_list
from .custom_element import CustomElement
from .util_funcs import safe_name

SPEC_WS = r"[\t\n\r ]"


@cache
def get_phrasing_tags():
    """
    Get the list of phrasing tags from the HTML spec
    """
    result = []
    for e in dir(el_list):
        val = getattr(el_list, e)
        if isinstance(val, type) and issubclass(val, el_list.BaseElement):
            if val is el_list.BaseElement:
                continue

            categories = getattr(val, "categories")
            tag = getattr(val, "tag")
            for c in categories:
                if "phrasing" in c:
                    result.append(tag)
    return result


def read_string(
    input_str: NavigableString,
    prev_tag: Optional[Tag],
    next_tag: Optional[Tag],
    phrasing_tags: list[str],
) -> Union[str, None]:
    """
    Helper to sort of 'auto-translate' HTML formatted strings into what
    they would be viewed as in a browser, which can then be represented in
    Python.

    It collapses whitespace based on the context of the surrounding tags.
    """
    text = str(input_str)

    # Trim if the previous or next tag is not an inline (phrasing) tag
    trim_left = False
    if prev_tag:
        trim_left = prev_tag.name not in phrasing_tags
    else:
        # No previous sibling, trim leading space
        trim_left = True

    trim_right = False
    if next_tag:
        trim_right = next_tag.name not in phrasing_tags
    else:
        # No next sibling, trim trailing space
        trim_right = True

    if trim_left:
        text = text.lstrip()
    if trim_right:
        text = text.rstrip()

    # Collapse multiple whitespace characters into a single space
    result = re.sub(f"{SPEC_WS}+", " ", text)

    if not result:
        return None

    # If the original string was just whitespace and it got completely removed,
    # but it was between two inline tags, we should preserve a single space.
    if not result and input_str.strip() == "":
        if (
            prev_tag
            and next_tag
            and prev_tag.name in phrasing_tags
            and next_tag.name in phrasing_tags
        ):
            return repr(" ")

    return repr(result) if result else None


# HTML spec doesn't say this casually, but these are preformatted.
WHITESPACE_PRE = ["pre", "textarea", "listing", "xmp"]


def read_pre_string(input_str: NavigableString) -> Union[str, None]:
    """
    pre elements do the same as above, but remove the first newline
    """
    result = re.sub("^\n", "", input_str)
    if not result:
        return None
    return repr(result)


class TranslateResult:
    """
    Class to hold the result of the translation
    """

    def __init__(
        self,
        elements: list[str],
        tags: dict[str, Any],
        import_statement: str = "",
        custom_elements: Optional[list[str]] = None,
    ):
        self.elements = elements
        self.tags = tags
        self.import_statement = import_statement
        self.custom_elements = custom_elements or []

    def as_array(self):
        """
        Return the elements as an array
        """
        sep = ",\n"
        return f"[\n{sep.join(self.elements)}\n]"


def is_preformatted(tag_name):
    return tag_name in {"pre", "textarea"}


def translate(
    html: str, import_module: Optional[str] = None
) -> TranslateResult:
    """
    Translate HTML string into Python code representing a similar HTML structure

    We try to strip aesthetic line breaks from original HTML in this process.
    """
    soup = BeautifulSoup(html, features="html.parser")

    tags: dict[str, Any] = {}
    prefix = ""
    if import_module is not None:
        prefix = import_module + ("." if import_module else "")

    custom_elements = set()

    phrasing_tags = get_phrasing_tags()

    def process_element(element) -> Union[str, None]:
        if isinstance(element, Doctype):
            dt: Doctype = element
            tags["doctype"] = None
            return f"doctype({repr(dt)})"
        elif isinstance(element, NavigableString):
            return read_string(element, None, None, phrasing_tags)

        assert isinstance(element, Tag)
        safe_tag_name = safe_name(element.name)
        if safe_tag_name not in tags:
            try:
                tags[safe_tag_name] = getattr(el_list, safe_tag_name)
            except AttributeError:
                # This is a custom element, let's add it to the list
                tags["CustomElement"] = None
                tags[safe_tag_name] = CustomElement.create(safe_tag_name)
                custom_elements.add(safe_tag_name)
        is_custom = safe_tag_name in custom_elements
        tag_cls = tags[safe_tag_name]

        if is_custom:
            # Custom elements aren't imported
            result = [f"{safe_tag_name}"]
        else:
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
        child_nodes = list(element.children)
        for i, child in enumerate(child_nodes):
            if element.name in WHITESPACE_PRE and isinstance(
                child, NavigableString
            ):
                processed = read_pre_string(child)
                if processed:
                    children.append(processed)
                continue

            if isinstance(child, NavigableString):
                # We step backwards until we find a tag
                prev_tag = next(
                    (
                        cast(Tag, child_nodes[j])
                        for j in range(i - 1, -1, -1)
                        if isinstance(child_nodes[j], Tag)
                    ),
                    None,
                )
                # Same deal, forwards until we find a tag
                next_tag = next(
                    (
                        cast(Tag, child_nodes[j])
                        for j in range(i + 1, len(child_nodes))
                        if isinstance(child_nodes[j], Tag)
                    ),
                    None,
                )
                processed = read_string(
                    child, prev_tag, next_tag, phrasing_tags
                )
                if processed:
                    children.append(processed)
            elif isinstance(child, Tag):
                processed = process_element(child)
                if processed:
                    children.append(processed)

        if children:
            result.append("[")
            result.append(", ".join(children))
            result.append("]")
        return "".join(result)

    elements = [process_element(child) for child in soup.children]
    import_statement = ""
    if not import_module:
        keys = [key for key in tags.keys() if key not in custom_elements]
        if len(keys) > 3:
            # Add parens
            import_statement = f"from html_compose import ({', '.join(keys)})"
        else:
            import_statement = f"from html_compose import {', '.join(keys)}"
    else:
        if import_module == "html_compose":
            import_statement = "import html_compose"
        else:
            import_statement = f"import html_compose as {import_module}"

    custom_el_stmts = [
        f'{e} = {prefix}CustomElement.create("{e}")' for e in custom_elements
    ]

    return TranslateResult(
        [e for e in elements if e], tags, import_statement, custom_el_stmts
    )
