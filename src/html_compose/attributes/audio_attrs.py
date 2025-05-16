from . import BaseAttribute
from typing import Literal


class AudioAttrs:
    """
    This module contains functions for attributes in the 'audio' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def autoplay(value: bool) -> BaseAttribute:
        """
        "audio" attribute: autoplay  
        Hint that the media resource can be started automatically when the page is loaded  

        :param value: Boolean attribute  
        :return: An autoplay attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("autoplay", value)

    @staticmethod
    def controls(value: bool) -> BaseAttribute:
        """
        "audio" attribute: controls  
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
        "audio" attribute: crossorigin  
        How the element handles crossorigin requests  

        :param value: ['anonymous', 'use-credentials']  
        :return: An crossorigin attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("crossorigin", value)

    @staticmethod
    def loop(value: bool) -> BaseAttribute:
        """
        "audio" attribute: loop  
        Whether to loop the media resource  

        :param value: Boolean attribute  
        :return: An loop attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("loop", value)

    @staticmethod
    def muted(value: bool) -> BaseAttribute:
        """
        "audio" attribute: muted  
        Whether to mute the media resource by default  

        :param value: Boolean attribute  
        :return: An muted attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("muted", value)

    @staticmethod
    def preload(value: Literal["none", "metadata", "auto"]) -> BaseAttribute:
        """
        "audio" attribute: preload  
        Hints how much buffering the media resource will likely need  

        :param value: ['none', 'metadata', 'auto']  
        :return: An preload attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("preload", value)

    @staticmethod
    def src(value) -> BaseAttribute:
        """
        "audio" attribute: src  
        Address of the resource  

        :param value: Valid non-empty URL potentially surrounded by spaces  
        :return: An src attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("src", value)
