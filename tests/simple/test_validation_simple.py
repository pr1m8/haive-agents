#!/usr/bin/env python3
"""Simple test for ValidationNodeConfigV2 with LangGraph."""

import asyncio
import logging

from pydantic import BaseModel, Field

from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.core.engine.aug_llm import AugLLMConfig


# Set up basic logging
logging.basicConfig(level=logging.WARNING)  # Reduce noise
logger = logging.getLogger(__name__)

class Analysis(BaseModel):
    """Simple analysis model."""
    topic: str = Field(description="The main topic")
    summary: str = Field(description="Brief summary")

async def test_validation():
    """Test if new ValidationNodeConfigV2 works."""
    try:
        agent = SimpleAgentV3(
            name="test",
            engine=AugLLMConfig(
                structured_output_model=Analysis,
                temperature=0.3
            ),
            debug=False  # Reduce output
        )

        print("✅ Agent created successfully")

        # Quick test
        result = await agent.arun("Analyze renewable energy")

        print(f"🎯 Result type: {type(result)}")

        if hasattr(result, "analysis") and hasattr(result.analysis, "topic"):
            print("✅ SUCCESS: Structured output working!")
            print(f"   Topic: {result.analysis.topic}")
            print(f"   Summary: {result.analysis.summary}")
            return True
        print("❌ No structured output in expected field")
        # Check if it's in the messages
        if "messages" in result:
            for msg in result["messages"]:
                if hasattr(msg, "tool_calls"):
                    print(f"   Found tool calls: {len(msg.tool_calls)}")
                if hasattr(msg, "name") and msg.name == "Analysis":
                    print(f"   Found ToolMessage: {msg.content}")
        print(f"   Result keys: {list(result.keys()) if hasattr(result, 'keys') else type(result)}")
        return False

    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

if __name__ == "__main__":
    success = asyncio.run(test_validation())
    print(f"\n{'✅ SUCCESS' if success else '❌ FAILED'}")
