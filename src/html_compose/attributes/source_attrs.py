from . import BaseAttribute


class SourceAttrs:
    """
    This module contains classes for attributes in the <source> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """

    class height(BaseAttribute):
        """
        source attribute: height
        Description: Vertical dimension
        Value: Valid non-negative integer
        """

        def __init__(self, value: int):
            super().__init__("height", value)

    class media(BaseAttribute):
        """
        source attribute: media
        Description: Applicable media
        Value: Valid media query list
        """

        def __init__(self, value):
            super().__init__("media", value)

    class sizes(BaseAttribute):
        """
        source attribute: sizes
        Description: Image sizes for different page layouts
        Value: Valid source size list
        """

        def __init__(self, value):
            super().__init__("sizes", value)

    class src(BaseAttribute):
        """
        source attribute: src
        Description: Address of the resource
        Value: Valid non-empty URL potentially surrounded by spaces
        """

        def __init__(self, value):
            super().__init__("src", value)

    class srcset(BaseAttribute):
        """
        source attribute: srcset
        Description: Images to use in different situations, e.g., high-resolution displays, small monitors, etc.
        Value: Comma-separated list of image candidate strings
        """

        def __init__(self, value):
            super().__init__("srcset", value)

    class type(BaseAttribute):
        """
        source attribute: type
        Description: Type of embedded resource
        Value: Valid MIME type string
        """

        def __init__(self, value):
            super().__init__("type", value)

    class width(BaseAttribute):
        """
        source attribute: width
        Description: Horizontal dimension
        Value: Valid non-negative integer
        """

        def __init__(self, value: int):
            super().__init__("width", value)
