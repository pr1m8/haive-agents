agents.conversation.round_robin.agent
=====================================

.. py:module:: agents.conversation.round_robin.agent

.. autoapi-nested-parse::

   Round-robin conversation agent where each participant speaks in turn.


   .. autolink-examples:: agents.conversation.round_robin.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.conversation.round_robin.agent.logger


Classes
-------

.. autoapisummary::

   agents.conversation.round_robin.agent.RoundRobinConversation


Module Contents
---------------

.. py:class:: RoundRobinConversation

   Bases: :py:obj:`haive.agents.conversation.base.agent.BaseConversationAgent`


   Round-robin conversation where each agent speaks in a fixed order.

   Each participant gets exactly one turn per round, with the order
   maintained throughout the conversation.


   .. autolink-examples:: RoundRobinConversation
      :collapse:

   .. py:method:: __repr__() -> str


   .. py:method:: _custom_initialization(state: haive.agents.conversation.base.state.ConversationState) -> dict[str, Any]

      Add round-robin specific initialization.


      .. autolink-examples:: _custom_initialization
         :collapse:


   .. py:method:: _prepare_agent_input(state: haive.agents.conversation.base.state.ConversationState, agent_name: str) -> dict[str, Any]

      Prepare input with round context.


      .. autolink-examples:: _prepare_agent_input
         :collapse:


   .. py:method:: create_simple(participants: list[str], topic: str = 'General discussion', max_rounds: int = 3, system_message_template: str | None = None, **kwargs)
      :classmethod:


      Create a simple round-robin conversation with auto-generated agents.

      :param participants: List of participant names
      :param topic: Conversation topic
      :param max_rounds: Maximum number of rounds
      :param system_message_template: Template for system messages (use {name} for participant name)
      :param \*\*kwargs: Additional arguments for the conversation

      :returns: Configured RoundRobinConversation


      .. autolink-examples:: create_simple
         :collapse:


   .. py:method:: select_speaker(state: haive.agents.conversation.base.state.ConversationState) -> dict[str, Any]

      Select the next speaker in round-robin order.


      .. autolink-examples:: select_speaker
         :collapse:


   .. py:attribute:: announce_speaker
      :type:  bool
      :value: None



   .. py:attribute:: mode
      :type:  Literal['round_robin']
      :value: None



   .. py:attribute:: skip_unavailable
      :type:  bool
      :value: None



.. py:data:: logger

