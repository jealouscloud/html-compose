from . import BaseAttribute
from typing import Literal
from ..base_types import Resolvable


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

        Args:
            value:
                Serialized permissions policy

        Returns:
            An allow attribute to be added to your element

        """

        return BaseAttribute("allow", value)

    @staticmethod
    def allowfullscreen(value: bool) -> BaseAttribute:
        """
        "iframe" attribute: allowfullscreen
        Whether to allow the iframe's contents to use requestFullscreen()

        Args:
            value:
                Boolean attribute

        Returns:
            An allowfullscreen attribute to be added to your element

        """

        return BaseAttribute("allowfullscreen", value)

    @staticmethod
    def height(value: int) -> BaseAttribute:
        """
        "iframe" attribute: height
        Vertical dimension

        Args:
            value:
                Valid non-negative integer

        Returns:
            An height attribute to be added to your element

        """

        return BaseAttribute("height", value)

    @staticmethod
    def loading(value: Literal["lazy", "eager"]) -> BaseAttribute:
        """
        "iframe" attribute: loading
        Used when determining loading deferral

        Args:
            value:
                ['lazy', 'eager']

        Returns:
            An loading attribute to be added to your element

        """

        return BaseAttribute("loading", value)

    @staticmethod
    def name(value) -> BaseAttribute:
        """
        "iframe" attribute: name
        Name of content navigable

        Args:
            value:
                Valid navigable target name or keyword

        Returns:
            An name attribute to be added to your element

        """

        return BaseAttribute("name", value)

    @staticmethod
    def referrerpolicy(value) -> BaseAttribute:
        """
        "iframe" attribute: referrerpolicy
        Referrer policy for fetches initiated by the element

        Args:
            value:
                Referrer policy

        Returns:
            An referrerpolicy attribute to be added to your element

        """

        return BaseAttribute("referrerpolicy", value)

    @staticmethod
    def sandbox(value: Resolvable) -> BaseAttribute:
        """
        "iframe" attribute: sandbox
        Security rules for nested content

        Args:
            value:
                Unordered set of unique space-separated tokens, ASCII case-insensitive, consisting of "allow-downloads" "allow-forms" "allow-modals" "allow-orientation-lock" "allow-pointer-lock" "allow-popups" "allow-popups-to-escape-sandbox" "allow-presentation" "allow-same-origin" "allow-scripts" "allow-top-navigation" "allow-top-navigation-by-user-activation" "allow-top-navigation-to-custom-protocols"

        Returns:
            An sandbox attribute to be added to your element

        """

        return BaseAttribute("sandbox", value)

    @staticmethod
    def src(value) -> BaseAttribute:
        """
        "iframe" attribute: src
        Address of the resource

        Args:
            value:
                Valid non-empty URL potentially surrounded by spaces

        Returns:
            An src attribute to be added to your element

        """

        return BaseAttribute("src", value)

    @staticmethod
    def srcdoc(value) -> BaseAttribute:
        """
        "iframe" attribute: srcdoc
        A document to render in the iframe

        Args:
            value:
                The source of an iframe srcdoc document*

        Returns:
            An srcdoc attribute to be added to your element

        """

        return BaseAttribute("srcdoc", value)

    @staticmethod
    def width(value: int) -> BaseAttribute:
        """
        "iframe" attribute: width
        Horizontal dimension

        Args:
            value:
                Valid non-negative integer

        Returns:
            An width attribute to be added to your element

        """

        return BaseAttribute("width", value)
