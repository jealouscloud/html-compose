from . import BaseAttribute
from typing import Literal, Union

class StyleAttrs:
    """ 
    This module contains classes for attributes in the <style> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """ 
    
    class blocking(BaseAttribute):
        """
        style attribute: blocking
        Description: Whether the element is potentially render-blocking
        Value: Unordered set of unique space-separated tokens*
        """
        
        def __init__(self, value):
            super().__init__("blocking", value)
            


    class media(BaseAttribute):
        """
        style attribute: media
        Description: Applicable media
        Value: Valid media query list
        """
        
        def __init__(self, value):
            super().__init__("media", value)
            


    class title(BaseAttribute):
        """
        style attribute: title
        Description: CSS style sheet set name
        Value: Text
        """
        
        def __init__(self, value: str):
            super().__init__("title", value)
            