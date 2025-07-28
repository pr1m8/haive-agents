"""Action generation models for LATS algorithm."""

from typing import List

from pydantic import BaseModel, Field


class CandidateAction(BaseModel):
    """A candidate action that can be taken from the current state."""

    action: str = Field(description="The action to take")
    reasoning: str = Field(description="Reasoning behind why this action might be good")
    expected_outcome: str = Field(
        description="Expected outcome if this action is taken"
    )
    confidence: float = Field(
        description="Confidence in this action (0.0-1.0)", ge=0.0, le=1.0
    )


class ActionGeneration(BaseModel):
    """Structured output for generating multiple candidate actions."""

    situation_analysis: str = Field(
        description="Analysis of the current situation and context"
    )

    candidate_actions: List[CandidateAction] = Field(
        description="List of candidate actions to consider", min_items=1, max_items=10
    )

    selection_criteria: str = Field(
        description="Criteria that should be used to select the best action"
    )

    diversity_check: str = Field(
        description="Explanation of how the candidate actions differ and explore different approaches"
    )
