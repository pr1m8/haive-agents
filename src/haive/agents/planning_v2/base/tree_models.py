"""Tree-based planning models using the enhanced tree_leaf structure.

This module provides planning models that leverage the generic tree/leaf
structure from haive-core for more flexible and type-safe planning.
"""

from enum import Enum
from typing import List, Optional, Union

from haive.core.common.structures import DefaultResult, Leaf, Tree, TreeNode
from pydantic import BaseModel, Field


class PlanStatus(str, Enum):
    """Status for plan nodes."""

    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    BLOCKED = "blocked"


class PlanContent(BaseModel):
    """Content for plan nodes (both tasks and sub-plans)."""

    objective: str = Field(..., description="What this node aims to accomplish")
    description: str = Field("", description="Detailed description")
    priority: int = Field(1, ge=1, le=5, description="Priority (1=lowest, 5=highest)")
    status: PlanStatus = Field(PlanStatus.PENDING, description="Current status")
    metadata: dict = Field(default_factory=dict, description="Additional metadata")


class PlanResult(BaseModel):
    """Result of executing a plan node."""

    success: bool = Field(..., description="Whether execution succeeded")
    output: Optional[str] = Field(None, description="Execution output")
    error: Optional[str] = Field(None, description="Error message if failed")
    duration_seconds: Optional[float] = Field(None, description="Execution time")
    artifacts: dict = Field(default_factory=dict, description="Any artifacts produced")


# Type aliases for common planning patterns
PlanLeaf = Leaf[PlanContent, PlanResult]
PlanTree = Tree[PlanContent, TreeNode[PlanContent, PlanResult], PlanResult]
SimplePlanTree = Tree[PlanContent, Union[PlanLeaf, "SimplePlanTree"], PlanResult]


class TaskPlan(PlanTree):
    """A concrete plan implementation using the tree structure.

    This class extends the generic Tree to provide planning-specific
    functionality while maintaining type safety.

    Example:
        ```python
        # Create a plan
        plan = TaskPlan(content=PlanContent(
            objective="Deploy new feature",
            priority=4
        ))

        # Add simple tasks
        plan.add_task("Write tests", priority=5)
        plan.add_task("Code review", priority=3)

        # Add sub-plan
        deploy_plan = plan.add_subplan("Deploy to production")
        deploy_plan.add_task("Deploy to staging")
        deploy_plan.add_task("Run smoke tests")
        deploy_plan.add_task("Deploy to prod")

        # Check status
        print(f"Total tasks: {plan.total_nodes}")
        print(f"Progress: {plan.progress_percentage}%")
        ```
    """

    def add_task(
        self, objective: str, description: str = "", priority: int = 1
    ) -> PlanLeaf:
        """Add a simple task to the plan."""
        task = PlanLeaf(
            content=PlanContent(
                objective=objective, description=description, priority=priority
            )
        )
        return self.add_child(task)

    def add_subplan(
        self, objective: str, description: str = "", priority: int = 1
    ) -> "TaskPlan":
        """Add a sub-plan that can contain its own tasks."""
        subplan = TaskPlan(
            content=PlanContent(
                objective=objective, description=description, priority=priority
            )
        )
        return self.add_child(subplan)

    def add_parallel_tasks(self, tasks: List[tuple[str, int]]) -> List[PlanLeaf]:
        """Add multiple tasks that can execute in parallel.

        Args:
            tasks: List of (objective, priority) tuples

        Returns:
            List of created task nodes
        """
        task_nodes = [
            PlanLeaf(content=PlanContent(objective=obj, priority=pri))
            for obj, pri in tasks
        ]
        # Use inherited parallel children method
        return super().add_parallel_children(task_nodes)

    def mark_current_completed(self, output: str = "Done") -> bool:
        """Mark the current active task as completed."""
        current = self.get_current_task()
        if current:
            current.content.status = PlanStatus.COMPLETED
            current.result = PlanResult(success=True, output=output)
            return True
        return False

    def mark_current_failed(self, error: str) -> bool:
        """Mark the current active task as failed."""
        current = self.get_current_task()
        if current:
            current.content.status = PlanStatus.FAILED
            current.result = PlanResult(success=False, error=error)
            return True
        return False

    def get_current_task(self) -> Optional[Union[PlanLeaf, "TaskPlan"]]:
        """Get the current task to execute (first pending or in-progress)."""
        # Check self first
        if self.content.status == PlanStatus.IN_PROGRESS:
            return self

        # Find in children
        for child in self.children:
            if child.content.status == PlanStatus.IN_PROGRESS:
                return child
            elif isinstance(child, TaskPlan):
                current = child.get_current_task()
                if current:
                    return current

        # Find first pending
        for child in self.children:
            if child.content.status == PlanStatus.PENDING:
                return child
            elif isinstance(child, TaskPlan):
                pending = child.get_current_task()
                if pending:
                    return pending

        return None

    def get_tasks_by_priority(
        self, min_priority: int = 1
    ) -> List[Union[PlanLeaf, "TaskPlan"]]:
        """Get all tasks with priority >= min_priority."""
        tasks = []

        if self.content.priority >= min_priority:
            tasks.append(self)

        for child in self.children:
            if child.content.priority >= min_priority:
                tasks.append(child)
            if isinstance(child, TaskPlan):
                tasks.extend(child.get_tasks_by_priority(min_priority))

        return tasks

    def get_blocked_tasks(self) -> List[Union[PlanLeaf, "TaskPlan"]]:
        """Get all tasks that are blocked."""
        blocked = []

        if self.content.status == PlanStatus.BLOCKED:
            blocked.append(self)

        for child in self.children:
            if child.content.status == PlanStatus.BLOCKED:
                blocked.append(child)
            if isinstance(child, TaskPlan):
                blocked.extend(child.get_blocked_tasks())

        return blocked

    def to_markdown(self, indent: int = 0) -> str:
        """Convert plan to markdown representation."""
        prefix = "  " * indent
        status_emoji = {
            PlanStatus.PENDING: "⏳",
            PlanStatus.IN_PROGRESS: "🔄",
            PlanStatus.COMPLETED: "✅",
            PlanStatus.FAILED: "❌",
            PlanStatus.CANCELLED: "🚫",
            PlanStatus.BLOCKED: "🚧",
        }

        emoji = status_emoji.get(self.content.status, "❓")
        priority_stars = "⭐" * self.content.priority

        lines = [f"{prefix}- {emoji} **{self.content.objective}** {priority_stars}"]

        if self.content.description:
            lines.append(f"{prefix}  {self.content.description}")

        if self.result:
            if self.result.success:
                lines.append(f"{prefix}  ✓ {self.result.output}")
            else:
                lines.append(f"{prefix}  ✗ Error: {self.result.error}")

        # Add children
        for child in self.children:
            if isinstance(child, TaskPlan):
                lines.append(child.to_markdown(indent + 1))
            else:
                child_emoji = status_emoji.get(child.content.status, "❓")
                child_stars = "⭐" * child.content.priority
                lines.append(
                    f"{prefix}  - {child_emoji} {child.content.objective} {child_stars}"
                )
                if child.result:
                    if child.result.success:
                        lines.append(f"{prefix}    ✓ {child.result.output}")
                    else:
                        lines.append(f"{prefix}    ✗ Error: {child.result.error}")

        return "\n".join(lines)


# Convenience functions
def create_simple_plan(objective: str, tasks: List[str]) -> TaskPlan:
    """Create a simple linear plan from a list of task names."""
    plan = TaskPlan(content=PlanContent(objective=objective))
    for task in tasks:
        plan.add_task(task)
    return plan


def create_phased_plan(objective: str, phases: dict[str, List[str]]) -> TaskPlan:
    """Create a plan with phases (sub-plans).

    Args:
        objective: Main plan objective
        phases: Dict of phase_name -> list of tasks

    Example:
        plan = create_phased_plan(
            "Launch Product",
            {
                "Development": ["Code", "Test", "Review"],
                "Deployment": ["Stage", "Verify", "Prod"],
                "Marketing": ["Announce", "Demo", "Feedback"]
            }
        )
    """
    plan = TaskPlan(content=PlanContent(objective=objective))

    for phase_name, tasks in phases.items():
        phase = plan.add_subplan(phase_name)
        for task in tasks:
            phase.add_task(task)

    return plan
