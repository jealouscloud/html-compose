from collections import namedtuple
from pathlib import Path

from html_compose.util_funcs import safe_name

AttrDefinition = namedtuple(
    "AttrDefinition", ["name", "safe_name", "value_desc", "description"]
)


def get_path(fn):
    if Path("tools").exists():
        return Path("tools") / fn
    else:
        return Path(fn)


def ReadAttr(attr_spec) -> AttrDefinition:
    name = attr_spec["Attribute"]
    safe_attr_name = safe_name(name)
    attr_desc = attr_spec["Description"]
    value_desc = attr_spec["Value"]
    return AttrDefinition(name, safe_attr_name, value_desc, attr_desc)


def value_hint_to_python_type(value):
    if isinstance(value, list) or value.startswith("[") and value.endswith("]"):
        # Since the list looks like ["a", "b", "c"]
        # this works
        return f"Literal{value}"
    if value in ("Text", "Text*"):
        return "str"
    if value == "Boolean attribute":
        return "bool"
    if value in ("Valid non-negative integer", "Valid integer"):
        return "int"
    if value.startswith("Valid floating-point number"):
        return "float"
    if "space-separated tokens" in value:
        return "list"
    return None


def type_for_value(value):
    new_type = value_hint_to_python_type(value)
    if new_type:
        return f": {new_type}"
    return ""
