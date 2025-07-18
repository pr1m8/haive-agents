"""Simple reflection models following Plan and Execute pattern."""

from typing import List, Literal, Optional

from pydantic import BaseModel, Field


class Critique(BaseModel):
    """Analysis of content quality and issues."""

    strengths: List[str] = Field(
        default_factory=list, description="What works well in the content"
    )
    weaknesses: List[str] = Field(
        default_factory=list, description="What needs improvement"
    )
    quality_score: float = Field(
        ..., description="Overall quality score from 0.0 to 1.0", ge=0.0, le=1.0
    )
    needs_improvement: bool = Field(
        ..., description="Whether the content needs to be improved"
    )


class Improvement(BaseModel):
    """Improved version of the content."""

    improved_content: str = Field(
        ..., description="The improved version of the content"
    )
    changes_made: List[str] = Field(
        default_factory=list, description="List of changes made during improvement"
    )
    confidence: float = Field(
        ..., description="Confidence in the improvement from 0.0 to 1.0", ge=0.0, le=1.0
    )


class ReflectionResult(BaseModel):
    """Result of reflection process."""

    original_content: str = Field(..., description="The original content")
    final_content: str = Field(..., description="The final improved content")
    iterations: int = Field(default=1, description="Number of improvement iterations")
    final_quality: float = Field(..., description="Final quality score", ge=0.0, le=1.0)
    improvement_summary: List[str] = Field(
        default_factory=list, description="Summary of all improvements made"
    )


class ReflectionAction(BaseModel):
    """Action to take during reflection - either improve or finalize."""

    action: Literal["improve", "finalize"] = Field(
        ..., description="Action to take: improve content or finalize result"
    )
    reason: str = Field(..., description="Reason for this action")


# Rebuild forward references
Critique.model_rebuild()
Improvement.model_rebuild()
ReflectionResult.model_rebuild()
ReflectionAction.model_rebuild()
