from . import BaseAttribute
from typing import Literal, Union

class AnchorAttrs:
    """ 
    This module contains functions for attributes in the 'a' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def download(value: str) -> BaseAttribute:
        """
        "a" attribute: download  
        Whether to download the resource instead of navigating to it, and its filename if so  

        :param value: Text  
        :return: An download attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("download", value)
            


    @staticmethod
    def href(value) -> BaseAttribute:
        """
        "a" attribute: href  
        Address of the hyperlink  

        :param value: Valid URL potentially surrounded by spaces  
        :return: An href attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("href", value)
            


    @staticmethod
    def hreflang(value) -> BaseAttribute:
        """
        "a" attribute: hreflang  
        Language of the linked resource  

        :param value: Valid BCP 47 language tag  
        :return: An hreflang attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("hreflang", value)
            


    @staticmethod
    def ping(value: list) -> BaseAttribute:
        """
        "a" attribute: ping  
        URLs to ping  

        :param value: Set of space-separated tokens consisting of valid non-empty URLs  
        :return: An ping attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("ping", value)
            


    @staticmethod
    def referrerpolicy(value) -> BaseAttribute:
        """
        "a" attribute: referrerpolicy  
        Referrer policy for fetches initiated by the element  

        :param value: Referrer policy  
        :return: An referrerpolicy attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("referrerpolicy", value)
            


    @staticmethod
    def rel(value: list) -> BaseAttribute:
        """
        "a" attribute: rel  
        Relationship between the location in the document containing the hyperlink and the destination resource  

        :param value: Unordered set of unique space-separated tokens*  
        :return: An rel attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("rel", value)
            


    @staticmethod
    def target(value) -> BaseAttribute:
        """
        "a" attribute: target  
        Navigable for hyperlink navigation  

        :param value: Valid navigable target name or keyword  
        :return: An target attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("target", value)
            


    @staticmethod
    def type(value) -> BaseAttribute:
        """
        "a" attribute: type  
        Hint for the type of the referenced resource  

        :param value: Valid MIME type string  
        :return: An type attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("type", value)
            