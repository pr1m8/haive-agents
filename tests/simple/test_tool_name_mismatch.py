#!/usr/bin/env python3
"""Test the exact tool name mismatch causing the routing issue."""

import sys
import os

# Add the packages to path  
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../src"))

from pydantic import BaseModel, Field
from langchain_core.messages import AIMessage, ToolMessage


class SimpleResult(BaseModel):
    """Simple structured result."""
    answer: str = Field(description="The answer")


def test_tool_name_mismatch():
    """Test the exact name mismatch between tool call and tool routes."""
    
    print("🔍 TOOL NAME MISMATCH ANALYSIS")
    print("=" * 60)
    
    try:
        from haive.core.engine.aug_llm import AugLLMConfig
        from haive.core.graph.node.validation_router_v2 import validation_router_v2
        
        # Create engine like SimpleAgent does
        engine = AugLLMConfig(
            structured_output_model=SimpleResult,
            temperature=0.3,
        )
        
        print(f"📋 Engine setup:")
        print(f"   - tool_routes: {engine.tool_routes}")
        print(f"   - tools: {[tool.name if hasattr(tool, 'name') else str(tool) for tool in engine.tools]}")
        
        # Get a real tool call from the engine
        result = engine.invoke({"messages": [{"role": "user", "content": "What is 2+2?"}]})
        
        if result.tool_calls:
            tool_call = result.tool_calls[0]
            tool_call_name = tool_call.get('name')
            tool_call_id = tool_call.get('id')
            tool_call_args = tool_call.get('args')
            
            print(f"\n📋 Real engine output:")
            print(f"   - tool_call_name: '{tool_call_name}'")
            print(f"   - tool_call_args: {tool_call_args}")
            
            # Check if tool name exists in routes
            route_exists = tool_call_name in engine.tool_routes
            print(f"   - route exists for '{tool_call_name}': {route_exists}")
            
            if not route_exists:
                print(f"   ❌ MISMATCH: Tool call name '{tool_call_name}' not found in routes!")
                print(f"   📋 Available route keys: {list(engine.tool_routes.keys())}")
                
                # Check if there's a case mismatch
                for route_key in engine.tool_routes.keys():
                    if route_key.lower() == tool_call_name.lower():
                        print(f"   🔍 FOUND CASE MISMATCH: '{tool_call_name}' vs '{route_key}'")
            
            # Create state that validation_router_v2 would receive
            ai_message = AIMessage(
                content="",
                tool_calls=[tool_call]
            )
            
            # Simulate ValidationNodeV2 creating a SUCCESS ToolMessage
            success_tool_message = ToolMessage(
                content='{"success": true, "data": {"answer": "4"}}',
                name=tool_call_name,  # Use the ACTUAL tool call name
                tool_call_id=tool_call_id,
                additional_kwargs={
                    "is_error": False,
                    "validation_passed": True
                }
            )
            
            # Test state with the actual tool call name
            state = {
                "messages": [ai_message, success_tool_message],
                "tool_routes": engine.tool_routes  # Use actual routes from engine
            }
            
            print(f"\n📋 Testing validation_router_v2:")
            print(f"   - ToolMessage name: '{success_tool_message.name}'")
            print(f"   - Tool routes: {state['tool_routes']}")
            print(f"   - ToolMessage is_error: {success_tool_message.additional_kwargs.get('is_error')}")
            
            # Call the router
            router_result = validation_router_v2(state)
            
            print(f"   🎯 Router result: '{router_result}'")
            
            if router_result == "agent_node":
                print(f"   ❌ ROUTES TO AGENT_NODE - This causes infinite loop!")
                print(f"   📋 Likely because tool name '{tool_call_name}' not found in routes")
            elif router_result == "parse_output":
                print(f"   ✅ ROUTES TO PARSE_OUTPUT - This would work correctly")
            else:
                print(f"   🤔 ROUTES TO: {router_result}")
            
            return tool_call_name, list(engine.tool_routes.keys()), router_result
            
    except Exception as e:
        print(f"❌ Error in test: {e}")
        import traceback
        traceback.print_exc()
        return None, None, None


def test_route_lookup_logic():
    """Test the exact logic validation_router_v2 uses for route lookup."""
    
    print(f"\n🔍 ROUTE LOOKUP LOGIC TEST")
    print("=" * 60)
    
    try:
        from haive.core.graph.node.validation_router_v2 import validation_router_v2
        
        # Simulate the exact name mismatch we found
        tool_call_name = "simple_result"  # lowercase - what engine produces
        route_key = "SimpleResult"        # uppercase - what's in tool_routes
        
        # Create state with the mismatch
        state = {
            "messages": [],
            "tool_routes": {route_key: "parse_output"}  # Route uses uppercase
        }
        
        print(f"📋 Simulated mismatch:")
        print(f"   - Tool call name: '{tool_call_name}'")
        print(f"   - Route key: '{route_key}'")
        print(f"   - Tool routes: {state['tool_routes']}")
        
        # Check lookup manually
        route_found = state["tool_routes"].get(tool_call_name)
        print(f"   - Direct lookup result: {route_found}")
        
        if route_found is None:
            print(f"   ❌ LOOKUP FAILED - Tool name not found in routes!")
            print(f"   📋 This explains why router goes to agent_node")
        else:
            print(f"   ✅ LOOKUP SUCCESS - Found route: {route_found}")
        
        # Check if case-insensitive lookup would work
        for key, value in state["tool_routes"].items():
            if key.lower() == tool_call_name.lower():
                print(f"   🔍 Case-insensitive match found: '{key}' -> '{value}'")
                break
        
    except Exception as e:
        print(f"❌ Error in route lookup test: {e}")


def main():
    """Run tool name mismatch analysis."""
    
    print("🔬 TOOL NAME MISMATCH ANALYSIS")
    print("=" * 80)
    
    # Test the actual mismatch
    tool_name, route_keys, router_result = test_tool_name_mismatch()
    
    # Test the lookup logic
    test_route_lookup_logic()
    
    print(f"\n" + "=" * 80)
    print("🎯 ROOT CAUSE IDENTIFIED:")
    if tool_name and route_keys:
        print(f"   Tool call name: '{tool_name}'")
        print(f"   Route keys: {route_keys}")
        print(f"   Router result: '{router_result}'")
        
        if tool_name not in route_keys:
            print(f"\n❌ CONFIRMED: Tool name mismatch causes infinite loop!")
            print(f"   The engine produces tool calls with name '{tool_name}'")
            print(f"   But tool_routes only has keys: {route_keys}")
            print(f"   validation_router_v2 can't find the route, defaults to agent_node")
            print(f"   This creates the infinite loop we observed!")
    
    print(f"\n📋 SOLUTION:")
    print(f"   Fix the tool name generation in AugLLMConfig to match the route keys")
    print(f"   OR fix the route key generation to match the tool names")


if __name__ == "__main__":
    main()