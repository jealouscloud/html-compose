from . import BaseAttribute
from typing import Literal, Iterable, Mapping
from ..base_types import Resolvable, StrLike

class ImgAttrs:
    """ 
    This module contains functions for attributes in the 'img' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def alt(value: StrLike) -> BaseAttribute:
        """
        "img" attribute: alt  
        Replacement text for use when images are not available  

        Args:
            value:
                Text*
        
        Returns:
            An alt attribute to be added to your element

        """
        
        return BaseAttribute("alt", value)
            


    @staticmethod
    def crossorigin(value: Literal['anonymous', 'use-credentials']) -> BaseAttribute:
        """
        "img" attribute: crossorigin  
        How the element handles crossorigin requests  

        Args:
            value:
                ['anonymous', 'use-credentials']
        
        Returns:
            An crossorigin attribute to be added to your element

        """
        
        return BaseAttribute("crossorigin", value)
            


    @staticmethod
    def decoding(value: Literal['sync', 'async', 'auto']) -> BaseAttribute:
        """
        "img" attribute: decoding  
        Decoding hint to use when processing this image for presentation  

        Args:
            value:
                ['sync', 'async', 'auto']
        
        Returns:
            An decoding attribute to be added to your element

        """
        
        return BaseAttribute("decoding", value)
            


    @staticmethod
    def fetchpriority(value: Literal['auto', 'high', 'low']) -> BaseAttribute:
        """
        "img" attribute: fetchpriority  
        Sets the priority for fetches initiated by the element  

        Args:
            value:
                ['auto', 'high', 'low']
        
        Returns:
            An fetchpriority attribute to be added to your element

        """
        
        return BaseAttribute("fetchpriority", value)
            


    @staticmethod
    def height(value: int) -> BaseAttribute:
        """
        "img" attribute: height  
        Vertical dimension  

        Args:
            value:
                Valid non-negative integer
        
        Returns:
            An height attribute to be added to your element

        """
        
        return BaseAttribute("height", value)
            


    @staticmethod
    def ismap(value: bool) -> BaseAttribute:
        """
        "img" attribute: ismap  
        Whether the image is a server-side image map  

        Args:
            value:
                Boolean attribute
        
        Returns:
            An ismap attribute to be added to your element

        """
        
        return BaseAttribute("ismap", value)
            


    @staticmethod
    def loading(value: Literal['lazy', 'eager']) -> BaseAttribute:
        """
        "img" attribute: loading  
        Used when determining loading deferral  

        Args:
            value:
                ['lazy', 'eager']
        
        Returns:
            An loading attribute to be added to your element

        """
        
        return BaseAttribute("loading", value)
            


    @staticmethod
    def referrerpolicy(value) -> BaseAttribute:
        """
        "img" attribute: referrerpolicy  
        Referrer policy for fetches initiated by the element  

        Args:
            value:
                Referrer policy
        
        Returns:
            An referrerpolicy attribute to be added to your element

        """
        
        return BaseAttribute("referrerpolicy", value)
            


    @staticmethod
    def sizes(value) -> BaseAttribute:
        """
        "img" attribute: sizes  
        Image sizes for different page layouts  

        Args:
            value:
                Valid source size list
        
        Returns:
            An sizes attribute to be added to your element

        """
        
        return BaseAttribute("sizes", value)
            


    @staticmethod
    def src(value) -> BaseAttribute:
        """
        "img" attribute: src  
        Address of the resource  

        Args:
            value:
                Valid non-empty URL potentially surrounded by spaces
        
        Returns:
            An src attribute to be added to your element

        """
        
        return BaseAttribute("src", value)
            


    @staticmethod
    def srcset(value) -> BaseAttribute:
        """
        "img" attribute: srcset  
        Images to use in different situations, e.g., high-resolution displays, small monitors, etc.  

        Args:
            value:
                Comma-separated list of image candidate strings
        
        Returns:
            An srcset attribute to be added to your element

        """
        
        return BaseAttribute("srcset", value)
            


    @staticmethod
    def usemap(value) -> BaseAttribute:
        """
        "img" attribute: usemap  
        Name of image map to use  

        Args:
            value:
                Valid hash-name reference*
        
        Returns:
            An usemap attribute to be added to your element

        """
        
        return BaseAttribute("usemap", value)
            


    @staticmethod
    def width(value: int) -> BaseAttribute:
        """
        "img" attribute: width  
        Horizontal dimension  

        Args:
            value:
                Valid non-negative integer
        
        Returns:
            An width attribute to be added to your element

        """
        
        return BaseAttribute("width", value)
            