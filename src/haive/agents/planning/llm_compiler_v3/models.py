"""Pydantic models for LLM Compiler V3 Agent.

This module defines structured data models for the LLM Compiler pattern
optimized for Enhanced MultiAgent V3 architecture.
"""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, ConfigDict, Field


class ExecutionMode(str, Enum):
    """Execution mode for tasks."""

    PARALLEL = "parallel"
    SEQUENTIAL = "sequential"
    HYBRID = "hybrid"


class TaskDependency(BaseModel):
    """Represents a dependency between tasks."""

    model_config = ConfigDict(
        str_strip_whitespace=True, validate_assignment=True, extra="forbid"
    )

    task_id: str = Field(
        ...,
        description="ID of the task this depends on",
        examples=["task_1", "search_task", "analysis_step"],
    )

    output_key: Optional[str] = Field(
        default=None,
        description="Specific output key to reference (optional)",
        examples=["result", "data", "summary"],
    )

    def resolve_reference(self) -> str:
        """Generate reference string for task dependency."""
        if self.output_key:
            return f"${{{self.task_id}.{self.output_key}}}"
        return f"${{{self.task_id}}}"


class CompilerTask(BaseModel):
    """Individual task in the LLM Compiler execution DAG."""

    model_config = ConfigDict(
        str_strip_whitespace=True, validate_assignment=True, extra="forbid"
    )

    task_id: str = Field(
        ...,
        description="Unique identifier for this task",
        examples=["search_web", "analyze_data", "summarize_results"],
    )

    tool_name: str = Field(
        ...,
        description="Name of the tool to execute",
        examples=["web_search", "calculator", "code_executor", "join"],
    )

    description: str = Field(
        ...,
        description="Human-readable description of the task",
        examples=["Search for recent AI developments", "Calculate the sum"],
    )

    arguments: Dict[str, Any] = Field(
        default_factory=dict,
        description="Arguments to pass to the tool",
        examples=[{"query": "latest AI news"}, {"expression": "15 + 27"}],
    )

    dependencies: List[TaskDependency] = Field(
        default_factory=list, description="Tasks this task depends on"
    )

    priority: int = Field(
        default=1, ge=1, le=10, description="Task priority (1=highest, 10=lowest)"
    )

    estimated_duration: Optional[float] = Field(
        default=None, ge=0.0, description="Estimated execution time in seconds"
    )

    @property
    def is_join_task(self) -> bool:
        """Check if this is the final join task."""
        return self.tool_name.lower() == "join"

    @property
    def dependency_ids(self) -> List[str]:
        """Get list of task IDs this task depends on."""
        return [dep.task_id for dep in self.dependencies]

    def has_dependencies(self) -> bool:
        """Check if this task has any dependencies."""
        return len(self.dependencies) > 0

    def can_execute_with_results(self, completed_tasks: List[str]) -> bool:
        """Check if all dependencies are satisfied."""
        return all(dep.task_id in completed_tasks for dep in self.dependencies)


class CompilerPlan(BaseModel):
    """Execution plan containing tasks and their dependencies."""

    model_config = ConfigDict(
        str_strip_whitespace=True, validate_assignment=True, extra="forbid"
    )

    plan_id: str = Field(
        ...,
        description="Unique identifier for this plan",
        examples=["plan_20250121_001", "research_plan"],
    )

    description: str = Field(
        ..., description="High-level description of what this plan accomplishes"
    )

    tasks: List[CompilerTask] = Field(
        default_factory=list, description="Tasks in execution order"
    )

    execution_mode: ExecutionMode = Field(
        default=ExecutionMode.HYBRID, description="How to execute tasks"
    )

    max_parallel_tasks: int = Field(
        default=3, ge=1, le=10, description="Maximum number of tasks to run in parallel"
    )

    created_at: datetime = Field(
        default_factory=datetime.now, description="When this plan was created"
    )

    def get_executable_tasks(self, completed_task_ids: List[str]) -> List[CompilerTask]:
        """Get tasks that can be executed now (dependencies satisfied)."""
        return [
            task
            for task in self.tasks
            if task.task_id not in completed_task_ids
            and task.can_execute_with_results(completed_task_ids)
        ]

    def get_join_task(self) -> Optional[CompilerTask]:
        """Get the final join task if it exists."""
        for task in self.tasks:
            if task.is_join_task:
                return task
        return None

    def get_task_by_id(self, task_id: str) -> Optional[CompilerTask]:
        """Find task by ID."""
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def validate_dependencies(self) -> List[str]:
        """Validate that all dependencies reference existing tasks."""
        errors = []
        task_ids = {task.task_id for task in self.tasks}

        for task in self.tasks:
            for dep in task.dependencies:
                if dep.task_id not in task_ids:
                    errors.append(
                        f"Task '{task.task_id}' depends on non-existent task '{dep.task_id}'"
                    )

        return errors


class ParallelExecutionResult(BaseModel):
    """Result from executing a task."""

    model_config = ConfigDict(
        str_strip_whitespace=True, validate_assignment=True, extra="forbid"
    )

    task_id: str = Field(..., description="ID of the executed task")

    success: bool = Field(..., description="Whether the task executed successfully")

    result: Any = Field(..., description="Task execution result")

    error_message: Optional[str] = Field(
        default=None, description="Error message if execution failed"
    )

    execution_time: float = Field(
        ..., ge=0.0, description="Time taken to execute in seconds"
    )

    tool_name: str = Field(..., description="Name of tool that was executed")

    metadata: Dict[str, Any] = Field(
        default_factory=dict, description="Additional execution metadata"
    )


class CompilerInput(BaseModel):
    """Input to the LLM Compiler V3 Agent."""

    model_config = ConfigDict(
        str_strip_whitespace=True, validate_assignment=True, extra="forbid"
    )

    query: str = Field(
        ...,
        min_length=1,
        description="The user's query or task to accomplish",
        examples=["Find recent AI papers and summarize key findings"],
    )

    context: Optional[Dict[str, Any]] = Field(
        default=None, description="Additional context for the task"
    )

    execution_preferences: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Preferences for how to execute the plan",
        examples=[{"max_parallel": 5, "timeout": 300}],
    )

    available_tools: Optional[List[str]] = Field(
        default=None, description="Specific tools to use (if None, uses all available)"
    )


class CompilerOutput(BaseModel):
    """Final output from the LLM Compiler V3 Agent."""

    model_config = ConfigDict(
        str_strip_whitespace=True, validate_assignment=True, extra="forbid"
    )

    final_answer: str = Field(..., description="The final answer to the user's query")

    execution_plan: CompilerPlan = Field(..., description="The plan that was executed")

    execution_results: List[ParallelExecutionResult] = Field(
        default_factory=list, description="Results from all executed tasks"
    )

    total_execution_time: float = Field(
        ..., ge=0.0, description="Total time for entire execution"
    )

    tasks_executed: int = Field(
        ..., ge=0, description="Number of tasks that were executed"
    )

    parallel_efficiency: Optional[float] = Field(
        default=None,
        ge=0.0,
        le=1.0,
        description="Efficiency score for parallel execution (0-1)",
    )

    reasoning_trace: List[str] = Field(
        default_factory=list, description="Step-by-step reasoning trace"
    )

    metadata: Dict[str, Any] = Field(
        default_factory=dict, description="Additional metadata about execution"
    )

    def get_successful_tasks(self) -> List[ParallelExecutionResult]:
        """Get only the successfully executed tasks."""
        return [result for result in self.execution_results if result.success]

    def get_failed_tasks(self) -> List[ParallelExecutionResult]:
        """Get only the failed tasks."""
        return [result for result in self.execution_results if not result.success]

    @property
    def success_rate(self) -> float:
        """Calculate the success rate of task execution."""
        if not self.execution_results:
            return 0.0
        successful = len(self.get_successful_tasks())
        return successful / len(self.execution_results)


class ReplanRequest(BaseModel):
    """Request for replanning when initial plan fails."""

    model_config = ConfigDict(
        str_strip_whitespace=True, validate_assignment=True, extra="forbid"
    )

    feedback: str = Field(..., description="Analysis of why replanning is needed")

    failed_tasks: List[str] = Field(
        default_factory=list, description="IDs of tasks that failed"
    )

    partial_results: Dict[str, Any] = Field(
        default_factory=dict, description="Results from tasks that succeeded"
    )

    suggested_changes: Optional[List[str]] = Field(
        default=None, description="Specific suggestions for the new plan"
    )
