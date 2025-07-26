"""Comprehensive test for SimpleAgentV3 with various tools and structured output."""

from typing import List

import pytest
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.simple.agent_v3 import SimpleAgentV3


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
    key_points: List[str] = Field(description="Key points from analysis")
    confidence_score: float = Field(ge=0.0, le=1.0, description="Confidence score")
    recommendations: List[str] = Field(description="Recommendations")


# Define test tools
@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"


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
    elif operation == "count":
        return f"Data length: {len(data)} characters"
    elif operation == "reverse":
        return f"Reversed: {data[::-1]}"
    else:
        return f"Unknown operation: {operation}"


def test_simple_agent_v3_with_multiple_tools():
    """Test SimpleAgentV3 with multiple different tools."""
    print("\n" + "=" * 80)
    print("TESTING SimpleAgentV3 with Multiple Tools")
    print("=" * 80)

    # Create agent with multiple tools
    agent = SimpleAgentV3(
        name="multi_tool_agent",
        engine=AugLLMConfig(temperature=0.1),
        tools=[calculator, inventory_lookup, text_analyzer, data_processor],
        debug=True,
    )

    # Test 1: Calculator
    print("\nTest 1: Calculator Tool")
    print("-" * 40)
    result1 = agent.run("Calculate (150 * 4) + 200")
    print(f"Result: {result1}")

    # Test 2: Inventory lookup
    print("\nTest 2: Inventory Lookup")
    print("-" * 40)
    result2 = agent.run("Look up the price and quantity of laptop in inventory")
    print(f"Result: {result2}")

    # Test 3: Text analysis
    print("\nTest 3: Text Analysis")
    print("-" * 40)
    result3 = agent.run(
        "Analyze this text: 'The quick brown fox jumps over the lazy dog. It's a beautiful day!'"
    )
    print(f"Result: {result3}")

    # Test 4: Data processing
    print("\nTest 4: Data Processing")
    print("-" * 40)
    result4 = agent.run("Process this data 'Hello World' by reversing it")
    print(f"Result: {result4}")

    # Test 5: Multiple tools in sequence
    print("\nTest 5: Multiple Tools in Sequence")
    print("-" * 40)
    result5 = agent.run(
        "First calculate 30 * 20, then look up laptop inventory, "
        "and finally analyze the text 'Great products at great prices!'"
    )
    print(f"Result: {result5}")

    print("\n✅ Multiple tools test completed")


def test_simple_agent_v3_with_structured_output():
    """Test SimpleAgentV3 with structured output models."""
    print("\n" + "=" * 80)
    print("TESTING SimpleAgentV3 with Structured Output")
    print("=" * 80)

    # Test 1: Product Info structured output
    print("\nTest 1: Product Info Structured Output")
    print("-" * 40)

    agent1 = SimpleAgentV3(
        name="product_agent",
        engine=AugLLMConfig(temperature=0.1, structured_output_model=ProductInfo),
        tools=[inventory_lookup, calculator],
        debug=True,
    )

    result1 = agent1.run(
        "Look up laptop inventory and calculate total value (price * quantity). "
        "Return as ProductInfo with name='Laptop'"
    )
    print(f"Result type: {type(result1)}")
    print(f"Result: {result1}")

    # Test 2: Analysis Result structured output
    print("\nTest 2: Analysis Result Structured Output")
    print("-" * 40)

    agent2 = SimpleAgentV3(
        name="analysis_agent",
        engine=AugLLMConfig(temperature=0.1, structured_output_model=AnalysisResult),
        tools=[text_analyzer, data_processor],
        debug=True,
    )

    result2 = agent2.run(
        "Analyze the following business scenario: 'Our company sells laptops and accessories. "
        "Sales are growing 20% monthly. Customer satisfaction is high.' "
        "Provide analysis with summary, 3 key points, confidence score 0.8, and 2 recommendations."
    )
    print(f"Result type: {type(result2)}")
    print(f"Result: {result2}")

    print("\n✅ Structured output test completed")


def test_simple_agent_v3_tools_and_structured_output():
    """Test SimpleAgentV3 using tools to gather data for structured output."""
    print("\n" + "=" * 80)
    print("TESTING SimpleAgentV3 with Tools + Structured Output")
    print("=" * 80)

    # Create agent that uses tools and returns structured output
    agent = SimpleAgentV3(
        name="research_agent",
        engine=AugLLMConfig(temperature=0.1, structured_output_model=ProductInfo),
        tools=[inventory_lookup, calculator],
        debug=True,
    )

    # Test: Use tools to gather data, then format as structured output
    print("\nTest: Tools → Structured Output")
    print("-" * 40)

    result = agent.run(
        "Look up the monitor in inventory, calculate its total value, "
        "and return the complete ProductInfo"
    )

    print(f"Result type: {type(result)}")
    print(f"Result: {result}")

    # Verify the result if it's the expected type
    if isinstance(result, ProductInfo):
        print(f"\nValidation:")
        print(f"  - Name: {result.name}")
        print(f"  - Price: ${result.price}")
        print(f"  - Quantity: {result.quantity}")
        print(f"  - Total Value: ${result.total_value}")

        # Check calculations
        expected_total = result.price * result.quantity
        print(
            f"  - Calculation Check: {result.total_value} == {expected_total}? "
            f"{abs(result.total_value - expected_total) < 0.01}"
        )

    print("\n✅ Tools + Structured output test completed")


def test_simple_agent_v3_error_handling():
    """Test SimpleAgentV3 error handling with tools."""
    print("\n" + "=" * 80)
    print("TESTING SimpleAgentV3 Error Handling")
    print("=" * 80)

    agent = SimpleAgentV3(
        name="error_test_agent",
        engine=AugLLMConfig(temperature=0.1),
        tools=[calculator, inventory_lookup],
        debug=True,
    )

    # Test 1: Invalid calculation
    print("\nTest 1: Invalid Calculation")
    print("-" * 40)
    result1 = agent.run("Calculate this invalid expression: 10 / / 5")
    print(f"Result: {result1}")

    # Test 2: Non-existent product
    print("\nTest 2: Non-existent Product")
    print("-" * 40)
    result2 = agent.run("Look up the price of 'quantum computer' in inventory")
    print(f"Result: {result2}")

    # Test 3: Recovery from error
    print("\nTest 3: Error Recovery")
    print("-" * 40)
    result3 = agent.run(
        "Try to calculate 'abc + 123' (this will fail), "
        "then calculate 100 + 200 instead"
    )
    print(f"Result: {result3}")

    print("\n✅ Error handling test completed")


if __name__ == "__main__":
    # Run all tests
    test_simple_agent_v3_with_multiple_tools()
    test_simple_agent_v3_with_structured_output()
    test_simple_agent_v3_tools_and_structured_output()
    test_simple_agent_v3_error_handling()

    print("\n" + "=" * 80)
    print("ALL TESTS COMPLETED!")
    print("=" * 80)
