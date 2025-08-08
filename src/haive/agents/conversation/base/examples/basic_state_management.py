#!/usr/bin/env python3
"""Basic State Management Example for Base Conversation Agents.

This example demonstrates the core state management capabilities of the base
conversation system, including automatic tracking, computed properties, and
reducer-based state updates.
"""

import asyncio
import contextlib
import operator
from typing import Any

from pydantic import Field

from haive.agents.conversation.base import ConversationState

# Functions not available: create_conversation_state, get_conversation_progress, validate_conversation_participants
from haive.agents.simple import SimpleAgent


# TODO: Implement these helper functions properly
def create_conversation_state(participants, topic, max_rounds=10):
    """Create a conversation state with participants."""
    return ConversationState(
        participants=[p.name if hasattr(p, "name") else str(p) for p in participants],
        topic=topic,
        max_rounds=max_rounds,
    )


def get_conversation_progress(state):
    """Get conversation progress information."""
    return {
        "current_round": getattr(state, "current_round", 0),
        "max_rounds": getattr(state, "max_rounds", 10),
        "completion": getattr(state, "current_round", 0)
        / getattr(state, "max_rounds", 10),
    }


def validate_conversation_participants(participants):
    """Validate conversation participants."""
    if not participants or len(participants) < 2:
        raise ValueError("At least 2 participants required for conversation")
    return True


def demonstrate_basic_state_creation() -> Any:
    """Demonstrate basic conversation state creation and properties."""
    # Create simple agents
    alice = SimpleAgent(name="Alice")
    bob = SimpleAgent(name="Bob")
    charlie = SimpleAgent(name="Charlie")

    # Create conversation state
    state = create_conversation_state(
        participants=[alice, bob, charlie],
        topic="Future of Artificial Intelligence",
        max_rounds=5,
    )

    return state, [alice, bob, charlie]


def demonstrate_state_updates(state: ConversationState):
    """Demonstrate reducer-based state updates."""
    # Simulate first turn (Alice speaks)
    state = state.model_copy(
        update={
            "turn_count": 1,
            "speaker_history": ["Alice"],
            "current_speaker": "Alice",
        }
    )

    # Simulate second turn (Bob speaks)
    state = state.model_copy(
        update={
            # This will be added to existing count (becomes 2)
            "turn_count": 1,
            # This will be appended to existing history
            "speaker_history": ["Bob"],
            "current_speaker": "Bob",
        }
    )

    # Simulate third turn (Charlie speaks - completes round 1)
    state = state.model_copy(
        update={
            "turn_count": 1,
            "speaker_history": ["Charlie"],
            "current_speaker": "Charlie",
        }
    )

    return state


def demonstrate_computed_properties(state: ConversationState):
    """Demonstrate computed properties for conversation analysis."""
    # Simulate several more turns to show progress
    for _round_num in range(2, 6):  # Rounds 2-5
        for speaker in state.speakers:
            state = state.model_copy(
                update={
                    "turn_count": 1,
                    "speaker_history": [speaker],
                    "current_speaker": speaker,
                }
            )

    return state


def demonstrate_progress_tracking(state: ConversationState):
    """Demonstrate progress tracking utilities."""
    progress_info = get_conversation_progress(state)

    for _key, value in progress_info.items():
        if isinstance(value, float):
            pass
        else:
            pass


def demonstrate_participant_validation() -> None:
    """Demonstrate participant validation."""
    # Valid participants
    alice = SimpleAgent(name="Alice")
    bob = SimpleAgent(name="Bob")
    charlie = SimpleAgent(name="Charlie")

    with contextlib.suppress(ValueError):
        validate_conversation_participants([alice, bob, charlie])

    # Test with duplicate names
    duplicate_alice = SimpleAgent(name="Alice")  # Same name as alice

    with contextlib.suppress(ValueError):
        validate_conversation_participants([alice, bob, duplicate_alice])

    # Test with insufficient participants
    try:
        validate_conversation_participants([alice])  # Only one participant
    except ValueError:
        pass


def demonstrate_custom_state_fields() -> Any:
    """Demonstrate extending ConversationState with custom fields."""

    class ExtendedConversationState(ConversationState):
        """Extended conversation state with custom fields."""

        # Custom fields
        quality_scores: list[float] = Field(default_factory=list)
        engagement_metrics: dict[str, float] = Field(default_factory=dict)

        # Custom reducers
        __reducer_fields__ = {
            **ConversationState.__reducer_fields__,
            "quality_scores": operator.add,  # Append quality scores
        }

        @property
        def average_quality(self) -> float:
            """Calculate average conversation quality."""
            if not self.quality_scores:
                return 0.0
            return sum(self.quality_scores) / len(self.quality_scores)

    # Create extended state
    SimpleAgent(name="Alice")
    SimpleAgent(name="Bob")

    extended_state = ExtendedConversationState(
        speakers=["Alice", "Bob"], topic="Quality conversation example", max_rounds=3
    )

    # Update with custom data
    extended_state = extended_state.model_copy(
        update={
            "quality_scores": [8.5, 7.2],  # Will be appended
            "engagement_metrics": {"participation": 0.85, "sentiment": 0.72},
        }
    )


async def main():
    """Run all state management demonstrations."""
    # Basic state creation
    state, participants = demonstrate_basic_state_creation()

    # Demonstrate participant validation
    demonstrate_participant_validation()

    # State updates via reducers
    state = demonstrate_state_updates(state)

    # Computed properties
    state = demonstrate_computed_properties(state)

    # Progress tracking utilities
    demonstrate_progress_tracking(state)

    # Custom state extensions
    demonstrate_custom_state_fields()


if __name__ == "__main__":
    asyncio.run(main())
