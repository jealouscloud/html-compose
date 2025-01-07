from . import BaseAttribute
from typing import Union, Callable


class SlotAttrs:
    """
    This module contains classes for attributes in the <slot> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """

    class name(BaseAttribute):
        """
        slot attribute: name
        Description: Name of shadow tree slot
        Value: Text
        """

        def __init__(self, value: Union[str, Callable[[], str]]):
            super().__init__("name", value)
