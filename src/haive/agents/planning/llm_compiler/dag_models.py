"""Structured DAG models for LLM Compiler planning.

These Pydantic models are used as structured output from the planner LLM,
replacing the text-based output parser. The LLM returns a proper DAGPlan
directly, which is more reliable and leverages AugLLMConfig's structured
output capability.
"""

from typing import Any, Literal

from pydantic import BaseModel, Field


class DAGTask(BaseModel):
    """A single task in the execution DAG."""

    id: int = Field(description="Unique task ID (sequential, starting from 1)")
    tool: str = Field(description="Name of the tool to call, or 'join' for the final aggregation step")
    args: dict[str, Any] = Field(
        default_factory=dict,
        description="Arguments for the tool. Use '$N' to reference the output of task N (e.g. '$1' for task 1's result)",
    )
    depends_on: list[int] = Field(
        default_factory=list,
        description="IDs of tasks that must complete before this one. Empty = can run immediately",
    )
    thought: str = Field(
        default="",
        description="Brief reasoning for why this task is needed",
    )


class DAGPlan(BaseModel):
    """A directed acyclic graph of tasks to execute.

    The planner LLM outputs this structured plan. Tasks with no dependencies
    run in parallel. The last task should be 'join' to aggregate results.
    """

    tasks: list[DAGTask] = Field(
        description="Ordered list of tasks forming the DAG. Maximize parallelism - "
        "only add dependencies when a task truly needs another's output."
    )
    reasoning: str = Field(
        default="",
        description="High-level reasoning about the approach",
    )


class JoinerDecision(BaseModel):
    """The joiner's decision after inspecting execution results."""

    thought: str = Field(description="Reasoning about whether results are sufficient")
    action: Literal["answer", "replan"] = Field(
        description="'answer' if results are sufficient, 'replan' if more work needed"
    )
    response: str = Field(
        default="",
        description="Final answer (required if action='answer')",
    )
    feedback: str = Field(
        default="",
        description="What went wrong and what to try next (required if action='replan')",
    )
