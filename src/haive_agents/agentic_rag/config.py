from typing import Dict, List, Any, Optional, Union, Type
from pydantic import BaseModel, Field, model_validator
from langchain_core.tools import BaseTool
from langchain_core.documents import Document

from haive_agents.react.react.config import ReactAgentConfig
from haive_agents.react.react.state import ReactAgentState
from haive_agents.rag.llm_rag.config import LLMRAGConfig
from haive_agents.react.agentic_rag.state import ReactRAGState

class ReactRAGConfig(ReactAgentConfig):
    """
    Configuration for React Agent with RAG capabilities.
    
    Combines React Agent's tool usage with RAG agent's document retrieval.
    """
    # Override state schema
    state_schema: Type[BaseModel] = Field(default=ReactRAGState)
    
    # RAG configuration
    rag_config: Optional[LLMRAGConfig] = Field(
        default=None,
        description="RAG agent configuration"
    )
    
    # Document retrieval configuration
    retriever_config: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Document retriever configuration"
    )
    
    # Nodes for RAG workflow
    retrieval_node_name: str = Field(default="retrieve")
    answer_generation_node_name: str = Field(default="generate_answer")
    
    @model_validator(mode="after")
    def ensure_valid_configuration(self):
        """Validate the configuration."""
        # Call parent validator
        super().ensure_valid_configuration()
        
        # Ensure RAG configuration or retriever configuration is provided
        if not self.rag_config and not self.retriever_config:
            raise ValueError("Either rag_config or retriever_config must be provided")
        
        return self