"""Models for Plan and Execute Agent v2.
"""

from typing import Literal, Optional, Union

from pydantic import BaseModel, Field


class Step(BaseModel):
    """A step in the plan.
    """

    id: int = Field(..., description="Unique identifier for the step")
    description: str = Field(...,
     description="Description of what this step does")
    status: Literal["not_started", "in_progress", "complete"] = Field(
        default="not_started", description="Current status of the step"
    )
    result: Optional[str] = Field(
        default=None, description="Result of executing this step"
    )

    def add_result(self, result: str) -> None:
        """Add result and mark step as complete.
        """
        self.result = result
        self.status = "complete"

    def is_complete(self) -> bool:
        """Check if step is complete.
        """
        return self.status == "complete"


class Plan(BaseModel):
    """A plan containing steps to execute.
    """

    description: str = Field(...,
     description="Overall description of the plan")
    steps: list[Step] = Field(
        default_factory=list, description="List of steps in the plan"
    )
    status: Literal["not_started", "in_progress", "complete"] = Field(
        default="not_started", description="Overall status of the plan"
    )

    def update_status(self) -> None:
        """Update plan status based on step completion.
        """
        if all(step.is_complete() for step in self.steps):
            self.status = "complete"
        elif any(step.status == "in_progress" for step in self.steps):
            self.status = "in_progress"
        else:
            self.status = "not_started"

    def get_next_step(self -> Optional[Step]:
        """Get the next incomplete step.
        """
        for step in self.steps:
            if step.status in ["not_started", "in_progress"]:
                return step
        return None


class Response(BaseModel):
    """Final response to user.
    """

    response: str = Field(..., description="The final response to the user")


class Act(BaseModel):
    """Action to take - either respond or create new plan."""

    action: Union[Response, Plan] = Field(
        ...,
        description="Action to perform. Use Response for final answer, Plan for more steps.",
    )


class ExecutionResult(BaseModel):
    """Result of executing a step.
    """

    step_id: Optional[int] = Field(
        default=None, description="ID of the step that was executed"
    )
    result: str = Field(..., description="Result of the execution")
    step_completed: bool = Field(
        default=False, description="Whether the step is now complete"
    )


# Rebuild forward references
Step.model_rebuild()
Plan.model_rebuild()
Act.model_rebuild()
