from . import BaseAttribute
from typing import Literal, Union

class LabelAttrs:
    """ 
    This module contains classes for attributes in the <label> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """ 
    
    class for_(BaseAttribute):
        """
        label attribute: for
        Description: Associate the label with form control
        Value: ID*
        """
        
        def __init__(self, value):
            super().__init__("for", value)
            