from . import BaseAttribute


class IframeAttrs:
    """
    This module contains classes for attributes in the <iframe> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """

    class allow(BaseAttribute):
        """
        iframe attribute: allow
        Description: Permissions policy to be applied to the iframe's contents
        Value: Serialized permissions policy
        """

        def __init__(self, value):
            super().__init__("allow", value)

    class allowfullscreen(BaseAttribute):
        """
        iframe attribute: allowfullscreen
        Description: Whether to allow the iframe's contents to use requestFullscreen()
        Value: Boolean attribute
        """

        def __init__(self, value: bool):
            super().__init__("allowfullscreen", value)

    class height(BaseAttribute):
        """
        iframe attribute: height
        Description: Vertical dimension
        Value: Valid non-negative integer
        """

        def __init__(self, value: int):
            super().__init__("height", value)

    class loading(BaseAttribute):
        """
        iframe attribute: loading
        Description: Used when determining loading deferral
        Value: ['lazy', 'eager']
        """

        def __init__(self, value):
            super().__init__("loading", value)

    class name(BaseAttribute):
        """
        iframe attribute: name
        Description: Name of content navigable
        Value: Valid navigable target name or keyword
        """

        def __init__(self, value):
            super().__init__("name", value)

    class referrerpolicy(BaseAttribute):
        """
        iframe attribute: referrerpolicy
        Description: Referrer policy for fetches initiated by the element
        Value: Referrer policy
        """

        def __init__(self, value):
            super().__init__("referrerpolicy", value)

    class sandbox(BaseAttribute):
        """
        iframe attribute: sandbox
        Description: Security rules for nested content
        Value: Unordered set of unique space-separated tokens, ASCII case-insensitive, consisting of "allow-downloads" "allow-forms" "allow-modals" "allow-orientation-lock" "allow-pointer-lock" "allow-popups" "allow-popups-to-escape-sandbox" "allow-presentation" "allow-same-origin" "allow-scripts" "allow-top-navigation" "allow-top-navigation-by-user-activation" "allow-top-navigation-to-custom-protocols"
        """

        def __init__(self, value):
            super().__init__("sandbox", value)

    class src(BaseAttribute):
        """
        iframe attribute: src
        Description: Address of the resource
        Value: Valid non-empty URL potentially surrounded by spaces
        """

        def __init__(self, value):
            super().__init__("src", value)

    class srcdoc(BaseAttribute):
        """
        iframe attribute: srcdoc
        Description: A document to render in the iframe
        Value: The source of an iframe srcdoc document*
        """

        def __init__(self, value):
            super().__init__("srcdoc", value)

    class width(BaseAttribute):
        """
        iframe attribute: width
        Description: Horizontal dimension
        Value: Valid non-negative integer
        """

        def __init__(self, value: int):
            super().__init__("width", value)
