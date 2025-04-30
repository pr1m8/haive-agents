from typing import List, Dict, Any, Optional
from langchain_core.documents import Document
from pydantic import BaseModel, Field
from agents.react.react.state import ReactAgentState

class ReactRAGState(ReactAgentState):
    """
    State for React Agent with RAG capabilities.
    
    Adds fields for document retrieval and answer generation.
    """
    # Document retrieval fields
    query: Optional[str] = None
    retrieved_documents: List[Document] = Field(default_factory=list)
    
    # RAG-specific fields
    context: Optional[str] = None
    answer: Optional[str] = None
    
    # RAG metadata
    retrieval_metadata: Dict[str, Any] = Field(default_factory=dict)
