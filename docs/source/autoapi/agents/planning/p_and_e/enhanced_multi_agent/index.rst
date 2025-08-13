
:py:mod:`agents.planning.p_and_e.enhanced_multi_agent`
======================================================

.. py:module:: agents.planning.p_and_e.enhanced_multi_agent

Enhanced Multi-Agent Base for Plan and Execute patterns.

This module provides an enhanced version of MultiAgent that allows for cleaner
configuration with agents, state schema, and branches passed directly.


.. autolink-examples:: agents.planning.p_and_e.enhanced_multi_agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning.p_and_e.enhanced_multi_agent.EnhancedMultiAgent
   agents.planning.p_and_e.enhanced_multi_agent.PlanAndExecuteMultiAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnhancedMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_EnhancedMultiAgent {
        node [shape=record];
        "EnhancedMultiAgent" [label="EnhancedMultiAgent"];
        "haive.agents.multi.base.MultiAgent" -> "EnhancedMultiAgent";
      }

.. autoclass:: agents.planning.p_and_e.enhanced_multi_agent.EnhancedMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PlanAndExecuteMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_PlanAndExecuteMultiAgent {
        node [shape=record];
        "PlanAndExecuteMultiAgent" [label="PlanAndExecuteMultiAgent"];
        "EnhancedMultiAgent" -> "PlanAndExecuteMultiAgent";
      }

.. autoclass:: agents.planning.p_and_e.enhanced_multi_agent.PlanAndExecuteMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.planning.p_and_e.enhanced_multi_agent
   :collapse:
   
.. autolink-skip:: next
