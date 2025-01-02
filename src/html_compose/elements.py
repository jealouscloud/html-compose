from typing import Any, Callable, Optional, TypeAlias, Union

from .attributes import GlobalAttrs, ImgAttrs
from .base_attribute import BaseAttribute
from .base_element import BaseElement


class img(BaseElement, GlobalAttrs, ImgAttrs):
    attr_type: TypeAlias = Union[
        Callable[["img"], list[BaseAttribute]], list[BaseAttribute]
    ]

    def attrs(fun: Callable[["img"], list[BaseAttribute]]):
        """
        Callable for type hints while generating attr list

        Example: img(attrs=img.attrs(lambda _: [img.src("google.com")]))
        """
        return fun(img)

    def __init__(
        self,
        id: GlobalAttrs.id = None,
        class_: GlobalAttrs.class_ = None,
        attrs: attr_type = None,
        data: Optional[Any] = None,
    ) -> None:
        super().__init__(
            "img",
            void_element=True,
            id=id,
            class_=class_,
            attrs=attrs,
            data=data,
        )


class div(BaseElement, ImgAttrs):
    attr_type: TypeAlias = Callable[["div"], list[BaseAttribute]]

    def attrs(fun: attr_type):
        """
        Callable for type hints while generating attr list

        Example: img(attrs=img.attrs(lambda _: [img.src("google.com")]))
        """
        return fun(img)

    def __init__(
        self,
        id: GlobalAttrs.id = None,
        class_: GlobalAttrs.class_ = None,
        attrs: attr_type = None,
        data: Optional[Any] = None,
    ):
        super().__init__(
            "div",
            void_element=False,
            id=id,
            class_=class_,
            attrs=attrs,
            data=data,
        )


# img(id="demo", class_=["demo", "demo2"], attrs=img.attrs(lambda x: img

# img(attrs=[img.href("google.com")])
# img(attrs=img.attrs(lambda _: AnchorAttrs.href(

# # https://developer.mozilla.org/en-US/docs/Glossary/Doctype
# html = HTMLElement("html")

# # https://developer.mozilla.org/en-US/docs/Glossary/Void_element
# area = VoidElement("area")
# base = VoidElement("base")
# br = VoidElement("br")
# col = VoidElement("col")
# embed = VoidElement("embed")
# hr = VoidElement("hr")
# img = VoidElement("img")
# input = VoidElement("input")
# link = VoidElement("link")
# meta = VoidElement("meta")
# param = VoidElement("param")
# source = VoidElement("source")
# track = VoidElement("track")
# wbr = VoidElement("wbr")

# # Non-deprecated HTML elements, extracted from
# # https://developer.mozilla.org/en-US/docs/Web/HTML/Element
# # Located via the inspector with:
# # Array.from($0.querySelectorAll('li')).filter(x=>!x.querySelector('.icon-deprecated')).map(x => x.querySelector('code').textContent) # noqa: E501
# a = Element("a")
# abbr = Element("abbr")
# abc = Element("abc")
# address = Element("address")
# article = Element("article")
# aside = Element("aside")
# audio = Element("audio")
# b = Element("b")
# bdi = Element("bdi")
# bdo = Element("bdo")
# blockquote = Element("blockquote")
# body = Element("body")
# button = Element("button")
# canvas = Element("canvas")
# caption = Element("caption")
# cite = Element("cite")
# code = Element("code")
# colgroup = Element("colgroup")
# data = Element("data")
# datalist = Element("datalist")
# dd = Element("dd")
# del_ = Element("del_")
# details = Element("details")
# dfn = Element("dfn")
# dialog = Element("dialog")
# div = Element("div")
# dl = Element("dl")
# dt = Element("dt")
# em = Element("em")
# fieldset = Element("fieldset")
# figcaption = Element("figcaption")
# figure = Element("figure")
# footer = Element("footer")
# form = Element("form")
# h1 = Element("h1")
# h2 = Element("h2")
# h3 = Element("h3")
# h4 = Element("h4")
# h5 = Element("h5")
# h6 = Element("h6")
# head = Element("head")
# header = Element("header")
# hgroup = Element("hgroup")
# i = Element("i")
# iframe = Element("iframe")
# ins = Element("ins")
# kbd = Element("kbd")
# label = Element("label")
# legend = Element("legend")
# li = Element("li")
# main = Element("main")
# map = Element("map")
# mark = Element("mark")
# menu = Element("menu")
# meter = Element("meter")
# nav = Element("nav")
# noscript = Element("noscript")
# object = Element("object")
# ol = Element("ol")
# optgroup = Element("optgroup")
# option = Element("option")
# output = Element("output")
# p = Element("p")
# picture = Element("picture")
# portal = Element("portal")
# pre = Element("pre")
# progress = Element("progress")
# q = Element("q")
# rp = Element("rp")
# rt = Element("rt")
# ruby = Element("ruby")
# s = Element("s")
# samp = Element("samp")
# script = Element("script")
# search = Element("search")
# section = Element("section")
# select = Element("select")
# slot = Element("slot")
# small = Element("small")
# span = Element("span")
# strong = Element("strong")
# style = Element("style")
# sub = Element("sub")
# summary = Element("summary")
# sup = Element("sup")
# table = Element("table")
# tbody = Element("tbody")
# td = Element("td")
# template = Element("template")
# textarea = Element("textarea")
# tfoot = Element("tfoot")
# th = Element("th")
# thead = Element("thead")
# time = Element("time")
# title = Element("title")
# tr = Element("tr")
# u = Element("u")
# ul = Element("ul")
# var = Element("var")
