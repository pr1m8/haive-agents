
:py:mod:`agents.chain.examples`
===============================

.. py:module:: agents.chain.examples

Examples of using DeclarativeChainAgent to build complex RAG flows.

Shows how to recreate our complex agents using declarative specifications.


.. autolink-examples:: agents.chain.examples
   :collapse:

Classes
-------

.. autoapisummary::

   agents.chain.examples.StrategyDecision


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for StrategyDecision:

   .. graphviz::
      :align: center

      digraph inheritance_StrategyDecision {
        node [shape=record];
        "StrategyDecision" [label="StrategyDecision"];
        "pydantic.BaseModel" -> "StrategyDecision";
      }

.. autopydantic_model:: agents.chain.examples.StrategyDecision
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:



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



.. rubric:: Related Links

.. autolink-examples:: agents.chain.examples
   :collapse:
   
.. autolink-skip:: next
