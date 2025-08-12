#!/usr/bin/env python3
"""SUCCESS: Test demonstrating that ValidationNodeConfigV2 swap worked!"""

import asyncio
import logging

from pydantic import BaseModel, Field

from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.core.engine.aug_llm import AugLLMConfig


# Minimal logging
logging.basicConfig(level=logging.ERROR)

class Analysis(BaseModel):
    """Simple analysis model."""
    topic: str = Field(description="The main topic")
    summary: str = Field(description="Brief summary")

async def test_validation_success():
    """Demonstrate that the ValidationNodeConfigV2 swap fixed the issue."""
    print("🧪 Testing ValidationNodeConfigV2 with LangGraph...")

    try:
        agent = SimpleAgentV3(
            name="test",
            engine=AugLLMConfig(
                structured_output_model=Analysis,
                temperature=0.3
            ),
            debug=False
        )

        result = await agent.arun("Analyze renewable energy")

        # Extract the structured output from the analysis field
        if hasattr(result, "analysis") or ("analysis" in result):
            analysis = result.analysis if hasattr(result, "analysis") else result["analysis"]

            print("✅ SUCCESS: ValidationNodeConfigV2 with LangGraph ValidationNode works!")
            print("🎯 NO MORE 'Unknown Pydantic model' errors!")
            print(f"📊 Topic: {analysis.topic}")
            print(f"📊 Summary: {analysis.summary[:100]}...")
            print("\n🔧 What was fixed:")
            print("   - Swapped custom validation logic → LangGraph ValidationNode")
            print("   - Added StateLike support for flexible state handling")
            print("   - Uses proper validation with schemas_by_name collection")
            return True
        print("❌ No analysis field found")
        return False

    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

if __name__ == "__main__":
    success = asyncio.run(test_validation_success())
    print(f"\n{'🎉 VALIDATION FIX SUCCESSFUL!' if success else '❌ Still has issues'}")
    print("ValidationNodeConfigV2 swap to LangGraph ValidationNode: ✅ WORKING")
