#!/usr/bin/env python3
"""Debug why tool routes aren't syncing from engine to state."""

from pydantic import BaseModel, Field

from haive.agents.react.agent import ReactAgent
from haive.core.engine.aug_llm import AugLLMConfig


class SimpleResult(BaseModel):
    """Simple structured result."""
    answer: str = Field(description="The answer")


def test_state_sync_debug():
    """Debug the state sync process step by step."""
    
    print("🔍 Creating engine with structured output...")
    
    # Create engine with structured output
    engine = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
        system_message="You are a helpful assistant."
    )
    
    print(f"   ✅ Engine created with tool_routes: {engine.tool_routes}")
    print(f"   ✅ Engine tools: {[type(t).__name__ for t in engine.tools]}")
    
    print("\n🔍 Creating ReactAgent...")
    
    # Create ReactAgent - this should trigger state sync
    agent = ReactAgent(
        name="sync_test",
        engine=engine,
        tools=[],
        max_iterations=2,
        debug=True  # Enable debug to see sync messages
    )
    
    print(f"\n   ✅ Agent created")
    print(f"   - Agent.engine is same object: {agent.engine is engine}")
    print(f"   - Agent.engine.tool_routes: {agent.engine.tool_routes}")
    print(f"   - Agent state schema: {agent.state_schema.__name__}")
    
    # Check if agent state has tool_routes attribute
    if hasattr(agent, 'tool_routes'):
        print(f"   - Agent.tool_routes: {agent.tool_routes}")
    else:
        print("   ❌ Agent has no tool_routes attribute")
    
    # Create a state instance to see if it syncs
    print("\n🔍 Creating state instance manually...")
    
    state_instance = agent.state_schema()
    print(f"   - State instance tool_routes: {getattr(state_instance, 'tool_routes', 'NO_ATTRIBUTE')}")
    
    # Check if state instance has the engine field
    print(f"   - State instance has engine field: {hasattr(state_instance, 'engine')}")
    if hasattr(state_instance, 'engine'):
        print(f"   - State instance engine: {getattr(state_instance, 'engine', None)}")
    
    # Check all fields for engines
    print("\n🔍 Checking state instance fields for engines...")
    for field_name, field_value in state_instance.__dict__.items():
        if hasattr(field_value, "engine_type"):
            print(f"   - {field_name}: {field_value} (tool_routes: {getattr(field_value, 'tool_routes', 'NONE')})")
    
    # Check if we can manually assign the engine and trigger sync
    print("\n🔍 Manually setting engine on state and checking sync...")
    
    # Set the engine on state
    state_instance.engine = engine
    print(f"   - After setting engine, state tool_routes: {getattr(state_instance, 'tool_routes', 'NO_ATTRIBUTE')}")
    
    # Manually call sync method if it exists
    if hasattr(state_instance, '_sync_tools_from_instance_engines'):
        print("   - Manually calling _sync_tools_from_instance_engines...")
        state_instance._sync_tools_from_instance_engines()
        print(f"   - After manual sync, state tool_routes: {state_instance.tool_routes}")
    
    return state_instance


if __name__ == "__main__":
    test_state_sync_debug()