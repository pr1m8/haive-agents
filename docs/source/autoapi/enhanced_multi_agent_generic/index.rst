
:py:mod:`enhanced_multi_agent_generic`
======================================

.. py:module:: enhanced_multi_agent_generic

Enhanced MultiAgent with proper generics for contained agents (Experimental).

**Current Status**: This is an **experimental implementation** exploring advanced
generic typing patterns for multi-agent systems. It provides type-safe agent
collections with specialized variants like BranchingMultiAgent and AdaptiveBranchingMultiAgent.

For production use, consider:
- **MultiAgent** (default): Stable production implementation
- **MultiAgent**: Recommended for new projects
- **EnhancedMultiAgent** (V3): For generic typing with more features

This implementation explores the pattern: MultiAgent[AgentsT] where AgentsT
represents the type of agents it contains, enabling compile-time type safety
for agent collections.


.. autolink-examples:: enhanced_multi_agent_generic
   :collapse:

Classes
-------

.. autoapisummary::

   enhanced_multi_agent_generic.AdaptiveBranchingMultiAgent
   enhanced_multi_agent_generic.BranchingMultiAgent
   enhanced_multi_agent_generic.ConditionalMultiAgent
   enhanced_multi_agent_generic.MultiAgent
   enhanced_multi_agent_generic.ReportTeamAgents


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AdaptiveBranchingMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_AdaptiveBranchingMultiAgent {
        node [shape=record];
        "AdaptiveBranchingMultiAgent" [label="AdaptiveBranchingMultiAgent"];
        "BranchingMultiAgent" -> "AdaptiveBranchingMultiAgent";
      }

.. autoclass:: enhanced_multi_agent_generic.AdaptiveBranchingMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BranchingMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_BranchingMultiAgent {
        node [shape=record];
        "BranchingMultiAgent" [label="BranchingMultiAgent"];
        "MultiAgent[dict[str, Agent]]" -> "BranchingMultiAgent";
      }

.. autoclass:: enhanced_multi_agent_generic.BranchingMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ConditionalMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ConditionalMultiAgent {
        node [shape=record];
        "ConditionalMultiAgent" [label="ConditionalMultiAgent"];
        "MultiAgent[dict[str, Agent]]" -> "ConditionalMultiAgent";
      }

.. autoclass:: enhanced_multi_agent_generic.ConditionalMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_MultiAgent {
        node [shape=record];
        "MultiAgent" [label="MultiAgent"];
        "Agent" -> "MultiAgent";
        "Generic[AgentsT]" -> "MultiAgent";
      }

.. autoclass:: enhanced_multi_agent_generic.MultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReportTeamAgents:

   .. graphviz::
      :align: center

      digraph inheritance_ReportTeamAgents {
        node [shape=record];
        "ReportTeamAgents" [label="ReportTeamAgents"];
        "TypedDict" -> "ReportTeamAgents";
      }

.. autoclass:: enhanced_multi_agent_generic.ReportTeamAgents
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: enhanced_multi_agent_generic
   :collapse:
   
.. autolink-skip:: next
