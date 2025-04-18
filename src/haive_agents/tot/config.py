from haive_core.engine.agent.agent import AgentConfig
from haive_core.engine.aug_llm import AugLLMConfig
from haive_core.models.llm.base import AzureLLMConfig
from haive_agents.tot.state import ToTState
from typing import Dict
from pydantic import Field

class TOTAgentConfig(AgentConfig):
    """Configuration for the ToT agent"""
    engines: Dict[str,AugLLMConfig] = Field(default={
        'solution_generator':AugLLMConfig(name="solution_generator",llm_config=AzureLLMConfig(model="gpt-4o",parameters={"temperature": 0.7}))
    },description="The configuration for the LLM")
    #tree_config: TreeConfig = Field(default=TreeConfig())
    state_schema: ToTState = Field(default=ToTState)
    max_depth: int = Field(description="Maximum depth of the ToT tree",default=3)
    threshold: float = Field(description="Threshold for the ToT agent",default=0.5)
    k: int = Field(description="Number of candidates to consider",default=5)