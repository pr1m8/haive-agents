
:py:mod:`agents.memory_v2.advanced_rag_memory_agent`
====================================================

.. py:module:: agents.memory_v2.advanced_rag_memory_agent

Advanced RAG Memory Agent with multi-stage retrieval and reranking.

This implementation provides state-of-the-art RAG capabilities:
1. Multi-stage retrieval: dense → sparse → reranking
2. Hybrid search combining vector, keyword, and graph
3. Query decomposition for complex questions
4. Memory-augmented generation with citations
5. Adaptive retrieval based on query complexity


.. autolink-examples:: agents.memory_v2.advanced_rag_memory_agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_v2.advanced_rag_memory_agent.AdvancedRAGConfig
   agents.memory_v2.advanced_rag_memory_agent.AdvancedRAGMemoryAgent
   agents.memory_v2.advanced_rag_memory_agent.QueryComplexity
   agents.memory_v2.advanced_rag_memory_agent.RetrievalStrategy


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AdvancedRAGConfig:

   .. graphviz::
      :align: center

      digraph inheritance_AdvancedRAGConfig {
        node [shape=record];
        "AdvancedRAGConfig" [label="AdvancedRAGConfig"];
      }

.. autoclass:: agents.memory_v2.advanced_rag_memory_agent.AdvancedRAGConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AdvancedRAGMemoryAgent:

   .. graphviz::
      :align: center

      digraph inheritance_AdvancedRAGMemoryAgent {
        node [shape=record];
        "AdvancedRAGMemoryAgent" [label="AdvancedRAGMemoryAgent"];
      }

.. autoclass:: agents.memory_v2.advanced_rag_memory_agent.AdvancedRAGMemoryAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for QueryComplexity:

   .. graphviz::
      :align: center

      digraph inheritance_QueryComplexity {
        node [shape=record];
        "QueryComplexity" [label="QueryComplexity"];
        "str" -> "QueryComplexity";
        "enum.Enum" -> "QueryComplexity";
      }

.. autoclass:: agents.memory_v2.advanced_rag_memory_agent.QueryComplexity
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **QueryComplexity** is an Enum defined in ``agents.memory_v2.advanced_rag_memory_agent``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RetrievalStrategy:

   .. graphviz::
      :align: center

      digraph inheritance_RetrievalStrategy {
        node [shape=record];
        "RetrievalStrategy" [label="RetrievalStrategy"];
        "str" -> "RetrievalStrategy";
        "enum.Enum" -> "RetrievalStrategy";
      }

.. autoclass:: agents.memory_v2.advanced_rag_memory_agent.RetrievalStrategy
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **RetrievalStrategy** is an Enum defined in ``agents.memory_v2.advanced_rag_memory_agent``.



Functions
---------

.. autoapisummary::

   agents.memory_v2.advanced_rag_memory_agent.create_conversational_memory_agent
   agents.memory_v2.advanced_rag_memory_agent.create_research_memory_agent
   agents.memory_v2.advanced_rag_memory_agent.example_advanced_rag_usage

.. py:function:: create_conversational_memory_agent() -> AdvancedRAGMemoryAgent
   :async:


   Create a conversation-focused memory agent.


   .. autolink-examples:: create_conversational_memory_agent
      :collapse:

.. py:function:: create_research_memory_agent() -> AdvancedRAGMemoryAgent
   :async:


   Create a research-focused memory agent.


   .. autolink-examples:: create_research_memory_agent
      :collapse:

.. py:function:: example_advanced_rag_usage()
   :async:


   Example of using Advanced RAG Memory Agent.


   .. autolink-examples:: example_advanced_rag_usage
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.memory_v2.advanced_rag_memory_agent
   :collapse:
   
.. autolink-skip:: next
