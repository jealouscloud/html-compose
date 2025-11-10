from . import BaseAttribute
from typing import Literal, Iterable, Mapping
from ..base_types import Resolvable, StrLike

class AreaAttrs:
    """ 
    This module contains functions for attributes in the 'area' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def alt(value: StrLike) -> BaseAttribute:
        """
        "area" attribute: alt  
        Replacement text for use when images are not available  

        Args:
            value:
                Text*
        
        Returns:
            An alt attribute to be added to your element

        """
        
        return BaseAttribute("alt", value)
            


    @staticmethod
    def coords(value) -> BaseAttribute:
        """
        "area" attribute: coords  
        Coordinates for the shape to be created in an image map  

        Args:
            value:
                Valid list of floating-point numbers*
        
        Returns:
            An coords attribute to be added to your element

        """
        
        return BaseAttribute("coords", value)
            


    @staticmethod
    def download(value: StrLike) -> BaseAttribute:
        """
        "area" attribute: download  
        Whether to download the resource instead of navigating to it, and its filename if so  

        Args:
            value:
                Text
        
        Returns:
            An download attribute to be added to your element

        """
        
        return BaseAttribute("download", value)
            


    @staticmethod
    def href(value) -> BaseAttribute:
        """
        "area" attribute: href  
        Address of the hyperlink  

        Args:
            value:
                Valid URL potentially surrounded by spaces
        
        Returns:
            An href attribute to be added to your element

        """
        
        return BaseAttribute("href", value)
            


    @staticmethod
    def ping(value: Resolvable) -> BaseAttribute:
        """
        "area" attribute: ping  
        URLs to ping  

        Args:
            value:
                Set of space-separated tokens consisting of valid non-empty URLs
        
        Returns:
            An ping attribute to be added to your element

        """
        
        return BaseAttribute("ping", value)
            


    @staticmethod
    def referrerpolicy(value) -> BaseAttribute:
        """
        "area" attribute: referrerpolicy  
        Referrer policy for fetches initiated by the element  

        Args:
            value:
                Referrer policy
        
        Returns:
            An referrerpolicy attribute to be added to your element

        """
        
        return BaseAttribute("referrerpolicy", value)
            


    @staticmethod
    def rel(value: Resolvable) -> BaseAttribute:
        """
        "area" attribute: rel  
        Relationship between the location in the document containing the hyperlink and the destination resource  

        Args:
            value:
                Unordered set of unique space-separated tokens*
        
        Returns:
            An rel attribute to be added to your element

        """
        
        return BaseAttribute("rel", value)
            


    @staticmethod
    def shape(value: Literal['circle', 'default', 'poly', 'rect']) -> BaseAttribute:
        """
        "area" attribute: shape  
        The kind of shape to be created in an image map  

        Args:
            value:
                ['circle', 'default', 'poly', 'rect']
        
        Returns:
            An shape attribute to be added to your element

        """
        
        return BaseAttribute("shape", value)
            


    @staticmethod
    def target(value) -> BaseAttribute:
        """
        "area" attribute: target  
        Navigable for hyperlink navigation  

        Args:
            value:
                Valid navigable target name or keyword
        
        Returns:
            An target attribute to be added to your element

        """
        
        return BaseAttribute("target", value)
            