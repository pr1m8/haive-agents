#!/usr/bin/env python3
"""Simple test to verify tool binding works."""

import asyncio

from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

from haive.agents.planning_v2.base.models import Plan, Task
from haive.core.engine.aug_llm import AugLLMConfig


async def test_direct_tool_binding():
    """Test direct LLM tool binding."""
    print("\n" + "="*80)
    print("DIRECT TOOL BINDING TEST")
    print("="*80)

    # Create a simple tool for the Plan model
    @tool
    def create_plan(objective: str, steps: list = None) -> dict:
        """Create a structured plan with the given objective and steps."""
        return {
            "objective": objective,
            "status": "pending",
            "steps": steps or [],
            "result": None
        }

    # Direct LLM with tool
    llm = ChatOpenAI(model="gpt-4o", temperature=0.3)
    llm_with_tools = llm.bind_tools([create_plan], tool_choice="required")

    print("1. Testing direct LLM with tool...")
    messages = [HumanMessage(content="Create a plan to build a REST API")]

    response = await llm_with_tools.ainvoke(messages)

    print(f"2. Response type: {type(response)}")
    print(f"   Content: {response.content}")
    print(f"   Tool calls: {len(response.tool_calls)}")

    if response.tool_calls:
        print("3. Tool call details:")
        for tc in response.tool_calls:
            print(f"   - Name: {tc['name']}")
            print(f"   - Args: {tc['args']}")

        return True
    print("3. ❌ NO TOOL CALLS - This would be the problem")
    return False


async def test_aug_llm_config_tool_binding():
    """Test AugLLMConfig tool binding."""
    print("\n" + "="*80)
    print("AUG LLM CONFIG TOOL BINDING TEST")
    print("="*80)

    # Create AugLLMConfig with structured output
    config = AugLLMConfig(
        temperature=0.3,
        structured_output_model=Plan[Task],
        force_tool_use=True
    )

    print("1. AugLLMConfig configuration:")
    print(f"   - Force tool use: {getattr(config, 'force_tool_use', 'NOT SET')}")
    print(f"   - Force tool choice: {getattr(config, 'force_tool_choice', 'NOT SET')}")
    print(f"   - Tool choice mode: {getattr(config, 'tool_choice_mode', 'NOT SET')}")
    print(f"   - Tools: {len(getattr(config, 'tools', []))}")

    # Get the runnable
    print("\n2. Getting runnable...")
    runnable = config.get_runnable()
    print(f"   Runnable type: {type(runnable)}")

    # Check if it has bind_tools or tools in kwargs
    if hasattr(runnable, "kwargs"):
        print(f"   Runnable kwargs keys: {list(runnable.kwargs.keys())}")
        if "tools" in runnable.kwargs:
            print(f"   Tools in runnable: {len(runnable.kwargs['tools'])}")
            print(f"   Tool names: {[getattr(t, 'name', str(t)) for t in runnable.kwargs['tools']]}")
        if "tool_choice" in runnable.kwargs:
            print(f"   Tool choice: {runnable.kwargs['tool_choice']}")

    print("\n3. Testing AugLLMConfig execution...")
    try:
        result = await config.ainvoke({"objective": "Build a REST API"})
        print(f"   Result type: {type(result)}")
        if hasattr(result, "tool_calls"):
            print(f"   Tool calls: {len(result.tool_calls) if result.tool_calls else 0}")
        else:
            print("   No tool_calls attribute")
        return result
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return None


async def main():
    """Run all tests."""
    print("Testing tool binding issues...")

    # Test 1: Direct tool binding (should work)
    direct_success = await test_direct_tool_binding()

    # Test 2: AugLLMConfig tool binding (may not work)
    aug_result = await test_aug_llm_config_tool_binding()

    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Direct tool binding works: {'✅ YES' if direct_success else '❌ NO'}")
    print(f"AugLLMConfig binding works: {'✅ YES' if aug_result and hasattr(aug_result, 'tool_calls') and aug_result.tool_calls else '❌ NO'}")

    if direct_success and not (aug_result and hasattr(aug_result, "tool_calls") and aug_result.tool_calls):
        print("\n🎯 DIAGNOSIS: Direct tool binding works, but AugLLMConfig doesn't bind tools properly.")
        print("The issue is in how AugLLMConfig converts structured_output_model to tool bindings.")
    elif not direct_success:
        print("\n🎯 DIAGNOSIS: Even direct tool binding doesn't work - LLM issue?")
    else:
        print("\n🎯 DIAGNOSIS: Both work - issue may be elsewhere in the chain.")


if __name__ == "__main__":
    asyncio.run(main())
