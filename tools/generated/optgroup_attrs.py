from . import BaseAttribute
from typing import Literal, Union, Callable

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
        
        def __init__(self, value: Union[bool, Callable[[], bool]]):
            super().__init__("disabled", value)
            


    class label(BaseAttribute):
        """
        optgroup attribute: label
        Description: User-visible label
        Value: Text
        """
        
        def __init__(self, value: Union[str, Callable[[], str]]):
            super().__init__("label", value)
            