from . import BaseAttribute


class MapAttrs:
    """
    This module contains functions for attributes in the 'map' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def name(value: str) -> BaseAttribute:
        """
        "map" attribute: name  
        Name of image map to reference from the usemap attribute  

        :param value: Text*  
        :return: An name attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("name", value)
