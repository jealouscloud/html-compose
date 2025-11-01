from . import BaseAttribute


class ProgressAttrs:
    """
    This module contains functions for attributes in the 'progress' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def max(value: float) -> BaseAttribute:
        """
        "progress" attribute: max
        Upper bound of range

        Args:
            value:
                Valid floating-point number*

        Returns:
            An max attribute to be added to your element

        """

        return BaseAttribute("max", value)

    @staticmethod
    def value(value: float) -> BaseAttribute:
        """
        "progress" attribute: value
        Current value of the element

        Args:
            value:
                Valid floating-point number

        Returns:
            An value attribute to be added to your element

        """

        return BaseAttribute("value", value)
