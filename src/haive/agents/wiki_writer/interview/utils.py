"""Utils utility module.

This module provides utils functionality for the Haive framework.

Functions:
    add_messages: Add Messages functionality.
    update_references: Update References functionality.
    update_editor: Update Editor functionality.
"""

from typing import Any


def add_messages(left, right) -> Any:
    if not isinstance(left, list):
        left = [left]
    if not isinstance(right, list):
        right = [right]
    return left + right


def update_references(references, new_references) -> Any:
    if not references:
        references = {}
    references.update(new_references)
    return references


def update_editor(editor, new_editor) -> Any:
    # Can only set at the outset
    if not editor:
        return new_editor
    return editor
