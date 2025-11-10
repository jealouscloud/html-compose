from . import BaseAttribute


class BaseAttrs:
    """
    This module contains functions for attributes in the 'base' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def href(value) -> BaseAttribute:
        """
        "base" attribute: href
        Document base URL

        Args:
            value:
                Valid URL potentially surrounded by spaces

        Returns:
            An href attribute to be added to your element

        """

        return BaseAttribute("href", value)

    @staticmethod
    def target(value) -> BaseAttribute:
        """
        "base" attribute: target
        Default navigable for hyperlink navigation and form submission

        Args:
            value:
                Valid navigable target name or keyword

        Returns:
            An target attribute to be added to your element

        """

        return BaseAttribute("target", value)
