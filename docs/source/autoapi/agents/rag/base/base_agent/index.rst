agents.rag.base.base_agent
==========================

.. py:module:: agents.rag.base.base_agent


Classes
-------

.. autoapisummary::

   agents.rag.base.base_agent.BaseRAGAgent


Module Contents
---------------

.. py:class:: BaseRAGAgent

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.agents.rag.base.config.BaseRAGConfig`\ ]


   Simple base RAG agent with retrieve and generate functionality.


   .. autolink-examples:: BaseRAGAgent
      :collapse:

   .. py:method:: generate_answer(state: dict[str, Any])

      Generate an answer based on retrieved documents.


      .. autolink-examples:: generate_answer
         :collapse:


   .. py:method:: retrieve(state: dict[str, Any])

      Retrieve documents based on the query.


      .. autolink-examples:: retrieve
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the RAG workflow for this agent.


      .. autolink-examples:: setup_workflow
         :collapse:


