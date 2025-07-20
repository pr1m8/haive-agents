import operator
from typing import Annotated

from haive.core.common.mixins.getter_mixin import GetterMixin
from haive.core.engine.aug_llm import AugLLMConfig

# ============================================================================
# REACT AGENT
# ============================================================================
from langchain_core.tools import tool
from pydantic import (
    Any,
    BaseModel,
    Dict,
    Field,
    computed_field,
    from,
    import,
    typing,
)

from haive.agents.base.agent import Agent
from haive.agents.react.agent import ReactAgent

# from haive.agents.rag.base.agent import SimpleRAGAgent
from haive.agents.simple.agent import SimpleAgent


@tool
def add(a: int, b: int) -> int:
    """Returns the sum of two numbers."""
    return a + b


class Plan(BaseModel):
    steps: list[str] = Field(description="list of steps")


add_aug = AugLLMConfig(tools=[add])
plan_aug = AugLLMConfig(structured_output_model=Plan, structured_output_version="v2")
simple_agent = SimpleAgent(engine=plan_aug)
react_agent = ReactAgent(engine=add_aug)


class MultiAgentState(BaseModel, GetterMixin):
    agents: list[Agent] = Field(default_factory=[])
    selected_agents: Annotated[list[Agent], operator.add] = Field(default_factory=[])

    @computed_field
    def selected_agent(self) -> Agent:
        return selected_agents[-1] if selected_agents else None


def temp_node(state: Dict[str, Any]):
    state.get("selected_agent")
    agent = agent.create_runnable()
    agent.run(input_payload)


from langgraph.graph import StateGraph

base_graph = StateGraph(state_schema=MultiAgentState)
base_graph.add_node(temp_node)
base_graph.set_entry_point("temp_node")
base_graph.set_finish_point("temp_node")
base_graph.compile()
