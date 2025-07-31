import re


def replace_empty_placeholders(template: str) -> str:
    """Replace `{}` (empty placeholders) with `None`."""
    return re.sub(r"\{\s*\}", "None", template)
