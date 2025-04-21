
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


def update_candidates(existing: list["Candidate"] | None = None,
                     updates: list["Candidate"] | str | None = None) -> list["Candidate"]:
    """Update candidate list, handling special cases like clearing.
    
    Args:
        existing: Current list of candidates
        updates: New candidates to add, or "clear" to empty the list
        
    Returns:
        Updated list of candidates
    """
    if existing is None:
        existing = []
    if updates is None:
        return existing
    if updates == "clear":
        return []
    # Concatenate the lists
    return existing + updates


class Candidate(BaseModel):
    """A candidate solution in the Tree of Thoughts algorithm.
    """
    content: str = Field(description="The candidate solution content")
    score: float | None = Field(default=None, description="Score assigned to this candidate")
    feedback: str | None = Field(default=None, description="Feedback on this candidate")
    metadata: dict[str, Any] = Field(default_factory=dict, description="Additional metadata")

    # Use Pydantic v2 configuration
    model_config = ConfigDict(
        validate_assignment=True,
        extra="allow",
        arbitrary_types_allowed=True,
    )

    def __str__(self) -> str:
        """String representation of the candidate."""
        content_preview = self.content[:50] + "..." if len(self.content) > 50 else self.content
        return f"Candidate(content='{content_preview}', score={self.score})"
