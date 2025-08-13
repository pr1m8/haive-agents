
:py:mod:`agents.memory.unified_memory_api`
==========================================

.. py:module:: agents.memory.unified_memory_api

Unified Memory API - Complete Memory System Integration.

This module provides a unified, easy-to-use API for the complete memory system,
integrating all components including classification, storage, retrieval,
knowledge graph generation, and multi-agent coordination.


.. autolink-examples:: agents.memory.unified_memory_api
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory.unified_memory_api.MemorySystemConfig
   agents.memory.unified_memory_api.MemorySystemResult
   agents.memory.unified_memory_api.UnifiedMemorySystem


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemorySystemConfig:

   .. graphviz::
      :align: center

      digraph inheritance_MemorySystemConfig {
        node [shape=record];
        "MemorySystemConfig" [label="MemorySystemConfig"];
        "pydantic.BaseModel" -> "MemorySystemConfig";
      }

.. autopydantic_model:: agents.memory.unified_memory_api.MemorySystemConfig
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

   Inheritance diagram for MemorySystemResult:

   .. graphviz::
      :align: center

      digraph inheritance_MemorySystemResult {
        node [shape=record];
        "MemorySystemResult" [label="MemorySystemResult"];
        "pydantic.BaseModel" -> "MemorySystemResult";
      }

.. autopydantic_model:: agents.memory.unified_memory_api.MemorySystemResult
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

   Inheritance diagram for UnifiedMemorySystem:

   .. graphviz::
      :align: center

      digraph inheritance_UnifiedMemorySystem {
        node [shape=record];
        "UnifiedMemorySystem" [label="UnifiedMemorySystem"];
      }

.. autoclass:: agents.memory.unified_memory_api.UnifiedMemorySystem
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.memory.unified_memory_api.create_memory_system
   agents.memory.unified_memory_api.quick_memory_demo

.. py:function:: create_memory_system(store_type: str = 'memory', collection_name: str = 'haive_memories', enable_all_features: bool = True) -> UnifiedMemorySystem
   :async:


   Create a unified memory system with sensible default configuration.

   This convenience function creates a UnifiedMemorySystem with commonly used
   settings, making it easy to get started without complex configuration.

   :param store_type: Type of store backend to use ("memory", "postgres", "redis")
   :param collection_name: Name for the memory collection/table
   :param enable_all_features: Whether to enable all advanced features (Graph RAG,
                               multi-agent coordination, auto-classification)

   :returns: Fully configured and ready-to-use memory system
   :rtype: UnifiedMemorySystem

   .. rubric:: Examples

   Quick start with in-memory storage::

       # Create system with all features enabled
       memory_system = await create_memory_system()

       # System is ready to use immediately
       result = await memory_system.store_memory("Hello, world!")
       print(f"Stored memory: {result.success}")

   Production setup with PostgreSQL::

       memory_system = await create_memory_system(
           store_type="postgres",
           collection_name="company_memories",
           enable_all_features=True
       )

       # Verify system health
       diag = await memory_system.run_system_diagnostic()
       print(f"System health: {diag.result['system_health']}")

   Performance-focused setup::

       # Disable resource-intensive features for speed
       memory_system = await create_memory_system(
           store_type="memory",
           collection_name="fast_cache",
           enable_all_features=False
       )

       # System will use basic storage and retrieval only
       result = await memory_system.store_memory("Fast storage test")

   .. note::

      When enable_all_features=True, the system includes:
      - Automatic memory classification
      - Enhanced multi-strategy retrieval
      - Graph RAG with knowledge graph traversal
      - Multi-agent coordination for optimal routing
      
      When enable_all_features=False, only basic storage and retrieval are enabled
      for maximum performance.


   .. autolink-examples:: create_memory_system
      :collapse:

.. py:function:: quick_memory_demo()
   :async:


   Comprehensive demonstration of the unified memory system capabilities.

   This demo showcases the main features of the UnifiedMemorySystem including:
   - Memory storage with automatic classification
   - Intelligent retrieval with multiple strategies
   - Knowledge graph generation and analysis
   - System diagnostics and health monitoring
   - Performance metrics and statistics

   .. rubric:: Examples

   Run the complete demo::

       await quick_memory_demo()

   Use as a template for your own integration::

       # Copy relevant sections from this demo
       memory_system = await create_memory_system()

       # Store your data
       for item in your_data:
           await memory_system.store_memory(item)

       # Query your data
       result = await memory_system.retrieve_memories("your query")


   .. autolink-examples:: quick_memory_demo
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.memory.unified_memory_api
   :collapse:
   
.. autolink-skip:: next
