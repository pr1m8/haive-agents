"""Configuration for Language Agent Tree Search (LATS) agent."""

from typing import Any

from pydantic import BaseModel, Field


class LATSAgentConfig(BaseModel):
    """Plain configuration model for LATS agent parameters.

    This is a simple Pydantic BaseModel holding LATS-specific knobs.
    The LATSAgent itself extends haive.agents.base.agent.Agent and
    owns the engine / graph lifecycle.
    """

    # Core LATS parameters
    max_tree_height: int = Field(
        default=5, description="Maximum height of the search tree"
    )
    n_candidates: int = Field(
        default=5, description="Number of candidate responses per expansion"
    )
    exploration_weight: float = Field(
        default=1.0, description="Exploration weight for UCB1 calculation"
    )

    # LLM settings
    model: str = Field(default="gpt-4o", description="OpenAI model name")
    temperature: float = Field(
        default=0.7, description="Temperature for candidate generation"
    )

    # Prompts
    system_prompt: str = Field(
        default="You are an AI assistant that provides accurate, helpful responses.",
        description="System prompt for generation",
    )
    reflection_prompt: str = Field(
        default="Reflect and grade the assistant response to the user question below.",
        description="Prompt prefix for reflection",
    )

    # Tools (langchain BaseTool / StructuredTool instances)
    tools: list[Any] = Field(
        default_factory=list, description="Tools available to the LATS agent"
    )
