agents.discovery.semantic_discovery
===================================

.. py:module:: agents.discovery.semantic_discovery

.. autoapi-nested-parse::

   Semantic Discovery Engine with Vector-Based Tool Selection.

   This module implements semantic discovery capabilities inspired by LangGraph's
   many-tools pattern, using vector embeddings to match tools and components
   based on query content and semantic similarity.

   Key Features:
   - Vector-based tool discovery and ranking
   - Semantic capability matching
   - Query analysis and tool recommendation
   - Dynamic tool binding and selection
   - Context-aware component matching


   .. autolink-examples:: agents.discovery.semantic_discovery
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.discovery.semantic_discovery.AdaptiveSelectionStrategy
   agents.discovery.semantic_discovery.BaseSelectionStrategy
   agents.discovery.semantic_discovery.CapabilityBasedStrategy
   agents.discovery.semantic_discovery.ContextualSelectionStrategy
   agents.discovery.semantic_discovery.EnhancedComponentRegistry
   agents.discovery.semantic_discovery.EnsembleSelectionStrategy
   agents.discovery.semantic_discovery.SemanticSelectionStrategy
   agents.discovery.semantic_discovery.UnifiedHaiveDiscovery
   agents.discovery.semantic_discovery.logger


Classes
-------

.. autoapisummary::

   agents.discovery.semantic_discovery.CapabilityMatcher
   agents.discovery.semantic_discovery.DiscoveryMode
   agents.discovery.semantic_discovery.QueryAnalysis
   agents.discovery.semantic_discovery.QueryAnalyzer
   agents.discovery.semantic_discovery.SemanticDiscoveryEngine
   agents.discovery.semantic_discovery.ToolSelectionStrategy
   agents.discovery.semantic_discovery.VectorBasedToolSelector


Functions
---------

.. autoapisummary::

   agents.discovery.semantic_discovery._lazy_import_strategies
   agents.discovery.semantic_discovery.create_component_registry
   agents.discovery.semantic_discovery.create_semantic_discovery


Module Contents
---------------

.. py:class:: CapabilityMatcher(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Matches tools based on required capabilities.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CapabilityMatcher
      :collapse:

   .. py:method:: _infer_capabilities(tool: Any) -> list[str]

      Infer capabilities from tool attributes.


      .. autolink-examples:: _infer_capabilities
         :collapse:


   .. py:method:: build_capability_matrix(tools: list[Any]) -> None

      Build capability matrix from tools.


      .. autolink-examples:: build_capability_matrix
         :collapse:


   .. py:method:: match_tools(required_capabilities: list[str], optional_capabilities: list[str] | None = None) -> list[tuple[str, float]]

      Match tools based on capabilities.


      .. autolink-examples:: match_tools
         :collapse:


   .. py:attribute:: capability_matrix
      :type:  dict[str, list[str]]
      :value: None



   .. py:attribute:: component_registry
      :type:  EnhancedComponentRegistry | None
      :value: None



.. py:class:: DiscoveryMode

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Different modes for semantic discovery.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DiscoveryMode
      :collapse:

   .. py:attribute:: CAPABILITY
      :value: 'capability'



   .. py:attribute:: CONTEXTUAL
      :value: 'contextual'



   .. py:attribute:: HYBRID
      :value: 'hybrid'



   .. py:attribute:: MEMORY_ENHANCED
      :value: 'memory_enhanced'



   .. py:attribute:: SIMILARITY
      :value: 'similarity'



.. py:class:: QueryAnalysis

   Analysis of user query for tool selection.


   .. autolink-examples:: QueryAnalysis
      :collapse:

   .. py:attribute:: complexity_score
      :type:  float


   .. py:attribute:: domain_tags
      :type:  list[str]


   .. py:attribute:: extracted_keywords
      :type:  list[str]


   .. py:attribute:: inferred_capabilities
      :type:  list[str]


   .. py:attribute:: intent_classification
      :type:  str


   .. py:attribute:: original_query
      :type:  str


   .. py:attribute:: suggested_tools
      :type:  list[str]
      :value: []



.. py:class:: QueryAnalyzer(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Analyzes queries to extract relevant information for tool selection.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QueryAnalyzer
      :collapse:

   .. py:method:: _calculate_complexity(query: str) -> float

      Calculate query complexity score.


      .. autolink-examples:: _calculate_complexity
         :collapse:


   .. py:method:: _classify_intent(query: str, capabilities: list[str]) -> str

      Classify the primary intent of the query.


      .. autolink-examples:: _classify_intent
         :collapse:


   .. py:method:: _extract_domain_tags(query: str) -> list[str]

      Extract domain-specific tags from query.


      .. autolink-examples:: _extract_domain_tags
         :collapse:


   .. py:method:: analyze_query(query: str) -> QueryAnalysis

      Analyze query to extract useful information.


      .. autolink-examples:: analyze_query
         :collapse:


   .. py:attribute:: capability_keywords
      :type:  dict[str, list[str]]
      :value: None



.. py:class:: SemanticDiscoveryEngine(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Main semantic discovery engine combining all capabilities.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SemanticDiscoveryEngine
      :collapse:

   .. py:method:: discover_tools(tools: list[Any] | None = None, haive_root: str | None = None) -> list[haive.core.registry.ComponentMetadata]
      :async:


      Discover available tools.


      .. autolink-examples:: discover_tools
         :collapse:


   .. py:method:: get_tools_for_capabilities(required_capabilities: list[str], optional_capabilities: list[str] | None = None, max_tools: int = 5) -> list[haive.core.registry.ComponentMetadata]
      :async:


      Get tools that match specific capabilities.


      .. autolink-examples:: get_tools_for_capabilities
         :collapse:


   .. py:method:: semantic_tool_selection(query: str, max_tools: int = 5, strategy: ToolSelectionStrategy = ToolSelectionStrategy.HYBRID, capability_filter: list[str] | None = None) -> tuple[list[haive.core.registry.ComponentMetadata], QueryAnalysis]
      :async:


      Perform semantic tool selection for a query.


      .. autolink-examples:: semantic_tool_selection
         :collapse:


   .. py:method:: setup_registry() -> SemanticDiscoveryEngine

      Setup shared component registry.


      .. autolink-examples:: setup_registry
         :collapse:


   .. py:method:: update_selection_strategy(strategy: haive.agents.discovery.selection_strategies.BaseSelectionStrategy | str) -> None

      Update the selection strategy.


      .. autolink-examples:: update_selection_strategy
         :collapse:


   .. py:attribute:: capability_matcher
      :type:  CapabilityMatcher
      :value: None



   .. py:attribute:: component_registry
      :type:  EnhancedComponentRegistry | None
      :value: None



   .. py:attribute:: query_analyzer
      :type:  QueryAnalyzer
      :value: None



   .. py:attribute:: selection_strategy
      :type:  _lazy_import_strategies.BaseSelectionStrategy
      :value: None



   .. py:attribute:: vector_selector
      :type:  VectorBasedToolSelector
      :value: None



.. py:class:: ToolSelectionStrategy

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Strategies for tool selection.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ToolSelectionStrategy
      :collapse:

   .. py:attribute:: ADAPTIVE
      :value: 'adaptive'



   .. py:attribute:: CONTEXTUAL
      :value: 'contextual'



   .. py:attribute:: HYBRID
      :value: 'hybrid'



   .. py:attribute:: THRESHOLD
      :value: 'threshold'



   .. py:attribute:: TOP_K
      :value: 'top_k'



.. py:class:: VectorBasedToolSelector(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Selects tools using vector similarity search.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: VectorBasedToolSelector
      :collapse:

   .. py:method:: _select_by_threshold(query: str) -> list[haive.core.registry.ComponentMetadata]
      :async:


      Select tools above similarity threshold.


      .. autolink-examples:: _select_by_threshold
         :collapse:


   .. py:method:: _select_hybrid(query: str) -> list[haive.core.registry.ComponentMetadata]
      :async:


      Hybrid selection combining similarity and capability matching.


      .. autolink-examples:: _select_hybrid
         :collapse:


   .. py:method:: _select_top_k(query: str) -> list[haive.core.registry.ComponentMetadata]
      :async:


      Select top K most similar tools.


      .. autolink-examples:: _select_top_k
         :collapse:


   .. py:method:: index_tools(tools: list[Any]) -> None

      Index tools in vector store and component registry.


      .. autolink-examples:: index_tools
         :collapse:


   .. py:method:: select_tools(query: str, strategy: ToolSelectionStrategy = ToolSelectionStrategy.TOP_K) -> list[haive.core.registry.ComponentMetadata]
      :async:


      Select tools based on query using specified strategy.


      .. autolink-examples:: select_tools
         :collapse:


   .. py:method:: setup_vector_store() -> VectorBasedToolSelector

      Setup vector store if not provided.


      .. autolink-examples:: setup_vector_store
         :collapse:


   .. py:attribute:: component_registry
      :type:  EnhancedComponentRegistry | None
      :value: None



   .. py:attribute:: max_tools
      :type:  int
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: similarity_threshold
      :type:  float
      :value: None



   .. py:attribute:: vector_store_config
      :type:  haive.core.engine.vectorstore.vectorstore.VectorStoreConfig | None
      :value: None



.. py:function:: _lazy_import_strategies()

   Lazy import to avoid circular imports.


   .. autolink-examples:: _lazy_import_strategies
      :collapse:

.. py:function:: create_component_registry(**kwargs)

.. py:function:: create_semantic_discovery() -> SemanticDiscoveryEngine

   Create a semantic discovery engine with default configuration.


   .. autolink-examples:: create_semantic_discovery
      :collapse:

.. py:data:: AdaptiveSelectionStrategy
   :value: None


.. py:data:: BaseSelectionStrategy
   :value: None


.. py:data:: CapabilityBasedStrategy
   :value: None


.. py:data:: ContextualSelectionStrategy
   :value: None


.. py:data:: EnhancedComponentRegistry

.. py:data:: EnsembleSelectionStrategy
   :value: None


.. py:data:: SemanticSelectionStrategy
   :value: None


.. py:data:: UnifiedHaiveDiscovery

.. py:data:: logger

