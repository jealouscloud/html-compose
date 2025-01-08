from . import BaseAttribute
from typing import Literal, Union

class AnchorAttrs:
    """ 
    This module contains classes for attributes in the <a> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """ 
    
    class download(BaseAttribute):
        """
        a attribute: download
        Description: Whether to download the resource instead of navigating to it, and its filename if so
        Value: Text
        """
        
        def __init__(self, value: str):
            super().__init__("download", value)
            


    class href(BaseAttribute):
        """
        a attribute: href
        Description: Address of the hyperlink
        Value: Valid URL potentially surrounded by spaces
        """
        
        def __init__(self, value):
            super().__init__("href", value)
            


    class hreflang(BaseAttribute):
        """
        a attribute: hreflang
        Description: Language of the linked resource
        Value: Valid BCP 47 language tag
        """
        
        def __init__(self, value):
            super().__init__("hreflang", value)
            


    class ping(BaseAttribute):
        """
        a attribute: ping
        Description: URLs to ping
        Value: Set of space-separated tokens consisting of valid non-empty URLs
        """
        
        def __init__(self, value):
            super().__init__("ping", value)
            


    class referrerpolicy(BaseAttribute):
        """
        a attribute: referrerpolicy
        Description: Referrer policy for fetches initiated by the element
        Value: Referrer policy
        """
        
        def __init__(self, value):
            super().__init__("referrerpolicy", value)
            


    class rel(BaseAttribute):
        """
        a attribute: rel
        Description: Relationship between the location in the document containing the hyperlink and the destination resource
        Value: Unordered set of unique space-separated tokens*
        """
        
        def __init__(self, value):
            super().__init__("rel", value)
            


    class target(BaseAttribute):
        """
        a attribute: target
        Description: Navigable for hyperlink navigation
        Value: Valid navigable target name or keyword
        """
        
        def __init__(self, value):
            super().__init__("target", value)
            


    class type(BaseAttribute):
        """
        a attribute: type
        Description: Hint for the type of the referenced resource
        Value: Valid MIME type string
        """
        
        def __init__(self, value):
            super().__init__("type", value)
            