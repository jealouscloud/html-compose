from . import BaseAttribute


class ObjectAttrs:
    """
    This module contains classes for attributes in the <object> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """

    class data(BaseAttribute):
        """
        object attribute: data
        Description: Address of the resource
        Value: Valid non-empty URL potentially surrounded by spaces
        """

        def __init__(self, value):
            super().__init__("data", value)

    class form(BaseAttribute):
        """
        object attribute: form
        Description: Associates the element with a form element
        Value: ID*
        """

        def __init__(self, value):
            super().__init__("form", value)

    class height(BaseAttribute):
        """
        object attribute: height
        Description: Vertical dimension
        Value: Valid non-negative integer
        """

        def __init__(self, value: int):
            super().__init__("height", value)

    class name(BaseAttribute):
        """
        object attribute: name
        Description: Name of content navigable
        Value: Valid navigable target name or keyword
        """

        def __init__(self, value):
            super().__init__("name", value)

    class type(BaseAttribute):
        """
        object attribute: type
        Description: Type of embedded resource
        Value: Valid MIME type string
        """

        def __init__(self, value):
            super().__init__("type", value)

    class width(BaseAttribute):
        """
        object attribute: width
        Description: Horizontal dimension
        Value: Valid non-negative integer
        """

        def __init__(self, value: int):
            super().__init__("width", value)
