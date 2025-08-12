"""Debug MultiAgent issue with proper test structure."""

from datetime import datetime

from langchain_core.tools import tool
from pydantic import BaseModel, Field
import pytest

from haive.agents.multi.agent import MultiAgent

# Import our agents
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig


class TestResult(BaseModel):
    """Simple test result model."""
    message: str = Field(description="Result message")
    confidence: float = Field(description="Confidence score", default=0.8)
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())


@tool
def simple_calculator(expression: str) -> str:
    """Calculate simple math expressions."""
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {e}"


class TestMultiAgentDebug:
    """Debug test for MultiAgent issues."""

    @pytest.fixture
    def react_agent(self):
        """ReactAgent without structured output."""
        return ReactAgent(
            name="react_test",
            engine=AugLLMConfig(
                llm_config=AzureLLMConfig(
                    model="gpt-4o",
                    temperature=0.7,
                ),
                system_message="You are a reasoning agent.",
                tools=[simple_calculator],
            ),
            debug=True,
        )

    @pytest.fixture
    def simple_agent(self):
        """SimpleAgent WITH structured output (will auto-wrap)."""
        return SimpleAgent(
            name="simple_test",
            engine=AugLLMConfig(
                llm_config=AzureLLMConfig(
                    model="gpt-4o",
                    temperature=0.3,
                ),
                system_message="You are a formatter agent.",
            ),
            structured_output_model=TestResult,
            structured_output_version="v2",
            debug=True,
        )

    def test_agent_creation_and_auto_wrap(self, react_agent, simple_agent):
        """Test agent creation and auto-wrap detection."""
        print("\n🔍 ReactAgent:")
        print(f"   - Class: {react_agent.__class__.__name__}")
        print(f"   - Has structured_output_model: {bool(getattr(react_agent, 'structured_output_model', None))}")
        print(f"   - Auto-wrap needed: {bool(getattr(react_agent, '_needs_structured_output_wrapper', False))}")

        print("\n🔍 SimpleAgent:")
        print(f"   - Class: {simple_agent.__class__.__name__}")
        print(f"   - Has structured_output_model: {bool(getattr(simple_agent, 'structured_output_model', None))}")
        print(f"   - Auto-wrap needed: {bool(getattr(simple_agent, '_needs_structured_output_wrapper', False))}")

        # This is the key discovery point
        assert getattr(simple_agent, "_needs_structured_output_wrapper", False) == True
        assert getattr(react_agent, "_needs_structured_output_wrapper", False) == False

    def test_multi_agent_creation(self, react_agent, simple_agent):
        """Test MultiAgent creation."""
        multi_agent = MultiAgent(
            name="test_multi",
            agents=[react_agent, simple_agent],
            execution_mode="sequential",
            debug=True,
        )

        print("\n🔍 MultiAgent:")
        print(f"   - Class: {multi_agent.__class__.__name__}")
        print(f"   - Agent count: {len(multi_agent.agents)}")
        print(f"   - Agent names: {list(multi_agent.agent_dict.keys())}")

        # Check what kind of agents are actually in the dict
        for name, agent in multi_agent.agent_dict.items():
            print(f"   - Agent '{name}': {agent.__class__.__name__}")
            if hasattr(agent, "_needs_structured_output_wrapper"):
                print(f"     * Auto-wrap: {agent._needs_structured_output_wrapper}")
            if hasattr(agent, "structured_output_model"):
                print(f"     * Structured output: {agent.structured_output_model}")

        assert len(multi_agent.agents) == 2
        assert "react_test" in multi_agent.agent_dict
        assert "simple_test" in multi_agent.agent_dict

    def test_multi_agent_compilation(self, react_agent, simple_agent):
        """Test MultiAgent compilation."""
        multi_agent = MultiAgent(
            name="test_multi",
            agents=[react_agent, simple_agent],
            execution_mode="sequential",
            debug=True,
        )

        print("\n🔍 Compiling MultiAgent...")

        # This should work
        multi_agent.compile()

        print(f"   - Compiled: {multi_agent._is_compiled}")
        print(f"   - App type: {type(multi_agent._app)}")

        assert multi_agent._is_compiled == True
        assert multi_agent._app is not None

    def test_multi_agent_execution_failure(self, react_agent, simple_agent):
        """Test MultiAgent execution - THIS SHOULD FAIL and show us the issue."""
        multi_agent = MultiAgent(
            name="test_multi",
            agents=[react_agent, simple_agent],
            execution_mode="sequential",
            debug=True,
        )

        # Compile first
        multi_agent.compile()

        # Create test input
        test_input = "Calculate 15 * 23 and format the result"

        print("\n🔍 Testing MultiAgent execution...")
        print(f"   - Input: '{test_input}'")
        print(f"   - Input type: {type(test_input)}")

        # ADD BREAKPOINT HERE TO TRACE THE ISSUE
        try:
            # This is where the error should occur
            result = multi_agent.run(test_input)

            print(f"   - ✅ SUCCESS: {result}")

        except Exception as e:
            print(f"   - ❌ FAILED: {e}")
            print(f"   - Error type: {type(e)}")

            # Re-raise so we can see the full traceback
            raise

    def test_direct_simple_agent_execution(self, simple_agent):
        """Test SimpleAgent execution directly to see if auto-wrapping works."""
        print("\n🔍 Testing SimpleAgent directly...")

        test_input = "Format this: Hello World"

        try:
            # Test direct execution
            result = simple_agent.run(test_input)

            print(f"   - ✅ SUCCESS: {type(result)}")
            print(f"   - Result: {result}")

        except Exception as e:
            print(f"   - ❌ FAILED: {e}")
            print(f"   - Error type: {type(e)}")

            # Re-raise so we can see what happens
            raise

    def test_input_format_tracing(self, react_agent, simple_agent):
        """Trace input formats through the execution chain."""
        multi_agent = MultiAgent(
            name="test_multi",
            agents=[react_agent, simple_agent],
            execution_mode="sequential",
            debug=True,
        )

        multi_agent.compile()

        # Let's examine what gets passed to the execution chain
        test_input = "Test input"

        print("\n🔍 Tracing input format...")

        # Check what _prepare_input returns
        prepared = multi_agent._prepare_input(test_input)
        print(f"   - Prepared input type: {type(prepared)}")
        print(f"   - Prepared input: {prepared}")

        # Check what state schema is expected
        print(f"   - MultiAgent state schema: {multi_agent.state_schema}")

        # This should tell us about the format mismatch

        # Don't actually run to avoid the error, just trace the format
