"""Final test of ReactAgent → SimpleAgent sequential flow."""

import asyncio
import sys

sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool

from haive.agents.multi.proper_base import ProperMultiAgent
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent


@tool
def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""
    try:
        result = eval(expression)
        return f"The result of {expression} is {result}"
    except Exception as e:
        return f"Error calculating {expression}: {str(e)}"


async def test_react_simple_flow():
    """Test ReactAgent → SimpleAgent sequential flow."""

    print("🚀 Testing ReactAgent → SimpleAgent Sequential Flow")
    print("=" * 60)

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

    print(f"✅ Created multi-agent with: {list(multi_agent.agents.keys())}")

    # Test input
    test_problem = "What is 25 * 37? Please calculate this and explain your reasoning."
    test_input = {"messages": [HumanMessage(content=test_problem)]}

    print(f"\n📝 Problem: {test_problem}")
    print(f"🔄 Starting execution...")

    try:
        # Execute the multi-agent workflow
        result = await multi_agent.ainvoke(test_input)

        print(f"\n✅ Execution completed successfully!")
        print(f"📊 Result type: {type(result)}")

        # If result is a coroutine, await it
        if hasattr(result, "__await__"):
            result = await result
            print(f"📊 Awaited result type: {type(result)}")

        # Try to extract messages
        if hasattr(result, "messages"):
            print(f"\n📨 Messages ({len(result.messages)}):")
            for i, msg in enumerate(result.messages):
                if hasattr(msg, "content"):
                    print(f"\n{i+1}. {type(msg).__name__}:")
                    print(
                        f"   {msg.content[:200]}..."
                        if len(msg.content) > 200
                        else f"   {msg.content}"
                    )

        # Check if it's a dict with messages
        elif isinstance(result, dict) and "messages" in result:
            print(f"\n📨 Messages ({len(result['messages'])}):")
            for i, msg in enumerate(result["messages"]):
                if hasattr(msg, "content"):
                    print(f"\n{i+1}. {type(msg).__name__}:")
                    print(
                        f"   {msg.content[:200]}..."
                        if len(msg.content) > 200
                        else f"   {msg.content}"
                    )

        return True

    except Exception as e:
        print(f"\n❌ Execution failed: {e}")
        return False


if __name__ == "__main__":
    success = asyncio.run(test_react_simple_flow())

    if success:
        print(f"\n🎉 ReactAgent → SimpleAgent flow working successfully!")
    else:
        print(f"\n💔 Flow failed - see error above")

    print("\n" + "=" * 60)
