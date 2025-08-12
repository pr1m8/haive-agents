#!/usr/bin/env python3
"""Test if force_tool_use is causing the infinite loop."""

from pydantic import BaseModel, Field

from haive.agents.react.agent import ReactAgent
from haive.core.engine.aug_llm import AugLLMConfig


class SimpleResult(BaseModel):
    """Simple structured result."""
    answer: str = Field(description="The answer")


def test_force_tool_use_impact():
    """Test with and without force_tool_use."""
    
    print("🔍 Testing force_tool_use impact...")
    
    # Test 1: With force_tool_use (default for structured output)
    print("\n   📋 Test 1: With force_tool_use=True (default)")
    engine1 = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
    )
    print(f"     - Engine force_tool_use: {getattr(engine1, 'force_tool_use', 'NOT_SET')}")
    print(f"     - Engine tool_choice_mode: {getattr(engine1, 'tool_choice_mode', 'NOT_SET')}")
    
    agent1 = ReactAgent(
        name="force_tool_test",
        engine=engine1,
        max_iterations=1,  # Limit to 1 to prevent infinite
        debug=False
    )
    
    # Test 2: Explicitly disable force_tool_use  
    print("\n   📋 Test 2: With force_tool_use=False")
    engine2 = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
        force_tool_use=False  # Explicitly disable
    )
    print(f"     - Engine force_tool_use: {getattr(engine2, 'force_tool_use', 'NOT_SET')}")
    print(f"     - Engine tool_choice_mode: {getattr(engine2, 'tool_choice_mode', 'NOT_SET')}")
    
    agent2 = ReactAgent(
        name="no_force_tool_test", 
        engine=engine2,
        max_iterations=1,
        debug=False
    )
    
    # Test 3: Check what happens with 'auto' tool choice
    print("\n   📋 Test 3: With tool_choice_mode='auto'")
    engine3 = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
        tool_choice_mode="auto"  # Let LLM decide
    )
    print(f"     - Engine force_tool_use: {getattr(engine3, 'force_tool_use', 'NOT_SET')}")
    print(f"     - Engine tool_choice_mode: {getattr(engine3, 'tool_choice_mode', 'NOT_SET')}")
    
    agent3 = ReactAgent(
        name="auto_tool_test",
        engine=engine3,
        max_iterations=1,
        debug=False
    )
    
    print(f"\n   🎯 Summary:")
    print(f"     - Agent 1 force_tool_use: {getattr(agent1.engine, 'force_tool_use', 'NOT_SET')}")
    print(f"     - Agent 2 force_tool_use: {getattr(agent2.engine, 'force_tool_use', 'NOT_SET')}")  
    print(f"     - Agent 3 force_tool_use: {getattr(agent3.engine, 'force_tool_use', 'NOT_SET')}")
    
    # All configs should route to parse_output
    for i, agent in enumerate([agent1, agent2, agent3], 1):
        if hasattr(agent, 'state_schema'):
            state = agent.state_schema()
            state.engine = agent.engine
            print(f"     - Agent {i} state tool_routes: {getattr(state, 'tool_routes', 'NO_ROUTES')}")
    
    return agent1, agent2, agent3


if __name__ == "__main__":
    test_force_tool_use_impact()