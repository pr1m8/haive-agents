"""Final test of ReactAgent → SimpleAgent sequential flow."""

import asyncio
import sys


sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")

from langchain_core.messages import HumanMessage
from langchain_core.tools import tool

from haive.agents.multi.proper_base import ProperMultiAgent
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


@tool
def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""
    try:
        result = eval(expression)
        return f"The result of {expression} is {result}"
    except Exception as e:
        return f"Error calculating {expression}: {e!s}"


async def test_react_simple_flow():
    """Test ReactAgent → SimpleAgent sequential flow."""
    # Create ReactAgent with calculator tool
    react_agent = ReactAgent(
        name="analyzer",
        engine=AugLLMConfig(
            system_message="You are an analytical agent. Use the calculator tool to solve math problems and provide detailed reasoning.",
            temperature=0.1,
        ),
        tools=[calculator],
    )

    # Create SimpleAgent for summary
    simple_agent = SimpleAgent(
        name="summarizer",
        engine=AugLLMConfig(
            system_message="You are a summary agent. Take the previous analysis and create a clean, structured summary.",
            temperature=0.1,
        ),
    )

    # Create ProperMultiAgent
    multi_agent = ProperMultiAgent(
        name="math_workflow",
        agents=[react_agent, simple_agent],
        execution_mode="sequential",
    )

    # Test input
    test_problem = "What is 25 * 37? Please calculate this and explain your reasoning."
    test_input = {"messages": [HumanMessage(content=test_problem)]}

    try:
        # Execute the multi-agent workflow
        result = await multi_agent.ainvoke(test_input)

        # If result is a coroutine, await it
        if hasattr(result, "__await__"):
            result = await result

        # Try to extract messages
        if hasattr(result, "messages"):
            for _i, msg in enumerate(result.messages):
                if hasattr(msg, "content"):
                    pass

        # Check if it's a dict with messages
        elif isinstance(result, dict) and "messages" in result:
            for _i, msg in enumerate(result["messages"]):
                if hasattr(msg, "content"):
                    pass

        return True

    except Exception:
        return False


if __name__ == "__main__":
    success = asyncio.run(test_react_simple_flow())

    if success:
        pass
    else:
        pass
