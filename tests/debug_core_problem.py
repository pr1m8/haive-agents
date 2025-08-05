"""Debug script to trace the core problem with detailed breakpoints."""

import sys
import traceback


# Add paths
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")

from langchain_core.messages import HumanMessage

from haive.agents.multi.proper_base import ProperMultiAgent
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


# Monkey patch AgentNodeV3 to add debugging
def debug_agent_node_call(original_call):
    def wrapper(self, state):
        if hasattr(state, "agents"):
            if hasattr(state.agents, "__len__"):
                pass
            if isinstance(state.agents, dict) or hasattr(state.agents, "__iter__"):
                pass
            else:
                pass

        # Check all state attributes

        # Show state dict if available
        if hasattr(state, "__dict__") and "agents" in state.__dict__:
            if isinstance(state.__dict__["agents"], dict):
                pass

        # Call original
        try:
            result = original_call(state)
            return result
        except Exception:
            traceback.print_exc()
            raise

    return wrapper


# Apply monkey patch
from haive.core.graph.node.agent_node_v3 import AgentNodeV3Config


original_call = AgentNodeV3Config.__call__
AgentNodeV3Config.__call__ = debug_agent_node_call(original_call)


# Also patch the set_active_agent method to see what's happening
def debug_set_active_agent(original_method):
    def wrapper(self, agent_name):
        if hasattr(self, "agents"):
            if isinstance(self.agents, dict):
                pass
            else:
                pass

        # Call original
        return original_method(agent_name)

    return wrapper


import contextlib

from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState


original_set_active = MultiAgentState.set_active_agent
MultiAgentState.set_active_agent = debug_set_active_agent(original_set_active)


# Also patch the schema input preparation
def debug_prepare_schema_input(original_method):
    def wrapper(self, input_data, input_schema):
        if hasattr(self, "agents") and isinstance(self.agents, dict):
            pass

        # Call original
        result = original_method(input_data, input_schema)

        if hasattr(result, "agents") and isinstance(result.agents, dict):
            pass

        return result

    return wrapper


# Apply to ProperMultiAgent
ProperMultiAgent._prepare_schema_input = debug_prepare_schema_input(
    ProperMultiAgent._prepare_schema_input
)


async def trace_execution():
    """Trace the complete execution with detailed debugging."""
    # Step 1: Create agents
    agent1 = SimpleAgent(
        name="agent1",
        engine=AugLLMConfig(system_message="You are agent 1"),
    )
    agent2 = SimpleAgent(
        name="agent2",
        engine=AugLLMConfig(system_message="You are agent 2"),
    )

    # Step 2: Create multi-agent
    multi = ProperMultiAgent(
        name="debug_multi", agents=[agent1, agent2], execution_mode="sequential"
    )

    # Step 3: Check state schema

    # Step 4: Create test state manually
    multi.state_schema(
        messages=[HumanMessage(content="Test")],
        agents=multi.agents,  # Explicitly set
    )

    # Step 5: Test input preparation
    test_input = {"messages": [HumanMessage(content="Test")]}

    # Call the input preparation method directly
    try:
        multi._prepare_schema_input(test_input, multi.state_schema)
    except Exception:
        # Try without the second parameter
        with contextlib.suppress(Exception):
            multi._prepare_schema_input(test_input)

    # Step 6: Check graph structure

    # Step 7: Try to execute

    try:
        result = await multi.ainvoke(test_input)

    except Exception as e:
        traceback.print_exc()

        # Try to get more info about the failure

        if "not found in agents" in str(e):
            pass

        return None

    return result


if __name__ == "__main__":
    import asyncio

    result = asyncio.run(trace_execution())

    if result:
        pass
    else:
        pass
