
:py:mod:`agents.memory_v2.conversation_memory_agent`
====================================================

.. py:module:: agents.memory_v2.conversation_memory_agent

Conversation Memory Agent using BaseRAGAgent.

This module provides conversation memory storage and retrieval using BaseRAGAgent
with semantic search over conversation history and optional time-weighting.


.. autolink-examples:: agents.memory_v2.conversation_memory_agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_v2.conversation_memory_agent.ConversationMemoryAgent
   agents.memory_v2.conversation_memory_agent.ConversationMemoryConfig
   agents.memory_v2.conversation_memory_agent.MessageDocumentConverter


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ConversationMemoryAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ConversationMemoryAgent {
        node [shape=record];
        "ConversationMemoryAgent" [label="ConversationMemoryAgent"];
      }

.. autoclass:: agents.memory_v2.conversation_memory_agent.ConversationMemoryAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ConversationMemoryConfig:

   .. graphviz::
      :align: center

      digraph inheritance_ConversationMemoryConfig {
        node [shape=record];
        "ConversationMemoryConfig" [label="ConversationMemoryConfig"];
        "pydantic.BaseModel" -> "ConversationMemoryConfig";
      }

.. autopydantic_model:: agents.memory_v2.conversation_memory_agent.ConversationMemoryConfig
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MessageDocumentConverter:

   .. graphviz::
      :align: center

      digraph inheritance_MessageDocumentConverter {
        node [shape=record];
        "MessageDocumentConverter" [label="MessageDocumentConverter"];
      }

.. autoclass:: agents.memory_v2.conversation_memory_agent.MessageDocumentConverter
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.memory_v2.conversation_memory_agent.demo_conversation_memory

.. py:function:: demo_conversation_memory()
   :async:


   Demo conversation memory agent functionality.


   .. autolink-examples:: demo_conversation_memory
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.memory_v2.conversation_memory_agent
   :collapse:
   
.. autolink-skip:: next
