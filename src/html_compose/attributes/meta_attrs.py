from . import BaseAttribute


class MetaAttrs:
    """
    This module contains classes for attributes in the <meta> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """

    class charset(BaseAttribute):
        """
        meta attribute: charset
        Description: Character encoding declaration
        Value: ['utf-8']
        """

        def __init__(self, value):
            super().__init__("charset", value)

    class content(BaseAttribute):
        """
        meta attribute: content
        Description: Value of the element
        Value: Text*
        """

        def __init__(self, value: str):
            super().__init__("content", value)

    class http_equiv(BaseAttribute):
        """
        meta attribute: http-equiv
        Description: Pragma directive
        Value: ['content-type', 'default-style', 'refresh', 'x-ua-compatible', 'content-security-policy']
        """

        def __init__(self, value):
            super().__init__("http-equiv", value)

    class media(BaseAttribute):
        """
        meta attribute: media
        Description: Applicable media
        Value: Valid media query list
        """

        def __init__(self, value):
            super().__init__("media", value)

    class name(BaseAttribute):
        """
        meta attribute: name
        Description: Metadata name
        Value: Text*
        """

        def __init__(self, value: str):
            super().__init__("name", value)
