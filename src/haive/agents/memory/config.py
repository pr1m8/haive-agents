"""Memory Agent Configuration."""

from typing import Any
from pydantic import Field
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.engine.agent.agent import AgentConfig


class MemoryAgentConfig(AgentConfig):
    """Configuration for the Memory Agent."""
    
    name: str = Field(default="memory_agent", description="Agent name")
    engine: AugLLMConfig = Field(default_factory=AugLLMConfig, description="LLM configuration")
    description: str = Field(
        default="An agent with memory capabilities",
        description="Agent description"
    )
    vector_store: Any = Field(default=None, description="Vector store for memory persistence")
    max_memories_per_retrieval: int = Field(default=10, description="Maximum memories to retrieve")
    memory_type: str = Field(default="general", description="Type of memory")
    runnable_config: Any = Field(default=None, description="Runnable configuration")
    state_schema: Any = Field(default=None, description="State schema")