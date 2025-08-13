
:py:mod:`agents.memory_reorganized.retrieval.enhanced_retriever`
================================================================

.. py:module:: agents.memory_reorganized.retrieval.enhanced_retriever

Enhanced Self-Query Retriever with Memory Context.

This module implements Phase 2 of the incremental memory system: Enhanced Self-Query
retriever that integrates memory classification with sophisticated retrieval strategies.

The enhanced retriever builds on the memory classification system to provide:
- Memory-type aware retrieval (semantic, episodic, procedural, etc.)
- Context-aware query expansion
- Memory importance weighting
- Time-based relevance scoring
- Self-query with metadata filtering

This is the next phase after the foundational memory classification system,
bridging toward full Graph RAG implementation.


.. autolink-examples:: agents.memory_reorganized.retrieval.enhanced_retriever
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_reorganized.retrieval.enhanced_retriever.EnhancedMemoryRetriever
   agents.memory_reorganized.retrieval.enhanced_retriever.EnhancedQueryResult
   agents.memory_reorganized.retrieval.enhanced_retriever.EnhancedRetrieverConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnhancedMemoryRetriever:

   .. graphviz::
      :align: center

      digraph inheritance_EnhancedMemoryRetriever {
        node [shape=record];
        "EnhancedMemoryRetriever" [label="EnhancedMemoryRetriever"];
      }

.. autoclass:: agents.memory_reorganized.retrieval.enhanced_retriever.EnhancedMemoryRetriever
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnhancedQueryResult:

   .. graphviz::
      :align: center

      digraph inheritance_EnhancedQueryResult {
        node [shape=record];
        "EnhancedQueryResult" [label="EnhancedQueryResult"];
        "pydantic.BaseModel" -> "EnhancedQueryResult";
      }

.. autopydantic_model:: agents.memory_reorganized.retrieval.enhanced_retriever.EnhancedQueryResult
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnhancedRetrieverConfig:

   .. graphviz::
      :align: center

      digraph inheritance_EnhancedRetrieverConfig {
        node [shape=record];
        "EnhancedRetrieverConfig" [label="EnhancedRetrieverConfig"];
        "pydantic.BaseModel" -> "EnhancedRetrieverConfig";
      }

.. autopydantic_model:: agents.memory_reorganized.retrieval.enhanced_retriever.EnhancedRetrieverConfig
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:



Functions
---------

.. autoapisummary::

   agents.memory_reorganized.retrieval.enhanced_retriever.create_enhanced_memory_retriever

.. py:function:: create_enhanced_memory_retriever(store_manager: haive.core.tools.store_tools.StoreManager, namespace: tuple[str, Ellipsis] = ('memory', 'enhanced'), classifier_config: haive.agents.memory.core.types.Optional[haive.agents.memory.core.classifier.MemoryClassifierConfig] = None, **retriever_kwargs) -> EnhancedMemoryRetriever
   :async:


   Factory function to create an enhanced memory retriever.

   :param store_manager: Store manager for memory persistence
   :param namespace: Default memory namespace
   :param classifier_config: Optional classifier configuration
   :param \*\*retriever_kwargs: Additional retriever configuration options

   :returns: Configured EnhancedMemoryRetriever ready for use


   .. autolink-examples:: create_enhanced_memory_retriever
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.memory_reorganized.retrieval.enhanced_retriever
   :collapse:
   
.. autolink-skip:: next
