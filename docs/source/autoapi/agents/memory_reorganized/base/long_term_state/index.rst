agents.memory_reorganized.base.long_term_state
==============================================

.. py:module:: agents.memory_reorganized.base.long_term_state

.. autoapi-nested-parse::

   State core module.

   This module provides state functionality for the Haive framework.

   Classes:
       LongTermMemoryState: LongTermMemoryState implementation.


   .. autolink-examples:: agents.memory_reorganized.base.long_term_state
      :collapse:


Classes
-------

.. autoapisummary::

   agents.memory_reorganized.base.long_term_state.LongTermMemoryState


Module Contents
---------------

.. py:class:: LongTermMemoryState

   Bases: :py:obj:`agents.react_agent.state.AgentState`


   State for the long term memory agent.


   .. autolink-examples:: LongTermMemoryState
      :collapse:

   .. py:attribute:: memories
      :type:  list[pydantic.BaseModel | agents.long_term_memory.models.KnowledgeTriple]
      :value: None



