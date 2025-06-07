"""
RAG Structured Output Models

Pydantic models for structured outputs from RAG evaluation agents.
"""

from enum import Enum
from typing import Any, Dict, List, Literal, Optional, Union

from pydantic import BaseModel, Field

# Import the grading models from your system
from haive.agents.common.models.grade.base import Grade
from haive.agents.common.models.grade.binary import BinaryGrade
from haive.agents.common.models.grade.composite import CompositeGrade
from haive.agents.common.models.grade.numeric import NumericGrade
from haive.agents.common.models.grade.rubric import RubricCriterion, RubricGrade
from haive.agents.common.models.grade.scale import ScaleGrade

# ============================================================================
# DOCUMENT GRADING MODELS
# ============================================================================


class DocumentRelevanceScore(BaseModel):
    """Individual document relevance assessment."""

    document_id: str = Field(description="Identifier for the document")
    document_title: Optional[str] = Field(
        default=None, description="Title or summary of document"
    )
    relevance_score: float = Field(
        ge=0.0, le=1.0, description="Relevance score from 0.0 to 1.0"
    )
    justification: str = Field(
        min_length=10, description="Detailed explanation for the relevance score"
    )
    key_information: List[str] = Field(
        default_factory=list,
        description="Key pieces of information that support the query",
    )
    limitations: List[str] = Field(
        default_factory=list, description="Missing information or gaps in the document"
    )
    confidence: float = Field(
        default=1.0, ge=0.0, le=1.0, description="Confidence in the assessment"
    )


class DocumentGradingResponse(BaseModel):
    """Comprehensive document grading response."""

    query: str = Field(description="The original query")
    document_scores: List[DocumentRelevanceScore] = Field(
        description="Individual scores for each document"
    )
    overall_assessment: str = Field(
        description="Summary assessment of the document collection"
    )
    coverage_analysis: str = Field(
        description="Analysis of how well documents cover the query"
    )
    recommendations: List[str] = Field(
        default_factory=list, description="Recommendations for improving retrieval"
    )


class DocumentBinaryGrading(BaseModel):
    """Binary pass/fail document grading."""

    document_id: str = Field(description="Document identifier")
    decision: Literal["pass", "fail"]
    justification: str = Field(description="Reasoning for the decision")
    confidence: float = Field(
        default=1.0, ge=0.0, le=1.0, description="Confidence in the decision"
    )


class DocumentBinaryResponse(BaseModel):
    """Response for binary document grading."""

    query: str = Field(description="The original query")
    document_decisions: List[DocumentBinaryGrading] = Field(
        description="Binary decisions for each document"
    )
    summary: str = Field(description="Overall summary of filtering results")
