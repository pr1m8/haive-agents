#!/usr/bin/env python3
"""Test SimpleAgent vs ReactAgent with structured output to see which works."""

from pydantic import BaseModel, Field

from haive.agents.simple.agent import SimpleAgent
from haive.agents.react.agent import ReactAgent
from haive.core.engine.aug_llm import AugLLMConfig


class SimpleResult(BaseModel):
    """Simple structured result."""
    answer: str = Field(description="The answer")


def test_simple_agent_structured():
    """Test if SimpleAgent works with structured output."""
    
    print("🔍 Testing SimpleAgent with structured output...")
    
    engine = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
    )
    
    agent = SimpleAgent(
        name="simple_test",
        engine=engine,
        debug=True
    )
    
    print(f"   📋 Engine tool_routes: {engine.tool_routes}")
    print(f"   📋 Engine force_tool_use: {getattr(engine, 'force_tool_use', 'NOT_SET')}")
    
    try:
        print("   🎯 Executing SimpleAgent...")
        result = agent.run("What is 2+2?", debug=True)
        print(f"   ✅ SimpleAgent SUCCESS: {result}")
        return True, result
    except Exception as e:
        print(f"   ❌ SimpleAgent FAILED: {e}")
        return False, str(e)


def test_react_agent_structured():
    """Test if ReactAgent works with structured output."""
    
    print("\n🔍 Testing ReactAgent with structured output...")
    
    engine = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
    )
    
    agent = ReactAgent(
        name="react_test",
        engine=engine,
        tools=[],  # No tools to avoid confusion
        max_iterations=2,  # Limit to prevent infinite
        debug=True
    )
    
    print(f"   📋 Engine tool_routes: {engine.tool_routes}")
    print(f"   📋 Engine force_tool_use: {getattr(engine, 'force_tool_use', 'NOT_SET')}")
    
    try:
        print("   🎯 Executing ReactAgent...")
        result = agent.run("What is 2+2?", debug=True)
        print(f"   ✅ ReactAgent SUCCESS: {result}")
        return True, result
    except Exception as e:
        print(f"   ❌ ReactAgent FAILED: {e}")
        return False, str(e)


def test_comparison():
    """Compare SimpleAgent vs ReactAgent with structured output."""
    
    print("=" * 60)
    print("STRUCTURED OUTPUT COMPARISON TEST")
    print("=" * 60)
    
    # Test SimpleAgent
    simple_success, simple_result = test_simple_agent_structured()
    
    # Test ReactAgent  
    react_success, react_result = test_react_agent_structured()
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"SimpleAgent: {'✅ WORKS' if simple_success else '❌ FAILS'}")
    print(f"ReactAgent:  {'✅ WORKS' if react_success else '❌ FAILS'}")
    
    if simple_success and not react_success:
        print("\n🎯 CONCLUSION: SimpleAgent works, ReactAgent fails")
        print("   This confirms the issue is specific to ReactAgent")
    elif not simple_success and not react_success:
        print("\n🎯 CONCLUSION: Both fail - issue is in structured output system")
    elif simple_success and react_success:
        print("\n🎯 CONCLUSION: Both work - no issue found")
    else:
        print("\n🎯 CONCLUSION: ReactAgent works but SimpleAgent fails - unexpected")
    
    return simple_success, react_success


if __name__ == "__main__":
    test_comparison()