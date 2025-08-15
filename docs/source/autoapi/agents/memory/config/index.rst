agents.memory.config
====================

.. py:module:: agents.memory.config

.. autoapi-nested-parse::

   Memory Agent Configuration.


   .. autolink-examples:: agents.memory.config
      :collapse:


Classes
-------

.. autoapisummary::

   agents.memory.config.MemoryAgentConfig


Module Contents
---------------

.. py:class:: MemoryAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Configuration for the Memory Agent.


   .. autolink-examples:: MemoryAgentConfig
      :collapse:

   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: llm_node_name
      :type:  str
      :value: None



   .. py:attribute:: max_memories_per_retrieval
      :type:  int
      :value: None



   .. py:attribute:: memory_extract_node_name
      :type:  str
      :value: None



   .. py:attribute:: memory_extraction_engine
      :type:  Any
      :value: None



   .. py:attribute:: memory_extraction_prompt
      :type:  str
      :value: None



   .. py:attribute:: memory_load_node_name
      :type:  str
      :value: None



   .. py:attribute:: memory_save_node_name
      :type:  str
      :value: None



   .. py:attribute:: memory_system_prompt
      :type:  str
      :value: None



   .. py:attribute:: memory_type
      :type:  str
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: output_node_name
      :type:  str
      :value: None



   .. py:attribute:: runnable_config
      :type:  Any
      :value: None



   .. py:attribute:: state_schema
      :type:  Any
      :value: None



   .. py:attribute:: structured_output_schema
      :type:  Any
      :value: None



   .. py:attribute:: system_prompt
      :type:  str
      :value: None



   .. py:attribute:: tool_node_name
      :type:  str
      :value: None



   .. py:attribute:: vector_store
      :type:  Any
      :value: None



