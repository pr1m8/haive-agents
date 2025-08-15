agents.memory_reorganized.base.state
====================================

.. py:module:: agents.memory_reorganized.base.state

.. autoapi-nested-parse::

   State core module.

   This module provides state functionality for the Haive framework.

   Classes:
       MemoryAgentState: MemoryAgentState implementation.


   .. autolink-examples:: agents.memory_reorganized.base.state
      :collapse:


Classes
-------

.. autoapisummary::

   agents.memory_reorganized.base.state.MemoryAgentState


Module Contents
---------------

.. py:class:: MemoryAgentState

   Bases: :py:obj:`agents.react.react.state.ReactAgentState`


   State for Memory Agent, extending ReactAgentState.

   Adds fields for storing and retrieving memories.


   .. autolink-examples:: MemoryAgentState
      :collapse:

   .. py:attribute:: extracted_memories
      :type:  list[agents.react.memory.models.MemoryItem | agents.react.memory.models.KnowledgeTriple]
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



