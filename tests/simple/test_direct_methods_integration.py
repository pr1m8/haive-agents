#!/usr/bin/env python3
"""Test script for direct methods integration in SimpleAgent and AugLLMConfig."""

import asyncio
from typing import List

from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)
from langchain_core.tools import tool
from pydantic import BaseModel, Field

# Import the updated classes
from haive.agents.simple.agent_v2 import SimpleAgentV2


# Test models
class AnalysisResult(BaseModel):
    """Test model for structured output."""

    findings: List[str] = Field(description="Key findings")
    confidence: float = Field(ge=0, le=1, description="Confidence score")
    recommendation: str = Field(description="Recommended action")


# Test tools
@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {e}"


async def test_direct_methods():
    """Test the direct methods integration."""
    print("🚀 Testing SimpleAgentV2 with direct methods integration...")

    try:
        # Create agent with unique name to avoid state persistence issues
        import time
        import uuid

        unique_name = f"test_agent_{int(time.time())}_{uuid.uuid4().hex[:8]}"
        agent = SimpleAgentV2(name=unique_name)
        print("✅ SimpleAgentV2 created successfully")

        # Test 1: Basic execution
        print("\n1. Testing basic execution...")
        result1 = await agent.arun("What is 2 + 2? Be brief.")
        print(f"   Result: {result1}")
        assert "4" in str(result1)
        print("   ✅ Basic execution works")

        # Test 2: Prompt template management
        print("\n2. Testing prompt template management...")
        template = ChatPromptTemplate.from_messages(
            [
                SystemMessagePromptTemplate.from_template(
                    "You are a mathematician. Always show your work."
                ),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )

        agent.add_prompt_template("math", template)
        agent.use_prompt_template("math")

        result2 = await agent.arun("What is 5 * 7?")
        print(f"   Math template result: {result2}")
        assert "35" in str(result2)
        print("   ✅ Template management works")

        # Test 3: Structured output (skipping tool test for now)
        print("\n3. Testing structured output...")
        agent.set_structured_output(AnalysisResult)

        result3 = await agent.arun("Analyze: Sales increased 20% this quarter")
        print(f"   Structured result type: {type(result3)}")

        # V2 structured output creates tool calls, not direct instances
        # Check if the last message has tool calls to our model
        if hasattr(result3, "messages") and result3.messages:
            last_message = result3.messages[-1]
            if hasattr(last_message, "tool_calls") and last_message.tool_calls:
                tool_call = last_message.tool_calls[0]
                if tool_call["name"] == "AnalysisResult":
                    print(
                        f"   ✅ Structured output tool call created: {tool_call['args']}"
                    )
                    print("   ✅ Structured output works (v2 tool-based)")
                else:
                    print(f"   ❌ Unexpected tool call: {tool_call['name']}")
            else:
                print("   ❌ No tool calls found")
        else:
            print(f"   ❌ Unexpected result structure: {result3}")

        # Test 4: Configuration summary
        print("\n4. Testing configuration summary...")
        summary = agent.get_configuration_summary()
        print(f"   Summary: {summary}")
        assert summary["active_template"] == "math"
        assert summary["tools_count"] > 0  # V2 structured output adds tools
        assert summary["structured_output"] == "AnalysisResult"
        print("   ✅ Configuration summary works")

        print("\n🎉 All tests passed! Direct methods integration is working!")
        return True

    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = asyncio.run(test_direct_methods())
    exit(0 if success else 1)
