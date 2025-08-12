#!/usr/bin/env python3
"""Test the actual execution to see if state routes are preserved."""

from pydantic import BaseModel, Field

from haive.agents.react.agent import ReactAgent
from haive.core.engine.aug_llm import AugLLMConfig


class SimpleResult(BaseModel):
    """Simple structured result."""
    answer: str = Field(description="The answer")


def test_execution_state_routes():
    """Test if routes are preserved in actual execution state."""
    
    print("🔍 Testing actual execution state routes...")
    
    # Create engine with structured output
    engine = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
        system_message="You are a helpful assistant."
    )
    
    print(f"   ✅ Engine tool_routes: {engine.tool_routes}")
    
    # Create ReactAgent
    agent = ReactAgent(
        name="execution_test",
        engine=engine,
        tools=[],
        max_iterations=2,
        debug=True
    )
    
    print(f"   ✅ Agent tool_routes (should be empty): {agent.tool_routes}")
    
    # Check if we can access the state schema and see its routes
    if hasattr(agent, 'state_schema'):
        print(f"   ✅ Agent has state_schema: {agent.state_schema.__name__}")
        
        # Create a state instance to see its routes
        state_instance = agent.state_schema()
        print(f"   ✅ State instance tool_routes: {getattr(state_instance, 'tool_routes', 'NO_ROUTES')}")
        
        # Set the engine on the state (simulating what happens during execution)
        state_instance.engine = engine
        print(f"   ✅ After setting engine, state tool_routes: {state_instance.tool_routes}")
    
    # Try running the agent with a simple input and see what happens
    print("\n🔍 Testing actual execution...")
    
    try:
        # Use a timeout and limited iterations to prevent infinite loops
        result = agent.run(
            "What is 2+2?",
            debug=True,
            max_iterations_override=1  # Limit to 1 iteration
        )
        print(f"   ✅ Execution completed: {type(result)}")
        if hasattr(result, 'answer'):
            print(f"   ✅ Result answer: {result.answer}")
    except Exception as e:
        print(f"   ❌ Execution failed: {e}")
    
    return True


if __name__ == "__main__":
    test_execution_state_routes()