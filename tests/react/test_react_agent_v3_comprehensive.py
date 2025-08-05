#!/usr/bin/env python3
"""Comprehensive tests for ReactAgentV3 with tool loops and structured output."""

from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.react.agent_v3 import ReactAgentV3
from haive.core.engine.aug_llm import AugLLMConfig


# LangChain tools for testing
@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    try:
        result = eval(expression)
        return f"The result of {expression} is {result}"
    except Exception as e:
        return f"Error calculating {expression}: {e}"


@tool
def memory_store(key: str, value: str) -> str:
    """Store a value in memory with a key."""
    if not hasattr(memory_store, "memory"):
        memory_store.memory = {}
    memory_store.memory[key] = value
    return f"Stored '{value}' with key '{key}'"


@tool
def memory_recall(key: str) -> str:
    """Recall a value from memory using a key."""
    if not hasattr(memory_store, "memory"):
        memory_store.memory = {}
    value = memory_store.memory.get(key, "Not found")
    return f"Retrieved: {value}"


@tool
def text_analyzer(text: str) -> str:
    """Analyze text and provide statistics."""
    words = text.split()
    chars = len(text)
    sentences = text.count(".") + text.count("!") + text.count("?")
    return f"Analysis: {len(words)} words, {chars} characters, {sentences} sentences"


# Structured output model for complex reasoning
class ReasoningAnalysis(BaseModel):
    """Structured output for multi-step reasoning."""

    original_question: str = Field(description="The original question asked")
    reasoning_steps: list[str] = Field(description="Step-by-step reasoning process")
    tools_used: list[str] = Field(description="Tools used during reasoning")
    intermediate_results: list[str] = Field(description="Results from each tool usage")
    final_answer: str = Field(description="Final comprehensive answer")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence in the answer")


def test_react_agent_v3_basic_tool_loop():
    """Test ReactAgentV3 basic tool loop functionality with LangChain tools only."""
    # Create ReactAgent with simple LangChain tools - no structured output for now
    agent = ReactAgentV3(
        name="react_calculator",
        engine=AugLLMConfig(
            temperature=0.1,
            tools=[calculator, memory_store, memory_recall],  # Multiple tools for ReAct
            max_tokens=800,
        ),
        max_iterations=5,
        debug=True,
    )

    # Test that should require tool usage and iteration
    agent.run(
        "First calculate 15 * 23, store the result with key 'first_calc', then recall it and multiply by 2."
    )

    # Debug the ReactAgent behavior

    if agent.reasoning_trace:
        for _i, _step in enumerate(agent.reasoning_trace):
            pass

    if agent.tool_results_history:
        for _i, _tool_use in enumerate(agent.tool_results_history):
            pass

    # Don't return in pytest tests


def test_react_agent_v3_memory_workflow():
    """Test ReactAgentV3 with memory tools that require sequencing."""
    # Reset memory between tests
    if hasattr(memory_store, "memory"):
        memory_store.memory.clear()

    agent = ReactAgentV3(
        name="react_memory",
        engine=AugLLMConfig(
            temperature=0.1,
            tools=[memory_store, memory_recall, calculator],
            max_tokens=1000,
        ),
        max_iterations=8,
        debug=True,
    )

    # Test complex workflow requiring memory and calculation
    agent.run(
        "Store the number 42 with key 'answer', then store 58 with key 'question'. "
        "Then recall both values and calculate their sum and product."
    )

    # Verify memory was used correctly
    assert "answer" in memory_store.memory
    assert "question" in memory_store.memory
    assert memory_store.memory["answer"] == "42"
    assert memory_store.memory["question"] == "58"

    # Don't return in pytest tests


def test_react_agent_v3_structured_output():
    """Test ReactAgentV3 with structured output after tool loops."""
    agent = ReactAgentV3(
        name="react_structured",
        engine=AugLLMConfig(
            temperature=0.1,
            tools=[calculator, text_analyzer],
            structured_output_model=ReasoningAnalysis,
            structured_output_version="v2",
            max_tokens=1200,
        ),
        max_iterations=6,
        debug=True,
    )

    # Test complex reasoning that requires multiple tools and structured output
    result = agent.run(
        "Calculate the area of a circle with radius 7, then analyze the text 'The area is important for geometry.' "
        "Provide a complete reasoning analysis."
    )

    # Check if result is structured
    if hasattr(result, "get_latest_structured_output"):
        structured_output = result.get_latest_structured_output()

        if structured_output and hasattr(structured_output, "model_dump"):
            # Verify structured output contains expected data
            assert "circle" in structured_output.original_question.lower()
            assert len(structured_output.tools_used) > 0
            assert len(structured_output.reasoning_steps) > 1
            assert 0 <= structured_output.confidence <= 1

            return structured_output

    return result


def test_react_agent_v3_iteration_limits():
    """Test ReactAgentV3 respects iteration limits."""
    agent = ReactAgentV3(
        name="react_limited",
        engine=AugLLMConfig(
            temperature=0.1,
            tools=[calculator, memory_store, memory_recall],
            max_tokens=600,
        ),
        max_iterations=3,  # Very low limit
        debug=True,
    )

    # Test that agent respects iteration limits
    agent.run(
        "Perform a very complex calculation that might take many steps: "
        "calculate 2^10, store it, then calculate 3^5, store it, then multiply them, "
        "then calculate the square root, then store the final result."
    )

    # Verify iteration limit was respected
    assert agent.iteration_count <= agent.max_iterations, "Should not exceed max iterations"

    # Don't return in pytest tests


def test_react_agent_v3_vs_simple_agent():
    """Compare ReactAgentV3 vs SimpleAgentV3 behavior."""
    from haive.agents.simple.agent_v3 import SimpleAgentV3

    # Simple agent (should use tools once)
    simple_agent = SimpleAgentV3(
        name="simple_calc",
        engine=AugLLMConfig(temperature=0.1, tools=[calculator], max_tokens=600),
    )

    # React agent (should use tools iteratively)
    react_agent = ReactAgentV3(
        name="react_calc",
        engine=AugLLMConfig(temperature=0.1, tools=[calculator], max_tokens=600),
        max_iterations=5,
        debug=True,
    )

    question = "Calculate 10 * 5, then subtract 20, then multiply by 3"

    simple_result = simple_agent.run(question)

    react_result = react_agent.run(question)

    # ReactAgent should use multiple iterations for multi-step problems
    assert react_agent.iteration_count > 1, "ReactAgent should use multiple iterations"

    return simple_result, react_result


def run_all_tests():
    """Run all ReactAgentV3 tests."""
    try:
        # Test 1: Basic tool loop
        test_react_agent_v3_basic_tool_loop()

        # Test 2: Memory workflow
        test_react_agent_v3_memory_workflow()

        # Test 3: Structured output
        test_react_agent_v3_structured_output()

        # Test 4: Iteration limits
        test_react_agent_v3_iteration_limits()

        # Test 5: Comparison with SimpleAgent
        test_react_agent_v3_vs_simple_agent()

    except Exception:
        raise


if __name__ == "__main__":
    # Run just one test first to debug
    test_react_agent_v3_basic_tool_loop()
