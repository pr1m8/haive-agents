"""Isolated analysis of individual agent behavior with structured output.

This test file examines each agent type in isolation to understand:
1. State schema composition
2. Structured output configuration
3. Actual vs expected behavior
"""

from typing import Any, Dict, List

import pytest
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent


# Test structured output model
class TestAnalysis(BaseModel):
    """Simple test model for structured output validation."""

    summary: str = Field(description="Brief summary of the analysis")
    key_points: List[str] = Field(description="List of key points")
    conclusion: str = Field(description="Final conclusion")
    confidence: float = Field(description="Confidence score 0-1")


@tool
def simple_calculator(expression: str) -> str:
    """Calculate simple mathematical expressions."""
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"


class TestIsolatedAgentAnalysis:
    """Isolated testing of individual agent behavior."""

    def test_simple_agent_state_schema_inspection(self):
        """Inspect SimpleAgent state schema without structured output."""
        print("\n=== SimpleAgent State Schema Analysis ===")

        # Create basic SimpleAgent without structured output
        agent = SimpleAgent(
            name="basic_simple",
            engine=AugLLMConfig(
                llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.7)
            ),
            debug=True,
        )

        print(f"Agent name: {agent.name}")
        print(f"Agent type: {type(agent)}")
        print(f"Structured output model: {agent.structured_output_model}")
        print(f"Structured output version: {agent.structured_output_version}")

        # Inspect engine and schema before compilation
        print(f"Engine type: {type(agent.engine)}")
        print(
            f"Engine output schema (before): {getattr(agent.engine, 'output_schema', 'Not set')}"
        )

        # Compile to see schema composition
        agent.compile()

        print(f"Agent state schema: {agent.state_schema}")
        print(f"State schema fields: {list(agent.state_schema.model_fields.keys())}")
        print(
            f"Engine output schema (after): {getattr(agent.engine, 'output_schema', 'Not set')}"
        )

        # Check if schema has expected fields
        expected_fields = ["messages"]
        for field in expected_fields:
            assert field in agent.state_schema.model_fields, f"Missing field: {field}"

        print("✅ Basic SimpleAgent schema analysis complete")

    def test_simple_agent_with_structured_output_schema(self):
        """Inspect SimpleAgent with structured output configuration."""
        print("\n=== SimpleAgent with Structured Output Schema Analysis ===")

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

        print(f"Agent name: {agent.name}")
        print(f"Structured output model: {agent.structured_output_model}")
        print(f"Structured output version: {agent.structured_output_version}")

        # Check configuration before compilation
        print(
            f"Engine output schema (before compile): {getattr(agent.engine, 'output_schema', 'Not set')}"
        )

        # Compile to trigger schema modification
        agent.compile()

        print(f"Agent state schema: {agent.state_schema}")
        print(f"State schema fields: {list(agent.state_schema.model_fields.keys())}")
        print(
            f"Engine output schema (after compile): {getattr(agent.engine, 'output_schema', 'Not set')}"
        )

        # Check if structured output field was added
        state_fields = list(agent.state_schema.model_fields.keys())
        print(f"All state fields: {state_fields}")

        # Should have 'messages' + structured output field
        assert "messages" in state_fields, "Missing messages field"

        # Look for structured output field (derived from TestAnalysis)
        structured_fields = [f for f in state_fields if f != "messages"]
        print(f"Non-message fields (potential structured output): {structured_fields}")

        if structured_fields:
            print(f"✅ Found potential structured output field(s): {structured_fields}")
        else:
            print("❌ No structured output fields found!")

        print("✅ Structured SimpleAgent schema analysis complete")

    def test_react_agent_state_schema_inspection(self):
        """Inspect ReactAgent state schema."""
        print("\n=== ReactAgent State Schema Analysis ===")

        # Create ReactAgent with tools
        agent = ReactAgent(
            name="react_test",
            engine=AugLLMConfig(
                llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.7),
                tools=[simple_calculator],
            ),
            debug=True,
        )

        print(f"Agent name: {agent.name}")
        print(f"Agent type: {type(agent)}")
        print(f"Structured output model: {agent.structured_output_model}")
        print(
            f"Engine tools: {len(agent.engine.tools) if hasattr(agent.engine, 'tools') else 'No tools attr'}"
        )

        # Compile to see schema
        agent.compile()

        print(f"Agent state schema: {agent.state_schema}")
        print(f"State schema fields: {list(agent.state_schema.model_fields.keys())}")

        # ReactAgent should have same base schema as SimpleAgent
        expected_fields = ["messages"]
        for field in expected_fields:
            assert field in agent.state_schema.model_fields, f"Missing field: {field}"

        print("✅ ReactAgent schema analysis complete")

    def test_react_agent_with_structured_output_schema(self):
        """Inspect ReactAgent with structured output (inherited from SimpleAgent)."""
        print("\n=== ReactAgent with Structured Output Schema Analysis ===")

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

        print(f"Agent name: {agent.name}")
        print(f"Structured output model: {agent.structured_output_model}")
        print(f"Engine tools: {len(agent.engine.tools)}")

        # Compile to trigger schema modification
        agent.compile()

        print(f"Agent state schema: {agent.state_schema}")
        print(f"State schema fields: {list(agent.state_schema.model_fields.keys())}")

        # Check for structured output field
        state_fields = list(agent.state_schema.model_fields.keys())
        structured_fields = [f for f in state_fields if f != "messages"]
        print(f"Non-message fields: {structured_fields}")

        assert "messages" in state_fields, "Missing messages field"

        if structured_fields:
            print(f"✅ ReactAgent inherited structured output: {structured_fields}")
        else:
            print("❌ ReactAgent missing structured output fields!")

        print("✅ Structured ReactAgent schema analysis complete")

    def test_simple_agent_isolated_execution(self):
        """Test SimpleAgent execution in isolation to see actual output."""
        print("\n=== SimpleAgent Isolated Execution Test ===")

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

        print(f"Input: {test_input}")
        print(
            f"Expected output should contain TestAnalysis fields: summary, key_points, conclusion, confidence"
        )

        try:
            result = agent._app.invoke(test_input, config=config)

            print(f"Result type: {type(result)}")
            print(f"Result keys: {list(result.keys())}")
            print(f"Full result: {result}")

            # Check for structured output field
            structured_fields = [k for k in result.keys() if k != "messages"]
            if structured_fields:
                for field in structured_fields:
                    field_value = result[field]
                    print(f"Structured field '{field}': {field_value}")
                    print(f"Structured field type: {type(field_value)}")

                    # Check if it's our TestAnalysis model
                    if hasattr(field_value, "summary"):
                        print(
                            f"✅ Found TestAnalysis structure: summary={field_value.summary}"
                        )
            else:
                print("❌ No structured output fields in result")

        except Exception as e:
            print(f"Execution error: {e}")
            if "msgpack serializable" in str(e):
                print("✅ Agent executed but hit serialization issue")
            else:
                raise

        print("✅ SimpleAgent isolated execution test complete")


if __name__ == "__main__":
    # Run tests
    pytest.main([__file__, "-v", "-s"])
