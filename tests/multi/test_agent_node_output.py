#!/usr/bin/env python3
"""Test what the agent_node is actually outputting."""

from pydantic import BaseModel, Field

from haive.agents.simple.agent import SimpleAgent
from haive.agents.react.agent import ReactAgent
from haive.core.engine.aug_llm import AugLLMConfig


class SimpleResult(BaseModel):
    """Simple structured result."""
    answer: str = Field(description="The answer")


def test_simple_agent_force_tool_use():
    """Check if SimpleAgent should have force_tool_use=True."""
    
    print("🔍 Testing SimpleAgent with structured output...")
    
    engine = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
    )
    
    print(f"   📋 Engine force_tool_use: {getattr(engine, 'force_tool_use', 'NOT_SET')}")
    print(f"   📋 Engine tool_choice_mode: {getattr(engine, 'tool_choice_mode', 'NOT_SET')}")
    
    # SimpleAgent with structured output SHOULD have force_tool_use=True
    # Because it needs to always call the structured output tool
    
    agent = SimpleAgent(
        name="simple_test",
        engine=engine,
        debug=True
    )
    
    print(f"   📋 Agent type: {type(agent).__name__}")
    print(f"   📋 Agent engine force_tool_use: {getattr(agent.engine, 'force_tool_use', 'NOT_SET')}")


def test_react_agent_force_tool_use():
    """Check if ReactAgent should have force_tool_use=True."""
    
    print("\n🔍 Testing ReactAgent with structured output...")
    
    engine = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
    )
    
    print(f"   📋 Engine force_tool_use: {getattr(engine, 'force_tool_use', 'NOT_SET')}")
    print(f"   📋 Engine tool_choice_mode: {getattr(engine, 'tool_choice_mode', 'NOT_SET')}")
    
    # ReactAgent with structured output should NOT have force_tool_use=True
    # Because ReAct needs to decide when to use tools vs give final answer
    
    agent = ReactAgent(
        name="react_test",
        engine=engine,
        tools=[],  # No additional tools
        debug=True
    )
    
    print(f"   📋 Agent type: {type(agent).__name__}")
    print(f"   📋 Agent engine force_tool_use: {getattr(agent.engine, 'force_tool_use', 'NOT_SET')}")


def test_react_agent_without_structured_output():
    """Check ReactAgent without structured output."""
    
    print("\n🔍 Testing ReactAgent WITHOUT structured output...")
    
    engine = AugLLMConfig(
        temperature=0.3,
        # No structured_output_model
    )
    
    print(f"   📋 Engine force_tool_use: {getattr(engine, 'force_tool_use', 'NOT_SET')}")
    print(f"   📋 Engine tool_choice_mode: {getattr(engine, 'tool_choice_mode', 'NOT_SET')}")
    
    agent = ReactAgent(
        name="react_no_struct",
        engine=engine,
        tools=[],  # No tools
        debug=True
    )
    
    print(f"   📋 Agent type: {type(agent).__name__}")
    print(f"   📋 Agent engine force_tool_use: {getattr(agent.engine, 'force_tool_use', 'NOT_SET')}")


def main():
    """Test different agent configurations."""
    
    print("=" * 80)
    print("AGENT FORCE_TOOL_USE ANALYSIS")
    print("=" * 80)
    
    test_simple_agent_force_tool_use()
    test_react_agent_force_tool_use()
    test_react_agent_without_structured_output()
    
    print("\n" + "=" * 80)
    print("ANALYSIS")
    print("=" * 80)
    print("Key Questions:")
    print("1. Should SimpleAgent with structured_output have force_tool_use=True?")
    print("   → YES - it must always call the structured output tool")
    print("")
    print("2. Should ReactAgent with structured_output have force_tool_use=True?")
    print("   → NO - ReAct needs to decide when to use tools vs final answer")
    print("")
    print("3. Should ReactAgent without structured_output have force_tool_use?")
    print("   → NO - ReAct should decide when to use tools")


if __name__ == "__main__":
    main()