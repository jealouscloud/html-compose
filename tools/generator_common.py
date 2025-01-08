from pathlib import Path


def get_path(fn):
    if Path("tools").exists():
        return Path("tools") / fn
    else:
        return Path(fn)


def safe_name(name):
    """
    Some names are reserved in Python, so we need to add an underscore
    An underscore after was chosen so type hints match what user is looking for
    """
    # Keywords
    if name in ("class", "is", "for", "as", "async" "del"):
        name = name + "_"

    if "-" in name:
        # Fixes for 'accept-charset' etc.
        name = name.replace("-", "_")

    return name
