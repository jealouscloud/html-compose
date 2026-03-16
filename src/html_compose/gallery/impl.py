import weakref
from collections.abc import Callable
from typing import Any, Literal, NamedTuple

from .. import render, resource
from ..base_types import Node


class ShowcaseEntry(NamedTuple):
    fixtures: Any
    kwargs: dict[str, Any] | None
    name: str | None
    category: str | None
    tags: list[str] | None
    env: str


class ShowcaseResult(NamedTuple):
    name: str | None
    func_name: str
    func_module: str
    category: str | None
    tags: list[str] | None
    success: bool
    result: str | Exception
    env: str


class ShowcaseEnvironment(NamedTuple):
    css: list[resource.css_import | str]
    js: list[resource.js_import | str]
    fonts: list[resource.font_import_manual | resource.font_import_provider]
    isolation: Literal["shadow-dom", "iframe", "none"]
    parent: str | None
    body_override: Node | None
    parent_element: Node | None


showcase_registry: weakref.WeakKeyDictionary[Callable, list[ShowcaseEntry]] = (
    weakref.WeakKeyDictionary()
)
env_registry: dict[str, ShowcaseEnvironment] = {}


def resolve_environment(env_name: str) -> ShowcaseEnvironment:
    """
    Resolve the environment by name, including inheritance.
    """
    if env_name not in env_registry:
        if env_name == "default":
            # Default environment
            return ShowcaseEnvironment(
                css=[],
                js=[],
                fonts=[],
                isolation="none",
                parent=None,
                body_override=None,
                parent_element=None,
            )

        raise ValueError(f"Environment '{env_name}' is not declared")

    env = env_registry[env_name]

    css: list[resource.css_import | str] = env.css
    js: list[resource.js_import | str] = env.js
    fonts: list[resource.font_import_manual | resource.font_import_provider] = (
        env.fonts
    )
    parent = env.parent
    parent_set = set()
    body_inherited = None
    parent_element_inherited = None
    while parent:
        # prevent infinite loop
        if parent in parent_set:
            raise ValueError(
                f"Circular environment inheritance detected at '{parent}'"
            )
        parent_set.add(parent)

        # Resolve parent
        parent_env = env_registry.get(parent)
        if not parent_env:
            raise ValueError(f"Environment '{parent}' is not declared")

        # Add its resources
        css = parent_env.css + css
        js = parent_env.js + js
        fonts = parent_env.fonts + fonts
        # If we haven't previously inherited a body, take this one
        if body_inherited is None and parent_env.body_override is not None:
            body_inherited = parent_env.body_override
            parent_element_inherited = parent_env.parent_element

        parent = parent_env.parent

    body_override = (
        env.body_override if env.body_override is not None else body_inherited
    )
    parent_element = (
        env.parent_element
        if env.parent_element is not None
        else parent_element_inherited
    )
    return ShowcaseEnvironment(
        css=css,
        js=js,
        fonts=fonts,
        isolation=env.isolation,
        parent=env.parent,
        body_override=body_override,
        parent_element=parent_element,
    )


def prepare(fn, showcase_entry: ShowcaseEntry) -> tuple[bool, str | Exception]:
    """
    Prepare the function with the given showcase entry.
    This may involve setting up the environment, injecting fixtures, etc.
    """
    try:
        env = resolve_environment(showcase_entry.env)
        component = fn(
            *showcase_entry.fixtures, **(showcase_entry.kwargs or {})
        )

        if env.body_override is not None and env.parent_element is not None:
            env.parent_element.append(component)  # type: ignore
            try:
                html = render(env.body_override)
            finally:
                env.parent_element._children.pop()  # type: ignore
        else:
            html = render(component)
    except Exception as e:
        return False, e
    return True, html


def show_showcases(
    filter_allows: Callable[[ShowcaseEntry], bool] | None = None,
) -> list[ShowcaseResult]:
    """
    Return all registered showcases, optionally filtered by a predicate.
    """
    all_showcases: list[ShowcaseResult] = []
    for func, entries in showcase_registry.items():
        for entry in entries:
            if filter_allows is None or filter_allows(entry):
                success, result = prepare(func, entry)
                all_showcases.append(
                    ShowcaseResult(
                        name=entry.name,
                        func_name=func.__qualname__,
                        func_module=func.__module__,
                        category=entry.category,
                        tags=entry.tags,
                        success=success,
                        result=result,
                        env=entry.env,
                    )
                )
    return all_showcases
