
:py:mod:`enhanced_multi_agent_v3`
=================================

.. py:module:: enhanced_multi_agent_v3

Enhanced MultiAgent V3 - Full feature implementation using enhanced base Agent.

This version combines the best features from clean.py and enhanced_multi_agent_standalone.py:
- Production-ready coordination from clean.py
- Generic typing and performance features from standalone
- Full integration with enhanced base Agent class
- V3 pattern consistency with SimpleAgent V3 and ReactAgent V3

Key Features:
- Generic typing: MultiAgent[AgentsT] for type safety
- Performance tracking and adaptive routing
- Rich debugging and observability like other V3 agents
- Multi-engine coordination capabilities
- Comprehensive persistence and state management
- Backward compatibility with existing patterns


.. autolink-examples:: enhanced_multi_agent_v3
   :collapse:

Classes
-------

.. autoapisummary::

   enhanced_multi_agent_v3.EnhancedMultiAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnhancedMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_EnhancedMultiAgent {
        node [shape=record];
        "EnhancedMultiAgent" [label="EnhancedMultiAgent"];
        "haive.agents.base.agent.Agent" -> "EnhancedMultiAgent";
        "Generic[AgentsT]" -> "EnhancedMultiAgent";
      }

.. autoclass:: enhanced_multi_agent_v3.EnhancedMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: enhanced_multi_agent_v3
   :collapse:
   
.. autolink-skip:: next
