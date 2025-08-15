agents.rag.query_decomposition.agent
====================================

.. py:module:: agents.rag.query_decomposition.agent

.. autoapi-nested-parse::

   Query Decomposition Agents.

   Modular agents for breaking down complex queries into manageable sub-queries.
   Can be plugged into any workflow with compatible I/O schemas.


   .. autolink-examples:: agents.rag.query_decomposition.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.query_decomposition.agent.ADAPTIVE_DECOMPOSITION_PROMPT
   agents.rag.query_decomposition.agent.BASIC_DECOMPOSITION_PROMPT
   agents.rag.query_decomposition.agent.CONTEXTUAL_DECOMPOSITION_PROMPT
   agents.rag.query_decomposition.agent.HIERARCHICAL_DECOMPOSITION_PROMPT
   agents.rag.query_decomposition.agent.logger


Classes
-------

.. autoapisummary::

   agents.rag.query_decomposition.agent.AdaptiveQueryDecomposerAgent
   agents.rag.query_decomposition.agent.ContextualDecomposition
   agents.rag.query_decomposition.agent.ContextualQueryDecomposerAgent
   agents.rag.query_decomposition.agent.HierarchicalDecomposition
   agents.rag.query_decomposition.agent.HierarchicalQueryDecomposerAgent
   agents.rag.query_decomposition.agent.QueryDecomposerAgent
   agents.rag.query_decomposition.agent.QueryDecomposition
   agents.rag.query_decomposition.agent.QueryType
   agents.rag.query_decomposition.agent.SubQuery


Functions
---------

.. autoapisummary::

   agents.rag.query_decomposition.agent.create_query_decomposer
   agents.rag.query_decomposition.agent.get_query_decomposer_io_schema


Module Contents
---------------

.. py:class:: AdaptiveQueryDecomposerAgent(llm_config: haive.core.models.llm.base.LLMConfig | None = None, enable_fallback: bool = True, **kwargs)

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Adaptive query decomposition that selects best strategy.

   Initialize adaptive query decomposer.

   :param llm_config: LLM configuration
   :param enable_fallback: Whether to fallback to simpler decomposition if needed
   :param \*\*kwargs: Additional agent arguments


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AdaptiveQueryDecomposerAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build adaptive decomposition graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: enable_fallback
      :value: True



   .. py:attribute:: llm_config


   .. py:attribute:: name
      :type:  str
      :value: 'Adaptive Query Decomposer'



.. py:class:: ContextualDecomposition(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Context-aware query decomposition.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ContextualDecomposition
      :collapse:

   .. py:attribute:: context_analysis
      :type:  str
      :value: None



   .. py:attribute:: context_dependent_queries
      :type:  list[str]
      :value: None



   .. py:attribute:: context_independent_queries
      :type:  list[str]
      :value: None



   .. py:attribute:: context_sufficiency
      :type:  float
      :value: None



   .. py:attribute:: missing_context_queries
      :type:  list[str]
      :value: None



   .. py:attribute:: original_query
      :type:  str
      :value: None



   .. py:attribute:: retrieval_strategy
      :type:  Literal['broad', 'focused', 'mixed']
      :value: None



.. py:class:: ContextualQueryDecomposerAgent(llm_config: haive.core.models.llm.base.LLMConfig | None = None, context_threshold: float = 0.7, **kwargs)

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Context-aware query decomposition agent.

   Initialize contextual query decomposer.

   :param llm_config: LLM configuration
   :param context_threshold: Threshold for context sufficiency
   :param \*\*kwargs: Additional agent arguments


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ContextualQueryDecomposerAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build contextual decomposition graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: context_threshold
      :value: 0.7



   .. py:attribute:: llm_config


   .. py:attribute:: name
      :type:  str
      :value: 'Contextual Query Decomposer'



.. py:class:: HierarchicalDecomposition(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Hierarchical query decomposition with levels.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HierarchicalDecomposition
      :collapse:

   .. py:attribute:: confidence_level
      :type:  float
      :value: None



   .. py:attribute:: dependency_map
      :type:  dict[str, list[str]]
      :value: None



   .. py:attribute:: detail_questions
      :type:  list[str]
      :value: None



   .. py:attribute:: execution_levels
      :type:  list[list[int]]
      :value: None



   .. py:attribute:: main_question
      :type:  str
      :value: None



   .. py:attribute:: original_query
      :type:  str
      :value: None



   .. py:attribute:: sub_questions
      :type:  list[str]
      :value: None



   .. py:attribute:: synthesis_plan
      :type:  str
      :value: None



.. py:class:: HierarchicalQueryDecomposerAgent(llm_config: haive.core.models.llm.base.LLMConfig | None = None, max_levels: int = 3, **kwargs)

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Hierarchical query decomposition agent.

   Initialize hierarchical query decomposer.

   :param llm_config: LLM configuration
   :param max_levels: Maximum hierarchy levels
   :param \*\*kwargs: Additional agent arguments


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HierarchicalQueryDecomposerAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build hierarchical decomposition graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: llm_config


   .. py:attribute:: max_levels
      :value: 3



   .. py:attribute:: name
      :type:  str
      :value: 'Hierarchical Query Decomposer'



.. py:class:: QueryDecomposerAgent(llm_config: haive.core.models.llm.base.LLMConfig | None = None, max_sub_queries: int = 5, **kwargs)

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Basic query decomposition agent.

   Initialize query decomposer.

   :param llm_config: LLM configuration
   :param max_sub_queries: Maximum number of sub-queries to generate
   :param \*\*kwargs: Additional agent arguments


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QueryDecomposerAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build query decomposition graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: llm_config


   .. py:attribute:: max_sub_queries
      :value: 5



   .. py:attribute:: name
      :type:  str
      :value: 'Query Decomposer'



.. py:class:: QueryDecomposition(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Complete query decomposition result.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QueryDecomposition
      :collapse:

   .. py:attribute:: alternative_approaches
      :type:  list[str]
      :value: None



   .. py:attribute:: complexity_score
      :type:  float
      :value: None



   .. py:attribute:: estimated_difficulty
      :type:  Literal['easy', 'moderate', 'hard', 'very_hard']
      :value: None



   .. py:attribute:: execution_order
      :type:  list[int]
      :value: None



   .. py:attribute:: original_query
      :type:  str
      :value: None



   .. py:attribute:: query_type
      :type:  QueryType
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: sub_queries
      :type:  list[SubQuery]
      :value: None



   .. py:attribute:: synthesis_strategy
      :type:  str
      :value: None



.. py:class:: QueryType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of queries for decomposition strategy.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QueryType
      :collapse:

   .. py:attribute:: CAUSAL
      :value: 'causal'



   .. py:attribute:: COMPARATIVE
      :value: 'comparative'



   .. py:attribute:: COMPOUND
      :value: 'compound'



   .. py:attribute:: HYPOTHETICAL
      :value: 'hypothetical'



   .. py:attribute:: MULTI_HOP
      :value: 'multi_hop'



   .. py:attribute:: SIMPLE
      :value: 'simple'



   .. py:attribute:: TEMPORAL
      :value: 'temporal'



.. py:class:: SubQuery(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Individual sub-query in decomposition.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SubQuery
      :collapse:

   .. py:attribute:: dependencies
      :type:  list[int]
      :value: None



   .. py:attribute:: expected_info_type
      :type:  str
      :value: None



   .. py:attribute:: priority
      :type:  int
      :value: None



   .. py:attribute:: query_text
      :type:  str
      :value: None



   .. py:attribute:: query_type
      :type:  QueryType
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



.. py:function:: create_query_decomposer(decomposer_type: Literal['basic', 'hierarchical', 'contextual', 'adaptive'] = 'basic', llm_config: haive.core.models.llm.base.LLMConfig | None = None, **kwargs) -> haive.agents.base.agent.Agent

   Create a query decomposer agent.

   :param decomposer_type: Type of decomposer to create
   :param llm_config: LLM configuration
   :param \*\*kwargs: Additional arguments

   :returns: Configured query decomposer agent


   .. autolink-examples:: create_query_decomposer
      :collapse:

.. py:function:: get_query_decomposer_io_schema() -> dict[str, list[str]]

   Get I/O schema for query decomposers for compatibility checking.


   .. autolink-examples:: get_query_decomposer_io_schema
      :collapse:

.. py:data:: ADAPTIVE_DECOMPOSITION_PROMPT

.. py:data:: BASIC_DECOMPOSITION_PROMPT

.. py:data:: CONTEXTUAL_DECOMPOSITION_PROMPT

.. py:data:: HIERARCHICAL_DECOMPOSITION_PROMPT

.. py:data:: logger

