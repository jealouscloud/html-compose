"""
Generate machine readable HTML SPEC from MDN and w3c spec document
"""

import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path

import hext
import requests

SPECS_BASE = (
    "https://raw.githubusercontent.com/mdn/browser-compat-data/refs/heads/main/"
)
SPECS_INDEX = "https://w3c.github.io/mdn-spec-links/html.json"

WHATWG_STANDARD = "https://html.spec.whatwg.org/"

index_fn = "reference/html-index.json"


@dataclass
class Compat:
    experimental: bool
    standard_track: bool
    deprecated: bool
    support: dict


@dataclass
class Attribute:
    name: str
    summary: str = None
    type: str = "str"
    compatibility: Compat = None
    subattrs: list = field(default_factory=list)


@dataclass
class Element:
    name: str
    summary: str = None
    engines: list[str] = field(default_factory=list)
    mdn_url: str = None
    attributes: list[Attribute] = field(default_factory=list)


def get_path(fn):
    if Path("tools").exists():
        return Path("tools") / fn
    else:
        return Path(fn)


def fetch_or_retrieve(url, fn):
    spec_path = get_path(fn)
    if spec_path.exists():
        spec_doc = spec_path.read_text()
    else:
        spec_data = requests.get(url)
        assert spec_data.status_code == 200, "Failed to fetch the spec"
        spec_path.parent.mkdir(parents=True, exist_ok=True)
        spec_path.write_text(spec_data.text)
        spec_doc = spec_data.text

    return spec_doc


class Hextract:
    def parse_table(columns, column_data):
        index = 0
        items = []
        while True:
            element = {}
            for i in range(len(columns)):
                col_name = columns[i]
                col_value = column_data[index]
                element[col_name] = col_value
                index += 1
            items.append(element)
            if index >= len(column_data):
                break
        return items

    def parse_element_table(html):
        """
        Return all elements in format
        {
            "tr": {
            "Element": "tr",
            "Description": "Table row",
            "Categories": "none",
            "Parents": "table thead tbody tfoot",
            "Children": "th* td script-supporting elements",
            "Attributes": "globals",
            "Interface": "HTMLTableRowElement"
            },
        }
        """
        rule = hext.Rule(
            """
        <h3 id="elements-3" @text:link />
        # match <article> and store its content as "content"
            <table>
                <thead>
                    <tr>
                        <th @text:replace(/†/, ""):columns>
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <* @text:replace(/(;)/, ""):column_data />
                    </tr>
                </tbody>
            </table>
        """
        )

        results = rule.extract(html)
        result = results[0]

        columns = result["columns"]
        column_data = result["column_data"]
        return {
            el["Element"]: el
            for el in Hextract.parse_table(columns, column_data)
        }

    def parse_attr_table(html):
        """
        Return all html attrs in format

        "wrap": {
            "Attribute": "wrap",
            "Element(s)": "textarea",
            "Description": "How the value of the form control is to be wrapped for form submission",
            "Value": "\"soft\"; \"hard\""
        },
        """

        rule_attrs = hext.Rule(
            """
        <h3 id="attributes-3" @text:link />
            <table>
                <thead>
                    <tr>
                        <th @text:columns>
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <+tr>
                        <* @text:column_data />
                    </tr>
                </tbody>
            </table>          
            
        """
        )
        rule_events = hext.Rule(
            """
            <table id="ix-event-handlers">
                <thead>
                    <tr>
                        <th @text:columns>
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <+tr>
                        <* @text:column_data />
                    </tr>
                </tbody>
            </table>"""
        )

        attr_result = rule_attrs.extract(html)
        assert len(attr_result) == 1, "Expected 1, check the parser"
        attr_result = attr_result[0]

        event_result = rule_events.extract(html)
        assert len(event_result) == 1, "Expected 1, check the parser"
        event_result = event_result[0]

        assert event_result["columns"] == attr_result["columns"], (
            "Columns mismatch"
        )
        elements = []
        for result in [attr_result, event_result]:
            columns = result["columns"]
            column_data = result["column_data"]
            for el in Hextract.parse_table(columns, column_data):
                print(el)
                elements.append(el)
        return elements

    def refine_attrs(table_list):
        for table_idx in range(len(table_list)):
            attr = table_list[table_idx]
            els = attr["Element(s)"]
            els = els.split("; ")
            for i in range(len(els)):
                # Some elements are like "source (in picture)"
                els[i] = re.sub(r" \(.*\)", "", els[i])

            # Most values will just be strings
            # But some are enums so we can at least try to parse them
            values = attr["Value"].split("; ")
            # This bit fixes some arrays like "one; two;"
            # which, at this time, occurs on the popover element
            if values[-1].endswith(";"):
                values[-1] = values[-1].rstrip(";")
            if all(
                [
                    (v.startswith('"') and v.endswith('"'))
                    or v == "the empty string"
                    for v in values
                ]
            ):
                values = [
                    v.replace('"', "").replace("the empty string", "")
                    for v in values
                ]
                attr["Value"] = values
            attr["Element(s)"] = els
            table_list[table_idx] = attr

    spec_doc = fetch_or_retrieve(WHATWG_STANDARD, "reference/w3-spec.html")

    def hextract(spec_doc):
        html = hext.Html(spec_doc)

        attrs = Hextract.parse_attr_table(html)
        Hextract.refine_attrs(attrs)
        elements = Hextract.parse_element_table(html)
        global_atttrs = []

        for attr in attrs:
            for element in attr["Element(s)"]:
                if element == "HTML elements":
                    global_atttrs.append(attr)

        for this_element_name, this_element in elements.items():
            this_element["attributes"] = []
            for attr in attrs:
                for element in attr["Element(s)"]:
                    if element == this_element_name:
                        this_element["attributes"].append(attr)

        spec = {"_global_attributes": global_atttrs} | elements

        return spec


class MDNSpec:
    def attr_parse(attr_name, attr_defn):
        attr_compat = attr_defn["__compat"]
        compat_status = attr_compat["status"]
        attr_summary = None
        result = Attribute(
            name=attr_name,
            summary=attr_summary,
            type="str",
            compatibility=Compat(
                compat_status["experimental"],
                compat_status["standard_track"],
                compat_status["deprecated"],
                support=attr_compat["support"],
            ),
        )

        for key in attr_defn:
            if key.startswith("__"):
                continue
            result.subattrs.append(MDNSpec.attr_parse(key, attr_defn[key]))
        return result

    def parse():
        spec = json.loads(fetch_or_retrieve(SPECS_INDEX, index_fn))

        spec_items = {}
        for e in spec:
            item = spec[e]
            for defn in item:
                fn = defn["filename"]
                if isinstance(fn, str) and fn.startswith("html/"):
                    spec_items[e] = defn
                    spec_items[e]["spec"] = json.loads(
                        fetch_or_retrieve(
                            f"{SPECS_BASE}/{fn}", f"reference/{fn}"
                        )
                    )

        global_spec = json.loads(
            fetch_or_retrieve(
                f"{SPECS_BASE}/html/global_attributes.json",
                "reference/global_attributes.json",
            )
        )
        global_attrs = global_spec["html"]["global_attributes"]

        elements = {}
        for el in [e for e in spec_items if e.endswith("-element")]:
            defn = spec_items[el]
            element = Element(
                name=defn["name"],
                engines=defn["engines"],
                mdn_url=defn["mdn_url"],
                summary=defn["summary"],
            )
            element_spec = spec_items[el]["spec"]["html"]["elements"][
                element.name
            ]
            compatibility = element_spec["__compat"]
            for attr_name in element_spec | global_attrs:
                if attr_name == "__compat":
                    continue
                if not (attr_defn := global_attrs.get(attr_name, None)):
                    attr_defn = element_spec[attr_name]

                element.attributes.append(
                    MDNSpec.attr_parse(attr_name, attr_defn)
                )

            status = compatibility["status"]
            experimental, standard_track, deprecated = (
                status["experimental"],
                status["standard_track"],
                status["deprecated"],
            )
            assert not (experimental or deprecated or not standard_track), (
                "Out of support element not typically found here in MDN"
            )
            elements[element.name] = element

        output = {}
        for element in elements.values():
            element: Element
            output[element.name] = asdict(element)

        return output


spec_doc = fetch_or_retrieve(WHATWG_STANDARD, "reference/w3-spec.html")
mdn = MDNSpec.parse()
hextracted = Hextract.hextract(spec_doc)
document = {}

for element, defn in hextracted.items():
    document[element] = {"spec": defn, "mdn": None}

for element, defn in MDNSpec.parse().items():
    document[element]["mdn"] = defn

get_path("spec_reference.json").write_text(json.dumps(document, indent=2))
