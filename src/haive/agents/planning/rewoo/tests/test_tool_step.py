"""from typing import Any, List
Tests for ToolStep - Tool validation and execution.
"""

import contextlib
from typing import Any

import pytest
from langchain_core.tools import tool
from pydantic import ValidationError

from haive.agents.planning.rewoo.models.plans import ExecutionPlan
from haive.agents.planning.rewoo.models.tool_step import (
    ToolStep,
    create_tool_steps_from_plan,
    validate_tool_compatibility)


# Test tools
@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {e!s}"


@tool
def text_analyzer(text: str, min_length: int = 5) -> str:
    """Analyze text and return insights."""
    word_count = len(text.split())
    char_count = len(text)

    if char_count < min_length:
        return f"Text too short (min {min_length} chars)"

    return f"Analysis: {word_count} words, {char_count} characters"


@tool
def file_reader(filepath: str, encoding: str = "utf-8") -> str:
    """Read file contents."""
    return f"Reading {filepath} with encoding {encoding}"


class TestToolStep:
    """Test suite for ToolStep functionality."""

    @pytest.fixture
    def available_tools(self) -> list[Any]:
        """Fixture providing test tools."""
        return [calculator, text_analyzer, file_reader]

    def test_valid_tool_step_creation(self, available_tools) -> None:
        """Test creating a valid ToolStep."""
        step = ToolStep(
            description="Calculate 2 + 2",
            tool_name="calculator",
            tool_args={"expression": "2 + 2"},
            available_tools=available_tools)

        assert step.tool_name == "calculator"
        assert step.tool_args == {"expression": "2 + 2"}
        assert step.is_tool_valid
        assert step.selected_tool == calculator
        assert "expression" in step.required_args

    def test_invalid_tool_name(self, available_tools) -> None:
        """Test validation fails for invalid tool name."""
        with pytest.raises(ValidationError, match="Tool 'nonexistent' not found"):
            ToolStep(
                description="Invalid tool",
                tool_name="nonexistent",
                tool_args={},
                available_tools=available_tools)

    def test_missing_required_args(self, available_tools) -> None:
        """Test validation fails for missing required arguments."""
        with pytest.raises(ValidationError, match="Missing required arguments"):
            ToolStep(
                description="Calculator without expression",
                tool_name="calculator",
                tool_args={},  # Missing required 'expression'
                available_tools=available_tools)

    def test_invalid_args(self, available_tools) -> None:
        """Test validation fails for invalid arguments."""
        with pytest.raises(ValidationError, match="Invalid arguments"):
            ToolStep(
                description="Calculator with invalid args",
                tool_name="calculator",
                tool_args={"expression": "2 + 2", "invalid_arg": "should not exist"},
                available_tools=available_tools)

    def test_optional_args(self, available_tools) -> None:
        """Test tool with optional arguments."""
        # With optional arg
        step1 = ToolStep(
            description="Analyze text with min length",
            tool_name="text_analyzer",
            tool_args={"text": "Hello world", "min_length": 10},
            available_tools=available_tools)
        assert step1.is_tool_valid

        # Without optional arg
        step2 = ToolStep(
            description="Analyze text default min length",
            tool_name="text_analyzer",
            tool_args={"text": "Hello world"},
            available_tools=available_tools)
        assert step2.is_tool_valid

    def test_computed_fields(self, available_tools) -> None:
        """Test computed fields are calculated correctly."""
        step = ToolStep(
            description="Test computed fields",
            tool_name="text_analyzer",
            tool_args={"text": "test"},
            available_tools=available_tools)

        assert "calculator" in step.tool_names
        assert "text_analyzer" in step.tool_names
        assert "file_reader" in step.tool_names

        assert step.selected_tool == text_analyzer
        assert step.tool_schema is not None
        assert "text" in step.required_args
        assert "min_length" in step.optional_args

    def test_tool_execution(self, available_tools) -> None:
        """Test actual tool execution."""
        step = ToolStep(
            description="Calculate 15 * 8",
            tool_name="calculator",
            tool_args={"expression": "15 * 8"},
            available_tools=available_tools)

        # Should be able to execute
        assert step.can_execute(set())

        # Execute and check result
        result = step.execute({"completed_steps": set()})
        assert "120" in str(result)
        assert step.result is not None

    def test_tool_execution_with_dependencies(self, available_tools) -> None:
        """Test tool execution with dependencies."""
        step1 = ToolStep(
            description="First calculation",
            tool_name="calculator",
            tool_args={"expression": "10 + 5"},
            available_tools=available_tools)

        step2 = ToolStep(
            description="Second calculation",
            tool_name="calculator",
            tool_args={"expression": "20 * 2"},
            depends_on=[step1.id],
            available_tools=available_tools)

        # Step 1 can execute
        assert step1.can_execute(set())

        # Step 2 cannot execute yet
        assert not step2.can_execute(set())

        # After step 1 completes
        assert step2.can_execute({step1.id})

    def test_tool_info(self, available_tools) -> None:
        """Test get_tool_info method."""
        step = ToolStep(
            description="Get tool info",
            tool_name="text_analyzer",
            tool_args={"text": "test"},
            available_tools=available_tools)

        info = step.get_tool_info()
        assert info["name"] == "text_analyzer"
        assert "Analyze text" in info["description"]
        assert "text" in info["required_args"]
        assert "min_length" in info["optional_args"]
        assert info["provided_args"] == ["text"]
        assert info["missing_args"] == []
        assert info["is_valid"]

    def test_update_tool_args(self, available_tools) -> None:
        """Test updating tool arguments."""
        step = ToolStep(
            description="Update args test",
            tool_name="text_analyzer",
            tool_args={"text": "original"},
            available_tools=available_tools)

        # Update args
        step.update_tool_args(text="updated", min_length=20)
        assert step.tool_args["text"] == "updated"
        assert step.tool_args["min_length"] == 20

    def test_factory_method(self, available_tools) -> None:
        """Test create_from_tool factory method."""
        step = ToolStep.create_from_tool(
            tool=calculator,
            tool_args={"expression": "5 * 5"},
            available_tools=available_tools,
            description="Factory created step")

        assert step.tool_name == "calculator"
        assert step.description == "Factory created step"
        assert step.is_tool_valid

    def test_empty_tools_list(self) -> None:
        """Test validation fails for empty tools list."""
        with pytest.raises(
            ValidationError, match="Available tools list cannot be empty"
        ):
            ToolStep(
                description="No tools available",
                tool_name="calculator",
                tool_args={"expression": "1 + 1"},
                available_tools=[])

    def test_duplicate_tool_names(self, available_tools) -> None:
        """Test validation fails for duplicate tool names."""
        # Create duplicate tool
        duplicate_tools = available_tools + [calculator]  # calculator appears twice

        with pytest.raises(ValidationError, match="Duplicate tool names"):
            ToolStep(
                description="Duplicate tools",
                tool_name="calculator",
                tool_args={"expression": "1 + 1"},
                available_tools=duplicate_tools)


class TestToolStepFactories:
    """Test factory functions for ToolStep."""

    @pytest.fixture
    def available_tools(self) -> list[Any]:
        return [calculator, text_analyzer, file_reader]

    def test_create_tool_steps_from_plan(self, available_tools) -> None:
        """Test creating multiple steps from plan."""
        plan_data = [
            {
                "description": "Calculate result",
                "tool_name": "calculator",
                "tool_args": {"expression": "10 + 5"},
            },
            {
                "description": "Analyze result",
                "tool_name": "text_analyzer",
                "tool_args": {"text": "Result is 15"},
                # Will need to be updated with actual IDs
                "depends_on": ["step_1"],
            },
        ]

        steps = create_tool_steps_from_plan(plan_data, available_tools)

        assert len(steps) == 2
        assert steps[0].tool_name == "calculator"
        assert steps[1].tool_name == "text_analyzer"
        assert all(step.is_tool_valid for step in steps)

    def test_validate_tool_compatibility(self, available_tools) -> None:
        """Test tool compatibility validation."""
        issues = validate_tool_compatibility(available_tools)

        assert len(issues["duplicate_names"]) == 0
        assert len(issues["missing_schemas"]) == 0
        assert len(issues["tools_without_descriptions"]) == 0
        assert len(issues["valid_tools"]) == 3

    def test_validate_problematic_tools(self) -> str:
        """Test validation with problematic tools."""

        @tool
        def bad_tool_no_desc() -> str:
            return "no description"

        @tool
        def good_tool() -> str:
            """A tool with description."""
            return "good"

        # Test with duplicate names and missing descriptions
        tools = [
            calculator,
            calculator,
            bad_tool_no_desc,
            good_tool,
        ]  # calculator appears twice

        issues = validate_tool_compatibility(tools)

        assert "calculator" in issues["duplicate_names"]
        assert "bad_tool_no_desc" in issues["tools_without_descriptions"]
        assert "good_tool" in issues["valid_tools"]


class TestToolStepIntegration:
    """Test ToolStep integration with ExecutionPlan."""

    @pytest.fixture
    def available_tools(self) -> list[Any]:
        return [calculator, text_analyzer, file_reader]

    def test_tool_steps_in_execution_plan(self, available_tools) -> None:
        """Test ToolSteps work in ExecutionPlan."""
        step1 = ToolStep(
            description="Calculate base value",
            tool_name="calculator",
            tool_args={"expression": "10 * 2"},
            available_tools=available_tools)

        step2 = ToolStep(
            description="Analyze result",
            tool_name="text_analyzer",
            tool_args={"text": "Result is 20"},
            depends_on=[step1.id],
            available_tools=available_tools)

        plan = ExecutionPlan(
            name="Tool Step Plan",
            description="Plan using tool steps",
            steps=[step1, step2])

        assert plan.step_count == 2
        assert plan.max_parallelism == 1
        assert len(plan.execution_levels) == 2

    def test_parallel_tool_execution(self, available_tools) -> None:
        """Test parallel tool steps."""
        step1 = ToolStep(
            description="Calculate first",
            tool_name="calculator",
            tool_args={"expression": "5 + 5"},
            available_tools=available_tools)

        step2 = ToolStep(
            description="Analyze text",
            tool_name="text_analyzer",
            tool_args={"text": "Independent analysis"},
            available_tools=available_tools)

        step3 = ToolStep(
            description="Final calculation",
            tool_name="calculator",
            tool_args={"expression": "10 + 10"},
            depends_on=[step1.id, step2.id],
            available_tools=available_tools)

        plan = ExecutionPlan(
            name="Parallel Tool Plan",
            description="Plan with parallel tool steps",
            steps=[step1, step2, step3])

        assert plan.max_parallelism == 2  # step1 and step2 can run in parallel
        assert len(plan.execution_levels) == 2
        assert set(plan.execution_levels[0]) == {step1.id, step2.id}
        assert plan.execution_levels[1] == [step3.id]


if __name__ == "__main__":
    # Run basic tests without pytest

    tools = [calculator, text_analyzer, file_reader]

    # Test valid step
    with contextlib.suppress(Exception):
        step = ToolStep(
            description="Test calculation",
            tool_name="calculator",
            tool_args={"expression": "2 + 2"},
            available_tools=tools)

    # Test invalid tool name
    with contextlib.suppress(ValidationError):
        ToolStep(
            description="Invalid tool",
            tool_name="nonexistent",
            tool_args={},
            available_tools=tools)

    # Test missing args
    with contextlib.suppress(ValidationError):
        ToolStep(
            description="Missing args",
            tool_name="calculator",
            tool_args={},
            available_tools=tools)

    # Test execution
    try:
        step = ToolStep(
            description="Execute calculation",
            tool_name="calculator",
            tool_args={"expression": "15 * 8"},
            available_tools=tools)
        result = step.execute({"completed_steps": set()})
    except Exception:
        pass
