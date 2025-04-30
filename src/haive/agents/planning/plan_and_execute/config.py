from pydantic import BaseModel
from haive.agents.planning.plan_and_execute.state import PlanAndExecuteState
from haive.core.engine.base import Engine

from typing import Dict,List,Type,Union
from haive.core.engine.agent.config import AgentConfig
from haive.core.engine.agent.react import ReactAgentConfig


class PlanAndExecuteConfig(AgentConfig):
    engines:Dict[str,Engine] ={"planner":planner_aug_llm_config,
                                             #"agent_executor":agent_executor_aug_llm_config,
                                             "replanner":rPlanAndExecuteStatenfig}
    agent_executor_config:ReactAgentConfig = ReactAgentConfig(
        #llm_config=agent_executor_aug_llm_config,
        #tools=[],
        #state_schema=PlanAndExecuteState
    )
    #models:List[BaseModel] = [Plan,Act,Response,Step,Status]
    state_schema:Union[Type[BaseModel],List[BaseModel]] = PlanAndExecuteState
    default_input_schema:Dict[str,List] = {"input": [("user", "{}")]}
