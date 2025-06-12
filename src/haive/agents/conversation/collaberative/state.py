# src/haive/agents/conversation/collaborative.py
"""
Collaborative conversation agent for building shared content together.
"""

import logging
import operator
from typing import Any, Dict, List, Literal, Optional, Tuple

from haive.core.logging.rich_logger import LogLevel, get_logger
from pydantic import Field

from haive.agents.conversation.base.state import ConversationState

logger = get_logger(__name__)
logger.set_level(LogLevel.WARNING)


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

    # Add custom reducer for contributions
    __reducer_fields__ = {
        **ConversationState.__reducer_fields__,
        "contributions": operator.add,  # Accumulate contributions
    }
