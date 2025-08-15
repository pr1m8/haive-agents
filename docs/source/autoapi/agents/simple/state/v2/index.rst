agents.simple.state.v2
======================

.. py:module:: agents.simple.state.v2

.. autoapi-nested-parse::

   State core module.

   This module provides state functionality for the Haive framework.

   Classes:
       SimpleAgentState: SimpleAgentState implementation.

   Functions:
       add_human_message: Add Human Message functionality.
       add_ai_message: Add Ai Message functionality.
       extract_last_message_content: Extract Last Message Content functionality.


   .. autolink-examples:: agents.simple.state.v2
      :collapse:


Classes
-------

.. autoapisummary::

   agents.simple.state.v2.SimpleAgentState


Module Contents
---------------

.. py:class:: SimpleAgentState

   Bases: :py:obj:`haive.core.schema.state_schema.StateSchema`


   Base state for simple agents.

   This provides a standard chat-based state with a messages field that
   supports proper message history management through the add_messages reducer.


   .. autolink-examples:: SimpleAgentState
      :collapse:

   .. py:method:: add_ai_message(content: str) -> SimpleAgentState

      Add an AI message to the state.

      :param content: Message content

      :returns: Self for chaining


      .. autolink-examples:: add_ai_message
         :collapse:


   .. py:method:: add_human_message(content: str) -> SimpleAgentState

      Add a human message to the state.

      :param content: Message content

      :returns: Self for chaining


      .. autolink-examples:: add_human_message
         :collapse:


   .. py:method:: extract_last_message_content() -> str | None

      Extract the content of the last message in the state.

      :returns: Content of the last message or None if no messages


      .. autolink-examples:: extract_last_message_content
         :collapse:


   .. py:method:: with_messages(messages: list[langchain_core.messages.BaseMessage]) -> SimpleAgentState
      :classmethod:


      Create a new instance with the given messages.

      :param messages: Initial messages

      :returns: New SimpleAgentState instance


      .. autolink-examples:: with_messages
         :collapse:


   .. py:attribute:: messages
      :type:  Annotated[collections.abc.Sequence[langchain_core.messages.BaseMessage], langgraph.graph.add_messages]
      :value: None



