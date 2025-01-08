from . import BaseAttribute


class AbbrAttrs:
    """
    This module contains classes for attributes in the <abbr> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """

    class title(BaseAttribute):
        """
        abbr attribute: title
        Description: Full term or expansion of abbreviation
        Value: Text
        """

        def __init__(self, value: str):
            super().__init__("title", value)
