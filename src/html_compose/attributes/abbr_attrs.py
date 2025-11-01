from . import BaseAttribute
from ..base_types import StrLike


class AbbrAttrs:
    """
    This module contains functions for attributes in the 'abbr' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def title(value: StrLike) -> BaseAttribute:
        """
        "abbr" attribute: title
        Full term or expansion of abbreviation

        Args:
            value:
                Text

        Returns:
            An title attribute to be added to your element

        """

        return BaseAttribute("title", value)
