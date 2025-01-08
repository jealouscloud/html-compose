from typing import Iterable, TypeAlias, Union

from markupsafe import Markup


def unsafe_text(value) -> str:
    return Markup(str(value))


Resolveable: TypeAlias = Union[
    None,
    str,
    list[str],
    dict[str, str],
]


class BaseAttribute:
    """
    Base class for all HTML element attributes. It resolves to a string.

    Attribute Reference: https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes
    """

    def __init__(self, name, data: Resolveable = None):
        self.name = name
        self.data = data

    def resolve_join(self, input_data: Iterable):
        """
        Join a list of strings
        Split out for implementors to override
        """
        return " ".join(input_data)

    def list_string_generator(self, data):
        """
        Resolve list into string list (generator)
        """
        for data_provider in data:
            # You're gonna be a string then
            if not isinstance(data_provider, str):
                raise ValueError(
                    f"Input data must be a string, got {type(data_provider)}"
                )
            yield data_provider

    def dict_string_generator(self, data):
        """
        Resolve dictionary into string list (generator)

        Keys are returned if value is truthy
        The value only determines if the key should be included
        """
        for key, value in data.items():
            if not value:
                continue
            yield key

    def resolve_data(self):
        """
        Resolve right half of attribute into a string

        A resolved string is returned from the input or resolved list/dict
        """

        data = self.data
        # Just a string
        if isinstance(data, str):
            return data

        if isinstance(data, int):
            return str(data)

        # Just a bool that needs to be marshalled to a string
        # evaluate normally blocks this
        if isinstance(data, bool):
            return "true" if data else "false"

        if data is None:
            return None

        # a list which can be resolved via join
        _resolved = None

        # List of strings
        if isinstance(data, list):
            _resolved = self.list_string_generator(data)
        # dictionary of key value pairs
        elif isinstance(data, dict):
            _resolved = self.dict_string_generator()
        else:
            raise ValueError(f"Input data type {data} not supported")

        return self.resolve_join(_resolved)

    def evaluate(self):
        """
        Evaluate attribute, return key, value as tuple
        or None if attribute is falsey
        """
        if self.data is None or self.data is False:
            return None

        resolved = self.resolve_data()
        return (self.name, resolved)

    def __repr__(self):
        return self.evaluate()
