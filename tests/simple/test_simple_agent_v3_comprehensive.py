"""Comprehensive test for SimpleAgentV3 with various tools and structured output."""

from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.core.engine.aug_llm import AugLLMConfig


# Define structured output models
class ProductInfo(BaseModel):
    """Product information model."""

    name: str = Field(description="Product name")
    price: float = Field(description="Product price")
    quantity: int = Field(description="Quantity in stock")
    total_value: float = Field(description="Total inventory value")


class AnalysisResult(BaseModel):
    """Analysis result with multiple fields."""

    summary: str = Field(description="Brief summary")
    key_points: list[str] = Field(description="Key points from analysis")
    confidence_score: float = Field(ge=0.0, le=1.0, description="Confidence score")
    recommendations: list[str] = Field(description="Recommendations")


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
def inventory_lookup(product_name: str) -> str:
    """Look up product inventory information."""
    # Simulated inventory data
    inventory = {
        "laptop": {"price": 999.99, "quantity": 15},
        "mouse": {"price": 29.99, "quantity": 50},
        "keyboard": {"price": 79.99, "quantity": 30},
        "monitor": {"price": 299.99, "quantity": 20},
    }

    product = product_name.lower()
    if product in inventory:
        info = inventory[product]
        return f"Product: {product_name}, Price: ${info['price']}, Quantity: {info['quantity']}"
    return f"Product '{product_name}' not found in inventory"


@tool
def text_analyzer(text: str) -> str:
    """Analyze text and provide statistics."""
    words = text.split()
    chars = len(text)
    sentences = text.count(".") + text.count("!") + text.count("?")
    return f"Words: {len(words)}, Characters: {chars}, Sentences: {sentences}"


@tool
def data_processor(data: str, operation: str = "summarize") -> str:
    """Process data with various operations."""
    if operation == "summarize":
        return f"Summary of data: {data[:50]}..."
    if operation == "count":
        return f"Data length: {len(data)} characters"
    if operation == "reverse":
        return f"Reversed: {data[::-1]}"
    return f"Unknown operation: {operation}"


def test_simple_agent_v3_with_multiple_tools():
    """Test SimpleAgentV3 with multiple different tools."""
    # Create agent with multiple tools
    agent = SimpleAgentV3(
        name="multi_tool_agent",
        engine=AugLLMConfig(temperature=0.1),
        tools=[calculator, inventory_lookup, text_analyzer, data_processor],
        debug=True,
    )

    # Test 1: Calculator
    agent.run("Calculate (150 * 4) + 200")

    # Test 2: Inventory lookup
    agent.run("Look up the price and quantity of laptop in inventory")

    # Test 3: Text analysis
    agent.run(
        "Analyze this text: 'The quick brown fox jumps over the lazy dog. It's a beautiful day!'"
    )

    # Test 4: Data processing
    agent.run("Process this data 'Hello World' by reversing it")

    # Test 5: Multiple tools in sequence
    agent.run(
        "First calculate 30 * 20, then look up laptop inventory, "
        "and finally analyze the text 'Great products at great prices!'"
    )


def test_simple_agent_v3_with_structured_output():
    """Test SimpleAgentV3 with structured output models."""
    # Test 1: Product Info structured output

    agent1 = SimpleAgentV3(
        name="product_agent",
        engine=AugLLMConfig(temperature=0.1, structured_output_model=ProductInfo),
        tools=[inventory_lookup, calculator],
        debug=True,
    )

    agent1.run(
        "Look up laptop inventory and calculate total value (price * quantity). "
        "Return as ProductInfo with name='Laptop'"
    )

    # Test 2: Analysis Result structured output

    agent2 = SimpleAgentV3(
        name="analysis_agent",
        engine=AugLLMConfig(temperature=0.1, structured_output_model=AnalysisResult),
        tools=[text_analyzer, data_processor],
        debug=True,
    )

    agent2.run(
        "Analyze the following business scenario: 'Our company sells laptops and accessories. "
        "Sales are growing 20% monthly. Customer satisfaction is high.' "
        "Provide analysis with summary, 3 key points, confidence score 0.8, and 2 recommendations."
    )


def test_simple_agent_v3_tools_and_structured_output():
    """Test SimpleAgentV3 using tools to gather data for structured output."""
    # Create agent that uses tools and returns structured output
    agent = SimpleAgentV3(
        name="research_agent",
        engine=AugLLMConfig(temperature=0.1, structured_output_model=ProductInfo),
        tools=[inventory_lookup, calculator],
        debug=True,
    )

    # Test: Use tools to gather data, then format as structured output

    result = agent.run(
        "Look up the monitor in inventory, calculate its total value, "
        "and return the complete ProductInfo"
    )

    # Verify the result if it's the expected type
    if isinstance(result, ProductInfo):
        # Check calculations
        result.price * result.quantity


def test_simple_agent_v3_error_handling():
    """Test SimpleAgentV3 error handling with tools."""
    agent = SimpleAgentV3(
        name="error_test_agent",
        engine=AugLLMConfig(temperature=0.1),
        tools=[calculator, inventory_lookup],
        debug=True,
    )

    # Test 1: Invalid calculation
    agent.run("Calculate this invalid expression: 10 / / 5")

    # Test 2: Non-existent product
    agent.run("Look up the price of 'quantum computer' in inventory")

    # Test 3: Recovery from error
    agent.run("Try to calculate 'abc + 123' (this will fail), then calculate 100 + 200 instead")


if __name__ == "__main__":
    # Run all tests
    test_simple_agent_v3_with_multiple_tools()
    test_simple_agent_v3_with_structured_output()
    test_simple_agent_v3_tools_and_structured_output()
    test_simple_agent_v3_error_handling()
