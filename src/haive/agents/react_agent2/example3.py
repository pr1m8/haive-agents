import json
import logging

from langchain_core.tools import Tool
from pydantic import BaseModel, Field

from haive.agents.react_agent2.agent import create_react_agent

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 1. Define some example tools
def get_current_weather(location: str) -> str:
    """Get the current weather in a given location."""
    # In a real implementation, this would call a weather API
    weather_conditions = {
        "san francisco": "sunny and 72°F",
        "new york": "partly cloudy and 65°F",
        "london": "rainy and 55°F",
        "tokyo": "clear and 70°F"
    }
    location = location.lower()
    condition = weather_conditions.get(location, "unknown")
    return f"The weather in {location} is {condition}."

def search_knowledge_base(query: str) -> str:
    """Search a knowledge base for information."""
    # This would typically connect to a real search engine or database
    return f"Here is some information about '{query}': This is a placeholder result for demonstration purposes."

def calculate(expression: str) -> str:
    """Calculate the result of a mathematical expression."""
    try:
        # In production, use a safer evaluation method
        result = eval(expression)
        return f"The result of {expression} is {result}"
    except Exception as e:
        return f"Error calculating {expression}: {e!s}"

def translate_text(text: str, target_language: str) -> str:
    """Translate text to the target language."""
    languages = {
        "spanish": "Hola, ¿cómo estás?",
        "french": "Bonjour, comment ça va?",
        "german": "Hallo, wie geht es dir?",
        "japanese": "こんにちは、お元気ですか？"
    }
    if target_language.lower() in languages:
        return f"Translation to {target_language}: '{languages[target_language.lower()]}'"
    return f"Translation to {target_language} not supported."

# Create tool definitions
tools = [
    Tool.from_function(
        func=get_current_weather,
        name="get_weather",
        description="Get the current weather in a given location"
    ),
    Tool.from_function(
        func=search_knowledge_base,
        name="search",
        description="Search for information about a topic"
    ),
    Tool.from_function(
        func=calculate,
        name="calculator",
        description="Calculate the result of a mathematical expression"
    ),
    Tool.from_function(
        func=translate_text,
        name="translate",
        description="Translate text to another language"
    )
]

# 2. Define a structured output model for travel recommendations
class TravelRecommendation(BaseModel):
    """Travel recommendation with details."""
    destination: str = Field(description="The recommended destination")
    activities: list[str] = Field(description="Suggested activities for the destination")
    weather: str = Field(description="Current weather at the destination")
    budget: float = Field(description="Estimated budget for a 3-day trip in USD")
    best_time_to_visit: str = Field(description="The best time of year to visit")

# 3. Example using the basic React agent
def run_basic_react_agent():
    """Run an example with the basic React agent."""
    print("\n===== BASIC REACT AGENT EXAMPLE =====")

    # Create the agent
    agent = create_react_agent(
        system_prompt="You are a helpful travel assistant that can find information and make recommendations.",
        model="gpt-4o",
        temperature=0.7,
        tools=tools,
        name="travel_assistant",
        structured_output_model=TravelRecommendation,
        max_iterations=5
    )

    # Run the agent with a query
    query = "I want to visit San Francisco this weekend. Can you check the weather, recommend 3 activities, and calculate a budget if I spend $200 per day for 3 days plus $400 for flights?"

    print(f"Query: {query}\n")
    result = agent.run(query)

    # Print messages
    print("--- Conversation ---")
    for msg in result["messages"]:
        if hasattr(msg, "content"):
            print(f"{msg.type.upper()}: {msg.content}")
            # Print tool calls if present
            if hasattr(msg, "tool_calls") and msg.tool_calls:
                print("  Tool Calls:")
                for tool_call in msg.tool_calls:
                    print(f"  - {tool_call['name']}: {json.dumps(tool_call['args'], indent=2)}")

# 4. Example using the react agent with custom tool routing
def run_react_agent_with_routing():
    """Run an example with react agent using custom tool routing."""
    print("\n===== REACT AGENT WITH ROUTING EXAMPLE =====")

    # Define tool routing - different tools go to different nodes
    tool_routing = {
        "get_weather": "weather_node",
        "calculator": "math_node",
        "translate": "language_node"
    }

    # Create the agent
    agent = create_react_agent(
        system_prompt="You are a helpful travel assistant with specialized tools.",
        model="gpt-4o",
        temperature=0.7,
        tools=tools,
        tool_routing=tool_routing,
        name="travel_assistant_specialized",
        max_iterations=5
    )

    # Define post-processing functions that you could add to the agent
    def process_weather_results(state):
        """Process weather results with additional information."""
        state_dict = state.model_dump() if hasattr(state, "model_dump") else state
        # Add seasonal information based on location
        messages = state_dict.get("messages", [])
        for msg in messages:
            if hasattr(msg, "name") and msg.name == "get_weather" and hasattr(msg, "content"):
                content = msg.content
                if "san francisco" in content.lower():
                    state_dict["seasonal_info"] = "San Francisco has mild temperatures year-round."
        return state_dict

    def process_calculation_results(state):
        """Process calculation results with additional context."""
        state_dict = state.model_dump() if hasattr(state, "model_dump") else state
        # Add a running total for budget calculations
        messages = state_dict.get("messages", [])
        for msg in messages:
            if hasattr(msg, "name") and msg.name == "calculator" and hasattr(msg, "content"):
                content = msg.content
                if "result" in content:
                    try:
                        # Extract the result value
                        import re
                        match = re.search(r"result of .* is ([0-9.]+)", content)
                        if match:
                            value = float(match.group(1))
                            state_dict["last_calculation"] = value
                    except:
                        pass
        return state_dict

    # Initialize state with a query
    query = "I want to plan a trip to San Francisco. Can you check the weather, suggest some activities, calculate a budget for 3 days if I spend $200 per day plus $400 for flights, and translate 'Hello, how are you?' to Spanish?"

    # Run the agent
    print(f"Query: {query}\n")
    result = agent.run(query)

    # Print messages
    print("--- Conversation ---")
    for msg in result["messages"]:

        if hasattr(msg, "content"):
            print(f"{msg.type.upper()}: {msg.content}")
            # Print tool calls if present
            if hasattr(msg, "tool_calls") and msg.tool_calls:
                print("  Tool Calls:")
                for tool_call in msg.tool_calls:
                    print(f"  - {tool_call['name']}: {json.dumps(tool_call['args'], indent=2)}")

# 5. Example showing how to add post-processing after creating the agent
def run_react_agent_with_post_processing():
    """Run an example with post-processing added after agent creation."""
    print("\n===== REACT AGENT WITH POST-PROCESSING EXAMPLE =====")

    # Create the basic agent
    agent = create_react_agent(
        system_prompt="You are a helpful travel assistant that can find information and make recommendations.",
        model="gpt-4o",
        temperature=0.7,
        tools=tools,
        name="travel_assistant_with_processing"
    )

    # Define a simple post-processor for the agent
    def track_tool_usage(state):
        """Track and analyze tool usage patterns."""
        state_dict = state.model_dump() if hasattr(state, "model_dump") else state

        # Make sure we have a stats dictionary
        if "tool_usage_stats" not in state_dict:
            state_dict["tool_usage_stats"] = {}

        # Extract the last message with tool calls
        messages = state_dict.get("messages", [])
        for msg in reversed(messages):
            tool_calls = []

            # Try to extract tool calls from the message
            if hasattr(msg, "tool_calls") and msg.tool_calls:
                tool_calls = msg.tool_calls
            elif hasattr(msg, "additional_kwargs") and "tool_calls" in msg.additional_kwargs:
                tool_calls = msg.additional_kwargs.get("tool_calls", [])

            # Update stats for each tool call
            for tool_call in tool_calls:
                tool_name = tool_call.get("name", "unknown")
                stats = state_dict["tool_usage_stats"]
                stats[tool_name] = stats.get(tool_name, 0) + 1

            # Stop after processing one message with tool calls
            if tool_calls:
                break

        return state_dict

    # Run the agent with a query
    query = "I want to plan a trip to San Francisco. Calculate the budget for 3 days at $200 per day plus $400 for flights, check the weather, and translate 'Hello' to Spanish."

    print(f"Query: {query}\n")

    # Run the agent and apply post-processing to the result
    result = agent.run(query)
    processed_result = track_tool_usage(result)

    # Print messages
    print("--- Conversation ---")
    for msg in processed_result["messages"]:
        if hasattr(msg, "content"):
            print(f"{msg.type.upper()}: {msg.content}")
            # Print tool calls if present
            if hasattr(msg, "tool_calls") and msg.tool_calls:
                print("  Tool Calls:")
                for tool_call in msg.tool_calls:
                    print(f"  - {tool_call['name']}: {json.dumps(tool_call['args'], indent=2)}")

    # Print tool usage statistics
    if "tool_usage_stats" in processed_result:
        print("\n--- Tool Usage Statistics ---")
        for tool, count in processed_result["tool_usage_stats"].items():
            print(f"{tool}: {count} calls")

# Run the examples
if __name__ == "__main__":
    run_basic_react_agent()
    run_react_agent_with_routing()
    run_react_agent_with_post_processing()
