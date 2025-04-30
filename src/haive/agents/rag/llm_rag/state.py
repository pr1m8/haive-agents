from pydantic import BaseModel, Field
from typing import List, Optional, Union, Any
from langchain.schema import Document
from haive.agents.rag.base.state import BaseRAGState, BaseRAGInputState, BaseRAGOutputState

class LLMRAGInputState(BaseRAGInputState):
    """Input state for LLM RAG agents."""
    pass

class LLMRAGOutputState(BaseRAGOutputState):
    """Output state for LLM RAG agents."""
    answer: str = Field(default="", description="The generated answer based on retrieved documents")
    is_relevant: bool = Field(default=False, description="Whether the retrieved documents are relevant to the query")

class LLMRAGState(BaseRAGState, LLMRAGOutputState):
    """State for LLM RAG agents."""
    pass