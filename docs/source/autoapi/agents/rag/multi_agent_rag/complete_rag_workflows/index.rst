
:py:mod:`agents.rag.multi_agent_rag.complete_rag_workflows`
===========================================================

.. py:module:: agents.rag.multi_agent_rag.complete_rag_workflows

Complete RAG Workflows Implementation.

Implements all RAG architectures from rag-architectures-flows.md including:
- Corrective RAG with web search fallback
- Self-RAG with reflection tokens
- Adaptive RAG with complexity routing
- Multi-Query RAG and RAG Fusion
- HYDE and Step-Back prompting
- Hallucination detection and requerying


.. autolink-examples:: agents.rag.multi_agent_rag.complete_rag_workflows
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.multi_agent_rag.complete_rag_workflows.AdaptiveRAGAgent
   agents.rag.multi_agent_rag.complete_rag_workflows.CorrectiveRAGAgent
   agents.rag.multi_agent_rag.complete_rag_workflows.HYDERAGAgent
   agents.rag.multi_agent_rag.complete_rag_workflows.RAGQuality
   agents.rag.multi_agent_rag.complete_rag_workflows.ReflectionToken
   agents.rag.multi_agent_rag.complete_rag_workflows.SelfRAGAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AdaptiveRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_AdaptiveRAGAgent {
        node [shape=record];
        "AdaptiveRAGAgent" [label="AdaptiveRAGAgent"];
        "haive.agents.multi.base.ConditionalAgent" -> "AdaptiveRAGAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.complete_rag_workflows.AdaptiveRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CorrectiveRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_CorrectiveRAGAgent {
        node [shape=record];
        "CorrectiveRAGAgent" [label="CorrectiveRAGAgent"];
        "haive.agents.multi.base.ConditionalAgent" -> "CorrectiveRAGAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.complete_rag_workflows.CorrectiveRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HYDERAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_HYDERAGAgent {
        node [shape=record];
        "HYDERAGAgent" [label="HYDERAGAgent"];
        "haive.agents.multi.base.SequentialAgent" -> "HYDERAGAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.complete_rag_workflows.HYDERAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RAGQuality:

   .. graphviz::
      :align: center

      digraph inheritance_RAGQuality {
        node [shape=record];
        "RAGQuality" [label="RAGQuality"];
        "str" -> "RAGQuality";
        "enum.Enum" -> "RAGQuality";
      }

.. autoclass:: agents.rag.multi_agent_rag.complete_rag_workflows.RAGQuality
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **RAGQuality** is an Enum defined in ``agents.rag.multi_agent_rag.complete_rag_workflows``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReflectionToken:

   .. graphviz::
      :align: center

      digraph inheritance_ReflectionToken {
        node [shape=record];
        "ReflectionToken" [label="ReflectionToken"];
        "str" -> "ReflectionToken";
        "enum.Enum" -> "ReflectionToken";
      }

.. autoclass:: agents.rag.multi_agent_rag.complete_rag_workflows.ReflectionToken
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ReflectionToken** is an Enum defined in ``agents.rag.multi_agent_rag.complete_rag_workflows``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SelfRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SelfRAGAgent {
        node [shape=record];
        "SelfRAGAgent" [label="SelfRAGAgent"];
        "haive.agents.multi.base.ConditionalAgent" -> "SelfRAGAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.complete_rag_workflows.SelfRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.rag.multi_agent_rag.complete_rag_workflows.crag_relevance_check
   agents.rag.multi_agent_rag.complete_rag_workflows.create_complete_rag_workflow
   agents.rag.multi_agent_rag.complete_rag_workflows.generate_multi_queries
   agents.rag.multi_agent_rag.complete_rag_workflows.hallucination_detection
   agents.rag.multi_agent_rag.complete_rag_workflows.hyde_hypothesis_generation
   agents.rag.multi_agent_rag.complete_rag_workflows.query_complexity_analysis
   agents.rag.multi_agent_rag.complete_rag_workflows.self_rag_retrieval_decision
   agents.rag.multi_agent_rag.complete_rag_workflows.web_search_fallback

.. py:function:: crag_relevance_check(input_data: dict) -> dict

   CRAG relevance checking with three-way classification.


   .. autolink-examples:: crag_relevance_check
      :collapse:

.. py:function:: create_complete_rag_workflow(workflow_type: str, documents: list[langchain_core.documents.Document] | None = None, **kwargs) -> haive.agents.base.agent.Agent

   Factory for creating complete RAG workflows.

   Available types:
   - 'crag': Corrective RAG with web search
   - 'self_rag': Self-RAG with reflection tokens
   - 'adaptive': Adaptive RAG with complexity routing
   - 'hyde': HYDE RAG with hypothesis generation
   - 'multi_query': Multi-Query RAG with query variations


   .. autolink-examples:: create_complete_rag_workflow
      :collapse:


.. py:function:: hallucination_detection(input_data: dict) -> dict

   Detect hallucination in generated response.


   .. autolink-examples:: hallucination_detection
      :collapse:




.. py:function:: web_search_fallback(input_data: dict) -> dict

   Web search fallback for when documents are insufficient.


   .. autolink-examples:: web_search_fallback
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.multi_agent_rag.complete_rag_workflows
   :collapse:
   
.. autolink-skip:: next
