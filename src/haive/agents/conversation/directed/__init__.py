"""Directed Conversation
===================

Conversations with explicit flow control directed by a moderator agent.

The directed conversation implements a flexible conversation pattern where a moderator
agent directs the flow of the conversation by explicitly selecting which participant
should speak next. This enables:

- Dynamic conversation flow based on content
- Targeted follow-up questions and responses
- Conversation branching and focusing
- Structured interviews and panel discussions
- Conditional speaker selection based on expertise

Unlike round-robin conversations that follow a fixed pattern, directed conversations
allow for organic development guided by a moderator's decisions about which participant
should contribute at each point.

Features:
--------
- Moderator agent with speaker selection control
- Configurable selection criteria
- Support for interview and panel formats
- Targeted questioning and response tracking
- Dynamic conversation flow based on content

Usage:
------
```python
from haive.agents.conversation import DirectedConversation

# Create a directed conversation (interview format)
interview = DirectedConversation.create_interview(
    interviewer="Interviewer",
    interviewees=["Expert1", "Expert2", "Expert3"],
    topic="Climate Change Solutions",
    max_rounds=5
)

# Run the conversation
result = interview.invoke()

# Access conversation results
messages = result["messages"]
```

The directed conversation is particularly useful for:
- Simulating interviews with multiple subjects
- Creating panel discussions with a moderator
- Implementing Q&A sessions with dynamic follow-up
- Content-driven conversations where flow matters more than turn equality
"""

from haive.agents.conversation.directed.agent import DirectedConversation
from haive.agents.conversation.directed.state import DirectedState

__all__ = ["DirectedConversation", "DirectedState"]
