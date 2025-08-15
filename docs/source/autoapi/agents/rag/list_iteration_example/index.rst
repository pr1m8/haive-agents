agents.rag.list_iteration_example
=================================

.. py:module:: agents.rag.list_iteration_example

.. autoapi-nested-parse::

   Example of using ListIterationNode with RAG agents.

   Shows how to use the list iteration pattern for processing multiple queries
   or documents through RAG agents.


   .. autolink-examples:: agents.rag.list_iteration_example
      :collapse:


Functions
---------

.. autoapisummary::

   agents.rag.list_iteration_example.create_document_summarizer
   agents.rag.list_iteration_example.create_entity_extractor
   agents.rag.list_iteration_example.create_multi_query_processor
   agents.rag.list_iteration_example.create_parallel_document_grader
   agents.rag.list_iteration_example.example_graph_usage


Module Contents
---------------

.. py:function:: create_document_summarizer() -> Any

   Create a list iteration node that summarizes multiple documents.


   .. autolink-examples:: create_document_summarizer
      :collapse:

.. py:function:: create_entity_extractor() -> Any

   Create a list iteration node for entity extraction.


   .. autolink-examples:: create_entity_extractor
      :collapse:

.. py:function:: create_multi_query_processor(documents: list[langchain_core.documents.Document])

   Create a list iteration node that processes multiple queries.


   .. autolink-examples:: create_multi_query_processor
      :collapse:

.. py:function:: create_parallel_document_grader() -> Any

   Create a list iteration node that grades documents in parallel.


   .. autolink-examples:: create_parallel_document_grader
      :collapse:

.. py:function:: example_graph_usage() -> Any

   Example of how to use list iteration nodes in a graph.


   .. autolink-examples:: example_graph_usage
      :collapse:

