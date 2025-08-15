agents.memory_reorganized.coordination.multi_agent_coordinator
==============================================================

.. py:module:: agents.memory_reorganized.coordination.multi_agent_coordinator

.. autoapi-nested-parse::

   Multi-Agent Memory Coordinator using MetaStateSchema patterns.

   This module provides a comprehensive coordinator that orchestrates multiple memory
   agents using the MetaStateSchema pattern for proper state management and agent
   composition.


   .. autolink-examples:: agents.memory_reorganized.coordination.multi_agent_coordinator
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory_reorganized.coordination.multi_agent_coordinator.logger


Classes
-------

.. autoapisummary::

   agents.memory_reorganized.coordination.multi_agent_coordinator.MemoryAgentCapabilities
   agents.memory_reorganized.coordination.multi_agent_coordinator.MemoryTask
   agents.memory_reorganized.coordination.multi_agent_coordinator.MultiAgentCoordinatorConfig
   agents.memory_reorganized.coordination.multi_agent_coordinator.MultiAgentMemoryCoordinator


Module Contents
---------------

.. py:class:: MemoryAgentCapabilities(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Describes the capabilities and characteristics of a memory agent.

   This model defines what a memory agent can do, its performance characteristics,
   and specializations. It's used by the multi-agent coordinator for intelligent
   task routing and load balancing.

   .. attribute:: agent_name

      Unique identifier for the agent

   .. attribute:: agent_type

      Class or type name of the agent (e.g., "KGGeneratorAgent")

   .. attribute:: can_store_memories

      Whether the agent can store new memories

   .. attribute:: can_retrieve_memories

      Whether the agent can retrieve existing memories

   .. attribute:: can_analyze_memories

      Whether the agent can analyze memory content

   .. attribute:: can_generate_knowledge_graph

      Whether the agent can build knowledge graphs

   .. attribute:: can_coordinate_retrieval

      Whether the agent can coordinate retrieval strategies

   .. attribute:: supported_memory_types

      List of memory types the agent can handle

   .. attribute:: typical_latency_ms

      Expected response time in milliseconds

   .. attribute:: max_concurrent_tasks

      Maximum number of concurrent tasks the agent can handle

   .. attribute:: specialization

      List of agent specializations and strengths

   .. rubric:: Examples

   KG Generator Agent capabilities::

       kg_capabilities = MemoryAgentCapabilities(
           agent_name="kg_generator",
           agent_type="KGGeneratorAgent",
           can_analyze_memories=True,
           can_generate_knowledge_graph=True,
           supported_memory_types=[
               MemoryType.SEMANTIC,
               MemoryType.EPISODIC,
               MemoryType.CONTEXTUAL
           ],
           typical_latency_ms=2000,
           max_concurrent_tasks=2,
           specialization=[
               "entity_extraction",
               "relationship_discovery",
               "graph_construction"
           ]
       )

   Agentic RAG Coordinator capabilities::

       rag_capabilities = MemoryAgentCapabilities(
           agent_name="agentic_rag",
           agent_type="AgenticRAGCoordinator",
           can_retrieve_memories=True,
           can_coordinate_retrieval=True,
           supported_memory_types=list(MemoryType),  # Supports all types
           typical_latency_ms=1500,
           max_concurrent_tasks=3,
           specialization=[
               "strategy_selection",
               "result_fusion",
               "intelligent_retrieval"
           ]
       )

   Memory Store Agent capabilities::

       store_capabilities = MemoryAgentCapabilities(
           agent_name="memory_store",
           agent_type="MemoryStoreAgent",
           can_store_memories=True,
           can_retrieve_memories=True,
           supported_memory_types=list(MemoryType),
           typical_latency_ms=500,
           max_concurrent_tasks=5,
           specialization=[
               "memory_storage",
               "basic_retrieval",
               "memory_management"
           ]
       )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryAgentCapabilities
      :collapse:

   .. py:attribute:: agent_name
      :type:  str
      :value: None



   .. py:attribute:: agent_type
      :type:  str
      :value: None



   .. py:attribute:: can_analyze_memories
      :type:  bool
      :value: None



   .. py:attribute:: can_coordinate_retrieval
      :type:  bool
      :value: None



   .. py:attribute:: can_generate_knowledge_graph
      :type:  bool
      :value: None



   .. py:attribute:: can_retrieve_memories
      :type:  bool
      :value: None



   .. py:attribute:: can_store_memories
      :type:  bool
      :value: None



   .. py:attribute:: max_concurrent_tasks
      :type:  int
      :value: None



   .. py:attribute:: specialization
      :type:  list[str]
      :value: None



   .. py:attribute:: supported_memory_types
      :type:  list[haive.agents.memory.core.types.MemoryType]
      :value: None



   .. py:attribute:: typical_latency_ms
      :type:  float
      :value: None



.. py:class:: MemoryTask(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a memory-related task for multi-agent coordination.

   A MemoryTask encapsulates a specific memory operation (store, retrieve, analyze, etc.)
   that can be executed by the multi-agent coordinator system. It contains all necessary
   information for task routing, execution, and result tracking.

   .. attribute:: id

      Unique identifier for the task, used for tracking and coordination

   .. attribute:: type

      Type of memory operation (store, retrieve, analyze, generate_kg, etc.)

   .. attribute:: query

      Natural language description of the task or query content

   .. attribute:: parameters

      Dictionary of task-specific parameters and configuration

   .. attribute:: priority

      Task priority level (1=highest, 10=lowest) for execution ordering

   .. attribute:: namespace

      Memory namespace to operate within (e.g., ("user", "personal"))

   .. attribute:: memory_types

      Specific memory types to target (semantic, episodic, etc.)

   .. attribute:: status

      Current task status (pending, routing, executing, completed, failed)

   .. attribute:: assigned_agent

      Name of the agent assigned to execute this task

   .. attribute:: result

      Task execution result (populated after completion)

   .. attribute:: error

      Error message if task execution failed

   .. attribute:: created_at

      UTC timestamp when the task was created

   .. attribute:: started_at

      UTC timestamp when task execution started

   .. attribute:: completed_at

      UTC timestamp when task execution completed

   .. rubric:: Examples

   Creating a memory storage task::

       task = MemoryTask(
           id="store_001",
           type="store_memory",
           query="Store information about Python programming",
           parameters={"content": "Python is a programming language"},
           priority=3,
           namespace=("user", "learning")
       )

   Creating a retrieval task::

       task = MemoryTask(
           id="retrieve_001",
           type="retrieve_memories",
           query="Find information about machine learning",
           parameters={"limit": 10, "use_graph_rag": True},
           priority=1,
           memory_types=[MemoryType.SEMANTIC, MemoryType.EPISODIC]
       )

   Creating an analysis task::

       task = MemoryTask(
           id="analyze_001",
           type="analyze_memory",
           query="Analyze patterns in my learning history",
           parameters={"analysis_type": "pattern_detection"},
           priority=2
       )

   Creating a knowledge graph generation task::

       task = MemoryTask(
           id="kg_001",
           type="generate_knowledge_graph",
           query="Build knowledge graph from recent memories",
           parameters={"max_memories": 100, "confidence_threshold": 0.7},
           priority=4,
           namespace=("user", "work")
       )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryTask
      :collapse:

   .. py:attribute:: assigned_agent
      :type:  haive.agents.memory.agentic_rag_coordinator.Optional[str]
      :value: None



   .. py:attribute:: completed_at
      :type:  haive.agents.memory.agentic_rag_coordinator.Optional[datetime.datetime]
      :value: None



   .. py:attribute:: created_at
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: error
      :type:  haive.agents.memory.agentic_rag_coordinator.Optional[str]
      :value: None



   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: memory_types
      :type:  list[haive.agents.memory.core.types.MemoryType] | None
      :value: None



   .. py:attribute:: namespace
      :type:  tuple[str, Ellipsis] | None
      :value: None



   .. py:attribute:: parameters
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: priority
      :type:  int
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



   .. py:attribute:: result
      :type:  haive.agents.memory.agentic_rag_coordinator.Optional[Any]
      :value: None



   .. py:attribute:: started_at
      :type:  haive.agents.memory.agentic_rag_coordinator.Optional[datetime.datetime]
      :value: None



   .. py:attribute:: status
      :type:  str
      :value: None



   .. py:attribute:: type
      :type:  str
      :value: None



.. py:class:: MultiAgentCoordinatorConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for Multi-Agent Memory Coordinator.

   This configuration class defines all parameters needed to create and configure
   a MultiAgentMemoryCoordinator, including agent configurations, coordination settings,
   and performance parameters.

   .. attribute:: name

      Unique identifier for the coordinator instance

   .. attribute:: memory_store_manager

      Manager for memory storage and retrieval operations

   .. attribute:: memory_classifier

      Classifier for analyzing memory content and types

   .. attribute:: kg_generator_config

      Configuration for the knowledge graph generator agent

   .. attribute:: agentic_rag_config

      Configuration for the agentic RAG coordinator agent

   .. attribute:: max_concurrent_tasks

      Maximum number of tasks that can execute simultaneously

   .. attribute:: task_timeout_seconds

      Maximum time (in seconds) a task can run before timing out

   .. attribute:: enable_agent_communication

      Whether to enable communication between agents

   .. attribute:: coordinator_llm

      LLM configuration for the coordinator's decision-making

   .. attribute:: routing_strategy

      Strategy for routing tasks to agents (capability_based, load_balanced, etc.)

   .. attribute:: enable_task_decomposition

      Whether to enable breaking complex tasks into subtasks

   .. attribute:: enable_caching

      Whether to enable result caching for performance

   .. attribute:: cache_ttl_seconds

      Time-to-live for cached results in seconds

   .. attribute:: persistence

      Persistence configuration passed to sub-agents

   .. rubric:: Examples

   Basic configuration::

       config = MultiAgentCoordinatorConfig(
           name="my_coordinator",
           memory_store_manager=store_manager,
           memory_classifier=classifier,
           kg_generator_config=kg_config,
           agentic_rag_config=rag_config,
           max_concurrent_tasks=3,
           task_timeout_seconds=180
       )

   Advanced configuration with custom settings::

       config = MultiAgentCoordinatorConfig(
           name="advanced_coordinator",
           memory_store_manager=store_manager,
           memory_classifier=classifier,
           kg_generator_config=kg_config,
           agentic_rag_config=rag_config,

           # Coordination settings
           max_concurrent_tasks=10,
           task_timeout_seconds=600,
           enable_agent_communication=True,

           # Coordinator LLM
           coordinator_llm=AugLLMConfig(
               model="gpt-4",
               temperature=0.2,
               max_tokens=1000
           ),

           # Task routing
           routing_strategy="capability_based",
           enable_task_decomposition=True,

           # Performance
           enable_caching=True,
           cache_ttl_seconds=7200,  # 2 hours

           # Persistence
           persistence=False  # Disable for testing
       )

   Production configuration::

       config = MultiAgentCoordinatorConfig(
           name="production_coordinator",
           memory_store_manager=store_manager,
           memory_classifier=classifier,
           kg_generator_config=kg_config,
           agentic_rag_config=rag_config,

           # High-performance settings
           max_concurrent_tasks=20,
           task_timeout_seconds=900,
           enable_agent_communication=True,

           # Optimized coordinator
           coordinator_llm=AugLLMConfig(
               model="gpt-4-turbo",
               temperature=0.1,
               max_tokens=2000
           ),

           # Advanced routing
           routing_strategy="load_balanced",
           enable_task_decomposition=True,

           # Production caching
           enable_caching=True,
           cache_ttl_seconds=3600
       )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MultiAgentCoordinatorConfig
      :collapse:

   .. py:attribute:: agentic_rag_config
      :type:  haive.agents.memory.agentic_rag_coordinator.AgenticRAGCoordinatorConfig
      :value: None



   .. py:attribute:: cache_ttl_seconds
      :type:  int
      :value: None



   .. py:attribute:: coordinator_llm
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: enable_agent_communication
      :type:  bool
      :value: None



   .. py:attribute:: enable_caching
      :type:  bool
      :value: None



   .. py:attribute:: enable_task_decomposition
      :type:  bool
      :value: None



   .. py:attribute:: kg_generator_config
      :type:  haive.agents.memory.kg_generator_agent.KGGeneratorAgentConfig
      :value: None



   .. py:attribute:: max_concurrent_tasks
      :type:  int
      :value: None



   .. py:attribute:: memory_classifier
      :type:  haive.agents.memory.core.classifier.MemoryClassifier
      :value: None



   .. py:attribute:: memory_store_manager
      :type:  haive.agents.memory.core.stores.MemoryStoreManager
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: persistence
      :type:  Any
      :value: None



   .. py:attribute:: routing_strategy
      :type:  str
      :value: None



   .. py:attribute:: task_timeout_seconds
      :type:  int
      :value: None



.. py:class:: MultiAgentMemoryCoordinator(config: MultiAgentCoordinatorConfig)

   Orchestrates multiple memory agents using MetaStateSchema patterns.

   The MultiAgentMemoryCoordinator is the central orchestrator for the memory system,
   managing a collection of specialized memory agents and intelligently routing tasks
   based on agent capabilities, performance characteristics, and current load.

   This coordinator provides:
   - Intelligent task routing based on agent capabilities
   - Load balancing across multiple agents
   - Task decomposition for complex operations
   - Performance monitoring and optimization
   - Fault tolerance and error handling
   - Agent communication and coordination

   .. attribute:: config

      Configuration object containing all coordinator settings

   .. attribute:: memory_store

      Memory store manager for direct storage operations

   .. attribute:: classifier

      Memory classifier for content analysis

   .. attribute:: coordinator_llm

      LLM runnable for coordinator decision-making

   .. attribute:: meta_agents

      Dictionary of agents wrapped in MetaStateSchema

   .. attribute:: agent_capabilities

      Dictionary mapping agent names to their capabilities

   .. attribute:: task_queue

      List of pending tasks waiting for execution

   .. attribute:: active_tasks

      Dictionary of currently executing tasks

   .. attribute:: completed_tasks

      Dictionary of completed tasks with results

   .. attribute:: performance_metrics

      Dictionary tracking system performance metrics

   .. rubric:: Examples

   Basic coordinator usage::

       # Create coordinator
       coordinator = MultiAgentMemoryCoordinator(config)

       # Store memory
       result = await coordinator.store_memory(
           "I learned about machine learning algorithms today"
       )

       # Retrieve memories
       memories = await coordinator.retrieve_memories(
           query="machine learning",
           limit=5
       )

       # Analyze memory content
       analysis = await coordinator.analyze_memory(
           "Complex analysis of learning patterns"
       )

   Advanced task execution::

       # Create custom task
       task = MemoryTask(
           id="complex_analysis",
           type="analyze_and_graph",
           query="Analyze learning patterns and build knowledge graph",
           parameters={
               "analysis_depth": "comprehensive",
               "graph_confidence": 0.8
           },
           priority=1
       )

       # Execute task
       result = await coordinator.execute_task(task)

       # Check task status
       if result.status == "completed":
           print(f"Task completed: {result.result}")
       else:
           print(f"Task failed: {result.error}")

   System monitoring::

       # Get system status
       status = coordinator.get_system_status()
       print(f"Total agents: {status['total_agents']}")
       print(f"Active tasks: {status['active_tasks']}")

       # Run diagnostic
       diagnostic = await coordinator.run_diagnostic()
       if diagnostic["system_status"] == "healthy":
           print("System is healthy")
       else:
           print("System issues detected")

   Performance monitoring::

       # Get performance metrics
       metrics = coordinator.performance_metrics
       print(f"Total tasks: {metrics['total_tasks']}")
       print(f"Success rate: {metrics['successful_tasks'] / metrics['total_tasks'] * 100:.1f}%")
       print(f"Average latency: {metrics['avg_latency_ms']:.1f}ms")

   Initialize the multi-agent coordinator.

   Sets up the coordinator with the provided configuration, initializes
   all managed agents, and prepares the task management system.

   :param config: MultiAgentCoordinatorConfig containing all coordinator settings

   .. rubric:: Examples

   Basic initialization::

       config = MultiAgentCoordinatorConfig(
           memory_store_manager=store_manager,
           memory_classifier=classifier,
           kg_generator_config=kg_config,
           agentic_rag_config=rag_config
       )

       coordinator = MultiAgentMemoryCoordinator(config)

   Advanced initialization with custom settings::

       config = MultiAgentCoordinatorConfig(
           name="production_coordinator",
           memory_store_manager=store_manager,
           memory_classifier=classifier,
           kg_generator_config=kg_config,
           agentic_rag_config=rag_config,
           max_concurrent_tasks=10,
           task_timeout_seconds=600,
           enable_caching=True
       )

       coordinator = MultiAgentMemoryCoordinator(config)


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MultiAgentMemoryCoordinator
      :collapse:

   .. py:method:: _create_classifier_agent() -> haive.agents.simple.SimpleAgent

      Create a simple agent wrapper for memory classification.


      .. autolink-examples:: _create_classifier_agent
         :collapse:


   .. py:method:: _create_store_agent() -> haive.agents.simple.SimpleAgent

      Create a simple agent wrapper for memory store operations.


      .. autolink-examples:: _create_store_agent
         :collapse:


   .. py:method:: _execute_decomposed_task(task: MemoryTask, routing_decision: dict[str, Any]) -> Any
      :async:


      Execute task that has been decomposed into subtasks.


      .. autolink-examples:: _execute_decomposed_task
         :collapse:


   .. py:method:: _execute_multi_agent_task(task: MemoryTask, routing_decision: dict[str, Any]) -> Any
      :async:


      Execute task with multiple agents in parallel.


      .. autolink-examples:: _execute_multi_agent_task
         :collapse:


   .. py:method:: _execute_sequential_task(task: MemoryTask, routing_decision: dict[str, Any]) -> Any
      :async:


      Execute task with agents in sequence.


      .. autolink-examples:: _execute_sequential_task
         :collapse:


   .. py:method:: _execute_single_agent_task(task: MemoryTask, routing_decision: dict[str, Any]) -> Any
      :async:


      Execute task with a single agent.


      .. autolink-examples:: _execute_single_agent_task
         :collapse:


   .. py:method:: _fallback_task_routing(task: MemoryTask) -> dict[str, Any]

      Fallback rule-based task routing.


      .. autolink-examples:: _fallback_task_routing
         :collapse:


   .. py:method:: _parse_json_response(response: str) -> dict[str, Any] | None

      Parse JSON response from LLM.


      .. autolink-examples:: _parse_json_response
         :collapse:


   .. py:method:: _route_task(task: MemoryTask) -> dict[str, Any]
      :async:


      Route task to appropriate agents using LLM-based intelligent routing.

      This method analyzes the task and uses the coordinator's LLM to determine
      the best routing strategy and agent assignment. It considers agent capabilities,
      specializations, current load, and task requirements.

      :param task: MemoryTask to route containing query, type, and parameters

      :returns:

                Routing decision containing:
                    - routing_decision: Strategy type (single_agent, multi_agent, sequential, decompose)
                    - primary_agent: Name of primary agent to handle the task
                    - secondary_agents: List of secondary agents (if applicable)
                    - execution_strategy: How to execute (single, parallel, sequential)
                    - reasoning: Explanation of routing decision
                    - estimated_time_ms: Expected execution time
                    - confidence: Confidence score (0.0-1.0)
      :rtype: Dict[str, Any]

      .. rubric:: Examples

      The returned routing decision format::

          {
              "routing_decision": "single_agent",
              "primary_agent": "agentic_rag",
              "secondary_agents": [],
              "execution_strategy": "single",
              "reasoning": "Query requires retrieval expertise",
              "estimated_time_ms": 1500,
              "confidence": 0.9
          }

      Multi-agent routing example::

          {
              "routing_decision": "multi_agent",
              "primary_agent": "kg_generator",
              "secondary_agents": ["memory_classifier", "agentic_rag"],
              "execution_strategy": "parallel",
              "reasoning": "Complex analysis requires multiple perspectives",
              "estimated_time_ms": 2500,
              "confidence": 0.85
          }


      .. autolink-examples:: _route_task
         :collapse:


   .. py:method:: _setup_agents() -> None

      Setup and wrap agents with MetaStateSchema.


      .. autolink-examples:: _setup_agents
         :collapse:


   .. py:method:: _setup_prompts() -> None

      Setup prompts for task routing and coordination.


      .. autolink-examples:: _setup_prompts
         :collapse:


   .. py:method:: _update_performance_metrics(task: MemoryTask, success: bool) -> None

      Update performance metrics.


      .. autolink-examples:: _update_performance_metrics
         :collapse:


   .. py:method:: analyze_memory(content: str) -> dict[str, Any]
      :async:


      Analyze memory content using the multi-agent system with specialized routing.

      This method creates a memory analysis task and routes it to the most appropriate
      agent (typically the memory classifier). The system provides comprehensive
      analysis including classification, entity extraction, and importance scoring.

      :param content: The memory content to analyze (text, structured data, etc.)

      :returns:

                Analysis results containing:
                    - analysis: Detailed analysis results from the assigned agent
                    - success: Boolean indicating if analysis completed successfully
                    - error: Error message if analysis failed
      :rtype: Dict[str, Any]

      .. rubric:: Examples

      Basic memory analysis::

          analysis = await coordinator.analyze_memory(
              "I attended a machine learning conference where I learned about neural networks"
          )

          if analysis["success"]:
              result = analysis["analysis"]
              print(f"Memory type: {result.get('memory_type')}")
              print(f"Entities: {result.get('entities')}")
              print(f"Importance: {result.get('importance_score')}")
          else:
              print(f"Analysis failed: {analysis['error']}")

      Complex content analysis::

          analysis = await coordinator.analyze_memory(
              '''
              Meeting Notes: Q1 Planning
              Attendees: Alice (PM), Bob (Engineer), Carol (Designer)
              Decisions:
              - Use React for the frontend
              - Deploy on AWS with auto-scaling
              - Launch beta by March 15th
              '''
          )

          if analysis["success"]:
              result = analysis["analysis"]
              print(f"Extracted entities: {result.get('entities')}")
              print(f"Key decisions: {result.get('decisions')}")
              print(f"Action items: {result.get('action_items')}")
              print(f"Participants: {result.get('participants')}")

      .. note::

         The analysis typically includes:
         - Memory type classification (semantic, episodic, procedural, etc.)
         - Entity extraction (people, organizations, concepts, etc.)
         - Importance and relevance scoring
         - Metadata extraction (dates, locations, etc.)
         - Relationship identification
         - Content summarization


      .. autolink-examples:: analyze_memory
         :collapse:


   .. py:method:: execute_task(task: MemoryTask) -> MemoryTask
      :async:


      Execute a memory task using appropriate agents with intelligent routing.

      This method is the core of the multi-agent coordinator, responsible for:
      1. Routing tasks to the most appropriate agent(s)
      2. Executing tasks based on routing decisions
      3. Handling different execution strategies (single, multi, sequential, decomposed)
      4. Updating performance metrics and task status

      :param task: MemoryTask to execute containing query, parameters, and metadata

      :returns: The same task object updated with results, status, and timing
      :rtype: MemoryTask

      :raises ValueError: If routing decision is unknown or invalid
      :raises RuntimeError: If task execution fails due to agent errors

      .. rubric:: Examples

      Basic task execution::

          task = MemoryTask(
              id="simple_task",
              type="retrieve_memories",
              query="Find information about Python programming",
              priority=1
          )

          result_task = await coordinator.execute_task(task)

          if result_task.status == "completed":
              print(f"Task completed: {result_task.result}")
          else:
              print(f"Task failed: {result_task.error}")

      Complex task with custom parameters::

          task = MemoryTask(
              id="complex_analysis",
              type="analyze_and_graph",
              query="Analyze learning patterns and build knowledge graph",
              parameters={
                  "analysis_depth": "comprehensive",
                  "graph_confidence": 0.8,
                  "include_relationships": True
              },
              priority=1,
              namespace=("user", "work")
          )

          result_task = await coordinator.execute_task(task)

          # Check execution details
          print(f"Assigned agent: {result_task.assigned_agent}")
          print(f"Duration: {result_task.completed_at - result_task.started_at}")
          print(f"Result: {result_task.result}")

      Error handling::

          try:
              result_task = await coordinator.execute_task(task)

              if result_task.status == "failed":
                  logger.error(f"Task {task.id} failed: {result_task.error}")
                  # Handle failure - maybe retry or use fallback

          except Exception as e:
              logger.error(f"Unexpected error executing task: {e}")


      .. autolink-examples:: execute_task
         :collapse:


   .. py:method:: generate_knowledge_graph(namespace: tuple[str, Ellipsis] | None = None) -> dict[str, Any]
      :async:


      Generate knowledge graph using the multi-agent system with KG specialization.

      This method creates a knowledge graph generation task and routes it to the
      specialized KG generator agent. The system extracts entities, relationships,
      and builds a comprehensive knowledge graph from stored memories.

      :param namespace: Optional namespace tuple to limit graph generation scope

      :returns:

                Knowledge graph results containing:
                    - knowledge_graph: Generated graph with nodes and relationships
                    - success: Boolean indicating if generation completed successfully
                    - error: Error message if generation failed
      :rtype: Dict[str, Any]

      .. rubric:: Examples

      Basic knowledge graph generation::

          kg_result = await coordinator.generate_knowledge_graph()

          if kg_result["success"]:
              graph = kg_result["knowledge_graph"]
              print(f"Nodes: {len(graph.get('nodes', []))}")
              print(f"Relationships: {len(graph.get('relationships', []))}")

              # Explore entities
              for node in graph.get('nodes', []):
                  print(f"Entity: {node['name']} ({node['type']})")

              # Explore relationships
              for rel in graph.get('relationships', []):
                  print(f"{rel['source']} -> {rel['target']} ({rel['type']})")
          else:
              print(f"KG generation failed: {kg_result['error']}")

      Scoped knowledge graph generation::

          kg_result = await coordinator.generate_knowledge_graph(
              namespace=("user", "work", "projects")
          )

          if kg_result["success"]:
              graph = kg_result["knowledge_graph"]

              # Analyze work-related entities
              work_entities = [
                  node for node in graph.get('nodes', [])
                  if node.get('type') in ['person', 'organization', 'project']
              ]

              print(f"Work entities: {len(work_entities)}")

              # Find project relationships
              project_rels = [
                  rel for rel in graph.get('relationships', [])
                  if 'project' in rel.get('type', '').lower()
              ]

              print(f"Project relationships: {len(project_rels)}")

      .. note::

         The knowledge graph typically includes:
         - Entities: People, organizations, concepts, technologies, etc.
         - Relationships: Works_at, uses, knows, creates, etc.
         - Confidence scores for entities and relationships
         - Metadata: Creation timestamps, memory references, etc.
         - Graph statistics: Node counts, relationship types, etc.


      .. autolink-examples:: generate_knowledge_graph
         :collapse:


   .. py:method:: get_system_status() -> dict[str, Any]

      Get comprehensive system status and health information.

      This method provides a complete overview of the multi-agent system's current
      state, including agent health, performance metrics, and operational status.

      :returns:

                System status containing:
                    - coordinator_status: Overall coordinator status (active, degraded, error)
                    - total_agents: Number of managed agents
                    - active_tasks: Number of currently executing tasks
                    - completed_tasks: Number of completed tasks
                    - performance_metrics: System performance statistics
                    - agent_status: Individual agent status and health
                    - agent_capabilities: Summary of each agent's capabilities
      :rtype: Dict[str, Any]

      .. rubric:: Examples

      Basic system status check::

          status = coordinator.get_system_status()

          print(f"Coordinator: {status['coordinator_status']}")
          print(f"Total agents: {status['total_agents']}")
          print(f"Active tasks: {status['active_tasks']}")
          print(f"Success rate: {status['performance_metrics']['successful_tasks'] / status['performance_metrics']['total_tasks'] * 100:.1f}%")

      Detailed agent status::

          status = coordinator.get_system_status()

          for agent_name, agent_info in status['agent_status'].items():
              print(f"Agent: {agent_name}")
              print(f"  Type: {agent_info['agent_type']}")
              print(f"  Status: {agent_info['execution_status']}")
              print(f"  Executions: {agent_info['execution_count']}")
              print(f"  Needs recompile: {agent_info['needs_recompile']}")

      Performance monitoring::

          status = coordinator.get_system_status()
          metrics = status['performance_metrics']

          print(f"Total tasks: {metrics['total_tasks']}")
          print(f"Successful: {metrics['successful_tasks']}")
          print(f"Failed: {metrics['failed_tasks']}")
          print(f"Average latency: {metrics['avg_latency_ms']:.1f}ms")

          # Agent utilization
          for agent, count in metrics['agent_utilization'].items():
              utilization = count / metrics['total_tasks'] * 100
              print(f"Agent {agent}: {utilization:.1f}% utilization")

      .. note::

         This method is synchronous and provides a snapshot of the current system
         state. For continuous monitoring, call this method periodically or use
         the run_diagnostic() method for health checks.


      .. autolink-examples:: get_system_status
         :collapse:


   .. py:method:: retrieve_memories(query: str, limit: int = 10, memory_types: list[haive.agents.memory.core.types.MemoryType] | None = None, namespace: tuple[str, Ellipsis] | None = None) -> list[dict[str, Any]]
      :async:


      Retrieve memories using the multi-agent system with intelligent routing.

      This method creates a memory retrieval task and routes it to the most appropriate
      agent (typically the agentic RAG coordinator). The system automatically selects
      the best retrieval strategy based on the query characteristics.

      :param query: Natural language query describing what memories to retrieve
      :param limit: Maximum number of memories to return (default: 10)
      :param memory_types: Optional list of specific memory types to search within
      :param namespace: Optional namespace tuple to limit search scope

      :returns: List of memory objects with content, metadata, and relevance scores
      :rtype: List[Dict[str, Any]]

      .. rubric:: Examples

      Basic memory retrieval::

          memories = await coordinator.retrieve_memories(
              "What did I learn about Python programming?"
          )

          for memory in memories:
              print(f"Content: {memory['content']}")
              print(f"Relevance: {memory['relevance_score']}")
              print(f"Timestamp: {memory['timestamp']}")

      Targeted retrieval with filters::

          memories = await coordinator.retrieve_memories(
              query="machine learning algorithms",
              limit=5,
              memory_types=[MemoryType.SEMANTIC, MemoryType.EPISODIC],
              namespace=("user", "learning")
          )

      Complex query with context::

          memories = await coordinator.retrieve_memories(
              "Find all meetings where we discussed the API project and show related decisions",
              limit=20,
              namespace=("user", "work")
          )

          # System automatically uses graph traversal for complex queries
          for memory in memories:
              if memory.get('graph_connections'):
                  print(f"Connected entities: {memory['graph_connections']}")

      .. note::

         The system automatically:
         - Analyzes query complexity and selects appropriate retrieval strategy
         - Uses vector similarity, graph traversal, or hybrid approaches
         - Applies relevance scoring and ranking
         - Returns structured results with metadata and provenance


      .. autolink-examples:: retrieve_memories
         :collapse:


   .. py:method:: run_diagnostic() -> dict[str, Any]
      :async:


      Run comprehensive system diagnostic with agent health checks.

      This method performs a complete system diagnostic by testing each agent
      with a simple diagnostic query. It identifies unhealthy agents and provides
      detailed error information for troubleshooting.

      :returns:

                Diagnostic results containing:
                    - system_status: Overall system health (healthy, degraded, critical)
                    - agent_diagnostics: Individual agent diagnostic results
                    - performance_metrics: Current system performance metrics
      :rtype: Dict[str, Any]

      .. rubric:: Examples

      Basic diagnostic check::

          diagnostic = await coordinator.run_diagnostic()

          print(f"System status: {diagnostic['system_status']}")

          if diagnostic['system_status'] != 'healthy':
              print("Issues detected:")
              for agent, result in diagnostic['agent_diagnostics'].items():
                  if result['status'] != 'healthy':
                      print(f"  {agent}: {result.get('error', 'Unknown error')}")
          else:
              print("All agents are healthy")

      Detailed diagnostic analysis::

          diagnostic = await coordinator.run_diagnostic()

          for agent_name, result in diagnostic['agent_diagnostics'].items():
              print(f"Agent: {agent_name}")
              print(f"  Status: {result['status']}")

              if result['status'] == 'healthy':
                  print(f"  Test result: {result.get('test_result', 'N/A')}")
              else:
                  print(f"  Error: {result.get('error', 'Unknown error')}")

      Performance analysis::

          diagnostic = await coordinator.run_diagnostic()
          metrics = diagnostic['performance_metrics']

          if metrics['total_tasks'] > 0:
              success_rate = metrics['successful_tasks'] / metrics['total_tasks']
              print(f"Success rate: {success_rate * 100:.1f}%")

              if success_rate < 0.9:
                  print("Warning: Low success rate detected")

              if metrics['avg_latency_ms'] > 5000:
                  print("Warning: High latency detected")

      .. note::

         This diagnostic runs a simple test query on each agent to verify basic
         functionality. For production systems, consider running this periodically
         to monitor system health and detect degradation early.


      .. autolink-examples:: run_diagnostic
         :collapse:


   .. py:method:: store_memory(content: str, namespace: tuple[str, Ellipsis] | None = None) -> str
      :async:


      Store a memory using the multi-agent system with intelligent routing.

      This method creates a memory storage task and routes it to the appropriate
      agent (typically the memory store agent). The system automatically handles
      classification, metadata extraction, and storage optimization.

      :param content: The memory content to store (text, structured data, etc.)
      :param namespace: Optional namespace tuple for organizing memories (e.g., ("user", "work"))

      :returns: Success message with storage details or error message
      :rtype: str

      .. rubric:: Examples

      Basic memory storage::

          result = await coordinator.store_memory(
              "I learned about machine learning algorithms today"
          )
          print(result)  # "Memory stored successfully: {...}"

      Memory with namespace::

          result = await coordinator.store_memory(
              "Completed project milestone: API integration",
              namespace=("user", "work", "projects")
          )

      Structured memory storage::

          result = await coordinator.store_memory(
              json.dumps({
                  "event": "meeting",
                  "participants": ["Alice", "Bob"],
                  "decisions": ["Use React for frontend", "Deploy on AWS"]
              }),
              namespace=("user", "work", "meetings")
          )

      .. note::

         The system automatically classifies the memory type, extracts metadata,
         and updates relevant knowledge graphs based on the content.


      .. autolink-examples:: store_memory
         :collapse:


   .. py:attribute:: active_tasks
      :type:  dict[str, MemoryTask]


   .. py:attribute:: agent_capabilities
      :type:  dict[str, MemoryAgentCapabilities]


   .. py:attribute:: classifier


   .. py:attribute:: completed_tasks
      :type:  dict[str, MemoryTask]


   .. py:attribute:: config


   .. py:attribute:: coordinator_llm


   .. py:attribute:: memory_store


   .. py:attribute:: meta_agents
      :type:  dict[str, haive.core.schema.prebuilt.meta_state.MetaStateSchema]


   .. py:attribute:: performance_metrics


   .. py:attribute:: task_queue
      :type:  list[MemoryTask]
      :value: []



.. py:data:: logger

