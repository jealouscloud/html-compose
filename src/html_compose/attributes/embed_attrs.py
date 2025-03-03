from . import BaseAttribute


class EmbedAttrs:
    """
    This module contains classes for attributes in the <embed> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """

    class height(BaseAttribute):
        """
        embed attribute: height
        Description: Vertical dimension
        Value: Valid non-negative integer
        """

        def __init__(self, value: int):
            super().__init__("height", value)

    class src(BaseAttribute):
        """
        embed attribute: src
        Description: Address of the resource
        Value: Valid non-empty URL potentially surrounded by spaces
        """

        def __init__(self, value):
            super().__init__("src", value)

    class type(BaseAttribute):
        """
        embed attribute: type
        Description: Type of embedded resource
        Value: Valid MIME type string
        """

        def __init__(self, value):
            super().__init__("type", value)

    class width(BaseAttribute):
        """
        embed attribute: width
        Description: Horizontal dimension
        Value: Valid non-negative integer
        """

        def __init__(self, value: int):
            super().__init__("width", value)
