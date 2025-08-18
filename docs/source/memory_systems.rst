Memory Systems
==============

Haive Agents features a **revolutionary, fully recompilable memory architecture** that can be **dynamically reconfigured**, **serialized**, and **transferred** between agents and systems at runtime. Our memory system combines **Neo4j knowledge graphs**, **vector embeddings**, and **temporal intelligence** with **complete serializability** and **live reconfiguration** capabilities.

🧠 **The Game Changer**: **Dynamically recompilable memory systems** that can switch between graph/vector/temporal modes, modify retrieval strategies, reconfigure storage backends, and adapt cognitive classification - **all at runtime without data loss**!

Memory Architecture Overview
-----------------------------

.. grid:: 3
   :gutter: 2

   .. grid-item-card:: 📊 Graph Memory
      :img-top: _static/graph-memory-icon.png
      :link: #graph-memory-system
      :link-type: ref
      :class-card: graph-card

      **Dynamically Recompilable Neo4j Knowledge Graphs**
      
      **Runtime-modifiable** semantic relationships and entity connections. Graph schemas, entity types, and relationship patterns can be **modified, serialized, and transferred** between systems without data migration.

      +++
      
      **Dynamic Features**: Hot-swap entity schemas, Live relationship reconfiguration, Runtime graph topology modification, Serializable graph structures

   .. grid-item-card:: 🔍 Vector Memory
      :img-top: _static/vector-memory-icon.png  
      :link: #vector-memory-system
      :link-type: ref
      :class-card: vector-card

      **Recompilable High-Performance Semantic Search**
      
      **Live-reconfigurable** vector embeddings with **hot-swappable** embedding models and **runtime index modification**. Vector stores can be **serialized, transferred, and dynamically recompiled** with different backends.

      +++
      
      **Adaptive Features**: Dynamic embedding model switching, Live vector store migration, Runtime similarity algorithm modification, Serializable vector indices

   .. grid-item-card:: ⏰ Temporal Memory
      :img-top: _static/temporal-memory-icon.png
      :link: #temporal-memory-system  
      :link-type: ref
      :class-card: temporal-card

      **Self-Adapting Time-Aware Intelligence**
      
      **Runtime-configurable** recency weighting and **dynamic consolidation strategies**. Temporal patterns, decay models, and time-based retrieval can be **modified and serialized** while preserving temporal relationships.

      +++
      
      **Temporal Adaptation Features**: Live decay model modification, Dynamic consolidation rule changes, Runtime temporal pattern reconfiguration, Serializable time-based indices

11 Cognitive Memory Types
-------------------------

Our memory system classifies information using 11 distinct cognitive categories, mirroring human memory organization:

.. grid:: 2 2 4 4
   :gutter: 2

   .. grid-item-card:: 🧠 SEMANTIC
      :class-card: memory-type-card semantic

      **Factual Knowledge**
      
      Facts, definitions, concepts, and general world knowledge.

   .. grid-item-card:: 📅 EPISODIC  
      :class-card: memory-type-card episodic

      **Personal Experiences**
      
      Specific events, personal experiences, and autobiographical information.

   .. grid-item-card:: 🔧 PROCEDURAL
      :class-card: memory-type-card procedural

      **Skills & Processes**
      
      How-to knowledge, skills, and step-by-step procedures.

   .. grid-item-card:: 🎯 CONTEXTUAL
      :class-card: memory-type-card contextual

      **Situational Context**
      
      Environment-specific information and situational awareness.

   .. grid-item-card:: 🏢 PROFESSIONAL
      :class-card: memory-type-card professional

      **Work-Related Knowledge**
      
      Job-specific information, professional relationships, and work context.

   .. grid-item-card:: 📚 EDUCATION
      :class-card: memory-type-card education

      **Learning & Study**
      
      Educational content, learning experiences, and academic knowledge.

   .. grid-item-card:: 🤝 SOCIAL
      :class-card: memory-type-card social

      **Relationships & Interactions**
      
      Social connections, relationship dynamics, and interpersonal knowledge.

   .. grid-item-card:: 💭 EMOTIONAL
      :class-card: memory-type-card emotional

      **Feelings & Reactions**
      
      Emotional responses, preferences, and affective associations.

   .. grid-item-card:: 🎨 CREATIVE
      :class-card: memory-type-card creative

      **Imagination & Ideas**
      
      Creative thoughts, artistic expressions, and imaginative content.

   .. grid-item-card:: 📊 ANALYTICAL
      :class-card: memory-type-card analytical

      **Logic & Reasoning**
      
      Analytical thinking, logical deductions, and problem-solving approaches.

   .. grid-item-card:: 🎭 NARRATIVE
      :class-card: memory-type-card narrative

      **Stories & Sequences**
      
      Story-like information, sequences of events, and narrative structures.

Core Memory Agents
------------------

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: SimpleMemoryAgent
      :img-top: _static/simple-memory-large.png
      :link: #simple-memory-agent
      :link-type: ref
      :class-card: memory-agent-card

      **Foundation Memory Agent**
      
      SimpleAgent enhanced with automatic memory classification, storage, and retrieval capabilities.

      +++

      **Key Features:**
      
      * Automatic memory classification
      * Conversation context preservation  
      * Multi-modal retrieval scoring
      * Memory consolidation mechanisms

   .. grid-item-card:: ReactMemoryAgent
      :img-top: _static/react-memory-large.png
      :link: #react-memory-agent
      :link-type: ref
      :class-card: memory-agent-card

      **Reasoning with Memory Context**
      
      ReactAgent with intelligent memory retrieval for context-aware tool execution and reasoning.

      +++

      **Key Features:**
      
      * Context-aware tool selection
      * Memory-guided reasoning
      * Experience-based optimization
      * Adaptive context windows

   .. grid-item-card:: MultiMemoryAgent
      :img-top: _static/multi-memory-large.png
      :link: #multi-memory-agent
      :link-type: ref
      :class-card: memory-agent-card

      **Shared Memory Coordination**
      
      MultiAgent with shared memory systems for coordinated team intelligence and context sharing.

      +++

      **Key Features:**
      
      * Shared memory spaces
      * Cross-agent context transfer
      * Collaborative knowledge building
      * Distributed memory management

   .. grid-item-card:: LongTermMemoryAgent
      :img-top: _static/ltm-large.png
      :link: #long-term-memory-agent
      :link-type: ref
      :class-card: memory-agent-card

      **Advanced Consolidation System**
      
      Agent with sophisticated memory consolidation, importance scoring, and long-term retention mechanisms.

      +++

      **Key Features:**
      
      * Memory importance scoring
      * Automatic consolidation
      * Long-term retention strategies
      * Adaptive forgetting mechanisms

.. _graph-memory-system:

Graph Memory System
-------------------

The graph memory system uses **Neo4j** to create rich, interconnected knowledge representations that mirror how humans organize information.

Core Components
~~~~~~~~~~~~~~~

.. grid:: 2
   :gutter: 2

   .. grid-item-card:: 🏗️ Knowledge Graph Generator
      :class-card: component-card

      **Automatic Graph Construction**
      
      * Entity extraction from text
      * Relationship identification
      * Semantic type classification
      * Graph structure optimization

   .. grid-item-card:: 🔍 Graph RAG Retriever
      :class-card: component-card

      **Advanced Graph Traversal**
      
      * Multi-hop relationship queries
      * Centrality-based ranking
      * Path-aware retrieval
      * Context expansion

   .. grid-item-card:: 📊 Entity Relationship Mapping
      :class-card: component-card

      **Semantic Connections**
      
      * Entity disambiguation
      * Relationship strength scoring
      * Temporal relationship tracking
      * Cross-reference validation

   .. grid-item-card:: 🎯 Context-Aware Querying
      :class-card: component-card

      **Intelligent Information Access**
      
      * Query intent understanding
      * Multi-modal result fusion
      * Relevance ranking
      * Context-sensitive filtering

Usage Examples
~~~~~~~~~~~~~~

.. tab-set::

   .. tab-item:: Basic Graph Memory

      Store and query knowledge with automatic graph construction::

          from haive.agents.memory_reorganized.knowledge import KGGeneratorAgent
          from haive.agents.memory_reorganized.retrieval import GraphRAGRetriever

          # Create knowledge graph generator
          kg_agent = KGGeneratorAgent(
              neo4j_config={
                  "uri": "bolt://localhost:7687",
                  "username": "neo4j",
                  "password": "password"
              }
          )

          # Store information with automatic graph construction
          await kg_agent.store_memory(
              "Alice works at TechCorp as a senior engineer and mentors new hires"
          )
          # Creates entities: Alice, TechCorp, "senior engineer", "mentoring"
          # Creates relationships: Alice works_at TechCorp, Alice mentors new_hires

          # Query with graph traversal
          retriever = GraphRAGRetriever(kg_agent=kg_agent)
          results = await retriever.retrieve_memories(
              "Who mentors people at technology companies?"
          )

   .. tab-item:: Advanced Graph Queries

      Complex multi-hop queries with relationship traversal::

          # Multi-hop relationship query
          query = """
          Find people who work at technology companies and have leadership roles,
          then find who they mentor and what skills those mentees are learning
          """

          results = await retriever.retrieve_memories(
              query,
              max_hops=3,  # Allow 3-hop traversal
              include_relationship_paths=True,
              min_centrality_score=0.1
          )

          # Results include full relationship paths
          for result in results:
              print(f"Memory: {result.memory_content}")
              print(f"Entities: {result.entities}")
              print(f"Relationship path: {result.relationship_path}")
              print(f"Graph centrality: {result.centrality_score}")

   .. tab-item:: Domain-Specific Graphs

      Create specialized knowledge graphs for specific domains::

          # Professional network graph
          professional_kg = KGGeneratorAgent(
              neo4j_config=neo4j_config,
              entity_types=["Person", "Company", "Role", "Skill", "Project"],
              relationship_types=["works_at", "reports_to", "collaborates", "mentors", "has_skill"]
          )

          # Store professional information
          await professional_kg.store_memory(
              "Sarah is the CTO at StartupX, she oversees the engineering team of 15 developers specializing in React and Python"
          )

.. _vector-memory-system:

Vector Memory System
--------------------

High-performance semantic search using dense vector embeddings for fast similarity matching and content discovery.

Core Components
~~~~~~~~~~~~~~~

.. grid:: 2
   :gutter: 2

   .. grid-item-card:: ⚡ Enhanced Retriever
      :class-card: component-card

      **Multi-Factor Scoring System**
      
      * Semantic similarity scoring
      * Recency weighting
      * Importance amplification
      * Context relevance boosting

   .. grid-item-card:: 🎯 Quick Search
      :class-card: component-card

      **Ultra-Fast Retrieval (<10ms)**
      
      * Optimized vector indexing
      * Cached embeddings
      * Approximate nearest neighbors
      * Memory-efficient storage

   .. grid-item-card:: 📊 Pro Search
      :class-card: component-card

      **Deep Analysis (100-500ms)**
      
      * Comprehensive semantic analysis
      * Multi-modal fusion
      * Relationship context integration
      * Advanced ranking algorithms

   .. grid-item-card:: 🔧 Vector Store Integration
      :class-card: component-card

      **Multiple Backend Support**
      
      * Chroma vector database
      * FAISS indexing
      * In-memory stores
      * Distributed scaling

Usage Examples
~~~~~~~~~~~~~~

.. tab-set::

   .. tab-item:: Quick Semantic Search

      Ultra-fast retrieval for real-time applications::

          from haive.agents.memory_reorganized.search.quick_search import QuickSearchAgent

          # Create quick search agent
          quick_search = QuickSearchAgent(
              vector_store="chroma",  # Or "faiss", "inmemory"
              embedding_model="all-MiniLM-L6-v2",
              max_results=5
          )

          # Store memories for search
          await quick_search.store_memory("I love hiking in the mountains")
          await quick_search.store_memory("My favorite outdoor activity is rock climbing")
          await quick_search.store_memory("I prefer indoor activities like reading")

          # Quick semantic search (<10ms)
          results = await quick_search.quick_retrieve("outdoor adventures")
          # Returns hiking and climbing memories with high similarity scores

   .. tab-item:: Multi-Factor Retrieval

      Advanced retrieval with multiple scoring factors::

          from haive.agents.memory_reorganized.retrieval import EnhancedMemoryRetriever

          # Enhanced retriever with multi-factor scoring
          retriever = EnhancedMemoryRetriever(
              vector_store=chroma_store,
              enable_recency_weighting=True,
              enable_importance_scoring=True,
              enable_context_boosting=True
          )

          # Retrieve with comprehensive scoring
          results = await retriever.retrieve_memories(
              query="programming experience",
              max_results=10,
              include_scores=True
          )

          for result in results:
              print(f"Content: {result.content}")
              print(f"Similarity: {result.similarity_score:.3f}")
              print(f"Recency: {result.recency_score:.3f}")
              print(f"Importance: {result.importance_score:.3f}")
              print(f"Final score: {result.final_score:.3f}")

   .. tab-item:: Professional Search

      Deep analysis for complex queries::

          from haive.agents.memory_reorganized.search.pro_search import ProSearchAgent

          # Professional search with deep analysis
          pro_search = ProSearchAgent(
              vector_store=chroma_store,
              graph_store=neo4j_store,
              enable_relationship_context=True,
              analysis_depth="deep"  # "quick", "standard", "deep"
          )

          # Complex query with relationship context
          results = await pro_search.professional_retrieve(
              query="What do I know about Python frameworks for web development?",
              include_relationship_context=True,
              expand_context=True,
              max_analysis_time=500  # ms
          )

.. _temporal-memory-system:

Temporal Memory System
----------------------

Time-aware memory management with recency weighting, consolidation, and temporal pattern recognition.

Core Components
~~~~~~~~~~~~~~~

.. grid:: 2
   :gutter: 2

   .. grid-item-card:: ⏰ Recency Weighting
      :class-card: component-card

      **Time-Based Relevance**
      
      * Exponential decay models
      * Configurable half-life periods
      * Context-aware aging
      * Activity-based refresh

   .. grid-item-card:: 🔄 Memory Consolidation
      :class-card: component-card

      **Intelligent Organization**
      
      * Related memory clustering
      * Redundancy elimination
      * Importance-based retention
      * Automatic summarization

   .. grid-item-card:: 📈 Temporal Patterns
      :class-card: component-card

      **Time-Series Analysis**
      
      * Recurring pattern detection
      * Temporal correlation analysis
      * Seasonal memory activation
      * Predictive memory retrieval

   .. grid-item-card:: 🧹 Adaptive Forgetting
      :class-card: component-card

      **Intelligent Memory Management**
      
      * Low-importance memory removal
      * Storage optimization
      * Performance-based retention
      * Configurable retention policies

Usage Examples
~~~~~~~~~~~~~~

.. tab-set::

   .. tab-item:: Recency-Aware Retrieval

      Retrieve recent memories with higher relevance::

          from haive.agents.memory_reorganized.core import TemporalMemoryManager

          # Create temporal memory manager
          temporal_manager = TemporalMemoryManager(
              recency_half_life=7,  # 7 days
              importance_threshold=0.5,
              max_memory_age=90  # 90 days
          )

          # Store memories with timestamps
          await temporal_manager.store_memory(
              "Started learning React hooks",
              timestamp=datetime.now() - timedelta(days=1)
          )
          await temporal_manager.store_memory(
              "Completed JavaScript course",
              timestamp=datetime.now() - timedelta(days=30)
          )

          # Retrieve with recency weighting
          results = await temporal_manager.retrieve_with_recency(
              query="web development learning",
              include_recency_scores=True
          )

   .. tab-item:: Memory Consolidation

      Automatic organization and consolidation of related memories::

          from haive.agents.memory_reorganized.coordination import MemoryConsolidator

          # Memory consolidation system
          consolidator = MemoryConsolidator(
              consolidation_interval=24,  # hours
              similarity_threshold=0.8,
              max_cluster_size=10
          )

          # Automatic consolidation process
          consolidation_results = await consolidator.consolidate_memories(
              memory_type="PROFESSIONAL",
              time_window_days=30
          )

          print(f"Consolidated {consolidation_results.original_count} memories")
          print(f"Into {consolidation_results.cluster_count} clusters")
          print(f"Storage reduction: {consolidation_results.compression_ratio:.2f}")

   .. tab-item:: Temporal Patterns

      Detect and leverage temporal patterns in memory access::

          from haive.agents.memory_reorganized.core import TemporalPatternAnalyzer

          # Pattern analyzer for temporal insights
          pattern_analyzer = TemporalPatternAnalyzer(
              pattern_window_days=90,
              min_pattern_frequency=3
          )

          # Analyze memory access patterns
          patterns = await pattern_analyzer.analyze_access_patterns(
              memory_types=["PROFESSIONAL", "EDUCATION"],
              include_seasonal=True
          )

          for pattern in patterns:
              print(f"Pattern: {pattern.description}")
              print(f"Frequency: {pattern.frequency}")
              print(f"Confidence: {pattern.confidence:.2f}")
              print(f"Next predicted access: {pattern.next_activation}")

Memory Integration Patterns
----------------------------

.. grid:: 2
   :gutter: 2

   .. grid-item-card:: 🎯 Integrated Memory System
      :link: #integrated-memory-system
      :link-type: ref
      :class-card: integration-card

      **Unified Memory Architecture**
      
      Combines graph, vector, and temporal memory for comprehensive intelligence.

   .. grid-item-card:: 🤝 Multi-Agent Coordination
      :link: #multi-agent-memory-coordination  
      :link-type: ref
      :class-card: integration-card

      **Shared Memory Spaces**
      
      Enable multiple agents to share and coordinate through common memory systems.

   .. grid-item-card:: 📚 Domain-Specific Memory
      :link: #domain-specific-memory
      :link-type: ref
      :class-card: integration-card

      **Specialized Knowledge**
      
      Create focused memory systems for specific domains like medicine, law, or engineering.

   .. grid-item-card:: 🔄 Memory Transfer
      :link: #memory-transfer-patterns
      :link-type: ref
      :class-card: integration-card

      **Knowledge Sharing**
      
      Transfer memories between agents for knowledge propagation and team learning.

.. _integrated-memory-system:

Integrated Memory System
------------------------

The **IntegratedMemorySystem** combines all three memory modalities for comprehensive intelligence:

.. tab-set::

   .. tab-item:: INTEGRATED Mode

      Full integration of graph, vector, and temporal memory::

          from haive.agents.memory_reorganized.coordination import IntegratedMemorySystem

          # Create comprehensive memory system
          memory_system = IntegratedMemorySystem(
              mode="INTEGRATED",  # Graph + Vector + Time
              neo4j_config=neo4j_config,
              vector_store_config=chroma_config,
              enable_consolidation=True,
              enable_importance_scoring=True
          )

          # Store with full processing
          await memory_system.store_memory(
              "Alice mentored me on React development last month, and now I'm building my first web app",
              user_context={"domain": "education"}
          )
          # → Creates graph entities and relationships
          # → Stores vector embeddings for semantic search
          # → Applies temporal weighting and classification

          # Query with multi-modal retrieval
          results = await memory_system.query_memory(
              "Who can help me with web development?",
              include_graph_context=True,
              include_temporal_context=True,
              max_results=5
          )

   .. tab-item:: GRAPH_VECTOR Mode

      Graph and vector memory without temporal features::

          # Graph + Vector (no temporal processing)
          memory_system = IntegratedMemorySystem(
              mode="GRAPH_VECTOR",
              neo4j_config=neo4j_config,
              vector_store_config=chroma_config
          )

          # Optimized for relationship-aware semantic search
          results = await memory_system.query_memory(
              "Technical mentorship relationships",
              prioritize_relationships=True
          )

   .. tab-item:: VECTOR_TIME Mode

      Vector and temporal memory without graph relationships::

          # Vector + Temporal (no graph processing)
          memory_system = IntegratedMemorySystem(
              mode="VECTOR_TIME",
              vector_store_config=chroma_config,
              enable_recency_weighting=True
          )

          # Optimized for time-aware semantic search
          results = await memory_system.query_memory(
              "Recent learning experiences",
              recency_boost=2.0
          )

Dynamic Memory Reconfiguration Examples
-----------------------------------------

**🔄 Live Memory System Transformation:**

Transform memory systems at runtime without data loss:

.. code-block:: python

   # Start with simple vector memory
   memory_system = IntegratedMemorySystem(mode="VECTOR_ONLY")
   
   # Store initial memories
   await memory_system.store_memory("Alice works at TechCorp")
   
   # 🚀 DYNAMICALLY UPGRADE TO FULL GRAPH+VECTOR+TEMPORAL
   await memory_system.live_reconfigure({
       "mode": "INTEGRATED",  # Add graph + temporal processing
       "neo4j_config": neo4j_config,
       "enable_consolidation": True,
       "migrate_existing_data": True  # Preserve all existing memories
   })
   
   # 📡 SERIALIZE ENTIRE SYSTEM INCLUDING DATA
   serialized_state = await memory_system.serialize_complete_state()
   
   # 🔄 TRANSFER TO NEW AGENT/SYSTEM
   new_agent = SimpleMemoryAgent(name="transferred_agent")
   await new_agent.deserialize_memory_system(serialized_state)
   
   # ⚡ MODIFY RETRIEVAL STRATEGIES LIVE
   await new_agent.modify_retrieval_strategy({
       "similarity_algorithm": "cosine",  # Was euclidean
       "graph_traversal_depth": 3,       # Was 2
       "temporal_decay_rate": 0.95       # Was 0.9
   })

**🧠 Hot-Swap Embedding Models:**

Change embedding models without losing semantic relationships:

.. code-block:: python

   # 🔄 LIVE EMBEDDING MODEL MIGRATION
   await memory_system.migrate_embedding_model({
       "from_model": "all-MiniLM-L6-v2",
       "to_model": "text-embedding-ada-002",
       "preserve_similarities": True,     # Maintain relationship strengths
       "background_migration": True,     # Don't block operations
       "validation_sample_size": 1000    # Test on sample first
   })

**📊 Dynamic Graph Schema Evolution:**

Modify graph schemas and entity types at runtime:

.. code-block:: python

   # 🏗️ LIVE GRAPH SCHEMA MODIFICATION
   await graph_memory.evolve_schema({
       "new_entity_types": ["Project", "Technology", "Skill"],
       "new_relationship_types": ["uses", "requires", "expertise_in"],
       "migrate_existing_entities": {
           "Person": {"add_properties": ["experience_level", "specialization"]},
           "Company": {"add_properties": ["industry", "size"]}
       },
       "recompile_existing_relationships": True
   })

Memory-Enhanced Agent Examples
------------------------------

.. tab-set::

   .. tab-item:: Learning Assistant

      Agent that learns and adapts from interactions::

          from haive.agents.memory_reorganized import SimpleMemoryAgent

          # Create learning assistant with comprehensive memory
          assistant = SimpleMemoryAgent(
              name="learning_assistant",
              engine=AugLLMConfig(
                  temperature=0.7,
                  system_message="You are a personalized learning assistant that remembers student progress and adapts recommendations."
              ),
              memory_config={
                  "store_type": "integrated",
                  "enable_classification": True,
                  "consolidation_enabled": True,
                  "neo4j_config": neo4j_config
              }
          )

          # Learning conversation with memory
          await assistant.arun("I'm struggling with Python decorators")
          # Stores: EDUCATION + PROCEDURAL memory

          await assistant.arun("I finished the decorator tutorial you suggested")
          # Updates: Progress tracking, connects to previous memory

          await assistant.arun("What should I learn next in Python?")
          # Retrieves: Learning history, recommends based on progress

   .. tab-item:: Research Agent

      Agent with domain-specific knowledge accumulation::

          from haive.agents.memory_reorganized import ReactMemoryAgent

          # Research agent with tools and memory
          researcher = ReactMemoryAgent(
              name="research_assistant",
              engine=AugLLMConfig(tools=[web_search, paper_analysis]),
              memory_config={
                  "store_type": "graph_vector",
                  "domain_focus": ["research", "academic", "scientific"],
                  "entity_types": ["Author", "Paper", "Concept", "Method"]
              }
          )

          # Research with memory accumulation
          await researcher.arun("Research the latest advances in transformer architectures")
          # Stores: Paper entities, author relationships, concept connections

          await researcher.arun("How do these advances relate to what we learned about attention mechanisms last month?")
          # Retrieves: Previous research, connects new and old knowledge

   .. tab-item:: Team Coordinator

      Multi-agent system with shared memory::

          from haive.agents.memory_reorganized import MultiMemoryAgent

          # Shared memory for team coordination
          team_memory = IntegratedMemorySystem(
              mode="INTEGRATED",
              shared_memory_space="product_team"
          )

          # Create team agents with shared memory
          product_manager = SimpleMemoryAgent(
              name="pm",
              memory_config={"shared_memory": team_memory}
          )

          engineer = ReactMemoryAgent(
              name="engineer",
              memory_config={"shared_memory": team_memory}
          )

          designer = SimpleMemoryAgent(
              name="designer", 
              memory_config={"shared_memory": team_memory}
          )

          # Team coordination with shared context
          team = MultiMemoryAgent(
              name="product_team",
              agents=[product_manager, engineer, designer],
              shared_memory=team_memory
          )

Performance Characteristics
---------------------------

.. grid:: 3
   :gutter: 2

   .. grid-item-card:: ⚡ Speed Benchmarks
      :text-align: center
      :class-card: performance-card

      **Quick Search**: <10ms
      **Standard Retrieval**: 50-100ms
      **Pro Search**: 100-500ms
      **Graph Traversal**: 200-800ms

   .. grid-item-card:: 📊 Scalability Metrics
      :text-align: center
      :class-card: performance-card

      **Memory Capacity**: 100K+ memories
      **Concurrent Agents**: 50+ agents
      **Graph Nodes**: 1M+ entities
      **Vector Dimensions**: 384-1536

   .. grid-item-card:: 🎯 Accuracy Measures
      :text-align: center
      :class-card: performance-card

      **Classification**: 85%+ accuracy
      **Retrieval Relevance**: 90%+ precision
      **Consolidation**: 95%+ retention
      **Pattern Detection**: 80%+ recall

Best Practices
--------------

Memory Configuration Guidelines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. grid:: 2
   :gutter: 2

   .. grid-item-card:: 🎯 Mode Selection
      :class-card: best-practice-card

      **INTEGRATED**: Complex applications needing full intelligence
      **GRAPH_VECTOR**: Relationship-heavy domains (professional networks)
      **VECTOR_TIME**: Content-heavy applications (document management)
      **GRAPH_ONLY**: Pure knowledge graphs (academic research)
      **VECTOR_ONLY**: Fast similarity search (recommendation systems)

   .. grid-item-card:: 🔧 Performance Optimization
      :class-card: best-practice-card

      **Vector Store**: Use Chroma for development, FAISS for production
      **Batch Processing**: Store memories in batches for better performance
      **Index Optimization**: Configure appropriate vector dimensions
      **Memory Limits**: Set reasonable retention periods and cleanup policies

Memory Design Patterns
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :class: memory-patterns-table

   * - Pattern
     - Use Case
     - Memory Types
     - Best Configuration

   * - Personal Assistant
     - Individual user support
     - EPISODIC, CONTEXTUAL, PROFESSIONAL
     - INTEGRATED mode with consolidation

   * - Research Assistant
     - Academic/scientific research
     - SEMANTIC, ANALYTICAL, EDUCATION
     - GRAPH_VECTOR with domain entities

   * - Learning System
     - Educational applications
     - EDUCATION, PROCEDURAL, EPISODIC
     - INTEGRATED with progress tracking

   * - Team Coordination
     - Multi-agent collaboration
     - PROFESSIONAL, SOCIAL, CONTEXTUAL
     - Shared INTEGRATED memory

   * - Content Management
     - Document/content systems
     - SEMANTIC, NARRATIVE, CREATIVE
     - VECTOR_TIME with recency weighting

Next Steps
----------

- :doc:`quickstart` - Get started with memory-enhanced agents
- :doc:`agent_types` - Learn about different agent capabilities
- :doc:`conversation_orchestration` - Add memory to conversations
- :doc:`advanced` - Explore self-modifying memory systems
- :doc:`examples` - See complete memory system implementations