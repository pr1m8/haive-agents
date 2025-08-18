# from haive.core.utils.doc_utils import

from typing import Any


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


def format_doc(doc, max_length=1000) -> Any:
    """Format Doc.

    Args:
        doc: [TODO: Add description]
        max_length: [TODO: Add description]

    Returns:
        [TODO: Add return description]
    """
    related = "- ".join(doc.metadata["categories"])
    return f"### {doc.metadata['title']}\n\nSummary: {doc.page_content}\n\nRelated\n{related}"[
        :max_length
    ]
