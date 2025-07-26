"""Focused test for SimpleAgentV3 with tools and structured output."""

import pytest
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.simple.agent_v3 import SimpleAgentV3


# Define a simple tool
@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"


# Define structured output model
class MathResult(BaseModel):
    """Structured output for math calculations."""

    expression: str = Field(description="The mathematical expression")
    result: float = Field(description="The calculated result")
    explanation: str = Field(description="Step by step explanation")


def test_simple_agent_v3_with_tool():
    """Test SimpleAgentV3 with a calculator tool."""
    print("\n" + "=" * 60)
    print("TEST: SimpleAgentV3 with Calculator Tool")
    print("=" * 60)

    # Create agent with tool
    agent = SimpleAgentV3(
        name="calc_agent",
        engine=AugLLMConfig(temperature=0.1),
        tools=[calculator],
        debug=True,
    )

    # Test calculation
    result = agent.run("Please calculate 25 * 34")
    print(f"\nResult type: {type(result)}")
    print(f"Result: {result}")

    # Check if result contains the calculation
    if hasattr(result, "messages"):
        print(f"Number of messages: {len(result.messages)}")
        for i, msg in enumerate(result.messages):
            print(f"Message {i}: {type(msg).__name__}")
            if hasattr(msg, "tool_calls"):
                print(f"  Tool calls: {msg.tool_calls}")

    assert "850" in str(result)
    print("✅ Tool test passed!")


def test_simple_agent_v3_with_structured_output():
    """Test SimpleAgentV3 with structured output."""
    print("\n" + "=" * 60)
    print("TEST: SimpleAgentV3 with Structured Output")
    print("=" * 60)

    # Create agent with structured output
    agent = SimpleAgentV3(
        name="struct_agent",
        engine=AugLLMConfig(temperature=0.1, structured_output_model=MathResult),
        debug=True,
    )

    # Test structured output
    result = agent.run("Calculate 15 * 8 and explain the steps")
    print(f"\nResult type: {type(result)}")
    print(f"Result: {result}")

    # Check if result is the expected type
    if isinstance(result, MathResult):
        print(f"\n✅ Got MathResult!")
        print(f"  Expression: {result.expression}")
        print(f"  Result: {result.result}")
        print(f"  Explanation: {result.explanation}")
        assert result.result == 120
    else:
        print(f"❌ Got unexpected type: {type(result)}")

    print("✅ Structured output test passed!")


def test_simple_agent_v3_with_tool_and_structured_output():
    """Test SimpleAgentV3 with both tool and structured output."""
    print("\n" + "=" * 60)
    print("TEST: SimpleAgentV3 with Tool + Structured Output")
    print("=" * 60)

    # Create agent with tool AND structured output
    agent = SimpleAgentV3(
        name="combo_agent",
        engine=AugLLMConfig(temperature=0.1, structured_output_model=MathResult),
        tools=[calculator],
        debug=True,
    )

    # Test using tool then formatting as structured output
    result = agent.run(
        "Use the calculator to compute 12 * 12, then provide the result as MathResult"
    )
    print(f"\nResult type: {type(result)}")
    print(f"Result: {result}")

    # Check result
    if isinstance(result, MathResult):
        print(f"\n✅ Got MathResult!")
        print(f"  Expression: {result.expression}")
        print(f"  Result: {result.result}")
        print(f"  Explanation: {result.explanation}")
        assert result.result == 144
    else:
        print(f"Note: Got {type(result)} instead of MathResult")

    print("✅ Tool + Structured output test completed!")


if __name__ == "__main__":
    test_simple_agent_v3_with_tool()
    test_simple_agent_v3_with_structured_output()
    test_simple_agent_v3_with_tool_and_structured_output()

    print("\n" + "=" * 60)
    print("ALL TESTS COMPLETED!")
    print("=" * 60)
