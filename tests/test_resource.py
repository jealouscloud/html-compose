import json

from html_compose.resource import js_import, to_elements


def _extract_import_map(elements):
    for element in elements:
        if element.tag == "script" and element.attrs.get("type") == "importmap":
            rendered = element.render()
            payload = rendered.split(">", 1)[1].rsplit("<", 1)[0]
            return json.loads(payload)
    raise AssertionError("importmap script not found")


def test_js_import_scoped_single():
    elements = to_elements(
        js=[js_import("/static/mod.js", name="mod", scope_url="/admin")]
    )
    import_map = _extract_import_map(elements)
    assert import_map["imports"]["mod"].startswith("/static/mod.js")
    assert import_map["scopes"]["/admin"]["mod"].startswith("/static/mod.js")


def test_js_import_scoped_iterable():
    elements = to_elements(
        js=[
            js_import(
                "/static/feature.js",
                name="feature",
                scope_url=["/settings", "/profile"],
            )
        ]
    )
    import_map = _extract_import_map(elements)
    scopes = import_map["scopes"]
    assert scopes["/settings"]["feature"].startswith("/static/feature.js")
    assert scopes["/profile"]["feature"].startswith("/static/feature.js")
