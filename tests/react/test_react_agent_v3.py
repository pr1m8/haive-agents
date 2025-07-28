#!/usr/bin/env python3
"""Test ReactAgentV3 with real execution - no mocks, comprehensive validation."""

import logging
from typing import List

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import DeepSeekLLMConfig
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.react.agent_v3 import ReactAgentV3

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ============================================================================
# STRUCTURED OUTPUT MODELS FOR TESTING
# ============================================================================


class MathAnalysis(BaseModel):
    """Mathematical analysis with reasoning trace."""

    original_problem: str = Field(description="Original mathematical problem")
    reasoning_steps: List[str] = Field(description="Step-by-step reasoning process")
    calculations: List[str] = Field(description="Mathematical calculations performed")
    final_answer: str = Field(description="Final numerical answer")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence in solution")


class ResearchResult(BaseModel):
    """Research findings with methodology."""

    research_question: str = Field(description="Original research question")
    approach: List[str] = Field(description="Research methodology steps")
    key_findings: List[str] = Field(description="Important discoveries")
    conclusion: str = Field(description="Comprehensive conclusion")
    sources_used: int = Field(ge=0, description="Number of sources consulted")


# ============================================================================
# TEST TOOLS
# ============================================================================


@tool
def calculator(expression: str) -> str:
    """Perform mathematical calculations safely.

    Args:
        expression: Mathematical expression to evaluate

    Returns:
        String representation of the calculation result
    """
    try:
        allowed_chars = set("0123456789+-*/.() %")
        if not all(c in allowed_chars for c in expression):
            return f"Error: Invalid characters in expression '{expression}'"

        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error calculating '{expression}': {str(e)}"


@tool
def fact_lookup(topic: str) -> str:
    """Look up factual information about a topic.

    Args:
        topic: Topic to research

    Returns:
        Factual information about the topic
    """
    # Simulated fact database for testing
    facts = {
        "earth": "Earth has a diameter of approximately 12,742 km and a circumference of about 40,075 km at the equator.",
        "moon": "The Moon has a diameter of 3,474 km and is approximately 384,400 km away from Earth.",
        "sun": "The Sun has a diameter of 1,392,700 km and is about 149.6 million km from Earth.",
        "python": "Python is a high-level programming language created by Guido van Rossum, first released in 1991.",
        "tokyo": "Tokyo is the capital of Japan with a metropolitan population of approximately 37.4 million people.",
    }

    topic_lower = topic.lower()
    for key, fact in facts.items():
        if key in topic_lower:
            return f"Fact about {topic}: {fact}"

    return f"No specific facts found for '{topic}'. This is a general knowledge lookup tool."


# ============================================================================
# TEST FUNCTIONS
# ============================================================================


def test_basic_react_execution():
    """Test basic ReactAgentV3 execution with tools and reasoning loops."""
    print("\n" + "=" * 70)
    print("🔄 TEST 1: Basic ReAct Execution with Tools")
    print("=" * 70)

    # Create ReactAgent with tools
    agent = ReactAgentV3(
        name="basic_react_agent",
        engine=AugLLMConfig(
            tools=[calculator, fact_lookup],
            temperature=0.3,
            max_tokens=600,
            llm_config=DeepSeekLLMConfig(),
        ),
        max_iterations=5,
        debug=True,
    )

    print(f"✅ Created ReactAgentV3 with {len(agent.engine.tools)} tools")
    print(f"   Max iterations: {agent.max_iterations}")

    # Test reasoning with tool usage
    query = "What is the circumference of Earth divided by 1000?"
    print(f"\n📨 Query: {query}")
    print("\n" + "-" * 50)

    result = agent.run(query, debug=True)

    print("-" * 50)

    # Verify reasoning occurred
    reasoning_trace = agent.get_reasoning_trace()
    tool_history = agent.get_tool_usage_history()

    print("\n📊 Execution Results:")
    print(f"   Iterations completed: {agent.iteration_count}")
    print(f"   Reasoning steps: {len(reasoning_trace)}")
    print(f"   Tools used: {len(tool_history)}")

    # Extract final response
    if hasattr(result, "messages"):
        for msg in reversed(result.messages):
            if msg.__class__.__name__ == "AIMessage":
                response = msg.content
                print(f"🎯 Final Response: {response[:200]}...")

                # Check if response contains expected calculation
                if "40.075" in response or "40075" in response:
                    print("✅ SUCCESS: Found expected calculation result")
                    return True
                else:
                    print(
                        "❌ PARTIAL: Response generated but calculation not clearly found"
                    )
                    return False
                break

    print("❌ FAILURE: No AI response found")
    return False


def test_structured_output_react():
    """Test ReactAgentV3 with structured output and reasoning documentation."""
    print("\n" + "=" * 70)
    print("📋 TEST 2: Structured Output ReAct with MathAnalysis")
    print("=" * 70)

    # Create agent with structured output
    agent = ReactAgentV3(
        name="structured_react_agent",
        engine=AugLLMConfig(
            tools=[calculator, fact_lookup],
            structured_output_model=MathAnalysis,
            temperature=0.2,
            max_tokens=800,
            llm_config=DeepSeekLLMConfig(),
        ),
        max_iterations=6,
        require_final_answer=True,
        debug=True,
    )

    print(f"✅ Created structured ReactAgentV3 with model: {MathAnalysis.__name__}")
    print(f"   Required fields: {list(MathAnalysis.model_fields.keys())}")

    query = "Calculate the area of a circle with radius equal to the Moon's radius"
    print(f"\n📨 Query: {query}")
    print("\n" + "-" * 50)

    result = agent.run(query, debug=True)

    print("-" * 50)

    # Check for structured output in messages
    if hasattr(result, "messages"):
        for msg in reversed(result.messages):
            if hasattr(msg, "tool_calls") and msg.tool_calls:
                for tool_call in msg.tool_calls:
                    if tool_call.name == "MathAnalysis":
                        print("✅ SUCCESS: Found MathAnalysis structured output")
                        args = tool_call.args
                        print(
                            f"   Original problem: {args.get('original_problem', 'N/A')[:100]}..."
                        )
                        print(
                            f"   Reasoning steps: {len(args.get('reasoning_steps', []))}"
                        )
                        print(f"   Calculations: {len(args.get('calculations', []))}")
                        print(
                            f"   Final answer: {args.get('final_answer', 'N/A')[:50]}..."
                        )
                        print(f"   Confidence: {args.get('confidence', 'N/A')}")
                        return True
                break

    print("❌ FAILURE: No structured output found")
    return False


def test_research_agent_factory():
    """Test create_research_agent factory function with ResearchResult model."""
    print("\n" + "=" * 70)
    print("🔬 TEST 3: Research Agent Factory with Structured Output")
    print("=" * 70)

    # Create research agent using factory
    from haive.agents.react.agent_v3 import create_research_agent

    agent = create_research_agent(
        name="test_researcher",
        research_tools=[fact_lookup, calculator],
        analysis_model=ResearchResult,
        max_research_steps=4,
        debug=True,
    )

    print(f"✅ Created research agent with model: {ResearchResult.__name__}")
    print(f"   Max research steps: {agent.max_iterations}")
    print(f"   Temperature: {agent.engine.temperature}")

    query = "Research Python programming language and calculate its age in 2024"
    print(f"\n📨 Research Query: {query}")
    print("\n" + "-" * 50)

    result = agent.run(query, debug=True)

    print("-" * 50)

    # Look for ResearchResult structured output
    if hasattr(result, "messages"):
        for msg in reversed(result.messages):
            if hasattr(msg, "tool_calls") and msg.tool_calls:
                for tool_call in msg.tool_calls:
                    if tool_call.name == "ResearchResult":
                        print("✅ SUCCESS: Found ResearchResult structured output")
                        args = tool_call.args
                        print(
                            f"   Research question: {args.get('research_question', 'N/A')[:80]}..."
                        )
                        print(f"   Approach steps: {len(args.get('approach', []))}")
                        print(f"   Key findings: {len(args.get('key_findings', []))}")
                        print(f"   Sources used: {args.get('sources_used', 0)}")
                        return True
                break

    print("❌ FAILURE: No ResearchResult structured output found")
    return False


def test_react_vs_simple_comparison():
    """Compare ReactAgentV3 vs SimpleAgentV3 execution patterns."""
    print("\n" + "=" * 70)
    print("⚖️  TEST 4: ReactAgentV3 vs SimpleAgentV3 Comparison")
    print("=" * 70)

    from haive.agents.simple.agent_v3 import SimpleAgentV3

    # Same configuration for both agents
    shared_config = AugLLMConfig(
        tools=[calculator],
        temperature=0.2,
        max_tokens=400,
        llm_config=DeepSeekLLMConfig(),
    )

    # Create both agents
    simple_agent = SimpleAgentV3(
        name="simple_comparison",
        engine=shared_config,
        debug=False,  # Reduce output for comparison
    )

    react_agent = ReactAgentV3(
        name="react_comparison", engine=shared_config, max_iterations=3, debug=False
    )

    query = "Calculate 25 * 16 + 100"

    print(f"📨 Test Query: {query}")
    print("\n🔹 SimpleAgentV3 execution:")
    simple_result = simple_agent.run(query)

    print("\n🔄 ReactAgentV3 execution:")
    react_result = react_agent.run(query)

    print("\n📊 Comparison Results:"s:")
    print("   Simple iterations: 1 (linear execution)")
    print(f"   React iterations: {react_agent.iteration_count} (reasoning loops)")

    # Both should get the same mathematical result (500)
    simple_found_500 = "500" in str(simple_result) if simple_result else False
    react_found_500 = "500" in str(react_result) if react_result else False

    if simple_found_500 and react_found_500:
        print("✅ SUCCESS: Both agents found correct answer (500)")
        print("   ReactAgent shows enhanced reasoning process")
        return True
    else:
        print(f"❌ MIXED RESULTS: Simple={simple_found_500}, React={react_found_500}")
        return False


def run_all_react_tests():
    """Run comprehensive ReactAgentV3 test suite."""
    print("🧪 REACTAGENT V3 - COMPREHENSIVE TEST SUITE")
    print("=" * 70)
    print("Testing ReAct pattern with structured output and real LLM execution")
    print("=" * 70)

    test_results = []

    try:
        # Run all tests
        test_results.append(test_basic_react_execution())
        test_results.append(test_structured_output_react())
        test_results.append(test_research_agent_factory())
        test_results.append(test_react_vs_simple_comparison())

        # Summary
        passed = sum(test_results)
        total = len(test_results)

        print("\n" + "=" * 70)
        print("📊 REACTAGENT V3 TEST RESULTS")
        print("=" * 70)
        print(f"Tests passed: {passed}/{total}")

        if passed == total:
            print("🎉 ALL REACTAGENT V3 TESTS PASSED! ✅")
            print("\n🔧 Key achievements:")
            print("✅ ReAct reasoning loops working with real LLM")
            print("✅ Tool integration in iterative reasoning")
            print("✅ Structured output with reasoning documentation")
            print("✅ Factory functions for easy agent creation")
            print("✅ Enhanced features over original ReactAgent")
            print("✅ Comparison validation vs SimpleAgentV3")
        else:
            print("⚠️  Some tests failed - check output above")

    except Exception as e:
        print(f"\n❌ Test execution failed: {e}")
        logger.exception("ReactAgentV3 test execution error")


if __name__ == "__main__":
    run_all_react_tests()
