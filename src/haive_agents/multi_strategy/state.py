from haive_agents.rag.self_corr.state import SelfCorrectiveRAGState
from pydantic import Field
from typing import Optional, List, Dict, Any

class MultiStrategyRAGState(SelfCorrectiveRAGState):
    """State for multi-strategy RAG agents."""
    query_type: Optional[str] = Field(default=None, description="Classified query type")
    strategy_name: Optional[str] = Field(default=None, description="Selected retrieval strategy")
    query_variations: List[str] = Field(default_factory=list, description="Generated query variations")
    rewritten_query: Optional[str] = Field(default=None, description="Rewritten query")
    strategy_metrics: Dict[str, Any] = Field(default_factory=dict, description="Metrics for the selected strategy")