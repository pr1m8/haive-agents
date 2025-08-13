#!/usr/bin/env python3
"""Debug exactly where tool routes are being set."""

import sys
import os

# Add the packages to path  
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../src"))

from pydantic import BaseModel, Field


class SimpleResult(BaseModel):
    """Simple structured result."""
    answer: str = Field(description="The answer")


def patch_set_tool_route():
    """Patch set_tool_route to trace all calls."""
    
    import haive.core.common.mixins.tool_route_mixin as route_mixin
    
    original_set_tool_route = route_mixin.ToolRouteMixin.set_tool_route
    
    def debug_set_tool_route(self, tool_name, route, metadata=None):
        print(f"\n🔍 SET_TOOL_ROUTE CALLED:")
        print(f"   tool_name: '{tool_name}'")
        print(f"   route: '{route}'")
        print(f"   metadata: {metadata}")
        
        # Get stack trace to see where this is called from
        import traceback
        stack = traceback.extract_stack()
        print(f"   called from:")
        for frame in stack[-4:-1]:  # Show last 3 frames (excluding this one)
            print(f"     {frame.filename}:{frame.lineno} in {frame.name}")
        
        # Call original method
        result = original_set_tool_route(self, tool_name, route, metadata)
        
        print(f"   ✅ Route set")
        return result
    
    # Apply patch
    route_mixin.ToolRouteMixin.set_tool_route = debug_set_tool_route
    print("✅ Patched set_tool_route for debugging")


def test_engine_creation_trace():
    """Trace tool route setting during engine creation."""
    
    print("🔍 TRACING ENGINE CREATION")
    print("=" * 60)
    
    # Apply debug patch
    patch_set_tool_route()
    
    try:
        from haive.core.engine.aug_llm import AugLLMConfig
        
        print(f"\n📋 Creating AugLLMConfig with structured_output_model...")
        
        engine = AugLLMConfig(
            structured_output_model=SimpleResult,
            temperature=0.3,
        )
        
        print(f"\n📋 Engine created:")
        print(f"   Tool routes: {engine.tool_routes}")
        print(f"   Tools: {[str(tool) for tool in engine.tools]}")
        
        # Check if route was set correctly
        expected_route_key = 'simple_result'  # Expected sanitized name
        actual_route_keys = list(engine.tool_routes.keys())
        
        print(f"\n📋 Route analysis:")
        print(f"   Expected key: '{expected_route_key}'")
        print(f"   Actual keys: {actual_route_keys}")
        
        if expected_route_key in actual_route_keys:
            print(f"   ✅ SUCCESS: Found sanitized route key")
        else:
            print(f"   ❌ FAILED: Route key not sanitized")
        
        return engine
        
    except Exception as e:
        print(f"❌ Error creating engine: {e}")
        import traceback
        traceback.print_exc()
        return None


def test_manual_tool_route_fix():
    """Manually fix the tool route to confirm it works."""
    
    print(f"\n🔍 MANUAL TOOL ROUTE FIX TEST")
    print("=" * 60)
    
    try:
        from haive.core.engine.aug_llm import AugLLMConfig
        from haive.core.utils.naming import sanitize_tool_name
        
        # Create engine
        engine = AugLLMConfig(
            structured_output_model=SimpleResult,
            temperature=0.3,
        )
        
        print(f"📋 Before fix:")
        print(f"   Tool routes: {engine.tool_routes}")
        
        # Get actual tool name from engine output
        result = engine.invoke({"messages": [{"role": "user", "content": "What is 2+2?"}]})
        actual_tool_name = result.tool_calls[0].get('name')
        
        print(f"   Actual tool name: '{actual_tool_name}'")
        
        # Manually fix the tool route
        old_routes = dict(engine.tool_routes)
        engine.tool_routes.clear()
        
        # Set route with actual tool name
        engine.tool_routes[actual_tool_name] = "parse_output"
        
        print(f"\n📋 After manual fix:")
        print(f"   Old routes: {old_routes}")
        print(f"   New routes: {engine.tool_routes}")
        
        # Test validation router with fixed route
        from haive.core.graph.node.validation_router_v2 import validation_router_v2
        from langchain_core.messages import AIMessage, ToolMessage
        
        # Create test state
        ai_message = AIMessage(
            content="",
            tool_calls=[{
                "name": actual_tool_name,
                "args": {"answer": "4"},
                "id": "call_test123",
                "type": "tool_call"
            }]
        )
        
        success_tool_message = ToolMessage(
            content='{"success": true, "data": {"answer": "4"}}',
            name=actual_tool_name,
            tool_call_id="call_test123",
            additional_kwargs={
                "is_error": False,
                "validation_passed": True
            }
        )
        
        state = {
            "messages": [ai_message, success_tool_message],
            "tool_routes": engine.tool_routes
        }
        
        router_result = validation_router_v2(state)
        
        print(f"\n📋 Router test with manual fix:")
        print(f"   Router result: '{router_result}'")
        
        if router_result == "parse_output":
            print(f"   ✅ SUCCESS: Manual fix works!")
            return True
        else:
            print(f"   ❌ FAILED: Even manual fix doesn't work")
            return False
        
    except Exception as e:
        print(f"❌ Error in manual fix test: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run tool route setting debug."""
    
    print("🔬 TOOL ROUTE SETTING DEBUG")
    print("=" * 80)
    
    # Test 1: Trace engine creation
    engine = test_engine_creation_trace()
    
    # Test 2: Manual fix to confirm it would work
    manual_works = test_manual_tool_route_fix()
    
    print(f"\n" + "=" * 80)
    print("🎯 DEBUG SUMMARY:")
    print(f"   Engine created: {'✅' if engine else '❌'}")
    print(f"   Manual fix works: {'✅' if manual_works else '❌'}")
    
    if manual_works:
        print(f"\n📋 SOLUTION:")
        print(f"   The manual fix works, so we need to ensure the automatic")
        print(f"   tool route setting uses sanitized names consistently.")
        print(f"   Check where set_tool_route is called during engine creation.")


if __name__ == "__main__":
    main()