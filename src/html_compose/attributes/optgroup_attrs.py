from . import BaseAttribute


class OptgroupAttrs:
    """
    This module contains classes for attributes in the <optgroup> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """

    class disabled(BaseAttribute):
        """
        optgroup attribute: disabled
        Description: Whether the form control is disabled
        Value: Boolean attribute
        """

        def __init__(self, value: bool):
            super().__init__("disabled", value)

    class label(BaseAttribute):
        """
        optgroup attribute: label
        Description: User-visible label
        Value: Text
        """

        def __init__(self, value: str):
            super().__init__("label", value)
