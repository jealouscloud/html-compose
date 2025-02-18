import json

from generator_common import AttrDefinition, ReadAttr, get_path, safe_name

spec = json.loads(get_path("spec_reference.json").read_text())


def generate_attrs(attr_class, attr_list):
    attr_params = []
    attr_assignments = []
    attr_docstrings = []
    attrdefs = {}
    for attr in attr_list:
        attrdef = ReadAttr(attr)
        dupe = attrdefs.get(attrdef.name, None)
        def_dict = {
            "attr": attrdef,
            "docstring": [
                f":param {attrdef.safe_name}: {attrdef.description}",
                f"    | {attrdef.value_desc}",
            ],
        }
        if dupe:
            if "dupes" in dupe:
                dupes = dupe["dupes"] + [def_dict]
                def_dict["dupes"] = dupes
            else:
                dupes = [dupe]
                def_dict["dupes"] = dupes
        attrdefs[attrdef.name] = def_dict
    attr_list = sorted(set(x for x in attrdefs.keys()))
    for attr_name in attr_list:
        attrdef: AttrDefinition = attrdefs[attr_name]["attr"]
        attr_params.append(
            f"        {attrdef.safe_name}: Union[str, {attr_class}.{attrdef.safe_name}] = None,"
        )
        attr_assignments.append(
            f'        self._process_attr("{attrdef.name}", {attrdef.safe_name})'
        )
        attr_docstrings.append(attrdefs[attr_name]["docstring"])
        dupes = attrdefs[attr_name].get("dupes", [])
        for dupe in dupes:
            # <link> has two tile defs, but they are the same attr.
            # We provide both docstrings even though the editor won't
            # provide both on completion
            attr_docstrings.append(dupe["docstring"])
    return attr_params, attr_docstrings, attr_assignments


def gen_elements():
    result = []
    attr_imports = []
    global_attrs = spec["_global_attributes"]["spec"]
    global_attr_defs: list[AttrDefinition] = []
    for attr in global_attrs:
        global_attr_defs.append(ReadAttr(attr))
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

            if attrs != "globals":
                attr_class = f"{attr_name}Attrs"
                attr_string = f", {attr_class}"
                attr_imports.append(attr_class)
                attr_list = _spec["attributes"]
                if attr_list:
                    params, docstrings, attr_assignments = generate_attrs(
                        attr_class, attr_list
                    )
                    for docstring in docstrings:
                        attr_docstrings.extend(docstring)
                    extra_attrs = "\n".join(params)
                    attr_assignment = "\n".join(attr_assignments)
            else:
                attr_list = []
            # for attr in global_attr_defs:
            # attr_class = f"{attr}"

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
                "        dict, list[BaseAttribute]",
                "    ]",
                "",
                "",
                "    def __init__(",
                "        self,",
                "        id: GlobalAttrs.id = None,",
                "        class_: GlobalAttrs.class_ = None,",
                extra_attrs,
                "        attrs: attr_type = None,",
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

    header = f"""from typing import Any, Optional, TypeAlias, Union

from .attributes import GlobalAttrs, {", ".join(attr_imports)}
from .base_attribute import BaseAttribute
from .base_element import BaseElement

# This file is generated by tools/generate_elements.py
"""
    return header + "\n\n".join(result)


elements = gen_elements()
get_path("generated/elements.py").write_text(elements)
