from . import BaseAttribute
from typing import Literal, Union

class TrackAttrs:
    """ 
    This module contains classes for attributes in the <track> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """ 
    
    class default(BaseAttribute):
        """
        track attribute: default
        Description: Enable the track if no other text track is more suitable
        Value: Boolean attribute
        """
        
        def __init__(self, value: bool):
            super().__init__("default", value)
            


    class kind(BaseAttribute):
        """
        track attribute: kind
        Description: The type of text track
        Value: ['subtitles', 'captions', 'descriptions', 'chapters', 'metadata']
        """
        
        def __init__(self, value):
            super().__init__("kind", value)
            


    class label(BaseAttribute):
        """
        track attribute: label
        Description: User-visible label
        Value: Text
        """
        
        def __init__(self, value: str):
            super().__init__("label", value)
            


    class src(BaseAttribute):
        """
        track attribute: src
        Description: Address of the resource
        Value: Valid non-empty URL potentially surrounded by spaces
        """
        
        def __init__(self, value):
            super().__init__("src", value)
            


    class srclang(BaseAttribute):
        """
        track attribute: srclang
        Description: Language of the text track
        Value: Valid BCP 47 language tag
        """
        
        def __init__(self, value):
            super().__init__("srclang", value)
            