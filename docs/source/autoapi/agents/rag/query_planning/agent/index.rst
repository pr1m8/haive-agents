agents.rag.query_planning.agent
===============================

.. py:module:: agents.rag.query_planning.agent

.. autoapi-nested-parse::

   Query Planning Agentic RAG Agent.

   from typing import Any
   Implementation of query planning RAG with structured decomposition and execution.
   Provides intelligent query analysis, planning, and multi-stage retrieval strategies.


   .. autolink-examples:: agents.rag.query_planning.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.query_planning.agent.QUERY_PLANNING_PROMPT
   agents.rag.query_planning.agent.QUERY_SYNTHESIS_PROMPT
   agents.rag.query_planning.agent.SUB_QUERY_EXECUTION_PROMPT
   agents.rag.query_planning.agent.logger


Classes
-------

.. autoapisummary::

   agents.rag.query_planning.agent.QueryComplexity
   agents.rag.query_planning.agent.QueryPlan
   agents.rag.query_planning.agent.QueryPlanningRAGAgent
   agents.rag.query_planning.agent.QueryPlanningResult
   agents.rag.query_planning.agent.QueryType
   agents.rag.query_planning.agent.SubQuery
   agents.rag.query_planning.agent.SubQueryResult


Functions
---------

.. autoapisummary::

   agents.rag.query_planning.agent.create_query_planning_rag_agent
   agents.rag.query_planning.agent.get_query_planning_rag_io_schema


Module Contents
---------------

.. py:class:: QueryComplexity

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Query complexity levels.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QueryComplexity
      :collapse:

   .. py:attribute:: COMPLEX
      :value: 'complex'



   .. py:attribute:: MODERATE
      :value: 'moderate'



   .. py:attribute:: MULTI_FACETED
      :value: 'multi_faceted'



   .. py:attribute:: SIMPLE
      :value: 'simple'



.. py:class:: QueryPlan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Complete query execution plan.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QueryPlan
      :collapse:

   .. py:attribute:: estimated_retrievals
      :type:  int
      :value: None



   .. py:attribute:: estimated_time
      :type:  float
      :value: None



   .. py:attribute:: execution_order
      :type:  list[str]
      :value: None



   .. py:attribute:: fallback_plan
      :type:  str
      :value: None



   .. py:attribute:: original_query
      :type:  str
      :value: None



   .. py:attribute:: parallel_groups
      :type:  list[list[str]]
      :value: None



   .. py:attribute:: planning_confidence
      :type:  float
      :value: None



   .. py:attribute:: planning_rationale
      :type:  str
      :value: None



   .. py:attribute:: primary_intent
      :type:  str
      :value: None



   .. py:attribute:: query_complexity
      :type:  QueryComplexity
      :value: None



   .. py:attribute:: resource_requirements
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: retrieval_strategy
      :type:  str
      :value: None



   .. py:attribute:: sub_queries
      :type:  list[SubQuery]
      :value: None



   .. py:attribute:: synthesis_approach
      :type:  str
      :value: None



.. py:class:: QueryPlanningRAGAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Query Planning RAG agent with structured decomposition and execution.

   This agent uses conditional edges to execute sub-queries in a planned order.


   .. autolink-examples:: QueryPlanningRAGAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the query planning graph with conditional edges.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: create_query_plan(state: dict[str, Any]) -> dict[str, Any]

      Create a query execution plan.


      .. autolink-examples:: create_query_plan
         :collapse:


   .. py:method:: execute_sub_query(state: dict[str, Any]) -> dict[str, Any]

      Execute the current sub-query.


      .. autolink-examples:: execute_sub_query
         :collapse:


   .. py:method:: from_documents(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, planning_depth: int = 3, **kwargs)
      :classmethod:


      Create Query Planning RAG agent from documents.

      :param documents: Documents to index for retrieval
      :param llm_config: LLM configuration
      :param planning_depth: Maximum depth of query decomposition
      :param \*\*kwargs: Additional arguments

      :returns: QueryPlanningRAGAgent instance


      .. autolink-examples:: from_documents
         :collapse:


   .. py:method:: setup_agent() -> None

      Initialize engines.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:method:: should_continue_execution(state: dict[str, Any]) -> str

      Determine if more sub-queries should be executed.


      .. autolink-examples:: should_continue_execution
         :collapse:


   .. py:method:: synthesize_results(state: dict[str, Any]) -> dict[str, Any]

      Synthesize sub-query results into final answer.


      .. autolink-examples:: synthesize_results
         :collapse:


   .. py:attribute:: documents
      :type:  list[langchain_core.documents.Document]
      :value: None



   .. py:attribute:: execution_engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



   .. py:attribute:: llm_config
      :type:  haive.core.models.llm.base.LLMConfig
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: 'Query Planning RAG Agent'



   .. py:attribute:: planning_depth
      :type:  int
      :value: None



   .. py:attribute:: planning_engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



   .. py:attribute:: synthesis_engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



.. py:class:: QueryPlanningResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Complete result from query planning execution.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QueryPlanningResult
      :collapse:

   .. py:attribute:: answer_completeness
      :type:  float
      :value: None



   .. py:attribute:: answer_confidence
      :type:  float
      :value: None



   .. py:attribute:: bottlenecks
      :type:  list[str]
      :value: None



   .. py:attribute:: execution_metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: final_answer
      :type:  str
      :value: None



   .. py:attribute:: improvements
      :type:  list[str]
      :value: None



   .. py:attribute:: original_query
      :type:  str
      :value: None



   .. py:attribute:: plan_execution_rate
      :type:  float
      :value: None



   .. py:attribute:: plan_success_rate
      :type:  float
      :value: None



   .. py:attribute:: query_plan
      :type:  QueryPlan
      :value: None



   .. py:attribute:: sub_query_results
      :type:  list[SubQueryResult]
      :value: None



   .. py:attribute:: synthesis_quality
      :type:  float
      :value: None



   .. py:attribute:: total_execution_time
      :type:  float
      :value: None



   .. py:attribute:: total_retrievals
      :type:  int
      :value: None



.. py:class:: QueryType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of queries for planning.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QueryType
      :collapse:

   .. py:attribute:: ANALYTICAL
      :value: 'analytical'



   .. py:attribute:: COMPARATIVE
      :value: 'comparative'



   .. py:attribute:: CONCEPTUAL
      :value: 'conceptual'



   .. py:attribute:: EXPLORATORY
      :value: 'exploratory'



   .. py:attribute:: FACTUAL
      :value: 'factual'



   .. py:attribute:: PROCEDURAL
      :value: 'procedural'



.. py:class:: SubQuery(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Individual sub-query in a decomposed plan.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SubQuery
      :collapse:

   .. py:attribute:: dependencies
      :type:  list[str]
      :value: None



   .. py:attribute:: estimated_difficulty
      :type:  float
      :value: None



   .. py:attribute:: expected_info
      :type:  str
      :value: None



   .. py:attribute:: priority
      :type:  int
      :value: None



   .. py:attribute:: query_id
      :type:  str
      :value: None



   .. py:attribute:: query_text
      :type:  str
      :value: None



   .. py:attribute:: query_type
      :type:  QueryType
      :value: None



   .. py:attribute:: retrieval_strategy
      :type:  str
      :value: None



   .. py:attribute:: success_criteria
      :type:  str
      :value: None



.. py:class:: SubQueryResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result from executing a sub-query.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SubQueryResult
      :collapse:

   .. py:attribute:: answer
      :type:  str
      :value: None



   .. py:attribute:: completeness_score
      :type:  float
      :value: None



   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: execution_successful
      :type:  bool
      :value: None



   .. py:attribute:: execution_time
      :type:  float
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: query_id
      :type:  str
      :value: None



   .. py:attribute:: query_text
      :type:  str
      :value: None



   .. py:attribute:: relevance_score
      :type:  float
      :value: None



   .. py:attribute:: retrieval_count
      :type:  int
      :value: None



   .. py:attribute:: supporting_documents
      :type:  list[langchain_core.documents.Document]
      :value: None



.. py:function:: create_query_planning_rag_agent(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, planning_mode: str = 'comprehensive', **kwargs) -> QueryPlanningRAGAgent

   Create a Query Planning RAG agent.

   :param documents: Documents for retrieval
   :param llm_config: LLM configuration
   :param planning_mode: Planning mode ("simple", "moderate", "comprehensive")
   :param \*\*kwargs: Additional arguments

   :returns: Configured Query Planning RAG agent


   .. autolink-examples:: create_query_planning_rag_agent
      :collapse:

.. py:function:: get_query_planning_rag_io_schema() -> dict[str, list[str]]

   Get I/O schema for Query Planning RAG agents.


   .. autolink-examples:: get_query_planning_rag_io_schema
      :collapse:

.. py:data:: QUERY_PLANNING_PROMPT

.. py:data:: QUERY_SYNTHESIS_PROMPT

.. py:data:: SUB_QUERY_EXECUTION_PROMPT

.. py:data:: logger

