agents.rag.filtered.agent
=========================

.. py:module:: agents.rag.filtered.agent


Attributes
----------

.. autoapisummary::

   agents.rag.filtered.agent.logger


Classes
-------

.. autoapisummary::

   agents.rag.filtered.agent.FilteredRAGAgent


Module Contents
---------------

.. py:class:: FilteredRAGAgent(config: haive.agents.rag.filtered.config.FilteredRAGConfig)

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.agents.rag.filtered.config.FilteredRAGConfig`\ ]


   RAG agent with document filtering capabilities.

   This agent implements a workflow that:
   1. Retrieves relevant documents for a query
   2. Filters documents based on relevance to the query
   3. Generates an answer based on the filtered documents

   Initialize the agent with document filtering capabilities.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: FilteredRAGAgent
      :collapse:

   .. py:method:: _initialize_components(config)

      Initialize all components for the agent.


      .. autolink-examples:: _initialize_components
         :collapse:


   .. py:method:: filter_documents(state: haive.agents.rag.filtered.state.FilteredRAGState) -> langgraph.types.Command

      Filter documents based on relevance to the query.

      :param state: Current state with query and retrieved documents

      :returns: Command with filtered documents


      .. autolink-examples:: filter_documents
         :collapse:


   .. py:method:: generate_answer(state: haive.agents.rag.filtered.state.FilteredRAGState) -> langgraph.types.Command

      Generate an answer based on filtered documents.

      :param state: Current state with query and filtered documents

      :returns: Command with generated answer


      .. autolink-examples:: generate_answer
         :collapse:


   .. py:method:: retrieve_documents(state: haive.agents.rag.filtered.state.FilteredRAGState) -> langgraph.types.Command

      Retrieve documents based on the query.

      :param state: Current state with query

      :returns: Command with retrieved documents


      .. autolink-examples:: retrieve_documents
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the filtered RAG workflow.

      Workflow:
      START → retrieve_documents → filter_documents → generate_answer → END


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:property:: retriever
      :type: Any


      Lazy-loaded retriever property.

      .. autolink-examples:: retriever
         :collapse:


.. py:data:: logger

