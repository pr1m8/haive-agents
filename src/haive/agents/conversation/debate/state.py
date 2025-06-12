# src/haive/agents/conversation/debate.py
"""
Structured debate conversation agent with positions and argumentation.
"""

import logging
from typing import Any, Dict, List, Optional, Tuple

from haive.core.logging.rich_logger import LogLevel, get_logger
from pydantic import Field, model_validator

from haive.agents.conversation.base.state import ConversationState

logger = get_logger(__name__)
logger.set_level(LogLevel.WARNING)


class DebateState(ConversationState):
    """Extended state for debate conversations."""

    # Debate-specific fields
    debate_positions: Dict[str, str] = Field(default_factory=dict)
    arguments_made: Dict[str, List[str]] = Field(default_factory=dict)
    rebuttals: Dict[str, List[Tuple[str, str]]] = Field(
        default_factory=dict
    )  # (target, rebuttal)

    # Debate flow
    opening_statements_complete: bool = Field(default=False)
    in_rebuttal_phase: bool = Field(default=False)
    closing_statements_complete: bool = Field(default=False)

    # Scoring (optional)
    argument_scores: Dict[str, float] = Field(default_factory=dict)
    judge_feedback: List[str] = Field(default_factory=list)
