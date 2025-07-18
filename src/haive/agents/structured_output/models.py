"""Common structured output models for various agent patterns."""

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

# ========================================================================
# REFLECTION MODELS
# ========================================================================


class Critique(BaseModel):
    """Structured critique of an output."""

    strengths: List[str] = Field(description="List of strengths in the output")
    weaknesses: List[str] = Field(description="List of weaknesses or issues")
    suggestions: List[str] = Field(description="Specific suggestions for improvement")
    overall_quality: float = Field(
        ge=0.0, le=1.0, description="Overall quality score (0-1)"
    )
    needs_revision: bool = Field(description="Whether the output needs revision")


class Improvement(BaseModel):
    """Structured improvement suggestions."""

    original_issue: str = Field(description="Description of the issue to improve")
    proposed_solution: str = Field(description="Proposed solution or improvement")
    implementation_steps: List[str] = Field(
        description="Steps to implement the improvement"
    )
    expected_impact: str = Field(description="Expected impact of the improvement")
    priority: str = Field(description="Priority level: high, medium, low")


class ReflectionResult(BaseModel):
    """Complete reflection analysis."""

    summary: str = Field(description="Summary of the reflection")
    critique: Critique = Field(description="Detailed critique")
    improvements: List[Improvement] = Field(description="List of proposed improvements")
    action_items: List[str] = Field(description="Concrete action items")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence in the analysis")


# ========================================================================
# VALIDATION MODELS
# ========================================================================


class ValidationResult(BaseModel):
    """Result of validation check."""

    is_valid: bool = Field(description="Whether the output is valid")
    errors: List[str] = Field(
        default_factory=list, description="List of validation errors"
    )
    warnings: List[str] = Field(
        default_factory=list, description="List of validation warnings"
    )
    score: float = Field(ge=0.0, le=1.0, description="Validation score (0-1)")
    details: Dict[str, Any] = Field(
        default_factory=dict, description="Detailed validation results"
    )


class QualityCheck(BaseModel):
    """Quality assessment result."""

    completeness: float = Field(
        ge=0.0, le=1.0, description="How complete the output is"
    )
    accuracy: float = Field(ge=0.0, le=1.0, description="Accuracy of the information")
    clarity: float = Field(ge=0.0, le=1.0, description="Clarity of expression")
    relevance: float = Field(ge=0.0, le=1.0, description="Relevance to the task")
    overall_quality: float = Field(ge=0.0, le=1.0, description="Overall quality score")
    meets_requirements: bool = Field(description="Whether it meets all requirements")
    feedback: str = Field(description="Qualitative feedback")


# ========================================================================
# ANALYSIS MODELS
# ========================================================================


class Analysis(BaseModel):
    """Structured analysis result."""

    topic: str = Field(description="Main topic or subject")
    key_points: List[str] = Field(description="Key points identified")
    insights: List[str] = Field(description="Key insights discovered")
    data_points: Dict[str, Any] = Field(
        default_factory=dict, description="Relevant data points"
    )
    conclusions: List[str] = Field(description="Conclusions drawn")
    confidence_level: str = Field(description="Confidence level: high, medium, low")


class Summary(BaseModel):
    """Structured summary."""

    title: str = Field(description="Title or main topic")
    executive_summary: str = Field(description="Brief executive summary")
    main_points: List[str] = Field(description="Main points covered")
    details: Dict[str, str] = Field(
        default_factory=dict, description="Detailed sections"
    )
    action_items: List[str] = Field(
        default_factory=list, description="Action items if any"
    )
    word_count: int = Field(description="Approximate word count")


# ========================================================================
# TASK MODELS
# ========================================================================


class TaskResult(BaseModel):
    """Result of task execution."""

    task_id: str = Field(description="Unique task identifier")
    status: str = Field(description="Status: success, failed, partial")
    result: Any = Field(description="Task result")
    error: Optional[str] = Field(default=None, description="Error message if failed")
    metadata: Dict[str, Any] = Field(
        default_factory=dict, description="Additional metadata"
    )
    duration_ms: Optional[int] = Field(
        default=None, description="Execution duration in milliseconds"
    )


class Decision(BaseModel):
    """Structured decision output."""

    decision: str = Field(description="The decision made")
    reasoning: str = Field(description="Reasoning behind the decision")
    alternatives: List[str] = Field(description="Alternatives considered")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence in decision")
    risks: List[str] = Field(default_factory=list, description="Potential risks")
    next_steps: List[str] = Field(description="Recommended next steps")


# ========================================================================
# SEARCH/QUERY MODELS
# ========================================================================


class SearchQuery(BaseModel):
    """Structured search query."""

    query: str = Field(description="Main search query")
    filters: Dict[str, Any] = Field(default_factory=dict, description="Search filters")
    sort_by: Optional[str] = Field(default=None, description="Sort field")
    limit: int = Field(default=10, ge=1, le=100, description="Number of results")
    include_fields: List[str] = Field(
        default_factory=list, description="Fields to include"
    )


class SearchResult(BaseModel):
    """Structured search result."""

    query: str = Field(description="Original query")
    total_results: int = Field(description="Total number of results")
    results: List[Dict[str, Any]] = Field(description="List of results")
    facets: Dict[str, List[str]] = Field(
        default_factory=dict, description="Faceted search results"
    )
    next_page_token: Optional[str] = Field(
        default=None, description="Token for pagination"
    )


# ========================================================================
# CONVERSATION MODELS
# ========================================================================


class Intent(BaseModel):
    """User intent classification."""

    primary_intent: str = Field(description="Primary user intent")
    secondary_intents: List[str] = Field(
        default_factory=list, description="Secondary intents"
    )
    entities: Dict[str, Any] = Field(
        default_factory=dict, description="Extracted entities"
    )
    confidence: float = Field(
        ge=0.0, le=1.0, description="Confidence in classification"
    )
    suggested_action: str = Field(description="Suggested action based on intent")


class Response(BaseModel):
    """Structured response."""

    content: str = Field(description="Main response content")
    type: str = Field(description="Response type: answer, clarification, suggestion")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence in response")
    sources: List[str] = Field(default_factory=list, description="Sources used")
    follow_up: Optional[str] = Field(
        default=None, description="Follow-up question or suggestion"
    )


# ========================================================================
# EXTRACTION MODELS
# ========================================================================


class ExtractedData(BaseModel):
    """Extracted structured data."""

    entities: Dict[str, List[str]] = Field(
        default_factory=dict, description="Extracted entities by type"
    )
    relationships: List[Dict[str, str]] = Field(
        default_factory=list, description="Relationships between entities"
    )
    facts: List[str] = Field(default_factory=list, description="Extracted facts")
    metadata: Dict[str, Any] = Field(
        default_factory=dict, description="Additional metadata"
    )
    source_text: Optional[str] = Field(default=None, description="Original source text")
