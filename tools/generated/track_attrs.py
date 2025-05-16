from . import BaseAttribute
from typing import Literal, Union

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

        :param value: Boolean attribute  
        :return: An default attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("default", value)
            


    @staticmethod
    def kind(value: Literal['subtitles', 'captions', 'descriptions', 'chapters', 'metadata']) -> BaseAttribute:
        """
        "track" attribute: kind  
        The type of text track  

        :param value: ['subtitles', 'captions', 'descriptions', 'chapters', 'metadata']  
        :return: An kind attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("kind", value)
            


    @staticmethod
    def label(value: str) -> BaseAttribute:
        """
        "track" attribute: label  
        User-visible label  

        :param value: Text  
        :return: An label attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("label", value)
            


    @staticmethod
    def src(value) -> BaseAttribute:
        """
        "track" attribute: src  
        Address of the resource  

        :param value: Valid non-empty URL potentially surrounded by spaces  
        :return: An src attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("src", value)
            


    @staticmethod
    def srclang(value) -> BaseAttribute:
        """
        "track" attribute: srclang  
        Language of the text track  

        :param value: Valid BCP 47 language tag  
        :return: An srclang attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("srclang", value)
            