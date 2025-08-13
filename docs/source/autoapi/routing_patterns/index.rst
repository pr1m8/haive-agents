
:py:mod:`routing_patterns`
==========================

.. py:module:: routing_patterns

Routing patterns for multi-agent systems.

from typing import Any
Experiments with conditional routing, branching, and dynamic paths.
Uses BaseGraph's add_conditional_edges for sophisticated routing.


.. autolink-examples:: routing_patterns
   :collapse:

Classes
-------

.. autoapisummary::

   routing_patterns.BranchingMultiAgent
   routing_patterns.RoutingMultiAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BranchingMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_BranchingMultiAgent {
        node [shape=record];
        "BranchingMultiAgent" [label="BranchingMultiAgent"];
        "RoutingMultiAgent" -> "BranchingMultiAgent";
      }

.. autoclass:: routing_patterns.BranchingMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RoutingMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_RoutingMultiAgent {
        node [shape=record];
        "RoutingMultiAgent" [label="RoutingMultiAgent"];
        "haive.agents.multi.experiments.list_multi_agent.ListMultiAgent" -> "RoutingMultiAgent";
      }

.. autoclass:: routing_patterns.RoutingMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   routing_patterns.category_router
   routing_patterns.confidence_router
   routing_patterns.error_router
   routing_patterns.has_tool_calls_router

.. py:function:: category_router(state: dict[str, Any]) -> str

   Route based on category field.


   .. autolink-examples:: category_router
      :collapse:

.. py:function:: confidence_router(state: dict[str, Any]) -> str

   Route based on confidence level.


   .. autolink-examples:: confidence_router
      :collapse:

.. py:function:: error_router(state: dict[str, Any]) -> str

   Route based on error presence.


   .. autolink-examples:: error_router
      :collapse:

.. py:function:: has_tool_calls_router(state: dict[str, Any]) -> bool

   Check if there are tool calls in the last message.


   .. autolink-examples:: has_tool_calls_router
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: routing_patterns
   :collapse:
   
.. autolink-skip:: next
