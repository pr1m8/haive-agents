"""Tests for JoinStep - Auto DAG detection and parallelization."""

import contextlib

from haive.agents.planning.rewoo.models.join_step import JoinStep, JoinStrategy
from haive.agents.planning.rewoo.models.plans import ExecutionPlan
from haive.agents.planning.rewoo.models.steps import BasicStep


class TestJoinStep:
    """Test suite for JoinStep functionality."""

    def test_basic_join_step_creation(self) -> None:
        """Test creating a basic join step."""
        step1 = BasicStep(description="First parallel step")
        step2 = BasicStep(description="Second parallel step")

        join_step = JoinStep(
            description="Join two parallel branches",
            depends_on=[step1.id, step2.id],
            join_strategy=JoinStrategy.WAIT_ALL,
        )

        assert join_step.is_join_point
        assert join_step.parallel_branch_count == 2
        assert join_step.join_complexity == "simple_parallel"
        assert join_step.join_strategy == JoinStrategy.WAIT_ALL

    def test_auto_detection_on_init(self) -> None:
        """Test automatic detection during initialization."""
        deps = ["step_1", "step_2", "step_3"]

        join_step = JoinStep(description="Auto-detected join", depends_on=deps)

        # Should auto-detect parallel structure
        assert join_step.parallel_inputs == deps
        assert join_step.join_metadata["auto_detected"]
        assert join_step.join_metadata["parallel_inputs"] == deps
        assert join_step.join_function is not None

    def test_computed_fields(self) -> None:
        """Test computed fields are calculated correctly."""
        # Test sequential (single dependency)
        sequential = JoinStep(description="Sequential step", depends_on=["step_1"])
        assert not sequential.is_join_point
        assert sequential.parallel_branch_count == 1
        assert sequential.join_complexity == "sequential"

        # Test simple parallel
        simple_parallel = JoinStep(
            description="Simple parallel", depends_on=["step_1", "step_2"]
        )
        assert simple_parallel.is_join_point
        assert simple_parallel.parallel_branch_count == 2
        assert simple_parallel.join_complexity == "simple_parallel"

        # Test complex parallel
        complex_parallel = JoinStep(
            description="Complex parallel",
            depends_on=[f"step_{i}" for i in range(1, 8)],
        )
        assert complex_parallel.join_complexity == "complex_parallel"
        assert complex_parallel.parallel_branch_count == 7

    def test_join_strategies(self) -> None:
        """Test different join strategies."""
        deps = ["step_1", "step_2", "step_3"]

        # Test WAIT_ALL
        wait_all = JoinStep(
            description="Wait all", depends_on=deps, join_strategy=JoinStrategy.WAIT_ALL
        )
        assert not wait_all.can_execute(set())
        assert not wait_all.can_execute({"step_1"})
        assert not wait_all.can_execute({"step_1", "step_2"})
        assert wait_all.can_execute({"step_1", "step_2", "step_3"})

        # Test WAIT_ANY
        wait_any = JoinStep(
            description="Wait any", depends_on=deps, join_strategy=JoinStrategy.WAIT_ANY
        )
        assert not wait_any.can_execute(set())
        assert wait_any.can_execute({"step_1"})
        assert wait_any.can_execute({"step_1", "step_2"})

        # Test WAIT_MAJORITY
        wait_majority = JoinStep(
            description="Wait majority",
            depends_on=deps,
            join_strategy=JoinStrategy.WAIT_MAJORITY,
        )
        assert not wait_majority.can_execute(set())
        assert not wait_majority.can_execute({"step_1"})
        assert wait_majority.can_execute({"step_1", "step_2"})  # 2/3 is majority
        assert wait_majority.can_execute({"step_1", "step_2", "step_3"})

    def test_estimated_wait_time(self) -> None:
        """Test wait time estimation."""
        # More branches should generally mean longer wait time for WAIT_ALL
        simple_join = JoinStep(
            description="Simple",
            depends_on=["step_1", "step_2"],
            join_strategy=JoinStrategy.WAIT_ALL,
        )

        complex_join = JoinStep(
            description="Complex",
            depends_on=[f"step_{i}" for i in range(1, 6)],
            join_strategy=JoinStrategy.WAIT_ALL,
        )

        assert complex_join.estimated_wait_time > simple_join.estimated_wait_time

        # WAIT_ANY should be faster than WAIT_ALL
        wait_any_join = JoinStep(
            description="Wait any",
            depends_on=["step_1", "step_2", "step_3"],
            join_strategy=JoinStrategy.WAIT_ANY,
        )

        wait_all_join = JoinStep(
            description="Wait all",
            depends_on=["step_1", "step_2", "step_3"],
            join_strategy=JoinStrategy.WAIT_ALL,
        )

        assert wait_any_join.estimated_wait_time < wait_all_join.estimated_wait_time

    def test_optimization_detection(self) -> None:
        """Test optimization opportunity detection."""
        # Small joins shouldn't suggest optimization
        small_join = JoinStep(
            description="Small join",
            depends_on=["step_1", "step_2"],
            join_strategy=JoinStrategy.WAIT_ALL,
        )
        assert not small_join.can_optimize_parallel

        # Large joins with WAIT_ANY should suggest optimization
        large_join = JoinStep(
            description="Large join",
            depends_on=[f"step_{i}" for i in range(1, 5)],
            join_strategy=JoinStrategy.WAIT_ANY,
        )
        assert large_join.can_optimize_parallel

    def test_join_function_suggestions(self) -> None:
        """Test automatic join function suggestions."""
        # Single dependency should suggest passthrough
        single = JoinStep(description="Single", depends_on=["step_1"])
        assert single.join_function == "passthrough"

        # Two dependencies should suggest merge_two
        two_deps = JoinStep(description="Two deps", depends_on=["step_1", "step_2"])
        assert two_deps.join_function == "merge_two"

        # Multiple dependencies should suggest merge_multiple
        multi_deps = JoinStep(
            description="Multi deps", depends_on=["step_1", "step_2", "step_3"]
        )
        assert multi_deps.join_function == "merge_multiple"

        # Many dependencies should suggest reduce_complex
        many_deps = JoinStep(
            description="Many deps", depends_on=[f"step_{i}" for i in range(1, 8)]
        )
        assert many_deps.join_function == "reduce_complex"

    def test_execution_with_different_strategies(self) -> None:
        """Test execution with different join strategies."""
        join_step = JoinStep(
            description="Test execution",
            depends_on=["step_1", "step_2"],
            join_strategy=JoinStrategy.WAIT_ALL,
            join_function="merge_two",
        )

        # Should be able to execute when all dependencies complete
        context = {
            "completed_steps": {"step_1", "step_2"},
            "step_results": {
                "step_1": "Result from step 1",
                "step_2": "Result from step 2",
            },
        }

        result = join_step.execute(context)
        assert result is not None
        assert join_step.parallel_results["step_1"] == "Result from step 1"
        assert join_step.parallel_results["step_2"] == "Result from step 2"

    def test_dependency_analysis(self) -> None:
        """Test dependency pattern analysis."""
        # Create a set of steps with complex dependencies
        step1 = BasicStep(description="Independent 1")
        step2 = BasicStep(description="Independent 2")
        step3 = BasicStep(description="Depends on 1", depends_on=[step1.id])

        join_step = JoinStep(
            description="Join independent branches",
            depends_on=[step1.id, step2.id, step3.id],
        )

        all_steps = [step1, step2, step3, join_step]
        analysis = join_step.analyze_dependency_patterns(all_steps)

        assert "dependency_depth" in analysis
        assert "fan_in_degree" in analysis
        assert analysis["fan_in_degree"] == 3
        assert "parallel_opportunities" in analysis
        assert "suggested_optimizations" in analysis

    def test_factory_method(self) -> None:
        """Test factory method for creating join steps."""
        join_step = JoinStep.create_auto_join(
            description="Auto-created join",
            dependencies=["step_1", "step_2", "step_3"],
            strategy=JoinStrategy.WAIT_MAJORITY,
        )

        assert join_step.join_strategy == JoinStrategy.WAIT_MAJORITY
        assert join_step.depends_on == ["step_1", "step_2", "step_3"]
        assert join_step.join_metadata["auto_detected"]

    def test_get_join_info(self) -> None:
        """Test comprehensive join information."""
        join_step = JoinStep(
            description="Info test",
            depends_on=["step_1", "step_2", "step_3"],
            join_strategy=JoinStrategy.WAIT_ALL,
        )

        info = join_step.get_join_info()

        required_keys = [
            "step_id",
            "description",
            "join_strategy",
            "is_join_point",
            "parallel_branch_count",
            "join_complexity",
            "estimated_wait_time",
            "can_optimize_parallel",
            "parallel_inputs",
            "join_metadata",
        ]

        for key in required_keys:
            assert key in info

        assert info["is_join_point"]
        assert info["parallel_branch_count"] == 3
        assert info["join_complexity"] == "simple_parallel"


class TestJoinStepDAGAnalysis:
    """Test DAG-wide analysis methods."""

    def test_dag_structure_analysis(self) -> None:
        """Test analysis of entire DAG structure."""
        # Create a complex DAG
        step1 = BasicStep(description="Start 1")
        step2 = BasicStep(description="Start 2")
        step3 = BasicStep(description="Process 1", depends_on=[step1.id])
        step4 = BasicStep(description="Process 2", depends_on=[step2.id])

        # This step joins two parallel branches
        join_step = JoinStep(
            description="Join parallel branches", depends_on=[step3.id, step4.id]
        )

        # This step has multiple dependencies but isn't a JoinStep
        final_step = BasicStep(
            description="Final step", depends_on=[step1.id, step2.id, join_step.id]
        )

        all_steps = [step1, step2, step3, step4, join_step, final_step]
        analysis = JoinStep.analyze_dag_structure(all_steps)

        assert analysis["total_steps"] == 6
        assert analysis["existing_join_points"] == 1  # Only join_step
        assert analysis["potential_join_points"] == 1  # final_step
        assert len(analysis["suggested_conversions"]) >= 1
        assert "dag_complexity" in analysis
        assert "parallelization_score" in analysis

    def test_dag_complexity_calculation(self) -> None:
        """Test DAG complexity classification."""
        # Linear structure
        linear_steps = [
            BasicStep(description="Step 1"),
            BasicStep(description="Step 2", depends_on=["step_1"]),
            BasicStep(description="Step 3", depends_on=["step_2"]),
        ]
        linear_complexity = JoinStep._calculate_dag_complexity(linear_steps)
        assert linear_complexity in ["linear", "simple_dag"]

        # Complex structure
        complex_steps = []
        for i in range(5):
            deps = [f"step_{j}" for j in range(max(0, i - 2), i)]
            complex_steps.append(BasicStep(description=f"Step {i}", depends_on=deps))

        complex_complexity = JoinStep._calculate_dag_complexity(complex_steps)
        assert complex_complexity in ["moderate_dag", "complex_dag"]

    def test_parallelization_score(self) -> None:
        """Test parallelization benefit scoring."""
        # No parallelization opportunity
        sequential_steps = [
            BasicStep(description="Step 1"),
            BasicStep(description="Step 2", depends_on=["step_1"]),
        ]
        seq_score = JoinStep._calculate_parallelization_score(sequential_steps)
        assert seq_score == 0.0

        # Some parallelization opportunity
        parallel_steps = [
            BasicStep(description="Step 1"),
            BasicStep(description="Step 2"),
            JoinStep(description="Join", depends_on=["step_1", "step_2"]),
        ]
        par_score = JoinStep._calculate_parallelization_score(parallel_steps)
        assert par_score > 0.0


class TestJoinStepIntegration:
    """Test JoinStep integration with ExecutionPlan."""

    def test_join_steps_in_execution_plan(self) -> None:
        """Test JoinSteps work properly in ExecutionPlan."""
        # Create parallel branches
        step1 = BasicStep(description="Parallel branch 1")
        step2 = BasicStep(description="Parallel branch 2")

        # Join the branches
        join_step = JoinStep(
            description="Join parallel work",
            depends_on=[step1.id, step2.id],
            join_strategy=JoinStrategy.WAIT_ALL,
        )

        # Final step after join
        final_step = BasicStep(
            description="Final processing", depends_on=[join_step.id]
        )

        plan = ExecutionPlan(
            name="Join Step Plan",
            description="Plan demonstrating join steps",
            steps=[step1, step2, join_step, final_step],
        )

        assert plan.step_count == 4
        assert plan.max_parallelism == 2  # step1 and step2 can run in parallel
        assert len(plan.execution_levels) == 3

        # Check execution levels
        assert set(plan.execution_levels[0]) == {step1.id, step2.id}
        assert plan.execution_levels[1] == [join_step.id]
        assert plan.execution_levels[2] == [final_step.id]

    def test_complex_dag_with_multiple_joins(self) -> None:
        """Test complex DAG with multiple join points."""
        # Create initial parallel work
        init1 = BasicStep(description="Init 1")
        init2 = BasicStep(description="Init 2")
        init3 = BasicStep(description="Init 3")

        # First join point
        join1 = JoinStep(
            description="First join",
            depends_on=[init1.id, init2.id],
            join_strategy=JoinStrategy.WAIT_ALL,
        )

        # Second join point
        join2 = JoinStep(
            description="Second join",
            depends_on=[init3.id, join1.id],
            join_strategy=JoinStrategy.WAIT_ALL,
        )

        # Final step
        final = BasicStep(description="Final", depends_on=[join2.id])

        plan = ExecutionPlan(
            name="Multi-Join Plan",
            description="Plan with multiple join points",
            steps=[init1, init2, init3, join1, join2, final],
        )

        assert plan.step_count == 6
        assert plan.max_parallelism == 3  # init1, init2, init3 can run in parallel

        # Verify execution levels make sense
        level_0 = set(plan.execution_levels[0])
        assert level_0 == {init1.id, init2.id, init3.id}


if __name__ == "__main__":
    # Run basic tests without pytest

    # Test basic join creation
    with contextlib.suppress(Exception):
        join_step = JoinStep(
            description="Test join with auto-detection",
            depends_on=["step_1", "step_2", "step_3"],
        )

    # Test join strategies
    with contextlib.suppress(Exception):
        wait_any = JoinStep(
            description="Wait any strategy",
            depends_on=["step_1", "step_2"],
            join_strategy=JoinStrategy.WAIT_ANY,
        )

    # Test DAG analysis
    try:
        steps = [
            BasicStep(description="Start 1"),
            BasicStep(description="Start 2"),
            JoinStep(description="Join", depends_on=["start_1", "start_2"]),
        ]

        analysis = JoinStep.analyze_dag_structure(steps)

    except Exception:
        pass
