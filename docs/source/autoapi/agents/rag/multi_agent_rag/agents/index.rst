
:py:mod:`agents.rag.multi_agent_rag.agents`
===========================================

.. py:module:: agents.rag.multi_agent_rag.agents

Multi-Agent RAG System Components.

This module provides specialized RAG agents that can be composed into complex workflows
using the multi-agent framework. Each agent focuses on a specific aspect of the RAG process.


.. autolink-examples:: agents.rag.multi_agent_rag.agents
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.multi_agent_rag.agents.DocumentGradingAgent
   agents.rag.multi_agent_rag.agents.IterativeDocumentGradingAgent
   agents.rag.multi_agent_rag.agents.SimpleRAGAgent
   agents.rag.multi_agent_rag.agents.SimpleRAGAnswerAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DocumentGradingAgent:

   .. graphviz::
      :align: center

      digraph inheritance_DocumentGradingAgent {
        node [shape=record];
        "DocumentGradingAgent" [label="DocumentGradingAgent"];
        "haive.agents.simple.agent.SimpleAgent" -> "DocumentGradingAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.agents.DocumentGradingAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for IterativeDocumentGradingAgent:

   .. graphviz::
      :align: center

      digraph inheritance_IterativeDocumentGradingAgent {
        node [shape=record];
        "IterativeDocumentGradingAgent" [label="IterativeDocumentGradingAgent"];
        "DocumentGradingAgent" -> "IterativeDocumentGradingAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.agents.IterativeDocumentGradingAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SimpleRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleRAGAgent {
        node [shape=record];
        "SimpleRAGAgent" [label="SimpleRAGAgent"];
        "haive.agents.simple.agent.SimpleAgent" -> "SimpleRAGAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.agents.SimpleRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SimpleRAGAnswerAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleRAGAnswerAgent {
        node [shape=record];
        "SimpleRAGAnswerAgent" [label="SimpleRAGAnswerAgent"];
        "haive.agents.simple.agent.SimpleAgent" -> "SimpleRAGAnswerAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.agents.SimpleRAGAnswerAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.rag.multi_agent_rag.agents.create_document_grading_agent
   agents.rag.multi_agent_rag.agents.create_iterative_grading_agent
   agents.rag.multi_agent_rag.agents.create_rag_answer_agent
   agents.rag.multi_agent_rag.agents.create_simple_rag_agent
   agents.rag.multi_agent_rag.agents.generate_answer
   agents.rag.multi_agent_rag.agents.grade_document
   agents.rag.multi_agent_rag.agents.grade_documents
   agents.rag.multi_agent_rag.agents.retrieve_documents
   agents.rag.multi_agent_rag.agents.run_generation
   agents.rag.multi_agent_rag.agents.run_grading
   agents.rag.multi_agent_rag.agents.run_iterative_grading
   agents.rag.multi_agent_rag.agents.run_retrieval

.. py:function:: create_document_grading_agent(grading_mode: str = 'binary', min_threshold: float = 0.5, **kwargs) -> DocumentGradingAgent

   Create a document grading agent with default configuration.


   .. autolink-examples:: create_document_grading_agent
      :collapse:

.. py:function:: create_iterative_grading_agent(custom_grader: collections.abc.Callable | None = None, **kwargs) -> IterativeDocumentGradingAgent

   Create an iterative document grading agent.


   .. autolink-examples:: create_iterative_grading_agent
      :collapse:

.. py:function:: create_rag_answer_agent(use_citations: bool = False, **kwargs) -> SimpleRAGAnswerAgent

   Create a RAG answer agent with default configuration.


   .. autolink-examples:: create_rag_answer_agent
      :collapse:

.. py:function:: create_simple_rag_agent(documents: list[langchain_core.documents.Document] | None = None, **kwargs) -> SimpleRAGAgent

   Create a simple RAG agent with default configuration.


   .. autolink-examples:: create_simple_rag_agent
      :collapse:

.. py:function:: generate_answer(query, docs)

.. py:function:: grade_document(doc)

.. py:function:: grade_documents(docs)

.. py:function:: retrieve_documents(query)

.. py:function:: run_generation(state)

.. py:function:: run_grading(state)

.. py:function:: run_iterative_grading(state)

.. py:function:: run_retrieval(state)



.. rubric:: Related Links

.. autolink-examples:: agents.rag.multi_agent_rag.agents
   :collapse:
   
.. autolink-skip:: next
