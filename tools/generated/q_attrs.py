from . import BaseAttribute
from typing import Literal, Union

class QAttrs:
    """ 
    This module contains classes for attributes in the <q> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """ 
    
    class cite(BaseAttribute):
        """
        q attribute: cite
        Description: Link to the source of the quotation or more information about the edit
        Value: Valid URL potentially surrounded by spaces
        """
        
        def __init__(self, value):
            super().__init__("cite", value)
            