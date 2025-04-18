from haive_agents.rag.base.state import BaseRAGState
from pydantic import Field
from typing import Optional, Dict, Any, List
from langchain.schema import Document

class TypedRAGState(BaseRAGState):
    """State for Typed-RAG."""
    query_category: Optional[str] = Field(default=None, description="Classified query category")
    query_metadata: Dict[str, Any] = Field(default_factory=dict, description="Metadata about the query")
    subqueries: Dict[str, str] = Field(default_factory=dict, description="Generated subqueries by type")
    subquery_results: Dict[str, List[Document]] = Field(default_factory=dict, description="Results for each subquery")
    aggregated_answer: Optional[str] = Field(default=None, description="Aggregated answer")