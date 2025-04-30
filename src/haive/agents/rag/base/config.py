from typing import Optional, Dict, Any, Union, Type
import uuid

from pydantic import BaseModel, Field, ConfigDict, model_validator
from typing_extensions import Annotated

from haive.core.engine.agent.agent import AgentConfig
from haive.core.engine.vectorstore import VectorStoreConfig
from haive.core.engine.retriever import VectorStoreRetrieverConfig, BaseRetrieverConfig

# Import state models
from haive.agents.rag.base.state import (
    BaseRAGState, 
    BaseRAGInputState, 
    BaseRAGOutputState
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
    retriever_config: Union[BaseRetrieverConfig, VectorStoreConfig] = Field(
        ...,  # Required
        description="Configuration for the retriever component"
    )
    
    # Use class attributes instead of ClassVar for schema references
    state_schema:Type[BaseModel] = BaseRAGState
    input_schema:Type[BaseModel] = BaseRAGInputState
    output_schema:Type[BaseModel] = BaseRAGOutputState
    
    @model_validator(mode='before')
    @classmethod
    def convert_vector_store_to_retriever(cls, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Pre-validation converter from VectorStoreConfig to RetrieverConfig.
        This runs before Pydantic validation, ensuring the type checking works.
        """
        if isinstance(data, dict) and "retriever_config" in data:
            if isinstance(data["retriever_config"], VectorStoreConfig):
                vs_config = data["retriever_config"]
                data["retriever_config"] = VectorStoreRetrieverConfig(
                    name=f"retriever_for_{data.get('name', 'rag_agent')}",
                    vector_store_config=vs_config
                )
        return data
        
    @model_validator(mode='after')
    def setup_engine(self) -> 'BaseRAGConfig':
        """
        After validation, set the engine property to the retriever_config.
        This ensures the agent can use the retriever directly.
        """
        self.engine = self.retriever_config
        return self