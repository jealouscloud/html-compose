from bs4 import BeautifulSoup

import html_compose as h
from html_compose import a, div, img


def get_soup(input: str):
    return BeautifulSoup(input, features="html.parser")


def normalize_html(html):
    soup = get_soup(html)
    return soup.prettify()


def test_soup_empty_attrs():
    data_1 = '<div hidden="">'
    data_2 = "<div hidden>"

    soup_1 = get_soup(data_1)
    soup_2 = get_soup(data_2)
    assert soup_1.prettify() == soup_2.prettify()


def test_base_element_initialization():
    expected = """<div id="a">
 <img src = "google.com"/>
 <div>
  <div>
   <div>
    hi
   </div>
  </div>
 </div>
</div>"""
    element = div(id="a")[
        img(attrs={"src": "google.com"}), div()[div()[div()["hi"]]]
    ]

    rasterized = element.__html__()
    print("--")
    p1 = normalize_html(rasterized)
    p2 = normalize_html(expected)
    assert p1 == p2
    print(rasterized)
    print(element.__html__())


def test_attr_syntax_variations():
    a = div(id=1, attrs=(div._.accesskey("a"), div._.tabindex(1))).render()
    b = div(id=1, attrs=[{"accesskey": "a", "tabindex": "1"}]).render()
    assert a == b
    c = div(id=1, attrs=[{"accesskey": "a"}, div._.tabindex(1)]).render()
    assert c == b


def test_nested_callables():
    """
    Test that nesting callables works correctly.
    """
    a = div()
    a.append("text", lambda x: div()[x.tag, lambda y: y.tag])
    assert a.render() == "<div>text<div>divdiv</div></div>"


def test_resolve_none():
    el = div()[None].render()
    assert el == "<div></div>", "Nonetype should result in empty string"


def test_xss():
    bad_string = "<SCRIPT SRC=https://cdn.jsdelivr.net/gh/Moksh45/host-xss.rocks/index.js></SCRIPT>"
    el = div(attrs={"class": ["a", bad_string, "c"]})[
        lambda: bad_string
    ].render()
    assert bad_string not in el, "xss string should not be present"
    el = div(id=bad_string, class_=bad_string).render()
    assert bad_string not in el, "xss string should not be present"
    el = div()[bad_string].render()
    assert bad_string not in el, "xss string should not be present"
    from html_compose import unsafe_text

    el = div(id="1")[unsafe_text(bad_string)].render()
    assert bad_string in el, "xss string manually added should be present"


def test_id():
    el = div(id="123").render()
    assert el == '<div id="123"></div>'


def test_href():
    literal = '<a href="https://google.com">Search Engine</a>'
    a1 = a(href=a._.href("https://google.com"))["Search Engine"].render()
    a2 = a(href="https://google.com")["Search Engine"].render()
    assert a1 == literal
    assert a2 == literal
    assert a1 == a2


def test_doc():
    username = "wanderer"
    print(
        h.html()[
            h.head()[
                h.title()[f"Welcome, {username}!"],
                h.body()[
                    h.article()[
                        h.p()[
                            "Welcome to the internet", h.strong()[username], "!"
                        ],
                        h.br(),
                        h.p()[
                            "Have you checked out this cool thing called a ",
                            h.a(href="https://google.com")["search engine"],
                            "?",
                        ],
                    ]
                ],
            ]
        ].render()
    )
    # h.form(enctype=h.form.enctype()


def test_generic_attr():
    from html_compose.attributes import BaseAttribute

    el = div(attrs={"data-foo": "bar"})
    assert el.render() == '<div data-foo="bar"></div>'
    el = div(attrs=[BaseAttribute("data-foo", "bar")])
    assert el.render() == '<div data-foo="bar"></div>'


def test_kw_arg_attr():
    el = div(id="test", class_="test-class", tabindex=1)
    assert (
        el.render() == '<div id="test" class="test-class" tabindex="1"></div>'
    )


def test_class_getitem():
    """
    Sometimes I forget to construct elements that only contain a string.

    A syntax alteration was added __class_getitem__ which this test verifies.
    """
    el = div["demo"]
    assert el.render() == "<div>demo</div>"


def test_doubled_class():
    el = div(attrs=[div._.class_("flex")], class_={"dark-mode": True})
    assert el.render() == '<div class="flex dark-mode"></div>'


def test_equivalent():
    a = h.meta(name="viewport", content="width=device-width, initial-scale=1.0")
    b = h.meta(name="viewport", content="width=device-width, initial-scale=1.0")
    assert a == b


def test_document():
    doc = h.HTML5Document(
        "Test",
        lang="en",
        head=None,
        body=[h.button["Button"], h.br(), h.p["demo 2"]],
    )
    expected = "\n".join(
        [
            "<!DOCTYPE html>",
            '<html lang="en"><head><meta content="width=device-width, initial-scale=1.0" name="viewport"/><title>Test</title></head><body><button>Button</button><br/><p>demo 2</p></body></html>',
        ]
    )
    assert doc == expected


def test_float_precision():
    """Test float precision and setting per-element settings"""
    num = 1 / 3
    a = h.p[num].render()
    assert a == "<p>0.333</p>"
    h.p.FLOAT_PRECISION = 0
    b = h.p[num].render()
    assert b == "<p>0</p>"
    c = h.h1[num].render()
    assert c == "<h1>0.333</h1>"
    # Now set globally
    h.elements.BaseElement.FLOAT_PRECISION = 0
    d = h.h1[num].render()
    assert d == "<h1>0</h1>"


def test_list_attribute():
    el = div({"class": ["a", "b", "c"]})
    assert el.render() == '<div class="a b c"></div>'


def test_rel_array():
    # ensure the list type arg doesnt violate type checks and builds
    # correctly
    el = a(rel=["noopener", "noreferrer"])
    assert el.render() == '<a rel="noopener noreferrer"></a>'


def test_custom_element():
    from html_compose import CustomElement

    custom = CustomElement.create("custom")
    el = custom["Hello world"]
    assert el.render() == "<custom>Hello world</custom>"
