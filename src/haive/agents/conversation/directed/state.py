# src/haive/agents/conversation/directed.py
"""
Directed conversation agent where participants respond to mentions and direct questions.
"""

import logging
import re
from typing import Any, Dict, List, Optional, Set

from haive.core.logging.rich_logger import LogLevel, get_logger
from langchain_core.messages import AIMessage, BaseMessage, SystemMessage
from pydantic import Field

from haive.agents.conversation.base.agent import BaseConversationAgent
from haive.agents.conversation.base.state import ConversationState

logger = get_logger(__name__)
logger.set_level(LogLevel.WARNING)


class DirectedState(ConversationState):
    """Extended state for directed conversations."""

    # Track who was mentioned
    mentioned_speakers: List[str] = Field(default_factory=list)
    pending_speakers: List[str] = Field(default_factory=list)
    # Track interaction patterns
    interaction_count: Dict[str, Dict[str, int]] = Field(
        default_factory=dict, description="Track who mentions whom"
    )
