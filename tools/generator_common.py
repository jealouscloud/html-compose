from collections import namedtuple
from pathlib import Path

AttrDefinition = namedtuple(
    "AttrDefinition", ["name", "safe_name", "value_desc", "description"]
)


def get_path(fn):
    if Path("tools").exists():
        return Path("tools") / fn
    else:
        return Path(fn)


def safe_name(name):
    """
    Some names are reserved in Python, so we need to add an underscore
    An underscore after was chosen so type hints match what user is looking for
    """
    # Keywords
    if name in ("class", "is", "for", "as", "async", "del"):
        name = name + "_"

    if "-" in name:
        # Fixes for 'accept-charset' etc.
        name = name.replace("-", "_")

    return name


def ReadAttr(attr_spec) -> AttrDefinition:
    name = attr_spec["Attribute"]
    safe_attr_name = safe_name(name)
    attr_desc = attr_spec["Description"]
    value_desc = attr_spec["Value"]
    return AttrDefinition(name, safe_attr_name, value_desc, attr_desc)
