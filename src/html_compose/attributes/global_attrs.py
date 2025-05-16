from . import BaseAttribute
from typing import Literal


class GlobalAttrs:
    """
    This module contains classes for all global attributes.
    Elements can inherit it so the element can be a reference to our attributes
    """

    @staticmethod
    def accesskey(value: list) -> BaseAttribute:
        """
        "global" attribute: accesskey  
        Keyboard shortcut to activate or focus element  

        :param value: Ordered set of unique space-separated tokens, none of which are identical to another, each consisting of one code point in length  
        :return: An accesskey attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("accesskey", value)

    @staticmethod
    def autocapitalize(
        value: Literal["on", "off", "none", "sentences", "words", "characters"],
    ) -> BaseAttribute:
        """
        "global" attribute: autocapitalize  
        Recommended autocapitalization behavior (for supported input methods)  

        :param value: ['on', 'off', 'none', 'sentences', 'words', 'characters']  
        :return: An autocapitalize attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("autocapitalize", value)

    @staticmethod
    def autocorrect(value: Literal["on", "off"]) -> BaseAttribute:
        """
        "global" attribute: autocorrect  
        Recommended autocorrection behavior (for supported input methods)  

        :param value: ['on', 'off']  
        :return: An autocorrect attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("autocorrect", value)

    @staticmethod
    def autofocus(value: bool) -> BaseAttribute:
        """
        "global" attribute: autofocus  
        Automatically focus the element when the page is loaded  

        :param value: Boolean attribute  
        :return: An autofocus attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("autofocus", value)

    @staticmethod
    def class_(value: list) -> BaseAttribute:
        """
        "global" attribute: class  
        Classes to which the element belongs  

        :param value: Set of space-separated tokens  
        :return: An class attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("class", value)

    @staticmethod
    def contenteditable(
        value: Literal["true", "plaintext-only", "false"],
    ) -> BaseAttribute:
        """
        "global" attribute: contenteditable  
        Whether the element is editable  

        :param value: ['true', 'plaintext-only', 'false']  
        :return: An contenteditable attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("contenteditable", value)

    @staticmethod
    def dir(value: Literal["ltr", "rtl", "auto"]) -> BaseAttribute:
        """
        "global" attribute: dir  
        The text directionality of the element  

        :param value: ['ltr', 'rtl', 'auto']  
        :return: An dir attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("dir", value)

    @staticmethod
    def draggable(value: Literal["true", "false"]) -> BaseAttribute:
        """
        "global" attribute: draggable  
        Whether the element is draggable  

        :param value: ['true', 'false']  
        :return: An draggable attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("draggable", value)

    @staticmethod
    def enterkeyhint(
        value: Literal[
            "enter", "done", "go", "next", "previous", "search", "send"
        ],
    ) -> BaseAttribute:
        """
        "global" attribute: enterkeyhint  
        Hint for selecting an enter key action  

        :param value: ['enter', 'done', 'go', 'next', 'previous', 'search', 'send']  
        :return: An enterkeyhint attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("enterkeyhint", value)

    @staticmethod
    def hidden(value: Literal["until-found", "hidden", ""]) -> BaseAttribute:
        """
        "global" attribute: hidden  
        Whether the element is relevant  

        :param value: ['until-found', 'hidden', '']  
        :return: An hidden attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("hidden", value)

    @staticmethod
    def id(value: str) -> BaseAttribute:
        """
        "global" attribute: id  
        The element's ID  

        :param value: Text*  
        :return: An id attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("id", value)

    @staticmethod
    def inert(value: bool) -> BaseAttribute:
        """
        "global" attribute: inert  
        Whether the element is inert.  

        :param value: Boolean attribute  
        :return: An inert attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("inert", value)

    @staticmethod
    def inputmode(
        value: Literal[
            "none",
            "text",
            "tel",
            "email",
            "url",
            "numeric",
            "decimal",
            "search",
        ],
    ) -> BaseAttribute:
        """
        "global" attribute: inputmode  
        Hint for selecting an input modality  

        :param value: ['none', 'text', 'tel', 'email', 'url', 'numeric', 'decimal', 'search']  
        :return: An inputmode attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("inputmode", value)

    @staticmethod
    def is_(value) -> BaseAttribute:
        """
        "global" attribute: is  
        Creates a customized built-in element  

        :param value: Valid custom element name of a defined customized built-in element  
        :return: An is attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("is", value)

    @staticmethod
    def itemid(value) -> BaseAttribute:
        """
        "global" attribute: itemid  
        Global identifier for a microdata item  

        :param value: Valid URL potentially surrounded by spaces  
        :return: An itemid attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("itemid", value)

    @staticmethod
    def itemprop(value: list) -> BaseAttribute:
        """
        "global" attribute: itemprop  
        Property names of a microdata item  

        :param value: Unordered set of unique space-separated tokens consisting of valid absolute URLs, defined property names, or text*  
        :return: An itemprop attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("itemprop", value)

    @staticmethod
    def itemref(value: list) -> BaseAttribute:
        """
        "global" attribute: itemref  
        Referenced elements  

        :param value: Unordered set of unique space-separated tokens consisting of IDs*  
        :return: An itemref attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("itemref", value)

    @staticmethod
    def itemscope(value: bool) -> BaseAttribute:
        """
        "global" attribute: itemscope  
        Introduces a microdata item  

        :param value: Boolean attribute  
        :return: An itemscope attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("itemscope", value)

    @staticmethod
    def itemtype(value: list) -> BaseAttribute:
        """
        "global" attribute: itemtype  
        Item types of a microdata item  

        :param value: Unordered set of unique space-separated tokens consisting of valid absolute URLs*  
        :return: An itemtype attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("itemtype", value)

    @staticmethod
    def lang(value) -> BaseAttribute:
        """
        "global" attribute: lang  
        Language of the element  

        :param value: Valid BCP 47 language tag or the empty string  
        :return: An lang attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("lang", value)

    @staticmethod
    def nonce(value: str) -> BaseAttribute:
        """
        "global" attribute: nonce  
        Cryptographic nonce used in Content Security Policy checks [CSP]  

        :param value: Text  
        :return: An nonce attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("nonce", value)

    @staticmethod
    def popover(value: Literal["auto", "manual"]) -> BaseAttribute:
        """
        "global" attribute: popover  
        Makes the element a popover element  

        :param value: ['auto', 'manual']  
        :return: An popover attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("popover", value)

    @staticmethod
    def slot(value: str) -> BaseAttribute:
        """
        "global" attribute: slot  
        The element's desired slot  

        :param value: Text  
        :return: An slot attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("slot", value)

    @staticmethod
    def spellcheck(value: Literal["true", "false", ""]) -> BaseAttribute:
        """
        "global" attribute: spellcheck  
        Whether the element is to have its spelling and grammar checked  

        :param value: ['true', 'false', '']  
        :return: An spellcheck attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("spellcheck", value)

    @staticmethod
    def style(value) -> BaseAttribute:
        """
        "global" attribute: style  
        Presentational and formatting instructions  

        :param value: CSS declarations*  
        :return: An style attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("style", value)

    @staticmethod
    def tabindex(value: int) -> BaseAttribute:
        """
        "global" attribute: tabindex  
        Whether the element is focusable and sequentially focusable, and the relative order of the element for the purposes of sequential focus navigation  

        :param value: Valid integer  
        :return: An tabindex attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("tabindex", value)

    @staticmethod
    def title(value: str) -> BaseAttribute:
        """
        "global" attribute: title  
        Advisory information for the element  

        :param value: Text  
        :return: An title attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("title", value)

    @staticmethod
    def translate(value: Literal["yes", "no"]) -> BaseAttribute:
        """
        "global" attribute: translate  
        Whether the element is to be translated when the page is localized  

        :param value: ['yes', 'no']  
        :return: An translate attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("translate", value)

    @staticmethod
    def writingsuggestions(
        value: Literal["true", "false", ""],
    ) -> BaseAttribute:
        """
        "global" attribute: writingsuggestions  
        Whether the element can offer writing suggestions or not.  

        :param value: ['true', 'false', '']  
        :return: An writingsuggestions attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("writingsuggestions", value)

    @staticmethod
    def onauxclick(value) -> BaseAttribute:
        """
        "global" attribute: onauxclick  
        auxclick event handler  

        :param value: Event handler content attribute  
        :return: An onauxclick attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onauxclick", value)

    @staticmethod
    def onbeforeinput(value) -> BaseAttribute:
        """
        "global" attribute: onbeforeinput  
        beforeinput event handler  

        :param value: Event handler content attribute  
        :return: An onbeforeinput attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onbeforeinput", value)

    @staticmethod
    def onbeforematch(value) -> BaseAttribute:
        """
        "global" attribute: onbeforematch  
        beforematch event handler  

        :param value: Event handler content attribute  
        :return: An onbeforematch attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onbeforematch", value)

    @staticmethod
    def onbeforetoggle(value) -> BaseAttribute:
        """
        "global" attribute: onbeforetoggle  
        beforetoggle event handler  

        :param value: Event handler content attribute  
        :return: An onbeforetoggle attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onbeforetoggle", value)

    @staticmethod
    def onblur(value) -> BaseAttribute:
        """
        "global" attribute: onblur  
        blur event handler  

        :param value: Event handler content attribute  
        :return: An onblur attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onblur", value)

    @staticmethod
    def oncancel(value) -> BaseAttribute:
        """
        "global" attribute: oncancel  
        cancel event handler  

        :param value: Event handler content attribute  
        :return: An oncancel attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("oncancel", value)

    @staticmethod
    def oncanplay(value) -> BaseAttribute:
        """
        "global" attribute: oncanplay  
        canplay event handler  

        :param value: Event handler content attribute  
        :return: An oncanplay attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("oncanplay", value)

    @staticmethod
    def oncanplaythrough(value) -> BaseAttribute:
        """
        "global" attribute: oncanplaythrough  
        canplaythrough event handler  

        :param value: Event handler content attribute  
        :return: An oncanplaythrough attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("oncanplaythrough", value)

    @staticmethod
    def onchange(value) -> BaseAttribute:
        """
        "global" attribute: onchange  
        change event handler  

        :param value: Event handler content attribute  
        :return: An onchange attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onchange", value)

    @staticmethod
    def onclick(value) -> BaseAttribute:
        """
        "global" attribute: onclick  
        click event handler  

        :param value: Event handler content attribute  
        :return: An onclick attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onclick", value)

    @staticmethod
    def onclose(value) -> BaseAttribute:
        """
        "global" attribute: onclose  
        close event handler  

        :param value: Event handler content attribute  
        :return: An onclose attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onclose", value)

    @staticmethod
    def oncontextlost(value) -> BaseAttribute:
        """
        "global" attribute: oncontextlost  
        contextlost event handler  

        :param value: Event handler content attribute  
        :return: An oncontextlost attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("oncontextlost", value)

    @staticmethod
    def oncontextmenu(value) -> BaseAttribute:
        """
        "global" attribute: oncontextmenu  
        contextmenu event handler  

        :param value: Event handler content attribute  
        :return: An oncontextmenu attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("oncontextmenu", value)

    @staticmethod
    def oncontextrestored(value) -> BaseAttribute:
        """
        "global" attribute: oncontextrestored  
        contextrestored event handler  

        :param value: Event handler content attribute  
        :return: An oncontextrestored attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("oncontextrestored", value)

    @staticmethod
    def oncopy(value) -> BaseAttribute:
        """
        "global" attribute: oncopy  
        copy event handler  

        :param value: Event handler content attribute  
        :return: An oncopy attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("oncopy", value)

    @staticmethod
    def oncuechange(value) -> BaseAttribute:
        """
        "global" attribute: oncuechange  
        cuechange event handler  

        :param value: Event handler content attribute  
        :return: An oncuechange attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("oncuechange", value)

    @staticmethod
    def oncut(value) -> BaseAttribute:
        """
        "global" attribute: oncut  
        cut event handler  

        :param value: Event handler content attribute  
        :return: An oncut attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("oncut", value)

    @staticmethod
    def ondblclick(value) -> BaseAttribute:
        """
        "global" attribute: ondblclick  
        dblclick event handler  

        :param value: Event handler content attribute  
        :return: An ondblclick attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("ondblclick", value)

    @staticmethod
    def ondrag(value) -> BaseAttribute:
        """
        "global" attribute: ondrag  
        drag event handler  

        :param value: Event handler content attribute  
        :return: An ondrag attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("ondrag", value)

    @staticmethod
    def ondragend(value) -> BaseAttribute:
        """
        "global" attribute: ondragend  
        dragend event handler  

        :param value: Event handler content attribute  
        :return: An ondragend attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("ondragend", value)

    @staticmethod
    def ondragenter(value) -> BaseAttribute:
        """
        "global" attribute: ondragenter  
        dragenter event handler  

        :param value: Event handler content attribute  
        :return: An ondragenter attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("ondragenter", value)

    @staticmethod
    def ondragleave(value) -> BaseAttribute:
        """
        "global" attribute: ondragleave  
        dragleave event handler  

        :param value: Event handler content attribute  
        :return: An ondragleave attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("ondragleave", value)

    @staticmethod
    def ondragover(value) -> BaseAttribute:
        """
        "global" attribute: ondragover  
        dragover event handler  

        :param value: Event handler content attribute  
        :return: An ondragover attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("ondragover", value)

    @staticmethod
    def ondragstart(value) -> BaseAttribute:
        """
        "global" attribute: ondragstart  
        dragstart event handler  

        :param value: Event handler content attribute  
        :return: An ondragstart attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("ondragstart", value)

    @staticmethod
    def ondrop(value) -> BaseAttribute:
        """
        "global" attribute: ondrop  
        drop event handler  

        :param value: Event handler content attribute  
        :return: An ondrop attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("ondrop", value)

    @staticmethod
    def ondurationchange(value) -> BaseAttribute:
        """
        "global" attribute: ondurationchange  
        durationchange event handler  

        :param value: Event handler content attribute  
        :return: An ondurationchange attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("ondurationchange", value)

    @staticmethod
    def onemptied(value) -> BaseAttribute:
        """
        "global" attribute: onemptied  
        emptied event handler  

        :param value: Event handler content attribute  
        :return: An onemptied attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onemptied", value)

    @staticmethod
    def onended(value) -> BaseAttribute:
        """
        "global" attribute: onended  
        ended event handler  

        :param value: Event handler content attribute  
        :return: An onended attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onended", value)

    @staticmethod
    def onerror(value) -> BaseAttribute:
        """
        "global" attribute: onerror  
        error event handler  

        :param value: Event handler content attribute  
        :return: An onerror attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onerror", value)

    @staticmethod
    def onfocus(value) -> BaseAttribute:
        """
        "global" attribute: onfocus  
        focus event handler  

        :param value: Event handler content attribute  
        :return: An onfocus attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onfocus", value)

    @staticmethod
    def onformdata(value) -> BaseAttribute:
        """
        "global" attribute: onformdata  
        formdata event handler  

        :param value: Event handler content attribute  
        :return: An onformdata attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onformdata", value)

    @staticmethod
    def oninput(value) -> BaseAttribute:
        """
        "global" attribute: oninput  
        input event handler  

        :param value: Event handler content attribute  
        :return: An oninput attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("oninput", value)

    @staticmethod
    def oninvalid(value) -> BaseAttribute:
        """
        "global" attribute: oninvalid  
        invalid event handler  

        :param value: Event handler content attribute  
        :return: An oninvalid attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("oninvalid", value)

    @staticmethod
    def onkeydown(value) -> BaseAttribute:
        """
        "global" attribute: onkeydown  
        keydown event handler  

        :param value: Event handler content attribute  
        :return: An onkeydown attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onkeydown", value)

    @staticmethod
    def onkeypress(value) -> BaseAttribute:
        """
        "global" attribute: onkeypress  
        keypress event handler  

        :param value: Event handler content attribute  
        :return: An onkeypress attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onkeypress", value)

    @staticmethod
    def onkeyup(value) -> BaseAttribute:
        """
        "global" attribute: onkeyup  
        keyup event handler  

        :param value: Event handler content attribute  
        :return: An onkeyup attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onkeyup", value)

    @staticmethod
    def onload(value) -> BaseAttribute:
        """
        "global" attribute: onload  
        load event handler  

        :param value: Event handler content attribute  
        :return: An onload attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onload", value)

    @staticmethod
    def onloadeddata(value) -> BaseAttribute:
        """
        "global" attribute: onloadeddata  
        loadeddata event handler  

        :param value: Event handler content attribute  
        :return: An onloadeddata attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onloadeddata", value)

    @staticmethod
    def onloadedmetadata(value) -> BaseAttribute:
        """
        "global" attribute: onloadedmetadata  
        loadedmetadata event handler  

        :param value: Event handler content attribute  
        :return: An onloadedmetadata attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onloadedmetadata", value)

    @staticmethod
    def onloadstart(value) -> BaseAttribute:
        """
        "global" attribute: onloadstart  
        loadstart event handler  

        :param value: Event handler content attribute  
        :return: An onloadstart attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onloadstart", value)

    @staticmethod
    def onmousedown(value) -> BaseAttribute:
        """
        "global" attribute: onmousedown  
        mousedown event handler  

        :param value: Event handler content attribute  
        :return: An onmousedown attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onmousedown", value)

    @staticmethod
    def onmouseenter(value) -> BaseAttribute:
        """
        "global" attribute: onmouseenter  
        mouseenter event handler  

        :param value: Event handler content attribute  
        :return: An onmouseenter attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onmouseenter", value)

    @staticmethod
    def onmouseleave(value) -> BaseAttribute:
        """
        "global" attribute: onmouseleave  
        mouseleave event handler  

        :param value: Event handler content attribute  
        :return: An onmouseleave attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onmouseleave", value)

    @staticmethod
    def onmousemove(value) -> BaseAttribute:
        """
        "global" attribute: onmousemove  
        mousemove event handler  

        :param value: Event handler content attribute  
        :return: An onmousemove attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onmousemove", value)

    @staticmethod
    def onmouseout(value) -> BaseAttribute:
        """
        "global" attribute: onmouseout  
        mouseout event handler  

        :param value: Event handler content attribute  
        :return: An onmouseout attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onmouseout", value)

    @staticmethod
    def onmouseover(value) -> BaseAttribute:
        """
        "global" attribute: onmouseover  
        mouseover event handler  

        :param value: Event handler content attribute  
        :return: An onmouseover attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onmouseover", value)

    @staticmethod
    def onmouseup(value) -> BaseAttribute:
        """
        "global" attribute: onmouseup  
        mouseup event handler  

        :param value: Event handler content attribute  
        :return: An onmouseup attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onmouseup", value)

    @staticmethod
    def onpaste(value) -> BaseAttribute:
        """
        "global" attribute: onpaste  
        paste event handler  

        :param value: Event handler content attribute  
        :return: An onpaste attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onpaste", value)

    @staticmethod
    def onpause(value) -> BaseAttribute:
        """
        "global" attribute: onpause  
        pause event handler  

        :param value: Event handler content attribute  
        :return: An onpause attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onpause", value)

    @staticmethod
    def onplay(value) -> BaseAttribute:
        """
        "global" attribute: onplay  
        play event handler  

        :param value: Event handler content attribute  
        :return: An onplay attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onplay", value)

    @staticmethod
    def onplaying(value) -> BaseAttribute:
        """
        "global" attribute: onplaying  
        playing event handler  

        :param value: Event handler content attribute  
        :return: An onplaying attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onplaying", value)

    @staticmethod
    def onprogress(value) -> BaseAttribute:
        """
        "global" attribute: onprogress  
        progress event handler  

        :param value: Event handler content attribute  
        :return: An onprogress attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onprogress", value)

    @staticmethod
    def onratechange(value) -> BaseAttribute:
        """
        "global" attribute: onratechange  
        ratechange event handler  

        :param value: Event handler content attribute  
        :return: An onratechange attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onratechange", value)

    @staticmethod
    def onreset(value) -> BaseAttribute:
        """
        "global" attribute: onreset  
        reset event handler  

        :param value: Event handler content attribute  
        :return: An onreset attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onreset", value)

    @staticmethod
    def onresize(value) -> BaseAttribute:
        """
        "global" attribute: onresize  
        resize event handler  

        :param value: Event handler content attribute  
        :return: An onresize attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onresize", value)

    @staticmethod
    def onscroll(value) -> BaseAttribute:
        """
        "global" attribute: onscroll  
        scroll event handler  

        :param value: Event handler content attribute  
        :return: An onscroll attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onscroll", value)

    @staticmethod
    def onscrollend(value) -> BaseAttribute:
        """
        "global" attribute: onscrollend  
        scrollend event handler  

        :param value: Event handler content attribute  
        :return: An onscrollend attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onscrollend", value)

    @staticmethod
    def onsecuritypolicyviolation(value) -> BaseAttribute:
        """
        "global" attribute: onsecuritypolicyviolation  
        securitypolicyviolation event handler  

        :param value: Event handler content attribute  
        :return: An onsecuritypolicyviolation attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onsecuritypolicyviolation", value)

    @staticmethod
    def onseeked(value) -> BaseAttribute:
        """
        "global" attribute: onseeked  
        seeked event handler  

        :param value: Event handler content attribute  
        :return: An onseeked attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onseeked", value)

    @staticmethod
    def onseeking(value) -> BaseAttribute:
        """
        "global" attribute: onseeking  
        seeking event handler  

        :param value: Event handler content attribute  
        :return: An onseeking attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onseeking", value)

    @staticmethod
    def onselect(value) -> BaseAttribute:
        """
        "global" attribute: onselect  
        select event handler  

        :param value: Event handler content attribute  
        :return: An onselect attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onselect", value)

    @staticmethod
    def onslotchange(value) -> BaseAttribute:
        """
        "global" attribute: onslotchange  
        slotchange event handler  

        :param value: Event handler content attribute  
        :return: An onslotchange attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onslotchange", value)

    @staticmethod
    def onstalled(value) -> BaseAttribute:
        """
        "global" attribute: onstalled  
        stalled event handler  

        :param value: Event handler content attribute  
        :return: An onstalled attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onstalled", value)

    @staticmethod
    def onsubmit(value) -> BaseAttribute:
        """
        "global" attribute: onsubmit  
        submit event handler  

        :param value: Event handler content attribute  
        :return: An onsubmit attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onsubmit", value)

    @staticmethod
    def onsuspend(value) -> BaseAttribute:
        """
        "global" attribute: onsuspend  
        suspend event handler  

        :param value: Event handler content attribute  
        :return: An onsuspend attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onsuspend", value)

    @staticmethod
    def ontimeupdate(value) -> BaseAttribute:
        """
        "global" attribute: ontimeupdate  
        timeupdate event handler  

        :param value: Event handler content attribute  
        :return: An ontimeupdate attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("ontimeupdate", value)

    @staticmethod
    def ontoggle(value) -> BaseAttribute:
        """
        "global" attribute: ontoggle  
        toggle event handler  

        :param value: Event handler content attribute  
        :return: An ontoggle attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("ontoggle", value)

    @staticmethod
    def onvolumechange(value) -> BaseAttribute:
        """
        "global" attribute: onvolumechange  
        volumechange event handler  

        :param value: Event handler content attribute  
        :return: An onvolumechange attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onvolumechange", value)

    @staticmethod
    def onwaiting(value) -> BaseAttribute:
        """
        "global" attribute: onwaiting  
        waiting event handler  

        :param value: Event handler content attribute  
        :return: An onwaiting attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onwaiting", value)

    @staticmethod
    def onwheel(value) -> BaseAttribute:
        """
        "global" attribute: onwheel  
        wheel event handler  

        :param value: Event handler content attribute  
        :return: An onwheel attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("onwheel", value)
