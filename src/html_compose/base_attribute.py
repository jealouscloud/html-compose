from typing import Callable, Iterable, TypeAlias, Union

from markupsafe import Markup, escape

from . import util_funcs


def escape_text(value) -> str:
    return escape(str(value))


def unsafe_text(value) -> str:
    return Markup(str(value))


BoolCallable: TypeAlias = Callable[[], bool]

Resolveable: TypeAlias = Union[
    None,
    str,
    list[str],
    dict[str, str],
    dict[str, BoolCallable],
    list[Callable],
]


class BaseAttribute:
    """
    Base class for all HTML element attributes. It resolves to a string.

    Attribute Reference: https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes
    """

    def __init__(self, name, data: Resolveable = None):
        self.name = name
        self.data = data

    def resolve_key_value(self, key, value):
        """
        Resolve key value pair

        Default implementation:
        - If value is None, return None
        - If value is a bool, return key if True
        - If value is a callable, call and use above logic
        """

        def resolve_value(value):
            if value is None:
                return None

            if isinstance(value, bool):
                return key if value else None

            raise ValueError(
                f"Value must be a bool, NoneType or callable, got {type(value)}"
            )

        if callable(value):
            return resolve_value(value())

        return resolve_value(value)

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
            if callable(data_provider):
                yield data_provider()
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
        """
        for key, value in data.items():
            result = self.resolve_key_value(key, value)
            if result:
                yield result

    def resolve_data(self, element):
        """
        Resolve right half of attribute
        """

        # Just a string
        if isinstance(self.data, str):
            return self.data

        if isinstance(self.data, int):
            return str(self.data)

        # Just a bool that needs to be marhalled to a string
        if isinstance(self.data, bool):
            return "true" if self.data else "false"

        if self.data is None:
            return None

        # Just a callable
        if callable(self.data):
            param_count = util_funcs.get_param_count(self.data)
            if param_count == 0:
                data = self.data()
            if param_count == 1:
                data = self.data(element)
        else:
            data = self.data

        _resolved = None

        # List of strings or callables
        if isinstance(data, list):
            _resolved = self.list_string_generator(data)
        # dictionary of key value pairs

        if isinstance(data, dict):
            _resolved = self.dict_string_generator()
        else:
            raise ValueError(f"Input data type {data} not supported")

        return self.resolve_join(_resolved)

    def evaluate(self, element):
        """
        Evaluate attribute, return key, value as tuple
        """
        resolved = self.resolve_data(element)
        return (self.name, resolved)

    def __repr__(self):
        return self.evaluate()
