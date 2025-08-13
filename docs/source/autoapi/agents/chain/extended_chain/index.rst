
:py:mod:`agents.chain.extended_chain`
=====================================

.. py:module:: agents.chain.extended_chain

Extended Chain Agent with simplified chain building capabilities.

This module provides the ExtendedChainAgent class and utilities for building
complex multi-step agent workflows with easy-to-use chain syntax.


.. autolink-examples:: agents.chain.extended_chain
   :collapse:

Classes
-------

.. autoapisummary::

   agents.chain.extended_chain.ChainBuilder
   agents.chain.extended_chain.ChainConfig
   agents.chain.extended_chain.ChainEdge
   agents.chain.extended_chain.ChainNode
   agents.chain.extended_chain.ChainState
   agents.chain.extended_chain.ExtendedChainAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ChainBuilder:

   .. graphviz::
      :align: center

      digraph inheritance_ChainBuilder {
        node [shape=record];
        "ChainBuilder" [label="ChainBuilder"];
      }

.. autoclass:: agents.chain.extended_chain.ChainBuilder
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ChainConfig:

   .. graphviz::
      :align: center

      digraph inheritance_ChainConfig {
        node [shape=record];
        "ChainConfig" [label="ChainConfig"];
        "haive.core.engine.agent.AgentConfig" -> "ChainConfig";
      }

.. autoclass:: agents.chain.extended_chain.ChainConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ChainEdge:

   .. graphviz::
      :align: center

      digraph inheritance_ChainEdge {
        node [shape=record];
        "ChainEdge" [label="ChainEdge"];
        "pydantic.BaseModel" -> "ChainEdge";
      }

.. autopydantic_model:: agents.chain.extended_chain.ChainEdge
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

   Inheritance diagram for ChainNode:

   .. graphviz::
      :align: center

      digraph inheritance_ChainNode {
        node [shape=record];
        "ChainNode" [label="ChainNode"];
        "pydantic.BaseModel" -> "ChainNode";
      }

.. autopydantic_model:: agents.chain.extended_chain.ChainNode
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

   Inheritance diagram for ChainState:

   .. graphviz::
      :align: center

      digraph inheritance_ChainState {
        node [shape=record];
        "ChainState" [label="ChainState"];
        "haive.core.schema.state_schema.StateSchema" -> "ChainState";
      }

.. autoclass:: agents.chain.extended_chain.ChainState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ExtendedChainAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ExtendedChainAgent {
        node [shape=record];
        "ExtendedChainAgent" [label="ExtendedChainAgent"];
        "haive.core.engine.agent.Agent" -> "ExtendedChainAgent";
      }

.. autoclass:: agents.chain.extended_chain.ExtendedChainAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.chain.extended_chain.chain
   agents.chain.extended_chain.chain_with_edges

.. py:function:: chain(*agents: Any) -> ChainBuilder

   Create a simple sequential chain from a list of agents.

   :param \*agents: Variable number of agents to chain together

   :returns: ChainBuilder instance with sequential chain setup


   .. autolink-examples:: chain
      :collapse:

.. py:function:: chain_with_edges(nodes: dict[str, Any], edges: list[tuple]) -> ChainBuilder

   Create a chain with explicit nodes and edges.

   :param nodes: Dictionary mapping node names to agents
   :param edges: List of (from_node, to_node) tuples

   :returns: ChainBuilder instance with the specified structure


   .. autolink-examples:: chain_with_edges
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.chain.extended_chain
   :collapse:
   
.. autolink-skip:: next
