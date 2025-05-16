from . import BaseAttribute
from typing import Literal


class IframeAttrs:
    """
    This module contains functions for attributes in the 'iframe' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def allow(value) -> BaseAttribute:
        """
        "iframe" attribute: allow  
        Permissions policy to be applied to the iframe's contents  

        :param value: Serialized permissions policy  
        :return: An allow attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("allow", value)

    @staticmethod
    def allowfullscreen(value: bool) -> BaseAttribute:
        """
        "iframe" attribute: allowfullscreen  
        Whether to allow the iframe's contents to use requestFullscreen()  

        :param value: Boolean attribute  
        :return: An allowfullscreen attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("allowfullscreen", value)

    @staticmethod
    def height(value: int) -> BaseAttribute:
        """
        "iframe" attribute: height  
        Vertical dimension  

        :param value: Valid non-negative integer  
        :return: An height attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("height", value)

    @staticmethod
    def loading(value: Literal["lazy", "eager"]) -> BaseAttribute:
        """
        "iframe" attribute: loading  
        Used when determining loading deferral  

        :param value: ['lazy', 'eager']  
        :return: An loading attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("loading", value)

    @staticmethod
    def name(value) -> BaseAttribute:
        """
        "iframe" attribute: name  
        Name of content navigable  

        :param value: Valid navigable target name or keyword  
        :return: An name attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("name", value)

    @staticmethod
    def referrerpolicy(value) -> BaseAttribute:
        """
        "iframe" attribute: referrerpolicy  
        Referrer policy for fetches initiated by the element  

        :param value: Referrer policy  
        :return: An referrerpolicy attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("referrerpolicy", value)

    @staticmethod
    def sandbox(value: list) -> BaseAttribute:
        """
        "iframe" attribute: sandbox  
        Security rules for nested content  

        :param value: Unordered set of unique space-separated tokens, ASCII case-insensitive, consisting of "allow-downloads" "allow-forms" "allow-modals" "allow-orientation-lock" "allow-pointer-lock" "allow-popups" "allow-popups-to-escape-sandbox" "allow-presentation" "allow-same-origin" "allow-scripts" "allow-top-navigation" "allow-top-navigation-by-user-activation" "allow-top-navigation-to-custom-protocols"  
        :return: An sandbox attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("sandbox", value)

    @staticmethod
    def src(value) -> BaseAttribute:
        """
        "iframe" attribute: src  
        Address of the resource  

        :param value: Valid non-empty URL potentially surrounded by spaces  
        :return: An src attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("src", value)

    @staticmethod
    def srcdoc(value) -> BaseAttribute:
        """
        "iframe" attribute: srcdoc  
        A document to render in the iframe  

        :param value: The source of an iframe srcdoc document*  
        :return: An srcdoc attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("srcdoc", value)

    @staticmethod
    def width(value: int) -> BaseAttribute:
        """
        "iframe" attribute: width  
        Horizontal dimension  

        :param value: Valid non-negative integer  
        :return: An width attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("width", value)
