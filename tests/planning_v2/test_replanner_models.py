#!/usr/bin/env python3
"""Test the replanner models with Union types."""

from typing import Union

from haive.agents.planning_v2.base.models import Plan, Task
from haive.agents.planning_v2.base.replanner_models import Answer, Response


def test_answer_model():
    """Test Answer model creation."""
    answer = Answer(
        content="The REST API has been successfully built with authentication",
        confidence=0.95,
        sources=["Step 1 completion", "Step 2 validation"],
        reasoning="All required tasks have been completed successfully"
    )

    assert answer.content == "The REST API has been successfully built with authentication"
    assert answer.confidence == 0.95
    assert len(answer.sources) == 2
    print("✅ Answer model works correctly")


def test_response_with_answer():
    """Test Response model with Answer."""
    answer = Answer(
        content="Task completed successfully",
        confidence=0.9
    )

    response = Response[Union[Answer, Plan[Task]]](
        result=answer,
        response_type="answer",
        reasoning="All objectives have been met"
    )

    assert response.is_answer()
    assert not response.is_plan()
    assert isinstance(response.result, Answer)
    print("✅ Response[Union[Answer, Plan[Task]]] with Answer works")


def test_response_with_plan():
    """Test Response model with Plan."""
    plan = Plan[Task](
        objective="Continue API development",
        steps=[
            Task(objective="Add error handling"),
            Task(objective="Implement rate limiting")
        ]
    )

    response = Response[Union[Answer, Plan[Task]]](
        result=plan,
        response_type="plan",
        reasoning="Additional features needed"
    )

    assert response.is_plan()
    assert not response.is_answer()
    assert isinstance(response.result, Plan)
    print("✅ Response[Union[Answer, Plan[Task]]] with Plan works")


def test_response_type_checking():
    """Test that Response properly handles Union type checking."""
    # This should work with either Answer or Plan
    ResponseType = Response[Union[Answer, Plan[Task]]]

    # Test with Answer
    answer_response = ResponseType(
        result=Answer(content="Done"),
        response_type="answer"
    )

    # Test with Plan
    plan_response = ResponseType(
        result=Plan[Task](objective="Do more", steps=[]),
        response_type="plan"
    )

    # Both should be valid
    assert isinstance(answer_response.result, (Answer, Plan))
    assert isinstance(plan_response.result, (Answer, Plan))

    print("✅ Response Union type checking works correctly")


if __name__ == "__main__":
    test_answer_model()
    test_response_with_answer()
    test_response_with_plan()
    test_response_type_checking()

    print("\n🎉 All replanner model tests passed!")
    print("\nUsage pattern for replanner:")
    print("  ResponseType = Response[Union[Answer, Plan[Task]]]")
    print("  - Use for structured output model")
    print("  - Replanner returns either Answer or new Plan")
    print("  - Check with response.is_answer() or response.is_plan()")
