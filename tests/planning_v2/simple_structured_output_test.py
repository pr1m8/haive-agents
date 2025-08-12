#!/usr/bin/env python3
"""Simple test to diagnose structured output vs tool binding issue."""

import asyncio

from haive.agents.planning_v2.base.models import Plan, Task
from haive.core.engine.aug_llm import AugLLMConfig


async def test_aug_llm_config_structured_output():
    """Test how AugLLMConfig handles structured output."""
    print("\n" + "="*80)
    print("AUG LLM CONFIG STRUCTURED OUTPUT ANALYSIS")
    print("="*80)

    # Create AugLLMConfig with structured output
    config = AugLLMConfig(
        temperature=0.3,
        structured_output_model=Plan[Task],
        force_tool_use=True
    )

    print("1. Configuration Analysis:")
    print(f"   - LLM Config Type: {type(config.llm_config)}")
    print(f"   - Structured Output Model: {config.structured_output_model}")
    print(f"   - Force Tool Use: {config.force_tool_use}")
    print(f"   - Force Tool Choice: {getattr(config, 'force_tool_choice', 'NOT SET')}")
    print(f"   - Tool Choice Mode: {getattr(config, 'tool_choice_mode', 'NOT SET')}")
    print(f"   - Tools Count: {len(config.tools)}")
    print(f"   - Tool Routes: {config.tool_routes}")

    if config.tools:
        print("   - Tools Details:")
        for i, tool in enumerate(config.tools):
            print(f"     Tool {i+1}: {type(tool)} - {getattr(tool, '__name__', 'unknown')}")

    # Get the runnable
    print("\n2. Runnable Analysis:")
    runnable = config.create_runnable()
    print(f"   - Runnable Type: {type(runnable)}")

    # Check if it's using with_structured_output or bind_tools
    if hasattr(runnable, "bound"):
        print("   - Has 'bound' attribute: True")
        print(f"   - Bound type: {type(runnable.bound)}")

        if hasattr(runnable, "kwargs"):
            kwargs_keys = list(runnable.kwargs.keys())
            print(f"   - Runnable kwargs: {kwargs_keys}")

            if "tools" in runnable.kwargs:
                tools_in_kwargs = runnable.kwargs["tools"]
                print(f"   - Tools in kwargs: {len(tools_in_kwargs)} tools")
                for i, tool in enumerate(tools_in_kwargs):
                    tool_name = getattr(tool, "name", str(type(tool)))
                    print(f"     Bound tool {i+1}: {tool_name}")

            if "tool_choice" in runnable.kwargs:
                print(f"   - Tool choice: {runnable.kwargs['tool_choice']}")
    else:
        print("   - Has 'bound' attribute: False")

    # Check the actual LLM binding method
    print(f"   - Runnable chain length: {len(runnable.steps) if hasattr(runnable, 'steps') else 'unknown'}")

    # Test invocation
    print("\n3. Test Invocation:")
    try:
        result = await config.ainvoke({"objective": "Create a simple test plan"})

        print(f"   - Result type: {type(result)}")
        print(f"   - Has tool_calls: {hasattr(result, 'tool_calls')}")

        if hasattr(result, "tool_calls"):
            tool_calls_count = len(result.tool_calls) if result.tool_calls else 0
            print(f"   - Tool calls count: {tool_calls_count}")

            if result.tool_calls:
                print("   - Tool call details:")
                for i, tc in enumerate(result.tool_calls):
                    print(f"     Call {i+1}: {tc.get('name', 'unknown')} with args {list(tc.get('args', {}).keys())}")
            else:
                print("   - ❌ NO TOOL CALLS - LLM returned text instead")

        # Check content
        if hasattr(result, "content"):
            content_preview = result.content[:200] + "..." if len(result.content) > 200 else result.content
            print(f"   - Content preview: {content_preview}")

        return result

    except Exception as e:
        print(f"   - ❌ Error during invocation: {e}")
        import traceback
        traceback.print_exc()
        return None


async def test_direct_structured_output():
    """Test direct .with_structured_output() approach."""
    print("\n" + "="*80)
    print("DIRECT STRUCTURED OUTPUT TEST")
    print("="*80)

    try:
        # Get the raw LLM from AugLLMConfig
        config = AugLLMConfig(temperature=0.3)
        llm = config.instantiate_llm()

        print(f"1. LLM Type: {type(llm)}")

        # Use direct structured output
        structured_llm = llm.with_structured_output(Plan[Task])
        print(f"2. Structured LLM Type: {type(structured_llm)}")

        # Test invocation
        from langchain_core.messages import HumanMessage
        result = await structured_llm.ainvoke([
            HumanMessage(content="Create a plan to build a simple REST API for a todo list")
        ])

        print(f"3. Result type: {type(result)}")
        print(f"   - Is Plan instance: {isinstance(result, Plan)}")

        if isinstance(result, Plan):
            print(f"   - Objective: {result.objective}")
            print(f"   - Steps count: {len(result.steps)}")
            print(f"   - Status: {result.status}")
            print("   - ✅ DIRECT STRUCTURED OUTPUT WORKS!")
            return result
        print(f"   - ❌ Expected Plan, got {type(result)}")
        return None

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return None


async def main():
    """Run analysis tests."""
    print("🔍 DIAGNOSING STRUCTURED OUTPUT ISSUE...")

    # Test 1: How AugLLMConfig handles structured output
    aug_result = await test_aug_llm_config_structured_output()

    # Test 2: Direct structured output approach
    direct_result = await test_direct_structured_output()

    print("\n" + "="*80)
    print("DIAGNOSIS")
    print("="*80)

    aug_has_tool_calls = (
        aug_result and
        hasattr(aug_result, "tool_calls") and
        aug_result.tool_calls and
        len(aug_result.tool_calls) > 0
    )

    direct_works = direct_result and isinstance(direct_result, Plan)

    print(f"AugLLMConfig produces tool calls: {'✅ YES' if aug_has_tool_calls else '❌ NO'}")
    print(f"Direct structured output works: {'✅ YES' if direct_works else '❌ NO'}")

    if direct_works and not aug_has_tool_calls:
        print("\n🎯 ROOT CAUSE IDENTIFIED:")
        print("   - Direct .with_structured_output() works perfectly")
        print("   - AugLLMConfig with force_tool_use=True doesn't produce tool calls")
        print("   - The issue is that AugLLMConfig is using 'parse_output' route")
        print("   - This means the LLM gets format instructions instead of tool bindings")
        print("   - Solution: AugLLMConfig should use .with_structured_output() directly")
        print("     instead of treating structured_output_model as a tool")
    elif not direct_works:
        print("\n❓ UNEXPECTED: Even direct structured output doesn't work")
    else:
        print("\n✅ Both approaches work - issue may be elsewhere")


if __name__ == "__main__":
    asyncio.run(main())
