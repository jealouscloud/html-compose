import argparse
import json
from collections import namedtuple
from pathlib import Path

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


def elements_docstring():
    """
    Generate a docstring for the elements module.
    """
    return """
This module contains HTML elements.

Each element is a class that inherits from BaseElement.

The classes are generated from the WhatWG HTML specification.
We do not generate deprecated elements.

Each class has a hint class that provides type hints for the attributes.

## Construction
#### `[]` syntax
1. There is special syntax for constructed elements which will append
  any given parameters to the elements children. Internally this is simply
  `BaseElement.append(...)`
2. There is a special syntax for _unconstructed_ elements which will create
  an element with no parameters and append the children.

Example:
```python
from html_compose import p, strong
# Internally, this is what we're doing
# e1 = p()
# e2 = strong()
# e2.append("world!")
# e1.append("Hello ", e2)

# Syntax 1.
link = a()["Hello ", strong()["world!"]]

# Syntax 2.
link = a["Hello ", strong["world!"]]
```

#### Basic usage
Most hints are available right in the constructor signature.

This was done because it makes the constructor hint too heavy.

```python
from html_compose import a

link = a(href="https://example.com", target="_blank")["Click here"]
link.render()  # '<a href="https://example.com" target="_blank">Click here</a>'
```
#### Attributes that aren't in the constructor signature
**Note that events like .onclick are _not_ available in the constructor.**

We do however provide the type hint via `<element>.hint`

The first positional argument is `attrs=` which can be a list of attributes.
We generate many of these for type hints under `<element>.hint or `<element>._`

```python
# attrs can also be a list of BaseAttribute objects
link = a([a.hint.onclick("alert(1)")],
         href="https://example.com", target="_blank")["Click here"]
```

#### With attributes that aren't built-in
The first positional argument is `attrs=` which can also be a dictionary.

```python
from html_compose import a
# You can simply define any attribute in the attrs dict
link = a({"href": "https://example.com",
          "target": "_blank"})["Click here"]
link.render()  # '<a href="https://example.com" target="_blank">Click here</a>'

# attrs can also be a list of BaseAttribute objects
link = a([a.hint.onclick("alert(1)")],
         href="https://example.com", target="_blank")["Click here"]
```
#### Framework Attributes
Some attributes are not part of the HTML specification, but are
commonly used in web frameworks. You can make your own hint class to wrap these

```python
from html_compose.base_attribute import BaseAttribute
from html_compose import button
class htmx:
    '''
    Attributes for the HTMX framework.
    '''

    @staticmethod
    def hx_get(value: str) -> BaseAttribute:
        '''
        htmx attribute: hx-get
            The hx-get attribute will cause an element to issue a
            GET to the specified URL and swap the HTML into the DOM
            using a swap strategy

        :param value: URI to GET when the element is activated
        :return: An hx-get attribute to be added to your element
        '''

        return BaseAttribute("hx-get", value)

btn = button([htmx.hx_get("/api/data")])["Click me!"]
btn.render()  # '<button hx-get="/api/data">Click me!</button>'
```

Publish your own to make someone elses development experience better!
"""


def generate_attrs(attr_class, attr_list) -> list[processed_attr]:  # -> list:
    processed: list[processed_attr] = []
    attrdefs = {}
    for attr in attr_list:
        attrdef = ReadAttr(attr)
        dupe = attrdefs.get(attrdef.name, None)
        docstring = [f"`{attrdef.safe_name}` :"]

        docstring.append(f"    {attrdef.description}")
        if not value_hint_to_python_type(attrdef.value_desc):
            docstring[-1] += "  "  # markdown newline
            docstring.append(f"    {attrdef.value_desc}")

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
        param_types = []
        param_type = value_hint_to_python_type(attrdef.value_desc)
        if param_type and param_type not in param_types:
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
        # Even if we're specific, we should generate
        # StrLike as a fallback
        if "StrLike" not in param_types:
            param_types.append("StrLike")
        # Hardcode override for class and style, which uniquely are intended
        # for multiple types
        if attrdef.name in ("class", "style"):
            param_types = ["Resolvable"]

        p_type = f"{' | '.join(param_types)}"
        if len(param_types) == 1:
            p_type = param_types[0]
        param = f"        {attrdef.safe_name}: {p_type} | None = None,"
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
                "`attrs`: ",
                "    A list or dictionary of attributes for the element",
                "",
            ]

            attr_list = []
            assign_list = []
            attr_names = set()
            global_processed = generate_attrs("GlobalAttrs", global_attrs)

            def add_param(p):
                if p.name in attr_names:
                    return
                attr_docstrings.extend(p.docstrings + [""])
                attr_list.append(p.param)
                assign_list.append(p.assignment)
                attr_names.add(p.name)

            # Prefer id and class as first args
            for p in sorted(
                [x for x in global_processed if x.name in ("id", "class")],
                key=lambda x: x.name,
                reverse=True,
            ):
                add_param(p)

            if attrs != "globals":
                attr_class = f"{attr_name}Attrs"
                attr_string = f", {attr_class}"
                attr_imports.append(attr_class)
                spec_attrs = _spec["attributes"]
                if spec_attrs:
                    processed = generate_attrs(attr_class, spec_attrs)
                    shifted = [x for x in processed]
                    for p in shifted:
                        add_param(p)
                    extra_attrs = "\n".join(attr_list)
                    attr_assignment = "\n".join(assign_list)

            global_shifted = [
                x for x in global_processed if x.name not in ("id", "class")
            ]
            for p in global_shifted:
                add_param(p)

            extra_attrs = "\n".join(attr_list)
            attr_assignment = "\n".join(assign_list)
            fixed_name = safe_name(real_element)
            is_void_element = children == "empty"
            comment = ""
            if real_element in ("link", "input", "style"):
                # Duplicate "title" definition
                comment = " # type: ignore[misc]"
            categories_list = categories.split()
            template = [
                "",
                f"class {fixed_name}(BaseElement):{comment}",
                '    """',
                f"    The '{real_element}' element.  ",
                f"    Description: {desc}  ",
                f"    Categories: {categories}  ",
                f"    Parents: {parents}  ",
                f"    Children: {children}  ",
                f"    Interface: {interface}  ",
                f"    Documentation: {docs}  ",
                '    """ # fmt: skip',
                f"    tag = {repr(real_element)}",
                f"    categories = {repr(categories_list)}",
                f"    class hint(GlobalAttrs{attr_string}):",
                '        """',
                f'        Type hints for "{real_element}" attrs  ',
                "        This class holds functions which return BaseAttributes  ",
                "        Which you can add to your element attrs  ",
                '        """ # fmt: skip',
                "        pass",
                "    _ = hint",
                "    def __init__(",
                "        self,",
                "        attrs: Iterable[BaseAttribute] | "
                "Mapping[str, Resolvable] | "
                "Iterable[BaseAttribute | Iterable[BaseAttribute] | Mapping[str,Resolvable]] | None = None,",
                extra_attrs,
                "        children: Optional[list] = None",
                "    ) -> None:",
                '        """',
                f"        Initialize '{real_element}' ({desc}) element.  ",
                f"        Documentation: {docs}",
                "",
                "        Parameters",
                "        ----------",
                "        " + "\n        ".join(attr_docstrings),
                '        """ #fmt: skip',
                "        super().__init__(",
                f'            "{real_element}",',
                f"            void_element={is_void_element},",
                "            attrs=attrs,",
                "            children=children",
                "        )",
                attr_assignment,
            ]
            result.append((fixed_name, "\n".join(template)))

    header = f"""from typing import Union, Literal, Optional, Iterable, Mapping

from ..attributes import GlobalAttrs, {", ".join(attr_imports)}
from ..base_attribute import BaseAttribute
from ..base_element import BaseElement
from ..base_types import Resolvable, StrLike

# This file is generated by tools/generate_elements.py
"""
    return header, result  # header + "\n\n".join(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate HTML elements.")
    parser.add_argument(
        "--copy",
        action="store_true",
        help="Copy the output to a hardcoded path",
    )
    args = parser.parse_args()

    header, element_list = gen_elements()
    el_names = [name for name, _ in element_list]
    for name, element in element_list:
        default_output_path = get_path(f"generated/elements/{name}_element.py")
        default_output_path.write_text(f"{header}\n\n{element}")

    el_dir = get_path("generated/elements")
    print(f"Generated elements written to: {el_dir}")
    if args.copy:
        path_name = "./src/html_compose/elements/"
        real_path = Path(path_name)
        if not real_path.exists():
            real_path = Path("..") / path_name
            if not real_path.exists():
                raise FileNotFoundError(f"Unable to find {path_name}")
        for element in el_dir.glob("*.py"):
            data = element.read_text()

            path = Path(path_name) / element.name
            path.write_text(data)
        print(f"Copied generated elements to: {real_path}")
        init_data = [f'"""{elements_docstring()}\n"""']
        for name in el_names:
            init_data.append(f"from .{name}_element import {name}")

        imports = ", ".join(map(lambda x: f"'{x}'", el_names))
        init_data.append(
            "\n".join(
                [
                    "",
                    "import os",
                    "# hack: force PDOC to treat elements as submodules",
                    'if not os.environ.get("PDOC_GENERATING", False):',
                    f"    __all__ = [{imports}]",
                ]
            )
        )

        (Path(path_name) / "__init__.py").write_text("\n".join(init_data))
