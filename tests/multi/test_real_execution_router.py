#!/usr/bin/env python3
"""Test validation router with the EXACT state from real execution."""

import logging
from pydantic import BaseModel, Field

from haive.agents.react.agent import ReactAgent
from haive.core.engine.aug_llm import AugLLMConfig

# Patch the validation router to log what it receives
original_validation_router_v2 = None

def debug_validation_router_v2(state):
    """Debug wrapper for validation_router_v2."""
    print(f"\n🔍 VALIDATION ROUTER CALLED")
    print(f"   📋 State keys: {list(state.keys())}")
    print(f"   📋 Messages count: {len(state.get('messages', []))}")
    print(f"   📋 Tool routes: {state.get('tool_routes', {})}")
    
    messages = state.get('messages', [])
    print(f"   📋 Last 3 messages:")
    for i, msg in enumerate(messages[-3:]):
        print(f"     {i}: {type(msg).__name__}: {str(msg)[:100]}...")
    
    # Call the original function
    from haive.core.graph.node.validation_router_v2 import validation_router_v2
    result = validation_router_v2(state)
    print(f"   🎯 Router returned: '{result}'")
    
    return result


class SimpleResult(BaseModel):
    """Simple structured result."""
    answer: str = Field(description="The answer")


def test_real_execution_router():
    """Patch the router and see what it gets called with."""
    
    print("🔍 Testing validation router with REAL execution state...")
    
    # Patch the validation router
    import haive.core.graph.node.validation_router_v2
    haive.core.graph.node.validation_router_v2.validation_router_v2 = debug_validation_router_v2
    
    # Also patch the SimpleAgent's import
    import haive.agents.simple.agent
    haive.agents.simple.agent.validation_router_v2 = debug_validation_router_v2
    
    try:
        # Create agent
        engine = AugLLMConfig(
            structured_output_model=SimpleResult,
            temperature=0.3,
        )
        
        agent = ReactAgent(
            name="real_test",
            engine=engine,
            max_iterations=1,  # Limit to prevent infinite
            debug=True
        )
        
        print(f"   ✅ Agent created, attempting execution...")
        
        # Execute with limited iterations
        result = agent.run("What is 2+2?", debug=True)
        print(f"   ✅ Execution result: {result}")
        
    except Exception as e:
        print(f"   ❌ Execution failed: {e}")
    
    finally:
        # Restore original function
        from haive.core.graph.node.validation_router_v2 import validation_router_v2 as original
        haive.core.graph.node.validation_router_v2.validation_router_v2 = original
        haive.agents.simple.agent.validation_router_v2 = original


if __name__ == "__main__":
    # Set logging to INFO to see router logs
    logging.getLogger('haive.core.graph.node.validation_router_v2').setLevel(logging.INFO)
    test_real_execution_router()