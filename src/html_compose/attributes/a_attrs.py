from . import BaseAttribute
from ..base_types import Resolvable, StrLike


class AnchorAttrs:
    """
    This module contains functions for attributes in the 'a' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def download(value: StrLike) -> BaseAttribute:
        """
        "a" attribute: download
        Whether to download the resource instead of navigating to it, and its filename if so

        Args:
            value:
                Text

        Returns:
            An download attribute to be added to your element

        """

        return BaseAttribute("download", value)

    @staticmethod
    def href(value) -> BaseAttribute:
        """
        "a" attribute: href
        Address of the hyperlink

        Args:
            value:
                Valid URL potentially surrounded by spaces

        Returns:
            An href attribute to be added to your element

        """

        return BaseAttribute("href", value)

    @staticmethod
    def hreflang(value) -> BaseAttribute:
        """
        "a" attribute: hreflang
        Language of the linked resource

        Args:
            value:
                Valid BCP 47 language tag

        Returns:
            An hreflang attribute to be added to your element

        """

        return BaseAttribute("hreflang", value)

    @staticmethod
    def ping(value: Resolvable) -> BaseAttribute:
        """
        "a" attribute: ping
        URLs to ping

        Args:
            value:
                Set of space-separated tokens consisting of valid non-empty URLs

        Returns:
            An ping attribute to be added to your element

        """

        return BaseAttribute("ping", value)

    @staticmethod
    def referrerpolicy(value) -> BaseAttribute:
        """
        "a" attribute: referrerpolicy
        Referrer policy for fetches initiated by the element

        Args:
            value:
                Referrer policy

        Returns:
            An referrerpolicy attribute to be added to your element

        """

        return BaseAttribute("referrerpolicy", value)

    @staticmethod
    def rel(value: Resolvable) -> BaseAttribute:
        """
        "a" attribute: rel
        Relationship between the location in the document containing the hyperlink and the destination resource

        Args:
            value:
                Unordered set of unique space-separated tokens*

        Returns:
            An rel attribute to be added to your element

        """

        return BaseAttribute("rel", value)

    @staticmethod
    def target(value) -> BaseAttribute:
        """
        "a" attribute: target
        Navigable for hyperlink navigation

        Args:
            value:
                Valid navigable target name or keyword

        Returns:
            An target attribute to be added to your element

        """

        return BaseAttribute("target", value)

    @staticmethod
    def type(value) -> BaseAttribute:
        """
        "a" attribute: type
        Hint for the type of the referenced resource

        Args:
            value:
                Valid MIME type string

        Returns:
            An type attribute to be added to your element

        """

        return BaseAttribute("type", value)
