from . import BaseAttribute
from typing import Literal, Iterable, Mapping
from ..base_types import Resolvable, StrLike

class LinkAttrs:
    """ 
    This module contains functions for attributes in the 'link' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def as_(value) -> BaseAttribute:
        """
        "link" attribute: as  
        Potential destination for a preload request (for rel="preload" and rel="modulepreload")  

        Args:
            value:
                Potential destination, for rel="preload"; script-like destination, for rel="modulepreload"
        
        Returns:
            An as attribute to be added to your element

        """
        
        return BaseAttribute("as", value)
            


    @staticmethod
    def blocking(value: Resolvable) -> BaseAttribute:
        """
        "link" attribute: blocking  
        Whether the element is potentially render-blocking  

        Args:
            value:
                Unordered set of unique space-separated tokens*
        
        Returns:
            An blocking attribute to be added to your element

        """
        
        return BaseAttribute("blocking", value)
            


    @staticmethod
    def color(value) -> BaseAttribute:
        """
        "link" attribute: color  
        Color to use when customizing a site's icon (for rel="mask-icon")  

        Args:
            value:
                CSS <color>
        
        Returns:
            An color attribute to be added to your element

        """
        
        return BaseAttribute("color", value)
            


    @staticmethod
    def crossorigin(value: Literal['anonymous', 'use-credentials']) -> BaseAttribute:
        """
        "link" attribute: crossorigin  
        How the element handles crossorigin requests  

        Args:
            value:
                ['anonymous', 'use-credentials']
        
        Returns:
            An crossorigin attribute to be added to your element

        """
        
        return BaseAttribute("crossorigin", value)
            


    @staticmethod
    def disabled(value: bool) -> BaseAttribute:
        """
        "link" attribute: disabled  
        Whether the link is disabled  

        Args:
            value:
                Boolean attribute
        
        Returns:
            An disabled attribute to be added to your element

        """
        
        return BaseAttribute("disabled", value)
            


    @staticmethod
    def fetchpriority(value: Literal['auto', 'high', 'low']) -> BaseAttribute:
        """
        "link" attribute: fetchpriority  
        Sets the priority for fetches initiated by the element  

        Args:
            value:
                ['auto', 'high', 'low']
        
        Returns:
            An fetchpriority attribute to be added to your element

        """
        
        return BaseAttribute("fetchpriority", value)
            


    @staticmethod
    def href(value) -> BaseAttribute:
        """
        "link" attribute: href  
        Address of the hyperlink  

        Args:
            value:
                Valid non-empty URL potentially surrounded by spaces
        
        Returns:
            An href attribute to be added to your element

        """
        
        return BaseAttribute("href", value)
            


    @staticmethod
    def hreflang(value) -> BaseAttribute:
        """
        "link" attribute: hreflang  
        Language of the linked resource  

        Args:
            value:
                Valid BCP 47 language tag
        
        Returns:
            An hreflang attribute to be added to your element

        """
        
        return BaseAttribute("hreflang", value)
            


    @staticmethod
    def imagesizes(value) -> BaseAttribute:
        """
        "link" attribute: imagesizes  
        Image sizes for different page layouts (for rel="preload")  

        Args:
            value:
                Valid source size list
        
        Returns:
            An imagesizes attribute to be added to your element

        """
        
        return BaseAttribute("imagesizes", value)
            


    @staticmethod
    def imagesrcset(value) -> BaseAttribute:
        """
        "link" attribute: imagesrcset  
        Images to use in different situations, e.g., high-resolution displays, small monitors, etc. (for rel="preload")  

        Args:
            value:
                Comma-separated list of image candidate strings
        
        Returns:
            An imagesrcset attribute to be added to your element

        """
        
        return BaseAttribute("imagesrcset", value)
            


    @staticmethod
    def integrity(value: StrLike) -> BaseAttribute:
        """
        "link" attribute: integrity  
        Integrity metadata used in Subresource Integrity checks [SRI]  

        Args:
            value:
                Text
        
        Returns:
            An integrity attribute to be added to your element

        """
        
        return BaseAttribute("integrity", value)
            


    @staticmethod
    def media(value) -> BaseAttribute:
        """
        "link" attribute: media  
        Applicable media  

        Args:
            value:
                Valid media query list
        
        Returns:
            An media attribute to be added to your element

        """
        
        return BaseAttribute("media", value)
            


    @staticmethod
    def referrerpolicy(value) -> BaseAttribute:
        """
        "link" attribute: referrerpolicy  
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
        "link" attribute: rel  
        Relationship between the document containing the hyperlink and the destination resource  

        Args:
            value:
                Unordered set of unique space-separated tokens*
        
        Returns:
            An rel attribute to be added to your element

        """
        
        return BaseAttribute("rel", value)
            


    @staticmethod
    def sizes(value: Resolvable) -> BaseAttribute:
        """
        "link" attribute: sizes  
        Sizes of the icons (for rel="icon")  

        Args:
            value:
                Unordered set of unique space-separated tokens, ASCII case-insensitive, consisting of sizes*
        
        Returns:
            An sizes attribute to be added to your element

        """
        
        return BaseAttribute("sizes", value)
            


    @staticmethod
    def title(value) -> BaseAttribute:
        """
        "link" attribute: title  
        Title of the link  OR  CSS style sheet set name  

        Args:
            value:
                Text  OR  Text
        
        Returns:
            An title attribute to be added to your element

        """
        
        return BaseAttribute("title", value)
            


    @staticmethod
    def type(value) -> BaseAttribute:
        """
        "link" attribute: type  
        Hint for the type of the referenced resource  

        Args:
            value:
                Valid MIME type string
        
        Returns:
            An type attribute to be added to your element

        """
        
        return BaseAttribute("type", value)
            