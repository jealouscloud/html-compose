from collections.abc import Callable
from typing import Any, Literal

from .. import resource
from ..base_types import Node
from . import impl


def showcase(
    *fixtures,
    kwargs: dict[str, Any] | None = None,
    name: str | None = None,
    category: str | None = None,
    tags: list[str] | None = None,
    env: str = "default",
) -> Callable:
    """
    Register example fixtures for component preview and testing.

    You may set multiple showcases on the same component function with multiple
    decorator uses.

    Args:
        *fixtures:
            Zero or more arguments to be used as example inputs for the decorated function.

        kwargs:
            Optional dict of keyword arguments to be used as example inputs.

        name:
            Optional human-readable name for this showcase entry.
            Useful for distinguishing multiple showcases on the same component.

        category:
            Optional category string for grouping showcases in galleries or documentation.

        tags:
            Optional list of tag strings for filtering and organizing showcase entries.

        env:
            The environment in which this showcase should be active.
            Defaults to ``"default"``.

    Usage:
    ```python
    @showcase(example_post)
    @showcase(minimal_post, name="minimal")
    def post(post: blog_models.Post):
        return section(...)[...]
    ```
    This populates a gallery that can be viewed by running `html-compose gallery`
    """

    def decorator(func: Callable) -> Callable:
        func_fixtures: list[impl.ShowcaseEntry] = (
            impl.showcase_registry.setdefault(func, [])
        )
        func_fixtures.append(
            impl.ShowcaseEntry(fixtures, kwargs, name, category, tags, env)
        )

        # Attach metadata for introspection
        if not hasattr(func, "__showcases__"):
            func.__showcases__ = []  # type: ignore[attr-defined]
        func.__showcases__.extend(fixtures)  # type: ignore[attr-defined]

        return func

    return decorator


def declare_environment(
    env: str = "default",
    css: list[resource.css_import | str] | None = None,
    js: list[resource.js_import | str] | None = None,
    fonts: list[resource.font_import_manual | resource.font_import_provider]
    | None = None,
    isolation: Literal["shadow-dom", "iframe", "none"] = "none",
    parent: str | None = None,
    body_override: Node | None = None,
    parent_element: Node | None = None,
):
    """
    Declare resources for a named environment.
    Environments can be referenced by showcases to control their setup.

    Args:
        env: Name of the environment.

        css: List of CSS imports to include.

        js: List of JS imports to include.

        fonts: List of font imports to include.

        isolation: Isolation mode for the environment.

        parent: Name of a parent environment to inherit resources from.

        body_override: Optional body content to replace the default.

        parent_element: Optional parent element for the environment.
                        If body_override is set, this is required and must be
                        an element within the body_override.
    """
    if env in impl.env_registry:
        raise ValueError(f"Environment '{env}' is already declared")

    if isolation == "none":
        for e in impl.env_registry.values():
            if e.isolation == "none":
                raise ValueError(
                    "Only one environment can have 'none' isolation"
                )
    if body_override is not None and parent_element is None:
        raise ValueError(
            "If body_override is set, parent_element must also be provided"
        )
    if parent_element is not None and body_override is None:
        raise ValueError(
            "If parent_element is set, body_override must also be provided"
        )

    impl.env_registry[env] = impl.ShowcaseEnvironment(
        css=css or [],
        js=js or [],
        fonts=fonts or [],
        isolation=isolation,
        parent=parent,
        body_override=body_override,
        parent_element=parent_element,
    )
