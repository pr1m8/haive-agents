
:py:mod:`agents.simple.agent`
=============================

.. py:module:: agents.simple.agent

Agent_V3 core module.

This module provides agent v3 functionality for the Haive framework.

Classes:
    with: with implementation.
    SimpleAgent: SimpleAgent implementation.
    with: with implementation.

Functions:
    log_execution_start: Log Execution Start functionality.
    log_execution_complete: Log Execution Complete functionality.
    ensure_aug_llm_config_with_debug: Ensure Aug Llm Config With Debug functionality.


.. autolink-examples:: agents.simple.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.simple.agent.SimpleAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SimpleAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleAgent {
        node [shape=record];
        "SimpleAgent" [label="SimpleAgent"];
        "haive.agents.base.agent.Agent[haive.core.engine.aug_llm.AugLLMConfig]" -> "SimpleAgent";
        "haive.core.common.mixins.recompile_mixin.RecompileMixin" -> "SimpleAgent";
        "haive.core.common.mixins.dynamic_tool_route_mixin.DynamicToolRouteMixin" -> "SimpleAgent";
      }

.. autoclass:: agents.simple.agent.SimpleAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.simple.agent
   :collapse:
   
.. autolink-skip:: next
