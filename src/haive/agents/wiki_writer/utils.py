"""Utils utility module.

This module provides utils functionality for the Haive framework.

Functions:
    update_references: Update References functionality.
    update_editor: Update Editor functionality.
    format_doc: Format Doc functionality.
"""

# from haive.core.utils.doc_utils import


from typing import Any


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


def format_doc(doc, max_length=1000) -> Any:
    related = "- ".join(doc.metadata["categories"])
    return f"### {doc.metadata['title']}\n\nSummary: {doc.page_content}\n\nRelated\n{related}"[
        :max_length
    ]
