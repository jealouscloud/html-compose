from . import BaseAttribute
from typing import Literal


class ImgAttrs:
    """
    This module contains functions for attributes in the 'img' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def alt(value: str) -> BaseAttribute:
        """
        "img" attribute: alt  
        Replacement text for use when images are not available  

        :param value: Text*  
        :return: An alt attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("alt", value)

    @staticmethod
    def crossorigin(
        value: Literal["anonymous", "use-credentials"],
    ) -> BaseAttribute:
        """
        "img" attribute: crossorigin  
        How the element handles crossorigin requests  

        :param value: ['anonymous', 'use-credentials']  
        :return: An crossorigin attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("crossorigin", value)

    @staticmethod
    def decoding(value: Literal["sync", "async", "auto"]) -> BaseAttribute:
        """
        "img" attribute: decoding  
        Decoding hint to use when processing this image for presentation  

        :param value: ['sync', 'async', 'auto']  
        :return: An decoding attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("decoding", value)

    @staticmethod
    def fetchpriority(value: Literal["auto", "high", "low"]) -> BaseAttribute:
        """
        "img" attribute: fetchpriority  
        Sets the priority for fetches initiated by the element  

        :param value: ['auto', 'high', 'low']  
        :return: An fetchpriority attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("fetchpriority", value)

    @staticmethod
    def height(value: int) -> BaseAttribute:
        """
        "img" attribute: height  
        Vertical dimension  

        :param value: Valid non-negative integer  
        :return: An height attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("height", value)

    @staticmethod
    def ismap(value: bool) -> BaseAttribute:
        """
        "img" attribute: ismap  
        Whether the image is a server-side image map  

        :param value: Boolean attribute  
        :return: An ismap attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("ismap", value)

    @staticmethod
    def loading(value: Literal["lazy", "eager"]) -> BaseAttribute:
        """
        "img" attribute: loading  
        Used when determining loading deferral  

        :param value: ['lazy', 'eager']  
        :return: An loading attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("loading", value)

    @staticmethod
    def referrerpolicy(value) -> BaseAttribute:
        """
        "img" attribute: referrerpolicy  
        Referrer policy for fetches initiated by the element  

        :param value: Referrer policy  
        :return: An referrerpolicy attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("referrerpolicy", value)

    @staticmethod
    def sizes(value) -> BaseAttribute:
        """
        "img" attribute: sizes  
        Image sizes for different page layouts  

        :param value: Valid source size list  
        :return: An sizes attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("sizes", value)

    @staticmethod
    def src(value) -> BaseAttribute:
        """
        "img" attribute: src  
        Address of the resource  

        :param value: Valid non-empty URL potentially surrounded by spaces  
        :return: An src attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("src", value)

    @staticmethod
    def srcset(value) -> BaseAttribute:
        """
        "img" attribute: srcset  
        Images to use in different situations, e.g., high-resolution displays, small monitors, etc.  

        :param value: Comma-separated list of image candidate strings  
        :return: An srcset attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("srcset", value)

    @staticmethod
    def usemap(value) -> BaseAttribute:
        """
        "img" attribute: usemap  
        Name of image map to use  

        :param value: Valid hash-name reference*  
        :return: An usemap attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("usemap", value)

    @staticmethod
    def width(value: int) -> BaseAttribute:
        """
        "img" attribute: width  
        Horizontal dimension  

        :param value: Valid non-negative integer  
        :return: An width attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("width", value)
