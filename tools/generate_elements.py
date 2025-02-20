import json
from collections import namedtuple

from generator_common import (
    AttrDefinition,
    ReadAttr,
    get_path,
    safe_name,
    value_hint_to_python_type,
)

spec = json.loads(get_path("spec_reference.json").read_text())
processed_attr = namedtuple(
    "processed_attr", ["name", "param", "assignment", "docstrings"]
)


def generate_attrs(attr_class, attr_list) -> list[processed_attr]:  # -> list:
    processed: list[processed_attr] = []
    attrdefs = {}
    for attr in attr_list:
        attrdef = ReadAttr(attr)
        dupe = attrdefs.get(attrdef.name, None)
        docstring = [f":param {attrdef.safe_name}: {attrdef.description}"]

        if not value_hint_to_python_type(attrdef.value_desc):
            docstring.append(f"    | {attrdef.value_desc}")

        def_dict = {"attr": attrdef, "docstring": docstring}
        if dupe:
            if "dupes" in dupe:
                dupes = dupe["dupes"] + [def_dict]
                def_dict["dupes"] = dupes
            else:
                dupes = [dupe]
                def_dict["dupes"] = dupes
        attrdefs[attrdef.name] = def_dict
    # sort the list
    attr_list = sorted(set(x for x in attrdefs.keys()))
    for attr_name in attr_list:
        attrdef: AttrDefinition = attrdefs[attr_name]["attr"]

        assignment = (
            f"        if not ({attrdef.safe_name} is None or {attrdef.safe_name} is False):\n"
            f'            self._process_attr("{attrdef.name}", {attrdef.safe_name})'
        )
        docstrings = attrdefs[attr_name]["docstring"]

        dupes = attrdefs[attr_name].get("dupes", [])
        param_types = ["str", f"{attr_class}.{attrdef.safe_name}"]
        param_type = value_hint_to_python_type(attrdef.value_desc)
        if param_type:
            param_types.append(param_type)
        for dupe in dupes:
            # <link> has two tile defs, but they are the same attr.
            # We provide both docstrings even though the editor won't
            # provide both on completion
            docstrings.extend(dupe["docstring"])

            # Add the param type if it's not already in the list
            param_type = value_hint_to_python_type(attrdef.value_desc)
            if param_type and param_type not in param_types:
                param_types.append(param_type)

        param = f"        {attrdef.safe_name}: Union[{', '.join(param_types)}] = None,"
        processed.append(
            processed_attr(
                name=attr_name,
                param=param,
                assignment=assignment,
                docstrings=docstrings,
            )
        )

    return processed


def gen_elements():
    result = []
    attr_imports = []
    global_attrs = spec["_global_attributes"]["spec"]
    for element in spec:
        if element in ("_global_attributes", "autonomous custom elements"):
            continue
        split_elements = element.split(", ")
        for real_element in split_elements:
            _spec = spec[element]["spec"]
            desc = _spec["Description"]
            categories = _spec["Categories"]
            parents = _spec["Parents"]
            children = _spec["Children"]
            interface = _spec["Interface"]
            attrs = _spec["Attributes"]
            docs = spec[element]["mdn"]
            if docs:
                docs = docs["mdn_url"]

            real_element: str
            if real_element == "SVG svg":
                real_element = "svg"
                attrs = "globals"  # HACK: Give us the most basic element
                # TODO: Implement SVG
                # SVG is actually so much, and probably not worth the effort.
                # https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute
                #  We can give a half definition for SVG
            elif real_element == "MathML math":
                # We aren't bothering with MathML for now
                continue

            if real_element == "a":
                attr_name = "Anchor"
            else:
                attr_name = real_element.capitalize()

            attr_string = ""
            # Everyone gets global attrs, so ignore elements
            # that only have them.
            attr_class = "GlobalAttrs"
            extra_attrs = ""
            attr_assignment = ""
            attr_docstrings = [
                ":param id: The ID of the element",
                ":param class_ The class of the element",
                ":param attrs: A list or dictionary of attributes for the element",
            ]

            attr_list = []
            assign_list = []
            attr_names = set()
            if attrs != "globals":
                attr_class = f"{attr_name}Attrs"
                attr_string = f", {attr_class}"
                attr_imports.append(attr_class)
                spec_attrs = _spec["attributes"]
                if spec_attrs:
                    processed = generate_attrs(attr_class, spec_attrs)
                    shifted = [
                        x for x in processed if not x.name.startswith("on")
                    ]
                    for p in shifted:
                        attr_docstrings.extend(p.docstrings)
                        attr_list.append(p.param)
                        assign_list.append(p.assignment)
                        attr_names.add(p.name)
                    extra_attrs = "\n".join(attr_list)
                    attr_assignment = "\n".join(assign_list)

            global_processed = generate_attrs("GlobalAttrs", global_attrs)

            global_shifted = [
                x for x in global_processed if not x.name.startswith("on")
            ]
            for p in global_shifted:
                if p.name in ("id", "class") or p.name in attr_names:
                    continue
                attr_docstrings.extend(p.docstrings)
                attr_list.append(p.param)
                assign_list.append(p.assignment)

            extra_attrs = "\n".join(attr_list)
            attr_assignment = "\n".join(assign_list)
            fixed_name = safe_name(real_element)
            is_void_element = children == "empty"
            template = [
                "",
                f"class {fixed_name}(BaseElement, GlobalAttrs{attr_string}):",
                '    """',
                f"    The <{real_element}> element.",
                f"    Description: {desc}",
                f"    Categories: {categories}",
                f"    Parents: {parents}",
                f"    Children: {children}",
                f"    Interface: {interface}",
                f"    Documentation: {docs}",
                '    """',
                "    attr_type: TypeAlias = Union[",
                f"        dict, list[BaseAttribute], list[{attr_class}]",
                "    ]",
                "",
                "",
                "    def __init__(",
                "        self,",
                "        attrs: attr_type = None,",
                "        id: GlobalAttrs.id = None,",
                "        class_: GlobalAttrs.class_ = None,",
                extra_attrs,
                "        children: list = None",
                "    ) -> None:",
                '        """',
                f"        Initialize a <{real_element}> element.",
                f"        Description: {desc}",
                f"        Documentation: {docs}",
                "",
                "        " + "\n        ".join(attr_docstrings),
                '        """',
                "        super().__init__(",
                f'            "{real_element}",',
                f"            void_element={is_void_element},",
                "            id=id,",
                "            class_=class_,",
                "            attrs=attrs,",
                "            children=children",
                "        )",
                attr_assignment,
            ]
            result.append("\n".join(template))

    header = f"""from typing import Any, Optional, TypeAlias, Union, Literal

from .attributes import GlobalAttrs, {", ".join(attr_imports)}
from .base_attribute import BaseAttribute
from .base_element import BaseElement

# This file is generated by tools/generate_elements.py
"""
    return header + "\n\n".join(result)


elements = gen_elements()
get_path("generated/elements.py").write_text(elements)
