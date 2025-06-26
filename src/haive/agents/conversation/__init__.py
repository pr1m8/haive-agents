"""
Conversation Agents
==================

A suite of multi-agent conversation orchestrators for facilitating different types of
agent-to-agent interactions and dialogues.

This package provides specialized conversation frameworks that enable multiple agents
to interact with each other according to different patterns, structures, and rules.

Core conversation types:
------------------------
- **Base**: Foundation for all conversation agents with core orchestration logic
  (:class:`~haive.agents.conversation.base.agent.BaseConversationAgent`,
   :class:`~haive.agents.conversation.base.state.ConversationState`)

- **Round Robin**: Simple turn-taking conversation where each agent speaks in sequence
  (:class:`~haive.agents.conversation.round_robin.agent.RoundRobinConversation`)

- **Directed**: Conversations with a directed flow controlled by a moderator
  (:class:`~haive.agents.conversation.directed.agent.DirectedConversation`)

- **Debate**: Structured debates with positions, arguments, rebuttals and judging
  (:class:`~haive.agents.conversation.debate.agent.DebateConversation`,
   :class:`~haive.agents.conversation.debate.state.DebateState`)

- **Collaborative**: Multiple agents collaborating on a shared task
  (:class:`~haive.agents.conversation.collaberative.agent.CollaborativeConversation`)

- **Social Media**: Simulated social media interactions with posts, replies, and reactions
  (:class:`~haive.agents.conversation.social_media.agent.SocialMediaConversation`,
   :class:`~haive.agents.conversation.social_media.models.Post`)

Each conversation type extends the BaseConversationAgent with specialized behavior for
its particular interaction pattern, while sharing the common state tracking system,
message handling, and orchestration framework.

See Also:
    - :mod:`~haive.agents.base.agent`: Base agent classes that conversation agents extend
    - :mod:`~haive.agents.simple.agent`: Simple agent used for conversation participants
    - :mod:`~haive.core.graph.state_graph`: State graph system for conversation flow
"""

from haive.agents.conversation.base.agent import BaseConversationAgent
from haive.agents.conversation.collaberative.agent import CollaborativeConversation
from haive.agents.conversation.debate.agent import DebateConversation
from haive.agents.conversation.directed.agent import DirectedConversation
from haive.agents.conversation.round_robin.agent import RoundRobinConversation
from haive.agents.conversation.social_media.agent import SocialMediaConversation

__all__ = [
    "BaseConversationAgent",
    "RoundRobinConversation",
    "DirectedConversation",
    "DebateConversation",
    "CollaborativeConversation",
    "SocialMediaConversation",
]
