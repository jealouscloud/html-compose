from pathlib import Path


def get_path(fn):
    if Path("tools").exists():
        return Path("tools") / fn
    else:
        return Path(fn)
