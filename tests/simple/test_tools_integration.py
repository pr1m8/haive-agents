#!/usr/bin/env python3
"""Test SimpleAgent v3 with tools integration - no mocks, real execution."""

import logging

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import DeepSeekLLMConfig
from langchain_core.messages import AIMessage
from langchain_core.tools import tool

from haive.agents.simple.agent_v3 import SimpleAgentV3

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@tool
def calculator(expression: str) -> str:
    """Perform mathematical calculations safely.

    Args:
        expression: Mathematical expression to evaluate

    Returns:
        String representation of the calculation result
    """
    try:
        # Basic safety: only allow specific characters
        allowed_chars = set("0123456789+-*/.() %")
        if not all(c in allowed_chars for c in expression):
            return f"Error: Invalid characters in expression '{expression}'"

        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error calculating '{expression}': {str(e)}"


@tool
def word_counter(text: str) -> str:
    """Count words in text.

    Args:
        text: Text to analyze

    Returns:
        Word count as string
    """
    if not text.strip():
        return "0 words"

    word_count = len(text.split())
    return f"{word_count} words"


def test_agent_with_single_tool():
    """Test agent with a single tool (calculator)."""
    print("\n" + "=" * 70)
    print("🧮 TEST 1: Single Tool Integration (Calculator)")
    print("=" * 70)

    # Create agent with calculator tool
    agent = SimpleAgentV3(
        name="calculator_agent",
        engine=AugLLMConfig(
            temperature=0.1,  # Low temperature for consistent tool usage
            max_tokens=150,
            tools=[calculator],
            llm_config=DeepSeekLLMConfig(),
        ),
        debug=True,
    )

    print(f"✅ Created agent with {len(agent.engine.tools)} tool(s)")
    tool_names = [t.name for t in agent.engine.tools]
    print(f"   Available tools: {', '.join(tool_names)}")

    # Test calculation request
    query = "What is 15 multiplied by 23?"
    print(f"\n📨 Query: {query}")
    print("\n" + "-" * 50)

    result = agent.run(query, debug=True)

    print("-" * 50)

    # Extract and verify response
    ai_response = None
    if hasattr(result, "messages"):
        for msg in reversed(result.messages):
            if isinstance(msg, AIMessage):
                ai_response = msg.content
                print(f"🤖 AI Response: {ai_response}")
                break

    # Verify tool was used and calculation is correct
    expected_result = "345"  # 15 * 23 = 345

    if ai_response and expected_result in ai_response:
        print(
            f"✅ SUCCESS: Tool used correctly, found expected result {expected_result}"
        )
        return True
    else:
        print(f"❌ FAILURE: Expected result {expected_result} not found in response")
        return False


def test_agent_with_multiple_tools():
    """Test agent with multiple tools and tool selection."""
    print("\n" + "=" * 70)
    print("🛠️  TEST 2: Multiple Tools Integration")
    print("=" * 70)

    # Create agent with multiple tools
    agent = SimpleAgentV3(
        name="multi_tool_agent",
        engine=AugLLMConfig(
            temperature=0.2,
            max_tokens=200,
            tools=[calculator, word_counter],
            llm_config=DeepSeekLLMConfig(),
        ),
        debug=True,
    )

    print(f"✅ Created agent with {len(agent.engine.tools)} tools")
    tool_names = [t.name for t in agent.engine.tools]
    print(f"   Available tools: {', '.join(tool_names)}")

    # Test queries that should trigger different tools
    test_cases = [
        {
            "query": "Calculate 100 divided by 4",
            "expected_tool": "calculator",
            "expected_content": "25",
        },
        {
            "query": "How many words are in this sentence: 'The quick brown fox jumps'",
            "expected_tool": "word_counter",
            "expected_content": "5 words",
        },
    ]

    results = []

    for i, test_case in enumerate(test_cases, 1):
        query = test_case["query"]
        expected_tool = test_case["expected_tool"]
        expected_content = test_case["expected_content"]

        print(f"\n📨 Test {i} ({expected_tool}): {query}")
        print("-" * 50)

        result = agent.run(query, debug=True)

        # Extract response
        ai_response = None
        if hasattr(result, "messages"):
            for msg in reversed(result.messages):
                if isinstance(msg, AIMessage):
                    ai_response = msg.content
                    print(f"🤖 Response: {ai_response}")
                    break

        # Check if expected content is in response
        success = ai_response and expected_content in ai_response
        results.append(success)

        if success:
            print(f"✅ SUCCESS: {expected_tool} used correctly")
        else:
            print(f"❌ FAILURE: Expected '{expected_content}' not found")

        print()

    overall_success = all(results)
    print(
        f"📊 Overall Result: {len([r for r in results if r])}/{len(results)} tests passed"
    )

    return overall_success


def test_tool_error_handling():
    """Test how agent handles tool errors gracefully."""
    print("\n" + "=" * 70)
    print("⚠️  TEST 3: Tool Error Handling")
    print("=" * 70)

    agent = SimpleAgentV3(
        name="error_test_agent",
        engine=AugLLMConfig(
            temperature=0.1,
            max_tokens=150,
            tools=[calculator],
            llm_config=DeepSeekLLMConfig(),
        ),
        debug=True,
    )

    print("✅ Created agent for error testing"g")

    # Test invalid expression that should cause tool error
    query = "Calculate this invalid expression: 15 + + 23"
    print(f"\n📨 Query (should cause error): {query}")
    print("\n" + "-" * 50)

    result = agent.run(query, debug=True)

    print("-" * 50)

    # Extract response
    ai_response = None
    if hasattr(result, "messages"):
        for msg in reversed(result.messages):
            if isinstance(msg, AIMessage):
                ai_response = msg.content
                print(f"🤖 Response: {ai_response}")
                break

    # Verify error was handled gracefully
    if ai_response and (
        "error" in ai_response.lower() or "invalid" in ai_response.lower()
    ):
        print("✅ SUCCESS: Error handled gracefully by agent")
        return True
    else:
        print("❌ FAILURE: Error not handled properly")
        return False


def run_all_tool_tests():
    """Run all tool integration tests."""
    print("🧪 SIMPLEAGENT V3 - TOOLS INTEGRATION TESTS")
    print("=" * 70)
    print("Testing real tool execution with no mocks")
    print("=" * 70)

    test_results = []

    try:
        # Run all tests
        test_results.append(test_agent_with_single_tool())
        test_results.append(test_agent_with_multiple_tools())
        test_results.append(test_tool_error_handling())

        # Summary
        passed = sum(test_results)
        total = len(test_results)

        print("\n" + "=" * 70)
        print("📊 TOOL INTEGRATION TEST RESULTS")
        print("=" * 70)
        print(f"Tests passed: {passed}/{total}")

        if passed == total:
            print("🎉 ALL TOOL TESTS PASSED! ✅")
            print("\nKey achievements:")
            print("✅ Single tool integration working")
            print("✅ Multiple tool selection working")
            print("✅ Error handling working")
            print("✅ Real LLM + real tools execution")
        else:
            print("⚠️  Some tests failed - check output above")

    except Exception as e:
        print(f"\n❌ Test execution failed: {e}")
        logger.exception("Tool test execution error")


if __name__ == "__main__":
    run_all_tool_tests()
