agents.rag.simple.simple_rag
============================

.. py:module:: agents.rag.simple.simple_rag

.. autoapi-nested-parse::

   SimpleRAG - Class inheriting from MultiAgent.


   .. autolink-examples:: agents.rag.simple.simple_rag
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.simple.simple_rag.SimpleRAG


Module Contents
---------------

.. py:class:: SimpleRAG

   Bases: :py:obj:`haive.agents.multi.agent.MultiAgent`


   SimpleRAG inheriting from MultiAgent with sequential BaseRAGAgent + SimpleAgent.


   .. autolink-examples:: SimpleRAG
      :collapse:

   .. py:method:: create_agents() -> SimpleRAG

      Create the retriever and generator agents.


      .. autolink-examples:: create_agents
         :collapse:


   .. py:attribute:: llm_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: retriever_config
      :type:  haive.core.engine.retriever.BaseRetrieverConfig | haive.core.engine.vectorstore.VectorStoreConfig
      :value: None



