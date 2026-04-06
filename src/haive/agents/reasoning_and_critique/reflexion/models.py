"""Pydantic models for Reflexion structured output."""

from pydantic import BaseModel, Field


class Reflection(BaseModel):
    """Structured critique of a draft answer."""

    missing: str = Field(description="Critique of what is missing from the answer.")
    superfluous: str = Field(description="Critique of what is superfluous in the answer.")
    score: int = Field(
        default=5,
        ge=0,
        le=10,
        description="Quality score from 0-10.",
    )


class AnswerQuestion(BaseModel):
    """Initial answer with self-reflection and follow-up queries."""

    answer: str = Field(description="~250 word detailed answer to the question.")
    reflection: Reflection = Field(description="Your reflection on the initial answer.")
    search_queries: list[str] = Field(
        default_factory=list,
        description=(
            "1-3 search queries for researching improvements to address "
            "the critique of your current answer."
        ),
    )


class ReviseAnswer(AnswerQuestion):
    """Revised answer incorporating reflection and references."""

    references: list[str] = Field(
        description="Citations motivating your updated answer.",
    )
