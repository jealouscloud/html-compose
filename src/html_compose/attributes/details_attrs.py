from . import BaseAttribute


class DetailsAttrs:
    """
    This module contains classes for attributes in the <details> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """

    class name(BaseAttribute):
        """
        details attribute: name
        Description: Name of group of mutually-exclusive details elements
        Value: Text*
        """

        def __init__(self, value: str):
            super().__init__("name", value)

    class open(BaseAttribute):
        """
        details attribute: open
        Description: Whether the details are visible
        Value: Boolean attribute
        """

        def __init__(self, value: bool):
            super().__init__("open", value)
