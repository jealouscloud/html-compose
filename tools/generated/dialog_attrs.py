from . import BaseAttribute
from typing import Literal, Union

class DialogAttrs:
    """ 
    This module contains classes for attributes in the <dialog> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """ 
    
    class open(BaseAttribute):
        """
        dialog attribute: open
        Description: Whether the dialog box is showing
        Value: Boolean attribute
        """
        
        def __init__(self, value: bool):
            super().__init__("open", value)
            