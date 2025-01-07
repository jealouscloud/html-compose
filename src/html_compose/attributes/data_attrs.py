from . import BaseAttribute
from typing import Union, Callable


class DataAttrs:
    """
    This module contains classes for attributes in the <data> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """

    class value(BaseAttribute):
        """
        data attribute: value
        Description: Machine-readable value
        Value: Text*
        """

        def __init__(self, value: Union[str, Callable[[], str]]):
            super().__init__("value", value)
