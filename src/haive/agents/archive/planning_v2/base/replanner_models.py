"""Models for the replanner component.

This module contains the Answer and Response models used by the replanner
to return either a final answer or a new plan.
"""

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field


class Answer(BaseModel):
    """Simple answer response model.

    Used when the replanner determines that the objective has been
    completed and can provide a final answer.
    """

    content: str = Field(..., description="The answer content")
    confidence: float = Field(
        default=1.0, ge=0.0, le=1.0, description="Confidence score for the answer"
    )
    sources: list[str] = Field(
        default_factory=list, description="Sources used to generate the answer"
    )
    reasoning: str = Field(default="", description="Reasoning behind the answer")


# TypeVar for generic response model
T = TypeVar("T", bound=BaseModel)


class Response(BaseModel, Generic[T]):
    """Generic response model that can contain different response types.

    This model provides a flexible container for replanner outputs,
    supporting either an Answer response OR a Plan response.

    Examples:
        Answer response:
            Response[Union[Answer, Plan[Task]]](
                result=Answer(content="The task is complete"),
                response_type="answer"
            )

        Plan response:
            Response[Union[Answer, Plan[Task]]](
                result=Plan(objective="Continue with phase 2", steps=[...]),
                response_type="plan"
            )
    """

    result: T = Field(..., description="The response result - either Answer or Plan")
    response_type: str = Field(..., description="Type of response (answer/plan)")
    metadata: dict[str, Any] = Field(
        default_factory=dict, description="Additional metadata about the response"
    )
    reasoning: str = Field(
        default="", description="Reasoning for choosing this response type"
    )

    def is_answer(self) -> bool:
        """Check if this is an answer response."""
        return self.response_type.lower() == "answer"

    def is_plan(self) -> bool:
        """Check if this is a plan response."""
        return self.response_type.lower() == "plan"
