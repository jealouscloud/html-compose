from . import BaseAttribute
from typing import Literal, Union

class BodyAttrs:
    """ 
    This module contains classes for attributes in the <body> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """ 
    
    class onafterprint(BaseAttribute):
        """
        body attribute: onafterprint
        Description: afterprint event handler for Window object
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onafterprint", value)
            


    class onbeforeprint(BaseAttribute):
        """
        body attribute: onbeforeprint
        Description: beforeprint event handler for Window object
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onbeforeprint", value)
            


    class onbeforeunload(BaseAttribute):
        """
        body attribute: onbeforeunload
        Description: beforeunload event handler for Window object
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onbeforeunload", value)
            


    class onhashchange(BaseAttribute):
        """
        body attribute: onhashchange
        Description: hashchange event handler for Window object
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onhashchange", value)
            


    class onlanguagechange(BaseAttribute):
        """
        body attribute: onlanguagechange
        Description: languagechange event handler for Window object
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onlanguagechange", value)
            


    class onmessage(BaseAttribute):
        """
        body attribute: onmessage
        Description: message event handler for Window object
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onmessage", value)
            


    class onmessageerror(BaseAttribute):
        """
        body attribute: onmessageerror
        Description: messageerror event handler for Window object
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onmessageerror", value)
            


    class onoffline(BaseAttribute):
        """
        body attribute: onoffline
        Description: offline event handler for Window object
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onoffline", value)
            


    class ononline(BaseAttribute):
        """
        body attribute: ononline
        Description: online event handler for Window object
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("ononline", value)
            


    class onpagehide(BaseAttribute):
        """
        body attribute: onpagehide
        Description: pagehide event handler for Window object
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onpagehide", value)
            


    class onpagereveal(BaseAttribute):
        """
        body attribute: onpagereveal
        Description: pagereveal event handler for Window object
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onpagereveal", value)
            


    class onpageshow(BaseAttribute):
        """
        body attribute: onpageshow
        Description: pageshow event handler for Window object
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onpageshow", value)
            


    class onpageswap(BaseAttribute):
        """
        body attribute: onpageswap
        Description: pageswap event handler for Window object
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onpageswap", value)
            


    class onpopstate(BaseAttribute):
        """
        body attribute: onpopstate
        Description: popstate event handler for Window object
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onpopstate", value)
            


    class onrejectionhandled(BaseAttribute):
        """
        body attribute: onrejectionhandled
        Description: rejectionhandled event handler for Window object
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onrejectionhandled", value)
            


    class onstorage(BaseAttribute):
        """
        body attribute: onstorage
        Description: storage event handler for Window object
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onstorage", value)
            


    class onunhandledrejection(BaseAttribute):
        """
        body attribute: onunhandledrejection
        Description: unhandledrejection event handler for Window object
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onunhandledrejection", value)
            


    class onunload(BaseAttribute):
        """
        body attribute: onunload
        Description: unload event handler for Window object
        Value: Event handler content attribute
        """
        
        def __init__(self, value):
            super().__init__("onunload", value)
            