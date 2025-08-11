#!/usr/bin/env python3
"""Debug the result structure from the planning test."""

import asyncio
from haive.agents.simple import SimpleAgent
from haive.agents.planning_v2.base.models import Status, Plan, Task
from haive.agents.planning_v2.base.planner.prompts import planner_prompt
from haive.core.engine.aug_llm import AugLLMConfig


async def debug_planning_result():
    """Debug what the planning agent actually returns."""
    print("🔍 DEBUGGING PLANNING RESULT STRUCTURE")
    print("=" * 60)
    
    # Create engine with structured output AND prompt template
    engine = AugLLMConfig(
        temperature=0.3,
        structured_output_model=Plan[Task],
        prompt_template=planner_prompt
    )
    
    # Create planner using SimpleAgent directly
    planner = SimpleAgent(
        name="debug_planner",
        engine=engine
    )
    
    # Run planner
    result = await planner.arun({
        "objective": "Build a simple REST API for a todo list"
    })
    
    print(f"1. Result type: {type(result)}")
    print(f"2. Result class name: {result.__class__.__name__}")
    print(f"3. Is Plan instance: {isinstance(result, Plan)}")
    
    if hasattr(result, 'objective'):
        print(f"4. Has 'objective' attribute: ✅")
        print(f"   Objective value: '{result.objective}'")
    else:
        print(f"4. Has 'objective' attribute: ❌")
    
    if hasattr(result, 'steps'):
        print(f"5. Has 'steps' attribute: ✅")
        print(f"   Steps type: {type(result.steps)}")
        print(f"   Steps length: {len(result.steps)}")
        
        if len(result.steps) > 0:
            print(f"   First step type: {type(result.steps[0])}")
            print(f"   First step: {result.steps[0]}")
        else:
            print(f"   Steps is empty!")
    else:
        print(f"5. Has 'steps' attribute: ❌")
    
    if hasattr(result, 'status'):
        print(f"6. Has 'status' attribute: ✅")
        print(f"   Status value: {result.status}")
        print(f"   Status type: {type(result.status)}")
        print(f"   Is Status.PENDING: {result.status == Status.PENDING}")
    else:
        print(f"6. Has 'status' attribute: ❌")
    
    # Check all attributes
    print(f"7. All attributes: {dir(result)}")
    
    # Try model_dump if available
    if hasattr(result, 'model_dump'):
        print(f"8. Model dump:")
        try:
            dump = result.model_dump()
            print(f"   {dump}")
        except Exception as e:
            print(f"   Error: {e}")
    
    return result


async def main():
    """Main debug function."""
    result = await debug_planning_result()
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    is_plan = isinstance(result, Plan)
    has_objective = hasattr(result, 'objective') and result.objective
    has_steps = hasattr(result, 'steps') and len(result.steps) > 0
    has_status = hasattr(result, 'status') and result.status == Status.PENDING
    
    print(f"Is Plan instance: {'✅' if is_plan else '❌'}")
    print(f"Has objective: {'✅' if has_objective else '❌'}")
    print(f"Has steps: {'✅' if has_steps else '❌'}")
    print(f"Has correct status: {'✅' if has_status else '❌'}")
    
    if is_plan and has_objective and has_steps and has_status:
        print("🎉 RESULT IS CORRECT - Test should pass!")
    else:
        print("❌ RESULT HAS ISSUES - Need to investigate")


if __name__ == "__main__":
    asyncio.run(main())