
:py:mod:`agents.react.dynamic_react_agent.v2`
=============================================

.. py:module:: agents.react.dynamic_react_agent.v2

Dynamic React Agent with Tool Loading Capabilities.

This module provides DynamicReactAgent, an enhanced ReactAgent that can
dynamically discover, load, and activate tools based on task requirements
using the Dynamic Activation Pattern.

Based on:
- @project_docs/active/patterns/dynamic_activation_pattern.md
- @notebooks/tool_loader.ipynb pattern for tool loading
- @packages/haive-agents/examples/supervisor/advanced/dynamic_activation_example.py


.. autolink-examples:: agents.react.dynamic_react_agent.v2
   :collapse:

Classes
-------

.. autoapisummary::

   agents.react.dynamic_react_agent.v2.DynamicReactAgent
   agents.react.dynamic_react_agent.v2.DynamicToolState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DynamicReactAgent:

   .. graphviz::
      :align: center

      digraph inheritance_DynamicReactAgent {
        node [shape=record];
        "DynamicReactAgent" [label="DynamicReactAgent"];
        "haive.agents.react.agent.ReactAgent" -> "DynamicReactAgent";
      }

.. autoclass:: agents.react.dynamic_react_agent.v2.DynamicReactAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DynamicToolState:

   .. graphviz::
      :align: center

      digraph inheritance_DynamicToolState {
        node [shape=record];
        "DynamicToolState" [label="DynamicToolState"];
        "haive.core.schema.prebuilt.dynamic_activation_state.DynamicActivationState" -> "DynamicToolState";
      }

.. autoclass:: agents.react.dynamic_react_agent.v2.DynamicToolState
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.react.dynamic_react_agent.v2
   :collapse:
   
.. autolink-skip:: next
