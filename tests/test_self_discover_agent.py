"""Test the rewritten self-discover agent."""

import asyncio
import os
import sys

# Add direct paths to avoid import issues
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")

from langchain_core.messages import HumanMessage

from haive.agents.reasoning_and_critique.self_discover.v2.agent import (
    DEFAULT_REASONING_MODULES,
    self_discovery,
)


async def test_self_discover_agent():
    """Test the rewritten self-discover agent."""

    # Check agent setup

    # Test with a reasoning problem
    test_problem = """
    I need to solve a complex scheduling problem for a company with 100 employees across 5 departments.
    Each department has different shift requirements, and some employees have constraints on when they can work.
    The goal is to minimize overtime costs while ensuring all shifts are covered.
    """


    test_input = {
        "messages": [HumanMessage(content=test_problem)],
        "reasoning_modules": DEFAULT_REASONING_MODULES[:10],  # Use first 10 modules
    }

    try:
        # Execute the self-discovery process
        result = await self_discovery.ainvoke(test_input)


        # Check for expected outputs
        if isinstance(result, dict):
            if "messages" in result:

                # Show progression through the agents
                for i, message in enumerate(result["messages"]):
                    if hasattr(message, "content"):
                        content_preview = (
                            message.content[:100] + "..."
                            if len(message.content) > 100
                            else message.content
                        )

            if "agent_outputs" in result:

                # Show final reasoning result
                if "final_reasoning" in result["agent_outputs"]:
                    final_output = result["agent_outputs"]["final_reasoning"]
                    if isinstance(final_output, dict) and "answer" in final_output:
                        pass

        return True

    except Exception as e:
        import traceback

        traceback.print_exc()
        return False


async def test_agent_structure():
    """Test the agent structure and configuration."""

    # Check that all agents have proper names and configurations
    for agent_name, agent in self_discovery.agents.items():

        if (
            hasattr(agent.engine, "structured_output_model")
            and agent.engine.structured_output_model
        ):
            pass

    # Check engine integration

    # Check state schema


async def main():
    """Run all tests."""

    # Test agent structure
    await test_agent_structure()

    # Test agent execution
    success = await test_self_discover_agent()

    if success:
    else:


if __name__ == "__main__":
    asyncio.run(main())
