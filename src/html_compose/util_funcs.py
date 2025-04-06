import inspect
from functools import lru_cache
from os import getenv
from pathlib import PurePath
from typing import Any, Generator, Iterable, Optional


def join_attrs(k, value_trusted):
    """
    Join escaped value to key in form key="value"
    """
    return f'{k}="{value_trusted}"'


def is_iterable_but_not_str(input_iterable):
    """
    Check if an iterable is not a string or bytes.
    Which prevents some bugs.
    """
    return isinstance(input_iterable, Iterable) and not isinstance(
        input_iterable, (str, bytes)
    )


def flatten_iterable(input_iterable: Iterable) -> Generator[Any, None, None]:
    """
    Flatten an iterable of iterables into a single iterable
    """
    stack = [iter(input_iterable)]

    while stack:
        try:
            # Get next element from top iterator on the stack
            current = next(stack[-1])
            if is_iterable_but_not_str(current):
                stack.append(
                    iter(current)
                )  # Push new iterator for the current iterable item
            else:
                # Item isn't iterator, yield it.
                yield current
        except StopIteration:
            # The iterator was exhausted
            stack.pop()


@lru_cache(maxsize=500)
def get_param_count(func):
    return len(inspect.signature(func).parameters)


def safe_name(name):
    """
    Some names are reserved in Python, so we need to add an underscore
    An underscore after was chosen so type hints match what user is looking for
    """
    # Keywords
    if name in ("class", "is", "for", "as", "async", "del"):
        name = name + "_"

    if "-" in name:
        # Fixes for 'accept-charset' etc.
        name = name.replace("-", "_")

    return name


def get_livereload_env() -> Optional[str]:
    enabled = getenv("HTMLCOMPOSE_LIVERELOAD") == "1"
    if not enabled:
        return None
    flags = getenv("HTMLCOMPOSE_LIVERELOAD_FLAGS")
    return flags


def generate_livereload_env(host, port):
    return {
        "HTMLCOMPOSE_LIVERELOAD_FLAGS": f"port={port}&host={host}",
        "HTMLCOMPOSE_LIVERELOAD": "1",
    }


def glob_matcher(pattern, path):
    """
    Implementation of glob matcher which supports:
      recursive globbing i.e. **
      dir name matching via trailing /

    Notes:
      In Python 3.13 PurePath implemented full_match, but we don't
      have that in 3.10.
    """
    pure_path = PurePath(path)
    pure_pattern = PurePath(pattern)
    path_parts = pure_path.parts
    glob_parts = pure_pattern.parts
    is_double_star = "**" in pattern

    def _segment_match(pattern_segment, path_segment):
        """Match a single path segment against a pattern segment."""
        # fnmatch doesn't handle asterisk matching quite the same,
        # so we use PurePath.match for * and? patterns.
        return PurePath(path_segment).match(pattern_segment)

    def _section_match(
        pattern_segment: tuple, path_section: tuple, terminates=False
    ):
        """

        Match a single path segment against a pattern segment.
        Uses PurePath's match for * and ? patterns.

        :param pattern_segment: Description
        :type pattern_segment:
        :param path_section: Description
        :type path_section:
        :return: Description
        :rtype: bool"""
        if len(pattern_segment) > len(path_section):
            return False

        if terminates and (len(pattern_segment) != len(path_section)):
            return False

        # We match segment by segment because PurePath will do weird generalizations
        # such as matching "*.txt" against dir/file.txt
        for i, seg in enumerate(pattern_segment):
            if not _segment_match(seg, path_section[i]):
                return False

        return True

    # Simple: We can just match the path_parts against the glob_parts
    if not is_double_star:
        if pattern.endswith("/"):
            last_section = path_parts[0 : len(glob_parts)]
            return _section_match(glob_parts, last_section, terminates=False)

        return _section_match(glob_parts, path_parts, terminates=True)

    # Oops, there's a double star.
    # Build lists split on **
    glob_sections = []
    glob_section = []

    for part in glob_parts:
        if part == "**":
            glob_sections.append(glob_section)
            glob_section = []
        else:
            glob_section.append(part)

    if glob_section:
        glob_sections.append(glob_section)

    j = 0
    for i, current in enumerate(glob_sections):
        is_last_glob = i == len(glob_sections) - 1
        term = is_last_glob and not pattern.endswith("/")
        matched = False
        while j < len(path_parts):
            if _section_match(current, path_parts[j:], terminates=term):
                matched = True
                break
            if i > 0:
                j += 1
            else:
                break
        if not matched:
            return False
    return True
