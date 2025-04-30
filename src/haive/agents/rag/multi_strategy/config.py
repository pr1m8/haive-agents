from haive.agents.rag.multi_strategy.state import MultiStrategyRAGState
from haive.core.engine.aug_llm import AugLLMConfig
from pydantic import Field
from typing import Optional, Dict, Any
from haive.agents.rag.self_corr.config import SelfCorrectiveRAGConfig
class MultiStrategyRAGConfig(SelfCorrectiveRAGConfig):
    """Configuration for multi-strategy RAG agents."""
    state_schema: type[MultiStrategyRAGState] = Field(default=MultiStrategyRAGState, description="State schema")
    query_analyzer_config: Optional[AugLLMConfig] = Field(default=None, description="Configuration for query analysis")
    query_rewriter_config: Optional[AugLLMConfig] = Field(default=None, description="Configuration for query rewriting")
    retriever_strategies: Dict[str, Any] = Field(default_factory=dict, description="Specialized retriever configurations")
