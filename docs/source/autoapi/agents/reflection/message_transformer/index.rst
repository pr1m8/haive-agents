agents.reflection.message_transformer
=====================================

.. py:module:: agents.reflection.message_transformer

.. autoapi-nested-parse::

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


Attributes
----------

.. autoapisummary::

   agents.reflection.message_transformer.MESSAGE_TRANSFORMER_AVAILABLE


Classes
-------

.. autoapisummary::

   agents.reflection.message_transformer.ConversationalReflectionAgent
   agents.reflection.message_transformer.MessageTransformerReflectionAgent
   agents.reflection.message_transformer.ReflectionMessageFlow
   agents.reflection.message_transformer.SimpleReflectionTransformer


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


Module Contents
---------------

.. py:class:: ConversationalReflectionAgent(base_agent: haive.agents.simple.agent.SimpleAgent, name: str = 'conversational_reflection', reflection_frequency: int = 3)

   Reflection agent that maintains conversational flow with reflection context.

   This integrates message transformation to create natural reflection
   patterns within conversations, rather than separate analysis steps.

   Initialize conversational reflection agent.

   :param base_agent: The base agent to add reflection to
   :param name: Name for the reflection system
   :param reflection_frequency: How often to inject reflection (every N messages)


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ConversationalReflectionAgent
      :collapse:

   .. py:method:: run_with_reflection(input_data: str | dict[str, Any]) -> dict[str, Any]
      :async:


      Run the base agent with reflection context injection.

      :param input_data: Input for the base agent

      :returns: Agent result with reflection context applied


      .. autolink-examples:: run_with_reflection
         :collapse:


   .. py:attribute:: base_agent


   .. py:attribute:: context_transformer


   .. py:attribute:: message_count
      :value: 0



   .. py:attribute:: name
      :value: 'conversational_reflection'



   .. py:attribute:: reflection_frequency
      :value: 3



.. py:class:: MessageTransformerReflectionAgent(name: str = 'transformer_reflection_agent', temperature: float = 0.3, preserve_first_message: bool = True)

   Reflection agent using message transformer v2 pattern.

   Instead of structured output extraction, this uses message transformation
   to add reflection context directly to conversations, following the
   pattern from reflection_agent_pattern.md lines 565-594.

   Initialize message transformer reflection agent.

   :param name: Name for the agent
   :param temperature: Temperature for LLM generation
   :param preserve_first_message: Whether to preserve first message in transformation


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MessageTransformerReflectionAgent
      :collapse:

   .. py:method:: reflect_on_conversation(messages: list[langchain_core.messages.BaseMessage], original_query: str | None = None) -> dict[str, Any]
      :async:


      Perform reflection analysis using message transformation.

      :param messages: The conversation messages to reflect on
      :param original_query: Optional original query for context

      :returns: Dict containing reflection analysis and transformed messages


      .. autolink-examples:: reflect_on_conversation
         :collapse:


   .. py:attribute:: analyzer


   .. py:attribute:: name
      :value: 'transformer_reflection_agent'



   .. py:attribute:: preserve_first_message
      :value: True



.. py:class:: ReflectionMessageFlow(primary_agent: haive.agents.simple.agent.SimpleAgent, reflection_agent: haive.agents.simple.agent.SimpleAgent | None = None, name: str = 'reflection_flow')

   Manages reflection flow using message transformations.

   This creates a workflow where reflection insights are naturally
   integrated into message flows rather than separate analysis steps.

   Initialize reflection message flow.

   :param primary_agent: Main agent for primary responses
   :param reflection_agent: Optional dedicated reflection agent
   :param name: Name for the flow system


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReflectionMessageFlow
      :collapse:

   .. py:method:: run_primary_with_reflection(query: str, include_reflection: bool = True) -> dict[str, Any]
      :async:


      Run primary agent and optionally add reflection insights.

      :param query: Input query
      :param include_reflection: Whether to include reflection analysis

      :returns: Combined results with optional reflection insights


      .. autolink-examples:: run_primary_with_reflection
         :collapse:


   .. py:attribute:: ai_to_human_transformer


   .. py:attribute:: name
      :value: 'reflection_flow'



   .. py:attribute:: primary_agent


   .. py:attribute:: reflection_transformer


.. py:class:: SimpleReflectionTransformer(preserve_first_message: bool = True)

   Simple reflection transformer for when message_transformation_v2 is not available.


   .. autolink-examples:: SimpleReflectionTransformer
      :collapse:

   .. py:method:: _apply_transformation(messages: list[langchain_core.messages.BaseMessage]) -> list[langchain_core.messages.BaseMessage]

      Apply simple reflection transformation: swap AI ↔ Human roles.


      .. autolink-examples:: _apply_transformation
         :collapse:


   .. py:attribute:: preserve_first_message
      :value: True



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

.. py:data:: MESSAGE_TRANSFORMER_AVAILABLE
   :value: True


