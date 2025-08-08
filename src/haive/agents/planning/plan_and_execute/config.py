from haive.core.engine.agent.config import AgentConfig
from haive.core.engine.aug_llm import AugLLMConfig
from pydantic import BaseModel, Field

from haive.agents.planning.plan_and_execute.state import PlanAndExecuteState
from haive.agents.react.config import ReactAgentConfig


class PlanAndExecuteConfig(AgentConfig):
    aug_llm_configs: dict[str, AugLLMConfig] = Field(
        default_factory=lambda: {
            "planner": AugLLMConfig(),
            "replanner": AugLLMConfig(),
        }
    )
    agent_executor_config: ReactAgentConfig = Field(default_factory=ReactAgentConfig)
    state_schema: type[BaseModel] | list[BaseModel] = PlanAndExecuteState
    default_input_schema: dict[str, list] = {"input": [("user", "{}")]}
