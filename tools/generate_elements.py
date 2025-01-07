import json
from pathlib import Path


def get_path(fn):
    if Path("tools").exists():
        return Path("tools") / fn
    else:
        return Path(fn)


spec = json.loads(get_path("spec_reference.json").read_text())


def gen_elements():
    result = []
    for element in spec:
        if element in ("_global_attributes", "autonomous custom elements"):
            continue
        split_elements = element.split(", ")
        for real_element in split_elements:
            real_element: str
            if real_element == "SVG svg":
                real_element = "svg"
                #  We can give a half definition for SVG
            elif real_element == "MathML math":
                # We aren't bothering with MathML for now
                continue
            if real_element == "a":
                attr_name = "Anchor"
            else:
                attr_name = real_element.capitalize()

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

            attr_string = ""
            # Everyone gets global attrs, so ignore elements
            # that only have them
            if attrs != "globals":
                attr_string = f", {attr_name}Attrs"
            fixed_name = real_element
            if real_element == "del":
                fixed_name = "del_"

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
                "        attrs: attr_type = None,",
                "        data: Optional[Any] = None,",
                "    ) -> None:",
                "        super().__init__(",
                f'            "{real_element}",',
                "            void_element=True,",
                "            id=id,",
                "            class_=class_,",
                "            attrs=attrs,",
                "            data=data,",
                "        )",
            ]
            result.append("\n".join(template))
    return result


elements = "\n\n".join(gen_elements())
print(elements)
get_path("generated/elements.py").write_text(elements)
