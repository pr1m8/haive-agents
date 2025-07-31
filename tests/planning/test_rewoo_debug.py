"""Debug script for ReWOO V3 implementation."""

import asyncio

from langchain_core.tools import tool

from haive.agents.planning.rewoo_v3 import ReWOOV3Agent
from haive.core.engine.aug_llm import AugLLMConfig


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

    # Check if agents are callable
    for _name, sub_agent in agent.multi_agent.agents.items():
        if hasattr(sub_agent, "arun"):
            pass
        if hasattr(sub_agent, "invoke"):
            pass

    # Try simple execution
    try:
        await agent.arun("What is 2 + 2?")
    except Exception:
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(test_rewoo())
