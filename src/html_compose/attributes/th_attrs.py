from . import BaseAttribute


class ThAttrs:
    """
    This module contains classes for attributes in the <th> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """

    class abbr(BaseAttribute):
        """
        th attribute: abbr
        Description: Alternative label to use for the header cell when referencing the cell in other contexts
        Value: Text*
        """

        def __init__(self, value: str):
            super().__init__("abbr", value)

    class colspan(BaseAttribute):
        """
        th attribute: colspan
        Description: Number of columns that the cell is to span
        Value: Valid non-negative integer greater than zero
        """

        def __init__(self, value):
            super().__init__("colspan", value)

    class headers(BaseAttribute):
        """
        th attribute: headers
        Description: The header cells for this cell
        Value: Unordered set of unique space-separated tokens consisting of IDs*
        """

        def __init__(self, value):
            super().__init__("headers", value)

    class rowspan(BaseAttribute):
        """
        th attribute: rowspan
        Description: Number of rows that the cell is to span
        Value: Valid non-negative integer
        """

        def __init__(self, value: int):
            super().__init__("rowspan", value)

    class scope(BaseAttribute):
        """
        th attribute: scope
        Description: Specifies which cells the header cell applies to
        Value: ['row', 'col', 'rowgroup', 'colgroup']
        """

        def __init__(self, value):
            super().__init__("scope", value)
