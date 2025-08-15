agents.rag.simple_rag_agent_v4
==============================

.. py:module:: agents.rag.simple_rag_agent_v4

.. autoapi-nested-parse::

   SimpleRAGAgentV4 - Simple RAG with retrieved documents in prompt.


   .. autolink-examples:: agents.rag.simple_rag_agent_v4
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.simple_rag_agent_v4.SimpleRAGAgentV4


Module Contents
---------------

.. py:class:: SimpleRAGAgentV4

   Bases: :py:obj:`haive.agents.multi.agent.MultiAgent`


   Simple RAG = MultiAgent([BaseRAGAgent, AnswerAgent], mode="sequential").


   .. autolink-examples:: SimpleRAGAgentV4
      :collapse:

   .. py:method:: model_post_init(__context)

      Set up the agents with the configs.


      .. autolink-examples:: model_post_init
         :collapse:


   .. py:attribute:: agents
      :type:  list
      :value: None



   .. py:attribute:: execution_mode
      :type:  str
      :value: None



   .. py:attribute:: llm_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: vector_store_config
      :type:  haive.core.engine.vectorstore.vectorstore.VectorStoreConfig
      :value: None



