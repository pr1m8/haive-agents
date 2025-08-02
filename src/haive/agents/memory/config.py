"""Memory Agent Configuration."""

from pydantic import BaseModel, Field
from haive.core.engine.aug_llm import AugLLMConfig


class MemoryAgentConfig(BaseModel):
    """Configuration for the Memory Agent."""
    
    name: str = Field(default="memory_agent", description="Agent name")
    engine: AugLLMConfig = Field(default_factory=AugLLMConfig, description="LLM configuration")
    description: str = Field(
        default="An agent with memory capabilities",
        description="Agent description"
    )