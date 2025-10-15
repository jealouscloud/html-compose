from typing import Iterable, Literal

from .. import elements as el
from .util_funcs import _cachebust_resource_uri

_AUTODETECT_CSS_FONT_TYPES = {
    "otc": "collection",
    "ttc": "collection",
    "eot": "embedded-opentype",
    "otf": "opentype",
    "ttf": "truetype",
    "svg": "svg",
    "svgz": "svg",
    "woff": "woff",
    "woff2": "woff2",
}

_AUTODETECT_FONT_MIMETYPES = {
    "otc": "font/collection",
    "ttc": "font/collection",
    "eot": "application/vnd.ms-fontobject",
    "otf": "font/otf",
    "ttf": "font/ttf",
    "svg": "image/svg+xml",
    "woff": "font/woff",
    "woff2": "font/woff2",
}


class _font_import_base:
    def preload_links(self) -> list[el.link]:
        raise NotImplementedError()

    def links(self) -> list[el.link]:
        raise NotImplementedError()

    def style_data(self) -> str:
        raise NotImplementedError()

    def preconnect_links(self) -> list[el.link]:
        raise NotImplementedError()


class font_import_manual(_font_import_base):
    def __init__(
        self,
        hrefs: str | Iterable[str],
        family: str,
        weight: int
        | tuple
        | str
        | Literal["bold", "light", "lighter", "bolder", "normal"]
        | None = "normal",
        style: Literal["normal", "italic", "oblique"] | str = "normal",
        display: Literal["swap", "optional", "fallback", "auto", "block"]
        | str = "swap",
        preload: bool = True,
        crossorigin: Literal["", "anonymous", "use-credentials"] | None = None,
        unicode_range: str | None = None,
        cache_bust: bool = False,
    ) -> None:
        """
        Declare a web font via @font-face and (optionally) emit
        a preload `<link>`.
        This initializer targets the direct-file flow (you supply the exact .woff2 URL).

        If multiple hrefs are provided, preload must choose only one and so
        the first href is used for preload and the rest are only
        in the @font-face.

        Values are passed verbatim. NEVER use this with untrusted user input.

        Parameters
        ----------

        `hrefs`:
            1 or more URL to the font file (typically .woff2).
            Pass a str for a single URL, or an iterable of str for multiple URLs.

            The @font-face `src` will reference this URL verbatim.

        `family`:
            CSS `font-family` name to expose (e.g., "Noto Sans").
            Do not include quotes; they are added automatically.

        `weight`:
            Single numeric weight (e.g., 400) for a static face, or a `(low, high)`
            tuple (e.g., `(100, 900)`) for a variable font range.

        `style`:
            Font style for this face: `"normal"` or `"italic"`. Declare another
            instance for the other style if needed.

        `display`:
            `font-display` strategy. `"swap"` is a safe default to avoid FOIT.

        `preload`:
            If `True`, also create a `<link rel="preload" as="font" ...>` for `href`.
            Preload only warms the fetch; the @font-face rule still does the actual use.

        `crossorigin`:
            CORS mode for cross-origin fonts. When unset, it is
            fetched as same-origin Use `""` or `anonymous` for most CDN/remote
            cases, or `"use-credentials"` to pass cookies if strictly necessary.

        `unicode_range`:
            Optional CSS `unicode-range` (e.g., `"U+0000-00FF"`) to subset coverage.
        """
        if isinstance(hrefs, str):
            hrefs = [hrefs]
        self.hrefs = hrefs
        self.weight = weight
        self.style = style
        self.display = display
        self.preload = preload
        self.crossorigin = crossorigin
        self.cache_bust = cache_bust
        self.has_link = preload
        self.unicode_range = unicode_range
        self._hrefs = self.uris()

        # Escape most stuff that could break out of quotes
        safe_family = (
            family.replace("\\", "\\\\").replace("'", "\\'").replace('"', '\\"')
        )
        self.family = safe_family

    def uris(self) -> list[str]:  # -> list[str] | list[Any]:
        """
        Returns the source URI - with cache busting if enabled
        which is implemented by getting the mtime of the local file

        This operation performs up to two fs stats per call

        1. The base static directory is checked once and cached per interpreter
        2. The specific resource is checked if it is time to poll again
           based on settings.stat_poll_interval
        """
        hrefs = []
        for h in self.hrefs:
            if not self.cache_bust:
                hrefs.append(h)
                continue

            hrefs.append(_cachebust_resource_uri(h))
        return hrefs

    @staticmethod
    def get_font_format(href: str) -> str | None:
        ext = href.split(".")[-1].lower()
        return _AUTODETECT_CSS_FONT_TYPES.get(ext, None)

    @staticmethod
    def get_font_mime(href: str) -> str | None:
        ext = href.split(".")[-1].lower()
        return _AUTODETECT_FONT_MIMETYPES.get(ext, None)

    def preload_links(self) -> list[el.link]:
        """
        Returns preload links if preload is set
        """
        if not self.preload:
            return []

        first_href = self._hrefs[0]
        attrs = {"href": first_href}

        if self.crossorigin:
            attrs["crossorigin"] = self.crossorigin

        mimetype = font_import_manual.get_font_mime(first_href)

        if mimetype:
            attrs["type"] = mimetype

        return [el.link(attrs=attrs, rel="preload", as_="font")]

    def links(self) -> list[el.link]:
        return []

    def style_data(self) -> str:
        """
        Returns one or more nodes for this import
        """

        font_refs = []

        if len(self._hrefs) == 1:
            # we don't have to hint format if there's only one
            font_refs.append(f"url('{self._hrefs[0]}')")
        else:
            for h in self._hrefs:
                entry = f"url('{h}')"
                format = font_import_manual.get_font_format(h)
                if format:
                    entry += f" format('{format}')"

                font_refs.append(entry)

        if isinstance(self.weight, tuple):
            font_weight = f"{self.weight[0]} {self.weight[1]}"
        elif isinstance(self.weight, str):
            font_weight = self.weight
        elif isinstance(self.weight, int):
            font_weight = str(self.weight)
        else:
            raise TypeError("font weight must be int, str, or tuple")

        style_attrs = {
            "font-family": f"'{self.family}'",
            "src": ",\n\t\t".join(font_refs),
            "font-style": self.style,
            "font-display": self.display,
            "font-weight": font_weight,
            "unicode-range": self.unicode_range,
        }
        for k in list(style_attrs.keys()):
            v = style_attrs[k]
            if v is None:
                del style_attrs[k]

        return "\n".join(
            [
                "@font-face {",
                "".join(
                    [
                        "\t",
                        ";\n\t".join(
                            [f"{k}: {v}" for k, v in style_attrs.items()]
                        ),
                        ";",  # Ensure last property ends with semicolon
                    ]
                ),
                "}",
            ]
        )

    def preconnect_links(self) -> list[el.link]:
        return []


class font_import_provider(_font_import_base):
    def __init__(
        self,
        href: str,
        preload: bool = False,
        hash: str | None = None,
        crossorigin: Literal["", "anonymous", "user-credentials"]
        | str
        | None = None,
        cache_bust: bool = False,
        preconnect: list[str] | None = None,
        preconnect_crossorigin: Literal["", "anonymous", "user-credentials"]
        | None = None,
    ):
        """
        A font import helper class for css based imports which employs:
        - `link(rel="stylesheet")` to define the import
        - `link(rel="preload")` to preload the import
        - `link(rel="preconnect")` to preconnect to font providers
        - `hash` and `crossorigin` for SRI
        - Local resource cache busting

        NEVER use this with untrusted user input.

        Parameters
        ----------
        `href`:
            The literal href of the CSS resource which sets up the font

        `preload`:
            If true, adds a preload link for this resource

        `hash`:
            An optional SRI integrity hash for the import

        `crossorigin`:
            Optionally sets the crossorigin attribute on the link tag.
            Valid values are "", "anonymous", "use-credentials"

        `preconnect`:
            A list of URLs to preconnect to. This is useful for font providers
            such as Google Fonts.

        `preconnect_crossorigin`:
            Optionally sets the crossorigin attribute on the preconnect link tag.
            If not set, it defaults to the value of `crossorigin`.

        `cache_bust`:
            If true, appends a timestamp to the URL to prevent browser
            caching. Webservers configured for static resources manage this
            feature automatically, but for development this can be useful.

            This feature only works for local resources, i.e. those that
            exist in `resource.settings.base_dir`

        """
        self.href = href
        self.preload = preload
        self.hash = hash
        self.crossorigin = crossorigin
        self.cache_bust = cache_bust
        self.has_link = preload
        self._href = self.uri()
        self.preconnect = preconnect

        if hash and self.crossorigin is None:
            raise ValueError(
                "If hash is set, crossorigin must be set to ''/'anonymous'"
            )
        self.preconnect_crossorigin = preconnect_crossorigin
        if preconnect_crossorigin is None and self.crossorigin:
            if self.crossorigin != "user-credentials":
                self.preconnect_crossorigin = self.crossorigin  # type: ignore[assignment]
            else:
                raise ValueError(
                    "Please set preconnect_crossorigin explicitly if "
                    "crossorigin is 'user-credentials'"
                )

    def uri(self):
        """
        Returns the source URI - with cache busting if enabled
        which is implemented by getting the mtime of the local file

        This operation performs up to two fs stats per call

        1. The base static directory is checked once and cached per interpreter
        2. The specific resource is checked if it is time to poll again
           based on settings.stat_poll_interval
        """
        if not self.cache_bust:
            return self.href

        return _cachebust_resource_uri(self.href)

    def preload_links(
        self,
    ) -> list[el.link]:  # -> list[Any]:# -> list[Any]:# -> list[Any]:
        """
        Returns preload links if preload is set
        """

        links = []

        if self.preload:
            attrs = {"href": self._href}
            if self.hash:
                attrs["integrity"] = self.hash
            if self.crossorigin:
                attrs["crossorigin"] = self.crossorigin
            links.append(el.link(attrs=attrs, rel="preload", as_="style"))

        return links

    def links(self) -> list[el.link]:
        """
        Returns link elements for this import
        """
        links = []

        attrs = {"href": self._href}
        if self.hash:
            attrs["integrity"] = self.hash
        if self.crossorigin:
            attrs["crossorigin"] = self.crossorigin

        links.append(el.link(attrs=attrs, rel="stylesheet"))

        return links

    def style_data(self) -> str:
        # Fonts imported via CSS do not have style nodes
        return ""

    def preconnect_links(self) -> list[el.link]:
        """
        Returns generated preconnect link elements for this import
        """
        links = []
        if self.preconnect:
            for pc in self.preconnect:
                pc_attrs = {"href": pc}
                if self.preconnect_crossorigin:
                    pc_attrs["crossorigin"] = self.preconnect_crossorigin
                links.append(el.link(attrs=pc_attrs, rel="preconnect"))
        return links
