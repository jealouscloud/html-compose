from . import BaseAttribute
from typing import Literal, Union

class InputAttrs:
    """ 
    This module contains functions for attributes in the 'input' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def accept(value) -> BaseAttribute:
        """
        "input" attribute: accept  
        Hint for expected file type in file upload controls  

        :param value: Set of comma-separated tokens* consisting of valid MIME type strings with no parameters or audio/*, video/*, or image/*  
        :return: An accept attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("accept", value)
            


    @staticmethod
    def alpha(value: bool) -> BaseAttribute:
        """
        "input" attribute: alpha  
        Allow the color's alpha component to be set  

        :param value: Boolean attribute  
        :return: An alpha attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("alpha", value)
            


    @staticmethod
    def alt(value: str) -> BaseAttribute:
        """
        "input" attribute: alt  
        Replacement text for use when images are not available  

        :param value: Text*  
        :return: An alt attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("alt", value)
            


    @staticmethod
    def autocomplete(value) -> BaseAttribute:
        """
        "input" attribute: autocomplete  
        Hint for form autofill feature  

        :param value: Autofill field name and related tokens*  
        :return: An autocomplete attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("autocomplete", value)
            


    @staticmethod
    def checked(value: bool) -> BaseAttribute:
        """
        "input" attribute: checked  
        Whether the control is checked  

        :param value: Boolean attribute  
        :return: An checked attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("checked", value)
            


    @staticmethod
    def colorspace(value: Literal['limited-srgb', 'display-p3']) -> BaseAttribute:
        """
        "input" attribute: colorspace  
        The color space of the serialized color  

        :param value: ['limited-srgb', 'display-p3']  
        :return: An colorspace attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("colorspace", value)
            


    @staticmethod
    def dirname(value: str) -> BaseAttribute:
        """
        "input" attribute: dirname  
        Name of form control to use for sending the element's directionality in form submission  

        :param value: Text*  
        :return: An dirname attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("dirname", value)
            


    @staticmethod
    def disabled(value: bool) -> BaseAttribute:
        """
        "input" attribute: disabled  
        Whether the form control is disabled  

        :param value: Boolean attribute  
        :return: An disabled attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("disabled", value)
            


    @staticmethod
    def form(value) -> BaseAttribute:
        """
        "input" attribute: form  
        Associates the element with a form element  

        :param value: ID*  
        :return: An form attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("form", value)
            


    @staticmethod
    def formaction(value) -> BaseAttribute:
        """
        "input" attribute: formaction  
        URL to use for form submission  

        :param value: Valid non-empty URL potentially surrounded by spaces  
        :return: An formaction attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("formaction", value)
            


    @staticmethod
    def formenctype(value: Literal['application/x-www-form-urlencoded', 'multipart/form-data', 'text/plain']) -> BaseAttribute:
        """
        "input" attribute: formenctype  
        Entry list encoding type to use for form submission  

        :param value: ['application/x-www-form-urlencoded', 'multipart/form-data', 'text/plain']  
        :return: An formenctype attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("formenctype", value)
            


    @staticmethod
    def formmethod(value: Literal['GET', 'POST', 'dialog']) -> BaseAttribute:
        """
        "input" attribute: formmethod  
        Variant to use for form submission  

        :param value: ['GET', 'POST', 'dialog']  
        :return: An formmethod attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("formmethod", value)
            


    @staticmethod
    def formnovalidate(value: bool) -> BaseAttribute:
        """
        "input" attribute: formnovalidate  
        Bypass form control validation for form submission  

        :param value: Boolean attribute  
        :return: An formnovalidate attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("formnovalidate", value)
            


    @staticmethod
    def formtarget(value) -> BaseAttribute:
        """
        "input" attribute: formtarget  
        Navigable for form submission  

        :param value: Valid navigable target name or keyword  
        :return: An formtarget attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("formtarget", value)
            


    @staticmethod
    def height(value: int) -> BaseAttribute:
        """
        "input" attribute: height  
        Vertical dimension  

        :param value: Valid non-negative integer  
        :return: An height attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("height", value)
            


    @staticmethod
    def list(value) -> BaseAttribute:
        """
        "input" attribute: list  
        List of autocomplete options  

        :param value: ID*  
        :return: An list attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("list", value)
            


    @staticmethod
    def max(value) -> BaseAttribute:
        """
        "input" attribute: max  
        Maximum value  

        :param value: Varies*  
        :return: An max attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("max", value)
            


    @staticmethod
    def maxlength(value: int) -> BaseAttribute:
        """
        "input" attribute: maxlength  
        Maximum length of value  

        :param value: Valid non-negative integer  
        :return: An maxlength attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("maxlength", value)
            


    @staticmethod
    def min(value) -> BaseAttribute:
        """
        "input" attribute: min  
        Minimum value  

        :param value: Varies*  
        :return: An min attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("min", value)
            


    @staticmethod
    def minlength(value: int) -> BaseAttribute:
        """
        "input" attribute: minlength  
        Minimum length of value  

        :param value: Valid non-negative integer  
        :return: An minlength attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("minlength", value)
            


    @staticmethod
    def multiple(value: bool) -> BaseAttribute:
        """
        "input" attribute: multiple  
        Whether to allow multiple values  

        :param value: Boolean attribute  
        :return: An multiple attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("multiple", value)
            


    @staticmethod
    def name(value: str) -> BaseAttribute:
        """
        "input" attribute: name  
        Name of the element to use for form submission and in the form.elements API  

        :param value: Text*  
        :return: An name attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("name", value)
            


    @staticmethod
    def pattern(value) -> BaseAttribute:
        """
        "input" attribute: pattern  
        Pattern to be matched by the form control's value  

        :param value: Regular expression matching the JavaScript Pattern production  
        :return: An pattern attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("pattern", value)
            


    @staticmethod
    def placeholder(value: str) -> BaseAttribute:
        """
        "input" attribute: placeholder  
        User-visible label to be placed within the form control  

        :param value: Text*  
        :return: An placeholder attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("placeholder", value)
            


    @staticmethod
    def popovertarget(value) -> BaseAttribute:
        """
        "input" attribute: popovertarget  
        Targets a popover element to toggle, show, or hide  

        :param value: ID*  
        :return: An popovertarget attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("popovertarget", value)
            


    @staticmethod
    def popovertargetaction(value: Literal['toggle', 'show', 'hide']) -> BaseAttribute:
        """
        "input" attribute: popovertargetaction  
        Indicates whether a targeted popover element is to be toggled, shown, or hidden  

        :param value: ['toggle', 'show', 'hide']  
        :return: An popovertargetaction attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("popovertargetaction", value)
            


    @staticmethod
    def readonly(value: bool) -> BaseAttribute:
        """
        "input" attribute: readonly  
        Whether to allow the value to be edited by the user  

        :param value: Boolean attribute  
        :return: An readonly attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("readonly", value)
            


    @staticmethod
    def required(value: bool) -> BaseAttribute:
        """
        "input" attribute: required  
        Whether the control is required for form submission  

        :param value: Boolean attribute  
        :return: An required attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("required", value)
            


    @staticmethod
    def size(value) -> BaseAttribute:
        """
        "input" attribute: size  
        Size of the control  

        :param value: Valid non-negative integer greater than zero  
        :return: An size attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("size", value)
            


    @staticmethod
    def src(value) -> BaseAttribute:
        """
        "input" attribute: src  
        Address of the resource  

        :param value: Valid non-empty URL potentially surrounded by spaces  
        :return: An src attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("src", value)
            


    @staticmethod
    def step(value: float) -> BaseAttribute:
        """
        "input" attribute: step  
        Granularity to be matched by the form control's value  

        :param value: Valid floating-point number greater than zero, or "any"  
        :return: An step attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("step", value)
            


    @staticmethod
    def title(value: str) -> BaseAttribute:
        """
        "input" attribute: title  
        Description of pattern (when used with pattern attribute)  

        :param value: Text  
        :return: An title attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("title", value)
            


    @staticmethod
    def type(value) -> BaseAttribute:
        """
        "input" attribute: type  
        Type of form control  

        :param value: input type keyword  
        :return: An type attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("type", value)
            


    @staticmethod
    def value(value) -> BaseAttribute:
        """
        "input" attribute: value  
        Value of the form control  

        :param value: Varies*  
        :return: An value attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("value", value)
            


    @staticmethod
    def width(value: int) -> BaseAttribute:
        """
        "input" attribute: width  
        Horizontal dimension  

        :param value: Valid non-negative integer  
        :return: An width attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("width", value)
            