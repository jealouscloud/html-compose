from . import BaseAttribute


class AbbrAttrs:
    """
    This module contains functions for attributes in the 'abbr' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def title(value: str) -> BaseAttribute:
        """
        "abbr" attribute: title  
        Full term or expansion of abbreviation  

        :param value: Text  
        :return: An title attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("title", value)
