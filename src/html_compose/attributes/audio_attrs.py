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

        Args:
            value:
                Boolean attribute

        Returns:
            An autoplay attribute to be added to your element

        """

        return BaseAttribute("autoplay", value)

    @staticmethod
    def controls(value: bool) -> BaseAttribute:
        """
        "audio" attribute: controls
        Show user agent controls

        Args:
            value:
                Boolean attribute

        Returns:
            An controls attribute to be added to your element

        """

        return BaseAttribute("controls", value)

    @staticmethod
    def crossorigin(
        value: Literal["anonymous", "use-credentials"],
    ) -> BaseAttribute:
        """
        "audio" attribute: crossorigin
        How the element handles crossorigin requests

        Args:
            value:
                ['anonymous', 'use-credentials']

        Returns:
            An crossorigin attribute to be added to your element

        """

        return BaseAttribute("crossorigin", value)

    @staticmethod
    def loop(value: bool) -> BaseAttribute:
        """
        "audio" attribute: loop
        Whether to loop the media resource

        Args:
            value:
                Boolean attribute

        Returns:
            An loop attribute to be added to your element

        """

        return BaseAttribute("loop", value)

    @staticmethod
    def muted(value: bool) -> BaseAttribute:
        """
        "audio" attribute: muted
        Whether to mute the media resource by default

        Args:
            value:
                Boolean attribute

        Returns:
            An muted attribute to be added to your element

        """

        return BaseAttribute("muted", value)

    @staticmethod
    def preload(value: Literal["none", "metadata", "auto"]) -> BaseAttribute:
        """
        "audio" attribute: preload
        Hints how much buffering the media resource will likely need

        Args:
            value:
                ['none', 'metadata', 'auto']

        Returns:
            An preload attribute to be added to your element

        """

        return BaseAttribute("preload", value)

    @staticmethod
    def src(value) -> BaseAttribute:
        """
        "audio" attribute: src
        Address of the resource

        Args:
            value:
                Valid non-empty URL potentially surrounded by spaces

        Returns:
            An src attribute to be added to your element

        """

        return BaseAttribute("src", value)
