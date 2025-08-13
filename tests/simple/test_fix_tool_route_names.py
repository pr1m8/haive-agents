#!/usr/bin/env python3
"""Fix the tool route name mismatch by using snake_case names."""

import sys
import os

# Add the packages to path  
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../src"))

from pydantic import BaseModel, Field


class SimpleResult(BaseModel):
    """Simple structured result."""
    answer: str = Field(description="The answer")


def convert_to_snake_case(name: str) -> str:
    """Convert PascalCase to snake_case like LangChain does."""
    import re
    # Insert underscore before uppercase letters
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    # Insert underscore before uppercase letters preceded by lowercase
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def test_tool_name_conversion():
    """Test the tool name conversion logic."""
    
    print("🔍 TOOL NAME CONVERSION TEST")
    print("=" * 60)
    
    class_names = ["SimpleResult", "ComplexDataModel", "UserProfile", "APIResponse"]
    
    for class_name in class_names:
        snake_name = convert_to_snake_case(class_name)
        print(f"   {class_name} → {snake_name}")
    
    # Test with actual SimpleResult
    expected_tool_name = convert_to_snake_case("SimpleResult")
    print(f"\n📋 Expected tool name for SimpleResult: '{expected_tool_name}'")
    
    return expected_tool_name


def test_fixed_engine():
    """Test engine with corrected tool route names."""
    
    print(f"\n🔍 TESTING FIXED ENGINE")
    print("=" * 60)
    
    try:
        from haive.core.engine.aug_llm import AugLLMConfig
        
        # Create engine
        engine = AugLLMConfig(
            structured_output_model=SimpleResult,
            temperature=0.3,
        )
        
        print(f"📋 Original engine setup:")
        print(f"   - tool_routes: {engine.tool_routes}")
        
        # Get the actual tool name from engine output
        result = engine.invoke({"messages": [{"role": "user", "content": "What is 2+2?"}]})
        
        if result.tool_calls:
            actual_tool_name = result.tool_calls[0].get('name')
            print(f"   - actual tool name: '{actual_tool_name}'")
            
            # Check if route exists
            route_exists = actual_tool_name in engine.tool_routes
            print(f"   - route exists: {route_exists}")
            
            if not route_exists:
                print(f"   ❌ MISMATCH: Need to fix tool route key")
                
                # Fix the tool route
                original_route = engine.tool_routes.get("SimpleResult")
                if original_route:
                    engine.tool_routes[actual_tool_name] = original_route
                    del engine.tool_routes["SimpleResult"]
                    print(f"   ✅ FIXED: Updated route key to '{actual_tool_name}'")
                    print(f"   - new tool_routes: {engine.tool_routes}")
            
            return engine, actual_tool_name
            
    except Exception as e:
        print(f"❌ Error in test: {e}")
        return None, None


def test_validation_router_with_fix():
    """Test validation router with the fixed tool routes."""
    
    print(f"\n🔍 TESTING VALIDATION ROUTER WITH FIX")
    print("=" * 60)
    
    engine, actual_tool_name = test_fixed_engine()
    
    if not engine or not actual_tool_name:
        print("❌ Could not get fixed engine")
        return
    
    try:
        from haive.core.graph.node.validation_router_v2 import validation_router_v2
        from langchain_core.messages import AIMessage, ToolMessage
        
        # Create test state with corrected tool name
        ai_message = AIMessage(
            content="",
            tool_calls=[{
                "name": actual_tool_name,  # Use the actual tool name
                "args": {"answer": "4"},
                "id": "call_test123",
                "type": "tool_call"
            }]
        )
        
        # Success ToolMessage with corrected name
        success_tool_message = ToolMessage(
            content='{"success": true, "data": {"answer": "4"}}',
            name=actual_tool_name,  # Use the actual tool name
            tool_call_id="call_test123",
            additional_kwargs={
                "is_error": False,
                "validation_passed": True
            }
        )
        
        # Test state with fixed tool routes
        state = {
            "messages": [ai_message, success_tool_message],
            "tool_routes": engine.tool_routes  # Use fixed routes
        }
        
        print(f"📋 Test state:")
        print(f"   - tool_call_name: '{actual_tool_name}'")
        print(f"   - tool_routes: {state['tool_routes']}")
        print(f"   - route lookup: {state['tool_routes'].get(actual_tool_name)}")
        
        # Call validation router
        router_result = validation_router_v2(state)
        
        print(f"   🎯 Router result: '{router_result}'")
        
        if router_result == "parse_output":
            print(f"   ✅ SUCCESS: Routes to parse_output - infinite loop FIXED!")
        elif router_result == "agent_node":
            print(f"   ❌ STILL BROKEN: Routes to agent_node")
        else:
            print(f"   🤔 UNEXPECTED: Routes to {router_result}")
        
        return router_result
        
    except Exception as e:
        print(f"❌ Error testing router: {e}")
        import traceback
        traceback.print_exc()


def main():
    """Run tool route name fix test."""
    
    print("🔬 TOOL ROUTE NAME FIX TEST")
    print("=" * 80)
    
    # Test name conversion
    expected_name = test_tool_name_conversion()
    
    # Test fixed engine
    engine, actual_name = test_fixed_engine()
    
    # Test validation router with fix
    router_result = test_validation_router_with_fix()
    
    print(f"\n" + "=" * 80)
    print("🎯 RESULTS:")
    print(f"   Expected tool name: '{expected_name}'")
    print(f"   Actual tool name: '{actual_name}'")
    print(f"   Router result: '{router_result}'")
    
    if router_result == "parse_output":
        print(f"\n✅ FIX CONFIRMED: Tool route name correction solves infinite loop!")
        print(f"\n📋 SOLUTION:")
        print(f"   Update StructuredOutputMixin to use snake_case tool names")
        print(f"   Convert '{SimpleResult.__name__}' to '{convert_to_snake_case(SimpleResult.__name__)}'")
        print(f"   This matches what LangChain's bind_tools actually produces")
    else:
        print(f"\n❌ FIX NOT WORKING: Need to investigate further")


if __name__ == "__main__":
    main()