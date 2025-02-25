"""
Jupyter notebook helpers
"""


def render(html_string: str):
    """
    Renders the given HTML string as an IPython HTML object.
    This is used by Jupyter notebooks to display HTML content.
    """
    from IPython.core.display import HTML

    return HTML(html_string)
