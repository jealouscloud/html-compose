import json
from pathlib import Path


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
    if name in ("class", "is", "for", "as", "async"):
        name = name + "_"

    if "-" in name:
        # Fixes for 'accept-charset' etc.
        name = name.replace("-", "_")

    return name


def type_for_value(value):
    if isinstance(value, list):
        return f": Union[Literal{value}, Callable[[], str]]"
    if value in ("Text", "Text*"):
        return ": Union[str, Callable[[], str]]"
    if value == "Boolean attribute":
        return ": Union[bool, Callable[[], bool]]"
    return ""


def generate_class_template(
    safe_class_name, element_name, attr_name, attr_desc, value_desc, type_data
):
    template = f'''
    class {safe_class_name}(BaseAttribute):
        """
        {element_name} attribute: {attr_name}
        Description: {attr_desc}
        Value: {value_desc}
        """
        
        def __init__(self, value{type_data}):
            super().__init__("{attr_name}", value)
            '''
    return template


def global_attrs():
    result = []
    for attr in spec["_global_attributes"]["spec"]:
        attr_name = attr["Attribute"]
        safe_attr_name = safe_name(attr_name)
        attr_desc = attr["Description"]
        value_desc = attr["Value"]

        type_data = type_for_value(value_desc)

        _class = generate_class_template(
            safe_attr_name,
            "Global Attribute",
            attr_name,
            attr_desc,
            value_desc,
            type_data,
        )
        result.append(_class)

    doc = "\n\n".join(result)
    doc_lines = [
        "from . import BaseAttribute",
        "from typing import Literal, Union, Callable",
        "",
        "class GlobalAttrs:",
        '    """ ',
        "    This module contains classes for all global attributes.",
        "    Elements can inherit it so the element can be a reference to our attributes",
        '    """ ',
        "    ",
    ]
    doc = "\n".join(doc_lines) + doc
    get_path("generated/global_attrs.py").write_text(doc)


def other_attrs():
    for element in spec:
        result = []
        if element == "_global_attributes":
            continue
        attrs = spec[element]["spec"]["attributes"]
        if not attrs:
            continue

        defined_attrs = []
        for attr in attrs:
            attr_name = attr["Attribute"]
            if attr_name in defined_attrs:
                # no dupes
                continue
            safe_attr_name = safe_name(attr_name)

            dupes = list(filter(lambda x: x["Attribute"] == attr_name, attrs))
            # This case was spawned for the link element
            # and the title attr
            delim = "  OR  "
            attr_desc = delim.join(x["Description"] for x in dupes)
            value_desc = delim.join(str(x["Value"]) for x in dupes)

            type_data = type_for_value(value_desc)

            _class = generate_class_template(
                safe_attr_name,
                element,
                attr_name,
                attr_desc,
                value_desc,
                type_data,
            )
            defined_attrs.append(attr_name)
            result.append(_class)

        doc = "\n\n".join(result)

        element_name_for_class = element
        if element_name_for_class == "a":
            element_name_for_class = "Anchor"

        element_name_for_class = element_name_for_class.title()

        doc_lines = [
            "from . import BaseAttribute",
            "from typing import Literal, Union, Callable",
            "",
            f"class {element_name_for_class}Attrs:",
            '    """ ',
            f"    This module contains classes for attributes in the <{element}> element.",
            "    Which is inherited by the element so the element can be a reference to our attributes",
            '    """ ',
            "    ",
        ]
        doc = "\n".join(doc_lines) + doc
        get_path(f"generated/{element}_attrs.py").write_text(doc)


spec = json.loads(get_path("spec_reference.json").read_text())

global_attrs()

other_attrs()
