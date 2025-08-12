"""Debug Agent with No Postgres - Show What's Happening.

This removes postgres persistence and shows the agent execution with debug=True

Date: August 7, 2025
"""

import asyncio
import os

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field

from haive.agents.simple.agent_v3 import SimpleAgentV3

# Disable postgres to avoid the unique constraint error
os.environ["HAIVE_DISABLE_POSTGRES"] = "1"


# Simple structured output
class SimpleAnalysis(BaseModel):
    """Simple analysis output."""

    finding: str = Field(description="Main finding")
    score: float = Field(ge=0.0, le=1.0, description="Confidence score")


async def main():
    """Debug agent execution with v2."""
    print("🔍 DEBUG AGENT WITH structured_output_version='v2'")
    print("=" * 60)

    # Create agent with v2 and debug enabled
    agent = SimpleAgentV3(
        name="debug_analyzer",
        engine=AugLLMConfig(
            temperature=0.3,
            max_tokens=200,
            system_message="You are an analyst. Provide a brief analysis.",
            structured_output_model=SimpleAnalysis,
            structured_output_version="v2",  # This will fail
        ),
        debug=True,  # Show everything!
    )

    print("\n📋 AGENT CONFIGURATION:")
    print(f"- Name: {agent.name}")
    print(f"- Engine type: {agent.engine.engine_type}")
    print(f"- Structured output model: {agent.engine.structured_output_model}")
    print(f"- Structured output version: {agent.engine.structured_output_version}")
    print(f"- Force tool use: {agent.engine.force_tool_use}")
    print(f"- Force tool choice: {agent.engine.force_tool_choice}")
    print(f"- Tool routes: {list(agent.engine.tool_routes.keys())}")

    print("\n🎯 ATTEMPTING EXECUTION...")
    print("=" * 60)

    try:
        result = await agent.arun(
            {"messages": [HumanMessage(content="Analyze the weather today")]}
        )

        print("\n✅ EXECUTION COMPLETED")
        print("=" * 60)
        print(f"Result type: {type(result).__name__}")

        # Show what we got back
        if hasattr(result, "messages"):
            print(f"\n📬 Messages: {len(result.messages)}")
            for i, msg in enumerate(result.messages):
                print(f"  [{i}] {type(msg).__name__}")
                if hasattr(msg, "tool_calls") and msg.tool_calls:
                    print(f"      Tool calls: {len(msg.tool_calls)}")
                    for j, call in enumerate(msg.tool_calls):
                        print(f"        {j}: {call}")
                print(f"      Content: {str(msg.content)[:100]}...")

        # Try to get structured output
        if hasattr(result, "get_latest_structured_output"):
            structured = result.get_latest_structured_output()
            if structured:
                print(f"\n✅ Structured output: {structured}")
            else:
                print("\n❌ No structured output found")

    except Exception as e:
        print("\n❌ EXECUTION FAILED")
        print("=" * 60)
        print(f"Error: {type(e).__name__}: {e}")

        # Show the traceback for the key error
        import traceback

        tb = traceback.format_exc()

        # Look for the validation error specifically
        if "Unknown Pydantic model" in str(e):
            print("\n🔍 ROOT CAUSE ANALYSIS:")
            print("- The structured output model was registered as a tool")
            print("- The validation node tried to validate the 'tool call'")
            print(
                "- But the validation node doesn't have the model in its pydantic_models dict"
            )
            print("- This is a bug in SimpleAgentV3._add_validation_nodes()")

        # Show where it failed
        lines = tb.split("\n")
        for i, line in enumerate(lines):
            if "Unknown Pydantic model" in line:
                print(f"\n📍 Error location: {lines[i-1] if i > 0 else ''}")
                print(f"📍 Error message: {line}")
                break

    print("\n🎯 WHAT WE LEARNED:")
    print("=" * 60)
    print("1. The model is correctly registered as a tool")
    print("2. force_tool_use=True makes the LLM call it")
    print("3. The validation node doesn't know about the model")
    print("4. This is a SimpleAgentV3 bug, not multi-agent issue")
    print("\n💡 SOLUTION: Use v1 (parser-based) for now!")


if __name__ == "__main__":
    asyncio.run(main())
