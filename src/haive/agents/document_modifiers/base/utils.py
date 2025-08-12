"""Utility functions for document processing."""

from typing import Any

from langchain_core.documents import Document


def normalize_contents(contents: Any) -> list[str]:
    """Normalize inputs to strings.

    Accepts:
    - List[str]
    - List[Document]
    - Mixed list of strings and documents
    - Single string or Document

    Args:
        contents: The content to normalize

    Returns:
        List of strings extracted from the input

    Raises:
        TypeError: If unsupported content type is encountered
    """
    # Handle single items
    if isinstance(contents, str):
        return [contents]
    if isinstance(contents, Document):
        return [contents.page_content]

    # Handle lists
    if not isinstance(contents, list):
        raise TypeError(f"Expected string, Document, or list, got {type(contents)}")

    normalized = []
    for item in contents:
        if isinstance(item, Document):
            # Convert Document to string content
            normalized.append(item.page_content)
        elif isinstance(item, str):
            normalized.append(item)
        else:
            raise TypeError(
                f"Unsupported item type in contents: {type(item)}. Expected str or Document."
            )

    return normalized


def documents_to_strings(documents: list[Document]) -> list[str]:
    """Convert a list of Documents to a list of strings."""
    return [doc.page_content for doc in documents]


def strings_to_documents(strings: list[str]) -> list[Document]:
    """Convert a list of strings to a list of Documents."""
    return [Document(page_content=content) for content in strings]
