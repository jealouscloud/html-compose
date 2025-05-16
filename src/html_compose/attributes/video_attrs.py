from . import BaseAttribute
from typing import Literal


class VideoAttrs:
    """
    This module contains functions for attributes in the 'video' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def autoplay(value: bool) -> BaseAttribute:
        """
        "video" attribute: autoplay  
        Hint that the media resource can be started automatically when the page is loaded  

        :param value: Boolean attribute  
        :return: An autoplay attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("autoplay", value)

    @staticmethod
    def controls(value: bool) -> BaseAttribute:
        """
        "video" attribute: controls  
        Show user agent controls  

        :param value: Boolean attribute  
        :return: An controls attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("controls", value)

    @staticmethod
    def crossorigin(
        value: Literal["anonymous", "use-credentials"],
    ) -> BaseAttribute:
        """
        "video" attribute: crossorigin  
        How the element handles crossorigin requests  

        :param value: ['anonymous', 'use-credentials']  
        :return: An crossorigin attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("crossorigin", value)

    @staticmethod
    def height(value: int) -> BaseAttribute:
        """
        "video" attribute: height  
        Vertical dimension  

        :param value: Valid non-negative integer  
        :return: An height attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("height", value)

    @staticmethod
    def loop(value: bool) -> BaseAttribute:
        """
        "video" attribute: loop  
        Whether to loop the media resource  

        :param value: Boolean attribute  
        :return: An loop attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("loop", value)

    @staticmethod
    def muted(value: bool) -> BaseAttribute:
        """
        "video" attribute: muted  
        Whether to mute the media resource by default  

        :param value: Boolean attribute  
        :return: An muted attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("muted", value)

    @staticmethod
    def playsinline(value: bool) -> BaseAttribute:
        """
        "video" attribute: playsinline  
        Encourage the user agent to display video content within the element's playback area  

        :param value: Boolean attribute  
        :return: An playsinline attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("playsinline", value)

    @staticmethod
    def poster(value) -> BaseAttribute:
        """
        "video" attribute: poster  
        Poster frame to show prior to video playback  

        :param value: Valid non-empty URL potentially surrounded by spaces  
        :return: An poster attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("poster", value)

    @staticmethod
    def preload(value: Literal["none", "metadata", "auto"]) -> BaseAttribute:
        """
        "video" attribute: preload  
        Hints how much buffering the media resource will likely need  

        :param value: ['none', 'metadata', 'auto']  
        :return: An preload attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("preload", value)

    @staticmethod
    def src(value) -> BaseAttribute:
        """
        "video" attribute: src  
        Address of the resource  

        :param value: Valid non-empty URL potentially surrounded by spaces  
        :return: An src attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("src", value)

    @staticmethod
    def width(value: int) -> BaseAttribute:
        """
        "video" attribute: width  
        Horizontal dimension  

        :param value: Valid non-negative integer  
        :return: An width attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("width", value)
