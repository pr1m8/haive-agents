#!/usr/bin/env python3
"""Standalone test for infinite loop fix - no pytest needed."""

import asyncio
import time
from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.node.validation_router_v2 import validation_router_v2
from langchain_core.messages import AIMessage, ToolMessage
from pydantic import BaseModel, Field

from haive.agents.simple.agent import SimpleAgent


class SimpleResult(BaseModel):
    """Simple structured result."""

    answer: str = Field(description="The answer")
    confidence: float = Field(default=1.0, ge=0.0, le=1.0)


def test_tool_routes_are_correct():
    """Test that tool routes are set correctly for structured output."""
    print("\n🔍 Test 1: Tool Routes Configuration")
    print("=" * 60)

    # Create engine with V2 structured output
    engine = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
        structured_output_version="v2",
    )

    # Check tool routes
    print(f"Tool routes: {engine.tool_routes}")
    assert "simple_result" in engine.tool_routes, "simple_result not in tool_routes"
    assert (
        engine.tool_routes["simple_result"] == "parse_output"
    ), f"Route is {engine.tool_routes['simple_result']}, not parse_output"

    # Structured output model should be in tools
    assert SimpleResult in engine.tools, "SimpleResult not in tools"

    print("✅ PASS: Tool routes are correctly configured")


def test_validation_router_with_parse_output():
    """Test that validation router correctly handles parse_output route."""
    print("\n🔍 Test 2: Validation Router")
    print("=" * 60)

    # Create engine
    engine = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
    )

    # Simulate LLM response
    messages = [{"role": "user", "content": "What is 2+2?"}]
    llm_result = engine.invoke({"messages": messages})

    assert hasattr(llm_result, "tool_calls"), "No tool_calls in result"
    assert len(llm_result.tool_calls) > 0, "Empty tool_calls"

    tool_call = llm_result.tool_calls[0]
    tool_name = tool_call.get("name")

    print(f"Tool name from LLM: '{tool_name}'")

    # Tool name should be sanitized
    assert (
        tool_name == "simple_result"
    ), f"Tool name is '{tool_name}', not 'simple_result'"

    # Create AIMessage with tool call
    ai_message = AIMessage(content="", tool_calls=[tool_call])

    # Create success ToolMessage (what ValidationNodeV2 would create)
    tool_message = ToolMessage(
        content='{"success": true, "data": {"answer": "4", "confidence": 1.0}}',
        name=tool_name,
        tool_call_id=tool_call.get("id"),
        additional_kwargs={"is_error": False, "validation_passed": True},
    )

    # Test router
    state = {"messages": [ai_message, tool_message], "tool_routes": engine.tool_routes}

    router_result = validation_router_v2(state)

    print(f"Router result: '{router_result}'")

    # Router should return parse_output, not agent_node (which would cause loop)
    assert (
        router_result == "parse_output"
    ), f"Router returned '{router_result}' instead of 'parse_output'"

    print("✅ PASS: Router correctly returns 'parse_output'")


async def test_simple_agent_no_infinite_loop():
    """Test SimpleAgent with structured output - should not infinite loop."""
    print("\n🔍 Test 3: SimpleAgent Execution (No Infinite Loop)")
    print("=" * 60)

    # Create engine with structured output
    engine = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
        structured_output_version="v2",  # Use tool-based approach
    )

    # Create agent
    agent = SimpleAgent(
        name="test_agent",
        engine=engine,
    )

    print("Testing agent execution with 10 second timeout...")

    # Test execution with timeout
    start_time = time.time()

    try:
        # Use asyncio timeout - 10 seconds should be plenty
        result = await asyncio.wait_for(
            agent.arun("What is 2+2? Be confident."), timeout=10.0
        )

        end_time = time.time()
        execution_time = end_time - start_time

        print(f"Execution completed in {execution_time:.2f}s")
        print(f"Result type: {type(result)}")
        print(f"Result: {result}")

        # Should complete quickly, not timeout
        assert execution_time < 10.0, f"Execution took too long: {execution_time}s"

        # Check result
        assert result is not None

        print("✅ PASS: Agent executed without infinite loop")

    except asyncio.TimeoutError:
        print("❌ FAIL: Agent execution timed out - infinite loop still exists!")
        raise


async def main():
    """Run all tests."""
    print("🎉 INFINITE LOOP FIX VERIFICATION")
    print("=" * 80)

    try:
        # Test 1: Tool routes
        test_tool_routes_are_correct()

        # Test 2: Validation router
        test_validation_router_with_parse_output()

        # Test 3: SimpleAgent execution
        await test_simple_agent_no_infinite_loop()

        print("\n" + "=" * 80)
        print("🎉 ALL TESTS PASSED - INFINITE LOOP IS FIXED!")
        print("\nWhat was fixed:")
        print("  1. Tool routes now use 'parse_output' for structured output models")
        print("  2. Validation router correctly routes to parse_output node")
        print("  3. No more infinite loop between agent_node and validation")

    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        import traceback

        traceback.print_exc()
        raise


if __name__ == "__main__":
    # Enable some debug logging
    import logging

    logging.basicConfig(level=logging.WARNING)

    # Run tests
    asyncio.run(main())
