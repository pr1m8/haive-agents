
:py:mod:`agents.rag.multi_agent_rag.multi_rag`
==============================================

.. py:module:: agents.rag.multi_agent_rag.multi_rag

Multi-Agent RAG System Implementation.

from typing import Any
This module provides complete multi-agent RAG workflows using the multi-agent framework
with conditional routing, sequential processing, and parallel execution patterns.


.. autolink-examples:: agents.rag.multi_agent_rag.multi_rag
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.multi_agent_rag.multi_rag.AdaptiveRAGMultiAgent
   agents.rag.multi_agent_rag.multi_rag.BaseRAGMultiAgent
   agents.rag.multi_agent_rag.multi_rag.ConditionalRAGMultiAgent
   agents.rag.multi_agent_rag.multi_rag.IterativeRAGMultiAgent
   agents.rag.multi_agent_rag.multi_rag.ParallelRAGMultiAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AdaptiveRAGMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_AdaptiveRAGMultiAgent {
        node [shape=record];
        "AdaptiveRAGMultiAgent" [label="AdaptiveRAGMultiAgent"];
        "haive.agents.multi.base.ConditionalAgent" -> "AdaptiveRAGMultiAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.multi_rag.AdaptiveRAGMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BaseRAGMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_BaseRAGMultiAgent {
        node [shape=record];
        "BaseRAGMultiAgent" [label="BaseRAGMultiAgent"];
        "haive.agents.multi.base.SequentialAgent" -> "BaseRAGMultiAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.multi_rag.BaseRAGMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ConditionalRAGMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ConditionalRAGMultiAgent {
        node [shape=record];
        "ConditionalRAGMultiAgent" [label="ConditionalRAGMultiAgent"];
        "haive.agents.multi.base.ConditionalAgent" -> "ConditionalRAGMultiAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.multi_rag.ConditionalRAGMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for IterativeRAGMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_IterativeRAGMultiAgent {
        node [shape=record];
        "IterativeRAGMultiAgent" [label="IterativeRAGMultiAgent"];
        "haive.agents.multi.base.SequentialAgent" -> "IterativeRAGMultiAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.multi_rag.IterativeRAGMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ParallelRAGMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ParallelRAGMultiAgent {
        node [shape=record];
        "ParallelRAGMultiAgent" [label="ParallelRAGMultiAgent"];
        "haive.agents.multi.base.ParallelAgent" -> "ParallelRAGMultiAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.multi_rag.ParallelRAGMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.rag.multi_agent_rag.multi_rag.create_conditional_rag_system
   agents.rag.multi_agent_rag.multi_rag.create_iterative_rag_system
   agents.rag.multi_agent_rag.multi_rag.create_sequential_rag_system
   agents.rag.multi_agent_rag.multi_rag.document_quality_check
   agents.rag.multi_agent_rag.multi_rag.should_grade_documents
   agents.rag.multi_agent_rag.multi_rag.should_refine_query
   agents.rag.multi_agent_rag.multi_rag.test_agent_compatibility
   agents.rag.multi_agent_rag.multi_rag.validate_multi_agent_compatibility

.. py:function:: create_conditional_rag_system(documents: list[langchain_core.documents.Document] | None = None, custom_grader: collections.abc.Callable | None = None) -> ConditionalRAGMultiAgent

   Create a conditional RAG system with smart routing.


   .. autolink-examples:: create_conditional_rag_system
      :collapse:

.. py:function:: create_iterative_rag_system(documents: list[langchain_core.documents.Document] | None = None, custom_grader: collections.abc.Callable | None = None) -> IterativeRAGMultiAgent

   Create an iterative RAG system with document-by-document processing.


   .. autolink-examples:: create_iterative_rag_system
      :collapse:

.. py:function:: create_sequential_rag_system(documents: list[langchain_core.documents.Document] | None = None, use_grading: bool = True, use_citations: bool = False) -> haive.agents.multi.base.SequentialAgent

   Create a sequential RAG system with configurable components.


   .. autolink-examples:: create_sequential_rag_system
      :collapse:

.. py:function:: document_quality_check(state: haive.agents.rag.multi_agent_rag.state.MultiAgentRAGState) -> str

   Check document quality and route accordingly.

   :returns: Documents are good enough for generation
             - "insufficient": Need more/better documents
             - "regrade": Need different grading approach
   :rtype: - "sufficient"


   .. autolink-examples:: document_quality_check
      :collapse:

.. py:function:: should_grade_documents(state: haive.agents.rag.multi_agent_rag.state.MultiAgentRAGState) -> str

   Conditional routing function to determine if documents need grading.

   :returns: If documents need to be graded
             - "generate": If documents are already good enough
             - "refine": If query needs refinement
   :rtype: - "grade"


   .. autolink-examples:: should_grade_documents
      :collapse:

.. py:function:: should_refine_query(state: haive.agents.rag.multi_agent_rag.state.MultiAgentRAGState) -> str

   Conditional routing function to determine if query needs refinement.

   :returns: Try retrieval again with refined query
             - "generate": Generate answer with available documents
             - "END": Stop processing (failure case)
   :rtype: - "retrieve"


   .. autolink-examples:: should_refine_query
      :collapse:

.. py:function:: test_agent_compatibility(agent1: Any, agent2: Any) -> dict[str, Any]

   Test compatibility between two agents using the compatibility module.

   This demonstrates using the compatibility module to test if agents
   can work together as mentioned in the user prompt.


   .. autolink-examples:: test_agent_compatibility
      :collapse:

.. py:function:: validate_multi_agent_compatibility(agents: list[Any]) -> dict[str, Any]

   Validate compatibility across multiple agents in a workflow.

   Returns a comprehensive compatibility report for the agent chain.


   .. autolink-examples:: validate_multi_agent_compatibility
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.multi_agent_rag.multi_rag
   :collapse:
   
.. autolink-skip:: next
