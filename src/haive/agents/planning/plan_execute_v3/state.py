"""State schema for Plan-and-Execute V3 Agent.

This module defines the state schema used by the Plan-and-Execute V3 agent, extending
MessagesState with computed fields for plan tracking.
"""

from datetime import datetime
from typing import Any, Optional

from haive.core.schema.prebuilt.messages_state import MessagesState
from pydantic import Field, computed_field

from .models import ExecutionPlan, PlanEvaluation, StepExecution


class PlanExecuteV3State(MessagesState):
    """State schema for Plan-and-Execute V3 agent.

    This state is shared across the planner, executor, evaluator, and replanner sub-
    agents to maintain full context throughout the execution.
    """

    # Messages field is inherited from MessagesState

    # Current plan
    plan: Optional[ExecutionPlan] = Field(
        default=None, description="The current execution plan"
    )

    # Execution tracking
    current_step_id: Optional[int] = Field(
        default=None, description="ID of the step currently being executed"
    )

    step_executions: list[StepExecution] = Field(
        default_factory=list, description="History of all step executions"
    )

    # Evaluation history
    evaluations: list[PlanEvaluation] = Field(
        default_factory=list, description="History of plan evaluations"
    )

    # Plan revision tracking
    revision_count: int = Field(
        default=0, description="Number of times the plan has been revised"
    )

    plan_history: list[ExecutionPlan] = Field(
        default_factory=list, description="History of all plans (original + revisions)"
    )

    # Final result
    final_answer: Optional[str] = Field(
        default=None, description="Final answer once execution is complete"
    )

    # Timing
    started_at: datetime = Field(
        default_factory=datetime.now, description="When execution started"
    )

    completed_at: Optional[datetime] = Field(
        default=None, description="When execution completed"
    )

    # Additional context
    context: dict[str, Any] = Field(
        default_factory=dict, description="Additional context for execution"
    )

    # Error tracking
    errors: list[dict[str, Any]] = Field(
        default_factory=list, description="Errors encountered during execution"
    )

    @computed_field
    @property
    def objective(self) -> str:
        """Extract the objective from the plan or messages.
        """
        if self.plan and self.plan.objective:
            return self.plan.objective

        # Fallback to extracting from first human message
        for msg in self.messages:
            if hasattr(msg, "type") and msg.type == "human":
                return msg.content.strip()
            if isinstance(msg, dict) and msg.get("type") == "human":
                return msg.get("content", "").strip()

        return "No objective specified"

    @computed_field
    @property
    def current_step(self -> Optional[str]:
        """Get the current step description for the executor.
        """
        if not self.plan or not self.current_step_id:
            return None

        current_step = None
        for step in self.plan.steps:
            if step.step_id == self.current_step_id:
                current_step = step
                break

        if not current_step:
            return None

        # Format step for executor
        lines = [
            f"Step {current_step.step_id}: {current_step.description}",
            f"Expected Output: {current_step.expected_output}",
        ]

        if current_step.tools_required:
            lines.append(
    f"Tools Available: {
        ', '.join(
            current_step.tools_required)}")

        if current_step.dependencies:
            lines.append(
                f"Dependencies: Steps {', '.join(map(str,
     current_step.dependencies))}"
            )

        return "\n".join(lines)

    @ computed_field
    @ property
    def plan_status(self) -> str:
        """Get formatted plan status for agents.
        """
        if not self.plan:
            return "No plan available"

        lines = [
            f"Objective: {self.plan.objective}",
            f"Total Steps: {self.plan.total_steps}",
            f"Progress: {self.plan.get_progress_percentage():.1f}%",
            "Status:",
        ]

        # Count step statuses
        completed = sum(
    1 for s in self.plan.steps if s.status.value == "completed")
        failed = sum(1 for s in self.plan.steps if s.status.value == "failed")
        pending = sum(
    1 for s in self.plan.steps if s.status.value == "pending")
        in_progress = sum(
    1 for s in self.plan.steps if s.status.value == "in_progress")

        lines.extend(
            [
                f"  - Completed: {completed}",
                f"  - In Progress: {in_progress}",
                f"  - Pending: {pending}",
                f"  - Failed: {failed}",
            ]
        )

        next_step = self.plan.get_next_step()
        if next_step:
            lines.append(
                f"\nNext Step: Step {
    next_step.step_id} - {
        next_step.description}"
            )

        return "\n".join(lines)

    @ computed_field
    @ property
    def previous_results(self) -> str:
        """Get formatted previous step execution results.
        """
        if not self.step_executions:
            return "No previous results"

        lines = ["Previous Step Results:"]

        # Show last 5 executions
        for execution in self.step_executions[-5:]:
            status = "✓" if execution.success else "✗"
            lines.append(
                f"\n{status} Step {
    execution.step_id}: {
        execution.step_description}"
            )
            lines.append(
                f"   Result: {execution.result[:200]}..."
            )  # Truncate long results

            if execution.tools_used:
                lines.append(
    f"   Tools Used: {
        ', '.join(
            execution.tools_used)}")

            if execution.error:
                lines.append(f"   Error: {execution.error}")

            lines.append(f"   Time: {execution.execution_time:.2f}s")

        return "\n".join(lines)

    @ computed_field
    @ property
    def execution_summary(self) -> str:
        """Get a summary of the entire execution.
        """
        if not self.plan:
            return "No execution started"

        lines = [
            f"Plan: {self.plan.objective}",
            f"Progress: {
    self.plan.get_progress_percentage():.1f}% ({
        len(
            [
                s for s in self.plan.steps if s.status.value == 'completed'])}/{
                    self.plan.total_steps} steps)",
            f"Revisions: {self.revision_count}",
            f"Total Executions: {len(self.step_executions)}",
        ]

        if self.errors:
            lines.append(f"Errors Encountered: {len(self.errors)}")

        if self.completed_at and self.started_at:
            duration = (self.completed_at - self.started_at).total_seconds()
            lines.append(f"Total Time: {duration:.2f}s")

        return "\n".join(lines)

    @ computed_field
    @ property
    def should_evaluate(self) -> bool:
        """Determine if we should run evaluation.
        """
        if not self.plan:
            return False

        # Evaluate after every 3 steps
        completed_count = len(
            [s for s in self.plan.steps if s.status.value == "completed"]
        )
        if completed_count > 0 and completed_count % 3 == 0:
            return True

        # Evaluate if plan is complete
        if self.plan.is_complete():
            return True

        # Evaluate if there are failures
        if self.plan.has_failures():
            return True

        return False

    @ computed_field
    @ property
    def key_findings(self) -> list[str]:
        """Extract key findings from executions.
        """
        findings = []

        for execution in self.step_executions:
            if execution.observations:
                findings.append(
    f"Step {
        execution.step_id}: {
            execution.observations}")

        # Also extract from evaluations
        for evaluation in self.evaluations:
            if evaluation.current_progress:
                findings.append(
    f"Progress Update: {
        evaluation.current_progress}")

        return findings[-10:]  # Return last 10 findings

    @ computed_field
    @ property
    def execution_time(self -> Optional[float]:
        """Total execution time in seconds.
        """
        if self.started_at and self.completed_at:
            return (self.completed_at - self.started_at).total_seconds()
        if self.started_at:
            # Still running
            return (datetime.now() - self.started_at).total_seconds()
        return None

    def add_step_execution(self, execution: StepExecution) -> None:
        """Add a step execution result and update plan.
        """
        self.step_executions.append(execution)

        # Update plan step status
        if self.plan:
            for step in self.plan.steps:
                if step.step_id == execution.step_id:
                    if execution.success:
                        step.status="completed"
                        step.result=execution.result
                    else:
                        step.status="failed"
                        step.error=execution.error
                    step.execution_time=execution.execution_time
                    break

    def add_evaluation(self, evaluation: PlanEvaluation) -> None:
        """Add an evaluation result.
        """
        self.evaluations.append(evaluation)

        # Update final answer if provided
        if evaluation.final_answer:
            self.final_answer=evaluation.final_answer
            self.completed_at=datetime.now()

    def revise_plan(self, new_plan: ExecutionPlan) -> None:
        """Replace current plan with a revised version.
        """
        if self.plan:
            self.plan_history.append(self.plan)

        self.plan=new_plan
        self.revision_count += 1
        self.current_step_id=None  # Reset current step
