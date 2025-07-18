"""
Basic tests for ReWOO planning models
"""

import pytest

from haive.agents.planning.rewoo.models.plans import ExecutionPlan
from haive.agents.planning.rewoo.models.steps import BasicStep


def test_basic_step_creation():
    """Test basic step creation and computed fields."""
    step = BasicStep(description="Test step")

    assert step.description == "Test step"
    assert step.id.startswith("step_")
    assert step.has_dependencies == False
    assert step.dependency_count == 0
    assert step.can_execute(set()) == True


def test_step_with_dependencies():
    """Test step with dependencies."""
    step1 = BasicStep(description="First step")
    step2 = BasicStep(description="Second step", depends_on=[step1.id])

    assert step2.has_dependencies == True
    assert step2.dependency_count == 1
    assert step2.can_execute(set()) == False
    assert step2.can_execute({step1.id}) == True


def test_execution_plan():
    """Test execution plan with computed fields."""
    step1 = BasicStep(description="First step")
    step2 = BasicStep(description="Second step", depends_on=[step1.id])

    plan = ExecutionPlan(
        name="Test Plan", description="A test plan", steps=[step1, step2]
    )

    assert plan.step_count == 2
    assert plan.has_dependencies == True
    assert plan.max_parallelism == 1
    assert len(plan.execution_levels) == 2
    assert plan.execution_levels[0] == [step1.id]
    assert plan.execution_levels[1] == [step2.id]


def test_parallel_execution():
    """Test parallel execution levels."""
    step1 = BasicStep(description="Step 1")
    step2 = BasicStep(description="Step 2")
    step3 = BasicStep(description="Step 3", depends_on=[step1.id, step2.id])

    plan = ExecutionPlan(
        name="Parallel Plan",
        description="A plan with parallel steps",
        steps=[step1, step2, step3],
    )

    assert plan.max_parallelism == 2
    assert len(plan.execution_levels) == 2
    assert set(plan.execution_levels[0]) == {step1.id, step2.id}
    assert plan.execution_levels[1] == [step3.id]


def test_circular_dependency_detection():
    """Test circular dependency detection."""
    step1 = BasicStep(description="Step 1", depends_on=["step_2"])
    step2 = BasicStep(description="Step 2", depends_on=["step_1"])

    # Override IDs to create circular dependency
    step1.id = "step_1"
    step2.id = "step_2"

    with pytest.raises(ValueError, match="Circular dependency detected"):
        ExecutionPlan(
            name="Circular Plan", description="This should fail", steps=[step1, step2]
        )


if __name__ == "__main__":
    # Run basic tests
    test_basic_step_creation()
    test_step_with_dependencies()
    test_execution_plan()
    test_parallel_execution()
    print("✅ All basic tests passed!")

    # Test circular dependency (should fail)
    try:
        test_circular_dependency_detection()
        print("❌ Circular dependency test failed - should have raised exception")
    except ValueError:
        print("✅ Circular dependency detection working!")
