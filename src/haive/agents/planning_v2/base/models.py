"""Data models for planning agents.

This module contains Pydantic models for planning agent configurations,
plans, steps, and other planning-related data structures.
"""

from enum import Enum
from typing import Generic, List, Optional, TypeVar, Union

from pydantic import BaseModel, Field, PrivateAttr, computed_field


class Status(str, Enum):
    """Status for tasks and plans."""

    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class Task(BaseModel):
    """Simple task model.

    Attributes:
        objective: What this task aims to accomplish
        result: The outcome of the task (None if not completed)
        status: Current status of the task
    """

    objective: str = Field(..., description="What this task aims to accomplish")
    result: Optional[str] = Field(None, description="The outcome of the task")
    status: Status = Field(Status.PENDING, description="Current task status")

    # Private auto-indexing
    _index: int = PrivateAttr(default=0)
    _parent_index: Optional[int] = PrivateAttr(default=None)


# Create a TypeVar for the step type
StepType = TypeVar("StepType", bound=Task)


class Plan(BaseModel, Generic[StepType]):
    """Generic plan model that can work with any step type.

    Supports both linear and tree/split structures.

    Attributes:
        objective: What this plan aims to accomplish
        steps: List of steps (can be Tasks or nested Plans)
        result: The outcome of the plan execution
        status: Current status of the plan
    """

    objective: str = Field(..., description="What this plan aims to accomplish")
    steps: List[Union[StepType, "Plan"]] = Field(
        default_factory=list, description="List of steps (can be tasks or nested plans)"
    )
    result: Optional[str] = Field(None, description="The outcome of the plan")
    status: Status = Field(Status.PENDING, description="Current plan status")

    # Private auto-indexing
    _index: int = PrivateAttr(default=0)
    _parent_index: Optional[int] = PrivateAttr(default=None)
    _next_index: int = PrivateAttr(default=1)

    def add_step(self, step: Union[StepType, "Plan"]) -> Union[StepType, "Plan"]:
        """Add a step with auto-indexing."""
        # Set the index
        if hasattr(step, "_index"):
            step._index = self._next_index
            step._parent_index = self._index

        self.steps.append(step)
        self._next_index += 1
        return step

    def add_parallel_steps(
        self, steps: List[Union[StepType, "Plan"]]
    ) -> List[Union[StepType, "Plan"]]:
        """Add multiple steps that can be executed in parallel (same parent index)."""
        parent_index = self._next_index

        for i, step in enumerate(steps):
            if hasattr(step, "_index"):
                step._index = parent_index + i
                step._parent_index = self._index
            self.steps.append(step)

        self._next_index = parent_index + len(steps)
        return steps

    def create_subplan(self, objective: str) -> "Plan":
        """Create a nested subplan for tree structures."""
        subplan = Plan[StepType](
            objective=objective, _index=self._next_index, _parent_index=self._index
        )
        self.steps.append(subplan)
        self._next_index += 1
        return subplan

    @computed_field
    @property
    def total_steps(self) -> int:
        """Total number of steps (including nested)."""
        count = 0
        for step in self.steps:
            if isinstance(step, Plan):
                count += step.total_steps
            else:
                count += 1
        return count

    @computed_field
    @property
    def completed_steps(self) -> List[Union[StepType, "Plan"]]:
        """List of completed steps."""
        completed = []
        for step in self.steps:
            if isinstance(step, Plan):
                if step.status == Status.COMPLETED:
                    completed.append(step)
            elif step.status == Status.COMPLETED:
                completed.append(step)
        return completed

    @computed_field
    @property
    def completed_count(self) -> int:
        """Number of completed steps."""
        count = 0
        for step in self.steps:
            if isinstance(step, Plan):
                count += step.completed_count
            elif step.status == Status.COMPLETED:
                count += 1
        return count

    @computed_field
    @property
    def current_step(self) -> Optional[Union[StepType, "Plan"]]:
        """The current step being executed (first in_progress or pending)."""
        for step in self.steps:
            if step.status == Status.IN_PROGRESS:
                return step
            elif isinstance(step, Plan) and step.status == Status.IN_PROGRESS:
                # Check nested plan for current step
                nested_current = step.current_step
                if nested_current:
                    return nested_current

        # If no in_progress, return first pending
        for step in self.steps:
            if step.status == Status.PENDING:
                return step
            elif isinstance(step, Plan) and step.status == Status.PENDING:
                nested_current = step.current_step
                if nested_current:
                    return nested_current

        return None

    @computed_field
    @property
    def steps_remaining(self) -> List[Union[StepType, "Plan"]]:
        """List of steps that haven't been completed yet."""
        remaining = []
        for step in self.steps:
            if step.status in [Status.PENDING, Status.IN_PROGRESS]:
                remaining.append(step)
            elif step.status == Status.FAILED:
                remaining.append(step)  # Failed steps might need retry
        return remaining

    @computed_field
    @property
    def remaining_count(self) -> int:
        """Number of steps remaining."""
        return self.total_steps - self.completed_count

    @computed_field
    @property
    def progress_percentage(self) -> float:
        """Percentage of completion (0-100)."""
        if self.total_steps == 0:
            return 0.0
        return (self.completed_count / self.total_steps) * 100

    @computed_field
    @property
    def failed_steps(self) -> List[Union[StepType, "Plan"]]:
        """List of failed steps."""
        failed = []
        for step in self.steps:
            if isinstance(step, Plan):
                failed.extend(step.failed_steps)
            elif step.status == Status.FAILED:
                failed.append(step)
        return failed

    @computed_field
    @property
    def is_complete(self) -> bool:
        """Whether all steps are completed."""
        return self.remaining_count == 0 and len(self.failed_steps) == 0

    @computed_field
    @property
    def has_failures(self) -> bool:
        """Whether any steps have failed."""
        return len(self.failed_steps) > 0


# Enable forward reference
Plan.model_rebuild()
