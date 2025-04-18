from haive_agents.rag.base.state import BaseRAGState
from pydantic import Field
from typing import Optional, List, Dict, Any
from langchain.schema import Document

class DynamicRAGState(BaseRAGState):
    """State for Dynamic RAG."""
    selected_sources: List[str] = Field(default_factory=list, description="Selected data sources")
    source_documents: Dict[str, List[Document]] = Field(default_factory=dict, description="Documents by source")
    source_metrics: Dict[str, Dict[str, Any]] = Field(default_factory=dict, description="Metrics by source")
    routing_explanation: Optional[str] = Field(default=None, description="Explanation for routing decision")

