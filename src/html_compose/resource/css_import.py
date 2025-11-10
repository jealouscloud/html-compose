from typing import Literal

from .. import elements as el
from .util_funcs import _cachebust_resource_uri


class css_import:
    """
    A css import helper class which employs:
    - `link(rel="stylesheet")` to define the import
    - `link(rel="preload")` to preload the import
    - `hash` and `crossorigin` for SRI
    - Local resource cache busting

    An production usage might look like:
    ```python
    [
    css_import('./static/admin.css',
                cache_bust=True),

    css_import(
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css",
        hash=(
            "sha384-9ndCyUaIbzAi2FUVXJi0CjmCapS"
            "mO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM"
            ),
        crossorigin="anonymous",
        preload=True
    )

    ]
    ```

    ## Generated "HTML":

    ```python
    import json
    from html_compose import el

    [
        link(rel='preload',
            href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css',
            as_='style',
            integrity='sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7'
            'SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM',
            crossorigin='anonymous'),

        link(rel='stylesheet', href='./static/admin.css?ts=1760153426'),

        link(rel='stylesheet',
            href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css',
            integrity='sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7'
            'SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM',
            crossorigin='anonymous')
    ]
    ```

    See:
        https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload
        https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity
        https://www.srihash.org/

    """

    def __init__(
        self,
        href: str,
        preload: bool = False,
        hash: str | None = None,
        crossorigin: Literal["", "anonymous", "user-credentials"]
        | str
        | None = None,
        cache_bust: bool = False,
    ):
        """
        A css import wrapper to wrap some of the complexity of optimal
        resource loading.


        Parameters
        ----------
        `href`:
            The literal href passed to the link tag

        `preload`:
            If true, adds a preload link for this resource

        `hash`:
            An optional SRI integrity hash for the import

        `crossorigin`:
            Optionally sets the crossorigin attribute on the link tag.
            Valid values are "", "anonymous", "use-credentials"

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

        if hash and self.crossorigin is None:
            raise ValueError(
                "If hash is set, crossorigin must be set to ''/'anonymous'"
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

    def preloads(self) -> list[el.link]:
        """
        Returns a link element for preloading this import if preload is set
        """
        attrs = {"href": self._href}
        if self.hash:
            attrs["integrity"] = self.hash
        if self.crossorigin:
            attrs["crossorigin"] = self.crossorigin
        if self.preload:
            return [el.link(attrs=attrs, rel="preload", as_="style")]

        return []

    def links(self):
        """
        Returns one or more link element for this import
        """
        links = []
        attrs = {"href": self._href}
        if self.hash:
            attrs["integrity"] = self.hash
        if self.crossorigin:
            attrs["crossorigin"] = self.crossorigin

        links.append(el.link(attrs=attrs, rel="stylesheet"))

        return links
