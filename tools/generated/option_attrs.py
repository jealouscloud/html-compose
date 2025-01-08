from . import BaseAttribute
from typing import Literal, Union

class OptionAttrs:
    """ 
    This module contains classes for attributes in the <option> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """ 
    
    class disabled(BaseAttribute):
        """
        option attribute: disabled
        Description: Whether the form control is disabled
        Value: Boolean attribute
        """
        
        def __init__(self, value: bool):
            super().__init__("disabled", value)
            


    class label(BaseAttribute):
        """
        option attribute: label
        Description: User-visible label
        Value: Text
        """
        
        def __init__(self, value: str):
            super().__init__("label", value)
            


    class selected(BaseAttribute):
        """
        option attribute: selected
        Description: Whether the option is selected by default
        Value: Boolean attribute
        """
        
        def __init__(self, value: bool):
            super().__init__("selected", value)
            


    class value(BaseAttribute):
        """
        option attribute: value
        Description: Value to be used for form submission
        Value: Text
        """
        
        def __init__(self, value: str):
            super().__init__("value", value)
            