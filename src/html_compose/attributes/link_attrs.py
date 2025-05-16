from . import BaseAttribute
from typing import Literal


class LinkAttrs:
    """
    This module contains functions for attributes in the 'link' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def as_(value) -> BaseAttribute:
        """
        "link" attribute: as  
        Potential destination for a preload request (for rel="preload" and rel="modulepreload")  

        :param value: Potential destination, for rel="preload"; script-like destination, for rel="modulepreload"  
        :return: An as attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("as", value)

    @staticmethod
    def blocking(value: list) -> BaseAttribute:
        """
        "link" attribute: blocking  
        Whether the element is potentially render-blocking  

        :param value: Unordered set of unique space-separated tokens*  
        :return: An blocking attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("blocking", value)

    @staticmethod
    def color(value) -> BaseAttribute:
        """
        "link" attribute: color  
        Color to use when customizing a site's icon (for rel="mask-icon")  

        :param value: CSS <color>  
        :return: An color attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("color", value)

    @staticmethod
    def crossorigin(
        value: Literal["anonymous", "use-credentials"],
    ) -> BaseAttribute:
        """
        "link" attribute: crossorigin  
        How the element handles crossorigin requests  

        :param value: ['anonymous', 'use-credentials']  
        :return: An crossorigin attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("crossorigin", value)

    @staticmethod
    def disabled(value: bool) -> BaseAttribute:
        """
        "link" attribute: disabled  
        Whether the link is disabled  

        :param value: Boolean attribute  
        :return: An disabled attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("disabled", value)

    @staticmethod
    def fetchpriority(value: Literal["auto", "high", "low"]) -> BaseAttribute:
        """
        "link" attribute: fetchpriority  
        Sets the priority for fetches initiated by the element  

        :param value: ['auto', 'high', 'low']  
        :return: An fetchpriority attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("fetchpriority", value)

    @staticmethod
    def href(value) -> BaseAttribute:
        """
        "link" attribute: href  
        Address of the hyperlink  

        :param value: Valid non-empty URL potentially surrounded by spaces  
        :return: An href attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("href", value)

    @staticmethod
    def hreflang(value) -> BaseAttribute:
        """
        "link" attribute: hreflang  
        Language of the linked resource  

        :param value: Valid BCP 47 language tag  
        :return: An hreflang attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("hreflang", value)

    @staticmethod
    def imagesizes(value) -> BaseAttribute:
        """
        "link" attribute: imagesizes  
        Image sizes for different page layouts (for rel="preload")  

        :param value: Valid source size list  
        :return: An imagesizes attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("imagesizes", value)

    @staticmethod
    def imagesrcset(value) -> BaseAttribute:
        """
        "link" attribute: imagesrcset  
        Images to use in different situations, e.g., high-resolution displays, small monitors, etc. (for rel="preload")  

        :param value: Comma-separated list of image candidate strings  
        :return: An imagesrcset attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("imagesrcset", value)

    @staticmethod
    def integrity(value: str) -> BaseAttribute:
        """
        "link" attribute: integrity  
        Integrity metadata used in Subresource Integrity checks [SRI]  

        :param value: Text  
        :return: An integrity attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("integrity", value)

    @staticmethod
    def media(value) -> BaseAttribute:
        """
        "link" attribute: media  
        Applicable media  

        :param value: Valid media query list  
        :return: An media attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("media", value)

    @staticmethod
    def referrerpolicy(value) -> BaseAttribute:
        """
        "link" attribute: referrerpolicy  
        Referrer policy for fetches initiated by the element  

        :param value: Referrer policy  
        :return: An referrerpolicy attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("referrerpolicy", value)

    @staticmethod
    def rel(value: list) -> BaseAttribute:
        """
        "link" attribute: rel  
        Relationship between the document containing the hyperlink and the destination resource  

        :param value: Unordered set of unique space-separated tokens*  
        :return: An rel attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("rel", value)

    @staticmethod
    def sizes(value: list) -> BaseAttribute:
        """
        "link" attribute: sizes  
        Sizes of the icons (for rel="icon")  

        :param value: Unordered set of unique space-separated tokens, ASCII case-insensitive, consisting of sizes*  
        :return: An sizes attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("sizes", value)

    @staticmethod
    def title(value) -> BaseAttribute:
        """
        "link" attribute: title  
        Title of the link  OR  CSS style sheet set name  

        :param value: Text  OR  Text  
        :return: An title attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("title", value)

    @staticmethod
    def type(value) -> BaseAttribute:
        """
        "link" attribute: type  
        Hint for the type of the referenced resource  

        :param value: Valid MIME type string  
        :return: An type attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("type", value)
