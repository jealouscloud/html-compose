from html_compose.base_types import _HasHtml

"""
Jupyter notebook helpers
"""


def render(html_string: str | _HasHtml):
    """
    Renders the given HTML string as an IPython HTML object.
    This is used by Jupyter notebooks to display HTML content.
    """
    from IPython.core.display import HTML

    if isinstance(html_string, _HasHtml):
        html_string = html_string.__html__()
    return HTML(html_string)
