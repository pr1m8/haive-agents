
from pydantic import Field

from haive.agents.tot.state import ToTState
from haive.core.engine.agent.agent import AgentConfig
from haive.core.engine.aug_llm.base import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig


class TOTAgentConfig(AgentConfig):
    """Configuration for the ToT agent"""
    engines: dict[str,AugLLMConfig] = Field(default={
        "solution_generator":AugLLMConfig(name="solution_generator",llm_config=AzureLLMConfig(model="gpt-4o",parameters={"temperature": 0.7}))
    },description="The configuration for the LLM")
    #tree_config: TreeConfig = Field(default=TreeConfig())
    state_schema: ToTState = Field(default=ToTState)
    max_depth: int = Field(description="Maximum depth of the ToT tree",default=3)
    threshold: float = Field(description="Threshold for the ToT agent",default=0.5)
    k: int = Field(description="Number of candidates to consider",default=5)
