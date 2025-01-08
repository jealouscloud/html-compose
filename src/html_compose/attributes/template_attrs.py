from . import BaseAttribute


class TemplateAttrs:
    """
    This module contains classes for attributes in the <template> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """

    class shadowrootclonable(BaseAttribute):
        """
        template attribute: shadowrootclonable
        Description: Sets clonable on a declarative shadow root
        Value: Boolean attribute
        """

        def __init__(self, value: bool):
            super().__init__("shadowrootclonable", value)

    class shadowrootdelegatesfocus(BaseAttribute):
        """
        template attribute: shadowrootdelegatesfocus
        Description: Sets delegates focus on a declarative shadow root
        Value: Boolean attribute
        """

        def __init__(self, value: bool):
            super().__init__("shadowrootdelegatesfocus", value)

    class shadowrootmode(BaseAttribute):
        """
        template attribute: shadowrootmode
        Description: Enables streaming declarative shadow roots
        Value: ['open', 'closed']
        """

        def __init__(self, value):
            super().__init__("shadowrootmode", value)

    class shadowrootserializable(BaseAttribute):
        """
        template attribute: shadowrootserializable
        Description: Sets serializable on a declarative shadow root
        Value: Boolean attribute
        """

        def __init__(self, value: bool):
            super().__init__("shadowrootserializable", value)
