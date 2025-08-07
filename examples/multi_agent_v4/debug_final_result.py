#!/usr/bin/env python3
"""Just check if SimpleAgentV3 with v2 actually works or errors.

Date: August 7, 2025
"""

import asyncio
import os

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field

from haive.agents.simple.agent_v3 import SimpleAgentV3

# Disable postgres
os.environ["HAIVE_DISABLE_POSTGRES"] = "1"


class SimpleModel(BaseModel):
    text: str = Field(description="Simple text response")
    value: int = Field(description="A number")


async def test_final():
    agent = SimpleAgentV3(
        name="final_test",
        engine=AugLLMConfig(
            structured_output_model=SimpleModel,
            structured_output_version="v2",
            temperature=0.3,
            max_tokens=50,
        ),
    )

    try:
        result = await agent.arun({"messages": [HumanMessage(content="Say hello")]})
        print(f"✅ SUCCESS! Got result: {type(result).__name__}")

        # Try to get structured output
        if hasattr(result, "get_latest_structured_output"):
            structured = result.get_latest_structured_output()
            if structured:
                print(f"✅ Structured output: {structured}")
            else:
                print("❓ No structured output found")

        return True

    except Exception as e:
        print(f"❌ ERROR: {e}")
        if "Unknown Pydantic model" in str(e):
            print("🎯 CONFIRMED: ValidationNodeConfigV2 cannot find the model")
        return False


if __name__ == "__main__":
    success = asyncio.run(test_final())
    print(f"\nResult: {'WORKING' if success else 'BROKEN'}")
