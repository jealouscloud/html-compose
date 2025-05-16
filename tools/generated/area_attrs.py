from . import BaseAttribute
from typing import Literal, Union

class AreaAttrs:
    """ 
    This module contains functions for attributes in the 'area' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def alt(value: str) -> BaseAttribute:
        """
        "area" attribute: alt  
        Replacement text for use when images are not available  

        :param value: Text*  
        :return: An alt attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("alt", value)
            


    @staticmethod
    def coords(value) -> BaseAttribute:
        """
        "area" attribute: coords  
        Coordinates for the shape to be created in an image map  

        :param value: Valid list of floating-point numbers*  
        :return: An coords attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("coords", value)
            


    @staticmethod
    def download(value: str) -> BaseAttribute:
        """
        "area" attribute: download  
        Whether to download the resource instead of navigating to it, and its filename if so  

        :param value: Text  
        :return: An download attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("download", value)
            


    @staticmethod
    def href(value) -> BaseAttribute:
        """
        "area" attribute: href  
        Address of the hyperlink  

        :param value: Valid URL potentially surrounded by spaces  
        :return: An href attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("href", value)
            


    @staticmethod
    def ping(value: list) -> BaseAttribute:
        """
        "area" attribute: ping  
        URLs to ping  

        :param value: Set of space-separated tokens consisting of valid non-empty URLs  
        :return: An ping attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("ping", value)
            


    @staticmethod
    def referrerpolicy(value) -> BaseAttribute:
        """
        "area" attribute: referrerpolicy  
        Referrer policy for fetches initiated by the element  

        :param value: Referrer policy  
        :return: An referrerpolicy attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("referrerpolicy", value)
            


    @staticmethod
    def rel(value: list) -> BaseAttribute:
        """
        "area" attribute: rel  
        Relationship between the location in the document containing the hyperlink and the destination resource  

        :param value: Unordered set of unique space-separated tokens*  
        :return: An rel attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("rel", value)
            


    @staticmethod
    def shape(value: Literal['circle', 'default', 'poly', 'rect']) -> BaseAttribute:
        """
        "area" attribute: shape  
        The kind of shape to be created in an image map  

        :param value: ['circle', 'default', 'poly', 'rect']  
        :return: An shape attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("shape", value)
            


    @staticmethod
    def target(value) -> BaseAttribute:
        """
        "area" attribute: target  
        Navigable for hyperlink navigation  

        :param value: Valid navigable target name or keyword  
        :return: An target attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("target", value)
            