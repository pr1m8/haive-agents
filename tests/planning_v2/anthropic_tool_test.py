#!/usr/bin/env python3
"""Simple test to verify tool binding works with Anthropic."""

import asyncio
from haive.agents.planning_v2.base.models import Plan, Task
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.engine.llm.anthropic_config import AnthropicLLMConfig
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool


async def test_direct_anthropic_tool_binding():
    """Test direct Anthropic LLM tool binding."""
    print("\n" + "="*80)
    print("DIRECT ANTHROPIC TOOL BINDING TEST")
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
    
    # Direct Anthropic LLM with tool
    llm = ChatAnthropic(model="claude-3-5-sonnet-20241022", temperature=0.3)
    llm_with_tools = llm.bind_tools([create_plan], tool_choice="any")
    
    print("1. Testing direct Anthropic LLM with tool...")
    messages = [HumanMessage(content="Create a plan to build a REST API")]
    
    try:
        response = await llm_with_tools.ainvoke(messages)
        
        print(f"2. Response type: {type(response)}")
        print(f"   Content: {response.content}")
        print(f"   Tool calls: {len(response.tool_calls) if response.tool_calls else 0}")
        
        if response.tool_calls:
            print("3. Tool call details:")
            for tc in response.tool_calls:
                print(f"   - Name: {tc['name']}")
                print(f"   - Args: {tc['args']}")
                
            return True
        else:
            print("3. ❌ NO TOOL CALLS - This would be the problem")
            return False
            
    except Exception as e:
        print(f"❌ Error with direct binding: {e}")
        return False


async def test_aug_llm_config_anthropic_tool_binding():
    """Test AugLLMConfig with Anthropic tool binding."""
    print("\n" + "="*80)  
    print("AUG LLM CONFIG ANTHROPIC TOOL BINDING TEST")
    print("="*80)
    
    # Create AnthropicLLMConfig first
    anthropic_config = AnthropicLLMConfig(
        model="claude-3-5-sonnet-20241022",
        temperature=0.3
    )
    
    # Create AugLLMConfig with Anthropic backend and structured output
    config = AugLLMConfig(
        llm_config=anthropic_config,
        structured_output_model=Plan[Task],
        force_tool_use=True
    )
    
    print("1. AugLLMConfig configuration:")
    print(f"   - LLM Config: {type(config.llm_config)}")
    print(f"   - Force tool use: {getattr(config, 'force_tool_use', 'NOT SET')}")
    print(f"   - Force tool choice: {getattr(config, 'force_tool_choice', 'NOT SET')}")
    print(f"   - Tool choice mode: {getattr(config, 'tool_choice_mode', 'NOT SET')}")
    print(f"   - Tools: {len(getattr(config, 'tools', []))}")
    print(f"   - Tool routes: {getattr(config, 'tool_routes', {})}")
    
    # Get the runnable and inspect its binding
    print("\n2. Getting runnable...")
    try:
        runnable = config.get_runnable()
        print(f"   Runnable type: {type(runnable)}")
        
        # Check the binding details
        if hasattr(runnable, 'kwargs'):
            print(f"   Runnable kwargs keys: {list(runnable.kwargs.keys())}")
            if 'tools' in runnable.kwargs:
                tools_list = runnable.kwargs['tools']
                print(f"   Tools in runnable: {len(tools_list)}")
                for i, tool in enumerate(tools_list):
                    print(f"     Tool {i+1}: {getattr(tool, 'name', str(type(tool)))} - {type(tool)}")
            if 'tool_choice' in runnable.kwargs:
                print(f"   Tool choice: {runnable.kwargs['tool_choice']}")
        
        # Test execution
        print("\n3. Testing AugLLMConfig execution...")
        result = await config.ainvoke({"objective": "Build a REST API"})
        print(f"   Result type: {type(result)}")
        
        if hasattr(result, 'tool_calls'):
            print(f"   Tool calls: {len(result.tool_calls) if result.tool_calls else 0}")
            if result.tool_calls:
                print("   Tool call details:")
                for tc in result.tool_calls:
                    print(f"     - Name: {tc.get('name', 'NO NAME')}")
                    print(f"     - Args: {tc.get('args', {})}")
        else:
            print("   No tool_calls attribute")
            
        return result
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return None


async def test_simple_anthropic_structured_output():
    """Test simple Anthropic structured output without AugLLMConfig."""
    print("\n" + "="*80)
    print("SIMPLE ANTHROPIC STRUCTURED OUTPUT TEST")
    print("="*80)
    
    try:
        from langchain_anthropic import ChatAnthropic
        from langchain_core.messages import HumanMessage
        
        # Direct structured output
        llm = ChatAnthropic(model="claude-3-5-sonnet-20241022", temperature=0.3)
        structured_llm = llm.with_structured_output(Plan[Task])
        
        print("1. Testing direct structured output...")
        result = await structured_llm.ainvoke([
            HumanMessage(content="Create a plan to build a simple REST API for a todo list")
        ])
        
        print(f"2. Result type: {type(result)}")
        print(f"   Is Plan instance: {isinstance(result, Plan)}")
        if isinstance(result, Plan):
            print(f"   Objective: {result.objective}")
            print(f"   Steps count: {len(result.steps)}")
            print(f"   Status: {result.status}")
        
        return result
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return None


async def main():
    """Run all tests."""
    print("Testing tool binding issues with Anthropic...")
    
    # Test 1: Direct Anthropic tool binding (should work)
    direct_success = await test_direct_anthropic_tool_binding()
    
    # Test 2: Simple structured output (should work)
    structured_result = await test_simple_anthropic_structured_output()
    
    # Test 3: AugLLMConfig tool binding (may not work)
    aug_result = await test_aug_llm_config_anthropic_tool_binding()
    
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Direct Anthropic tool binding: {'✅ YES' if direct_success else '❌ NO'}")
    print(f"Simple structured output: {'✅ YES' if structured_result and isinstance(structured_result, Plan) else '❌ NO'}")
    print(f"AugLLMConfig binding: {'✅ YES' if aug_result and hasattr(aug_result, 'tool_calls') and aug_result.tool_calls else '❌ NO'}")
    
    if structured_result and isinstance(structured_result, Plan):
        print("\n🎯 DIAGNOSIS: Direct structured output works perfectly!")
        print("   The issue may be that AugLLMConfig is using tool routing instead of")
        print("   direct structured output with .with_structured_output()")


if __name__ == "__main__":
    asyncio.run(main())