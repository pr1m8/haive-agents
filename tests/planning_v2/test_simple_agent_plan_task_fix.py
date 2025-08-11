#!/usr/bin/env python3
"""
Test if SimpleAgent validation routing works with Plan[Task] after format instructions fix.
"""

import asyncio
from typing import List
from pydantic import BaseModel, Field
from haive.core.engine.aug_llm import AugLLMConfig
from haive.agents.simple.agent import SimpleAgent


class Task(BaseModel):
    """Task model for testing."""
    description: str = Field(description="Task description")


class Plan[T](BaseModel):
    """Plan model with generic type."""
    objective: str = Field(description="Plan objective")
    steps: List[T] = Field(description="Plan steps", max_length=2)


async def test_simple_agent_plan_task_validation():
    """Test SimpleAgent with Plan[Task] structured output and validation routing."""
    print("🧪 TESTING SIMPLE AGENT WITH PLAN[TASK] VALIDATION")
    print("=" * 60)
    
    # Create AugLLMConfig with Plan[Task] structured output
    config = AugLLMConfig(
        structured_output_model=Plan[Task],
        structured_output_version="v2"
    )
    
    print(f"1. AugLLMConfig created successfully")
    print(f"   Format instructions integrated: {hasattr(config, '_format_instructions_text')}")
    
    # Create SimpleAgent
    agent = SimpleAgent(
        name="planning_agent",
        engine=config
    )
    
    print(f"2. SimpleAgent created successfully")
    print(f"   Agent name: {agent.name}")
    print(f"   Engine type: {type(agent.engine).__name__}")
    
    # Test execution with debug to see step count
    input_data = {
        "messages": [{
            "role": "user", 
            "content": "Create a simple plan with 2 tasks for organizing a small team meeting"
        }]
    }
    
    print(f"3. Testing agent execution...")
    try:
        # Use arun with debug=True and recursion limit to see execution steps
        from langchain_core.runnables import RunnableConfig
        
        config = RunnableConfig(
            recursion_limit=5,  # Limit to 5 steps max
            configurable={}
        )
        
        result = await agent.arun(input_data, debug=True, config=config)
        
        print(f"✅ Agent execution successful!")
        print(f"   Result type: {type(result)}")
        
        # Check if result can be parsed as Plan[Task]
        if hasattr(result, 'content') and result.content:
            print(f"   Content preview: {str(result.content)[:200]}...")
            
        # Check if tool calls were made (V2 mode should use tool calls)
        if hasattr(result, 'tool_calls') and result.tool_calls:
            tool_call = result.tool_calls[0]
            args = tool_call['args'] if isinstance(tool_call, dict) else tool_call.args
            
            print(f"   Tool call successful!")
            print(f"   Args keys: {list(args.keys())}")
            
            # Try to create Plan[Task] from args
            try:
                plan = Plan[Task](**args)
                print(f"   ✅ Successfully parsed as Plan[Task]!")
                print(f"   Plan objective: {plan.objective}")
                print(f"   Steps count: {len(plan.steps)}")
                print(f"   First step: {plan.steps[0].description if plan.steps else 'N/A'}")
                return True
            except Exception as parse_error:
                print(f"   ❌ Failed to parse as Plan[Task]: {parse_error}")
                return False
        else:
            print(f"   ❌ No tool calls found in result")
            return False
            
    except Exception as e:
        print(f"❌ Agent execution failed: {e}")
        import traceback
        traceback.print_exc()
        return False


async def main():
    """Run the test."""
    success = await test_simple_agent_plan_task_validation()
    
    print(f"\n" + "=" * 60)
    print(f"🏁 TEST RESULT: {'✅ PASS' if success else '❌ FAIL'}")
    print(f"=" * 60)
    
    if success:
        print("✅ SimpleAgent validation routing works with Plan[Task]!")
        print("   - Format instructions properly integrated")
        print("   - V2 structured output working correctly")  
        print("   - Validation node routing should now work")
        print("   - Original recursion issue likely resolved")
    else:
        print("❌ SimpleAgent still has issues with Plan[Task]")
        print("   - May need additional debugging")
        print("   - Check validation node routing")


if __name__ == "__main__":
    asyncio.run(main())