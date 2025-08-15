agents.rag.self_route.agent
===========================

.. py:module:: agents.rag.self_route.agent

.. autoapi-nested-parse::

   Self-Route RAG Agents.

   from typing import Any
   Implementation of self-routing RAG with dynamic strategy selection and iterative planning.
   Uses structured output models for complex routing decisions and preprocessing.


   .. autolink-examples:: agents.rag.self_route.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.self_route.agent.ITERATIVE_PLANNING_PROMPT
   agents.rag.self_route.agent.QUERY_ANALYSIS_PROMPT
   agents.rag.self_route.agent.ROUTING_DECISION_PROMPT
   agents.rag.self_route.agent.logger


Classes
-------

.. autoapisummary::

   agents.rag.self_route.agent.IterativePlan
   agents.rag.self_route.agent.IterativePlannerAgent
   agents.rag.self_route.agent.QueryAnalysis
   agents.rag.self_route.agent.QueryAnalyzerAgent
   agents.rag.self_route.agent.QueryComplexity
   agents.rag.self_route.agent.RoutingDecision
   agents.rag.self_route.agent.RoutingDecisionAgent
   agents.rag.self_route.agent.RoutingStrategy
   agents.rag.self_route.agent.SelfRouteRAGAgent


Functions
---------

.. autoapisummary::

   agents.rag.self_route.agent.create_self_route_rag_agent
   agents.rag.self_route.agent.get_self_route_rag_io_schema


Module Contents
---------------

.. py:class:: IterativePlan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Iterative processing plan with loop structure.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: IterativePlan
      :collapse:

   .. py:attribute:: accumulated_context
      :type:  str
      :value: None



   .. py:attribute:: completion_reason
      :type:  str | None
      :value: None



   .. py:attribute:: convergence_criteria
      :type:  str
      :value: None



   .. py:attribute:: current_iteration
      :type:  int
      :value: None



   .. py:attribute:: iteration_goals
      :type:  dict[str, str]
      :value: None



   .. py:attribute:: iteration_results
      :type:  dict[str, str]
      :value: None



   .. py:attribute:: iteration_strategies
      :type:  dict[str, RoutingStrategy]
      :value: None



   .. py:attribute:: quality_threshold
      :type:  float
      :value: None



   .. py:attribute:: should_continue
      :type:  bool
      :value: None



   .. py:attribute:: total_iterations
      :type:  int
      :value: None



.. py:class:: IterativePlannerAgent(llm_config: haive.core.models.llm.base.LLMConfig | None = None, max_iterations: int = 3, **kwargs)

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Agent that creates iterative processing plans.

   Initialize iterative planner.

   :param llm_config: LLM configuration
   :param max_iterations: Maximum number of iterations
   :param \*\*kwargs: Additional agent arguments


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: IterativePlannerAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build iterative planning graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: llm_config


   .. py:attribute:: max_iterations
      :value: 3



   .. py:attribute:: name
      :type:  str
      :value: 'Iterative Planner'



.. py:class:: QueryAnalysis(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured analysis of query for routing decisions.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QueryAnalysis
      :collapse:

   .. py:attribute:: complexity_level
      :type:  QueryComplexity
      :value: None



   .. py:attribute:: complexity_score
      :type:  float
      :value: None



   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: domain_topics
      :type:  list[str]
      :value: None



   .. py:attribute:: fallback_strategies
      :type:  list[RoutingStrategy]
      :value: None



   .. py:attribute:: named_entities
      :type:  list[str]
      :value: None



   .. py:attribute:: needs_context_enrichment
      :type:  bool
      :value: None



   .. py:attribute:: needs_decomposition
      :type:  bool
      :value: None



   .. py:attribute:: needs_expansion
      :type:  bool
      :value: None



   .. py:attribute:: original_query
      :type:  str
      :value: None



   .. py:attribute:: primary_strategy
      :type:  RoutingStrategy
      :value: None



   .. py:attribute:: query_intent
      :type:  str
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: requires_domain_expertise
      :type:  bool
      :value: None



   .. py:attribute:: requires_factual_accuracy
      :type:  bool
      :value: None



   .. py:attribute:: requires_multiple_perspectives
      :type:  bool
      :value: None



   .. py:attribute:: requires_reasoning
      :type:  bool
      :value: None



   .. py:attribute:: requires_recent_information
      :type:  bool
      :value: None



.. py:class:: QueryAnalyzerAgent(llm_config: haive.core.models.llm.base.LLMConfig | None = None, analysis_depth: str = 'comprehensive', **kwargs)

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Agent that performs structured query analysis for routing.

   Initialize query analyzer.

   :param llm_config: LLM configuration
   :param analysis_depth: Depth of analysis ("basic", "comprehensive", "expert")
   :param \*\*kwargs: Additional agent arguments


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QueryAnalyzerAgent
      :collapse:

   .. py:method:: _extract_domain_info(query: str) -> str

      Extract domain information from query.


      .. autolink-examples:: _extract_domain_info
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build query analysis graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: analysis_depth
      :value: 'comprehensive'



   .. py:attribute:: llm_config


   .. py:attribute:: name
      :type:  str
      :value: 'Query Analyzer'



.. py:class:: QueryComplexity

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Query complexity levels for routing decisions.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QueryComplexity
      :collapse:

   .. py:attribute:: COMPLEX
      :value: 'complex'



   .. py:attribute:: EXPERT
      :value: 'expert'



   .. py:attribute:: MODERATE
      :value: 'moderate'



   .. py:attribute:: SIMPLE
      :value: 'simple'



.. py:class:: RoutingDecision(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Final routing decision with execution plan.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RoutingDecision
      :collapse:

   .. py:attribute:: estimated_latency
      :type:  str
      :value: None



   .. py:attribute:: execution_plan
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: expected_quality
      :type:  float
      :value: None



   .. py:attribute:: fallback_enabled
      :type:  bool
      :value: None



   .. py:attribute:: fallback_trigger
      :type:  str | None
      :value: None



   .. py:attribute:: mitigation_strategies
      :type:  list[str]
      :value: None



   .. py:attribute:: resource_requirements
      :type:  str
      :value: None



   .. py:attribute:: risk_factors
      :type:  list[str]
      :value: None



   .. py:attribute:: selected_strategy
      :type:  RoutingStrategy
      :value: None



.. py:class:: RoutingDecisionAgent(llm_config: haive.core.models.llm.base.LLMConfig | None = None, enable_fallback: bool = True, **kwargs)

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Agent that makes final routing decisions.

   Initialize routing decision agent.

   :param llm_config: LLM configuration
   :param enable_fallback: Whether to enable fallback strategies
   :param \*\*kwargs: Additional agent arguments


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RoutingDecisionAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build routing decision graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: enable_fallback
      :value: True



   .. py:attribute:: llm_config


   .. py:attribute:: name
      :type:  str
      :value: 'Routing Decision Engine'



.. py:class:: RoutingStrategy

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Available routing strategies.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RoutingStrategy
      :collapse:

   .. py:attribute:: ADAPTIVE_RAG
      :value: 'adaptive_rag'



   .. py:attribute:: CORRECTIVE_RAG
      :value: 'corrective_rag'



   .. py:attribute:: FUSION_RAG
      :value: 'fusion_rag'



   .. py:attribute:: HYDE_RAG
      :value: 'hyde_rag'



   .. py:attribute:: MULTI_QUERY_RAG
      :value: 'multi_query_rag'



   .. py:attribute:: SEARCH_ENHANCED_RAG
      :value: 'search_enhanced_rag'



   .. py:attribute:: SIMPLE_RAG
      :value: 'simple_rag'



   .. py:attribute:: STEP_BACK_RAG
      :value: 'step_back_rag'



.. py:class:: SelfRouteRAGAgent

   Bases: :py:obj:`haive.agents.multi.base.SequentialAgent`


   Complete Self-Route RAG agent with structured analysis and iterative planning.


   .. autolink-examples:: SelfRouteRAGAgent
      :collapse:

   .. py:method:: from_documents(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, analysis_depth: str = 'comprehensive', max_iterations: int = 3, enable_fallback: bool = True, **kwargs)
      :classmethod:


      Create Self-Route RAG agent from documents.

      :param documents: Documents to index
      :param llm_config: LLM configuration
      :param analysis_depth: Depth of query analysis
      :param max_iterations: Maximum iterations for planning
      :param enable_fallback: Whether to enable fallback routing
      :param \*\*kwargs: Additional arguments

      :returns: SelfRouteRAGAgent instance


      .. autolink-examples:: from_documents
         :collapse:


.. py:function:: create_self_route_rag_agent(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, routing_mode: str = 'adaptive', **kwargs) -> SelfRouteRAGAgent

   Create a Self-Route RAG agent.

   :param documents: Documents for retrieval
   :param llm_config: LLM configuration
   :param routing_mode: Routing mode ("conservative", "adaptive", "aggressive")
   :param \*\*kwargs: Additional arguments

   :returns: Configured Self-Route RAG agent


   .. autolink-examples:: create_self_route_rag_agent
      :collapse:

.. py:function:: get_self_route_rag_io_schema() -> dict[str, list[str]]

   Get I/O schema for Self-Route RAG agents.


   .. autolink-examples:: get_self_route_rag_io_schema
      :collapse:

.. py:data:: ITERATIVE_PLANNING_PROMPT

.. py:data:: QUERY_ANALYSIS_PROMPT

.. py:data:: ROUTING_DECISION_PROMPT

.. py:data:: logger

