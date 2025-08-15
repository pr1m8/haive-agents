agents.rag.typed.agent
======================

.. py:module:: agents.rag.typed.agent


Attributes
----------

.. autoapisummary::

   agents.rag.typed.agent.logger


Classes
-------

.. autoapisummary::

   agents.rag.typed.agent.TypedRAGAgent


Module Contents
---------------

.. py:class:: TypedRAGAgent(config: haive.agents.rag.typed.config.TypedRAGConfig)

   Bases: :py:obj:`haive.agents.rag.base.agent.BaseRAGAgent`


   Implements Typed-RAG that classifies queries and routes to specialized handlers.

   Initialize with TypedRAGConfig.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TypedRAGAgent
      :collapse:

   .. py:method:: _init_components()

      Initialize all components.


      .. autolink-examples:: _init_components
         :collapse:


   .. py:method:: aggregate_answers(state: dict[str, Any])

      Aggregate information from different subqueries.


      .. autolink-examples:: aggregate_answers
         :collapse:


   .. py:method:: classify_query(state: dict[str, Any])

      Classify the query into a category.


      .. autolink-examples:: classify_query
         :collapse:


   .. py:method:: filter_documents(state: dict[str, Any])

      Filter documents for relevance.


      .. autolink-examples:: filter_documents
         :collapse:


   .. py:method:: generate_answer(state: dict[str, Any])

      Generate an answer from the documents.


      .. autolink-examples:: generate_answer
         :collapse:


   .. py:method:: generate_subqueries(state: dict[str, Any])

      Generate specialized subqueries based on query category.


      .. autolink-examples:: generate_subqueries
         :collapse:


   .. py:method:: retrieve_for_subqueries(state: dict[str, Any])

      Retrieve documents for each subquery.


      .. autolink-examples:: retrieve_for_subqueries
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the Typed-RAG workflow.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:attribute:: config


.. py:data:: logger

