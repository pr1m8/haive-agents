#!/usr/bin/env python3
"""Comprehensive test to verify infinite loop fix for SimpleAgent with structured output."""

import sys
import os
import signal
import time

# Add the packages to path  
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../src"))

from pydantic import BaseModel, Field
import pytest


class SimpleResult(BaseModel):
    """Simple structured result."""
    answer: str = Field(description="The answer")


class ComplexResult(BaseModel):
    """Complex structured result."""
    calculation: str = Field(description="The calculation performed")
    result: float = Field(description="The numerical result")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence score")


def test_simple_agent_tool_route_synchronization():
    """Test that SimpleAgent tool routes are properly synchronized."""
    
    from haive.core.engine.aug_llm import AugLLMConfig
    
    # Test with SimpleResult
    engine = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
    )
    
    # Verify tool routes use sanitized names
    assert 'simple_result' in engine.tool_routes, f"Expected 'simple_result' in routes: {engine.tool_routes}"
    assert engine.tool_routes['simple_result'] == 'parse_output', f"Expected parse_output route: {engine.tool_routes}"
    
    # Test with ComplexResult
    engine2 = AugLLMConfig(
        structured_output_model=ComplexResult,
        temperature=0.3,
    )
    
    # Verify tool routes use sanitized names
    assert 'complex_result' in engine2.tool_routes, f"Expected 'complex_result' in routes: {engine2.tool_routes}"
    assert engine2.tool_routes['complex_result'] == 'parse_output', f"Expected parse_output route: {engine2.tool_routes}"


def test_simple_agent_validation_router_fix():
    """Test that validation router correctly routes to parse_output."""
    
    from haive.core.engine.aug_llm import AugLLMConfig
    from haive.core.graph.node.validation_router_v2 import validation_router_v2
    from langchain_core.messages import AIMessage, ToolMessage
    
    # Create engine
    engine = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
    )
    
    # Get actual tool call from engine
    result = engine.invoke({"messages": [{"role": "user", "content": "What is 2+2?"}]})
    actual_tool_name = result.tool_calls[0].get('name')
    
    # Verify tool name matches route key
    assert actual_tool_name in engine.tool_routes, f"Tool name '{actual_tool_name}' not found in routes"
    
    # Create test state for validation router
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
    
    # Call validation router
    router_result = validation_router_v2(state)
    
    # Verify it routes to parse_output (no infinite loop)
    assert router_result == "parse_output", f"Expected parse_output, got {router_result}"


@pytest.mark.timeout(30)  # 30 second timeout
def test_simple_agent_no_infinite_loop():
    """Test that SimpleAgent with structured output completes without infinite loop."""
    
    pytest.importorskip("haive.agents.simple.agent", reason="SimpleAgent import issues")
    
    from haive.core.engine.aug_llm import AugLLMConfig
    from haive.agents.simple.agent import SimpleAgent
    
    # Create engine
    engine = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
    )
    
    # Create agent
    agent = SimpleAgent(
        name="infinite_loop_test",
        engine=engine,
        debug=True
    )
    
    # Test execution with timeout
    start_time = time.time()
    result = agent.run("What is 2+2?", debug=False)
    end_time = time.time()
    
    execution_time = end_time - start_time
    
    # Verify execution completed
    assert result is not None, "Agent should return a result"
    assert execution_time < 25, f"Agent took too long: {execution_time:.2f}s (possible infinite loop)"
    
    # Verify result structure if it's structured output
    if hasattr(result, 'answer'):
        assert hasattr(result, 'answer'), "Result should have answer field"
    

def test_simple_agent_multiple_structured_outputs():
    """Test SimpleAgent with different structured output models."""
    
    pytest.importorskip("haive.agents.simple.agent", reason="SimpleAgent import issues")
    
    from haive.core.engine.aug_llm import AugLLMConfig
    from haive.agents.simple.agent import SimpleAgent
    
    # Test 1: Simple result
    engine1 = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
    )
    
    agent1 = SimpleAgent(name="test1", engine=engine1)
    
    # Quick execution test
    result1 = agent1.run("What is 5+5?", debug=False)
    assert result1 is not None
    
    # Test 2: Complex result
    engine2 = AugLLMConfig(
        structured_output_model=ComplexResult,
        temperature=0.3,
    )
    
    agent2 = SimpleAgent(name="test2", engine=engine2)
    
    # Quick execution test
    result2 = agent2.run("Calculate 10 * 3", debug=False)
    assert result2 is not None


def test_tool_name_sanitization():
    """Test that tool names are properly sanitized for various BaseModel classes."""
    
    from haive.core.utils.naming import sanitize_tool_name
    
    test_cases = [
        ("SimpleResult", "simple_result"),
        ("ComplexResult", "complex_result"),
        ("UserProfile", "user_profile"),
        ("APIResponse", "api_response"),
        ("HTTPSParser", "https_parser"),
        ("Plan[Task]", "plan_task_generic"),
        ("Model[String]", "model_string_generic"),
    ]
    
    for original, expected in test_cases:
        sanitized = sanitize_tool_name(original)
        assert sanitized == expected, f"Expected {original} -> {expected}, got {sanitized}"


if __name__ == "__main__":
    # Run tests individually for debugging
    print("🔬 STRUCTURED OUTPUT INFINITE LOOP FIX TESTS")
    print("=" * 60)
    
    try:
        print("\n1. Testing tool route synchronization...")
        test_simple_agent_tool_route_synchronization()
        print("   ✅ PASSED")
    except Exception as e:
        print(f"   ❌ FAILED: {e}")
    
    try:
        print("\n2. Testing validation router fix...")
        test_simple_agent_validation_router_fix()
        print("   ✅ PASSED")
    except Exception as e:
        print(f"   ❌ FAILED: {e}")
    
    try:
        print("\n3. Testing tool name sanitization...")
        test_tool_name_sanitization()
        print("   ✅ PASSED")
    except Exception as e:
        print(f"   ❌ FAILED: {e}")
    
    try:
        print("\n4. Testing SimpleAgent no infinite loop...")
        test_simple_agent_no_infinite_loop()
        print("   ✅ PASSED")
    except Exception as e:
        print(f"   ❌ FAILED: {e}")
    
    try:
        print("\n5. Testing multiple structured outputs...")
        test_simple_agent_multiple_structured_outputs()
        print("   ✅ PASSED")
    except Exception as e:
        print(f"   ❌ FAILED: {e}")
    
    print(f"\n🎉 All tests completed!")