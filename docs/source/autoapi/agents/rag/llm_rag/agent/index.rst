
:py:mod:`agents.rag.llm_rag.agent`
==================================

.. py:module:: agents.rag.llm_rag.agent


Classes
-------

.. autoapisummary::

   agents.rag.llm_rag.agent.LLMRAGAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LLMRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_LLMRAGAgent {
        node [shape=record];
        "LLMRAGAgent" [label="LLMRAGAgent"];
        "haive.agents.rag.base.agent.BaseRAGAgent" -> "LLMRAGAgent";
      }

.. autoclass:: agents.rag.llm_rag.agent.LLMRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.rag.llm_rag.agent.extract_answer
   agents.rag.llm_rag.agent.format_documents
   agents.rag.llm_rag.agent.parse_relevance_result

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



.. rubric:: Related Links

.. autolink-examples:: agents.rag.llm_rag.agent
   :collapse:
   
.. autolink-skip:: next
