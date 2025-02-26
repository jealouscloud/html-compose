from . import BaseAttribute
from typing import Literal, Union

class OlAttrs:
    """ 
    This module contains classes for attributes in the <ol> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """ 
    
    class reversed(BaseAttribute):
        """
        ol attribute: reversed
        Description: Number the list backwards
        Value: Boolean attribute
        """
        
        def __init__(self, value: bool):
            super().__init__("reversed", value)
            


    class start(BaseAttribute):
        """
        ol attribute: start
        Description: Starting value of the list
        Value: Valid integer
        """
        
        def __init__(self, value: int):
            super().__init__("start", value)
            


    class type(BaseAttribute):
        """
        ol attribute: type
        Description: Kind of list marker
        Value: ['1', 'a', 'A', 'i', 'I']
        """
        
        def __init__(self, value):
            super().__init__("type", value)
            