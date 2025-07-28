"""Debug the self-discover agent to see state projection issues."""

import asyncio
import sys

# Add direct paths to avoid import issues
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")

# Add debug to agent node v3
import logging

from langchain_core.messages import HumanMessage

from haive.agents.reasoning_and_critique.self_discover.v2.agent import (
    DEFAULT_REASONING_MODULES,
    self_discovery,
)

logging.basicConfig(level=logging.DEBUG)

# Patch the agent node v3 to add debug prints
from haive.core.graph.node.agent_node_v3 import AgentNodeV3

original_project_state = AgentNodeV3._project_state_for_agent


def debug_project_state(self, state, agent):
    """Debug version of _project_state_for_agent."""
    # Check what's in the state
    if hasattr(state, "agent_outputs"):
        pass
    if agent_name == "select_modules":
        required = ["reasoning_modules", "task_description"]
    elif agent_name == "adapt_modules":
        required = ["selected_modules", "task_description"]
    elif agent_name == "create_structure":
        required = ["adapted_modules", "task_description"]
    elif agent_name == "final_reasoning":
        required = ["reasoning_structure", "task_description"]
    else:
        required = []

    missing = [key for key in required if key not in projected]
    if missing:
        pass
    else:
        pass

    return projected


# Monkey patch for debugging
AgentNodeV3._project_state_for_agent = debug_project_state


async def test_self_discover_debug():
    """Test self-discover agent with debug."""
    # Simple test problem
    test_problem = "How do I solve 25 * 36?"

    test_input = {
        "messages": [HumanMessage(content=test_problem)],
        "reasoning_modules": DEFAULT_REASONING_MODULES[:5],
        "task_description": test_problem,  # Add task_description
    }

    try:
        result = await self_discovery.ainvoke(test_input, config={"debug": True})

        if isinstance(result, dict) and "agent_outputs" in result:
            for _agent_name, _output in result["agent_outputs"].items():
                pass

        return result

    except Exception:
        import traceback

        traceback.print_exc()
        return None


if __name__ == "__main__":
    result = asyncio.run(test_self_discover_debug())
