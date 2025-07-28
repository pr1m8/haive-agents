"""Pydantic models for ReWOO V3 Agent.

This module defines structured output models for the ReWOO (Reasoning without Observation)
methodology using Enhanced MultiAgent V3.

Key Models:
- ReWOOPlan: Planner agent structured output with evidence placeholders
- EvidenceItem: Individual evidence collected by worker
- EvidenceCollection: Worker agent structured output with all evidence
- ReWOOSolution: Solver agent final answer with reasoning
"""

from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class EvidenceStatus(str, Enum):
    """Status of evidence collection."""

    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"
    PARTIAL = "partial"


class PlanStep(BaseModel):
    """Individual step in the ReWOO plan."""

    step_id: str = Field(description="Unique step identifier (e.g., 'step_1')")
    description: str = Field(description="What this step accomplishes")
    evidence_id: str = Field(description="Evidence placeholder (e.g., '#E1')")
    tool_call: str | None = Field(default=None, description="Specific tool to use")
    depends_on: list[str] = Field(
        default_factory=list, description="Evidence IDs this step needs"
    )


class ReWOOPlan(BaseModel):
    """Structured planning output from Planner agent.

    The plan contains all steps upfront without seeing any tool results.
    Each step has an evidence placeholder that will be filled by the Worker.
    """

    plan_id: str = Field(description="Unique plan identifier")
    objective: str = Field(description="Original query/objective")
    approach: str = Field(description="Overall approach to solve the problem")

    steps: list[PlanStep] = Field(description="Complete execution plan")

    reasoning: str = Field(description="Why this plan will solve the objective")
    expected_evidence: dict[str, str] = Field(
        default_factory=dict,
        description="Map of evidence_id to expected content description",
    )

    total_steps: int = Field(description="Total number of steps")
    created_at: datetime = Field(default_factory=datetime.now)


class EvidenceItem(BaseModel):
    """Individual piece of evidence collected by Worker."""

    evidence_id: str = Field(description="Evidence identifier (e.g., '#E1')")
    step_id: str = Field(description="Corresponding step identifier")
    content: str = Field(description="Actual evidence content/result")
    source: str = Field(description="Tool or source that provided this evidence")
    status: EvidenceStatus = Field(description="Collection status")
    timestamp: datetime = Field(default_factory=datetime.now)
    metadata: dict[str, Any] = Field(
        default_factory=dict, description="Additional info"
    )


class EvidenceCollection(BaseModel):
    """Worker agent structured output with all collected evidence."""

    collection_id: str = Field(description="Unique collection identifier")
    plan_id: str = Field(description="Associated plan ID")

    evidence_items: list[EvidenceItem] = Field(description="All collected evidence")

    summary: str = Field(description="Summary of evidence collection process")
    success_count: int = Field(description="Number of successful evidence items")
    failure_count: int = Field(description="Number of failed evidence items")

    tools_used: list[str] = Field(
        default_factory=list, description="Tools that were invoked"
    )
    execution_notes: list[str] = Field(
        default_factory=list, description="Execution observations"
    )

    completed_at: datetime = Field(default_factory=datetime.now)


class ReWOOSolution(BaseModel):
    """Final synthesized solution from Solver agent."""

    solution_id: str = Field(description="Unique solution identifier")
    original_query: str = Field(description="Original user query")

    final_answer: str = Field(description="Comprehensive final answer")
    reasoning: str = Field(description="How the evidence supports this answer")

    evidence_used: list[str] = Field(
        description="Evidence IDs that contributed to answer"
    )
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence in solution")

    synthesis_process: str = Field(description="How evidence was combined")
    limitations: list[str] = Field(
        default_factory=list, description="Known limitations or gaps"
    )

    created_at: datetime = Field(default_factory=datetime.now)


# Input/Output models for the main ReWOO V3 agent


class ReWOOV3Input(BaseModel):
    """Input model for ReWOO V3 agent."""

    query: str = Field(description="User query to solve")
    context: str | None = Field(default=None, description="Additional context")
    max_steps: int | None = Field(
        default=10, ge=1, le=20, description="Maximum planning steps"
    )
    tools_preference: list[str] | None = Field(
        default=None, description="Preferred tools to use"
    )


class ReWOOV3Output(BaseModel):
    """Output model for ReWOO V3 agent."""

    query: str = Field(description="Original query")
    final_answer: str = Field(description="Complete solution")
    confidence: float = Field(ge=0.0, le=1.0, description="Solution confidence")

    # Execution summary
    steps_planned: int = Field(description="Number of steps in plan")
    evidence_collected: int = Field(description="Successfully collected evidence items")
    tools_used: list[str] = Field(description="Tools that were utilized")

    # Timing
    total_execution_time: float = Field(description="Total time in seconds")
    planning_time: float = Field(description="Time spent on planning")
    execution_time: float = Field(description="Time spent on tool execution")
    solving_time: float = Field(description="Time spent on synthesis")

    # Detailed results
    reasoning_process: str = Field(description="How the solution was derived")
    evidence_summary: str = Field(description="Summary of evidence collected")
    limitations: list[str] = Field(
        default_factory=list, description="Known limitations"
    )

    # Internal references
    plan_id: str = Field(description="Internal plan reference")
    solution_id: str = Field(description="Internal solution reference")
