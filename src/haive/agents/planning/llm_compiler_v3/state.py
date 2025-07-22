"""State schema for LLM Compiler V3 Agent."""

from datetime import datetime
from typing import Any, Dict, List, Optional

from haive.core.schema.prebuilt.messages_state import MessagesState
from pydantic import Field

from haive.agents.planning.llm_compiler_v3.models import (
    CompilerInput,
    CompilerPlan,
    CompilerTask,
    ParallelExecutionResult,
    ReplanRequest,
)


class LLMCompilerStateSchema(MessagesState):
    """State schema for LLM Compiler V3 Agent using Enhanced MultiAgent V3."""

    # Core compiler state
    original_query: str = Field(default="", description="The original user query")

    current_plan: Optional[CompilerPlan] = Field(
        default=None, description="Current execution plan"
    )

    execution_results: List[ParallelExecutionResult] = Field(
        default_factory=list, description="Results from executed tasks"
    )

    # Execution tracking
    completed_task_ids: List[str] = Field(
        default_factory=list, description="IDs of completed tasks"
    )

    failed_task_ids: List[str] = Field(
        default_factory=list, description="IDs of failed tasks"
    )

    currently_executing: List[str] = Field(
        default_factory=list, description="IDs of tasks currently being executed"
    )

    # Parallel execution management
    max_parallel_tasks: int = Field(
        default=3, ge=1, le=10, description="Maximum number of parallel tasks"
    )

    execution_start_time: Optional[datetime] = Field(
        default=None, description="When execution started"
    )

    # Task coordination state
    ready_tasks: List[CompilerTask] = Field(
        default_factory=list,
        description="Tasks ready for execution (dependencies satisfied)",
    )

    blocked_tasks: List[CompilerTask] = Field(
        default_factory=list, description="Tasks blocked by dependencies"
    )

    # Results storage for dependency resolution
    task_results: Dict[str, Any] = Field(
        default_factory=dict,
        description="Results indexed by task_id for dependency resolution",
    )

    # Replanning state
    replan_count: int = Field(
        default=0, ge=0, description="Number of times replanning has occurred"
    )

    replan_requests: List[ReplanRequest] = Field(
        default_factory=list, description="History of replanning requests"
    )

    # Agent coordination
    current_agent: str = Field(default="planner", description="Currently active agent")

    next_agent: Optional[str] = Field(default=None, description="Next agent to execute")

    # Execution metadata
    execution_metadata: Dict[str, Any] = Field(
        default_factory=dict, description="Metadata about execution progress"
    )

    compiler_context: Dict[str, Any] = Field(
        default_factory=dict, description="Compiler-specific context and configuration"
    )

    # Performance tracking
    total_execution_time: float = Field(
        default=0.0, ge=0.0, description="Total execution time so far"
    )

    parallel_efficiency_score: Optional[float] = Field(
        default=None, ge=0.0, le=1.0, description="Efficiency of parallel execution"
    )

    def add_execution_result(self, result: ParallelExecutionResult) -> None:
        """Add a task execution result to state."""
        self.execution_results.append(result)

        if result.success:
            self.completed_task_ids.append(result.task_id)
            self.task_results[result.task_id] = result.result
        else:
            self.failed_task_ids.append(result.task_id)

        # Remove from currently executing
        if result.task_id in self.currently_executing:
            self.currently_executing.remove(result.task_id)

    def mark_task_executing(self, task_id: str) -> None:
        """Mark a task as currently executing."""
        if task_id not in self.currently_executing:
            self.currently_executing.append(task_id)

    def get_successful_results(self) -> List[ParallelExecutionResult]:
        """Get all successful execution results."""
        return [result for result in self.execution_results if result.success]

    def get_failed_results(self) -> List[ParallelExecutionResult]:
        """Get all failed execution results."""
        return [result for result in self.execution_results if not result.success]

    def update_ready_tasks(self) -> None:
        """Update lists of ready and blocked tasks based on current state."""
        if not self.current_plan:
            self.ready_tasks = []
            self.blocked_tasks = []
            return

        ready = []
        blocked = []

        for task in self.current_plan.tasks:
            # Skip already completed or failed tasks
            if (
                task.task_id in self.completed_task_ids
                or task.task_id in self.failed_task_ids
            ):
                continue

            # Skip currently executing tasks
            if task.task_id in self.currently_executing:
                continue

            # Check if dependencies are satisfied
            if task.can_execute_with_results(self.completed_task_ids):
                ready.append(task)
            else:
                blocked.append(task)

        self.ready_tasks = ready
        self.blocked_tasks = blocked

    def can_execute_more_tasks(self) -> bool:
        """Check if more tasks can be executed in parallel."""
        return len(self.currently_executing) < self.max_parallel_tasks

    def get_next_executable_tasks(self, count: int = None) -> List[CompilerTask]:
        """Get the next tasks to execute, respecting parallel limits."""
        if count is None:
            count = self.max_parallel_tasks - len(self.currently_executing)

        self.update_ready_tasks()

        # Sort by priority (higher priority first)
        sorted_ready = sorted(self.ready_tasks, key=lambda t: t.priority)

        return sorted_ready[:count]

    def resolve_task_arguments(self, task: CompilerTask) -> Dict[str, Any]:
        """Resolve task arguments by substituting dependency references."""
        resolved_args = {}

        for key, value in task.arguments.items():
            if isinstance(value, str) and value.startswith("${"):
                # This is a dependency reference like ${task_1} or ${task_1.result}
                import re

                match = re.match(r"\\$\\{([^.}]+)(?:\\.([^}]+))?\\}", value)

                if match:
                    task_id = match.group(1)
                    output_key = match.group(2)

                    if task_id in self.task_results:
                        result = self.task_results[task_id]

                        if output_key and isinstance(result, dict):
                            resolved_args[key] = result.get(output_key, value)
                        else:
                            resolved_args[key] = result
                    else:
                        # Dependency not satisfied yet
                        resolved_args[key] = value
                else:
                    resolved_args[key] = value
            else:
                resolved_args[key] = value

        return resolved_args

    def is_execution_complete(self) -> bool:
        """Check if all tasks in the plan have been executed or failed."""
        if not self.current_plan:
            return False

        total_tasks = len(self.current_plan.tasks)
        finished_tasks = len(self.completed_task_ids) + len(self.failed_task_ids)

        return finished_tasks >= total_tasks

    def should_replan(self) -> bool:
        """Determine if replanning is needed based on execution state."""
        # Replan if critical tasks failed and we can't proceed
        if (
            self.failed_task_ids
            and not self.ready_tasks
            and not self.currently_executing
        ):
            return True

        # Replan if more than 50% of tasks failed
        if len(self.failed_task_ids) > len(self.completed_task_ids):
            return True

        return False

    def get_execution_summary(self) -> Dict[str, Any]:
        """Get comprehensive execution summary."""
        return {
            "original_query": self.original_query,
            "total_tasks": len(self.current_plan.tasks) if self.current_plan else 0,
            "completed_tasks": len(self.completed_task_ids),
            "failed_tasks": len(self.failed_task_ids),
            "currently_executing": len(self.currently_executing),
            "ready_tasks": len(self.ready_tasks),
            "blocked_tasks": len(self.blocked_tasks),
            "execution_complete": self.is_execution_complete(),
            "should_replan": self.should_replan(),
            "replan_count": self.replan_count,
            "total_execution_time": self.total_execution_time,
            "parallel_efficiency": self.parallel_efficiency_score,
            "success_rate": len(self.completed_task_ids)
            / max(1, len(self.execution_results)),
            "current_agent": self.current_agent,
            "next_agent": self.next_agent,
        }
