from . import BaseAttribute


class LiAttrs:
    """
    This module contains classes for attributes in the <li> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """

    class value(BaseAttribute):
        """
        li attribute: value
        Description: Ordinal value of the list item
        Value: Valid integer
        """

        def __init__(self, value: int):
            super().__init__("value", value)
