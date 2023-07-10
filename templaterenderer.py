from datetime import datetime
from typing import Any

from jinja2 import Environment, PackageLoader, select_autoescape


def render_template(module: str, template_path: str, context: dict[str, Any]) -> str:
    """
    Renders a Jinja2 template with the provided student data and returns the rendered output as a string.

    Args:
        module (str): The name of the Python module to search for templates in.
        template_path (str): The path to the Jinja2 template to render, relative to the module.
        context (dict): A dictionary containing the data to be rendered on the template.

    Returns:
        str: The rendered output of the template as a string.
    """
    try:
        env = Environment(loader=PackageLoader(module), autoescape=select_autoescape())
        template = env.get_template(template_path)
    except Exception as E:
        return f"Template not found.\n{E}"

    hour = datetime.now().hour
    return template.render(hour=hour, **context)
