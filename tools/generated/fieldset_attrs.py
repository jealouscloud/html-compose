from . import BaseAttribute
from typing import Literal, Union

class FieldsetAttrs:
    """ 
    This module contains classes for attributes in the <fieldset> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """ 
    
    class disabled(BaseAttribute):
        """
        fieldset attribute: disabled
        Description: Whether the descendant form controls, except any inside legend, are disabled
        Value: Boolean attribute
        """
        
        def __init__(self, value: bool):
            super().__init__("disabled", value)
            


    class form(BaseAttribute):
        """
        fieldset attribute: form
        Description: Associates the element with a form element
        Value: ID*
        """
        
        def __init__(self, value):
            super().__init__("form", value)
            


    class name(BaseAttribute):
        """
        fieldset attribute: name
        Description: Name of the element to use for form submission and in the form.elements API
        Value: Text*
        """
        
        def __init__(self, value: str):
            super().__init__("name", value)
            