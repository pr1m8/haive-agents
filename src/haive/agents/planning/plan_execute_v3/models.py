"""Plan-and-Execute V3 Models - Structured Output Models for the agent.

Based on the Plan-and-Execute methodology where planning and execution
are separated into distinct phases with structured outputs.
"""

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, field_validator, model_validator


class StepStatus(str, Enum):
    """Status of a plan step."""

    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"


class PlanStep(BaseModel):
    """Individual step in an execution plan."""

    step_id: int = Field(description="Unique identifier for this step (1-based)")
    description: str = Field(
        description="Clear, actionable description of what needs to be done"
    )
    expected_output: str = Field(description="What we expect to achieve from this step")
    dependencies: list[int] = Field(
        default_factory=list,
        description="List of step IDs that must be completed before this step",
    )
    tools_required: list[str] = Field(
        default_factory=list, description="Tools that might be needed for this step"
    )
    status: StepStatus = Field(default=StepStatus.PENDING)
    result: str | None = None
    error: str | None = None
    execution_time: float | None = None

    @field_validator("dependencies")
    @classmethod
    def validate_dependencies(cls, v, info):
        """Ensure dependencies are valid step IDs."""
        if "step_id" in info.data:
            step_id = info.data["step_id"]
            invalid = [d for d in v if d >= step_id]
            if invalid:
                raise ValueError(
                    f"Dependencies {invalid} must be less than step_id {step_id}"
                )
        return v


class ExecutionPlan(BaseModel):
    """Complete execution plan with metadata."""

    objective: str = Field(description="The main objective this plan aims to achieve")
    steps: list[PlanStep] = Field(description="Ordered list of steps to execute")
    total_steps: int = Field(description="Total number of steps in the plan")
    created_at: datetime = Field(default_factory=datetime.now)
    reasoning: str = Field(
        description="Reasoning behind this plan structure and approach"
    )
    estimated_duration: str | None = Field(
        default=None, description="Rough estimate of how long the plan might take"
    )

    @model_validator(mode="after")
    def update_total_steps(self):
        """Ensure total_steps matches actual step count."""
        self.total_steps = len(self.steps)
        return self

    @field_validator("steps")
    @classmethod
    def validate_step_ids(cls, v):
        """Ensure step IDs are sequential starting from 1."""
        for i, step in enumerate(v, 1):
            if step.step_id != i:
                step.step_id = i
        return v

    def get_next_step(self) -> PlanStep | None:
        """Get the next step ready for execution."""
        completed_ids = {
            s.step_id for s in self.steps if s.status == StepStatus.COMPLETED
        }

        for step in self.steps:
            if step.status == StepStatus.PENDING:
                # Check if all dependencies are completed
                if all(dep_id in completed_ids for dep_id in step.dependencies):
                    return step
        return None

    def is_complete(self) -> bool:
        """Check if all steps are completed."""
        return all(
            s.status in [StepStatus.COMPLETED, StepStatus.SKIPPED] for s in self.steps
        )

    def has_failures(self) -> bool:
        """Check if any steps have failed."""
        return any(s.status == StepStatus.FAILED for s in self.steps)

    def get_progress_percentage(self) -> float:
        """Calculate completion percentage."""
        if self.total_steps == 0:
            return 0.0
        completed = sum(1 for s in self.steps if s.status == StepStatus.COMPLETED)
        return (completed / self.total_steps) * 100


class StepExecution(BaseModel):
    """Result from executing a single step."""

    step_id: int = Field(description="ID of the executed step")
    step_description: str = Field(description="Description of what was executed")
    result: str = Field(description="Detailed result from the execution")
    tools_used: list[str] = Field(
        default_factory=list, description="Tools that were actually used"
    )
    success: bool = Field(description="Whether execution was successful")
    error: str | None = Field(default=None, description="Error message if failed")
    execution_time: float = Field(description="Time taken in seconds")
    observations: str = Field(
        default="", description="Key observations from this step execution"
    )


class PlanEvaluation(BaseModel):
    """Evaluation of current plan progress and decision on next action."""

    current_progress: str = Field(
        description="Summary of what has been accomplished so far"
    )
    plan_status: str = Field(
        description="Overall status of the plan (on_track, needs_revision, completed, failed)"
    )
    decision: str = Field(
        description="Decision on next action: continue, replan, or finalize"
    )
    reasoning: str = Field(description="Detailed reasoning for the decision")
    final_answer: str | None = Field(
        default=None, description="Final answer if decision is 'finalize'"
    )
    revision_notes: str | None = Field(
        default=None, description="Notes for replanning if decision is 'replan'"
    )

    @model_validator(mode="after")
    def validate_decision_fields(self):
        """Ensure required fields are present based on decision."""
        if self.decision == "finalize" and not self.final_answer:
            raise ValueError("final_answer required when decision is 'finalize'")
        if self.decision == "replan" and not self.revision_notes:
            raise ValueError("revision_notes required when decision is 'replan'")
        return self


class RevisedPlan(BaseModel):
    """Revised execution plan based on evaluation."""

    original_objective: str = Field(description="The original objective (unchanged)")
    revision_reason: str = Field(description="Why the plan needed revision")
    retained_results: list[str] = Field(
        description="Key results from completed steps to retain"
    )
    new_plan: ExecutionPlan = Field(description="The revised plan moving forward")
    changes_made: str = Field(
        description="Summary of what changed from the original plan"
    )


class PlanExecuteInput(BaseModel):
    """Input format for the Plan-and-Execute agent."""

    objective: str = Field(description="The main goal or question to address")
    context: str | None = Field(
        default=None, description="Additional context or constraints"
    )
    max_steps: int = Field(
        default=10, description="Maximum number of steps allowed in the plan"
    )
    time_limit: int | None = Field(
        default=None, description="Time limit in seconds for execution"
    )


class PlanExecuteOutput(BaseModel):
    """Final output from the Plan-and-Execute agent."""

    objective: str = Field(description="The original objective")
    final_answer: str = Field(description="The comprehensive final answer")
    execution_summary: str = Field(description="Summary of the execution process")
    steps_completed: int = Field(description="Number of steps completed")
    total_steps: int = Field(description="Total number of steps planned")
    revisions_made: int = Field(description="Number of plan revisions")
    total_execution_time: float = Field(description="Total time in seconds")
    key_findings: list[str] = Field(description="Key findings from the execution")
    confidence_score: float = Field(
        description="Confidence in the final answer (0-1)", ge=0.0, le=1.0
    )
