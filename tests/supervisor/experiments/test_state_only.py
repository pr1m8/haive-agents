"""Test just the state serialization without running the agent."""

import asyncio
import contextlib

from langchain_core.messages import HumanMessage
import ormsgpack

from haive.agents.experiments.supervisor.agent_info import AgentInfo
from haive.agents.experiments.supervisor.component_2_tools import (
    SupervisorStateWithTools,
)
from haive.agents.react.agent import ReactAgent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig
from haive.tools.tools.search_tools import tavily_search_tool


async def test_state_serialization():
    """Test state serialization directly."""
    # Create ReactAgent
    search_engine = AugLLMConfig(
        name="search_engine",
        llm_config=AzureLLMConfig(model="gpt-4o"),
        tools=[tavily_search_tool],
        system_message="You are a search specialist.",
    )

    search_agent = ReactAgent(name="search_agent", engine=search_engine)

    # Create state with agent
    state = SupervisorStateWithTools()
    state.messages = [HumanMessage(content="Find information about France")]

    with contextlib.suppress(Exception):
        ormsgpack.packb(state.model_dump())

    state.agents = {
        "search_agent": AgentInfo(
            agent=search_agent,
            name="search_agent",
            description="Web search specialist",
            active=True,
        )
    }
    state.active_agents = {"search_agent"}

    try:
        state_dict = state.model_dump()
        if "agents" in state_dict:
            pass
    except Exception:
        pass

    try:
        state_dict = state.model_dump()
        ormsgpack.packb(state_dict)
    except Exception:
        pass

    with contextlib.suppress(Exception):
        ormsgpack.packb(state)

    with contextlib.suppress(Exception):
        state.agents["search_agent"].model_dump()


if __name__ == "__main__":
    asyncio.run(test_state_serialization())
