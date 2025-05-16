from . import BaseAttribute
from typing import Literal, Union

class TemplateAttrs:
    """ 
    This module contains functions for attributes in the 'template' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def shadowrootclonable(value: bool) -> BaseAttribute:
        """
        "template" attribute: shadowrootclonable  
        Sets clonable on a declarative shadow root  

        :param value: Boolean attribute  
        :return: An shadowrootclonable attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("shadowrootclonable", value)
            


    @staticmethod
    def shadowrootdelegatesfocus(value: bool) -> BaseAttribute:
        """
        "template" attribute: shadowrootdelegatesfocus  
        Sets delegates focus on a declarative shadow root  

        :param value: Boolean attribute  
        :return: An shadowrootdelegatesfocus attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("shadowrootdelegatesfocus", value)
            


    @staticmethod
    def shadowrootmode(value: Literal['open', 'closed']) -> BaseAttribute:
        """
        "template" attribute: shadowrootmode  
        Enables streaming declarative shadow roots  

        :param value: ['open', 'closed']  
        :return: An shadowrootmode attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("shadowrootmode", value)
            


    @staticmethod
    def shadowrootserializable(value: bool) -> BaseAttribute:
        """
        "template" attribute: shadowrootserializable  
        Sets serializable on a declarative shadow root  

        :param value: Boolean attribute  
        :return: An shadowrootserializable attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("shadowrootserializable", value)
            