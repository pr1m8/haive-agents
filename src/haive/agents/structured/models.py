"""Pydantic models for structured output agents.

This module defines the common output models used by structured agents for converting
unstructured text into organized data.
"""

from typing import Any

from pydantic import BaseModel, Field


class GenericStructuredOutput(BaseModel):
    """Generic structured output model for any content.

    This model provides a flexible structure that can capture the essence of most text
    outputs in an organized way.
    """

    main_content: str = Field(
        ..., description="The main content, answer, or primary information"
    )

    key_points: list[str] = Field(
        default_factory=list,
        description="Key points, findings, or important items extracted",
    )

    action_items: list[str] = Field(
        default_factory=list,
        description="Action items, tasks, or things to do (if any)",
    )

    categories: dict[str, str] = Field(
        default_factory=dict, description="Categorized information by topic or theme"
    )

    metadata: dict[str, Any] = Field(
        default_factory=dict, description="Additional metadata or context"
    )

    confidence: float = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        description="Confidence level in the extraction (0-1)",
    )


class AnalysisOutput(BaseModel):
    """Structured output for analysis tasks."""

    summary: str = Field(..., description="Brief summary of the analysis")

    findings: list[str] = Field(..., description="Key findings from the analysis")

    evidence: list[str] = Field(
        default_factory=list, description="Supporting evidence for findings"
    )

    recommendations: list[str] = Field(
        default_factory=list, description="Recommendations based on analysis"
    )

    confidence_score: float = Field(
        default=0.8, ge=0.0, le=1.0, description="Overall confidence in the analysis"
    )

    limitations: list[str] = Field(
        default_factory=list, description="Limitations or caveats of the analysis"
    )


class TaskOutput(BaseModel):
    """Structured output for task-related content."""

    task_description: str = Field(..., description="Description of the task")

    steps: list[str] = Field(..., description="Steps to complete the task")

    requirements: list[str] = Field(
        default_factory=list, description="Requirements or prerequisites"
    )

    estimated_time: str | None = Field(
        default=None, description="Estimated time to complete"
    )

    complexity: int = Field(
        default=5, ge=1, le=10, description="Task complexity (1-10)"
    )

    dependencies: list[str] = Field(
        default_factory=list, description="Task dependencies"
    )


class DecisionOutput(BaseModel):
    """Structured output for decision-making content."""

    decision: str = Field(..., description="The decision or choice made")

    reasoning: str = Field(..., description="Reasoning behind the decision")

    alternatives: list[str] = Field(
        default_factory=list, description="Alternative options considered"
    )

    pros: list[str] = Field(
        default_factory=list, description="Advantages of the decision"
    )

    cons: list[str] = Field(default_factory=list, description="Disadvantages or risks")

    confidence: float = Field(
        default=0.7, ge=0.0, le=1.0, description="Confidence in the decision"
    )

    next_steps: list[str] = Field(
        default_factory=list, description="Recommended next steps"
    )
