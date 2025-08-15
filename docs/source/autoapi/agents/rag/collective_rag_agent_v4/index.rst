agents.rag.collective_rag_agent_v4
==================================

.. py:module:: agents.rag.collective_rag_agent_v4

.. autoapi-nested-parse::

   CollectiveRAGAgent - Multiple RAG sources with synthesis.


   .. autolink-examples:: agents.rag.collective_rag_agent_v4
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.collective_rag_agent_v4.CollectiveRAGAgent


Module Contents
---------------

.. py:class:: CollectiveRAGAgent

   Bases: :py:obj:`haive.agents.multi.agent.MultiAgent`


   Collective RAG = Multiple SimpleRAGAgent + SynthesisAgent, parallel then sequential.


   .. autolink-examples:: CollectiveRAGAgent
      :collapse:

   .. py:attribute:: agents
      :type:  list
      :value: None



   .. py:attribute:: execution_mode
      :type:  str
      :value: None



