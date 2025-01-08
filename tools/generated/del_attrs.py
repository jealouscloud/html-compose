from . import BaseAttribute
from typing import Literal, Union, Callable

class DelAttrs:
    """ 
    This module contains classes for attributes in the <del> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """ 
    
    class cite(BaseAttribute):
        """
        del attribute: cite
        Description: Link to the source of the quotation or more information about the edit
        Value: Valid URL potentially surrounded by spaces
        """
        
        def __init__(self, value):
            super().__init__("cite", value)
            


    class datetime(BaseAttribute):
        """
        del attribute: datetime
        Description: Date and (optionally) time of the change
        Value: Valid date string with optional time
        """
        
        def __init__(self, value):
            super().__init__("datetime", value)
            