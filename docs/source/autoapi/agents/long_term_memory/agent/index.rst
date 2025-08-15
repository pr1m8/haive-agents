agents.long_term_memory.agent
=============================

.. py:module:: agents.long_term_memory.agent


Classes
-------

.. autoapisummary::

   agents.long_term_memory.agent.LongTermMemoryAgent
   agents.long_term_memory.agent.LongTermMemoryAgentConfig


Module Contents
---------------

.. py:class:: LongTermMemoryAgent(config: LongTermMemoryAgentConfig)

   Bases: :py:obj:`haive.agents.react.agent.ReactAgent`


   Agent for the long term memory.


   .. autolink-examples:: LongTermMemoryAgent
      :collapse:

   .. py:method:: load_memories(state: dict[str, Any], config: langchain_core.runnables.RunnableConfig) -> dict[str, Any]

      Load memories for the current conversation.

      :param state: The current state of the conversation.
      :type state: Dict[str, Any]
      :param config: The runtime configuration for the agent.
      :type config: RunnableConfig

      :returns: The updated state with loaded memories.
      :rtype: Dict[str, Any]


      .. autolink-examples:: load_memories
         :collapse:


   .. py:method:: setup_workflow() -> None


   .. py:attribute:: config
      :type:  LongTermMemoryAgentConfig


.. py:class:: LongTermMemoryAgentConfig

   Bases: :py:obj:`haive.agents.react.config.ReactAgentConfig`


   Config for the long term memory agent.


   .. autolink-examples:: LongTermMemoryAgentConfig
      :collapse:

   .. py:attribute:: aug_llm
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: state
      :type:  haive.agents.long_term_memory.state.LongTermMemoryState
      :value: None



   .. py:attribute:: state_schema
      :type:  haive.agents.long_term_memory.state.LongTermMemoryState
      :value: None



   .. py:attribute:: vs_config
      :type:  haive.core.models.vectorstore.base.VectorStoreConfig
      :value: None



