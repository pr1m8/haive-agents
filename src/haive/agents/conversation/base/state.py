import logging
from typing import List, Optional

from haive.core.logging.rich_logger import LogLevel, get_logger
from haive.core.schema.prebuilt.messages_state import MessagesState
from haive.core.schema.state_schema import StateSchema
from pydantic import Field

logger = get_logger(__name__)
logger.set_level(LogLevel.WARNING)


class ConversationState(MessagesState):
    """
    Base conversation state extending MessagesState.

    MessagesState provides:
    - messages: List[BaseMessage] with add_messages reducer
    - __reducer_fields__ = {"messages": add_messages}
    """

    # Track conversation flow
    current_speaker: Optional[str] = Field(default=None)
    speakers: List[str] = Field(default_factory=list)
    round_number: int = Field(default=0)
    max_rounds: int = Field(default=10)

    # Conversation metadata
    topic: Optional[str] = Field(default=None)
    conversation_ended: bool = Field(default=False)
    mode: str = Field(default="round_robin")
