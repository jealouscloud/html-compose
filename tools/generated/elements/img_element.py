from typing import Union, Literal, Optional

from ..attributes import GlobalAttrs, AnchorAttrs, AreaAttrs, AudioAttrs, BaseAttrs, BlockquoteAttrs, BodyAttrs, ButtonAttrs, CanvasAttrs, ColAttrs, ColgroupAttrs, DataAttrs, DelAttrs, DetailsAttrs, DialogAttrs, EmbedAttrs, FieldsetAttrs, FormAttrs, IframeAttrs, ImgAttrs, InputAttrs, InsAttrs, LabelAttrs, LiAttrs, LinkAttrs, MapAttrs, MetaAttrs, MeterAttrs, ObjectAttrs, OlAttrs, OptgroupAttrs, OptionAttrs, OutputAttrs, ProgressAttrs, QAttrs, ScriptAttrs, SelectAttrs, SlotAttrs, SourceAttrs, StyleAttrs, TdAttrs, TemplateAttrs, TextareaAttrs, ThAttrs, TimeAttrs, TrackAttrs, VideoAttrs
from ..base_attribute import BaseAttribute
from ..base_element import BaseElement

# This file is generated by tools/generate_elements.py



class img(BaseElement):
    """
    The 'img' element.  
    Description: Image  
    Categories: flow phrasing embedded interactive* form-associated palpable  
    Parents: phrasing picture  
    Children: empty  
    Interface: HTMLImageElement  
    Documentation: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img  
    """ # fmt: skip
    tag = 'img'
    categories = ['flow', 'phrasing', 'embedded', 'interactive*', 'form-associated', 'palpable']
    class hint(GlobalAttrs, ImgAttrs):
        """
        Type hints for "img" attrs  
        This class holds functions which return BaseAttributes  
        Which you can add to your element attrs  
        """ # fmt: skip
        pass
    _ = hint
    def __init__(
        self,
        attrs: Optional[Union[dict[str, Union[str, dict, list]], list[BaseAttribute]]] = None,
        id: Optional[str] = None,
        class_: Optional[Union[str, list]] = None,
        alt: Optional[str] = None,
        crossorigin: Optional[Union[str, Literal['anonymous', 'use-credentials']]] = None,
        decoding: Optional[Union[str, Literal['sync', 'async', 'auto']]] = None,
        fetchpriority: Optional[Union[str, Literal['auto', 'high', 'low']]] = None,
        height: Optional[Union[str, int]] = None,
        ismap: Optional[Union[str, bool]] = None,
        loading: Optional[Union[str, Literal['lazy', 'eager']]] = None,
        referrerpolicy: Optional[str] = None,
        sizes: Optional[str] = None,
        src: Optional[str] = None,
        srcset: Optional[str] = None,
        usemap: Optional[str] = None,
        width: Optional[Union[str, int]] = None,
        accesskey: Optional[Union[str, list]] = None,
        autocapitalize: Optional[Union[str, Literal['on', 'off', 'none', 'sentences', 'words', 'characters']]] = None,
        autocorrect: Optional[Union[str, Literal['on', 'off']]] = None,
        autofocus: Optional[Union[str, bool]] = None,
        contenteditable: Optional[Union[str, Literal['true', 'plaintext-only', 'false']]] = None,
        dir: Optional[Union[str, Literal['ltr', 'rtl', 'auto']]] = None,
        draggable: Optional[Union[str, Literal['true', 'false']]] = None,
        enterkeyhint: Optional[Union[str, Literal['enter', 'done', 'go', 'next', 'previous', 'search', 'send']]] = None,
        hidden: Optional[Union[str, Literal['until-found', 'hidden', '']]] = None,
        inert: Optional[Union[str, bool]] = None,
        inputmode: Optional[Union[str, Literal['none', 'text', 'tel', 'email', 'url', 'numeric', 'decimal', 'search']]] = None,
        is_: Optional[str] = None,
        itemid: Optional[str] = None,
        itemprop: Optional[Union[str, list]] = None,
        itemref: Optional[Union[str, list]] = None,
        itemscope: Optional[Union[str, bool]] = None,
        itemtype: Optional[Union[str, list]] = None,
        lang: Optional[str] = None,
        nonce: Optional[str] = None,
        popover: Optional[Union[str, Literal['auto', 'manual']]] = None,
        slot: Optional[str] = None,
        spellcheck: Optional[Union[str, Literal['true', 'false', '']]] = None,
        style: Optional[str] = None,
        tabindex: Optional[Union[str, int]] = None,
        title: Optional[str] = None,
        translate: Optional[Union[str, Literal['yes', 'no']]] = None,
        writingsuggestions: Optional[Union[str, Literal['true', 'false', '']]] = None,
        children: Optional[list] = None
    ) -> None:
        """
        Initialize 'img' (Image) element.  
        Documentation: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img

        Parameters
        ----------
        `attrs`: 
            A list or dictionary of attributes for the element
        
        `id` :
            The element's ID
        
        `class_` :
            Classes to which the element belongs
        
        `alt` :
            Replacement text for use when images are not available
        
        `crossorigin` :
            How the element handles crossorigin requests
        
        `decoding` :
            Decoding hint to use when processing this image for presentation
        
        `fetchpriority` :
            Sets the priority for fetches initiated by the element
        
        `height` :
            Vertical dimension
        
        `ismap` :
            Whether the image is a server-side image map
        
        `loading` :
            Used when determining loading deferral
        
        `referrerpolicy` :
            Referrer policy for fetches initiated by the element  
            Referrer policy
        
        `sizes` :
            Image sizes for different page layouts  
            Valid source size list
        
        `src` :
            Address of the resource  
            Valid non-empty URL potentially surrounded by spaces
        
        `srcset` :
            Images to use in different situations, e.g., high-resolution displays, small monitors, etc.  
            Comma-separated list of image candidate strings
        
        `usemap` :
            Name of image map to use  
            Valid hash-name reference*
        
        `width` :
            Horizontal dimension
        
        `accesskey` :
            Keyboard shortcut to activate or focus element
        
        `autocapitalize` :
            Recommended autocapitalization behavior (for supported input methods)
        
        `autocorrect` :
            Recommended autocorrection behavior (for supported input methods)
        
        `autofocus` :
            Automatically focus the element when the page is loaded
        
        `contenteditable` :
            Whether the element is editable
        
        `dir` :
            The text directionality of the element
        
        `draggable` :
            Whether the element is draggable
        
        `enterkeyhint` :
            Hint for selecting an enter key action
        
        `hidden` :
            Whether the element is relevant
        
        `inert` :
            Whether the element is inert.
        
        `inputmode` :
            Hint for selecting an input modality
        
        `is_` :
            Creates a customized built-in element  
            Valid custom element name of a defined customized built-in element
        
        `itemid` :
            Global identifier for a microdata item  
            Valid URL potentially surrounded by spaces
        
        `itemprop` :
            Property names of a microdata item
        
        `itemref` :
            Referenced elements
        
        `itemscope` :
            Introduces a microdata item
        
        `itemtype` :
            Item types of a microdata item
        
        `lang` :
            Language of the element  
            Valid BCP 47 language tag or the empty string
        
        `nonce` :
            Cryptographic nonce used in Content Security Policy checks [CSP]
        
        `popover` :
            Makes the element a popover element
        
        `slot` :
            The element's desired slot
        
        `spellcheck` :
            Whether the element is to have its spelling and grammar checked
        
        `style` :
            Presentational and formatting instructions  
            CSS declarations*
        
        `tabindex` :
            Whether the element is focusable and sequentially focusable, and the relative order of the element for the purposes of sequential focus navigation
        
        `title` :
            Advisory information for the element
        
        `translate` :
            Whether the element is to be translated when the page is localized
        
        `writingsuggestions` :
            Whether the element can offer writing suggestions or not.
        
        """ #fmt: skip
        super().__init__(
            "img",
            void_element=True,
            attrs=attrs,
            children=children
        )
        if not (id is None or id is False):
            self._process_attr("id", id)
        if not (class_ is None or class_ is False):
            self._process_attr("class", class_)
        if not (alt is None or alt is False):
            self._process_attr("alt", alt)
        if not (crossorigin is None or crossorigin is False):
            self._process_attr("crossorigin", crossorigin)
        if not (decoding is None or decoding is False):
            self._process_attr("decoding", decoding)
        if not (fetchpriority is None or fetchpriority is False):
            self._process_attr("fetchpriority", fetchpriority)
        if not (height is None or height is False):
            self._process_attr("height", height)
        if not (ismap is None or ismap is False):
            self._process_attr("ismap", ismap)
        if not (loading is None or loading is False):
            self._process_attr("loading", loading)
        if not (referrerpolicy is None or referrerpolicy is False):
            self._process_attr("referrerpolicy", referrerpolicy)
        if not (sizes is None or sizes is False):
            self._process_attr("sizes", sizes)
        if not (src is None or src is False):
            self._process_attr("src", src)
        if not (srcset is None or srcset is False):
            self._process_attr("srcset", srcset)
        if not (usemap is None or usemap is False):
            self._process_attr("usemap", usemap)
        if not (width is None or width is False):
            self._process_attr("width", width)
        if not (accesskey is None or accesskey is False):
            self._process_attr("accesskey", accesskey)
        if not (autocapitalize is None or autocapitalize is False):
            self._process_attr("autocapitalize", autocapitalize)
        if not (autocorrect is None or autocorrect is False):
            self._process_attr("autocorrect", autocorrect)
        if not (autofocus is None or autofocus is False):
            self._process_attr("autofocus", autofocus)
        if not (contenteditable is None or contenteditable is False):
            self._process_attr("contenteditable", contenteditable)
        if not (dir is None or dir is False):
            self._process_attr("dir", dir)
        if not (draggable is None or draggable is False):
            self._process_attr("draggable", draggable)
        if not (enterkeyhint is None or enterkeyhint is False):
            self._process_attr("enterkeyhint", enterkeyhint)
        if not (hidden is None or hidden is False):
            self._process_attr("hidden", hidden)
        if not (inert is None or inert is False):
            self._process_attr("inert", inert)
        if not (inputmode is None or inputmode is False):
            self._process_attr("inputmode", inputmode)
        if not (is_ is None or is_ is False):
            self._process_attr("is", is_)
        if not (itemid is None or itemid is False):
            self._process_attr("itemid", itemid)
        if not (itemprop is None or itemprop is False):
            self._process_attr("itemprop", itemprop)
        if not (itemref is None or itemref is False):
            self._process_attr("itemref", itemref)
        if not (itemscope is None or itemscope is False):
            self._process_attr("itemscope", itemscope)
        if not (itemtype is None or itemtype is False):
            self._process_attr("itemtype", itemtype)
        if not (lang is None or lang is False):
            self._process_attr("lang", lang)
        if not (nonce is None or nonce is False):
            self._process_attr("nonce", nonce)
        if not (popover is None or popover is False):
            self._process_attr("popover", popover)
        if not (slot is None or slot is False):
            self._process_attr("slot", slot)
        if not (spellcheck is None or spellcheck is False):
            self._process_attr("spellcheck", spellcheck)
        if not (style is None or style is False):
            self._process_attr("style", style)
        if not (tabindex is None or tabindex is False):
            self._process_attr("tabindex", tabindex)
        if not (title is None or title is False):
            self._process_attr("title", title)
        if not (translate is None or translate is False):
            self._process_attr("translate", translate)
        if not (writingsuggestions is None or writingsuggestions is False):
            self._process_attr("writingsuggestions", writingsuggestions)