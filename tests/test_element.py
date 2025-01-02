from bs4 import BeautifulSoup

from html_compose.elements import div, img


def get_soup(input: str):
    return BeautifulSoup(input, features="html.parser")


def normalize_html(html):
    soup = get_soup(html)
    return soup.prettify()


# class MySpecialComponent(_ContextAware):
#     def __init__(self, name: str):
#         self.name = name

#     def context(self, ctx: Context) -> str:
#         return super().context(ctx)

#     def render(self, context):
#         return div()[img(src="google.com")]


def test_soup_empty_attrs():
    data_1 = '<div hidden="">'
    data_2 = "<div hidden>"

    soup_1 = get_soup(data_1)
    soup_2 = get_soup(data_2)
    assert soup_1.prettify() == soup_2.prettify()


def test_base_element_initialization():
    expected = """<div>
 <img src = "google.com"/>
 <div>
  <div>
   <div>
    hi
   </div>
  </div>
 </div>
</div>"""
    img(attrs=lambda x: x)
    element = div(id="a")[
        img(attrs={"src": "google.com"}), div()[div()[div()["hi"]]]
    ]

    element[div()[div()[div()["hi"]]]]
    rasterized = element.__html__()
    print("--")
    p1 = normalize_html(rasterized)
    p2 = normalize_html(expected)
    assert p1 == p2
    print(rasterized)
    print(element.__html__())


def test_attr_syntax_variations():
    a = div(id=1, attrs=[div.accesskey("a"), div.tabindex(1)]).render()
    b = div(id=1, attrs=[{"accesskey": "a", "tabindex": "1"}]).render()
    assert a == b
    c = div(id=1, attrs=[{"accesskey": "a"}, div.tabindex(1)]).render()
    assert c == b


def test_nested_callables():
    """
    Test that nesting callables works correctly.
    """
    a = div()
    a.append("text", lambda x: div()[x.name, lambda y: y.name])
    assert a.render() == "<div>text<div>divdiv</div></div>"


def test_resolve_none():
    assert div(div(None)), "Nonetype should result in empty string"


def test_xss():
    bad_string = "<SCRIPT SRC=https://cdn.jsdelivr.net/gh/Moksh45/host-xss.rocks/index.js></SCRIPT>"
    el = div(data=["a", bad_string, "c"])[lambda x: x.data].render()
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
    assert el == '<div id="123"></div'
