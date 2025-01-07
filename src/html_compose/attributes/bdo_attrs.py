from . import BaseAttribute


class BdoAttrs:
    """
    This module contains classes for attributes in the <bdo> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """

    class dir(BaseAttribute):
        """
        bdo attribute: dir
        Description: The text directionality of the element
        Value: ['ltr', 'rtl']
        """

        def __init__(self, value):
            super().__init__("dir", value)
