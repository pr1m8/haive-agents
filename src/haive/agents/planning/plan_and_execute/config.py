from haive.core.engine.agent.config import AgentConfig
from haive.core.engine.aug_llm import AugLLMConfig
from pydantic import BaseModel, Field

from haive.agents.planning.plan_and_execute.state import PlanAndExecuteState


class PlanAndExecuteConfig(AgentConfig):
    aug_llm_configs: dict[str, AugLLMConfig] = Field(
        default_factory=lambda: {
            "planner": AugLLMConfig(),
            "replanner": AugLLMConfig(),
        }
    )
    agent_executor_config: AugLLMConfig = Field(default_factory=AugLLMConfig)
    state_schema: type[BaseModel] | list[BaseModel] = PlanAndExecuteState
    default_input_schema: dict[str, list] = {"input": [("user", "{}")]}
