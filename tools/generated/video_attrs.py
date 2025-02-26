from . import BaseAttribute
from typing import Literal, Union

class VideoAttrs:
    """ 
    This module contains classes for attributes in the <video> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """ 
    
    class autoplay(BaseAttribute):
        """
        video attribute: autoplay
        Description: Hint that the media resource can be started automatically when the page is loaded
        Value: Boolean attribute
        """
        
        def __init__(self, value: bool):
            super().__init__("autoplay", value)
            


    class controls(BaseAttribute):
        """
        video attribute: controls
        Description: Show user agent controls
        Value: Boolean attribute
        """
        
        def __init__(self, value: bool):
            super().__init__("controls", value)
            


    class crossorigin(BaseAttribute):
        """
        video attribute: crossorigin
        Description: How the element handles crossorigin requests
        Value: ['anonymous', 'use-credentials']
        """
        
        def __init__(self, value):
            super().__init__("crossorigin", value)
            


    class height(BaseAttribute):
        """
        video attribute: height
        Description: Vertical dimension
        Value: Valid non-negative integer
        """
        
        def __init__(self, value: int):
            super().__init__("height", value)
            


    class loop(BaseAttribute):
        """
        video attribute: loop
        Description: Whether to loop the media resource
        Value: Boolean attribute
        """
        
        def __init__(self, value: bool):
            super().__init__("loop", value)
            


    class muted(BaseAttribute):
        """
        video attribute: muted
        Description: Whether to mute the media resource by default
        Value: Boolean attribute
        """
        
        def __init__(self, value: bool):
            super().__init__("muted", value)
            


    class playsinline(BaseAttribute):
        """
        video attribute: playsinline
        Description: Encourage the user agent to display video content within the element's playback area
        Value: Boolean attribute
        """
        
        def __init__(self, value: bool):
            super().__init__("playsinline", value)
            


    class poster(BaseAttribute):
        """
        video attribute: poster
        Description: Poster frame to show prior to video playback
        Value: Valid non-empty URL potentially surrounded by spaces
        """
        
        def __init__(self, value):
            super().__init__("poster", value)
            


    class preload(BaseAttribute):
        """
        video attribute: preload
        Description: Hints how much buffering the media resource will likely need
        Value: ['none', 'metadata', 'auto']
        """
        
        def __init__(self, value):
            super().__init__("preload", value)
            


    class src(BaseAttribute):
        """
        video attribute: src
        Description: Address of the resource
        Value: Valid non-empty URL potentially surrounded by spaces
        """
        
        def __init__(self, value):
            super().__init__("src", value)
            


    class width(BaseAttribute):
        """
        video attribute: width
        Description: Horizontal dimension
        Value: Valid non-negative integer
        """
        
        def __init__(self, value: int):
            super().__init__("width", value)
            