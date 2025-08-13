
:py:mod:`agents.reflection.message_transformer`
===============================================

.. py:module:: agents.reflection.message_transformer

Reflection patterns using Message Transformer V2.

This module implements reflection patterns that integrate with the message
transformation system, following the patterns described in:
- project_docs/active/patterns/reflection_agent_pattern.md (lines 565-594)
- packages/haive-core/src/haive/core/graph/node/message_transformation_v2.py

Key difference from structured output: This uses message transformation
to add reflection context to conversations, enabling more natural
reflection flows.


.. autolink-examples:: agents.reflection.message_transformer
   :collapse:

Classes
-------

.. autoapisummary::

   agents.reflection.message_transformer.ConversationalReflectionAgent
   agents.reflection.message_transformer.MessageTransformerReflectionAgent
   agents.reflection.message_transformer.ReflectionMessageFlow
   agents.reflection.message_transformer.SimpleReflectionTransformer


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ConversationalReflectionAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ConversationalReflectionAgent {
        node [shape=record];
        "ConversationalReflectionAgent" [label="ConversationalReflectionAgent"];
      }

.. autoclass:: agents.reflection.message_transformer.ConversationalReflectionAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MessageTransformerReflectionAgent:

   .. graphviz::
      :align: center

      digraph inheritance_MessageTransformerReflectionAgent {
        node [shape=record];
        "MessageTransformerReflectionAgent" [label="MessageTransformerReflectionAgent"];
      }

.. autoclass:: agents.reflection.message_transformer.MessageTransformerReflectionAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReflectionMessageFlow:

   .. graphviz::
      :align: center

      digraph inheritance_ReflectionMessageFlow {
        node [shape=record];
        "ReflectionMessageFlow" [label="ReflectionMessageFlow"];
      }

.. autoclass:: agents.reflection.message_transformer.ReflectionMessageFlow
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SimpleReflectionTransformer:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleReflectionTransformer {
        node [shape=record];
        "SimpleReflectionTransformer" [label="SimpleReflectionTransformer"];
      }

.. autoclass:: agents.reflection.message_transformer.SimpleReflectionTransformer
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.reflection.message_transformer.create_conversational_reflection_agent
   agents.reflection.message_transformer.create_message_transformer_reflection_agent
   agents.reflection.message_transformer.create_reflection_context_transformer
   agents.reflection.message_transformer.create_reflection_message_flow
   agents.reflection.message_transformer.example_conversational_reflection
   agents.reflection.message_transformer.example_message_transformer_reflection
   agents.reflection.message_transformer.example_reflection_message_flow
   agents.reflection.message_transformer.main

.. py:function:: create_conversational_reflection_agent(base_agent: haive.agents.simple.agent.SimpleAgent, name: str = 'conv_reflector', reflection_frequency: int = 3) -> ConversationalReflectionAgent

   Create a conversational reflection agent.


   .. autolink-examples:: create_conversational_reflection_agent
      :collapse:

.. py:function:: create_message_transformer_reflection_agent(name: str = 'mt_reflector', temperature: float = 0.3, **kwargs) -> MessageTransformerReflectionAgent

   Create a message transformer reflection agent.


   .. autolink-examples:: create_message_transformer_reflection_agent
      :collapse:

.. py:function:: create_reflection_context_transformer(messages: list[langchain_core.messages.BaseMessage]) -> list[langchain_core.messages.BaseMessage]

   Create a reflection context transformer function.

   This function adds reflection insights to conversation context,
   following the pattern from reflection_agent_pattern.md.

   :param messages: Input messages to transform

   :returns: Messages with reflection context added


   .. autolink-examples:: create_reflection_context_transformer
      :collapse:

.. py:function:: create_reflection_message_flow(primary_agent: haive.agents.simple.agent.SimpleAgent, reflection_agent: haive.agents.simple.agent.SimpleAgent | None = None, name: str = 'reflection_flow') -> ReflectionMessageFlow

   Create a reflection message flow system.


   .. autolink-examples:: create_reflection_message_flow
      :collapse:

.. py:function:: example_conversational_reflection()
   :async:


   Example: Conversational reflection with context injection.


   .. autolink-examples:: example_conversational_reflection
      :collapse:

.. py:function:: example_message_transformer_reflection()
   :async:


   Example: Reflection using message transformer patterns.


   .. autolink-examples:: example_message_transformer_reflection
      :collapse:

.. py:function:: example_reflection_message_flow()
   :async:


   Example: Complete reflection message flow system.


   .. autolink-examples:: example_reflection_message_flow
      :collapse:

.. py:function:: main()
   :async:


   Run all message transformer reflection examples.


   .. autolink-examples:: main
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.reflection.message_transformer
   :collapse:
   
.. autolink-skip:: next
