"""Models for STORM interview functionality."""

from typing import Any

from pydantic import BaseModel, Field


class InterviewState(BaseModel):
    """State for interview process in STORM research."""

    interviewer: str = Field(default="", description="Name of the interviewer")
    interviewee: str = Field(default="", description="Name of the interviewee")
    questions: list[str] = Field(
        default_factory=list, description="Interview questions"
    )
    answers: list[str] = Field(default_factory=list, description="Interview answers")
    metadata: dict[str, Any] = Field(
        default_factory=dict, description="Additional metadata"
    )

    class Config:
        arbitrary_types_allowed = True
