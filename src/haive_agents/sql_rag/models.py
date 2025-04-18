from pydantic import BaseModel, Field, field_validator
from typing import List, Dict, Any, Optional, Literal


class Query(BaseModel):
    """Model for a query to the SQL database."""
    question: str = Field(..., description="The question to search the SQL database with.")


class SQLQueryOutput(BaseModel):
    """Validated structured output model for SQL query generation."""
    query: str = Field(..., description="The generated SQL query.")
    parameters: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Query parameters if placeholders are used (e.g., ?1, ?2)."
    )

    @field_validator("query", mode="before")
    def validate_sql_syntax(cls, query: str) -> str:
        """Ensure the query starts with a valid SQL keyword."""
        valid_keywords = ["SELECT", "WITH"]
        if not any(query.strip().upper().startswith(kw) for kw in valid_keywords):
            raise ValueError("Invalid SQL query. Must start with SELECT or WITH")
        return query


class SQLValidationOutput(BaseModel):
    """Represents the validation result of a SQL query's output."""
    errors: List[str] = Field(
        default_factory=list,
        description="List of syntax or semantic errors in the SQL statement."
    )
    is_valid: bool = Field(
        default=False,
        description="Whether the SQL query is valid."
    )
    suggestions: Optional[str] = Field(
        default=None,
        description="Suggestions for improving the SQL query."
    )


class SQLAnalysisOutput(BaseModel):
    """Represents the analysis of a natural language query."""
    relevant_tables: List[str] = Field(
        description="The tables that are relevant to the query."
    )
    needed_columns: List[str] = Field(
        default_factory=list,
        description="The columns that are needed to answer the query."
    )
    constraints: List[str] = Field(
        default_factory=list,
        description="Any constraints that should be applied in the WHERE clause."
    )
    aggregations: List[str] = Field(
        default_factory=list,
        description="Any aggregations that should be performed (COUNT, SUM, AVG, etc.)."
    )
    joins_needed: List[Dict[str, str]] = Field(
        default_factory=list,
        description="Any joins that need to be performed, with the tables to join."
    )
    complexity: Literal["simple", "medium", "complex"] = Field(
        default="simple",
        description="The complexity of the query."
    )


class GuardrailsOutput(BaseModel):
    """Output from the guardrails check."""
    decision: str = Field(
        description="Decision on whether to proceed with the query. Should be 'database' to proceed or 'end' to stop."
    )
    reason: Optional[str] = Field(
        default=None,
        description="Reason for the decision."
    )


class GradeHallucinations(BaseModel):
    """Binary score for hallucination present in generated answer."""
    binary_score: str = Field(
        description="Answer is grounded in the facts, 'yes' or 'no'"
    )


class GradeAnswer(BaseModel):
    """Binary score to assess answer addresses question."""
    binary_score: str = Field(
        description="Answer addresses the question, 'yes' or 'no'"
    )