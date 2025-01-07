from . import BaseAttribute


class InsAttrs:
    """
    This module contains classes for attributes in the <ins> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """

    class cite(BaseAttribute):
        """
        ins attribute: cite
        Description: Link to the source of the quotation or more information about the edit
        Value: Valid URL potentially surrounded by spaces
        """

        def __init__(self, value):
            super().__init__("cite", value)

    class datetime(BaseAttribute):
        """
        ins attribute: datetime
        Description: Date and (optionally) time of the change
        Value: Valid date string with optional time
        """

        def __init__(self, value):
            super().__init__("datetime", value)
