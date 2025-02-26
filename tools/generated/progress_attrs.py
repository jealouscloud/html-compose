from . import BaseAttribute
from typing import Literal, Union

class ProgressAttrs:
    """ 
    This module contains classes for attributes in the <progress> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """ 
    
    class max(BaseAttribute):
        """
        progress attribute: max
        Description: Upper bound of range
        Value: Valid floating-point number*
        """
        
        def __init__(self, value: float):
            super().__init__("max", value)
            


    class value(BaseAttribute):
        """
        progress attribute: value
        Description: Current value of the element
        Value: Valid floating-point number
        """
        
        def __init__(self, value: float):
            super().__init__("value", value)
            