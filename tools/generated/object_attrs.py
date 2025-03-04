from . import BaseAttribute
from typing import Literal, Union

class ObjectAttrs:
    """ 
    This module contains functions for attributes in the 'object' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def data(value) -> BaseAttribute:
        """
        "object" attribute: data  
        Address of the resource  

        :param value: Valid non-empty URL potentially surrounded by spaces  
        :return: An data attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("data", value)
            


    @staticmethod
    def form(value) -> BaseAttribute:
        """
        "object" attribute: form  
        Associates the element with a form element  

        :param value: ID*  
        :return: An form attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("form", value)
            


    @staticmethod
    def height(value: int) -> BaseAttribute:
        """
        "object" attribute: height  
        Vertical dimension  

        :param value: Valid non-negative integer  
        :return: An height attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("height", value)
            


    @staticmethod
    def name(value) -> BaseAttribute:
        """
        "object" attribute: name  
        Name of content navigable  

        :param value: Valid navigable target name or keyword  
        :return: An name attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("name", value)
            


    @staticmethod
    def type(value) -> BaseAttribute:
        """
        "object" attribute: type  
        Type of embedded resource  

        :param value: Valid MIME type string  
        :return: An type attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("type", value)
            


    @staticmethod
    def width(value: int) -> BaseAttribute:
        """
        "object" attribute: width  
        Horizontal dimension  

        :param value: Valid non-negative integer  
        :return: An width attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("width", value)
            