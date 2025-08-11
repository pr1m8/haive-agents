#!/usr/bin/env python3
"""Debug the validation error in detail."""

import asyncio
import traceback
from haive.agents.simple import SimpleAgent
from haive.agents.planning_v2.base.models import Plan, Task
from haive.agents.planning_v2.base.planner.prompts import planner_prompt
from haive.core.engine.aug_llm import AugLLMConfig


async def debug_validation_error():
    """Debug the exact validation error."""
    print("🔍 DEBUGGING VALIDATION ERROR IN DETAIL")
    print("=" * 60)
    
    # Create the exact same config as the test
    config = AugLLMConfig(
        structured_output_model=Plan[Task],
        prompt_template=planner_prompt,
        temperature=0.3
    )
    
    agent = SimpleAgent(name='debug_agent', engine=config)
    
    print("1. Agent created successfully")
    print(f"   Graph type: {type(agent.graph)}")
    print(f"   Validation node type: {type(agent.graph.nodes.get('validation'))}")
    
    # Try to run and catch any detailed errors
    try:
        print("\n2. Starting agent execution...")
        result = await agent.arun({
            "objective": "Build a simple REST API for a todo list"
        })
        
        print(f"3. Execution completed")
        print(f"   Result type: {type(result)}")
        print(f"   Has 'steps' attribute: {hasattr(result, 'steps')}")
        
        if hasattr(result, 'steps'):
            print(f"   Steps count: {len(result.steps)}")
            if result.steps:
                print(f"   First step: {result.steps[0]}")
            else:
                print("   Steps is empty!")
        
        return result
        
    except Exception as e:
        print(f"❌ EXCEPTION DURING EXECUTION:")
        print(f"   Exception type: {type(e)}")
        print(f"   Exception message: {str(e)}")
        print(f"   Full traceback:")
        traceback.print_exc()
        
        return None


async def main():
    """Main debug function."""
    result = await debug_validation_error()
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    if result:
        print("✅ Agent executed without exceptions")
        print(f"Result type: {type(result)}")
        if hasattr(result, 'steps'):
            print(f"Has steps: {len(result.steps)} steps")
        else:
            print("❌ Result has no 'steps' attribute")
    else:
        print("❌ Agent execution failed with exception")


if __name__ == "__main__":
    asyncio.run(main())