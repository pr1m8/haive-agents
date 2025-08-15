agents.rag.query_planning.agent_chain
=====================================

.. py:module:: agents.rag.query_planning.agent_chain

.. autoapi-nested-parse::

   Query Planning RAG using ChainAgent.

   Simplified version using the new ChainAgent approach.


   .. autolink-examples:: agents.rag.query_planning.agent_chain
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.query_planning.agent_chain.QueryPlan
   agents.rag.query_planning.agent_chain.SubQueryResult


Functions
---------

.. autoapisummary::

   agents.rag.query_planning.agent_chain.create_adaptive_planning_chain
   agents.rag.query_planning.agent_chain.create_query_planning_chain
   agents.rag.query_planning.agent_chain.create_simple_decomposition_chain
   agents.rag.query_planning.agent_chain.get_query_planning_chain_io_schema


Module Contents
---------------

.. py:class:: QueryPlan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Simplified query plan.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QueryPlan
      :collapse:

   .. py:attribute:: execution_strategy
      :type:  str
      :value: None



   .. py:attribute:: sub_queries
      :type:  list[str]
      :value: None



   .. py:attribute:: synthesis_approach
      :type:  str
      :value: None



.. py:class:: SubQueryResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result from a sub-query.

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



   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



.. py:function:: create_adaptive_planning_chain(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None) -> haive.agents.chain.ChainAgent

   Adaptive planning based on query complexity.


   .. autolink-examples:: create_adaptive_planning_chain
      :collapse:

.. py:function:: create_query_planning_chain(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, name: str = 'Query Planning RAG') -> haive.agents.chain.ChainAgent

   Create query planning RAG using ChainAgent.


   .. autolink-examples:: create_query_planning_chain
      :collapse:

.. py:function:: create_simple_decomposition_chain(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None) -> haive.agents.chain.ChainAgent

   Even simpler version - just decompose and answer.


   .. autolink-examples:: create_simple_decomposition_chain
      :collapse:

.. py:function:: get_query_planning_chain_io_schema() -> dict[str, list[str]]

   Get I/O schema for query planning chain.


   .. autolink-examples:: get_query_planning_chain_io_schema
      :collapse:

