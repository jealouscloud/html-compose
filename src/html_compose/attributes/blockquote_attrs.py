from . import BaseAttribute


class BlockquoteAttrs:
    """
    This module contains classes for attributes in the <blockquote> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """

    class cite(BaseAttribute):
        """
        blockquote attribute: cite
        Description: Link to the source of the quotation or more information about the edit
        Value: Valid URL potentially surrounded by spaces
        """

        def __init__(self, value):
            super().__init__("cite", value)
