from . import BaseAttribute
from typing import Literal, Union

class AudioAttrs:
    """ 
    This module contains classes for attributes in the <audio> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """ 
    
    class autoplay(BaseAttribute):
        """
        audio attribute: autoplay
        Description: Hint that the media resource can be started automatically when the page is loaded
        Value: Boolean attribute
        """
        
        def __init__(self, value: bool):
            super().__init__("autoplay", value)
            


    class controls(BaseAttribute):
        """
        audio attribute: controls
        Description: Show user agent controls
        Value: Boolean attribute
        """
        
        def __init__(self, value: bool):
            super().__init__("controls", value)
            


    class crossorigin(BaseAttribute):
        """
        audio attribute: crossorigin
        Description: How the element handles crossorigin requests
        Value: ['anonymous', 'use-credentials']
        """
        
        def __init__(self, value):
            super().__init__("crossorigin", value)
            


    class loop(BaseAttribute):
        """
        audio attribute: loop
        Description: Whether to loop the media resource
        Value: Boolean attribute
        """
        
        def __init__(self, value: bool):
            super().__init__("loop", value)
            


    class muted(BaseAttribute):
        """
        audio attribute: muted
        Description: Whether to mute the media resource by default
        Value: Boolean attribute
        """
        
        def __init__(self, value: bool):
            super().__init__("muted", value)
            


    class preload(BaseAttribute):
        """
        audio attribute: preload
        Description: Hints how much buffering the media resource will likely need
        Value: ['none', 'metadata', 'auto']
        """
        
        def __init__(self, value):
            super().__init__("preload", value)
            


    class src(BaseAttribute):
        """
        audio attribute: src
        Description: Address of the resource
        Value: Valid non-empty URL potentially surrounded by spaces
        """
        
        def __init__(self, value):
            super().__init__("src", value)
            