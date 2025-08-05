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
    
    # Node names for memory operations
    memory_load_node_name: str = Field(default="memory_load", description="Name of memory loading node")
    memory_extract_node_name: str = Field(default="memory_extract", description="Name of memory extraction node")
    memory_save_node_name: str = Field(default="memory_save", description="Name of memory saving node")
    tool_node_name: str = Field(default="tools", description="Name of tool node")
    llm_node_name: str = Field(default="agent", description="Name of LLM node")
    
    # System prompts
    system_prompt: str = Field(default="You are a helpful assistant with memory capabilities.", description="System prompt")
    memory_system_prompt: str = Field(default="Use your memory to provide better responses.", description="Memory-specific system prompt")
    
    # Output schema and node
    structured_output_schema: Any = Field(default=None, description="Structured output schema")
    output_node_name: str = Field(default="output", description="Name of output node")
    
    # Memory extraction
    memory_extraction_engine: Any = Field(default=None, description="Engine for memory extraction")
    memory_extraction_prompt: str = Field(default="Extract key information from this conversation.", description="Prompt for memory extraction")