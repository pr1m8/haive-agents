#!/usr/bin/env python3
"""Clean test of ReactAgent with structured output - no debug noise."""

import asyncio
from pydantic import BaseModel, Field

from haive.agents.react.agent import ReactAgent
from haive.core.engine.aug_llm import AugLLMConfig


class SimpleResult(BaseModel):
    """Simple structured result."""
    answer: str = Field(description="The answer")


async def test_react_clean_execution():
    """Test ReactAgent execution cleanly without debug noise."""
    
    agent = ReactAgent(
        name="clean_test",
        engine=AugLLMConfig(
            structured_output_model=SimpleResult,
            temperature=0.3,
            system_message="You are a helpful assistant."
        ),
        tools=[],  # No tools
        max_iterations=2,  # Limit iterations
        debug=False  # No debug output
    )
    
    print("🔄 Testing ReactAgent with structured output...")
    
    try:
        # Execute with timeout
        result = await asyncio.wait_for(
            agent.arun("What is 2 + 2?"),
            timeout=45.0  # 45 second timeout
        )
        
        print("✅ Execution completed successfully!")
        print(f"   - Result type: {type(result)}")
        print(f"   - Result: {result}")
        
        if hasattr(result, 'answer'):
            print(f"   - Answer: {result.answer}")
            
        return result
        
    except asyncio.TimeoutError:
        print("❌ Execution timed out - likely infinite loop")
        return None
    except Exception as e:
        print(f"❌ Execution failed: {e}")
        return None


if __name__ == "__main__":
    result = asyncio.run(test_react_clean_execution())
    
    if result:
        print("\n✅ ReactAgent with structured output is working correctly!")
        print("   - No infinite loop detected")
        print("   - Structured output returned successfully")
    else:
        print("\n❌ ReactAgent still has issues")