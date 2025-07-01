"""Round Robin Conversation
=======================

A simple turn-based conversation agent where participants speak in sequence.

The round robin conversation follows a strict order of speakers, ensuring that each
participant gets exactly one turn per round. This is the most straightforward form of
multi-agent conversation, where:

- Participants speak in a fixed, predictable order
- Each speaker gets exactly one turn per round
- The conversation progresses through complete rounds
- Round counts and progress are automatically tracked

Features:
--------
- Configurable round limit
- Optional speaker announcements
- Ability to skip unavailable speakers
- Round context provided to each agent
- Simple factory method for quick setup

Usage:
------
```python
from haive.agents.conversation import RoundRobinConversation

# Create a simple round-robin conversation
conversation = RoundRobinConversation.create_simple(
    participants=["Alice", "Bob", "Charlie"],
    topic="The future of AI",
    max_rounds=3
)

# Run the conversation
result = conversation.invoke()

# Access the conversation messages
messages = result["messages"]
```

The round robin conversation is useful for structured discussions where turn equality
is important, or when simulating balanced group conversations.
"""

from haive.agents.conversation.round_robin.agent import RoundRobinConversation

__all__ = ["RoundRobinConversation"]
