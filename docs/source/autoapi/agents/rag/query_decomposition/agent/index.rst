
:py:mod:`agents.rag.query_decomposition.agent`
==============================================

.. py:module:: agents.rag.query_decomposition.agent

Query Decomposition Agents.

Modular agents for breaking down complex queries into manageable sub-queries.
Can be plugged into any workflow with compatible I/O schemas.


.. autolink-examples:: agents.rag.query_decomposition.agent
   :collapse:

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


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AdaptiveQueryDecomposerAgent:

   .. graphviz::
      :align: center

      digraph inheritance_AdaptiveQueryDecomposerAgent {
        node [shape=record];
        "AdaptiveQueryDecomposerAgent" [label="AdaptiveQueryDecomposerAgent"];
        "haive.agents.base.agent.Agent" -> "AdaptiveQueryDecomposerAgent";
      }

.. autoclass:: agents.rag.query_decomposition.agent.AdaptiveQueryDecomposerAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ContextualDecomposition:

   .. graphviz::
      :align: center

      digraph inheritance_ContextualDecomposition {
        node [shape=record];
        "ContextualDecomposition" [label="ContextualDecomposition"];
        "pydantic.BaseModel" -> "ContextualDecomposition";
      }

.. autopydantic_model:: agents.rag.query_decomposition.agent.ContextualDecomposition
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





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ContextualQueryDecomposerAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ContextualQueryDecomposerAgent {
        node [shape=record];
        "ContextualQueryDecomposerAgent" [label="ContextualQueryDecomposerAgent"];
        "haive.agents.base.agent.Agent" -> "ContextualQueryDecomposerAgent";
      }

.. autoclass:: agents.rag.query_decomposition.agent.ContextualQueryDecomposerAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HierarchicalDecomposition:

   .. graphviz::
      :align: center

      digraph inheritance_HierarchicalDecomposition {
        node [shape=record];
        "HierarchicalDecomposition" [label="HierarchicalDecomposition"];
        "pydantic.BaseModel" -> "HierarchicalDecomposition";
      }

.. autopydantic_model:: agents.rag.query_decomposition.agent.HierarchicalDecomposition
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





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HierarchicalQueryDecomposerAgent:

   .. graphviz::
      :align: center

      digraph inheritance_HierarchicalQueryDecomposerAgent {
        node [shape=record];
        "HierarchicalQueryDecomposerAgent" [label="HierarchicalQueryDecomposerAgent"];
        "haive.agents.base.agent.Agent" -> "HierarchicalQueryDecomposerAgent";
      }

.. autoclass:: agents.rag.query_decomposition.agent.HierarchicalQueryDecomposerAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for QueryDecomposerAgent:

   .. graphviz::
      :align: center

      digraph inheritance_QueryDecomposerAgent {
        node [shape=record];
        "QueryDecomposerAgent" [label="QueryDecomposerAgent"];
        "haive.agents.base.agent.Agent" -> "QueryDecomposerAgent";
      }

.. autoclass:: agents.rag.query_decomposition.agent.QueryDecomposerAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for QueryDecomposition:

   .. graphviz::
      :align: center

      digraph inheritance_QueryDecomposition {
        node [shape=record];
        "QueryDecomposition" [label="QueryDecomposition"];
        "pydantic.BaseModel" -> "QueryDecomposition";
      }

.. autopydantic_model:: agents.rag.query_decomposition.agent.QueryDecomposition
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





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for QueryType:

   .. graphviz::
      :align: center

      digraph inheritance_QueryType {
        node [shape=record];
        "QueryType" [label="QueryType"];
        "str" -> "QueryType";
        "enum.Enum" -> "QueryType";
      }

.. autoclass:: agents.rag.query_decomposition.agent.QueryType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **QueryType** is an Enum defined in ``agents.rag.query_decomposition.agent``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SubQuery:

   .. graphviz::
      :align: center

      digraph inheritance_SubQuery {
        node [shape=record];
        "SubQuery" [label="SubQuery"];
        "pydantic.BaseModel" -> "SubQuery";
      }

.. autopydantic_model:: agents.rag.query_decomposition.agent.SubQuery
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

   agents.rag.query_decomposition.agent.create_query_decomposer
   agents.rag.query_decomposition.agent.get_query_decomposer_io_schema

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



.. rubric:: Related Links

.. autolink-examples:: agents.rag.query_decomposition.agent
   :collapse:
   
.. autolink-skip:: next
