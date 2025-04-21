from typing import Any

from langchain_core.documents import Document
from pydantic import Field

from haive.agents.react.react.state import ReactAgentState


class ReactRAGState(ReactAgentState):
    """State for React Agent with RAG capabilities.
    
    Adds fields for document retrieval and answer generation.
    """
    # Document retrieval fields
    query: str | None = None
    retrieved_documents: list[Document] = Field(default_factory=list)

    # RAG-specific fields
    context: str | None = None
    answer: str | None = None

    # RAG metadata
    retrieval_metadata: dict[str, Any] = Field(default_factory=dict)
