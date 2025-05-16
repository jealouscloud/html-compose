from . import BaseAttribute
from typing import Literal


class MetaAttrs:
    """
    This module contains functions for attributes in the 'meta' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def charset(value: Literal["utf-8"]) -> BaseAttribute:
        """
        "meta" attribute: charset  
        Character encoding declaration  

        :param value: ['utf-8']  
        :return: An charset attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("charset", value)

    @staticmethod
    def content(value: str) -> BaseAttribute:
        """
        "meta" attribute: content  
        Value of the element  

        :param value: Text*  
        :return: An content attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("content", value)

    @staticmethod
    def http_equiv(
        value: Literal[
            "content-type",
            "default-style",
            "refresh",
            "x-ua-compatible",
            "content-security-policy",
        ],
    ) -> BaseAttribute:
        """
        "meta" attribute: http-equiv  
        Pragma directive  

        :param value: ['content-type', 'default-style', 'refresh', 'x-ua-compatible', 'content-security-policy']  
        :return: An http-equiv attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("http-equiv", value)

    @staticmethod
    def media(value) -> BaseAttribute:
        """
        "meta" attribute: media  
        Applicable media  

        :param value: Valid media query list  
        :return: An media attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("media", value)

    @staticmethod
    def name(value: str) -> BaseAttribute:
        """
        "meta" attribute: name  
        Metadata name  

        :param value: Text*  
        :return: An name attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("name", value)
