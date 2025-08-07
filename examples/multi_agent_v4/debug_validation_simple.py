#!/usr/bin/env python3
"""Simple validation debug - just get the error and analyze it.

Date: August 7, 2025
"""

import asyncio
import logging
import os

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field

from haive.agents.simple.agent_v3 import SimpleAgentV3

# Disable postgres
os.environ["HAIVE_DISABLE_POSTGRES"] = "1"


# Simple model
class TestModel(BaseModel):
    result: str = Field(description="Result")
    score: float = Field(ge=0.0, le=1.0)


async def debug_simple():
    """Simple debug to see the exact error."""

    print("🔍 SIMPLE VALIDATION DEBUG")
    print("=" * 50)

    agent = SimpleAgentV3(
        name="debug_agent",
        engine=AugLLMConfig(
            system_message="You are a test agent.",
            structured_output_model=TestModel,
            structured_output_version="v2",  # This will fail
            temperature=0.3,
            max_tokens=100,
        ),
    )

    print(f"Agent: {agent.name}")
    print(f"Engine: {agent.engine.name}")
    print(f"Model: {agent.engine.structured_output_model.__name__}")

    try:
        result = await agent.arun({"messages": [HumanMessage(content="Test")]})
        print("✅ SUCCESS - No error occurred!")

        if hasattr(result, "engines"):
            print(f"\n🔍 State engines: {list(result.engines.keys())}")
            for name, engine in result.engines.items():
                print(f"  - {name}: {engine.structured_output_model}")

    except Exception as e:
        print(f"\n❌ ERROR: {e}")

        # Look for validation-specific error
        if "Unknown Pydantic model" in str(e):
            print(f"\n🎯 VALIDATION ERROR CONFIRMED!")
            print(
                f"This means ValidationNodeConfigV2._find_model_class_from_engine() failed"
            )
            print(f"Even though the engine should be findable in state.engines")

        # Show the stack trace to see where it fails
        import traceback

        traceback.print_exc()

        return False

    return True


if __name__ == "__main__":
    success = asyncio.run(debug_simple())

    if not success:
        print(f"\n💡 ANALYSIS:")
        print(f"The ValidationNodeConfigV2 is supposed to:")
        print(f"1. Get engine_name from its config")
        print(f"2. Find engine in state.engines[engine_name]")
        print(f"3. Check engine.structured_output_model.__name__ == tool_name")
        print(f"4. Return the model class")
        print(
            f"\nBut this is failing - need to add debug logging to ValidationNodeConfigV2!"
        )
