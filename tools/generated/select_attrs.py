from . import BaseAttribute
from typing import Literal, Union

class SelectAttrs:
    """ 
    This module contains classes for attributes in the <select> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """ 
    
    class autocomplete(BaseAttribute):
        """
        select attribute: autocomplete
        Description: Hint for form autofill feature
        Value: Autofill field name and related tokens*
        """
        
        def __init__(self, value):
            super().__init__("autocomplete", value)
            


    class disabled(BaseAttribute):
        """
        select attribute: disabled
        Description: Whether the form control is disabled
        Value: Boolean attribute
        """
        
        def __init__(self, value: bool):
            super().__init__("disabled", value)
            


    class form(BaseAttribute):
        """
        select attribute: form
        Description: Associates the element with a form element
        Value: ID*
        """
        
        def __init__(self, value):
            super().__init__("form", value)
            


    class multiple(BaseAttribute):
        """
        select attribute: multiple
        Description: Whether to allow multiple values
        Value: Boolean attribute
        """
        
        def __init__(self, value: bool):
            super().__init__("multiple", value)
            


    class name(BaseAttribute):
        """
        select attribute: name
        Description: Name of the element to use for form submission and in the form.elements API
        Value: Text*
        """
        
        def __init__(self, value: str):
            super().__init__("name", value)
            


    class required(BaseAttribute):
        """
        select attribute: required
        Description: Whether the control is required for form submission
        Value: Boolean attribute
        """
        
        def __init__(self, value: bool):
            super().__init__("required", value)
            


    class size(BaseAttribute):
        """
        select attribute: size
        Description: Size of the control
        Value: Valid non-negative integer greater than zero
        """
        
        def __init__(self, value):
            super().__init__("size", value)
            