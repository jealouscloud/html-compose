import pytest

import html_compose as ht
from html_compose.gallery import declare_environment, showcase
from html_compose.gallery.impl import (
    env_registry,
    resolve_environment,
    show_showcases,
    showcase_registry,
)


@pytest.fixture(autouse=True)
def clean_registries():
    """Clear global registries between tests"""
    showcase_registry.clear()
    env_registry.clear()
    yield
    showcase_registry.clear()
    env_registry.clear()


# --- showcase decorator ---


def test_showcase_decorator():
    @showcase("example2", name="example_2", category="text")
    @showcase("example1", name="example_1", category="text")
    def my_component(text: str) -> list:
        return [ht.li()[text], ht.li["Static item"]]

    showcases = showcase_registry.get(my_component, [])
    assert len(showcases) == 2
    assert showcases[0].name == "example_1"
    assert showcases[0].category == "text"

    assert showcases[1].name == "example_2"
    assert showcases[1].category == "text"


def test_showcase_no_fixtures():
    """@showcase() with no fixtures registers with empty tuple"""

    @showcase()
    def my_component():
        return []

    showcases = showcase_registry.get(my_component, [])
    assert len(showcases) == 1
    assert showcases[0].fixtures == ()
    assert showcases[0].name is None
    assert showcases[0].category is None


def test_showcase_callable_fixture():
    """@showcase(callable) correctly treats the callable as a fixture, not the decorated function"""

    def my_fixture():
        return "test data"

    @showcase(my_fixture)
    def my_component(data):
        return [ht.div[data]]

    showcases = showcase_registry.get(my_component, [])
    assert len(showcases) == 1
    assert showcases[0].fixtures == (my_fixture,)


def test_showcase_kwargs():
    @showcase("hello", kwargs={"style": "bold"}, name="with_style")
    def my_component(text, style="normal"):
        return ht.div[f"{text} ({style})"]

    results = show_showcases()
    assert len(results) == 1
    assert results[0].success is True
    assert "bold" in results[0].result


# --- prepare / show_showcases ---


def test_prepare_renders_component():
    @showcase("world")
    def greeting(name):
        return ht.span[f"hello {name}"]

    results = show_showcases()
    assert len(results) == 1
    assert results[0].success is True
    assert "hello world" in results[0].result


def test_prepare_catches_exceptions():
    @showcase("bad input")
    def broken(x):
        raise ValueError("intentional")

    results = show_showcases()
    assert len(results) == 1
    assert results[0].success is False
    assert isinstance(results[0].result, ValueError)


# --- declare_environment validation ---


def test_declare_environment_body_override_requires_parent_element():
    with pytest.raises(
        ValueError, match="parent_element must also be provided"
    ):
        declare_environment(
            env="test", isolation="iframe", body_override=ht.div["wrapper"]
        )


def test_declare_environment_parent_element_requires_body_override():
    with pytest.raises(ValueError, match="body_override must also be provided"):
        declare_environment(
            env="test", isolation="iframe", parent_element=ht.div()
        )


def test_declare_environment_duplicate_raises():
    declare_environment(env="dup", isolation="iframe")
    with pytest.raises(ValueError, match="already declared"):
        declare_environment(env="dup", isolation="iframe")


# --- body_override rendering ---


def test_body_override_wraps_component():
    """Component renders inside the parent_element within body_override"""
    container = ht.main(class_="content")
    layout = ht.div(class_="app-shell")[ht.nav["sidebar"], container]
    declare_environment(
        env="wrapped",
        isolation="iframe",
        body_override=layout,
        parent_element=container,
    )

    @showcase("test content", env="wrapped")
    def my_component(text):
        return ht.p[text]

    results = show_showcases()
    assert len(results) == 1
    assert results[0].success is True
    html = results[0].result
    # Component should be inside the layout
    assert "app-shell" in html
    assert "sidebar" in html
    assert "test content" in html


def test_body_override_cleans_up_after_render():
    """parent_element is not permanently mutated after prepare()"""
    container = ht.main()
    layout = ht.div[container]
    declare_environment(
        env="cleanup",
        isolation="iframe",
        body_override=layout,
        parent_element=container,
    )

    @showcase("first", env="cleanup")
    def comp_a(text):
        return ht.span[text]

    # Render once
    results = show_showcases()
    assert results[0].success is True

    # The container should be clean — no leftover children from previous render
    assert len(container._children) == 0


def test_body_override_multiple_showcases_same_env():
    """Multiple showcases using the same body_override env render independently"""
    container = ht.main()
    layout = ht.div(class_="shell")[container]
    declare_environment(
        env="shared",
        isolation="iframe",
        body_override=layout,
        parent_element=container,
    )

    @showcase("alpha", name="a", env="shared")
    @showcase("beta", name="b", env="shared")
    def my_component(text):
        return ht.p[text]

    results = show_showcases()
    assert len(results) == 2
    assert results[0].success is True
    assert results[1].success is True
    # Decorator order: beta registered first (inner), alpha second (outer)
    assert results[0].name == "b"
    assert results[1].name == "a"
    # Each should contain only its own content, not the other's
    assert "beta" in results[0].result
    assert "alpha" not in results[0].result
    assert "alpha" in results[1].result
    assert "beta" not in results[1].result


# --- environment inheritance ---


def test_environment_inheritance_css():
    declare_environment(env="base", isolation="iframe", css=["base.css"])
    declare_environment(
        env="child", isolation="shadow-dom", parent="base", css=["child.css"]
    )

    resolved = resolve_environment("child")
    assert resolved.css == ["base.css", "child.css"]


def test_environment_inheritance_body_override_child_wins():
    """Child's body_override takes precedence over parent's"""
    parent_container = ht.div(class_="parent-container")
    parent_layout = ht.div(class_="parent-layout")[parent_container]
    declare_environment(
        env="parent",
        isolation="iframe",
        body_override=parent_layout,
        parent_element=parent_container,
    )

    child_container = ht.div(class_="child-container")
    child_layout = ht.div(class_="child-layout")[child_container]
    declare_environment(
        env="child",
        isolation="iframe",
        parent="parent",
        body_override=child_layout,
        parent_element=child_container,
    )

    resolved = resolve_environment("child")
    assert resolved.body_override is child_layout
    assert resolved.parent_element is child_container


def test_environment_inheritance_body_override_falls_back_to_parent():
    """If child doesn't set body_override, inherits from parent"""
    parent_container = ht.div(class_="parent-container")
    parent_layout = ht.div(class_="parent-layout")[parent_container]
    declare_environment(
        env="parent2",
        isolation="iframe",
        body_override=parent_layout,
        parent_element=parent_container,
    )

    declare_environment(env="child2", isolation="iframe", parent="parent2")

    resolved = resolve_environment("child2")
    assert resolved.body_override is parent_layout
    assert resolved.parent_element is parent_container


def test_environment_circular_inheritance_raises():
    declare_environment(env="a", isolation="iframe", parent="b")
    declare_environment(env="b", isolation="shadow-dom", parent="a")
    with pytest.raises(ValueError, match="Circular"):
        resolve_environment("a")
