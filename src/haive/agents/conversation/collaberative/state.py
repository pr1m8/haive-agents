# src/haive/agents/conversation/collaborative/state.py
"""
State for collaborative conversation agents.
"""

import operator
from typing import Any, Dict, List, Literal, Optional, Tuple

from pydantic import Field

from haive.agents.conversation.base.state import ConversationState


def merge_document_sections(
    current: Dict[str, str], update: Dict[str, str]
) -> Dict[str, str]:
    """Merge document sections, preserving existing content."""
    result = current.copy()
    for section, content in update.items():
        if section in result:
            # Append to existing content if there's already content
            if result[section] and content:
                result[section] = result[section].rstrip() + "\n" + content
            elif content:  # Only update if new content is non-empty
                result[section] = content
        else:
            result[section] = content
    return result


def merge_contribution_counts(
    current: Dict[str, int], update: Dict[str, int]
) -> Dict[str, int]:
    """Merge contribution counts by summing values."""
    result = current.copy()
    for contributor, count in update.items():
        result[contributor] = result.get(contributor, 0) + count
    return result


class CollaborativeState(ConversationState):
    """Extended state for collaborative conversations."""

    # Shared document/artifact
    shared_document: str = Field(default="")
    document_sections: Dict[str, str] = Field(default_factory=dict)

    # Contribution tracking
    contributions: List[Tuple[str, str, str]] = Field(
        default_factory=list,
        description="List of (contributor, section, content) tuples",
    )
    contribution_count: Dict[str, int] = Field(default_factory=dict)

    # Collaboration flow
    current_section: Optional[str] = Field(default=None)
    sections_order: List[str] = Field(default_factory=list)
    completed_sections: List[str] = Field(default_factory=list)

    # Review and consensus
    pending_reviews: List[Tuple[str, str]] = Field(
        default_factory=list, description="List of (section, content) pending review"
    )
    approvals: Dict[str, List[str]] = Field(
        default_factory=dict, description="Section -> list of approvers"
    )

    # Output format
    output_format: Literal["markdown", "code", "outline", "report"] = Field(
        default="markdown"
    )

    # Add custom reducers for proper merging
    __reducer_fields__ = {
        **ConversationState.__reducer_fields__,
        "contributions": operator.add,  # Accumulate contributions
        "document_sections": merge_document_sections,  # Merge sections properly
        "contribution_count": merge_contribution_counts,  # Sum contribution counts
        "completed_sections": operator.add,  # Accumulate completed sections
    }
