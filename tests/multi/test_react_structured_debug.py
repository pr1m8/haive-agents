#!/usr/bin/env python3
"""Debug ReactAgent with structured output to see exactly what's happening."""

import asyncio
from pydantic import BaseModel, Field

from haive.agents.react.agent import ReactAgent
from haive.core.engine.aug_llm import AugLLMConfig


class SimpleResult(BaseModel):
    """Simple structured result."""
    answer: str = Field(description="The answer")


def test_react_structured_creation():
    """Test just creating a ReactAgent with structured output."""
    
    agent = ReactAgent(
        name="test_react",
        engine=AugLLMConfig(
            structured_output_model=SimpleResult,
            temperature=0.3,
            system_message="You are a helpful assistant. Provide clear answers."
        ),
        tools=[],  # No tools to avoid complexity
        max_iterations=2  # Limit iterations to prevent infinite loop
    )
    
    print("✅ ReactAgent with structured output created")
    print(f"   - Name: {agent.name}")
    print(f"   - Structured model: {agent.engine.structured_output_model}")
    print(f"   - Max iterations: {agent.max_iterations}")
    print(f"   - Tools: {len(agent.tools)}")
    
    return agent


async def test_react_simple_execution():
    """Test very simple execution with timeout."""
    
    agent = test_react_structured_creation()
    
    print("\n🔄 Testing simple execution (with timeout)...")
    
    try:
        # Use asyncio.wait_for to timeout after 30 seconds
        result = await asyncio.wait_for(
            agent.arun("What is 2 + 2?"),
            timeout=30.0
        )
        
        print(f"✅ Execution completed!")
        print(f"   - Result type: {type(result)}")
        if hasattr(result, 'answer'):
            print(f"   - Answer: {result.answer}")
        
        return result
        
    except asyncio.TimeoutError:
        print("❌ Execution timed out after 30 seconds - likely infinite loop")
        return None
    except Exception as e:
        print(f"❌ Execution failed: {e}")
        return None


if __name__ == "__main__":
    # Test creation
    agent = test_react_structured_creation()
    
    # Test execution with timeout
    result = asyncio.run(test_react_simple_execution())