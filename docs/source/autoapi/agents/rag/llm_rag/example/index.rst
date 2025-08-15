agents.rag.llm_rag.example
==========================

.. py:module:: agents.rag.llm_rag.example

.. autoapi-nested-parse::

   Example usage of the LLM RAG Agent.

   from typing import Any
   This script demonstrates how to:
   1. Create and configure an LLM RAG agent
   2. Run queries and access the results
   3. Customize the agent's behavior


   .. autolink-examples:: agents.rag.llm_rag.example
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.llm_rag.example.SAMPLE_DOCUMENTS
   agents.rag.llm_rag.example.logger


Functions
---------

.. autoapisummary::

   agents.rag.llm_rag.example.compare_agent_configurations
   agents.rag.llm_rag.example.create_llm_rag_agent
   agents.rag.llm_rag.example.main
   agents.rag.llm_rag.example.run_example_queries


Module Contents
---------------

.. py:function:: compare_agent_configurations() -> None

   Compare different agent configurations side by side.


   .. autolink-examples:: compare_agent_configurations
      :collapse:

.. py:function:: create_llm_rag_agent(use_relevance_checker=True, return_documents=3) -> Any

   Creates and configures an LLM RAG agent.

   :param use_relevance_checker: Whether to include a relevance checking component
   :type use_relevance_checker: bool
   :param return_documents: Number of documents to retrieve
   :type return_documents: int

   :returns: Configured agent instance
   :rtype: LLMRAGAgent


   .. autolink-examples:: create_llm_rag_agent
      :collapse:

.. py:function:: main() -> None

   Main function to run the example.


   .. autolink-examples:: main
      :collapse:

.. py:function:: run_example_queries(agent: Any)

   Run a set of example queries against the agent.

   :param agent: The LLM RAG agent to query


   .. autolink-examples:: run_example_queries
      :collapse:

.. py:data:: SAMPLE_DOCUMENTS

.. py:data:: logger

