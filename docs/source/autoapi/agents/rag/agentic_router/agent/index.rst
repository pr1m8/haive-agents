agents.rag.agentic_router.agent
===============================

.. py:module:: agents.rag.agentic_router.agent

.. autoapi-nested-parse::

   Agentic RAG Router with ReAct Pattern Agents.

   from typing import Any
   Implementation of autonomous RAG routing using ReAct (Reason + Act) patterns.
   Provides intelligent agent selection, strategy planning, and execution coordination.


   .. autolink-examples:: agents.rag.agentic_router.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.agentic_router.agent.AGENTIC_SYNTHESIS_PROMPT
   agents.rag.agentic_router.agent.REACT_PLANNING_PROMPT
   agents.rag.agentic_router.agent.STRATEGY_EXECUTION_PROMPT
   agents.rag.agentic_router.agent.logger


Classes
-------

.. autoapisummary::

   agents.rag.agentic_router.agent.AgenticRAGRouterAgent
   agents.rag.agentic_router.agent.AgenticRouterResult
   agents.rag.agentic_router.agent.ExecutionResult
   agents.rag.agentic_router.agent.RAGStrategy
   agents.rag.agentic_router.agent.ReActPlan
   agents.rag.agentic_router.agent.ReasoningStep


Functions
---------

.. autoapisummary::

   agents.rag.agentic_router.agent.create_agentic_rag_router_agent
   agents.rag.agentic_router.agent.get_agentic_rag_router_io_schema


Module Contents
---------------

.. py:class:: AgenticRAGRouterAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Complete Agentic RAG Router with ReAct patterns and autonomous decision-making.

   This agent uses conditional edges to route between different RAG strategies based on
   query analysis and planning.


   .. autolink-examples:: AgenticRAGRouterAgent
      :collapse:

   .. py:method:: _process_strategy_result(state: haive.core.schema.prebuilt.rag_state.RAGState, result: dict[str, Any], strategy: RAGStrategy) -> dict[str, Any]

      Process the result from a strategy execution.


      .. autolink-examples:: _process_strategy_result
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the agentic RAG router graph with conditional edges.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: execute_flare_strategy(state: haive.core.schema.prebuilt.rag_state.RAGState) -> dict[str, Any]

      Execute FLARE RAG strategy.


      .. autolink-examples:: execute_flare_strategy
         :collapse:


   .. py:method:: execute_fusion_strategy(state: haive.core.schema.prebuilt.rag_state.RAGState) -> dict[str, Any]

      Execute fusion RAG strategy.


      .. autolink-examples:: execute_fusion_strategy
         :collapse:


   .. py:method:: execute_hyde_strategy(state: haive.core.schema.prebuilt.rag_state.RAGState) -> dict[str, Any]

      Execute HyDE RAG strategy.


      .. autolink-examples:: execute_hyde_strategy
         :collapse:


   .. py:method:: execute_multi_query_strategy(state: haive.core.schema.prebuilt.rag_state.RAGState) -> dict[str, Any]

      Execute multi-query RAG strategy.


      .. autolink-examples:: execute_multi_query_strategy
         :collapse:


   .. py:method:: execute_simple_strategy(state: haive.core.schema.prebuilt.rag_state.RAGState) -> dict[str, Any]

      Execute simple RAG strategy.


      .. autolink-examples:: execute_simple_strategy
         :collapse:


   .. py:method:: from_documents(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, autonomy_level: str = 'high', **kwargs)
      :classmethod:


      Create Agentic RAG Router from documents.

      :param documents: Documents to index for RAG strategies
      :param llm_config: LLM configuration
      :param autonomy_level: Autonomy level ("low", "medium", "high")
      :param \*\*kwargs: Additional arguments

      :returns: AgenticRAGRouterAgent instance


      .. autolink-examples:: from_documents
         :collapse:


   .. py:method:: plan_react_strategy(state: haive.core.schema.prebuilt.rag_state.RAGState) -> dict[str, Any]

      Plan RAG strategy using ReAct reasoning.


      .. autolink-examples:: plan_react_strategy
         :collapse:


   .. py:method:: setup_agent() -> None

      Initialize engines and strategy agents.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:method:: strategy_router(state: haive.core.schema.prebuilt.rag_state.RAGState) -> str

      Route to the appropriate strategy execution node based on the selected strategy.


      .. autolink-examples:: strategy_router
         :collapse:


   .. py:method:: synthesize_agentic_result(state: haive.core.schema.prebuilt.rag_state.RAGState) -> dict[str, Any]

      Synthesize final agentic routing result.


      .. autolink-examples:: synthesize_agentic_result
         :collapse:


   .. py:attribute:: autonomy_level
      :type:  str
      :value: None



   .. py:attribute:: documents
      :type:  list[langchain_core.documents.Document]
      :value: None



   .. py:attribute:: llm_config
      :type:  haive.core.models.llm.base.LLMConfig
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: 'Agentic RAG Router'



   .. py:attribute:: planning_engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



   .. py:attribute:: strategy_agents
      :type:  dict[RAGStrategy, haive.agents.base.agent.Agent] | None
      :value: None



   .. py:attribute:: synthesis_engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



.. py:class:: AgenticRouterResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Complete result from agentic RAG routing.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgenticRouterResult
      :collapse:

   .. py:attribute:: answer_quality
      :type:  float
      :value: None



   .. py:attribute:: autonomous_decisions
      :type:  int
      :value: None



   .. py:attribute:: decision_confidence
      :type:  float
      :value: None



   .. py:attribute:: efficiency_score
      :type:  float
      :value: None



   .. py:attribute:: evidence_strength
      :type:  float
      :value: None



   .. py:attribute:: final_response
      :type:  str
      :value: None



   .. py:attribute:: original_query
      :type:  str
      :value: None



   .. py:attribute:: primary_strategy
      :type:  RAGStrategy
      :value: None



   .. py:attribute:: processing_metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: reasoning_quality
      :type:  float
      :value: None



   .. py:attribute:: reasoning_steps
      :type:  int
      :value: None



   .. py:attribute:: resource_utilization
      :type:  dict[str, float]
      :value: None



   .. py:attribute:: strategies_considered
      :type:  list[RAGStrategy]
      :value: None



   .. py:attribute:: strategy_switch_count
      :type:  int
      :value: None



   .. py:attribute:: total_processing_time
      :type:  float
      :value: None



.. py:class:: ExecutionResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result from strategy execution.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ExecutionResult
      :collapse:

   .. py:attribute:: completeness_score
      :type:  float
      :value: None



   .. py:attribute:: errors_encountered
      :type:  list[str]
      :value: None



   .. py:attribute:: execution_metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: execution_successful
      :type:  bool
      :value: None



   .. py:attribute:: execution_time
      :type:  float
      :value: None



   .. py:attribute:: fallback_used
      :type:  bool
      :value: None



   .. py:attribute:: final_response
      :type:  str
      :value: None



   .. py:attribute:: processing_steps
      :type:  int
      :value: None



   .. py:attribute:: relevance_score
      :type:  float
      :value: None



   .. py:attribute:: result_confidence
      :type:  float
      :value: None



   .. py:attribute:: retrieval_count
      :type:  int
      :value: None



   .. py:attribute:: source_documents
      :type:  list[langchain_core.documents.Document]
      :value: None



   .. py:attribute:: strategy_used
      :type:  RAGStrategy
      :value: None



   .. py:attribute:: supporting_evidence
      :type:  list[str]
      :value: None



.. py:class:: RAGStrategy

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Available RAG strategies for routing.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RAGStrategy
      :collapse:

   .. py:attribute:: ADAPTIVE
      :value: 'adaptive'



   .. py:attribute:: CORRECTIVE
      :value: 'corrective'



   .. py:attribute:: FLARE
      :value: 'flare'



   .. py:attribute:: FUSION
      :value: 'fusion'



   .. py:attribute:: HYDE
      :value: 'hyde'



   .. py:attribute:: MULTI_QUERY
      :value: 'multi_query'



   .. py:attribute:: SIMPLE
      :value: 'simple'



.. py:class:: ReActPlan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Complete ReAct planning result.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReActPlan
      :collapse:

   .. py:attribute:: estimated_complexity
      :type:  float
      :value: None



   .. py:attribute:: estimated_time
      :type:  float
      :value: None



   .. py:attribute:: execution_steps
      :type:  list[str]
      :value: None



   .. py:attribute:: failure_handling
      :type:  str
      :value: None



   .. py:attribute:: fallback_strategies
      :type:  list[RAGStrategy]
      :value: None



   .. py:attribute:: planning_metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: query_analysis
      :type:  str
      :value: None



   .. py:attribute:: reasoning_chain
      :type:  list[ReasoningStep]
      :value: None



   .. py:attribute:: resource_requirements
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: selected_strategy
      :type:  RAGStrategy
      :value: None



   .. py:attribute:: strategy_confidence
      :type:  float
      :value: None



   .. py:attribute:: success_criteria
      :type:  list[str]
      :value: None



.. py:class:: ReasoningStep(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Individual reasoning step in ReAct pattern.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReasoningStep
      :collapse:

   .. py:attribute:: action
      :type:  str
      :value: None



   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: next_step_needed
      :type:  bool
      :value: None



   .. py:attribute:: observation
      :type:  str
      :value: None



   .. py:attribute:: step_number
      :type:  int
      :value: None



   .. py:attribute:: thought
      :type:  str
      :value: None



.. py:function:: create_agentic_rag_router_agent(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, routing_mode: str = 'autonomous', **kwargs) -> AgenticRAGRouterAgent

   Create an Agentic RAG Router agent.

   :param documents: Documents for RAG strategies
   :param llm_config: LLM configuration
   :param routing_mode: Routing mode ("conservative", "balanced", "autonomous")
   :param \*\*kwargs: Additional arguments

   :returns: Configured Agentic RAG Router agent


   .. autolink-examples:: create_agentic_rag_router_agent
      :collapse:

.. py:function:: get_agentic_rag_router_io_schema() -> dict[str, list[str]]

   Get I/O schema for Agentic RAG Router agents.


   .. autolink-examples:: get_agentic_rag_router_io_schema
      :collapse:

.. py:data:: AGENTIC_SYNTHESIS_PROMPT

.. py:data:: REACT_PLANNING_PROMPT

.. py:data:: STRATEGY_EXECUTION_PROMPT

.. py:data:: logger

