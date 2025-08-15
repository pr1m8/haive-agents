agents.chain.examples
=====================

.. py:module:: agents.chain.examples

.. autoapi-nested-parse::

   Examples of using DeclarativeChainAgent to build complex RAG flows.

   Shows how to recreate our complex agents using declarative specifications.


   .. autolink-examples:: agents.chain.examples
      :collapse:


Classes
-------

.. autoapisummary::

   agents.chain.examples.StrategyDecision


Functions
---------

.. autoapisummary::

   agents.chain.examples.create_agentic_router_declarative
   agents.chain.examples.create_complex_flow_from_spec
   agents.chain.examples.create_plan
   agents.chain.examples.create_query_planning_declarative
   agents.chain.examples.create_rag_with_fallback
   agents.chain.examples.create_self_reflective_declarative
   agents.chain.examples.execute_sub_query
   agents.chain.examples.finalize_answer
   agents.chain.examples.improve_answer
   agents.chain.examples.reflect_and_critique
   agents.chain.examples.synthesize_results


Module Contents
---------------

.. py:class:: StrategyDecision(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Strategy decision for RAG routing.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: StrategyDecision
      :collapse:

   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: strategy
      :type:  str
      :value: None



.. py:function:: create_agentic_router_declarative(documents: list[langchain_core.documents.Document])

   Create an agentic RAG router using declarative chain building.


   .. autolink-examples:: create_agentic_router_declarative
      :collapse:

.. py:function:: create_complex_flow_from_spec() -> Any

   Create a complex flow using raw ChainSpec.


   .. autolink-examples:: create_complex_flow_from_spec
      :collapse:

.. py:function:: create_plan(state: dict[str, Any]) -> dict[str, Any]

   Create query execution plan.


   .. autolink-examples:: create_plan
      :collapse:

.. py:function:: create_query_planning_declarative(documents: list[langchain_core.documents.Document])

   Create a query planning RAG using declarative chain building.


   .. autolink-examples:: create_query_planning_declarative
      :collapse:

.. py:function:: create_rag_with_fallback() -> Any

   Create a RAG with fallback strategies.


   .. autolink-examples:: create_rag_with_fallback
      :collapse:

.. py:function:: create_self_reflective_declarative(documents: list[langchain_core.documents.Document])

   Create a self-reflective RAG using declarative chain building.


   .. autolink-examples:: create_self_reflective_declarative
      :collapse:

.. py:function:: execute_sub_query(state: dict[str, Any]) -> dict[str, Any]

   Execute one sub-query.


   .. autolink-examples:: execute_sub_query
      :collapse:

.. py:function:: finalize_answer(state: dict[str, Any]) -> dict[str, Any]

   Finalize the answer.


   .. autolink-examples:: finalize_answer
      :collapse:

.. py:function:: improve_answer(state: dict[str, Any]) -> dict[str, Any]

   Improve the answer based on critique.


   .. autolink-examples:: improve_answer
      :collapse:

.. py:function:: reflect_and_critique(state: dict[str, Any]) -> dict[str, Any]

   Reflect on answer quality.


   .. autolink-examples:: reflect_and_critique
      :collapse:

.. py:function:: synthesize_results(state: dict[str, Any]) -> dict[str, Any]

   Synthesize all sub-query results.


   .. autolink-examples:: synthesize_results
      :collapse:

