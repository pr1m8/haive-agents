"""
Debate Conversation
==================

Structured debate agent with formal positions, arguments, rebuttals, and judging.

The debate conversation implements a formal debate structure where participants argue
from assigned positions following a multi-phase conversational format that includes:

- Opening statements
- Main arguments with specified number per side
- Rebuttals to opposing arguments
- Closing statements
- Optional judging and scoring

This agent is ideal for simulating formal debates, exploring opposing viewpoints,
and creating structured argumentative conversations with clear positions.

Features:
--------
- Multiple debate formats (traditional, oxford, parliamentary)
- Configurable debate phases
- Position assignment and tracking
- Automatic argument and rebuttal counting
- Optional judge participant for scoring and feedback
- Comprehensive debate statistics and results

Usage:
------
```python
from haive.agents.conversation import DebateConversation

# Create a simple two-sided debate
debate = DebateConversation.create_simple_debate(
    topic="Artificial Intelligence Benefits Outweigh Risks",
    position_a=("Proponent", "AI benefits far outweigh potential risks"),
    position_b=("Skeptic", "AI risks outweigh the potential benefits"),
    enable_judge=True,
    arguments_per_side=3
)

# Run the debate
result = debate.invoke()

# Access debate results
messages = result["messages"]
winner = result.get("debate_winner")
```

The debate conversation is particularly useful for:
- Exploring different perspectives on complex topics
- Creating balanced discussions with formal structure
- Educational simulations of debate formats
- Testing argument strength and persuasive capabilities
"""

from haive.agents.conversation.debate.agent import DebateConversation
from haive.agents.conversation.debate.state import DebateState

__all__ = ["DebateConversation", "DebateState"]
