from . import BaseAttribute
from typing import Literal, Union, Callable

class GlobalAttrs:
    """ 
    This module contains classes for all global attributes.
    Elements can inherit it so the element can be a reference to our attributes
    """ 
    
    class accesskey(BaseAttribute):
        """
        Global Attribute attribute: accesskey
        Description: Keyboard shortcut to activate or focus element
        Value: Ordered set of unique space-separated tokens, none of which are identical to another, each consisting of one code point in length
        """
        
        def __init__(self, value):
            super().__init__("accesskey", value)
            


    class autocapitalize(BaseAttribute):
        """
        Global Attribute attribute: autocapitalize
        Description: Recommended autocapitalization behavior (for supported input methods)
        Value: ['on', 'off', 'none', 'sentences', 'words', 'characters']
        """
        
        def __init__(self, value: Literal['on', 'off', 'none', 'sentences', 'words', 'characters']):
            super().__init__("autocapitalize", value)
            


    class autocorrect(BaseAttribute):
        """
        Global Attribute attribute: autocorrect
        Description: Recommended autocorrection behavior (for supported input methods)
        Value: ['on', 'off']
        """
        
        def __init__(self, value: Literal['on', 'off']):
            super().__init__("autocorrect", value)
            


    class autofocus(BaseAttribute):
        """
        Global Attribute attribute: autofocus
        Description: Automatically focus the element when the page is loaded
        Value: Boolean attribute
        """
        
        def __init__(self, value: bool):
            super().__init__("autofocus", value)
            


    class class_(BaseAttribute):
        """
        Global Attribute attribute: class
        Description: Classes to which the element belongs
        Value: Set of space-separated tokens
        """
        
        def __init__(self, value):
            super().__init__("class", value)
            


    class contenteditable(BaseAttribute):
        """
        Global Attribute attribute: contenteditable
        Description: Whether the element is editable
        Value: ['true', 'plaintext-only', 'false']
        """
        
        def __init__(self, value: Literal['true', 'plaintext-only', 'false']):
            super().__init__("contenteditable", value)
            


    class dir(BaseAttribute):
        """
        Global Attribute attribute: dir
        Description: The text directionality of the element
        Value: ['ltr', 'rtl', 'auto']
        """
        
        def __init__(self, value: Literal['ltr', 'rtl', 'auto']):
            super().__init__("dir", value)
            


    class draggable(BaseAttribute):
        """
        Global Attribute attribute: draggable
        Description: Whether the element is draggable
        Value: ['true', 'false']
        """
        
        def __init__(self, value: Literal['true', 'false']):
            super().__init__("draggable", value)
            


    class enterkeyhint(BaseAttribute):
        """
        Global Attribute attribute: enterkeyhint
        Description: Hint for selecting an enter key action
        Value: ['enter', 'done', 'go', 'next', 'previous', 'search', 'send']
        """
        
        def __init__(self, value: Literal['enter', 'done', 'go', 'next', 'previous', 'search', 'send']):
            super().__init__("enterkeyhint", value)
            


    class hidden(BaseAttribute):
        """
        Global Attribute attribute: hidden
        Description: Whether the element is relevant
        Value: ['until-found', 'hidden', '']
        """
        
        def __init__(self, value: Literal['until-found', 'hidden', '']):
            super().__init__("hidden", value)
            


    class id(BaseAttribute):
        """
        Global Attribute attribute: id
        Description: The element's ID
        Value: Text*
        """
        
        def __init__(self, value: str):
            super().__init__("id", value)
            


    class inert(BaseAttribute):
        """
        Global Attribute attribute: inert
        Description: Whether the element is inert.
        Value: Boolean attribute
        """
        
        def __init__(self, value: bool):
            super().__init__("inert", value)
            


    class inputmode(BaseAttribute):
        """
        Global Attribute attribute: inputmode
        Description: Hint for selecting an input modality
        Value: ['none', 'text', 'tel', 'email', 'url', 'numeric', 'decimal', 'search']
        """
        
        def __init__(self, value: Literal['none', 'text', 'tel', 'email', 'url', 'numeric', 'decimal', 'search']):
            super().__init__("inputmode", value)
            


    class is_(BaseAttribute):
        """
        Global Attribute attribute: is
        Description: Creates a customized built-in element
        Value: Valid custom element name of a defined customized built-in element
        """
        
        def __init__(self, value):
            super().__init__("is", value)
            


    class itemid(BaseAttribute):
        """
        Global Attribute attribute: itemid
        Description: Global identifier for a microdata item
        Value: Valid URL potentially surrounded by spaces
        """
        
        def __init__(self, value):
            super().__init__("itemid", value)
            


    class itemprop(BaseAttribute):
        """
        Global Attribute attribute: itemprop
        Description: Property names of a microdata item
        Value: Unordered set of unique space-separated tokens consisting of valid absolute URLs, defined property names, or text*
        """
        
        def __init__(self, value):
            super().__init__("itemprop", value)
            


    class itemref(BaseAttribute):
        """
        Global Attribute attribute: itemref
        Description: Referenced elements
        Value: Unordered set of unique space-separated tokens consisting of IDs*
        """
        
        def __init__(self, value):
            super().__init__("itemref", value)
            


    class itemscope(BaseAttribute):
        """
        Global Attribute attribute: itemscope
        Description: Introduces a microdata item
        Value: Boolean attribute
        """
        
        def __init__(self, value: bool):
            super().__init__("itemscope", value)
            


    class itemtype(BaseAttribute):
        """
        Global Attribute attribute: itemtype
        Description: Item types of a microdata item
        Value: Unordered set of unique space-separated tokens consisting of valid absolute URLs*
        """
        
        def __init__(self, value):
            super().__init__("itemtype", value)
            


    class lang(BaseAttribute):
        """
        Global Attribute attribute: lang
        Description: Language of the element
        Value: Valid BCP 47 language tag or the empty string
        """
        
        def __init__(self, value):
            super().__init__("lang", value)
            


    class nonce(BaseAttribute):
        """
        Global Attribute attribute: nonce
        Description: Cryptographic nonce used in Content Security Policy checks [CSP]
        Value: Text
        """
        
        def __init__(self, value: str):
            super().__init__("nonce", value)
            


    class popover(BaseAttribute):
        """
        Global Attribute attribute: popover
        Description: Makes the element a popover element
        Value: ['auto', 'manual']
        """
        
        def __init__(self, value: Literal['auto', 'manual']):
            super().__init__("popover", value)
            


    class slot(BaseAttribute):
        """
        Global Attribute attribute: slot
        Description: The element's desired slot
        Value: Text
        """
        
        def __init__(self, value: str):
            super().__init__("slot", value)
            


    class spellcheck(BaseAttribute):
        """
        Global Attribute attribute: spellcheck
        Description: Whether the element is to have its spelling and grammar checked
        Value: ['true', 'false', '']
        """
        
        def __init__(self, value: Literal['true', 'false', '']):
            super().__init__("spellcheck", value)
            


    class style(BaseAttribute):
        """
        Global Attribute attribute: style
        Description: Presentational and formatting instructions
        Value: CSS declarations*
        """
        
        def __init__(self, value):
            super().__init__("style", value)
            


    class tabindex(BaseAttribute):
        """
        Global Attribute attribute: tabindex
        Description: Whether the element is focusable and sequentially focusable, and the relative order of the element for the purposes of sequential focus navigation
        Value: Valid integer
        """
        
        def __init__(self, value: int):
            super().__init__("tabindex", value)
            


    class title(BaseAttribute):
        """
        Global Attribute attribute: title
        Description: Advisory information for the element
        Value: Text
        """
        
        def __init__(self, value: str):
            super().__init__("title", value)
            


    class translate(BaseAttribute):
        """
        Global Attribute attribute: translate
        Description: Whether the element is to be translated when the page is localized
        Value: ['yes', 'no']
        """
        
        def __init__(self, value: Literal['yes', 'no']):
            super().__init__("translate", value)
            


    class writingsuggestions(BaseAttribute):
        """
        Global Attribute attribute: writingsuggestions
        Description: Whether the element can offer writing suggestions or not.
        Value: ['true', 'false', '']
        """
        
        def __init__(self, value: Literal['true', 'false', '']):
            super().__init__("writingsuggestions", value)
            


    class onauxclick(BaseAttribute):
        """
        Global Attribute attribute: onauxclick
        Description: auxclick event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onauxclick", value)
            


    class onbeforeinput(BaseAttribute):
        """
        Global Attribute attribute: onbeforeinput
        Description: beforeinput event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onbeforeinput", value)
            


    class onbeforematch(BaseAttribute):
        """
        Global Attribute attribute: onbeforematch
        Description: beforematch event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onbeforematch", value)
            


    class onbeforetoggle(BaseAttribute):
        """
        Global Attribute attribute: onbeforetoggle
        Description: beforetoggle event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onbeforetoggle", value)
            


    class onblur(BaseAttribute):
        """
        Global Attribute attribute: onblur
        Description: blur event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onblur", value)
            


    class oncancel(BaseAttribute):
        """
        Global Attribute attribute: oncancel
        Description: cancel event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("oncancel", value)
            


    class oncanplay(BaseAttribute):
        """
        Global Attribute attribute: oncanplay
        Description: canplay event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("oncanplay", value)
            


    class oncanplaythrough(BaseAttribute):
        """
        Global Attribute attribute: oncanplaythrough
        Description: canplaythrough event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("oncanplaythrough", value)
            


    class onchange(BaseAttribute):
        """
        Global Attribute attribute: onchange
        Description: change event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onchange", value)
            


    class onclick(BaseAttribute):
        """
        Global Attribute attribute: onclick
        Description: click event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onclick", value)
            


    class onclose(BaseAttribute):
        """
        Global Attribute attribute: onclose
        Description: close event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onclose", value)
            


    class oncontextlost(BaseAttribute):
        """
        Global Attribute attribute: oncontextlost
        Description: contextlost event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("oncontextlost", value)
            


    class oncontextmenu(BaseAttribute):
        """
        Global Attribute attribute: oncontextmenu
        Description: contextmenu event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("oncontextmenu", value)
            


    class oncontextrestored(BaseAttribute):
        """
        Global Attribute attribute: oncontextrestored
        Description: contextrestored event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("oncontextrestored", value)
            


    class oncopy(BaseAttribute):
        """
        Global Attribute attribute: oncopy
        Description: copy event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("oncopy", value)
            


    class oncuechange(BaseAttribute):
        """
        Global Attribute attribute: oncuechange
        Description: cuechange event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("oncuechange", value)
            


    class oncut(BaseAttribute):
        """
        Global Attribute attribute: oncut
        Description: cut event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("oncut", value)
            


    class ondblclick(BaseAttribute):
        """
        Global Attribute attribute: ondblclick
        Description: dblclick event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("ondblclick", value)
            


    class ondrag(BaseAttribute):
        """
        Global Attribute attribute: ondrag
        Description: drag event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("ondrag", value)
            


    class ondragend(BaseAttribute):
        """
        Global Attribute attribute: ondragend
        Description: dragend event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("ondragend", value)
            


    class ondragenter(BaseAttribute):
        """
        Global Attribute attribute: ondragenter
        Description: dragenter event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("ondragenter", value)
            


    class ondragleave(BaseAttribute):
        """
        Global Attribute attribute: ondragleave
        Description: dragleave event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("ondragleave", value)
            


    class ondragover(BaseAttribute):
        """
        Global Attribute attribute: ondragover
        Description: dragover event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("ondragover", value)
            


    class ondragstart(BaseAttribute):
        """
        Global Attribute attribute: ondragstart
        Description: dragstart event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("ondragstart", value)
            


    class ondrop(BaseAttribute):
        """
        Global Attribute attribute: ondrop
        Description: drop event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("ondrop", value)
            


    class ondurationchange(BaseAttribute):
        """
        Global Attribute attribute: ondurationchange
        Description: durationchange event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("ondurationchange", value)
            


    class onemptied(BaseAttribute):
        """
        Global Attribute attribute: onemptied
        Description: emptied event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onemptied", value)
            


    class onended(BaseAttribute):
        """
        Global Attribute attribute: onended
        Description: ended event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onended", value)
            


    class onerror(BaseAttribute):
        """
        Global Attribute attribute: onerror
        Description: error event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onerror", value)
            


    class onfocus(BaseAttribute):
        """
        Global Attribute attribute: onfocus
        Description: focus event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onfocus", value)
            


    class onformdata(BaseAttribute):
        """
        Global Attribute attribute: onformdata
        Description: formdata event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onformdata", value)
            


    class oninput(BaseAttribute):
        """
        Global Attribute attribute: oninput
        Description: input event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("oninput", value)
            


    class oninvalid(BaseAttribute):
        """
        Global Attribute attribute: oninvalid
        Description: invalid event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("oninvalid", value)
            


    class onkeydown(BaseAttribute):
        """
        Global Attribute attribute: onkeydown
        Description: keydown event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onkeydown", value)
            


    class onkeypress(BaseAttribute):
        """
        Global Attribute attribute: onkeypress
        Description: keypress event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onkeypress", value)
            


    class onkeyup(BaseAttribute):
        """
        Global Attribute attribute: onkeyup
        Description: keyup event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onkeyup", value)
            


    class onload(BaseAttribute):
        """
        Global Attribute attribute: onload
        Description: load event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onload", value)
            


    class onloadeddata(BaseAttribute):
        """
        Global Attribute attribute: onloadeddata
        Description: loadeddata event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onloadeddata", value)
            


    class onloadedmetadata(BaseAttribute):
        """
        Global Attribute attribute: onloadedmetadata
        Description: loadedmetadata event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onloadedmetadata", value)
            


    class onloadstart(BaseAttribute):
        """
        Global Attribute attribute: onloadstart
        Description: loadstart event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onloadstart", value)
            


    class onmousedown(BaseAttribute):
        """
        Global Attribute attribute: onmousedown
        Description: mousedown event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onmousedown", value)
            


    class onmouseenter(BaseAttribute):
        """
        Global Attribute attribute: onmouseenter
        Description: mouseenter event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onmouseenter", value)
            


    class onmouseleave(BaseAttribute):
        """
        Global Attribute attribute: onmouseleave
        Description: mouseleave event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onmouseleave", value)
            


    class onmousemove(BaseAttribute):
        """
        Global Attribute attribute: onmousemove
        Description: mousemove event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onmousemove", value)
            


    class onmouseout(BaseAttribute):
        """
        Global Attribute attribute: onmouseout
        Description: mouseout event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onmouseout", value)
            


    class onmouseover(BaseAttribute):
        """
        Global Attribute attribute: onmouseover
        Description: mouseover event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onmouseover", value)
            


    class onmouseup(BaseAttribute):
        """
        Global Attribute attribute: onmouseup
        Description: mouseup event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onmouseup", value)
            


    class onpaste(BaseAttribute):
        """
        Global Attribute attribute: onpaste
        Description: paste event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onpaste", value)
            


    class onpause(BaseAttribute):
        """
        Global Attribute attribute: onpause
        Description: pause event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onpause", value)
            


    class onplay(BaseAttribute):
        """
        Global Attribute attribute: onplay
        Description: play event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onplay", value)
            


    class onplaying(BaseAttribute):
        """
        Global Attribute attribute: onplaying
        Description: playing event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onplaying", value)
            


    class onprogress(BaseAttribute):
        """
        Global Attribute attribute: onprogress
        Description: progress event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onprogress", value)
            


    class onratechange(BaseAttribute):
        """
        Global Attribute attribute: onratechange
        Description: ratechange event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onratechange", value)
            


    class onreset(BaseAttribute):
        """
        Global Attribute attribute: onreset
        Description: reset event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onreset", value)
            


    class onresize(BaseAttribute):
        """
        Global Attribute attribute: onresize
        Description: resize event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onresize", value)
            


    class onscroll(BaseAttribute):
        """
        Global Attribute attribute: onscroll
        Description: scroll event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onscroll", value)
            


    class onscrollend(BaseAttribute):
        """
        Global Attribute attribute: onscrollend
        Description: scrollend event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onscrollend", value)
            


    class onsecuritypolicyviolation(BaseAttribute):
        """
        Global Attribute attribute: onsecuritypolicyviolation
        Description: securitypolicyviolation event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onsecuritypolicyviolation", value)
            


    class onseeked(BaseAttribute):
        """
        Global Attribute attribute: onseeked
        Description: seeked event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onseeked", value)
            


    class onseeking(BaseAttribute):
        """
        Global Attribute attribute: onseeking
        Description: seeking event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onseeking", value)
            


    class onselect(BaseAttribute):
        """
        Global Attribute attribute: onselect
        Description: select event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onselect", value)
            


    class onslotchange(BaseAttribute):
        """
        Global Attribute attribute: onslotchange
        Description: slotchange event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onslotchange", value)
            


    class onstalled(BaseAttribute):
        """
        Global Attribute attribute: onstalled
        Description: stalled event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onstalled", value)
            


    class onsubmit(BaseAttribute):
        """
        Global Attribute attribute: onsubmit
        Description: submit event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onsubmit", value)
            


    class onsuspend(BaseAttribute):
        """
        Global Attribute attribute: onsuspend
        Description: suspend event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onsuspend", value)
            


    class ontimeupdate(BaseAttribute):
        """
        Global Attribute attribute: ontimeupdate
        Description: timeupdate event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("ontimeupdate", value)
            


    class ontoggle(BaseAttribute):
        """
        Global Attribute attribute: ontoggle
        Description: toggle event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("ontoggle", value)
            


    class onvolumechange(BaseAttribute):
        """
        Global Attribute attribute: onvolumechange
        Description: volumechange event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onvolumechange", value)
            


    class onwaiting(BaseAttribute):
        """
        Global Attribute attribute: onwaiting
        Description: waiting event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onwaiting", value)
            


    class onwheel(BaseAttribute):
        """
        Global Attribute attribute: onwheel
        Description: wheel event handler
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onwheel", value)
            