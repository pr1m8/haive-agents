
:py:mod:`enhanced_agent_v3`
===========================

.. py:module:: enhanced_agent_v3

Enhanced ReactAgent V3 - Full ReAct implementation with advanced features.

This version combines the ReAct (Reasoning and Acting) pattern with all enhanced
capabilities from the base Agent class and EnhancedSimpleAgent.

Key Features:
- Complete ReAct reasoning and action loop
- Advanced tool integration and routing
- Intelligent loop control and termination
- Rich execution tracking and debugging
- Performance optimizations for iterative workflows


.. autolink-examples:: enhanced_agent_v3
   :collapse:

Classes
-------

.. autoapisummary::

   enhanced_agent_v3.EnhancedReactAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnhancedReactAgent:

   .. graphviz::
      :align: center

      digraph inheritance_EnhancedReactAgent {
        node [shape=record];
        "EnhancedReactAgent" [label="EnhancedReactAgent"];
        "haive.agents.simple.enhanced_agent_v3.EnhancedSimpleAgent" -> "EnhancedReactAgent";
      }

.. autoclass:: enhanced_agent_v3.EnhancedReactAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: enhanced_agent_v3
   :collapse:
   
.. autolink-skip:: next
