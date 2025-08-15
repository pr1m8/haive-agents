agents.rag.multi_strategy.agent
===============================

.. py:module:: agents.rag.multi_strategy.agent


Classes
-------

.. autoapisummary::

   agents.rag.multi_strategy.agent.MultiStrategyRAGAgent


Module Contents
---------------

.. py:class:: MultiStrategyRAGAgent

   Bases: :py:obj:`haive.agents.rag.self_corr.agent.SelfCorrectiveRAGAgent`


   RAG agent with multiple retrieval strategies.


   .. autolink-examples:: MultiStrategyRAGAgent
      :collapse:

   .. py:method:: _create_query_analyzer()

      Create a query analyzer from the configuration.


      .. autolink-examples:: _create_query_analyzer
         :collapse:


   .. py:method:: _create_query_rewriter()

      Create a query rewriter from the configuration.


      .. autolink-examples:: _create_query_rewriter
         :collapse:


   .. py:method:: _create_retriever_strategies()

      Create specialized retrievers from the configuration.


      .. autolink-examples:: _create_retriever_strategies
         :collapse:


   .. py:method:: _init_components()

      Initialize components for multiple strategies.


      .. autolink-examples:: _init_components
         :collapse:


   .. py:method:: analyze_query(state: dict[str, Any])

      Analyze the query to determine the appropriate strategy.


      .. autolink-examples:: analyze_query
         :collapse:


   .. py:method:: retrieve_with_strategy(state: dict[str, Any])

      Retrieve documents using the selected strategy.


      .. autolink-examples:: retrieve_with_strategy
         :collapse:


   .. py:method:: rewrite_query(state: dict[str, Any])

      Generate variations of the query for better retrieval.


      .. autolink-examples:: rewrite_query
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the multi-strategy RAG workflow.


      .. autolink-examples:: setup_workflow
         :collapse:


