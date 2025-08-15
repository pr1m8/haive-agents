agents.memory_reorganized.agents.long_term_v2
=============================================

.. py:module:: agents.memory_reorganized.agents.long_term_v2

.. autoapi-nested-parse::

   Agent core module.

   This module provides agent functionality for the Haive framework.

   Classes:
       LongTermMemoryAgentConfig: LongTermMemoryAgentConfig implementation.
       LongTermMemoryAgent: LongTermMemoryAgent implementation.

   Functions:
       load_memories: Load Memories functionality.
       setup_workflow: Setup Workflow functionality.


   .. autolink-examples:: agents.memory_reorganized.agents.long_term_v2
      :collapse:


Classes
-------

.. autoapisummary::

   agents.memory_reorganized.agents.long_term_v2.LongTermMemoryAgent
   agents.memory_reorganized.agents.long_term_v2.LongTermMemoryAgentConfig


Module Contents
---------------

.. py:class:: LongTermMemoryAgent(config: LongTermMemoryAgentConfig)

   Bases: :py:obj:`ReactAgent`


   Agent for the long term memory.


   .. autolink-examples:: LongTermMemoryAgent
      :collapse:

   .. py:method:: load_memories(state: State, config: langchain_core.runnables.RunnableConfig) -> State

      Load memories for the current conversation.

      :param state: The current state of the conversation.
      :type state: schemas.State
      :param config: The runtime configuration for the agent.
      :type config: RunnableConfig

      :returns: The updated state with loaded memories.
      :rtype: State


      .. autolink-examples:: load_memories
         :collapse:


   .. py:method:: setup_workflow() -> None


   .. py:attribute:: config
      :type:  LongTermMemoryAgentConfig


.. py:class:: LongTermMemoryAgentConfig

   Bases: :py:obj:`haive.agents.memory_reorganized.agents.react_agent2.agent.ReactAgentConfig`


   Config for the long term memory agent.


   .. autolink-examples:: LongTermMemoryAgentConfig
      :collapse:

   .. py:attribute:: aug_llm
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: state
      :type:  haive.agents.memory_reorganized.agents.long_term_memory.state.LongTermMemoryState
      :value: None



   .. py:attribute:: state_schema
      :type:  haive.agents.memory_reorganized.agents.long_term_memory.state.LongTermMemoryState
      :value: None



   .. py:attribute:: vs_config
      :type:  haive.core.models.vectorstore.base.VectorStoreConfig
      :value: None



