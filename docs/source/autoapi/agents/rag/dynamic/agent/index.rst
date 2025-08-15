agents.rag.dynamic.agent
========================

.. py:module:: agents.rag.dynamic.agent


Attributes
----------

.. autoapisummary::

   agents.rag.dynamic.agent.logger


Classes
-------

.. autoapisummary::

   agents.rag.dynamic.agent.DynamicRAGAgent


Module Contents
---------------

.. py:class:: DynamicRAGAgent(config: haive.agents.rag.dynamic.config.DynamicRAGConfig)

   Bases: :py:obj:`haive.agents.rag.base.agent.BaseRAGAgent`


   Implements a dynamic RAG pipeline that routes queries to appropriate data sources.


   .. autolink-examples:: DynamicRAGAgent
      :collapse:

   .. py:method:: _init_data_sources()

      Initialize all configured data sources.


      .. autolink-examples:: _init_data_sources
         :collapse:


   .. py:method:: _init_merger()

      Initialize the result merger.


      .. autolink-examples:: _init_merger
         :collapse:


   .. py:method:: _init_router()

      Initialize the query router.


      .. autolink-examples:: _init_router
         :collapse:


   .. py:method:: merge_results(state: dict[str, Any])

      Merge results from multiple sources.


      .. autolink-examples:: merge_results
         :collapse:


   .. py:method:: retrieve_from_sources(state: dict[str, Any])

      Retrieve documents from selected sources.


      .. autolink-examples:: retrieve_from_sources
         :collapse:


   .. py:method:: route_query(state: dict[str, Any])

      Route the query to appropriate data sources.


      .. autolink-examples:: route_query
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the Dynamic RAG workflow.


      .. autolink-examples:: setup_workflow
         :collapse:


.. py:data:: logger

