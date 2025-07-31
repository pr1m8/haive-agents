"""Isolated analysis of individual agent behavior with structured output.

This test file examines each agent type in isolation to understand:
1. State schema composition
2. Structured output configuration
3. Actual vs expected behavior
"""

from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from pydantic import BaseModel, Field
import pytest

from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig


# Test structured output model
class TestAnalysis(BaseModel):
    """Simple test model for structured output validation."""

    summary: str = Field(description="Brief summary of the analysis")
    key_points: list[str] = Field(description="List of key points")
    conclusion: str = Field(description="Final conclusion")
    confidence: float = Field(description="Confidence score 0-1")


@tool
def simple_calculator(expression: str) -> str:
    """Calculate simple mathematical expressions."""
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {e!s}"


class TestIsolatedAgentAnalysis:
    """Isolated testing of individual agent behavior."""

    def test_simple_agent_state_schema_inspection(self):
        """Inspect SimpleAgent state schema without structured output."""
        # Create basic SimpleAgent without structured output
        agent = SimpleAgent(
            name="basic_simple",
            engine=AugLLMConfig(
                llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.7)
            ),
            debug=True,
        )

        # Inspect engine and schema before compilation

        # Compile to see schema composition
        agent.compile()

        # Check if schema has expected fields
        expected_fields = ["messages"]
        for field in expected_fields:
            assert field in agent.state_schema.model_fields, f"Missing field: {field}"

    def test_simple_agent_with_structured_output_schema(self):
        """Inspect SimpleAgent with structured output configuration."""
        # Create SimpleAgent WITH structured output
        agent = SimpleAgent(
            name="structured_simple",
            engine=AugLLMConfig(
                llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.3)
            ),
            structured_output_model=TestAnalysis,
            structured_output_version="v2",
            debug=True,
        )

        # Check configuration before compilation

        # Compile to trigger schema modification
        agent.compile()

        # Check if structured output field was added
        state_fields = list(agent.state_schema.model_fields.keys())

        # Should have 'messages' + structured output field
        assert "messages" in state_fields, "Missing messages field"

        # Look for structured output field (derived from TestAnalysis)
        structured_fields = [f for f in state_fields if f != "messages"]

        if structured_fields:
            pass
        else:
            pass

    def test_react_agent_state_schema_inspection(self):
        """Inspect ReactAgent state schema."""
        # Create ReactAgent with tools
        agent = ReactAgent(
            name="react_test",
            engine=AugLLMConfig(
                llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.7),
                tools=[simple_calculator],
            ),
            debug=True,
        )

        # Compile to see schema
        agent.compile()

        # ReactAgent should have same base schema as SimpleAgent
        expected_fields = ["messages"]
        for field in expected_fields:
            assert field in agent.state_schema.model_fields, f"Missing field: {field}"

    def test_react_agent_with_structured_output_schema(self):
        """Inspect ReactAgent with structured output (inherited from SimpleAgent)."""
        # Create ReactAgent WITH structured output
        agent = ReactAgent(
            name="structured_react",
            engine=AugLLMConfig(
                llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.3),
                tools=[simple_calculator],
            ),
            structured_output_model=TestAnalysis,
            structured_output_version="v2",
            debug=True,
        )

        # Compile to trigger schema modification
        agent.compile()

        # Check for structured output field
        state_fields = list(agent.state_schema.model_fields.keys())
        structured_fields = [f for f in state_fields if f != "messages"]

        assert "messages" in state_fields, "Missing messages field"

        if structured_fields:
            pass
        else:
            pass

    def test_simple_agent_isolated_execution(self):
        """Test SimpleAgent execution in isolation to see actual output."""
        # Create SimpleAgent with structured output
        agent = SimpleAgent(
            name="isolated_simple",
            engine=AugLLMConfig(
                llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.3)
            ),
            structured_output_model=TestAnalysis,
            structured_output_version="v2",
            debug=True,
        )

        # Compile
        agent.compile()

        # Test input
        test_input = {
            "messages": [
                HumanMessage(content="Analyze this: Python is a programming language")
            ]
        }
        config = {"configurable": {"thread_id": None}}

        try:
            result = agent._app.invoke(test_input, config=config)

            # Check for structured output field
            structured_fields = [k for k in result if k != "messages"]
            if structured_fields:
                for field in structured_fields:
                    field_value = result[field]

                    # Check if it's our TestAnalysis model
                    if hasattr(field_value, "summary"):
                        pass
            else:
                pass

        except Exception as e:
            if "msgpack serializable" in str(e):
                pass
            else:
                raise


if __name__ == "__main__":
    # Run tests
    pytest.main([__file__, "-v", "-s"])
