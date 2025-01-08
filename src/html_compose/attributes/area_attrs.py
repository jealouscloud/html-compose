from . import BaseAttribute


class AreaAttrs:
    """
    This module contains classes for attributes in the <area> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """

    class alt(BaseAttribute):
        """
        area attribute: alt
        Description: Replacement text for use when images are not available
        Value: Text*
        """

        def __init__(self, value: str):
            super().__init__("alt", value)

    class coords(BaseAttribute):
        """
        area attribute: coords
        Description: Coordinates for the shape to be created in an image map
        Value: Valid list of floating-point numbers*
        """

        def __init__(self, value):
            super().__init__("coords", value)

    class download(BaseAttribute):
        """
        area attribute: download
        Description: Whether to download the resource instead of navigating to it, and its filename if so
        Value: Text
        """

        def __init__(self, value: str):
            super().__init__("download", value)

    class href(BaseAttribute):
        """
        area attribute: href
        Description: Address of the hyperlink
        Value: Valid URL potentially surrounded by spaces
        """

        def __init__(self, value):
            super().__init__("href", value)

    class ping(BaseAttribute):
        """
        area attribute: ping
        Description: URLs to ping
        Value: Set of space-separated tokens consisting of valid non-empty URLs
        """

        def __init__(self, value):
            super().__init__("ping", value)

    class referrerpolicy(BaseAttribute):
        """
        area attribute: referrerpolicy
        Description: Referrer policy for fetches initiated by the element
        Value: Referrer policy
        """

        def __init__(self, value):
            super().__init__("referrerpolicy", value)

    class rel(BaseAttribute):
        """
        area attribute: rel
        Description: Relationship between the location in the document containing the hyperlink and the destination resource
        Value: Unordered set of unique space-separated tokens*
        """

        def __init__(self, value):
            super().__init__("rel", value)

    class shape(BaseAttribute):
        """
        area attribute: shape
        Description: The kind of shape to be created in an image map
        Value: ['circle', 'default', 'poly', 'rect']
        """

        def __init__(self, value):
            super().__init__("shape", value)

    class target(BaseAttribute):
        """
        area attribute: target
        Description: Navigable for hyperlink navigation
        Value: Valid navigable target name or keyword
        """

        def __init__(self, value):
            super().__init__("target", value)
