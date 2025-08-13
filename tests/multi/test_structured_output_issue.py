#!/usr/bin/env python3
"""Test to isolate the structured output infinite loop issue."""

from pydantic import BaseModel, Field

from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


class SimpleResult(BaseModel):
    """Simple structured result."""
    answer: str = Field(description="The answer")


def test_without_structured_output():
    """Test SimpleAgent WITHOUT structured output - should work."""
    
    print("🔍 Testing SimpleAgent WITHOUT structured output...")
    
    engine = AugLLMConfig(
        temperature=0.3,
        # NO structured_output_model
    )
    
    agent = SimpleAgent(
        name="no_struct_test",
        engine=engine,
        debug=True
    )
    
    print(f"   📋 Engine force_tool_use: {getattr(engine, 'force_tool_use', 'NOT_SET')}")
    print(f"   📋 Engine tools: {len(engine.tools)}")
    print(f"   📋 Engine tool_routes: {engine.tool_routes}")
    
    try:
        print("   🎯 Executing SimpleAgent without structured output...")
        result = agent.run("What is 2+2?", debug=False)  # Disable debug to reduce noise
        print(f"   ✅ WITHOUT structured output SUCCESS: {result}")
        return True, result
    except Exception as e:
        print(f"   ❌ WITHOUT structured output FAILED: {e}")
        return False, str(e)


def test_with_structured_output():
    """Test SimpleAgent WITH structured output - may fail."""
    
    print("\n🔍 Testing SimpleAgent WITH structured output...")
    
    engine = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
    )
    
    agent = SimpleAgent(
        name="struct_test",
        engine=engine,
        debug=True,
        max_iterations=3  # Limit iterations to prevent infinite loop
    )
    
    print(f"   📋 Engine force_tool_use: {getattr(engine, 'force_tool_use', 'NOT_SET')}")
    print(f"   📋 Engine tools: {len(engine.tools)}")
    print(f"   📋 Engine tool_routes: {engine.tool_routes}")
    
    try:
        print("   🎯 Executing SimpleAgent with structured output...")
        result = agent.run("What is 2+2?", debug=False)  # Disable debug to reduce noise
        print(f"   ✅ WITH structured output SUCCESS: {result}")
        return True, result
    except Exception as e:
        print(f"   ❌ WITH structured output FAILED: {e}")
        return False, str(e)


def test_force_tool_use_disabled():
    """Test with structured output but force_tool_use=False."""
    
    print("\n🔍 Testing SimpleAgent WITH structured output but force_tool_use=False...")
    
    engine = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
        force_tool_use=False  # Explicitly disable
    )
    
    agent = SimpleAgent(
        name="no_force_test",
        engine=engine,
        debug=True
    )
    
    print(f"   📋 Engine force_tool_use: {getattr(engine, 'force_tool_use', 'NOT_SET')}")
    print(f"   📋 Engine tools: {len(engine.tools)}")
    print(f"   📋 Engine tool_routes: {engine.tool_routes}")
    
    try:
        print("   🎯 Executing SimpleAgent with force_tool_use=False...")
        result = agent.run("What is 2+2?", debug=False)  # Disable debug to reduce noise
        print(f"   ✅ force_tool_use=False SUCCESS: {result}")
        return True, result
    except Exception as e:
        print(f"   ❌ force_tool_use=False FAILED: {e}")
        return False, str(e)


def main():
    """Run all tests to isolate the issue."""
    
    print("=" * 80)
    print("STRUCTURED OUTPUT INFINITE LOOP DEBUG")
    print("=" * 80)
    
    # Test 1: Without structured output (baseline)
    no_struct_success, no_struct_result = test_without_structured_output()
    
    # Test 2: With structured output (should fail)
    struct_success, struct_result = test_with_structured_output()
    
    # Test 3: With structured output but no force_tool_use
    no_force_success, no_force_result = test_force_tool_use_disabled()
    
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"WITHOUT structured output: {'✅ WORKS' if no_struct_success else '❌ FAILS'}")
    print(f"WITH structured output:    {'✅ WORKS' if struct_success else '❌ FAILS'}")
    print(f"WITH structured, no force: {'✅ WORKS' if no_force_success else '❌ FAILS'}")
    
    if no_struct_success and not struct_success and no_force_success:
        print("\n🎯 CONCLUSION: The issue is force_tool_use=True with structured output")
        print("   - Normal agents work fine")
        print("   - Structured output + force_tool_use=False works") 
        print("   - Structured output + force_tool_use=True causes infinite loop")
    elif no_struct_success and not struct_success and not no_force_success:
        print("\n🎯 CONCLUSION: The issue is structured output itself, not force_tool_use")
    elif not no_struct_success:
        print("\n🎯 CONCLUSION: The issue is deeper - even basic agents fail")
    else:
        print("\n🎯 CONCLUSION: Unexpected results - need more investigation")


if __name__ == "__main__":
    main()