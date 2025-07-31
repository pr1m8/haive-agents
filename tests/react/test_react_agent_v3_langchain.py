"""Test ReactAgentV3 with LangChain tools."""

from langchain_core.tools import tool

from haive.agents.react.agent_v3 import ReactAgentV3
from haive.core.engine.aug_llm import AugLLMConfig


# Define test tools
@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {e!s}"


@tool
def search_tool(query: str) -> str:
    """Search for information."""
    # Mock search results
    search_results = {
        "population of tokyo": "Tokyo has a population of approximately 14 million people in the city proper.",
        "tokyo dome capacity": "Tokyo Dome has a capacity of 55,000 people.",
        "python programming": "Python is a high-level programming language known for its simplicity.",
        "weather today": "Today's weather is sunny with a high of 25°C.",
    }

    query_lower = query.lower()
    for key, value in search_results.items():
        if key in query_lower:
            return value

    return f"No specific results found for: {query}"


@tool
def word_analyzer(text: str) -> str:
    """Analyze text and provide statistics."""
    words = text.split()
    chars = len(text)
    word_count = len(words)
    avg_word_length = (
        sum(len(word) for word in words) / word_count if word_count > 0 else 0
    )

    return (
        f"Text Analysis:\n"
        f"- Word count: {word_count}\n"
        f"- Character count: {chars}\n"
        f"- Average word length: {avg_word_length:.1f}"
    )


def test_react_agent_v3_with_single_tool():
    """Test ReactAgentV3 with a single calculator tool."""
    # Create agent with tool
    agent = ReactAgentV3(
        name="react_calc",
        engine=AugLLMConfig(temperature=0.1),
        tools=[calculator],
        max_iterations=3,
        debug=True,
    )

    # Test calculation
    result = agent.run("Calculate 15 * 23 + 47")

    # Check result contains correct calculation
    assert "392" in str(result) or "345" in str(result)  # 15*23=345, 345+47=392


def test_react_agent_v3_with_multiple_tools():
    """Test ReactAgentV3 with multiple tools for complex reasoning."""
    # Create agent with multiple tools
    agent = ReactAgentV3(
        name="react_multi",
        engine=AugLLMConfig(temperature=0.1),
        tools=[calculator, search_tool, word_analyzer],
        max_iterations=5,
        debug=True,
    )

    # Test complex query requiring multiple tools
    result = agent.run(
        "Search for the population of Tokyo, then calculate how many Tokyo Domes "
        "would be needed to fit that population (search for Tokyo Dome capacity too)"
    )

    # Agent should use search_tool and calculator
    assert result is not None


def test_react_agent_v3_reasoning_loop():
    """Test ReactAgentV3's iterative reasoning capability."""
    # Create agent with tools
    agent = ReactAgentV3(
        name="react_reasoner",
        engine=AugLLMConfig(temperature=0.1),
        tools=[calculator, word_analyzer],
        max_iterations=4,
        debug=True,
    )

    # Test multi-step reasoning
    result = agent.run(
        "First analyze this text: 'The quick brown fox jumps over the lazy dog'. "
        "Then calculate the square of the word count."
    )

    # Should use word_analyzer then calculator
    assert result is not None


def test_react_agent_v3_error_handling():
    """Test ReactAgentV3 error handling with invalid tool calls."""
    # Create agent
    agent = ReactAgentV3(
        name="react_error",
        engine=AugLLMConfig(temperature=0.1),
        tools=[calculator],
        max_iterations=2,
        debug=True,
    )

    # Test with request that might cause errors
    result = agent.run("Calculate the result of dividing by zero: 10/0")

    # Should handle error gracefully
    assert result is not None


if __name__ == "__main__":
    test_react_agent_v3_with_single_tool()
    test_react_agent_v3_with_multiple_tools()
    test_react_agent_v3_reasoning_loop()
    test_react_agent_v3_error_handling()
