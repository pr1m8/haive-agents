"""Test agent fixtures and auto-wrap behavior.

This test file validates the agent fixtures in conftest.py and tests the auto-wrapping
behavior for agents with structured output models.

Uses fixtures from conftest.py:
- simple_agent_with_structured_output (will auto-wrap)
- simple_agent_without_structured_output (no auto-wrap)  
- react_agent_with_tools (no auto-wrap)
- complex_structured_agent (will auto-wrap)
"""


# Import the models from parent conftest for type checking
from ..conftest import AnalysisResult, SimpleResult


# ========================================================================
# TEST CLASSES
# ========================================================================

class TestAgentFixtures:
    """Test the agent fixtures to ensure they're configured correctly."""

    def test_simple_agent_with_structured_output_fixture(self, simple_agent_with_structured_output):
        """Test SimpleAgent with structured output fixture."""
        agent = simple_agent_with_structured_output

        print("\n🔍 Testing SimpleAgent with structured output:")
        print(f"   - Name: {agent.name}")
        print(f"   - Class: {agent.__class__.__name__}")
        print(f"   - Has structured_output_model: {bool(agent.structured_output_model)}")
        print(f"   - Structured model: {agent.structured_output_model}")
        print(f"   - Auto-wrap needed: {bool(getattr(agent, '_needs_structured_output_wrapper', False))}")

        # Assertions
        assert agent.name == "simple_structured"
        assert agent.structured_output_model == SimpleResult
        assert getattr(agent, "_needs_structured_output_wrapper", False) == True

    def test_simple_agent_without_structured_output_fixture(self, simple_agent_without_structured_output):
        """Test SimpleAgent without structured output fixture."""
        agent = simple_agent_without_structured_output

        print("\n🔍 Testing SimpleAgent without structured output:")
        print(f"   - Name: {agent.name}")
        print(f"   - Class: {agent.__class__.__name__}")
        print(f"   - Has structured_output_model: {bool(getattr(agent, 'structured_output_model', None))}")
        print(f"   - Auto-wrap needed: {bool(getattr(agent, '_needs_structured_output_wrapper', False))}")

        # Assertions
        assert agent.name == "simple_plain"
        assert getattr(agent, "structured_output_model", None) is None
        assert getattr(agent, "_needs_structured_output_wrapper", False) == False

    def test_react_agent_with_tools_fixture(self, react_agent_with_tools):
        """Test ReactAgent with tools fixture."""
        agent = react_agent_with_tools

        print("\n🔍 Testing ReactAgent with tools:")
        print(f"   - Name: {agent.name}")
        print(f"   - Class: {agent.__class__.__name__}")
        print(f"   - Has structured_output_model: {bool(getattr(agent, 'structured_output_model', None))}")
        print(f"   - Auto-wrap needed: {bool(getattr(agent, '_needs_structured_output_wrapper', False))}")
        print(f"   - Tools: {len(getattr(agent.engine, 'tools', []))}")

        # Assertions
        assert agent.name == "react_with_tools"
        assert getattr(agent, "structured_output_model", None) is None
        assert getattr(agent, "_needs_structured_output_wrapper", False) == False
        assert len(getattr(agent.engine, "tools", [])) == 2

    def test_complex_structured_agent_fixture(self, complex_structured_agent):
        """Test complex structured output agent fixture."""
        agent = complex_structured_agent

        print("\n🔍 Testing complex structured agent:")
        print(f"   - Name: {agent.name}")
        print(f"   - Class: {agent.__class__.__name__}")
        print(f"   - Structured model: {agent.structured_output_model}")
        print(f"   - Auto-wrap needed: {bool(getattr(agent, '_needs_structured_output_wrapper', False))}")

        # Assertions
        assert agent.name == "complex_structured"
        assert agent.structured_output_model == AnalysisResult
        assert getattr(agent, "_needs_structured_output_wrapper", False) == True


class TestAgentExecution:
    """Test actual agent execution with fixtures."""

    def test_simple_agent_without_structured_execution(self, simple_agent_without_structured_output):
        """Test execution of SimpleAgent without structured output."""
        agent = simple_agent_without_structured_output

        print("\n🚀 Testing SimpleAgent execution (no structured output):")

        test_input = "Hello, how are you today?"

        try:
            result = agent.run(test_input)

            print("   - ✅ SUCCESS")
            print(f"   - Result type: {type(result)}")
            print(f"   - Result length: {len(str(result))}")

            assert result is not None
            assert len(str(result)) > 0

        except Exception as e:
            print(f"   - ❌ FAILED: {e}")
            print(f"   - Error type: {type(e)}")
            raise

    def test_simple_agent_with_structured_execution(self, simple_agent_with_structured_output):
        """Test execution of SimpleAgent WITH structured output (auto-wrapped)."""
        agent = simple_agent_with_structured_output

        print("\n🚀 Testing SimpleAgent execution (WITH structured output):")
        print(f"   - Auto-wrap needed: {getattr(agent, '_needs_structured_output_wrapper', False)}")

        test_input = "Format this message: Hello World"

        try:
            result = agent.run(test_input)

            print("   - ✅ SUCCESS")
            print(f"   - Result type: {type(result)}")
            print(f"   - Result: {result}")

            assert result is not None

            # Check if we got structured output
            if isinstance(result, SimpleResult):
                print(f"   - Got SimpleResult: {result.message}")
                assert result.message is not None
                assert 0.0 <= result.confidence <= 1.0

        except Exception as e:
            print(f"   - ❌ FAILED: {e}")
            print(f"   - Error type: {type(e)}")
            import traceback
            traceback.print_exc()
            raise

    def test_react_agent_with_tools_execution(self, react_agent_with_tools):
        """Test execution of ReactAgent with tools."""
        agent = react_agent_with_tools

        print("\n🚀 Testing ReactAgent execution (with tools):")

        test_input = "Calculate 15 * 23 and analyze the text 'Hello World'"

        try:
            result = agent.run(test_input)

            print("   - ✅ SUCCESS")
            print(f"   - Result type: {type(result)}")
            print(f"   - Result length: {len(str(result))}")

            assert result is not None
            assert len(str(result)) > 0

            # Check if tools were used (should contain calculation result)
            result_str = str(result)
            if "345" in result_str:
                print("   - ✅ Calculator tool was used (found 345)")

        except Exception as e:
            print(f"   - ❌ FAILED: {e}")
            print(f"   - Error type: {type(e)}")
            import traceback
            traceback.print_exc()
            raise


class TestAutoWrapDetection:
    """Test auto-wrap detection logic across different agent types."""

    def test_auto_wrap_detection_comparison(
        self,
        simple_agent_with_structured_output,
        simple_agent_without_structured_output,
        react_agent_with_tools
    ):
        """Compare auto-wrap detection across all agent types."""

        agents = [
            ("SimpleAgent WITH structured", simple_agent_with_structured_output),
            ("SimpleAgent WITHOUT structured", simple_agent_without_structured_output),
            ("ReactAgent with tools", react_agent_with_tools),
        ]

        print("\n🔍 Auto-wrap detection comparison:")

        for description, agent in agents:
            has_structured = bool(getattr(agent, "structured_output_model", None))
            needs_wrap = bool(getattr(agent, "_needs_structured_output_wrapper", False))

            print(f"   - {description}:")
            print(f"     * Has structured_output_model: {has_structured}")
            print(f"     * Needs auto-wrap: {needs_wrap}")

        # Assertions
        assert getattr(simple_agent_with_structured_output, "_needs_structured_output_wrapper", False) == True
        assert getattr(simple_agent_without_structured_output, "_needs_structured_output_wrapper", False) == False
        assert getattr(react_agent_with_tools, "_needs_structured_output_wrapper", False) == False
