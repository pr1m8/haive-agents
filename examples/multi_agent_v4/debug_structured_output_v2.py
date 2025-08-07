"""Debug Structured Output with v2 - See what's happening

This shows exactly what happens when we use structured_output_version="v2"

Date: August 7, 2025
"""

import asyncio
from typing import List

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field

from haive.agents.simple.agent_v3 import SimpleAgentV3


# Define structured output
class SimpleAnalysis(BaseModel):
    """Simple analysis output."""

    finding: str = Field(description="Main finding")
    score: float = Field(ge=0.0, le=1.0, description="Confidence score")


async def main():
    """Debug structured output v2."""

    print("Creating agent with structured_output_version='v2' and debug=True...")
    print("=" * 60)

    # Create agent with v2 and debug enabled
    analyzer = SimpleAgentV3(
        name="analyzer",
        engine=AugLLMConfig(
            temperature=0.3,
            max_tokens=200,
            system_message="You are an analyst. Provide a brief analysis.",
            structured_output_model=SimpleAnalysis,
            structured_output_version="v2",  # Tool-based approach
        ),
        debug=True,  # ENABLE DEBUG to see what's happening!
    )

    # Simple query
    query = "Analyze the weather today"
    print(f"\nQuery: {query}")
    print("=" * 60)

    # Execute with debug output
    print("\n🔍 EXECUTING AGENT WITH DEBUG OUTPUT...")
    print("=" * 60)

    try:
        result = await analyzer.arun({"messages": [HumanMessage(content=query)]})

        print("\n" + "=" * 60)
        print("✅ EXECUTION COMPLETE")
        print("=" * 60)

        print(f"\nResult type: {type(result).__name__}")
        print(f"Result: {result}")

        # Check for structured output
        if hasattr(result, "analyzer"):
            print(f"\n✅ Found 'analyzer' field!")
            print(f"   Type: {type(result.analyzer).__name__}")
            print(f"   Content: {result.analyzer}")
        else:
            print("\n❌ No 'analyzer' field found")

    except Exception as e:
        print(f"\n❌ ERROR: {type(e).__name__}: {e}")
        import traceback

        traceback.print_exc()

    print("\n" + "=" * 60)
    print("🔍 WHAT WE LEARNED")
    print("=" * 60)
    print("With debug=True, we can see:")
    print("1. How the structured output model is converted to a tool")
    print("2. What the agent is trying to do")
    print("3. Why we get 'Unknown Pydantic model' errors")


if __name__ == "__main__":
    print("Debug Structured Output v2")
    print("=" * 50 + "\n")
    asyncio.run(main())
