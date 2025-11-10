from . import BaseAttribute
from typing import Literal


class TemplateAttrs:
    """
    This module contains functions for attributes in the 'template' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def shadowrootclonable(value: bool) -> BaseAttribute:
        """
        "template" attribute: shadowrootclonable
        Sets clonable on a declarative shadow root

        Args:
            value:
                Boolean attribute

        Returns:
            An shadowrootclonable attribute to be added to your element

        """

        return BaseAttribute("shadowrootclonable", value)

    @staticmethod
    def shadowrootdelegatesfocus(value: bool) -> BaseAttribute:
        """
        "template" attribute: shadowrootdelegatesfocus
        Sets delegates focus on a declarative shadow root

        Args:
            value:
                Boolean attribute

        Returns:
            An shadowrootdelegatesfocus attribute to be added to your element

        """

        return BaseAttribute("shadowrootdelegatesfocus", value)

    @staticmethod
    def shadowrootmode(value: Literal["open", "closed"]) -> BaseAttribute:
        """
        "template" attribute: shadowrootmode
        Enables streaming declarative shadow roots

        Args:
            value:
                ['open', 'closed']

        Returns:
            An shadowrootmode attribute to be added to your element

        """

        return BaseAttribute("shadowrootmode", value)

    @staticmethod
    def shadowrootserializable(value: bool) -> BaseAttribute:
        """
        "template" attribute: shadowrootserializable
        Sets serializable on a declarative shadow root

        Args:
            value:
                Boolean attribute

        Returns:
            An shadowrootserializable attribute to be added to your element

        """

        return BaseAttribute("shadowrootserializable", value)
