"""
Resource import helper classes

For javascript:
* Manage preload
* Manage import maps
* Manage cache busting for local resources
* Manage SRI hashes

For css:
* Manage preload
* Manage cache busting for local resources
* Manage SRI hashes

For fonts:
* Manage preconnect
* Manage preload
* Manage css @font-face generation or importing from providers i.e. Google Fonts

"""

import json
from typing import Any, Iterable

from .. import base_types, unsafe_text
from .. import elements as el


class settings:
    """
    Global settings for js_import/css_import behavior.

    `base_dir` is base directory from which local static files are served
    and is used to construct cache busting URLs.
    """

    # Base directory when resolving relative paths for local resources
    base_dir = "."
    # html-compose cache-buster timestamp
    query_string = "hccbts"
    # Maximum number of cached URIs for cache busting
    cache_cap = 1000
    stat_poll_interval: int | float = 1  # seconds


class _State:
    """
    Internal state for local static resource imports
    """

    stat_cache: dict[str, int | float] = {}

    misc_stat_cache: dict[str, int | float] = {}


from .css_import import css_import  # noqa: E402
from .font_import import font_import_manual, font_import_provider  # noqa: E402
from .js_import import js_import  # noqa: E402


def to_elements(
    js: Iterable[str | js_import] | None = None,
    css: Iterable[str | css_import] | None = None,
    fonts: Iterable[font_import_manual | font_import_provider] | None = None,
):
    """
    Generate elements for `head` element from resource imports

    Depending on your use case consider caching the resolution of this function


    :param js: Javascript imports. A string is treated as a simple script src
    :param css: CSS imports. A string is treated as a simple link rel=stylesheet
    :param fonts: Font imports
    """
    head_elements: list[base_types.Node] = []

    preconnect_links = []
    preload_links = []
    links = []
    if css:
        for css_resource in css:
            if isinstance(css_resource, css_import):
                for link in css_resource.links():
                    links.append(link)
                for preload in css_resource.preloads():
                    preload_links.append(preload)
            else:
                if not isinstance(css_resource, str):
                    raise TypeError("css must be str or css_import")

                links.append(el.link(rel="stylesheet", href=css_resource))

    script_tags = []
    if js:
        #  <link rel="modulepreload" href="main.js" />
        js_imports: dict[str, str] = {}
        scopes: dict[str, dict[str, str]] = {}
        for js_src in js:
            if isinstance(js_src, js_import):
                jsi: js_import = js_src
                # Generate script tag
                script_tags.append(jsi.script())
                link = jsi.preload_link()
                if link:
                    preload_links.append(link)

                entry = jsi.import_map_entry()
                if entry:
                    # Add to import map
                    name, src = entry[0:2]
                    js_imports[name] = src
                    if len(entry) == 3:
                        # Scopes feature, although I can't imagine anyone
                        # using it.
                        scope = str(entry[2])
                        sdict = scopes.setdefault(scope, {})
                        sdict[name] = src

            else:
                if not isinstance(js_src, str):
                    raise TypeError("js must be str or js_import")
                script_tags.append(el.script(src=js_src))

        if js_imports:
            import_map: dict[str, Any] = {"imports": js_imports}
            if scopes:
                import_map["scopes"] = scopes
            # dump to json; prevent escapes
            js_dump = json.dumps(import_map).replace("<", "\\u003c")
            script_tags.insert(
                0, el.script(type="importmap")[unsafe_text(js_dump)]
            )
    style_text: list[str] = []
    if fonts:
        for font in fonts:
            # Each font may be a different kind but the interface means
            # we capture anything they generate
            links.extend(font.links())
            preconnect_links.extend(font.preconnect_links())
            preload_links.extend(font.preload_links())
            style_data = font.style_data()
            if style_data:
                style_text.append(style_data)

    if preconnect_links:
        head_elements.extend(preconnect_links)

    if preload_links:
        head_elements.extend(preload_links)

    if links:
        head_elements.extend(links)

    if style_text:
        head_elements.append(el.style()[unsafe_text("\n".join(style_text))])

    if script_tags:
        head_elements.extend(script_tags)

    return head_elements


__all__ = [
    "js_import",
    "css_import",
    "font_import_manual",
    "font_import_provider",
    "to_elements",
    "settings",
]
