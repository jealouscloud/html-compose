from . import BaseAttribute
from typing import Literal, Iterable, Mapping
from ..base_types import Resolvable, StrLike

class TrackAttrs:
    """ 
    This module contains functions for attributes in the 'track' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def default(value: bool) -> BaseAttribute:
        """
        "track" attribute: default  
        Enable the track if no other text track is more suitable  

        Args:
            value:
                Boolean attribute
        
        Returns:
            An default attribute to be added to your element

        """
        
        return BaseAttribute("default", value)
            


    @staticmethod
    def kind(value: Literal['subtitles', 'captions', 'descriptions', 'chapters', 'metadata']) -> BaseAttribute:
        """
        "track" attribute: kind  
        The type of text track  

        Args:
            value:
                ['subtitles', 'captions', 'descriptions', 'chapters', 'metadata']
        
        Returns:
            An kind attribute to be added to your element

        """
        
        return BaseAttribute("kind", value)
            


    @staticmethod
    def label(value: StrLike) -> BaseAttribute:
        """
        "track" attribute: label  
        User-visible label  

        Args:
            value:
                Text
        
        Returns:
            An label attribute to be added to your element

        """
        
        return BaseAttribute("label", value)
            


    @staticmethod
    def src(value) -> BaseAttribute:
        """
        "track" attribute: src  
        Address of the resource  

        Args:
            value:
                Valid non-empty URL potentially surrounded by spaces
        
        Returns:
            An src attribute to be added to your element

        """
        
        return BaseAttribute("src", value)
            


    @staticmethod
    def srclang(value) -> BaseAttribute:
        """
        "track" attribute: srclang  
        Language of the text track  

        Args:
            value:
                Valid BCP 47 language tag
        
        Returns:
            An srclang attribute to be added to your element

        """
        
        return BaseAttribute("srclang", value)
            