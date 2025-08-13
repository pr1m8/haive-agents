
:py:mod:`agents.memory_reorganized.retrieval.advanced_rag`
==========================================================

.. py:module:: agents.memory_reorganized.retrieval.advanced_rag

Advanced RAG Memory Agent with multi-stage retrieval and reranking.

This implementation provides state-of-the-art RAG capabilities:
1. Multi-stage retrieval: dense → sparse → reranking
2. Hybrid search combining vector, key, and graph
3. Query decomposition for complex questions
4. Memory-augmented generation with citations
5. Adaptive retrieval based on query complexity


.. autolink-examples:: agents.memory_reorganized.retrieval.advanced_rag
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_reorganized.retrieval.advanced_rag.AdvancedRAGConfig
   agents.memory_reorganized.retrieval.advanced_rag.AdvancedRAGMemoryAgent
   agents.memory_reorganized.retrieval.advanced_rag.QueryComplexity
   agents.memory_reorganized.retrieval.advanced_rag.RetrievalStrategy


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

.. autoclass:: agents.memory_reorganized.retrieval.advanced_rag.AdvancedRAGConfig
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

.. autoclass:: agents.memory_reorganized.retrieval.advanced_rag.AdvancedRAGMemoryAgent
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

.. autoclass:: agents.memory_reorganized.retrieval.advanced_rag.QueryComplexity
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **QueryComplexity** is an Enum defined in ``agents.memory_reorganized.retrieval.advanced_rag``.





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

.. autoclass:: agents.memory_reorganized.retrieval.advanced_rag.RetrievalStrategy
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **RetrievalStrategy** is an Enum defined in ``agents.memory_reorganized.retrieval.advanced_rag``.



Functions
---------

.. autoapisummary::

   agents.memory_reorganized.retrieval.advanced_rag.create_conversational_memory_agent
   agents.memory_reorganized.retrieval.advanced_rag.create_research_memory_agent
   agents.memory_reorganized.retrieval.advanced_rag.example_advanced_rag_usage

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

.. autolink-examples:: agents.memory_reorganized.retrieval.advanced_rag
   :collapse:
   
.. autolink-skip:: next
