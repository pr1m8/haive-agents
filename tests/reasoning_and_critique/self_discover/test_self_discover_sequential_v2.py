"""Test Self-Discover Sequential V2 implementation.

Tests follow the "no mocks" philosophy - using real LLMs and components.
"""

import pytest

from haive.agents.reasoning_and_critique.self_discover.self_discover_sequential_v2 import (
    DEFAULT_REASONING_MODULES,
    ModuleSelectionResult,
    ReasoningStructure,
    SelectedModule,
    create_adapter_agent,
    create_selector_agent,
    create_self_discover_sequential,
)


class TestSelfDiscoverAgents:
    """Test individual Self-Discover agents."""

    @pytest.mark.asyncio
    async def test_selector_agent_real_execution(self):
        """Test selector agent with real LLM."""
        # Create agent
        selector = create_selector_agent()

        # Test input
        test_task = "Design a recommendation system for an e-commerce platform"

        # Execute
        result = await selector.arun(
            {
                "available_modules": DEFAULT_REASONING_MODULES,
                "task_description": test_task,
                "system_message": "You are an expert at selecting reasoning strategies.",
            }
        )

        # Verify result structure
        assert isinstance(result, dict)

        # Check if we got the structured output
        if "task_summary" in result:
            assert result["task_summary"]
            assert "selected_modules" in result
            assert len(result["selected_modules"]) >= 3
            assert len(result["selected_modules"]) <= 5

            # Verify module structure
            for module in result["selected_modules"]:
                assert "module_number" in module
                assert "module_name" in module
                assert "relevance_explanation" in module
                assert "contribution" in module

    @pytest.mark.asyncio
    async def test_adapter_agent_formats_modules(self):
        """Test adapter agent with formatted module input."""
        # Create test modules
        test_modules = ModuleSelectionResult(
            task_summary="Design a recommendation system",
            selected_modules=[
                SelectedModule(
                    module_number=2,
                    module_name="Systems Analysis",
                    relevance_explanation="Understand system components",
                    contribution="Map out the recommendation engine architecture",
                ),
                SelectedModule(
                    module_number=14,
                    module_name="Pattern Recognition",
                    relevance_explanation="Identify user behavior patterns",
                    contribution="Detect purchasing patterns for recommendations",
                ),
            ],
            selection_rationale="Selected modules for system design and pattern analysis",
        )

        # Create adapter
        adapter = create_adapter_agent()

        # Execute with formatted input
        result = await adapter.arun(
            {
                "selected_modules_formatted": test_modules.format_for_adapter(),
                "system_message": "You are an expert at customizing reasoning strategies.",
            }
        )

        # Verify result
        assert isinstance(result, dict)
        if "adapted_modules" in result:
            assert len(result["adapted_modules"]) > 0
            for module in result["adapted_modules"]:
                assert "module_number" in module
                assert "adapted_description" in module
                assert "application_strategy" in module

    @pytest.mark.asyncio
    async def test_full_sequential_workflow(self):
        """Test the complete sequential workflow with real execution."""
        # Create the full workflow
        self_discover = create_self_discover_sequential()

        # Test task
        task = "How can I reduce food waste in my restaurant?"

        # Initial state with all required fields
        initial_state = {
            "available_modules": DEFAULT_REASONING_MODULES,
            "task_description": task,
            "selected_modules_formatted": "",
            "adapted_modules_formatted": "",
            "reasoning_plan_formatted": "",
            "system_message": "You are a helpful assistant.",
        }

        # Execute
        result = await self_discover.arun(initial_state)

        # Verify we got a result
        assert result is not None

        # The result should contain the final execution
        if isinstance(result, dict):
            # Check for final answer or execution result
            possible_keys = ["final_answer", "answer", "output", "execution_result"]
            found_answer = False
            for key in possible_keys:
                if result.get(key):
                    found_answer = True
                    break

            assert (
                found_answer
            ), f"No final answer found in result keys: {list(result.keys())}"


class TestPydanticModels:
    """Test Pydantic model validation and formatting."""

    def test_module_selection_validation(self):
        """Test ModuleSelectionResult validation."""
        # Valid case
        valid_selection = ModuleSelectionResult(
            task_summary="Test task",
            selected_modules=[
                SelectedModule(
                    module_number=1,
                    module_name="Critical Thinking",
                    relevance_explanation="Needed for analysis",
                    contribution="Will help analyze the problem",
                ),
                SelectedModule(
                    module_number=2,
                    module_name="Systems Analysis",
                    relevance_explanation="Break down complexity",
                    contribution="Identify system components",
                ),
                SelectedModule(
                    module_number=3,
                    module_name="Root Cause Analysis",
                    relevance_explanation="Find underlying issues",
                    contribution="Determine root causes",
                ),
            ],
            selection_rationale="Selected for comprehensive analysis",
        )

        assert len(valid_selection.selected_modules) == 3

        # Test formatting
        formatted = valid_selection.format_for_adapter()
        assert "TASK:" in formatted
        assert "SELECTED MODULES:" in formatted
        assert "1. Critical Thinking" in formatted

    def test_module_selection_validation_errors(self):
        """Test validation errors for module selection."""
        # Too few modules
        with pytest.raises(ValueError, match="At least 3 modules"):
            ModuleSelectionResult(
                task_summary="Test",
                selected_modules=[
                    SelectedModule(
                        module_number=1,
                        module_name="Test",
                        relevance_explanation="Test",
                        contribution="Test",
                    )
                ],
                selection_rationale="Test",
            )

        # Too many modules
        with pytest.raises(ValueError, match="Maximum 5 modules"):
            ModuleSelectionResult(
                task_summary="Test",
                selected_modules=[
                    SelectedModule(
                        module_number=i,
                        module_name=f"Module {i}",
                        relevance_explanation="Test",
                        contribution="Test",
                    )
                    for i in range(1, 7)  # 6 modules
                ],
                selection_rationale="Test",
            )

    def test_reasoning_structure_validation(self):
        """Test ReasoningStructure validation."""
        from haive.agents.reasoning_and_critique.self_discover.self_discover_sequential_v2 import (
            ReasoningStep,
        )

        # Valid structure
        structure = ReasoningStructure(
            steps=[
                ReasoningStep(
                    step_number=1,
                    description="Analyze the problem",
                    modules_used=[1, 2],
                    expected_output="Problem analysis",
                ),
                ReasoningStep(
                    step_number=2,
                    description="Generate solutions",
                    modules_used=[3, 4],
                    expected_output="Solution options",
                ),
            ]
        )

        assert len(structure.steps) == 2

        # Test formatting
        formatted = structure.format_for_executor()
        assert "REASONING PLAN:" in formatted
        assert "Step 1:" in formatted
        assert "Using modules: [1, 2]" in formatted

    def test_reasoning_structure_step_numbering(self):
        """Test that steps must be sequentially numbered."""
        from haive.agents.reasoning_and_critique.self_discover.self_discover_sequential_v2 import (
            ReasoningStep,
        )

        # Incorrect numbering
        with pytest.raises(ValueError, match="incorrect number"):
            ReasoningStructure(
                steps=[
                    ReasoningStep(
                        step_number=1,
                        description="Step 1",
                        modules_used=[],
                        expected_output="Output 1",
                    ),
                    ReasoningStep(
                        step_number=3,  # Wrong number!
                        description="Step 3",
                        modules_used=[],
                        expected_output="Output 3",
                    ),
                ]
            )
