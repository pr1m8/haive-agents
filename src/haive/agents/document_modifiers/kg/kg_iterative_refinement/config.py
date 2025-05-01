# Initial summary
from haive.core.engine.agent.agent import AgentConfig
from haive.core.engine.aug_llm import AugLLMConfig
from haive.agents.document_modifiers.kg.kg_iterative_refinement.state import IterativeGraphTransformerState
from typing import Dict
from pydantic import Field  
class IterativeGraphTransformerConfig(AgentConfig):
    """
    The configuration for the iterative graph transformer.
    """
    state_schema: IterativeGraphTransformerState = Field(default=IterativeGraphTransformerState,description="The state of the iterative graph transformer.")
    engines: Dict[str,AugLLMConfig] = Field(default={
    },description="The configuration for the Augmented LLMs.")
    