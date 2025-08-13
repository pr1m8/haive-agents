
:py:mod:`agents.conversation.base.agent`
========================================

.. py:module:: agents.conversation.base.agent

Base conversation agent providing core multi-agent conversation functionality.

This base class handles the orchestration of conversations between multiple agents,
with support for different conversation modes and patterns. It implements the core
graph-based state management system that all conversation types extend.

The BaseConversationAgent provides:

1. A common orchestration flow for all conversation types
2. Agent compilation and execution management
3. Message routing and processing
4. Automatic state tracking via reducers
5. Conversation initialization and conclusion
6. Extension points for specialized conversation behaviors

The conversation flow follows a standard pattern:
initialize → select_speaker → execute_agent → process_response → check_end → conclude

Each conversation type extends this base by implementing the abstract methods,
particularly the `select_speaker` method that defines the conversation pattern.


.. autolink-examples:: agents.conversation.base.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.conversation.base.agent.BaseConversationAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BaseConversationAgent:

   .. graphviz::
      :align: center

      digraph inheritance_BaseConversationAgent {
        node [shape=record];
        "BaseConversationAgent" [label="BaseConversationAgent"];
        "haive.agents.base.agent.Agent" -> "BaseConversationAgent";
      }

.. autoclass:: agents.conversation.base.agent.BaseConversationAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.conversation.base.agent
   :collapse:
   
.. autolink-skip:: next
