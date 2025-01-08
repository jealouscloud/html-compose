from . import BaseAttribute
from typing import Literal, Union

class OutputAttrs:
    """ 
    This module contains classes for attributes in the <output> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """ 
    
    class for_(BaseAttribute):
        """
        output attribute: for
        Description: Specifies controls from which the output was calculated
        Value: Unordered set of unique space-separated tokens consisting of IDs*
        """
        
        def __init__(self, value):
            super().__init__("for", value)
            


    class form(BaseAttribute):
        """
        output attribute: form
        Description: Associates the element with a form element
        Value: ID*
        """
        
        def __init__(self, value):
            super().__init__("form", value)
            


    class name(BaseAttribute):
        """
        output attribute: name
        Description: Name of the element to use for form submission and in the form.elements API
        Value: Text*
        """
        
        def __init__(self, value: str):
            super().__init__("name", value)
            