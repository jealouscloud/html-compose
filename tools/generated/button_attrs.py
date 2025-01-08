from . import BaseAttribute
from typing import Literal, Union

class ButtonAttrs:
    """ 
    This module contains classes for attributes in the <button> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """ 
    
    class disabled(BaseAttribute):
        """
        button attribute: disabled
        Description: Whether the form control is disabled
        Value: Boolean attribute
        """
        
        def __init__(self, value: bool):
            super().__init__("disabled", value)
            


    class form(BaseAttribute):
        """
        button attribute: form
        Description: Associates the element with a form element
        Value: ID*
        """
        
        def __init__(self, value):
            super().__init__("form", value)
            


    class formaction(BaseAttribute):
        """
        button attribute: formaction
        Description: URL to use for form submission
        Value: Valid non-empty URL potentially surrounded by spaces
        """
        
        def __init__(self, value):
            super().__init__("formaction", value)
            


    class formenctype(BaseAttribute):
        """
        button attribute: formenctype
        Description: Entry list encoding type to use for form submission
        Value: ['application/x-www-form-urlencoded', 'multipart/form-data', 'text/plain']
        """
        
        def __init__(self, value):
            super().__init__("formenctype", value)
            


    class formmethod(BaseAttribute):
        """
        button attribute: formmethod
        Description: Variant to use for form submission
        Value: ['GET', 'POST', 'dialog']
        """
        
        def __init__(self, value):
            super().__init__("formmethod", value)
            


    class formnovalidate(BaseAttribute):
        """
        button attribute: formnovalidate
        Description: Bypass form control validation for form submission
        Value: Boolean attribute
        """
        
        def __init__(self, value: bool):
            super().__init__("formnovalidate", value)
            


    class formtarget(BaseAttribute):
        """
        button attribute: formtarget
        Description: Navigable for form submission
        Value: Valid navigable target name or keyword
        """
        
        def __init__(self, value):
            super().__init__("formtarget", value)
            


    class name(BaseAttribute):
        """
        button attribute: name
        Description: Name of the element to use for form submission and in the form.elements API
        Value: Text*
        """
        
        def __init__(self, value: str):
            super().__init__("name", value)
            


    class popovertarget(BaseAttribute):
        """
        button attribute: popovertarget
        Description: Targets a popover element to toggle, show, or hide
        Value: ID*
        """
        
        def __init__(self, value):
            super().__init__("popovertarget", value)
            


    class popovertargetaction(BaseAttribute):
        """
        button attribute: popovertargetaction
        Description: Indicates whether a targeted popover element is to be toggled, shown, or hidden
        Value: ['toggle', 'show', 'hide']
        """
        
        def __init__(self, value):
            super().__init__("popovertargetaction", value)
            


    class type(BaseAttribute):
        """
        button attribute: type
        Description: Type of button
        Value: ['submit', 'reset', 'button']
        """
        
        def __init__(self, value):
            super().__init__("type", value)
            


    class value(BaseAttribute):
        """
        button attribute: value
        Description: Value to be used for form submission
        Value: Text
        """
        
        def __init__(self, value: str):
            super().__init__("value", value)
            