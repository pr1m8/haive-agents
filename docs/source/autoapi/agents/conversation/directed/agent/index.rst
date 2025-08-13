
:py:mod:`agents.conversation.directed.agent`
============================================

.. py:module:: agents.conversation.directed.agent

Directed conversation agent where participants respond to mentions and direct questions.
from typing import Any
Uses structured output models for robust speaker selection and interaction tracking.


.. autolink-examples:: agents.conversation.directed.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.conversation.directed.agent.DirectedConversation
   agents.conversation.directed.agent.DirectedConversationConfig
   agents.conversation.directed.agent.InteractionPattern
   agents.conversation.directed.agent.MentionType
   agents.conversation.directed.agent.SpeakerMention
   agents.conversation.directed.agent.SpeakerSelectionResult


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DirectedConversation:

   .. graphviz::
      :align: center

      digraph inheritance_DirectedConversation {
        node [shape=record];
        "DirectedConversation" [label="DirectedConversation"];
        "haive.agents.conversation.base.agent.BaseConversationAgent" -> "DirectedConversation";
      }

.. autoclass:: agents.conversation.directed.agent.DirectedConversation
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DirectedConversationConfig:

   .. graphviz::
      :align: center

      digraph inheritance_DirectedConversationConfig {
        node [shape=record];
        "DirectedConversationConfig" [label="DirectedConversationConfig"];
        "pydantic.BaseModel" -> "DirectedConversationConfig";
      }

.. autopydantic_model:: agents.conversation.directed.agent.DirectedConversationConfig
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

   Inheritance diagram for InteractionPattern:

   .. graphviz::
      :align: center

      digraph inheritance_InteractionPattern {
        node [shape=record];
        "InteractionPattern" [label="InteractionPattern"];
        "pydantic.BaseModel" -> "InteractionPattern";
      }

.. autopydantic_model:: agents.conversation.directed.agent.InteractionPattern
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

   Inheritance diagram for MentionType:

   .. graphviz::
      :align: center

      digraph inheritance_MentionType {
        node [shape=record];
        "MentionType" [label="MentionType"];
        "str" -> "MentionType";
        "enum.Enum" -> "MentionType";
      }

.. autoclass:: agents.conversation.directed.agent.MentionType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **MentionType** is an Enum defined in ``agents.conversation.directed.agent``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SpeakerMention:

   .. graphviz::
      :align: center

      digraph inheritance_SpeakerMention {
        node [shape=record];
        "SpeakerMention" [label="SpeakerMention"];
        "pydantic.BaseModel" -> "SpeakerMention";
      }

.. autopydantic_model:: agents.conversation.directed.agent.SpeakerMention
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

   Inheritance diagram for SpeakerSelectionResult:

   .. graphviz::
      :align: center

      digraph inheritance_SpeakerSelectionResult {
        node [shape=record];
        "SpeakerSelectionResult" [label="SpeakerSelectionResult"];
        "pydantic.BaseModel" -> "SpeakerSelectionResult";
      }

.. autopydantic_model:: agents.conversation.directed.agent.SpeakerSelectionResult
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





.. rubric:: Related Links

.. autolink-examples:: agents.conversation.directed.agent
   :collapse:
   
.. autolink-skip:: next
