import re
from typing import cast
from urllib.parse import urlencode

import html_compose as ht
from html_compose.base_types import Node
from html_compose.document import _livereload_script_tag, document_generator
from html_compose.elements import div, meta, title

from .. import resource
from .impl import ShowcaseResult, resolve_environment
from .resources import GALLERY_STYLES, NAV_STYLES, IframeScripts


class Settings:
    livereload_host = "localhost"
    livereload_port = 51353


def doc(body):
    return document_generator(
        head=[
            meta(charset="UTF-8"),
            meta(
                name="viewport", content="width=device-width, initial-scale=1"
            ),
            ht.style()[GALLERY_STYLES],
            title["Gallery"],
            _livereload_script_tag(
                dict(
                    host=Settings.livereload_host,
                    port=Settings.livereload_port,
                    proxy_host=None,
                    proxy_uri=None,
                )
            ),
        ],
        body=body,
    )


def showcase_id(result: ShowcaseResult) -> str:
    """Generate a stable ID for a showcase, used for anchors and element IDs."""
    base = f"{result.func_module}-{result.func_name}"
    if result.name:
        base += f"-{result.name}"
    # Sanitize for use as HTML id - keep only alphanumeric and hyphens
    sanitized = re.sub(r"[^a-zA-Z0-9-]", "-", base)
    # Collapse multiple hyphens
    sanitized = re.sub(r"-+", "-", sanitized)
    return sanitized.lower().strip("-")


def main_left_panel(modules: dict[str, list[ShowcaseResult]]):
    panel_sections = []

    for module, results in modules.items():
        showcases_by_function: dict[str, list[tuple[str, ShowcaseResult]]] = {}
        function_groups = []
        for r in results:
            grouped_showcases = showcases_by_function.setdefault(
                r.func_name, []
            )
            # Use showcase name, or function name with variant number if unnamed
            if r.name:
                display = r.name
            else:
                variant_num = len(grouped_showcases) + 1
                display = f"{r.func_name.replace('_', ' ')} #{variant_num}"
            grouped_showcases.append((display, r))

        for call_name, grouped_showcases in showcases_by_function.items():
            showcase_links = [
                ht.li()[ht.a(href=f"#{showcase_id(result)}")[name]]
                for name, result in grouped_showcases
            ]
            function_groups.append(
                ht.details()[ht.summary()[call_name], ht.ul()[showcase_links]]
            )

        module_section = ht.details(open=True)[
            ht.summary()[module], ht.ul()[function_groups]
        ]
        panel_sections.append(module_section)
    return [ht.style()[NAV_STYLES], ht.ul()[panel_sections]]


def get_showcase(result: ShowcaseResult) -> Node:
    """Create a self-contained page for a single showcase entry."""
    env = resolve_environment(result.env)
    # Use the showcase name if provided, otherwise use the function name
    display_name = result.name or result.func_name.replace("_", " ")
    resource_elements = resource.to_elements(
        js=env.js, css=env.css, fonts=env.fonts
    )
    broken = result.success is False
    card_id = showcase_id(result)
    standalone_url = f"/showcase/{result.func_module}/{result.func_name}"
    if result.name:
        standalone_url += f"?{urlencode({'name': result.name})}"

    header = ht.div(class_="o-showcase-header")[
        ht.span(class_="o-showcase-title")[
            "[broken] " if broken else "", display_name
        ],
        ht.a(
            class_="o-showcase-link",
            href=standalone_url,
            target="_blank",
            title="Open standalone",
        )["↗"],
    ]

    if env.isolation == "shadow-dom":
        content = ht.div(class_="o-showcase-content")[
            ht.template(shadowrootmode="open")[
                resource_elements, ht.unsafe_text(cast(str, result.result))
            ]
        ]
    elif env.isolation == "iframe":
        iframe_content = [
            # inject CSS to reliably hide scrollbars
            ht.style["html, body { overflow: hidden; }"],
            resource_elements,
            ht.unsafe_text(cast(str, result.result)),
        ]
        content = ht.iframe(
            id=f"iframe-{card_id}",
            class_="o-showcase-content",
            srcdoc=ht.render(iframe_content),
        )
    else:
        # no isolation
        content = ht.div(class_="o-showcase-content")[
            ht.unsafe_text(cast(str, result.result))
        ]

    return ht.div(class_="o-showcase-card", id=card_id)[header, content]


def get_showcases(content: list[ShowcaseResult]) -> list[Node]:
    return [get_showcase(result) for result in content]


def main_body(
    modules: dict[str, list[ShowcaseResult]], content: list[ShowcaseResult]
):
    resources = None
    for e in content:
        env = resolve_environment(e.env)
        # There can only be one 'none' isolation environment and it
        # sets up the whole page
        if env.isolation == "none":
            resources = resource.to_elements(
                js=env.js, css=env.css, fonts=env.fonts
            )

    return [
        resources,
        ht.script()[ht.unsafe_text(IframeScripts.parent)],
        div(class_="o-gallery-container")[
            div(class_="o-left-panel")[
                ht.template(shadowrootmode="open")[main_left_panel(modules)]
            ],
            div(class_="o-center-panel")[get_showcases(content)],
            div(class_="o-right-panel"),
        ],
    ]


def main_route(content: list[ShowcaseResult]) -> str:
    """
    Main gallery page showing all showcases
    """
    modules: dict[str, list[ShowcaseResult]] = {}
    for result in content:
        modules.setdefault(result.func_module, []).append(result)

    body_content = main_body(modules, content)
    return doc(body_content)


def generate_showcase(result: ShowcaseResult) -> str:
    """
    Single page view of a showcase
    """
    assert result.success, "Cannot generate showcase for failed result"
    assert isinstance(result.result, str)
    env = resolve_environment(result.env)
    resources = resource.to_elements(js=env.js, css=env.css, fonts=env.fonts)
    return doc(
        [
            resources,
            ht.script()[ht.unsafe_text(IframeScripts.parent)],
            ht.unsafe_text(result.result),
        ]
    )
