"""Base Conversation Agent.

Core foundation classes for conversation agents that orchestrate multi-agent interactions.

This module provides the base infrastructure for all conversation agent types, with a
focus on:

- Multi-agent conversation orchestration
- Automatic state tracking with reducers
- Phase-based conversation management
- Message routing and agent execution
- Extensible graph-based conversation flow

The base module consists of two primary components:

1. **BaseConversationAgent**: Abstract base agent that implements the core conversation
   flow logic, speaker selection, agent execution, and extension hooks.
   (:class:`~haive.agents.conversation.base.agent.BaseConversationAgent`)

2. **ConversationState**: State schema with automatic tracking for conversation rounds,
   speaker history, and message accumulation using reducers.
   (:class:`~haive.agents.conversation.base.state.ConversationState`)

All conversation types in the package extend these base classes to implement their
specific conversation patterns while inheriting the core orchestration mechanisms.

Conversation types that extend this base module:
    - :mod:`~haive.agents.conversation.round_robin`: Turn-taking conversations
    - :mod:`~haive.agents.conversation.debate`: Structured debate conversations
    - :mod:`~haive.agents.conversation.directed`: Moderator-controlled conversations
    - :mod:`~haive.agents.conversation.collaberative`: Task-focused collaborative conversations
    - :mod:`~haive.agents.conversation.social_media`: Social media-style interactions

See Also:
    - :class:`~haive.agents.base.agent.Agent`: Parent class that BaseConversationAgent extends
    - :class:`~haive.agents.simple.agent.SimpleAgent`: Used for conversation participants
    - :class:`~haive.core.schema.state_schema.StateSchema`: Parent class of ConversationState
"""

from haive.agents.conversation.base.agent import BaseConversationAgent
from haive.agents.conversation.base.state import ConversationState

__all__ = ["BaseConversationAgent", "ConversationState"]
