from . import BaseAttribute
from typing import Literal
from ..base_types import StrLike


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

        Args:
            value:
                ['utf-8']

        Returns:
            An charset attribute to be added to your element

        """

        return BaseAttribute("charset", value)

    @staticmethod
    def content(value: StrLike) -> BaseAttribute:
        """
        "meta" attribute: content
        Value of the element

        Args:
            value:
                Text*

        Returns:
            An content attribute to be added to your element

        """

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

        Args:
            value:
                ['content-type', 'default-style', 'refresh', 'x-ua-compatible', 'content-security-policy']

        Returns:
            An http-equiv attribute to be added to your element

        """

        return BaseAttribute("http-equiv", value)

    @staticmethod
    def media(value) -> BaseAttribute:
        """
        "meta" attribute: media
        Applicable media

        Args:
            value:
                Valid media query list

        Returns:
            An media attribute to be added to your element

        """

        return BaseAttribute("media", value)

    @staticmethod
    def name(value: StrLike) -> BaseAttribute:
        """
        "meta" attribute: name
        Metadata name

        Args:
            value:
                Text*

        Returns:
            An name attribute to be added to your element

        """

        return BaseAttribute("name", value)
