import urllib
import urllib.parse
from os import path, stat
from time import time

from . import _State, settings


def _cachebust_resource_uri(source: str):
    """
    Returns the source URI - with cache busting if enabled
    which is implemented by getting the mtime of the local file

    This operation performs up to two fs stats per call

    1. The base static directory is checked once and cached per interpreter
    2. The specific resource is checked if it is time to poll again
        based on settings.stat_poll_interval
    """

    misc_stat_cache = _State.misc_stat_cache
    stat_cache = _State.stat_cache
    base_dir = settings.base_dir

    if misc_stat_cache.get(base_dir) is None:
        try:
            misc_stat_cache[base_dir] = int(stat(base_dir).st_mtime)
        except FileNotFoundError as exc:
            raise FileNotFoundError(
                "js_import cache_bust enabled but "
                f"js_import.settings.base_dir {base_dir} "
                "does not exist"
            ) from exc

    source = source.lstrip("/")
    resource_path = path.join(base_dir, source)
    now = time()
    ts = misc_stat_cache.get(path.join(base_dir, source), None)
    update_ts = ts is None or (now - ts) > settings.stat_poll_interval
    if update_ts:
        try:
            ts = int(stat(resource_path).st_mtime)
        except FileNotFoundError as exc:
            raise FileNotFoundError(
                "js_import cache_bust enabled but "
                f"resource {resource_path} "
                "does not exist"
            ) from exc

        if len(stat_cache) >= settings.cache_cap:
            # Clear if it's too big
            stat_cache.clear()
        stat_cache[resource_path] = ts

    assert ts is not None, "ts should be set by now"

    spliturl = urllib.parse.urlsplit(source)
    pairs = urllib.parse.parse_qsl(
        spliturl.query,
        keep_blank_values=True,
        encoding="utf-8",
        errors="surrogateescape",
    )
    # add our cache buster
    pairs.append((settings.query_string, str(int(ts))))
    # re assemble the query string, try our best to preservees exactly
    new_qs = urllib.parse.urlencode(
        pairs,
        quote_via=urllib.parse.quote,
        encoding="utf-8",
        errors="surrogateescape",
    )
    return spliturl._replace(query=new_qs).geturl()
