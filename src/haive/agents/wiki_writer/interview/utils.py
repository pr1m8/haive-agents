from typing import Any


def add_messages(left, right) -> Any:
    """Add Messages.

    Args:
        left: [TODO: Add description]
        right: [TODO: Add description]

    Returns:
        [TODO: Add return description]
    """
    if not isinstance(left, list):
        left = [left]
    if not isinstance(right, list):
        right = [right]
    return left + right


def update_references(references, new_references) -> Any:
    """Update References.

    Args:
        references: [TODO: Add description]
        new_references: [TODO: Add description]

    Returns:
        [TODO: Add return description]
    """
    if not references:
        references = {}
    references.update(new_references)
    return references


def update_editor(editor, new_editor) -> Any:
    """Update Editor.

    Args:
        editor: [TODO: Add description]
        new_editor: [TODO: Add description]

    Returns:
        [TODO: Add return description]
    """
    # Can only set at the outset
    if not editor:
        return new_editor
    return editor
