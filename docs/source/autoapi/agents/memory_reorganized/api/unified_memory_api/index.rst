agents.memory_reorganized.api.unified_memory_api
================================================

.. py:module:: agents.memory_reorganized.api.unified_memory_api

.. autoapi-nested-parse::

   Unified Memory API - Complete Memory System Integration.

   This module provides a unified, easy-to-use API for the complete memory system,
   integrating all components including classification, storage, retrieval,
   knowledge graph generation, and multi-agent coordination.


   .. autolink-examples:: agents.memory_reorganized.api.unified_memory_api
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory_reorganized.api.unified_memory_api.logger


Classes
-------

.. autoapisummary::

   agents.memory_reorganized.api.unified_memory_api.MemorySystemConfig
   agents.memory_reorganized.api.unified_memory_api.MemorySystemResult
   agents.memory_reorganized.api.unified_memory_api.UnifiedMemorySystem


Functions
---------

.. autoapisummary::

   agents.memory_reorganized.api.unified_memory_api.create_memory_system
   agents.memory_reorganized.api.unified_memory_api.quick_memory_demo


Module Contents
---------------

.. py:class:: MemorySystemConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Comprehensive configuration for the unified memory system.

   This configuration class defines all settings needed to create and customize
   a UnifiedMemorySystem, including store settings, LLM configuration, feature
   toggles, and performance parameters.

   .. attribute:: store_type

      Type of store backend ("memory", "postgres", "redis", etc.)

   .. attribute:: collection_name

      Name of the collection/table for storing memories

   .. attribute:: default_namespace

      Default namespace tuple for memory organization

   .. attribute:: llm_config

      LLM configuration for classification, analysis, and generation

   .. attribute:: enable_auto_classification

      Whether to automatically classify stored memories

   .. attribute:: classification_confidence_threshold

      Minimum confidence for auto-classification

   .. attribute:: enable_enhanced_retrieval

      Whether to enable enhanced retrieval features

   .. attribute:: enable_graph_rag

      Whether to enable Graph RAG retrieval capabilities

   .. attribute:: enable_multi_agent_coordination

      Whether to enable multi-agent coordination

   .. attribute:: max_concurrent_operations

      Maximum number of concurrent memory operations

   .. attribute:: operation_timeout_seconds

      Timeout for individual memory operations

   .. attribute:: enable_memory_consolidation

      Whether to enable automatic memory consolidation

   .. attribute:: consolidation_interval_hours

      Hours between automatic consolidation runs

   .. rubric:: Examples

   Basic configuration for development::

       config = MemorySystemConfig(
           store_type="memory",
           collection_name="dev_memories",
           default_namespace=("user", "development")
       )

   Production configuration with PostgreSQL::

       config = MemorySystemConfig(
           store_type="postgres",
           collection_name="prod_memories",
           default_namespace=("company", "production"),
           llm_config=AugLLMConfig(
               model="gpt-4",
               temperature=0.1,
               max_tokens=1000
           ),
           enable_auto_classification=True,
           enable_graph_rag=True,
           enable_multi_agent_coordination=True,
           max_concurrent_operations=10,
           operation_timeout_seconds=600
       )

   Performance-optimized configuration::

       config = MemorySystemConfig(
           store_type="redis",
           collection_name="fast_memories",
           default_namespace=("user", "cache"),
           enable_auto_classification=False,  # Disable for speed
           enable_enhanced_retrieval=True,
           enable_graph_rag=False,  # Disable for speed
           enable_multi_agent_coordination=False,
           max_concurrent_operations=20,
           operation_timeout_seconds=30
       )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemorySystemConfig
      :collapse:

   .. py:attribute:: classification_confidence_threshold
      :type:  float
      :value: None



   .. py:attribute:: collection_name
      :type:  str
      :value: None



   .. py:attribute:: consolidation_interval_hours
      :type:  int
      :value: None



   .. py:attribute:: default_namespace
      :type:  tuple[str, Ellipsis]
      :value: None



   .. py:attribute:: enable_auto_classification
      :type:  bool
      :value: None



   .. py:attribute:: enable_enhanced_retrieval
      :type:  bool
      :value: None



   .. py:attribute:: enable_graph_rag
      :type:  bool
      :value: None



   .. py:attribute:: enable_memory_consolidation
      :type:  bool
      :value: None



   .. py:attribute:: enable_multi_agent_coordination
      :type:  bool
      :value: None



   .. py:attribute:: llm_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: max_concurrent_operations
      :type:  int
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: operation_timeout_seconds
      :type:  int
      :value: None



   .. py:attribute:: store_type
      :type:  str
      :value: None



.. py:class:: MemorySystemResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Comprehensive result from memory system operations with metrics and analysis.

   This class encapsulates all information returned from memory system operations,
   including success status, operation results, performance metrics, quality scores,
   and metadata for analysis and monitoring.

   .. attribute:: success

      Whether the operation completed successfully

   .. attribute:: operation

      Type of operation performed (store_memory, retrieve_memories, etc.)

   .. attribute:: result

      The actual result data from the operation (varies by operation type)

   .. attribute:: error

      Error message if the operation failed (None if successful)

   .. attribute:: execution_time_ms

      Time taken to complete the operation in milliseconds

   .. attribute:: agent_used

      Name of the agent/component that handled the operation

   .. attribute:: confidence_score

      Confidence in the result quality (0.0-1.0)

   .. attribute:: completeness_score

      How complete the result is (0.0-1.0)

   .. attribute:: timestamp

      UTC timestamp when the operation completed

   .. attribute:: metadata

      Additional metadata specific to the operation

   .. rubric:: Examples

   Checking operation success::

       result = await memory_system.store_memory("Important information")

       if result.success:
           memory_id = result.result["memory_id"]
           print(f"Memory stored successfully with ID: {memory_id}")
           print(f"Operation took {result.execution_time_ms:.1f}ms")
       else:
           print(f"Storage failed: {result.error}")

   Analyzing retrieval results::

       result = await memory_system.retrieve_memories("machine learning")

       if result.success:
           memories = result.result["memories"]
           count = result.result["count"]

           print(f"Retrieved {count} memories in {result.execution_time_ms:.1f}ms")
           print(f"Confidence: {result.confidence_score:.2f}")
           print(f"Completeness: {result.completeness_score:.2f}")
           print(f"Agent used: {result.agent_used}")

           for memory in memories:
               print(f"- {memory['content'][:100]}...")

   Performance monitoring::

       results = []

       # Perform multiple operations
       for query in ["Python", "AI", "databases"]:
           result = await memory_system.retrieve_memories(query)
           results.append(result)

       # Analyze performance
       avg_time = sum(r.execution_time_ms for r in results) / len(results)
       success_rate = sum(1 for r in results if r.success) / len(results)

       print(f"Average response time: {avg_time:.1f}ms")
       print(f"Success rate: {success_rate:.1%}")

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemorySystemResult
      :collapse:

   .. py:attribute:: agent_used
      :type:  str | None
      :value: None



   .. py:attribute:: completeness_score
      :type:  float
      :value: None



   .. py:attribute:: confidence_score
      :type:  float
      :value: None



   .. py:attribute:: error
      :type:  str | None
      :value: None



   .. py:attribute:: execution_time_ms
      :type:  float
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: operation
      :type:  str
      :value: None



   .. py:attribute:: result
      :type:  Any
      :value: None



   .. py:attribute:: success
      :type:  bool
      :value: None



   .. py:attribute:: timestamp
      :type:  datetime.datetime
      :value: None



.. py:class:: UnifiedMemorySystem(config: MemorySystemConfig)

   Unified Memory System - Complete memory management solution with intelligent coordination.

   The UnifiedMemorySystem provides a single, comprehensive interface to all memory
   system capabilities, automatically coordinating between multiple specialized agents
   to provide optimal memory storage, retrieval, and analysis. It combines traditional
   vector search with knowledge graph traversal, multi-agent coordination, and
   intelligent classification for superior memory management.

   Key Features:
       - Unified API: Single interface for all memory operations
       - Multi-Agent Coordination: Automatic routing to best-suited agents
       - Graph RAG: Knowledge graph enhanced retrieval
       - Auto-Classification: Intelligent memory type detection
       - Performance Monitoring: Built-in metrics and diagnostics
       - Flexible Storage: Support for multiple backend stores
       - Async Operations: Full async/await support for scalability

   Architecture:
       - Memory Store Manager: Handles storage and basic retrieval
       - Memory Classifier: Analyzes and categorizes memory content
       - KG Generator Agent: Builds and maintains knowledge graphs
       - Graph RAG Retriever: Enhanced retrieval with graph context
       - Agentic RAG Coordinator: Intelligent retrieval strategy selection
       - Multi-Agent Coordinator: Orchestrates all agents for complex tasks

   .. attribute:: config

      System configuration settings

   .. attribute:: memory_store

      Core memory storage manager

   .. attribute:: classifier

      Memory classification engine

   .. attribute:: kg_generator

      Knowledge graph generation agent

   .. attribute:: retrievers

      Dictionary of specialized retrieval systems

   .. attribute:: agentic_rag

      Intelligent retrieval coordinator

   .. attribute:: coordinator

      Multi-agent coordination system (optional)

   .. rubric:: Examples

   Basic usage with default configuration::

       # Create system with all features enabled
       memory_system = await create_memory_system()

       # Store memories
       result = await memory_system.store_memory(
           "Alice works at TechCorp as a software engineer"
       )

       if result.success:
           print(f"Memory stored: {result.result['memory_id']}")

       # Retrieve memories
       result = await memory_system.retrieve_memories(
           "Who works at TechCorp?", limit=5
       )

       if result.success:
           for memory in result.result["memories"]:
               print(f"Found: {memory['content']}")

   Advanced usage with custom configuration::

       config = MemorySystemConfig(
           store_type="postgres",
           collection_name="company_knowledge",
           default_namespace=("company", "engineering"),
           enable_graph_rag=True,
           enable_multi_agent_coordination=True,
           llm_config=AugLLMConfig(model="gpt-4", temperature=0.1)
       )

       memory_system = UnifiedMemorySystem(config)

       # Store with metadata
       result = await memory_system.store_memory(
           content="Neural networks are effective for pattern recognition",
           namespace=("company", "ai", "research"),
           metadata={"source": "research_paper", "confidence": 0.95}
       )

       # Advanced retrieval with filtering
       result = await memory_system.retrieve_memories(
           query="pattern recognition techniques",
           limit=10,
           memory_types=[MemoryType.SEMANTIC, MemoryType.PROCEDURAL],
           namespace=("company", "ai"),
           use_graph_rag=True
       )

   Knowledge graph operations::

       # Generate knowledge graph from stored memories
       kg_result = await memory_system.generate_knowledge_graph(
           namespace=("company", "projects")
       )

       if kg_result.success:
           kg = kg_result.result["knowledge_graph"]
           print(f"Generated graph with {len(kg.nodes)} nodes")

       # Search for specific entities
       entity_result = await memory_system.search_entities("Alice")

       if entity_result.success:
           context = entity_result.result["entity_context"]
           print(f"Found entity: {context['entity'].name}")
           print(f"Connected to {context['total_connections']} other entities")

   System monitoring and diagnostics::

       # Get comprehensive statistics
       stats_result = await memory_system.get_memory_statistics()

       if stats_result.success:
           stats = stats_result.result
           print(f"Total memories: {stats['store_statistics']['total_count']}")
           print(f"Operations performed: {stats['system_statistics']['total_operations']}")

       # Run system health check
       diag_result = await memory_system.run_system_diagnostic()

       if diag_result.success:
           health = diag_result.result["system_health"]
           print(f"System health: {health}")

           for component, status in diag_result.result["component_diagnostics"].items():
               print(f"{component}: {status['status']}")

   Memory lifecycle management::

       # Consolidate memories (remove duplicates, expired entries)
       consolidation_result = await memory_system.consolidate_memories(
           namespace=("user", "temp"),
           dry_run=True  # Preview changes first
       )

       if consolidation_result.success:
           result = consolidation_result.result["consolidation_result"]
           print(f"Would remove {result['duplicates_found']} duplicates")
           print(f"Would expire {result['expired_found']} old memories")

       # Actually perform consolidation
       if input("Proceed with consolidation? (y/n): ").lower() == 'y':
           final_result = await memory_system.consolidate_memories(
               namespace=("user", "temp"),
               dry_run=False
           )

   .. note::

      The UnifiedMemorySystem automatically selects the best agent for each operation
      based on the request type, available features, and performance considerations.
      Enable multi-agent coordination for the most intelligent behavior, or disable
      specific features for better performance in resource-constrained environments.

   Initialize the unified memory system with comprehensive component setup.

   Creates and configures all memory system components including stores, classifiers,
   knowledge graph generators, retrievers, and coordinators based on the provided
   configuration. All components are initialized and validated during construction.

   :param config: MemorySystemConfig with all system settings and feature flags

   :raises ValueError: If required configuration parameters are missing or invalid
   :raises RuntimeError: If component initialization fails

   .. rubric:: Examples

   Basic initialization::

       config = MemorySystemConfig(
           store_type="memory",
           collection_name="my_memories"
       )

       memory_system = UnifiedMemorySystem(config)
       print("System initialized successfully")

   Production initialization with validation::

       config = MemorySystemConfig(
           store_type="postgres",
           collection_name="prod_memories",
           default_namespace=("company", "prod"),
           enable_multi_agent_coordination=True,
           llm_config=AugLLMConfig(model="gpt-4")
       )

       try:
           memory_system = UnifiedMemorySystem(config)

           # Validate initialization
           system_info = memory_system.get_system_info()
           assert system_info["initialized"]

           print(f"System ready with {len(system_info['components'])} components")

       except Exception as e:
           print(f"Initialization failed: {e}")

   .. note::

      Component initialization follows dependency order: store → classifier →
      KG generator → retrievers → coordinator. If any component fails to
      initialize, the entire system initialization will fail.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: UnifiedMemorySystem
      :collapse:

   .. py:method:: _initialize_classifier() -> None

      Initialize the memory classifier.


      .. autolink-examples:: _initialize_classifier
         :collapse:


   .. py:method:: _initialize_coordinator() -> None

      Initialize the multi-agent coordinator.


      .. autolink-examples:: _initialize_coordinator
         :collapse:


   .. py:method:: _initialize_kg_generator() -> None

      Initialize the knowledge graph generator.


      .. autolink-examples:: _initialize_kg_generator
         :collapse:


   .. py:method:: _initialize_retrievers() -> None

      Initialize the retrieval systems.


      .. autolink-examples:: _initialize_retrievers
         :collapse:


   .. py:method:: _initialize_store() -> None

      Initialize the memory store.


      .. autolink-examples:: _initialize_store
         :collapse:


   .. py:method:: _update_operation_stats(start_time: datetime.datetime, success: bool) -> None

      Update operation statistics.


      .. autolink-examples:: _update_operation_stats
         :collapse:


   .. py:method:: classify_memory(content: str, user_context: dict[str, Any] | None = None) -> MemorySystemResult
      :async:


      Classify memory content.

      :param content: Memory content to classify
      :param user_context: User context for classification

      :returns: MemorySystemResult with classification result


      .. autolink-examples:: classify_memory
         :collapse:


   .. py:method:: consolidate_memories(namespace: tuple[str, Ellipsis] | None = None, dry_run: bool = False) -> MemorySystemResult
      :async:


      Consolidate memories by removing duplicates and expired entries.

      :param namespace: Memory namespace to consolidate
      :param dry_run: If True, only analyze without making changes

      :returns: MemorySystemResult with consolidation results


      .. autolink-examples:: consolidate_memories
         :collapse:


   .. py:method:: generate_knowledge_graph(namespace: tuple[str, Ellipsis] | None = None, force_regeneration: bool = False) -> MemorySystemResult
      :async:


      Generate knowledge graph from memories.

      :param namespace: Memory namespace to process
      :param force_regeneration: Force regeneration even if graph exists

      :returns: MemorySystemResult with knowledge graph


      .. autolink-examples:: generate_knowledge_graph
         :collapse:


   .. py:method:: get_memory_statistics(namespace: tuple[str, Ellipsis] | None = None) -> MemorySystemResult
      :async:


      Get comprehensive memory statistics.

      :param namespace: Memory namespace to analyze

      :returns: MemorySystemResult with statistics


      .. autolink-examples:: get_memory_statistics
         :collapse:


   .. py:method:: get_system_info() -> dict[str, Any]

      Get comprehensive system information.


      .. autolink-examples:: get_system_info
         :collapse:


   .. py:method:: retrieve_memories(query: str, limit: int = 10, namespace: tuple[str, Ellipsis] | None = None, memory_types: list[haive.agents.memory_reorganized.core.types.MemoryType] | None = None, use_graph_rag: bool = True, use_multi_agent: bool = True) -> MemorySystemResult
      :async:


      Retrieve memories from the system.

      :param query: Search query
      :param limit: Maximum number of memories to retrieve
      :param namespace: Memory namespace to search
      :param memory_types: Specific memory types to search
      :param use_graph_rag: Whether to use graph RAG
      :param use_multi_agent: Whether to use multi-agent coordination

      :returns: MemorySystemResult with retrieved memories


      .. autolink-examples:: retrieve_memories
         :collapse:


   .. py:method:: run_system_diagnostic() -> MemorySystemResult
      :async:


      Run comprehensive system diagnostic.

      :returns: MemorySystemResult with diagnostic results


      .. autolink-examples:: run_system_diagnostic
         :collapse:


   .. py:method:: search_entities(entity_name: str, namespace: tuple[str, Ellipsis] | None = None) -> MemorySystemResult
      :async:


      Search for entities in the knowledge graph.

      :param entity_name: Name of entity to search for
      :param namespace: Memory namespace to search

      :returns: MemorySystemResult with entity information


      .. autolink-examples:: search_entities
         :collapse:


   .. py:method:: store_memory(content: str, namespace: tuple[str, Ellipsis] | None = None, memory_type: haive.agents.memory_reorganized.core.types.MemoryType | None = None, importance: float | None = None, metadata: dict[str, Any] | None = None) -> MemorySystemResult
      :async:


      Store a memory in the system.

      :param content: Memory content to store
      :param namespace: Memory namespace (defaults to configured default)
      :param memory_type: Force specific memory type (otherwise auto-classified)
      :param importance: Override importance score
      :param metadata: Additional metadata

      :returns: MemorySystemResult with operation result


      .. autolink-examples:: store_memory
         :collapse:


   .. py:attribute:: _initialized
      :value: True



   .. py:attribute:: _stats


   .. py:attribute:: config


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

.. py:data:: logger

