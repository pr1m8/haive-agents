# src/haive/agents/conversation/base/state.py
"""Base conversation state with automatic round tracking via reducers.

This module defines the ConversationState class, which is the foundational state schema
for all conversation types. It extends MessagesState with specialized tracking for
conversation rounds, speaker history, and flow management.

The state uses Pydantic for validation and reducer functions for automatic field updates,
allowing for elegant tracking of conversation progress without complex manual state management.
Key features include:

- Automatic message accumulation (inherited from MessagesState)
- Turn count tracking with automatic incrementation
- Speaker history with automatic appending
- Round calculation based on turn count and speaker count
- Computed properties for conversation progress and remaining speakers
"""

import operator

from haive.core.logging.rich_logger import LogLevel, get_logger
from haive.core.schema.prebuilt.messages_state import MessagesState
from pydantic import Field, computed_field

logger = get_logger(__name__)
logger.set_level(LogLevel.WARNING)


class ConversationState(MessagesState):
    """Base conversation state schema with automatic tracking and progress calculations.

    This state schema extends MessagesState with specialized fields and reducers for
    tracking multi-agent conversations. It provides automatic management of turns,
    rounds, speaker history, and conversation progress through a combination of
    Pydantic fields, reducers, and computed properties.

    Attributes:
        messages (List[BaseMessage]): Conversation messages (inherited from MessagesState)
        current_speaker (Optional[str]): The currently active speaker
        speakers (List[str]): List of all participant speaker names
        turn_count (int): Total number of speaking turns taken (auto-incremented)
        max_rounds (int): Maximum number of conversation rounds
        topic (Optional[str]): The conversation topic
        conversation_ended (bool): Flag indicating if conversation is complete
        mode (str): Conversation mode identifier (e.g., "round_robin", "debate")
        speaker_history (List[str]): Chronological history of speakers (auto-appended)

    Computed Properties:
        round_number (int): Current round number calculated from turns and speakers
        current_round_speakers (List[str]): Speakers who have spoken in current round
        remaining_speakers_this_round (List[str]): Speakers yet to speak in current round
        should_end_by_rounds (bool): Whether round limit has been reached
        turns_per_round (int): Number of turns in a complete round
        conversation_progress (float): Progress from 0.0 to 1.0

    Note:
        This state uses reducer functions for automatic field updates. When a turn is taken,
        the turn_count and speaker_history are automatically updated through reducers,
        allowing for clean state updates without manual tracking.
    """

    # Track conversation flow
    current_speaker: str | None = Field(default=None)
    speakers: list[str] = Field(default_factory=list)

    # Use reducer for automatic round counting
    turn_count: int = Field(
        default=0, description="Total number of turns taken (auto-incremented)"
    )

    max_rounds: int = Field(default=10)

    # Conversation metadata
    topic: str | None = Field(default=None)
    conversation_ended: bool = Field(default=False)
    mode: str = Field(default="round_robin")

    # Speaker history for tracking
    speaker_history: list[str] = Field(
        default_factory=list, description="History of speakers in order"
    )

    # Add reducers for automatic tracking
    __reducer_fields__ = {
        **MessagesState.__reducer_fields__,  # Inherit messages reducer
        "turn_count": operator.add,  # Auto-increment turns
        "speaker_history": operator.add,  # Append to history
    }

    @computed_field
    @property
    def round_number(self) -> int:
        """Compute current round based on turn count and number of speakers.

        Returns:
            Current round number (1-based)
        """
        if not self.speakers or self.turn_count == 0:
            return 0
        # Calculate rounds based on turns and speaker count
        return (self.turn_count - 1) // len(self.speakers) + 1

    @computed_field
    @property
    def current_round_speakers(self) -> list[str]:
        """Get list of speakers who have already spoken in current round.

        Returns:
            List of speaker names
        """
        if not self.speakers or self.round_number == 0:
            return []

        # Calculate based on speaker history
        start_idx = (self.round_number - 1) * len(self.speakers)
        end_idx = start_idx + (
            self.turn_count % len(self.speakers) or len(self.speakers)
        )

        return self.speaker_history[start_idx:end_idx]

    @computed_field
    @property
    def remaining_speakers_this_round(self) -> list[str]:
        """Get speakers who haven't spoken yet in current round.

        Returns:
            List of speaker names
        """
        if not self.speakers:
            return []

        current_speakers = set(self.current_round_speakers)
        return [s for s in self.speakers if s not in current_speakers]

    @computed_field
    @property
    def should_end_by_rounds(self) -> bool:
        """Check if conversation should end based on round limit.

        Returns:
            True if round limit reached
        """
        return self.round_number >= self.max_rounds

    @computed_field
    @property
    def turns_per_round(self) -> int:
        """Calculate expected turns per round.

        Returns:
            Number of turns in a complete round
        """
        return len(self.speakers) if self.speakers else 1

    @computed_field
    @property
    def conversation_progress(self) -> float:
        """Calculate conversation progress as percentage.

        Returns:
            Progress from 0.0 to 1.0
        """
        if self.max_rounds == 0:
            return 1.0
        return min(1.0, self.round_number / self.max_rounds)
