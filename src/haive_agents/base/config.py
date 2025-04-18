from typing import Optional, Dict, Any, Union, Type, ClassVar
import uuid

from pydantic import BaseModel, Field, ConfigDict
from typing_extensions import Annotated

from haive_core.engine.agent.agent import AgentConfig
from haive_core.models.vectorstore.base import VectorStoreConfig
from haive_core.models.retriever.base import RetrieverConfig
from haive_core.graph.graph_pattern_registry import register_graph_component

# Import state models
from haive_agents.rag.base.state import (
    BaseRAGState, 
    BaseRAGInputState, 
    BaseRAGOutputState
)

@register_graph_component(
    "agent_config", 
    "BaseRAGConfig", 
    tags=["rag", "retrieval", "agent"],
    metadata={
        "description": "Base configuration for Retrieval-Augmented Generation agents"
    }
)
class BaseRAGConfig(AgentConfig):
    """Configuration for a basic RAG agent."""
    # Configuration for Pydantic
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True
    )
    
    name: str = Field(default_factory=lambda: f"rag_agent_{uuid.uuid4().hex[:8]}")
    description: str = Field(default="Basic Retrieval-Augmented Generation agent")
    
    # Allow either a VectorStoreConfig or RetrieverConfig to be provided
    retriever_config: Union[RetrieverConfig, VectorStoreConfig] = Field(
        ...,  # Required
        description="Configuration for the retriever component"
    )
    
    # Use ClassVar for type references to avoid Pydantic field detection
    state_schema: ClassVar[Type[BaseModel]] = BaseRAGState
    input_schema: ClassVar[Type[BaseModel]] = BaseRAGInputState
    output_schema: ClassVar[Type[BaseModel]] = BaseRAGOutputState
    
    def __init__(self, **data):
        """
        Initialize the RAG config, converting configurations as needed.
        """
        # If retriever_config is a VectorStoreConfig, convert it to a default RetrieverConfig
        if "retriever_config" in data and isinstance(data["retriever_config"], VectorStoreConfig):
            from haive_core.models.retriever.base import RetrieverConfig
            
            vs_config = data["retriever_config"]
            data["retriever_config"] = RetrieverConfig(
                name=f"retriever_for_{data.get('name', 'rag_agent')}",
                vector_store_config=vs_config
            )
        
        super().__init__(**data)