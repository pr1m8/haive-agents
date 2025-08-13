#!/usr/bin/env python3
"""Test the infinite loop fix with corrected tool route names."""

import sys
import os
import signal

# Add the packages to path  
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../src"))

from pydantic import BaseModel, Field


class SimpleResult(BaseModel):
    """Simple structured result."""
    answer: str = Field(description="The answer")


def test_fixed_tool_routes():
    """Test that tool routes now use sanitized names."""
    
    print("🔍 TESTING FIXED TOOL ROUTES")
    print("=" * 60)
    
    try:
        from haive.core.engine.aug_llm import AugLLMConfig
        
        # Create engine
        engine = AugLLMConfig(
            structured_output_model=SimpleResult,
            temperature=0.3,
        )
        
        print(f"📋 Engine with fix:")
        print(f"   Tool routes: {engine.tool_routes}")
        
        # Get actual tool name from output
        result = engine.invoke({"messages": [{"role": "user", "content": "What is 2+2?"}]})
        
        if result.tool_calls:
            actual_tool_name = result.tool_calls[0].get('name')
            print(f"   Actual tool name: '{actual_tool_name}'")
            
            # Check if route exists for actual name
            route_exists = actual_tool_name in engine.tool_routes
            route_value = engine.tool_routes.get(actual_tool_name)
            
            print(f"   Route exists: {route_exists}")
            print(f"   Route value: {route_value}")
            
            if route_exists and route_value == "parse_output":
                print(f"   ✅ SUCCESS: Route correctly set for sanitized name!")
                return True
            else:
                print(f"   ❌ FAILED: Route not found or incorrect")
                return False
        
    except Exception as e:
        print(f"❌ Error testing fixed routes: {e}")
        return False


def test_validation_router_with_fix():
    """Test validation router with the fixed tool routes."""
    
    print(f"\n🔍 TESTING VALIDATION ROUTER WITH FIX")
    print("=" * 60)
    
    try:
        from haive.core.engine.aug_llm import AugLLMConfig
        from haive.core.graph.node.validation_router_v2 import validation_router_v2
        from langchain_core.messages import AIMessage, ToolMessage
        
        # Create engine with fix
        engine = AugLLMConfig(
            structured_output_model=SimpleResult,
            temperature=0.3,
        )
        
        # Get actual tool name
        result = engine.invoke({"messages": [{"role": "user", "content": "What is 2+2?"}]})
        actual_tool_name = result.tool_calls[0].get('name')
        
        print(f"📋 Testing with actual tool name: '{actual_tool_name}'")
        print(f"   Tool routes: {engine.tool_routes}")
        
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
        
        # Success ToolMessage
        success_tool_message = ToolMessage(
            content='{"success": true, "data": {"answer": "4"}}',
            name=actual_tool_name,
            tool_call_id="call_test123",
            additional_kwargs={
                "is_error": False,
                "validation_passed": True
            }
        )
        
        # Test state
        state = {
            "messages": [ai_message, success_tool_message],
            "tool_routes": engine.tool_routes
        }
        
        # Call router
        router_result = validation_router_v2(state)
        
        print(f"   🎯 Router result: '{router_result}'")
        
        if router_result == "parse_output":
            print(f"   ✅ SUCCESS: Router correctly routes to parse_output!")
            return True
        else:
            print(f"   ❌ FAILED: Router routes to '{router_result}' instead of parse_output")
            return False
        
    except Exception as e:
        print(f"❌ Error testing router: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_simple_agent_no_infinite_loop():
    """Test SimpleAgent to confirm infinite loop is fixed."""
    
    print(f"\n🔍 TESTING SIMPLE AGENT - NO INFINITE LOOP")
    print("=" * 60)
    
    try:
        from haive.core.engine.aug_llm import AugLLMConfig
        from haive.agents.simple.agent import SimpleAgent
        
        # Create agent
        engine = AugLLMConfig(
            structured_output_model=SimpleResult,
            temperature=0.3,
        )
        
        agent = SimpleAgent(
            name="infinite_loop_test",
            engine=engine,
            debug=True
        )
        
        print(f"📋 Agent created:")
        print(f"   Tool routes: {engine.tool_routes}")
        
        # Set up timeout to prevent hanging
        def timeout_handler(signum, frame):
            raise TimeoutError("Agent execution timed out")
        
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(10)  # 10 second timeout
        
        try:
            print(f"   🎯 Executing agent (10 second timeout)...")
            result = agent.run("What is 2+2?", debug=False)
            signal.alarm(0)  # Cancel timeout
            
            print(f"   ✅ SUCCESS: Agent completed without infinite loop!")
            print(f"   Result: {result}")
            return True
            
        except TimeoutError:
            print(f"   ❌ TIMEOUT: Agent still has infinite loop")
            return False
        
    except Exception as e:
        print(f"❌ Error testing agent: {e}")
        return False


def main():
    """Run infinite loop fix tests."""
    
    print("🔬 INFINITE LOOP FIX VERIFICATION")
    print("=" * 80)
    
    # Test 1: Fixed tool routes
    routes_fixed = test_fixed_tool_routes()
    
    # Test 2: Validation router with fix
    router_fixed = test_validation_router_with_fix()
    
    # Test 3: SimpleAgent no infinite loop
    agent_fixed = test_simple_agent_no_infinite_loop()
    
    print(f"\n" + "=" * 80)
    print("🎯 FIX VERIFICATION RESULTS:")
    print(f"   Tool routes fixed: {'✅' if routes_fixed else '❌'}")
    print(f"   Validation router fixed: {'✅' if router_fixed else '❌'}")
    print(f"   SimpleAgent infinite loop fixed: {'✅' if agent_fixed else '❌'}")
    
    if routes_fixed and router_fixed and agent_fixed:
        print(f"\n🎉 ALL TESTS PASSED: Infinite loop fix is working!")
        print(f"\n📋 SUMMARY:")
        print(f"   - StructuredOutputMixin now uses sanitized tool names")
        print(f"   - Tool routes match actual LangChain tool call names")
        print(f"   - validation_router_v2 finds correct routes")
        print(f"   - SimpleAgent completes without infinite loop")
    else:
        print(f"\n❌ SOME TESTS FAILED: Fix needs more work")


if __name__ == "__main__":
    main()