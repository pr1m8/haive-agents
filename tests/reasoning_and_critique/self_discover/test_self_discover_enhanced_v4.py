"""Test Self-Discover Enhanced V4 implementation with real LLMs."""

import pytest

from haive.agents.reasoning_and_critique.self_discover.self_discover_enhanced_v4 import (
    DEFAULT_REASONING_MODULES,
    AdaptedModulesOutput,
    FinalAnswerOutput,
    ModuleSelectionOutput,
    ReasoningPlanOutput,
    SelfDiscoverAdapter,
    SelfDiscoverExecutor,
    SelfDiscoverSelector,
    SelfDiscoverStructurer,
    run_self_discover_workflow,
)


class TestSelfDiscoverAgents:
    """Test individual Self-Discover agents with real LLMs."""

    @pytest.mark.asyncio
    async def test_selector_agent(self):
        """Test the selector agent independently."""
        selector = SelfDiscoverSelector()

        # Test task
        task = "How can I improve my memory for studying?"

        # Run selector
        result = await selector.arun(
            {
                "task": task,
                "available_modules": DEFAULT_REASONING_MODULES,
                "system_message": selector.engine.system_message,
            }
        )

        # Verify result
        assert isinstance(result, dict)
        assert "selected_modules" in result or "modules" in result or "output" in result

        # If we got structured output, verify it
        if "selected_modules" in result:
            assert isinstance(result["selected_modules"], list)
            assert len(result["selected_modules"]) >= 3
            assert len(result["selected_modules"]) <= 5

            # Check structure of each module
            for module in result["selected_modules"]:
                assert "number" in module or "module_number" in module
                assert "name" in module or "module_name" in module
                assert "reason" in module or "explanation" in module

    @pytest.mark.asyncio
    async def test_adapter_agent(self):
        """Test the adapter agent with pre-selected modules."""
        adapter = SelfDiscoverAdapter()

        # Mock selected modules output
        selected_modules = """SELECTED MODULES:

1. Pattern Recognition
   Reason: Helps identify memory patterns

2. Systems Analysis  
   Reason: Break down memory systems

3. Optimization
   Reason: Find best memory techniques"""

        # Run adapter
        result = await adapter.arun(
            {
                "task": "How can I improve my memory for studying?",
                "selected_modules": selected_modules,
                "system_message": adapter.engine.system_message,
            }
        )

        # Verify result
        assert isinstance(result, dict)
        assert "adapted_modules" in result or "adapted" in result or "output" in result

        if "adapted_modules" in result:
            assert isinstance(result["adapted_modules"], list)
            assert len(result["adapted_modules"]) > 0

            for module in result["adapted_modules"]:
                assert "strategy" in module

    @pytest.mark.asyncio
    async def test_structurer_agent(self):
        """Test the structurer agent with adapted modules."""
        structurer = SelfDiscoverStructurer()

        # Mock adapted modules
        adapted_modules = """ADAPTED MODULES:

1. Pattern Recognition
   Strategy: Identify your learning patterns and memory strengths

2. Systems Analysis
   Strategy: Analyze your current study system and memory techniques

3. Optimization  
   Strategy: Optimize study schedule and memory techniques"""

        # Run structurer
        result = await structurer.arun(
            {
                "task": "How can I improve my memory for studying?",
                "adapted_modules": adapted_modules,
                "system_message": structurer.engine.system_message,
            }
        )

        # Verify result
        assert isinstance(result, dict)
        assert "steps" in result or "plan" in result or "output" in result

        if "steps" in result:
            assert isinstance(result["steps"], list)
            assert len(result["steps"]) > 0

            for step in result["steps"]:
                assert "action" in step

    @pytest.mark.asyncio
    async def test_executor_agent(self):
        """Test the executor agent with a plan."""
        executor = SelfDiscoverExecutor()

        # Mock reasoning plan
        reasoning_plan = """REASONING PLAN:

Step 1: Analyze current memory techniques
   Using modules: [2]

Step 2: Identify memory patterns
   Using modules: [1]
   
Step 3: Develop optimized techniques
   Using modules: [3]"""

        # Run executor
        result = await executor.arun(
            {
                "task": "How can I improve my memory for studying?",
                "reasoning_plan": reasoning_plan,
                "system_message": executor.engine.system_message,
            }
        )

        # Verify result
        assert isinstance(result, dict)
        assert "answer" in result or "output" in result

        if "answer" in result:
            assert len(result["answer"]) > 0
            assert "reasoning_process" in result or "reasoning" in result


class TestSelfDiscoverWorkflow:
    """Test the complete Self-Discover workflow."""

    @pytest.mark.asyncio
    async def test_simple_shape_task(self):
        """Test with a simple shape recognition task."""
        task = """What shape has these properties:
- 4 equal sides
- 4 right angles (90 degrees each)
- Opposite sides are parallel
- All angles add up to 360 degrees"""

        result = await run_self_discover_workflow(task)

        assert isinstance(result, dict)
        assert "answer" in result

        # Should identify it as a square
        answer = result["answer"].lower()
        assert "square" in answer

        # Check confidence if provided
        if "confidence" in result:
            assert result["confidence"] in ["HIGH", "MEDIUM", "LOW"]

    @pytest.mark.asyncio
    async def test_problem_solving_task(self):
        """Test with a problem-solving task."""
        task = "What are effective strategies for reducing procrastination?"

        result = await run_self_discover_workflow(task)

        assert isinstance(result, dict)
        assert "answer" in result
        assert len(result["answer"]) > 50  # Should have substantial answer

        # Should mention some strategies
        answer = result["answer"].lower()
        # At least one of these concepts should appear
        strategies = [
            "break",
            "task",
            "schedule",
            "time",
            "goal",
            "focus",
            "reward",
            "deadline",
        ]
        assert any(strategy in answer for strategy in strategies)

    @pytest.mark.asyncio
    async def test_analytical_task(self):
        """Test with an analytical task."""
        task = """Analyze the following data pattern and predict the next number:
2, 4, 8, 16, 32, ?"""

        result = await run_self_discover_workflow(task)

        assert isinstance(result, dict)
        assert "answer" in result

        # Should identify the pattern (doubling) and predict 64
        answer = result["answer"]
        assert "64" in answer or "sixty-four" in answer.lower()

    @pytest.mark.asyncio
    async def test_custom_modules(self):
        """Test with custom reasoning modules."""
        task = "How can I start a successful small business?"

        custom_modules = """1. Market Research - Analyze market needs and competition
2. Financial Planning - Budget and financial projections
3. Risk Assessment - Identify and mitigate risks
4. Customer Analysis - Understand target customers
5. Strategic Planning - Long-term business strategy"""

        result = await run_self_discover_workflow(task, modules=custom_modules)

        assert isinstance(result, dict)
        assert "answer" in result

        # Should use business-related concepts
        answer = result["answer"].lower()
        business_terms = ["market", "customer", "financial", "plan", "strategy", "risk"]
        assert any(term in answer for term in business_terms)


class TestOutputModels:
    """Test the Pydantic output models."""

    def test_module_selection_output(self):
        """Test ModuleSelectionOutput model and formatting."""
        output = ModuleSelectionOutput(
            selected_modules=[
                {
                    "number": "1",
                    "name": "Pattern Recognition",
                    "reason": "Identify patterns",
                },
                {"number": "2", "name": "Logic", "reason": "Apply logic"},
                {"number": "3", "name": "Analysis", "reason": "Analyze problem"},
            ]
        )

        # Test formatting
        formatted = output.format_as_text()
        assert "SELECTED MODULES:" in formatted
        assert "1. Pattern Recognition" in formatted
        assert "Reason: Identify patterns" in formatted

    def test_adapted_modules_output(self):
        """Test AdaptedModulesOutput model."""
        output = AdaptedModulesOutput(
            adapted_modules=[
                {
                    "number": "1",
                    "name": "Pattern Recognition",
                    "strategy": "Look for visual patterns",
                },
                {
                    "number": "2",
                    "name": "Logic",
                    "strategy": "Apply deductive reasoning",
                },
            ]
        )

        formatted = output.format_as_text()
        assert "ADAPTED MODULES:" in formatted
        assert "Strategy: Look for visual patterns" in formatted

    def test_reasoning_plan_output(self):
        """Test ReasoningPlanOutput model."""
        output = ReasoningPlanOutput(
            steps=[
                {"action": "Analyze the problem", "modules": ["1", "2"]},
                {"action": "Generate solutions", "modules": ["3"]},
                {"action": "Evaluate options"},
            ]
        )

        formatted = output.format_as_text()
        assert "REASONING PLAN:" in formatted
        assert "Step 1: Analyze the problem" in formatted
        assert "Using modules: ['1', '2']" in formatted

    def test_final_answer_output(self):
        """Test FinalAnswerOutput model."""
        output = FinalAnswerOutput(
            answer="The answer is 42",
            reasoning_process="Step 1: Analyzed... Step 2: Calculated...",
            confidence="HIGH",
        )

        assert output.answer == "The answer is 42"
        assert output.confidence == "HIGH"
        assert "Step 1:" in output.reasoning_process
