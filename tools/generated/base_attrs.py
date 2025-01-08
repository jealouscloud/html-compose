from . import BaseAttribute
from typing import Literal, Union

class BaseAttrs:
    """ 
    This module contains classes for attributes in the <base> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """ 
    
    class href(BaseAttribute):
        """
        base attribute: href
        Description: Document base URL
        Value: Valid URL potentially surrounded by spaces
        """
        
        def __init__(self, value):
            super().__init__("href", value)
            


    class target(BaseAttribute):
        """
        base attribute: target
        Description: Default navigable for hyperlink navigation and form submission
        Value: Valid navigable target name or keyword
        """
        
        def __init__(self, value):
            super().__init__("target", value)
            