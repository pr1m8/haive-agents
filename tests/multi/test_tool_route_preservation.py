#!/usr/bin/env python3
"""Test that tool routes are preserved correctly from engine to state."""

from pydantic import BaseModel, Field

from haive.agents.react.agent import ReactAgent
from haive.core.engine.aug_llm import AugLLMConfig


class SimpleResult(BaseModel):
    """Simple structured result."""
    answer: str = Field(description="The answer")


def test_tool_route_preservation():
    """Test that parse_output route is preserved from engine to state."""
    
    print("🔍 Testing tool route preservation...")
    
    # Create engine with structured output
    engine = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
        system_message="You are a helpful assistant."
    )
    
    print(f"   - Engine tool_routes: {engine.tool_routes}")
    print(f"   - Engine tools: {engine.tools}")
    print(f"   - Engine engine_type: {getattr(engine, 'engine_type', 'NOT_FOUND')}")
    
    # Create ReactAgent
    agent = ReactAgent(
        name="route_test",
        engine=engine,
        tools=[],
        max_iterations=2,
        debug=False
    )
    
    print(f"   - Agent state tool_routes: {agent.tool_routes}")
    print(f"   - Agent has engine field: {hasattr(agent, 'engine')}")
    print(f"   - Agent engine is same object: {agent.engine is engine}")
    
    # Check all fields to see what _sync_tools_from_instance_engines would find
    print(f"   - Agent fields with engine_type:")
    for field_name, field_value in agent.__dict__.items():
        if hasattr(field_value, "engine_type"):
            has_tools = hasattr(field_value, "tools")
            tools_count = len(field_value.tools) if has_tools else 0
            tool_routes = getattr(field_value, "tool_routes", {})
            print(f"     - {field_name}: has_tools={has_tools}, tools_count={tools_count}, tool_routes={tool_routes}")
    
    # Check specific route for SimpleResult
    simple_result_route_engine = engine.tool_routes.get("SimpleResult")
    simple_result_route_state = agent.tool_routes.get("SimpleResult")
    
    print(f"   - Engine route for SimpleResult: {simple_result_route_engine}")
    print(f"   - State route for SimpleResult: {simple_result_route_state}")
    
    # Check if routes match
    if simple_result_route_engine == simple_result_route_state:
        print("✅ Tool routes preserved correctly!")
        return True
    else:
        print("❌ Tool routes NOT preserved - route override detected!")
        print(f"   - Expected: {simple_result_route_engine}")
        print(f"   - Actual: {simple_result_route_state}")
        return False


if __name__ == "__main__":
    success = test_tool_route_preservation()
    
    if success:
        print("\n✅ Tool route preservation test PASSED")
    else:
        print("\n❌ Tool route preservation test FAILED")
        print("   - The fix needs additional work")