# Initial summary

from pydantic import Field

from haive.agents.document_agents.kg.kg_iterative_refinement.state import (
    IterativeGraphTransformerState,
)
from haive.core.engine.agent.agent import AgentConfig
from haive.core.engine.aug_llm.base import AugLLMConfig


class IterativeGraphTransformerConfig(AgentConfig):
    """The configuration for the iterative graph transformer.
    """
    state_schema: IterativeGraphTransformerState = Field(default=IterativeGraphTransformerState,description="The state of the iterative graph transformer.")
    engines: dict[str,AugLLMConfig] = Field(default={
    },description="The configuration for the Augmented LLMs.")
