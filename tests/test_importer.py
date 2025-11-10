import pytest

import html_compose.elements as el
from html_compose.document import HTML5Document
from html_compose.resource import (
    css_import,
    font_import_manual,
    font_import_provider,
    js_import,
    to_elements,
)


def get_css():
    return [
        css_import("./static/admin.css", cache_bust=False),
        css_import(
            "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css",
            hash=(
                "sha384-9ndCyUaIbzAi2FUVXJi0CjmCapS"
                "mO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM"
            ),
            crossorigin="anonymous",
            preload=True,
        ),
    ]


def get_js():
    return [
        js_import("./static/admin.js", name="admin", cache_bust=False),
        js_import(
            "https://cdn.jsdelivr.net/npm/alpinejs@3.15.0/+esm",
            name="alpinejs",
            preload=True,
            hash=(
                "sha384-Yf57wlxlrA1+0X6Ye9NOBxQ1tpmiwI/"
                "9mFpv9tT/Rh2UAajwwAlTWHnvTGYhgv7p"
            ),
            crossorigin="anonymous",
        ),
    ]


def get_font_manual():
    return [
        font_import_manual(
            "./static/fonts/MyFont.woff2",
            family="MyFont",
            weight="normal",
            style="normal",
            display="swap",
            cache_bust=False,
        ),
        font_import_manual(
            "https://example.com/fonts/OtherFontBold.woff2",
            family="OtherFont",
            weight="bold",
            display="swap",
            crossorigin="anonymous",
            preload=True,
        ),
        font_import_manual(
            "https://example.com/fonts/OtherFontLight.woff2",
            family="OtherFont",
            weight=(1, 400),
            style="normal",
            display="swap",
            crossorigin="anonymous",
            preload=True,
        ),
    ]


def get_font_remote():
    """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
    """

    return [
        font_import_provider(
            href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap",
            preconnect=[
                "https://fonts.googleapis.com",
                "https://fonts.gstatic.com",
            ],
            preconnect_crossorigin="anonymous",
        )
    ]


def get_fonts():
    return [
        font_import_manual(
            "./static/fonts/MyFont.woff2",
            family="MyFont",
            weight="normal",
            style="normal",
            display="swap",
            cache_bust=False,
        ),
        font_import_provider(
            href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap",
            preconnect=[
                "https://fonts.googleapis.com",
                "https://fonts.gstatic.com",
            ],
            preconnect_crossorigin="anonymous",
        ),
    ]


# This is only for the 06_resource_imports.md doc
@pytest.mark.skip(reason="For doc generation only")
def test_gen_docs():
    css = get_css()
    js = get_js()
    fonts = get_fonts()
    elements = to_elements(js, css, fonts)
    doc = el.head()[elements].resolve()
    for line in doc:
        print(line)
    print("---")
    print(
        HTML5Document(
            title="demo",
            lang="en",
            js=js,
            css=css,
            fonts=fonts,
            body=[el.h1()["Hello world"]],
        )
    )
    assert False


def test_get_fonts():
    fonts = get_fonts()
    elements = to_elements([], [], fonts)

    expected = [
        "<head>",
        '<link href="https://fonts.googleapis.com" crossorigin="anonymous" rel="preconnect"/>',
        '<link href="https://fonts.gstatic.com" crossorigin="anonymous" rel="preconnect"/>',
        '<link href="./static/fonts/MyFont.woff2" type="font/woff2" as="font" rel="preload"/>',
        '<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&amp;display=swap" rel="stylesheet"/>',
        "<style>",
        "@font-face {\n\tfont-family: 'MyFont';\n\tsrc: url('./static/fonts/MyFont.woff2');\n\tfont-style: normal;\n\tfont-display: swap;\n\tfont-weight: normal;\n}",
        "</style>",
        "</head>",
    ]

    result = [str(x) for x in el.head()[elements].resolve()]
    # print(result)
    for i, line in enumerate(result):
        assert line == expected[i], f"Line {i + 1} does not match"


def test_font_remote():
    fonts = get_font_remote()
    elements = to_elements([], [], fonts)

    expected = [
        "<head>",
        '<link href="https://fonts.googleapis.com" crossorigin="anonymous" rel="preconnect"/>',
        '<link href="https://fonts.gstatic.com" crossorigin="anonymous" rel="preconnect"/>',
        '<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&amp;display=swap" rel="stylesheet"/>',
        "</head>",
    ]

    result = [str(x) for x in el.head()[elements].resolve()]
    # print(result)
    for i, line in enumerate(result):
        assert line == expected[i], f"Line {i + 1} does not match"


def test_js_import():
    js = [
        js_import(
            "./static/admin.js", name="admin", preload=True, cache_bust=False
        ),
        js_import(
            "https://cdn.jsdelivr.net/npm/alpinejs@3.15.0/+esm",
            name="alpinejs",
            preload=True,
            hash=(
                "sha384-Yf57wlxlrA1+0X6Ye9NOBxQ1tpmiwI/"
                "9mFpv9tT/Rh2UAajwwAlTWHnvTGYhgv7p"
            ),
            crossorigin="anonymous",
        ),
    ]
    expected = [
        "<head>",
        '<link href="./static/admin.js" rel="modulepreload"/>',
        '<link href="https://cdn.jsdelivr.net/npm/alpinejs@3.15.0/+esm" integrity="sha384-Yf57wlxlrA1+0X6Ye9NOBxQ1tpmiwI/9mFpv9tT/Rh2UAajwwAlTWHnvTGYhgv7p" crossorigin="anonymous" rel="modulepreload"/>',
        '<script type="importmap">',
        '{"imports": {"admin": "./static/admin.js", "alpinejs": "https://cdn.jsdelivr.net/npm/alpinejs@3.15.0/+esm"}}',
        "</script>",
        '<script src="./static/admin.js" type="module">',
        "</script>",
        '<script src="https://cdn.jsdelivr.net/npm/alpinejs@3.15.0/+esm" type="module" integrity="sha384-Yf57wlxlrA1+0X6Ye9NOBxQ1tpmiwI/9mFpv9tT/Rh2UAajwwAlTWHnvTGYhgv7p" crossorigin="anonymous">',
        "</script>",
        "</head>",
    ]
    elements = to_elements(js, [])
    result = [str(x) for x in el.head()[elements].resolve()]

    for i, line in enumerate(result):
        assert line == expected[i], f"Line {i + 1} does not match"


def test_font_import_manual():
    fonts = get_font_manual()
    elements = to_elements([], [], fonts)

    expected = [
        "<head>",
        '<link href="./static/fonts/MyFont.woff2" type="font/woff2" as="font" rel="preload"/>',
        '<link href="https://example.com/fonts/OtherFontBold.woff2" crossorigin="anonymous" type="font/woff2" as="font" rel="preload"/>',
        '<link href="https://example.com/fonts/OtherFontLight.woff2" crossorigin="anonymous" type="font/woff2" as="font" rel="preload"/>',
        "<style>",
        (
            "@font-face {\n"
            "\tfont-family: 'MyFont';\n"
            "\tsrc: url('./static/fonts/MyFont.woff2');\n"
            "\tfont-style: normal;\n"
            "\tfont-display: swap;\n"
            "\tfont-weight: normal;\n"
            "}\n"
            "@font-face {\n"
            "\tfont-family: 'OtherFont';\n"
            "\tsrc: url('https://example.com/fonts/OtherFontBold.woff2');\n"
            "\tfont-style: normal;\n"
            "\tfont-display: swap;\n"
            "\tfont-weight: bold;\n"
            "}\n"
            "@font-face {\n"
            "\tfont-family: 'OtherFont';\n"
            "\tsrc: url('https://example.com/fonts/OtherFontLight.woff2');\n"
            "\tfont-style: normal;\n"
            "\tfont-display: swap;\n"
            "\tfont-weight: 1 400;\n"
            "}"
        ),
        "</style>",
        "</head>",
    ]

    result = [str(x) for x in el.head()[elements].resolve()]
    # print(result)
    for i, line in enumerate(result):
        assert line == expected[i], f"Line {i + 1} does not match"


def test_importer():
    css = get_css()
    js = get_js()
    elements = to_elements(js, css)
    expected = [
        "<head>",
        '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous" as="style" rel="preload"/>',
        '<link href="https://cdn.jsdelivr.net/npm/alpinejs@3.15.0/+esm" integrity="sha384-Yf57wlxlrA1+0X6Ye9NOBxQ1tpmiwI/9mFpv9tT/Rh2UAajwwAlTWHnvTGYhgv7p" crossorigin="anonymous" rel="modulepreload"/>',
        '<link href="./static/admin.css" rel="stylesheet"/>',
        '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous" rel="stylesheet"/>',
        '<script type="importmap">',
        '{"imports": {"admin": "./static/admin.js", "alpinejs": "https://cdn.jsdelivr.net/npm/alpinejs@3.15.0/+esm"}}',
        "</script>",
        '<script src="./static/admin.js" type="module">',
        "</script>",
        '<script src="https://cdn.jsdelivr.net/npm/alpinejs@3.15.0/+esm" type="module" integrity="sha384-Yf57wlxlrA1+0X6Ye9NOBxQ1tpmiwI/9mFpv9tT/Rh2UAajwwAlTWHnvTGYhgv7p" crossorigin="anonymous">',
        "</script>",
        "</head>",
    ]
    result = [str(x) for x in el.head()[elements].resolve()]
    # print(result)
    for i, line in enumerate(result):
        assert line == expected[i], f"Line {i + 1} does not match"

    with pytest.raises(ValueError):
        js_import(
            "https://cdn.jsdelivr.net/npm/alpinejs@3.15.0/+esm",
            name="alpinejs",
            preload=True,
            hash=(
                "sha384-Yf57wlxlrA1+0X6Ye9NOBxQ1tpmiwI/"
                "9mFpv9tT/Rh2UAajwwAlTWHnvTGYhgv7p"
            ),
        )  # noqa


def test_document_generator():
    css = get_css()
    js = get_js()
    result = HTML5Document(
        title="demo", lang="en", js=js, css=css, body=[el.h1()["Hello world"]]
    ).stream("full")
    expected = [
        '<!DOCTYPE html>\n<html lang="en">\n<head><meta content="width=device-width, initial-scale=1.0" name="viewport"/><title>demo</title><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous" as="style" rel="preload"/><link href="https://cdn.jsdelivr.net/npm/alpinejs@3.15.0/+esm" integrity="sha384-Yf57wlxlrA1+0X6Ye9NOBxQ1tpmiwI/9mFpv9tT/Rh2UAajwwAlTWHnvTGYhgv7p" crossorigin="anonymous" rel="modulepreload"/><link href="./static/admin.css" rel="stylesheet"/><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous" rel="stylesheet"/><script type="importmap">{"imports": {"admin": "./static/admin.js", "alpinejs": "https://cdn.jsdelivr.net/npm/alpinejs@3.15.0/+esm"}}</script><script src="./static/admin.js" type="module"></script><script src="https://cdn.jsdelivr.net/npm/alpinejs@3.15.0/+esm" type="module" integrity="sha384-Yf57wlxlrA1+0X6Ye9NOBxQ1tpmiwI/9mFpv9tT/Rh2UAajwwAlTWHnvTGYhgv7p" crossorigin="anonymous"></script></head>\n\n',
        "<body>",
        "<h1>",
        "Hello world",
        "</h1>",
        "</body>",
        "\n",
        "</html>",
    ]

    result = [str(x) for x in result]
    # print(result)
    for i, line in enumerate(result):
        assert line == expected[i], f"Line {i + 1} does not match"
