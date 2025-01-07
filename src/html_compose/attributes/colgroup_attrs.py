from . import BaseAttribute


class ColgroupAttrs:
    """
    This module contains classes for attributes in the <colgroup> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """

    class span(BaseAttribute):
        """
        colgroup attribute: span
        Description: Number of columns spanned by the element
        Value: Valid non-negative integer greater than zero
        """

        def __init__(self, value):
            super().__init__("span", value)
