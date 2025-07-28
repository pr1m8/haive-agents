"""Debug script for ReWOO V3 implementation."""

import asyncio

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.tools import tool

from haive.agents.planning.rewoo_v3 import ReWOOV3Agent


@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"


async def test_rewoo():
    """Test ReWOO V3 basic functionality."""

    # Create agent
    config = AugLLMConfig(temperature=0.1)
    agent = ReWOOV3Agent(name="test_rewoo", config=config, tools=[calculator])

    # Check structure
    print("=== ReWOO V3 Structure ===")
    print(f"Name: {agent.name}")
    print(f"Tools: {agent.tools}")
    print(
        f"Sub-agents: planner={agent.planner}, worker={agent.worker}, solver={agent.solver}"
    )
    print(f"Multi-agent: {agent.multi_agent}")
    print(f"Multi-agent agents: {agent.multi_agent.agents}")
    print()

    # Check if agents are callable
    print("=== Agent Callability Check ===")
    for name, sub_agent in agent.multi_agent.agents.items():
        print(f"{name}: callable={callable(sub_agent)}, has_call={callable(sub_agent)}")
        if hasattr(sub_agent, "arun"):
            print(f"  - has arun: {hasattr(sub_agent, 'arun')}")
        if hasattr(sub_agent, "invoke"):
            print(f"  - has invoke: {hasattr(sub_agent, 'invoke')}")
    print()

    # Try simple execution
    print("=== Testing Execution ===")
    try:
        result = await agent.arun("What is 2 + 2?")
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(test_rewoo())
