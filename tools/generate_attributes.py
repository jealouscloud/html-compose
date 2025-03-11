import argparse
import json
import shutil
from pathlib import Path

from generator_common import get_path, safe_name, type_for_value


def generate_class_template(
    safe_class_name, element_name, attr_name, attr_desc, value_desc, type_data
):
    safe_class_name = safe_class_name.lower()
    if element_name == "Global Attribute":
        element_name = "global"
    template = f'''
    @staticmethod
    def {safe_class_name.lower()}(value{type_data}) -> BaseAttribute:
        """
        "{element_name}" attribute: {attr_name}  
        {attr_desc}  

        :param value: {value_desc}  
        :return: An {attr_name} attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("{attr_name}", value)
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

        element_name_for_class = element
        if element_name_for_class == "a":
            element_name_for_class = "Anchor"

        element_name_for_class = element_name_for_class.title()
        attr_class_name = f"{element_name_for_class}Attrs"

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
        doc_lines = [
            "from . import BaseAttribute",
            "from typing import Literal, Union",
            "",
            f"class {attr_class_name}:",
            '    """ ',
            f"    This module contains functions for attributes in the '{element}' element.",
            "    Which is inherited by a class so we can generate type hints",
            '    """ ',
            "    ",
        ]
        doc = "\n".join(doc_lines) + doc
        get_path(f"generated/{element}_attrs.py").write_text(doc)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate HTML attrs.")
    parser.add_argument(
        "--copy", action="store_true", help="Copy the output to project"
    )
    args = parser.parse_args()
    spec = json.loads(get_path("spec_reference.json").read_text())

    global_attrs()

    other_attrs()
    if args.copy:
        path_base = "src/html_compose/attributes"
        output_path = Path(path_base)
        if not output_path.exists():
            output_path = Path("..") / output_path
            if not output_path.exists():
                print("Error: Could not find output path to copy to")
                exit(1)
        for attrscript in get_path("generated").glob("*_attrs.py"):
            shutil.copy(attrscript, output_path)
