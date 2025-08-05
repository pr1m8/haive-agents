#!/usr/bin/env python3

from langchain_core.tools import tool

from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.core.engine.aug_llm import AugLLMConfig


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
    return f"Text analysis: {len(words)} words, {chars} characters, {sentences} sentences"


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
    return f"Weather data not available for {city}"


def test_simple_agent_v3_with_tools():
    """Test SimpleAgentV3 with LangChain tools."""
    # Create agent with tools
    agent = SimpleAgentV3(
        name="tool_agent",
        engine=AugLLMConfig(temperature=0.1, tools=[calculator, text_analyzer, weather_info]),
    )

    # Test 1: Calculator tool
    agent.run("What is 25 * 34 + 100?", debug=True)

    # Test 2: Text analyzer tool
    agent.run("Analyze this text: 'Hello world! This is a test. How are you?'", debug=True)

    # Test 3: Weather tool
    agent.run("What's the weather like in Paris?", debug=True)

    # Test 4: Multiple tools in sequence
    agent.run(
        "Calculate 15 * 8, then analyze the text 'The result is interesting!' and tell me about weather in Tokyo",
        debug=True,
    )

    # Don't return in pytest tests


if __name__ == "__main__":
    test_agent = test_simple_agent_v3_with_tools()
