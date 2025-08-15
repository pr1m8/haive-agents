agents.memory.state
===================

.. py:module:: agents.memory.state


Classes
-------

.. autoapisummary::

   agents.memory.state.MemoryAgentState


Module Contents
---------------

.. py:class:: MemoryAgentState

   Bases: :py:obj:`haive.core.schema.prebuilt.messages_state.MessagesState`


   State for Memory Agent, extending MessagesState.

   Adds fields for storing and retrieving memories.


   .. autolink-examples:: MemoryAgentState
      :collapse:

   .. py:attribute:: extracted_memories
      :type:  list[haive.agents.memory.models.MemoryItem | haive.agents.memory.models.KnowledgeTriple]
      :value: None



   .. py:attribute:: memory_type
      :type:  str
      :value: None



   .. py:attribute:: model_config


   .. py:attribute:: recall_memories
      :type:  list[str]
      :value: None



   .. py:attribute:: should_save_memories
      :type:  bool
      :value: None



   .. py:attribute:: user_id
      :type:  str | None
      :value: None



