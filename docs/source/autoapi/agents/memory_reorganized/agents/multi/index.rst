agents.memory_reorganized.agents.multi
======================================

.. py:module:: agents.memory_reorganized.agents.multi

.. autoapi-nested-parse::

   MultiMemoryAgent - Coordinates different memory strategies.

   This agent acts as a meta-coordinator that routes queries to different specialized
   memory agents based on query type, context, and memory strategy optimization.


   .. autolink-examples:: agents.memory_reorganized.agents.multi
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory_reorganized.agents.multi.GraphMemoryAgent
   agents.memory_reorganized.agents.multi.GraphMemoryConfig
   agents.memory_reorganized.agents.multi.HAS_GRAPH_MEMORY
   agents.memory_reorganized.agents.multi.HAS_RAG_MEMORY
   agents.memory_reorganized.agents.multi.logger


Classes
-------

.. autoapisummary::

   agents.memory_reorganized.agents.multi.MemoryPriority
   agents.memory_reorganized.agents.multi.MemoryRoutingRule
   agents.memory_reorganized.agents.multi.MemoryStrategy
   agents.memory_reorganized.agents.multi.MultiMemoryAgent
   agents.memory_reorganized.agents.multi.MultiMemoryConfig
   agents.memory_reorganized.agents.multi.MultiMemoryState
   agents.memory_reorganized.agents.multi.QueryClassifier
   agents.memory_reorganized.agents.multi.QueryType
   agents.memory_reorganized.agents.multi.ResponseSynthesizer


Functions
---------

.. autoapisummary::

   agents.memory_reorganized.agents.multi.create_multi_memory_agent


Module Contents
---------------

.. py:class:: MemoryPriority

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Priority levels for memory processing.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryPriority
      :collapse:

   .. py:attribute:: BATCH
      :value: 'batch'



   .. py:attribute:: HIGH
      :value: 'high'



   .. py:attribute:: IMMEDIATE
      :value: 'immediate'



   .. py:attribute:: LOW
      :value: 'low'



   .. py:attribute:: NORMAL
      :value: 'normal'



.. py:class:: MemoryRoutingRule

   Rule for routing queries to specific memory strategies.


   .. autolink-examples:: MemoryRoutingRule
      :collapse:

   .. py:attribute:: conditions
      :type:  dict[str, Any]


   .. py:attribute:: confidence_threshold
      :type:  float
      :value: 0.7



   .. py:attribute:: fallback_strategy
      :type:  MemoryStrategy | None
      :value: None



   .. py:attribute:: query_type
      :type:  QueryType


   .. py:attribute:: strategy
      :type:  MemoryStrategy


.. py:class:: MemoryStrategy

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of memory strategies available.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryStrategy
      :collapse:

   .. py:attribute:: ADAPTIVE
      :value: 'adaptive'



   .. py:attribute:: GRAPH
      :value: 'graph'



   .. py:attribute:: HYBRID
      :value: 'hybrid'



   .. py:attribute:: RAG
      :value: 'rag'



   .. py:attribute:: SIMPLE
      :value: 'simple'



.. py:class:: MultiMemoryAgent(config: MultiMemoryConfig)

   Bases: :py:obj:`haive.agents.simple.agent.SimpleAgent`


   Agent that coordinates multiple memory strategies.

   This agent acts as a smart router and coordinator for different memory approaches,
   automatically selecting the best strategy based on query analysis and combining
   responses when appropriate.


   .. autolink-examples:: MultiMemoryAgent
      :collapse:

   .. py:method:: _adaptive_strategy_selection(query: str, context: dict[str, Any] | None = None) -> dict[str, Any]
      :async:


      Use AI to adaptively select the best memory strategy.


      .. autolink-examples:: _adaptive_strategy_selection
         :collapse:


   .. py:method:: _check_rule_conditions(rule: MemoryRoutingRule, context: dict[str, Any] | None) -> bool

      Check if additional rule conditions are met.


      .. autolink-examples:: _check_rule_conditions
         :collapse:


   .. py:method:: _init_memory_agents()

      Initialize the specialized memory agents.


      .. autolink-examples:: _init_memory_agents
         :collapse:


   .. py:method:: _init_query_classifier()

      Initialize the query classification system.


      .. autolink-examples:: _init_query_classifier
         :collapse:


   .. py:method:: _init_response_synthesizer()

      Initialize the response synthesis system.


      .. autolink-examples:: _init_response_synthesizer
         :collapse:


   .. py:method:: _prepare_input(input_data: Any) -> dict[str, Any]
      :async:


      Prepare input with multi-memory coordination.


      .. autolink-examples:: _prepare_input
         :collapse:


   .. py:method:: _update_query_stats(strategy: MemoryStrategy, start_time: datetime.datetime)

      Update query processing statistics.


      .. autolink-examples:: _update_query_stats
         :collapse:


   .. py:method:: classify_query(query: str) -> dict[str, Any]
      :async:


      Classify the query to determine appropriate memory strategy.


      .. autolink-examples:: classify_query
         :collapse:


   .. py:method:: execute_strategy(strategy: MemoryStrategy, query: str, context: dict[str, Any] | None = None) -> dict[str, Any]
      :async:


      Execute the selected memory strategy.


      .. autolink-examples:: execute_strategy
         :collapse:


   .. py:method:: get_comprehensive_status() -> dict[str, Any]

      Get comprehensive status of the MultiMemoryAgent.


      .. autolink-examples:: get_comprehensive_status
         :collapse:


   .. py:method:: get_coordination_stats() -> dict[str, Any]

      Get statistics about query coordination and routing.


      .. autolink-examples:: get_coordination_stats
         :collapse:


   .. py:method:: query_memory_agent(agent_key: str, query: str, context: dict[str, Any] | None = None) -> dict[str, Any]
      :async:


      Query a specific memory agent.


      .. autolink-examples:: query_memory_agent
         :collapse:


   .. py:method:: route_query(query_type: QueryType, confidence: float, context: dict[str, Any] | None = None) -> dict[str, Any]

      Route query to appropriate memory strategy based on classification.


      .. autolink-examples:: route_query
         :collapse:


   .. py:method:: synthesize_responses(responses: list[dict[str, Any]], query: str) -> dict[str, Any]
      :async:


      Synthesize multiple memory responses into a coherent answer.


      .. autolink-examples:: synthesize_responses
         :collapse:


   .. py:attribute:: _query_stats


   .. py:attribute:: multi_config


.. py:class:: MultiMemoryConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for MultiMemoryAgent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MultiMemoryConfig
      :collapse:

   .. py:attribute:: confidence_weighted_synthesis
      :type:  bool
      :value: None



   .. py:attribute:: default_strategy
      :type:  MemoryStrategy
      :value: None



   .. py:attribute:: enable_cross_memory_validation
      :type:  bool
      :value: None



   .. py:attribute:: enable_graph_memory
      :type:  bool
      :value: None



   .. py:attribute:: enable_parallel_querying
      :type:  bool
      :value: None



   .. py:attribute:: enable_rag_memory
      :type:  bool
      :value: None



   .. py:attribute:: enable_response_synthesis
      :type:  bool
      :value: None



   .. py:attribute:: enable_simple_memory
      :type:  bool
      :value: None



   .. py:attribute:: graph_memory_config
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: llm_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: max_concurrent_queries
      :type:  int
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: query_classification_confidence
      :type:  float
      :value: None



   .. py:attribute:: rag_memory_config
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: response_timeout_seconds
      :type:  int
      :value: None



   .. py:attribute:: routing_rules
      :type:  list[MemoryRoutingRule]
      :value: None



   .. py:attribute:: simple_memory_config
      :type:  haive.agents.memory_reorganized.agents.simple.TokenAwareMemoryConfig | None
      :value: None



.. py:class:: MultiMemoryState

   Bases: :py:obj:`haive.agents.memory_reorganized.base.token_state.MemoryStateWithTokens`


   Extended state for MultiMemoryAgent with routing information.


   .. autolink-examples:: MultiMemoryState
      :collapse:

   .. py:attribute:: classification_reasoning
      :type:  str
      :value: None



   .. py:attribute:: detected_query_type
      :type:  QueryType
      :value: None



   .. py:attribute:: fallback_used
      :type:  bool
      :value: None



   .. py:attribute:: memory_latencies
      :type:  dict[str, float]
      :value: None



   .. py:attribute:: memory_responses
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: query_confidence
      :type:  float
      :value: None



   .. py:attribute:: query_processing_time
      :type:  float
      :value: None



   .. py:attribute:: response_synthesis
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: routing_decision
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: selected_strategy
      :type:  MemoryStrategy
      :value: None



   .. py:attribute:: total_coordination_time
      :type:  float
      :value: None



.. py:class:: QueryClassifier(llm_config: haive.core.engine.aug_llm.AugLLMConfig)

   Classifies queries to determine appropriate memory strategy.


   .. autolink-examples:: QueryClassifier
      :collapse:

   .. py:method:: classify(query: str) -> dict[str, Any]
      :async:


      Classify a query to determine its type and characteristics.


      .. autolink-examples:: classify
         :collapse:


   .. py:attribute:: engine


   .. py:attribute:: llm_config


.. py:class:: QueryType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of queries that determine memory routing.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QueryType
      :collapse:

   .. py:attribute:: CONVERSATIONAL
      :value: 'conversational'



   .. py:attribute:: FACTUAL
      :value: 'factual'



   .. py:attribute:: MEMORY_RETRIEVAL
      :value: 'memory_retrieval'



   .. py:attribute:: MIXED
      :value: 'mixed'



   .. py:attribute:: PREFERENCE
      :value: 'preference'



   .. py:attribute:: RELATIONSHIP
      :value: 'relationship'



   .. py:attribute:: TEMPORAL
      :value: 'temporal'



.. py:class:: ResponseSynthesizer(llm_config: haive.core.engine.aug_llm.AugLLMConfig)

   Synthesizes responses from multiple memory agents.


   .. autolink-examples:: ResponseSynthesizer
      :collapse:

   .. py:method:: synthesize(responses: list[dict[str, Any]], original_query: str) -> dict[str, Any]
      :async:


      Synthesize multiple memory responses into a coherent answer.


      .. autolink-examples:: synthesize
         :collapse:


   .. py:attribute:: engine


   .. py:attribute:: llm_config


.. py:function:: create_multi_memory_agent(name: str = 'multi_memory_coordinator', enable_graph: bool = HAS_GRAPH_MEMORY, enable_rag: bool = HAS_RAG_MEMORY, **kwargs) -> MultiMemoryAgent

   Factory function to create a MultiMemoryAgent with sensible defaults.


   .. autolink-examples:: create_multi_memory_agent
      :collapse:

.. py:data:: GraphMemoryAgent
   :value: None


.. py:data:: GraphMemoryConfig
   :value: None


.. py:data:: HAS_GRAPH_MEMORY
   :value: False


.. py:data:: HAS_RAG_MEMORY
   :value: True


.. py:data:: logger

