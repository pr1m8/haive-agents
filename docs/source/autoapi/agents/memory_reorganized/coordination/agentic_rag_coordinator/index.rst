agents.memory_reorganized.coordination.agentic_rag_coordinator
==============================================================

.. py:module:: agents.memory_reorganized.coordination.agentic_rag_coordinator

.. autoapi-nested-parse::

   Agentic RAG Coordinator for Memory System.

   This module provides an intelligent coordinator that selects and combines multiple
   retrieval strategies based on query analysis and context.


   .. autolink-examples:: agents.memory_reorganized.coordination.agentic_rag_coordinator
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory_reorganized.coordination.agentic_rag_coordinator.logger


Classes
-------

.. autoapisummary::

   agents.memory_reorganized.coordination.agentic_rag_coordinator.AgenticRAGCoordinator
   agents.memory_reorganized.coordination.agentic_rag_coordinator.AgenticRAGCoordinatorConfig
   agents.memory_reorganized.coordination.agentic_rag_coordinator.AgenticRAGResult
   agents.memory_reorganized.coordination.agentic_rag_coordinator.RetrievalStrategy


Module Contents
---------------

.. py:class:: AgenticRAGCoordinator(config: AgenticRAGCoordinatorConfig)

   Bases: :py:obj:`haive.agents.simple.agent.SimpleAgent`


   Intelligent coordinator that selects and combines retrieval strategies for optimal.
   memory retrieval.

   The AgenticRAGCoordinator is an advanced memory retrieval agent that analyzes incoming
   queries and dynamically selects the most appropriate retrieval strategies from a
   comprehensive set of available options. It combines results from multiple strategies
   to provide comprehensive, diverse, and relevant memory retrieval.

   Key Features:
       - Intelligent strategy selection based on query analysis
       - Multi-strategy parallel execution for comprehensive coverage
       - Advanced result fusion with diversity and coverage optimization
       - Performance monitoring and optimization
       - Adaptive strategy weighting based on query characteristics
       - Support for graph-based, semantic, temporal, and procedural retrieval

   .. attribute:: memory_store

      Memory store manager for basic memory operations

   .. attribute:: classifier

      Memory classifier for query analysis and intent detection

   .. attribute:: kg_generator

      Optional knowledge graph generator for graph-based retrieval

   .. attribute:: enhanced_retriever_config

      Configuration for enhanced vector retrieval

   .. attribute:: graph_rag_config

      Configuration for graph-enhanced RAG retrieval

   .. attribute:: max_strategies

      Maximum number of strategies to use per query

   .. attribute:: min_confidence_threshold

      Minimum confidence score required to use a strategy

   .. attribute:: enable_strategy_combination

      Whether to enable multi-strategy result fusion

   .. attribute:: fusion_method

      Method used for combining results from multiple strategies

   .. attribute:: diversity_weight

      Weight given to diversity in result ranking (0.0-1.0)

   .. attribute:: coverage_weight

      Weight given to coverage in result ranking (0.0-1.0)

   .. attribute:: relevance_weight

      Weight given to relevance in result ranking (0.0-1.0)

   .. attribute:: coordinator_llm

      LLM runnable for strategy selection and coordination

   .. attribute:: retrievers

      Dictionary of available retrieval components

   .. attribute:: strategies

      Dictionary of available retrieval strategies

   .. attribute:: strategy_selection_prompt

      Prompt template for strategy selection

   .. attribute:: result_fusion_prompt

      Prompt template for result fusion

   .. rubric:: Examples

   Basic coordinator usage::

       # Create coordinator
       coordinator = AgenticRAGCoordinator(config)

       # Retrieve memories with intelligent strategy selection
       result = await coordinator.retrieve_memories(
           "How do I deploy a web application with Docker?"
       )

       print(f"Retrieved {len(result.final_memories)} memories")
       print(f"Used strategies: {result.selected_strategies}")
       print(f"Processing time: {result.total_time_ms:.1f}ms")

       # Access retrieved memories
       for i, memory in enumerate(result.final_memories):
           score = result.final_scores[i]
           print(f"Memory {i+1}: {memory['content'][:100]}... (score: {score:.2f})")

   Advanced retrieval with filtering::

       # Retrieve with specific memory types and limits
       result = await coordinator.retrieve_memories(
           query="What are the best practices for API security?",
           limit=5,
           memory_types=[MemoryType.SEMANTIC, MemoryType.PROCEDURAL],
           namespace=("user", "security")
       )

       # Analyze strategy performance
       print(f"Strategy reasoning: {result.strategy_reasoning}")
       print(f"Quality scores: diversity={result.diversity_score:.2f}, "
             f"coverage={result.coverage_score:.2f}, confidence={result.confidence_score:.2f}")

   Performance analysis::

       result = await coordinator.retrieve_memories("complex technical query")

       # Analyze individual strategy performance
       for strategy_name, strategy_data in result.strategy_results.items():
           memory_count = len(strategy_data.get('memories', []))
           exec_time = strategy_data.get('execution_time_ms', 0)
           print(f"{strategy_name}: {memory_count} memories in {exec_time:.1f}ms")

   Forced strategy selection (for testing)::

       # Force specific strategies for testing or optimization
       result = await coordinator.retrieve_memories(
           query="test query",
           force_strategies=["enhanced_similarity", "graph_traversal"]
       )

       print(f"Forced strategies: {result.selected_strategies}")

   .. note::

      The coordinator automatically selects the best strategies based on query
      analysis, but can be configured with custom weights and thresholds for
      different use cases and performance requirements.

   Initialize the Agentic RAG Coordinator with comprehensive strategy setup.

   Sets up the coordinator with all necessary components including retrievers,
   strategies, and prompts for intelligent memory retrieval coordination.

   :param config: AgenticRAGCoordinatorConfig containing all coordinator settings

   .. rubric:: Examples

   Basic initialization::

       config = AgenticRAGCoordinatorConfig(
           name="my_coordinator",
           memory_store_manager=store_manager,
           memory_classifier=classifier,
           kg_generator=kg_generator
       )

       coordinator = AgenticRAGCoordinator(config)

   Advanced initialization with custom settings::

       config = AgenticRAGCoordinatorConfig(
           name="advanced_coordinator",
           memory_store_manager=store_manager,
           memory_classifier=classifier,
           kg_generator=kg_generator,
           enhanced_retriever_config=enhanced_config,
           graph_rag_config=graph_config,
           max_strategies=3,
           min_confidence_threshold=0.7,
           enable_strategy_combination=True,
           coordinator_llm=AugLLMConfig(model="gpt-4", temperature=0.2),
           fusion_method="weighted_rank",
           diversity_weight=0.25,
           coverage_weight=0.35,
           relevance_weight=0.4
       )

       coordinator = AgenticRAGCoordinator(config)

   .. note::

      The coordinator automatically sets up all available retrieval strategies
      based on the provided configuration. Optional components (like graph RAG)
      will only be available if their configurations are provided.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgenticRAGCoordinator
      :collapse:

   .. py:method:: _analyze_query(query: str) -> dict[str, Any]
      :async:


      Analyze query to understand intent and requirements.


      .. autolink-examples:: _analyze_query
         :collapse:


   .. py:method:: _define_strategies() -> dict[str, RetrievalStrategy]

      Define available retrieval strategies.


      .. autolink-examples:: _define_strategies
         :collapse:


   .. py:method:: _execute_enhanced_similarity(query: str, limit: int, memory_types: list[haive.agents.memory.core.types.MemoryType] | None, namespace: tuple[str, Ellipsis] | None, parameters: dict[str, Any]) -> list[dict[str, Any]]
      :async:


      Execute enhanced similarity strategy.


      .. autolink-examples:: _execute_enhanced_similarity
         :collapse:


   .. py:method:: _execute_error_feedback_search(query: str, limit: int, memory_types: list[haive.agents.memory.core.types.MemoryType] | None, namespace: tuple[str, Ellipsis] | None, parameters: dict[str, Any]) -> list[dict[str, Any]]
      :async:


      Execute error/feedback search strategy.


      .. autolink-examples:: _execute_error_feedback_search
         :collapse:


   .. py:method:: _execute_graph_traversal(query: str, limit: int, memory_types: list[haive.agents.memory.core.types.MemoryType] | None, namespace: tuple[str, Ellipsis] | None, parameters: dict[str, Any]) -> list[dict[str, Any]]
      :async:


      Execute graph traversal strategy.


      .. autolink-examples:: _execute_graph_traversal
         :collapse:


   .. py:method:: _execute_procedural_search(query: str, limit: int, memory_types: list[haive.agents.memory.core.types.MemoryType] | None, namespace: tuple[str, Ellipsis] | None, parameters: dict[str, Any]) -> list[dict[str, Any]]
      :async:


      Execute procedural search strategy.


      .. autolink-examples:: _execute_procedural_search
         :collapse:


   .. py:method:: _execute_single_strategy(strategy_name: str, query: str, limit: haive.agents.memory.graph_rag_retriever.Optional[int], memory_types: list[haive.agents.memory.core.types.MemoryType] | None, namespace: tuple[str, Ellipsis] | None) -> dict[str, Any]
      :async:


      Execute a single retrieval strategy.


      .. autolink-examples:: _execute_single_strategy
         :collapse:


   .. py:method:: _execute_strategies(strategies: list[str], query: str, limit: haive.agents.memory.graph_rag_retriever.Optional[int], memory_types: list[haive.agents.memory.core.types.MemoryType] | None, namespace: tuple[str, Ellipsis] | None) -> dict[str, Any]
      :async:


      Execute selected strategies in parallel.


      .. autolink-examples:: _execute_strategies
         :collapse:


   .. py:method:: _execute_temporal_search(query: str, limit: int, memory_types: list[haive.agents.memory.core.types.MemoryType] | None, namespace: tuple[str, Ellipsis] | None, parameters: dict[str, Any]) -> list[dict[str, Any]]
      :async:


      Execute temporal search strategy.


      .. autolink-examples:: _execute_temporal_search
         :collapse:


   .. py:method:: _fallback_strategy_selection(query_analysis: dict[str, Any], memory_types: list[haive.agents.memory.core.types.MemoryType] | None = None) -> tuple[list[str], str]

      Fallback strategy selection using rules.


      .. autolink-examples:: _fallback_strategy_selection
         :collapse:


   .. py:method:: _fuse_results(query: str, strategy_results: dict[str, Any], limit: int) -> tuple[list[dict[str, Any]], list[float], dict[str, Any]]
      :async:


      Fuse results from multiple strategies.


      .. autolink-examples:: _fuse_results
         :collapse:


   .. py:method:: _parse_json_response(response: str) -> dict[str, Any] | None

      Parse JSON response from LLM.


      .. autolink-examples:: _parse_json_response
         :collapse:


   .. py:method:: _select_strategies(query: str, query_analysis: dict[str, Any], memory_types: list[haive.agents.memory.core.types.MemoryType] | None = None) -> tuple[list[str], str]
      :async:


      Select appropriate strategies for the query.


      .. autolink-examples:: _select_strategies
         :collapse:


   .. py:method:: _setup_prompts() -> None

      Setup prompts for strategy selection and coordination.


      .. autolink-examples:: _setup_prompts
         :collapse:


   .. py:method:: _setup_retrievers() -> None

      Setup individual retrievers.


      .. autolink-examples:: _setup_retrievers
         :collapse:


   .. py:method:: retrieve_memories(query: str, limit: haive.agents.memory.graph_rag_retriever.Optional[int] = None, memory_types: list[haive.agents.memory.core.types.MemoryType] | None = None, namespace: tuple[str, Ellipsis] | None = None, force_strategies: list[str] | None = None) -> AgenticRAGResult
      :async:


      Retrieve memories using intelligent strategy coordination and result fusion.

      This method is the core of the agentic RAG coordinator. It analyzes the query,
      selects appropriate retrieval strategies, executes them in parallel, and fuses
      the results to provide comprehensive, diverse, and relevant memory retrieval.

      :param query: Natural language query for memory retrieval
      :param limit: Maximum number of memories to return (default: 10)
      :param memory_types: Specific memory types to focus on (optional filtering)
      :param namespace: Memory namespace to search within (optional scoping)
      :param force_strategies: Force specific strategies for testing or optimization

      :returns: Comprehensive result with memories, strategy info, and metrics
      :rtype: AgenticRAGResult

      .. rubric:: Examples

      Basic memory retrieval::

          result = await coordinator.retrieve_memories(
              "How do I deploy a web application?"
          )

          print(f"Retrieved {len(result.final_memories)} memories")
          print(f"Used strategies: {result.selected_strategies}")
          print(f"Processing time: {result.total_time_ms:.1f}ms")

          # Access retrieved memories
          for i, memory in enumerate(result.final_memories):
              score = result.final_scores[i]
              print(f"Memory {i+1}: {memory['content'][:100]}... (score: {score:.2f})")

      Advanced retrieval with filtering::

          result = await coordinator.retrieve_memories(
              query="What are machine learning best practices?",
              limit=5,
              memory_types=[MemoryType.SEMANTIC, MemoryType.PROCEDURAL],
              namespace=("user", "ml", "practices")
          )

          # Analyze strategy performance
          print(f"Strategy reasoning: {result.strategy_reasoning}")
          print(f"Quality scores:")
          print(f"  Diversity: {result.diversity_score:.2f}")
          print(f"  Coverage: {result.coverage_score:.2f}")
          print(f"  Confidence: {result.confidence_score:.2f}")

      Performance analysis::

          result = await coordinator.retrieve_memories("complex technical query")

          # Analyze individual strategy performance
          for strategy_name, strategy_data in result.strategy_results.items():
              memory_count = len(strategy_data.get('memories', []))
              exec_time = strategy_data.get('execution_time_ms', 0)
              print(f"{strategy_name}: {memory_count} memories in {exec_time:.1f}ms")

          # Overall performance metrics
          print(f"Total execution time: {result.total_time_ms:.1f}ms")
          print(f"Average memory score: {sum(result.final_scores) / len(result.final_scores):.2f}")

      Forced strategy selection (for testing)::

          result = await coordinator.retrieve_memories(
              query="test query",
              force_strategies=["enhanced_similarity", "graph_traversal"]
          )

          print(f"Forced strategies: {result.selected_strategies}")
          assert result.selected_strategies == ["enhanced_similarity", "graph_traversal"]

      .. note::

         The coordinator automatically analyzes the query to select the most appropriate
         strategies. It considers query complexity, memory types needed, temporal scope,
         and other factors to optimize retrieval performance and quality.


      .. autolink-examples:: retrieve_memories
         :collapse:


   .. py:method:: run(user_input: str) -> str
      :async:


      Main execution method for the Agentic RAG Coordinator with comprehensive.
      reporting.

      This method serves as the primary interface for the coordinator, accepting natural
      language queries and returning formatted results with detailed performance metrics
      and strategy information.

      :param user_input: Natural language query for memory retrieval

      :returns: Formatted response with retrieval results, strategy information, and performance metrics
      :rtype: str

      .. rubric:: Examples

      Basic query execution::

          coordinator = AgenticRAGCoordinator(config)

          response = await coordinator.run(
              "How do I deploy a Docker container to AWS?"
          )

          print(response)
          # Output:
          # Retrieved 8 memories using 2 strategies:
          # - Strategies: enhanced_similarity, procedural_search
          # - Total time: 1247.3ms
          # - Quality scores: Diversity=0.78, Coverage=0.85, Confidence=0.82
          # - Strategy reasoning: Selected enhanced similarity for factual content and procedural search for deployment steps
          #
          # Top memories:
          # 1. [0.91] Docker deployment to AWS ECS requires proper image tagging and service configuration...
          # 2. [0.87] AWS deployment best practices include using IAM roles, security groups, and monitoring...
          # 3. [0.84] Container orchestration with ECS involves task definitions, services, and load balancers...

      Complex query with multiple strategies::

          response = await coordinator.run(
              "What are the relationships between machine learning algorithms and their applications in healthcare?"
          )

          print(response)
          # Output shows graph traversal strategy was used for relationship discovery
          # along with enhanced similarity for semantic content

      Error handling::

          response = await coordinator.run("complex query that might fail")

          # Response will include error information if retrieval fails
          # but still provide a graceful user experience

      .. note::

         The response format includes:
         - Number of memories retrieved and strategies used
         - Processing time and quality scores
         - Strategy selection reasoning
         - Top 3 memories with relevance scores
         - Graceful error handling for failed retrievals


      .. autolink-examples:: run
         :collapse:


   .. py:attribute:: classifier
      :type:  haive.agents.memory.core.classifier.MemoryClassifier
      :value: None



   .. py:attribute:: coordinator_llm
      :type:  Any
      :value: None



   .. py:attribute:: coverage_weight
      :type:  float
      :value: None



   .. py:attribute:: diversity_weight
      :type:  float
      :value: None



   .. py:attribute:: enable_strategy_combination
      :type:  bool
      :value: None



   .. py:attribute:: enhanced_retriever_config
      :type:  haive.agents.memory.graph_rag_retriever.Optional[haive.agents.memory.enhanced_retriever.EnhancedRetrieverConfig]
      :value: None



   .. py:attribute:: fusion_method
      :type:  str
      :value: None



   .. py:attribute:: graph_rag_config
      :type:  haive.agents.memory.graph_rag_retriever.Optional[haive.agents.memory.graph_rag_retriever.GraphRAGRetrieverConfig]
      :value: None



   .. py:attribute:: kg_generator
      :type:  haive.agents.memory.graph_rag_retriever.Optional[haive.agents.memory.kg_generator_agent.KGGeneratorAgent]
      :value: None



   .. py:attribute:: max_strategies
      :type:  int
      :value: None



   .. py:attribute:: memory_store
      :type:  haive.agents.memory.core.stores.MemoryStoreManager
      :value: None



   .. py:attribute:: min_confidence_threshold
      :type:  float
      :value: None



   .. py:attribute:: relevance_weight
      :type:  float
      :value: None



   .. py:attribute:: result_fusion_prompt
      :type:  langchain_core.prompts.PromptTemplate
      :value: None



   .. py:attribute:: retrievers
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: strategies
      :type:  dict[str, RetrievalStrategy]
      :value: None



   .. py:attribute:: strategy_selection_prompt
      :type:  langchain_core.prompts.PromptTemplate
      :value: None



.. py:class:: AgenticRAGCoordinatorConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for Agentic RAG Coordinator with intelligent strategy selection.

   This configuration class defines all parameters needed to create and configure
   an AgenticRAGCoordinator, including core components, retrieval strategies,
   coordination settings, and result fusion parameters.

   .. attribute:: name

      Unique identifier for the coordinator instance

   .. attribute:: memory_store_manager

      Manager for memory storage and retrieval operations

   .. attribute:: memory_classifier

      Classifier for analyzing query intent and memory types

   .. attribute:: kg_generator

      Optional knowledge graph generator for graph-based retrieval

   .. attribute:: enhanced_retriever_config

      Configuration for enhanced vector retrieval

   .. attribute:: graph_rag_config

      Configuration for graph-enhanced RAG retrieval

   .. attribute:: max_strategies

      Maximum number of strategies to use per query

   .. attribute:: min_confidence_threshold

      Minimum confidence score required to use a strategy

   .. attribute:: enable_strategy_combination

      Whether to enable multi-strategy result fusion

   .. attribute:: coordinator_llm

      LLM configuration for strategy selection and coordination

   .. attribute:: fusion_method

      Method used for combining results from multiple strategies

   .. attribute:: diversity_weight

      Weight given to diversity in result ranking (0.0-1.0)

   .. attribute:: coverage_weight

      Weight given to coverage in result ranking (0.0-1.0)

   .. attribute:: relevance_weight

      Weight given to relevance in result ranking (0.0-1.0)

   .. rubric:: Examples

   Basic configuration::

       config = AgenticRAGCoordinatorConfig(
           name="my_rag_coordinator",
           memory_store_manager=store_manager,
           memory_classifier=classifier,
           kg_generator=kg_generator,
           max_strategies=2,
           min_confidence_threshold=0.6
       )

   Advanced configuration with custom retrieval components::

       config = AgenticRAGCoordinatorConfig(
           name="advanced_rag_coordinator",
           memory_store_manager=store_manager,
           memory_classifier=classifier,
           kg_generator=kg_generator,

           # Enhanced retrieval configuration
           enhanced_retriever_config=EnhancedRetrieverConfig(
               enable_query_expansion=True,
               importance_boost=0.2
           ),

           # Graph RAG configuration
           graph_rag_config=GraphRAGRetrieverConfig(
               enable_graph_traversal=True,
               max_graph_depth=3,
               min_confidence_threshold=0.6
           ),

           # Coordination settings
           max_strategies=3,
           min_confidence_threshold=0.5,
           enable_strategy_combination=True,

           # LLM configuration
           coordinator_llm=AugLLMConfig(
               model="gpt-4",
               temperature=0.2,
               max_tokens=1000
           ),

           # Result fusion weights
           fusion_method="weighted_rank",
           diversity_weight=0.25,
           coverage_weight=0.35,
           relevance_weight=0.4
       )

   Performance-optimized configuration::

       config = AgenticRAGCoordinatorConfig(
           name="fast_rag_coordinator",
           memory_store_manager=store_manager,
           memory_classifier=classifier,

           # Single strategy for speed
           max_strategies=1,
           min_confidence_threshold=0.7,
           enable_strategy_combination=False,

           # Fast LLM configuration
           coordinator_llm=AugLLMConfig(
               model="gpt-3.5-turbo",
               temperature=0.1,
               max_tokens=500
           ),

           # Relevance-focused fusion
           fusion_method="relevance_only",
           diversity_weight=0.0,
           coverage_weight=0.0,
           relevance_weight=1.0
       )

   .. note::

      The weights for diversity, coverage, and relevance should sum to 1.0
      for optimal result fusion. The coordinator will normalize them if needed.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgenticRAGCoordinatorConfig
      :collapse:

   .. py:attribute:: coordinator_llm
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: coverage_weight
      :type:  float
      :value: None



   .. py:attribute:: diversity_weight
      :type:  float
      :value: None



   .. py:attribute:: enable_strategy_combination
      :type:  bool
      :value: None



   .. py:attribute:: enhanced_retriever_config
      :type:  haive.agents.memory.graph_rag_retriever.Optional[haive.agents.memory.enhanced_retriever.EnhancedRetrieverConfig]
      :value: None



   .. py:attribute:: fusion_method
      :type:  str
      :value: None



   .. py:attribute:: graph_rag_config
      :type:  haive.agents.memory.graph_rag_retriever.Optional[haive.agents.memory.graph_rag_retriever.GraphRAGRetrieverConfig]
      :value: None



   .. py:attribute:: kg_generator
      :type:  haive.agents.memory.graph_rag_retriever.Optional[haive.agents.memory.kg_generator_agent.KGGeneratorAgent]
      :value: None



   .. py:attribute:: max_strategies
      :type:  int
      :value: None



   .. py:attribute:: memory_classifier
      :type:  haive.agents.memory.core.classifier.MemoryClassifier
      :value: None



   .. py:attribute:: memory_store_manager
      :type:  haive.agents.memory.core.stores.MemoryStoreManager
      :value: None



   .. py:attribute:: min_confidence_threshold
      :type:  float
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: relevance_weight
      :type:  float
      :value: None



.. py:class:: AgenticRAGResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Comprehensive result from agentic RAG coordinator with performance metrics and.
   analysis.

   This class encapsulates all information from an agentic RAG retrieval operation,
   including the retrieved memories, strategy details, performance metrics, and
   quality scores for analysis and optimization.

   .. attribute:: query

      Original user query that was processed

   .. attribute:: selected_strategies

      List of strategy names that were selected and executed

   .. attribute:: strategy_results

      Detailed results from each individual strategy

   .. attribute:: final_memories

      Final ranked and deduplicated memories after strategy fusion

   .. attribute:: final_scores

      Relevance scores for each memory in final_memories

   .. attribute:: total_time_ms

      Total processing time for the entire operation

   .. attribute:: strategy_times

      Execution time for each individual strategy

   .. attribute:: query_analysis

      Detailed analysis of the query (intent, complexity, etc.)

   .. attribute:: strategy_reasoning

      Explanation of why specific strategies were selected

   .. attribute:: diversity_score

      Measure of diversity in the retrieved memories (0.0-1.0)

   .. attribute:: coverage_score

      Measure of how well results cover query aspects (0.0-1.0)

   .. attribute:: confidence_score

      Overall confidence in the result quality (0.0-1.0)

   .. rubric:: Examples

   Accessing retrieval results::

       result = await coordinator.retrieve_memories("How do I deploy web apps?")

       print(f"Query: {result.query}")
       print(f"Strategies used: {result.selected_strategies}")
       print(f"Total memories: {len(result.final_memories)}")
       print(f"Processing time: {result.total_time_ms:.1f}ms")

       # Access individual memories
       for i, memory in enumerate(result.final_memories):
           score = result.final_scores[i] if i < len(result.final_scores) else 0.0
           print(f"Memory {i+1}: {memory['content'][:100]}... (score: {score:.2f})")

   Analyzing strategy performance::

       result = await coordinator.retrieve_memories("complex query")

       print(f"Strategy reasoning: {result.strategy_reasoning}")
       print(f"Quality scores:")
       print(f"  Diversity: {result.diversity_score:.2f}")
       print(f"  Coverage: {result.coverage_score:.2f}")
       print(f"  Confidence: {result.confidence_score:.2f}")

       # Strategy timing analysis
       for strategy, time_ms in result.strategy_times.items():
           print(f"  {strategy}: {time_ms:.1f}ms")

   Query analysis details::

       result = await coordinator.retrieve_memories("What did I learn about ML?")

       if result.query_analysis:
           analysis = result.query_analysis
           print(f"Memory types needed: {analysis.get('memory_types', [])}")
           print(f"Query complexity: {analysis.get('complexity', 'unknown')}")
           print(f"Requires reasoning: {analysis.get('requires_reasoning', False)}")
           print(f"Entities: {analysis.get('entities', [])}")
           print(f"Topics: {analysis.get('topics', [])}")

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgenticRAGResult
      :collapse:

   .. py:attribute:: confidence_score
      :type:  float
      :value: None



   .. py:attribute:: coverage_score
      :type:  float
      :value: None



   .. py:attribute:: diversity_score
      :type:  float
      :value: None



   .. py:attribute:: final_memories
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: final_scores
      :type:  list[float]
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



   .. py:attribute:: query_analysis
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: selected_strategies
      :type:  list[str]
      :value: None



   .. py:attribute:: strategy_reasoning
      :type:  str
      :value: None



   .. py:attribute:: strategy_results
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: strategy_times
      :type:  dict[str, float]
      :value: None



   .. py:attribute:: total_time_ms
      :type:  float
      :value: None



.. py:class:: RetrievalStrategy(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a retrieval strategy with its configuration and performance.
   characteristics.

   A retrieval strategy defines how to retrieve memories for specific types of queries,
   including the strategy's strengths, supported memory types, and performance parameters.

   .. attribute:: name

      Unique identifier for the strategy (e.g., "enhanced_similarity")

   .. attribute:: description

      Human-readable description of what the strategy does

   .. attribute:: best_for

      List of query types this strategy excels at handling

   .. attribute:: memory_types

      List of memory types this strategy is optimized for

   .. attribute:: confidence_threshold

      Minimum confidence score required to use this strategy

   .. attribute:: typical_latency_ms

      Expected response time in milliseconds for this strategy

   .. attribute:: max_results

      Maximum number of results this strategy can return

   .. attribute:: parameters

      Strategy-specific configuration parameters

   .. rubric:: Examples

   Creating an enhanced similarity strategy::

       strategy = RetrievalStrategy(
           name="enhanced_similarity",
           description="Multi-factor similarity search with memory type awareness",
           best_for=["factual_queries", "recent_events", "personal_information"],
           memory_types=[MemoryType.SEMANTIC, MemoryType.EPISODIC],
           confidence_threshold=0.6,
           typical_latency_ms=300,
           max_results=15,
           parameters={"enable_query_expansion": True, "importance_boost": 0.2}
       )

   Creating a graph traversal strategy::

       strategy = RetrievalStrategy(
           name="graph_traversal",
           description="Knowledge graph traversal for relationship discovery",
           best_for=["relationship_queries", "entity_connections"],
           memory_types=[MemoryType.CONTEXTUAL, MemoryType.SEMANTIC],
           confidence_threshold=0.7,
           typical_latency_ms=800,
           max_results=12,
           parameters={"max_depth": 3, "min_confidence": 0.6}
       )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RetrievalStrategy
      :collapse:

   .. py:attribute:: best_for
      :type:  list[str]
      :value: None



   .. py:attribute:: confidence_threshold
      :type:  float
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: max_results
      :type:  int
      :value: None



   .. py:attribute:: memory_types
      :type:  list[haive.agents.memory.core.types.MemoryType]
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: parameters
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: typical_latency_ms
      :type:  float
      :value: None



.. py:data:: logger

