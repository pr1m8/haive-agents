#!/usr/bin/env python3
"""Test that the infinite loop is fixed with SimpleAgent."""

import asyncio
import time
from typing import Any

import pytest
from langchain_core.messages import AIMessage, ToolMessage
from pydantic import BaseModel, Field

from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.node.validation_router_v2 import validation_router_v2


class SimpleResult(BaseModel):
    """Simple structured result."""
    answer: str = Field(description="The answer")
    confidence: float = Field(default=1.0, ge=0.0, le=1.0)


@pytest.mark.asyncio
async def test_simple_agent_no_infinite_loop():
    """Test SimpleAgent with structured output - should not infinite loop."""
    # Create engine with structured output
    engine = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
        structured_output_version="v2",  # Use tool-based approach
    )
    
    # Verify tool routes are correct
    assert 'simple_result' in engine.tool_routes
    assert engine.tool_routes['simple_result'] == 'parse_output'
    
    # Create agent
    agent = SimpleAgent(
        name="test_agent",
        engine=engine,
    )
    
    # Test execution with timeout
    start_time = time.time()
    
    try:
        # Use asyncio timeout - 10 seconds should be plenty
        result = await asyncio.wait_for(
            agent.arun("What is 2+2? Be confident."),
            timeout=10.0
        )
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        # Should complete quickly, not timeout
        assert execution_time < 10.0, f"Execution took too long: {execution_time}s"
        
        # Check result
        assert result is not None
        
        # Result should be a SimpleResult or dict with the right fields
        if isinstance(result, SimpleResult):
            assert hasattr(result, 'answer')
            assert hasattr(result, 'confidence')
        elif isinstance(result, dict):
            assert 'answer' in result
            
    except asyncio.TimeoutError:
        pytest.fail("Agent execution timed out - infinite loop still exists!")


def test_validation_router_with_parse_output():
    """Test that validation router correctly handles parse_output route."""
    # Create engine
    engine = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
    )
    
    # Simulate LLM response
    messages = [{"role": "user", "content": "What is 2+2?"}]
    llm_result = engine.invoke({"messages": messages})
    
    assert hasattr(llm_result, 'tool_calls')
    assert len(llm_result.tool_calls) > 0
    
    tool_call = llm_result.tool_calls[0]
    tool_name = tool_call.get('name')
    
    # Tool name should be sanitized
    assert tool_name == 'simple_result'
    
    # Create AIMessage with tool call
    ai_message = AIMessage(
        content="",
        tool_calls=[tool_call]
    )
    
    # Create success ToolMessage (what ValidationNodeV2 would create)
    tool_message = ToolMessage(
        content='{"success": true, "data": {"answer": "4", "confidence": 1.0}}',
        name=tool_name,
        tool_call_id=tool_call.get('id'),
        additional_kwargs={
            "is_error": False,
            "validation_passed": True
        }
    )
    
    # Test router
    state = {
        "messages": [ai_message, tool_message],
        "tool_routes": engine.tool_routes
    }
    
    router_result = validation_router_v2(state)
    
    # Router should return parse_output, not agent_node (which would cause loop)
    assert router_result == "parse_output", f"Router returned '{router_result}' instead of 'parse_output'"


def test_tool_routes_are_correct():
    """Test that tool routes are set correctly for structured output."""
    # Create engine with V2 structured output
    engine = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
        structured_output_version="v2",
    )
    
    # Check tool routes
    assert 'simple_result' in engine.tool_routes
    assert engine.tool_routes['simple_result'] == 'parse_output'
    
    # Structured output model should be in tools
    assert SimpleResult in engine.tools
    
    # Force tool choice should be set
    assert engine.force_tool_choice == 'SimpleResult' or engine.force_tool_choice == 'simple_result'


def test_analyze_tool_returns_parse_output():
    """Test that _analyze_tool returns parse_output for structured output models."""
    engine = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
    )
    
    # Call _analyze_tool directly
    route, metadata = engine._analyze_tool(SimpleResult)
    
    # Should return parse_output route
    assert route == 'parse_output'
    assert metadata['purpose'] == 'structured_output'
    assert 'implementation' in metadata  # Should track V1 vs V2