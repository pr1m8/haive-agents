#!/usr/bin/env python3
"""Fix the tool naming issue in structured output."""

import asyncio
from haive.agents.planning_v2.base.models import Plan, Task
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.utils.naming import sanitize_tool_name


async def test_fix_tool_naming():
    """Test fixing the tool naming issue."""
    print("="*80)
    print("TOOL NAMING FIX TEST")
    print("="*80)
    
    # Original issue: force_tool_choice='plan_task_generic' but tool is named 'Plan[Task]'
    
    # Step 1: Check the original issue
    print("1. Reproducing the original issue...")
    config = AugLLMConfig(
        structured_output_model=Plan[Task],
        force_tool_use=True
    )
    
    original_tool_name = config.tools[0].__name__
    expected_tool_name = sanitize_tool_name(original_tool_name)
    force_choice = getattr(config, 'force_tool_choice', 'NOT SET')
    
    print(f"   - Original tool name: '{original_tool_name}'")
    print(f"   - Expected tool name: '{expected_tool_name}'")
    print(f"   - Force tool choice: '{force_choice}'")
    print(f"   - Names match: {original_tool_name == expected_tool_name}")
    
    # Step 2: Check where the naming conversion should happen
    print("\n2. Checking naming conversion...")
    
    # The issue is likely in tool_routes - it should use the sanitized name
    print(f"   - Tool routes: {config.tool_routes}")
    print(f"   - Route key matches force_choice: {expected_tool_name in config.tool_routes}")
    
    # Step 3: Test the fix approach
    print("\n3. Testing manual fix...")
    
    # Manually fix the tool_routes to use sanitized names
    fixed_config = AugLLMConfig(
        structured_output_model=Plan[Task],
        force_tool_use=True
    )
    
    # Fix the tool routes by updating the key
    original_key = list(fixed_config.tool_routes.keys())[0]
    route_value = fixed_config.tool_routes[original_key]
    
    # Create new tool_routes with sanitized key
    fixed_config.tool_routes = {expected_tool_name: route_value}
    
    print(f"   - Fixed tool routes: {fixed_config.tool_routes}")
    print(f"   - Force choice matches route: {force_choice in fixed_config.tool_routes}")
    
    # Step 4: Test if the fix works
    print("\n4. Testing fixed configuration...")
    try:
        # This should now work without the tool name mismatch error
        runnable = fixed_config.create_runnable()
        print(f"   - Runnable created successfully: {type(runnable)}")
        
        # Try a simple invoke to see if we get further
        result = await fixed_config.ainvoke({"objective": "Test plan"})
        print(f"   - Result type: {type(result)}")
        
        if hasattr(result, 'tool_calls'):
            print(f"   - Tool calls count: {len(result.tool_calls) if result.tool_calls else 0}")
            if result.tool_calls:
                for tc in result.tool_calls:
                    print(f"     Tool call: {tc.get('name')} with {list(tc.get('args', {}).keys())}")
        
        return True
        
    except Exception as e:
        print(f"   - ❌ Still failing: {e}")
        return False


async def main():
    """Main test function."""
    success = await test_fix_tool_naming()
    
    print("\n" + "="*80)
    if success:
        print("✅ FIX SUCCESSFUL - Tool naming issue resolved!")
        print("The solution is to ensure tool_routes uses sanitized names.")
    else:
        print("❌ FIX FAILED - Need to investigate further.")


if __name__ == "__main__":
    asyncio.run(main())