agents.rag.llm_rag.agent
========================

.. py:module:: agents.rag.llm_rag.agent


Attributes
----------

.. autoapisummary::

   agents.rag.llm_rag.agent.logger


Classes
-------

.. autoapisummary::

   agents.rag.llm_rag.agent.LLMRAGAgent


Functions
---------

.. autoapisummary::

   agents.rag.llm_rag.agent.extract_answer
   agents.rag.llm_rag.agent.format_documents
   agents.rag.llm_rag.agent.parse_relevance_result


Module Contents
---------------

.. py:class:: LLMRAGAgent

   Bases: :py:obj:`haive.agents.rag.base.agent.BaseRAGAgent`


   LLM-enhanced RAG agent that retrieves documents and generates answers.

   This agent extends the base RAG workflow:
   1. Receive a query
   2. Retrieve relevant documents (handled by BaseRAGAgent)
   3. Check if the documents are relevant to the query
   4. Generate an answer based on the documents if relevant


   .. autolink-examples:: LLMRAGAgent
      :collapse:

   .. py:method:: setup_workflow() -> None

      Set up the dynamic workflow for the LLM RAG agent.

      Creates a graph that extends the base RAG workflow with additional
      functionality for checking relevance and generating answers.


      .. autolink-examples:: setup_workflow
         :collapse:


.. py:function:: extract_answer(result: Any) -> str

   Extract the answer string from an LLM result, which could be in various formats.


   .. autolink-examples:: extract_answer
      :collapse:

.. py:function:: format_documents(documents: list[Any]) -> str

   Format a list of documents into a text string for LLM input.
   Handles both Document objects and strings.


   .. autolink-examples:: format_documents
      :collapse:

.. py:function:: parse_relevance_result(result: Any) -> bool

   Parse the output from the relevance checker to determine if documents are relevant.


   .. autolink-examples:: parse_relevance_result
      :collapse:

.. py:data:: logger

