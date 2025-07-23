#!/usr/bin/env python3

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.simple.agent_v3 import SimpleAgentV3


# Create LangChain tools
@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    try:
        result = eval(expression)
        return f"The result of {expression} is {result}"
    except Exception as e:
        return f"Error calculating {expression}: {e}"


@tool
def text_analyzer(text: str) -> str:
    """Analyze text and provide statistics."""
    words = text.split()
    chars = len(text)
    sentences = text.count(".") + text.count("!") + text.count("?")
    return (
        f"Text analysis: {len(words)} words, {chars} characters, {sentences} sentences"
    )


@tool
def weather_info(city: str) -> str:
    """Get weather information for a city."""
    # Mock weather data
    weather_data = {
        "paris": "Sunny, 22°C",
        "london": "Cloudy, 18°C",
        "new york": "Rainy, 15°C",
        "tokyo": "Clear, 25°C",
    }
    city_lower = city.lower()
    if city_lower in weather_data:
        return f"Weather in {city}: {weather_data[city_lower]}"
    else:
        return f"Weather data not available for {city}"


def test_simple_agent_v3_with_tools():
    """Test SimpleAgentV3 with LangChain tools."""

    # Create agent with tools
    agent = SimpleAgentV3(
        name="tool_agent",
        engine=AugLLMConfig(
            temperature=0.1, tools=[calculator, text_analyzer, weather_info]
        ),
    )

    print("=" * 80)
    print("TESTING SimpleAgentV3 with LangChain Tools")
    print("=" * 80)

    # Test 1: Calculator tool
    print("\nTest 1: Calculator")
    print("-" * 40)
    result1 = agent.run("What is 25 * 34 + 100?", debug=True)
    print(f"Result type: {type(result1)}")
    print(f"Result: {result1}")

    # Test 2: Text analyzer tool
    print("\nTest 2: Text Analyzer")
    print("-" * 40)
    result2 = agent.run(
        "Analyze this text: 'Hello world! This is a test. How are you?'", debug=True
    )
    print(f"Result type: {type(result2)}")
    print(f"Result: {result2}")

    # Test 3: Weather tool
    print("\nTest 3: Weather Info")
    print("-" * 40)
    result3 = agent.run("What's the weather like in Paris?", debug=True)
    print(f"Result type: {type(result3)}")
    print(f"Result: {result3}")

    # Test 4: Multiple tools in sequence
    print("\nTest 4: Multiple Tools")
    print("-" * 40)
    result4 = agent.run(
        "Calculate 15 * 8, then analyze the text 'The result is interesting!' and tell me about weather in Tokyo",
        debug=True,
    )
    print(f"Result type: {type(result4)}")
    print(f"Result: {result4}")

    return agent


if __name__ == "__main__":
    test_agent = test_simple_agent_v3_with_tools()
    print("\n" + "=" * 80)
    print("SimpleAgentV3 LangChain Tools Test Complete!")
    print("=" * 80)
