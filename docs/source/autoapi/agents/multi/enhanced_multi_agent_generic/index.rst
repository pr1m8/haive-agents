
:py:mod:`agents.multi.enhanced_multi_agent_generic`
===================================================

.. py:module:: agents.multi.enhanced_multi_agent_generic

Enhanced MultiAgent with proper generics for contained agents.

MultiAgent[AgentsT] where AgentsT represents the agents it contains.


.. autolink-examples:: agents.multi.enhanced_multi_agent_generic
   :collapse:

Classes
-------

.. autoapisummary::

   agents.multi.enhanced_multi_agent_generic.AdaptiveBranchingMultiAgent
   agents.multi.enhanced_multi_agent_generic.BranchingMultiAgent
   agents.multi.enhanced_multi_agent_generic.ConditionalMultiAgent
   agents.multi.enhanced_multi_agent_generic.MultiAgent
   agents.multi.enhanced_multi_agent_generic.ReportTeamAgents


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

.. autoclass:: agents.multi.enhanced_multi_agent_generic.AdaptiveBranchingMultiAgent
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

.. autoclass:: agents.multi.enhanced_multi_agent_generic.BranchingMultiAgent
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

.. autoclass:: agents.multi.enhanced_multi_agent_generic.ConditionalMultiAgent
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

.. autoclass:: agents.multi.enhanced_multi_agent_generic.MultiAgent
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

.. autoclass:: agents.multi.enhanced_multi_agent_generic.ReportTeamAgents
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.multi.enhanced_multi_agent_generic
   :collapse:
   
.. autolink-skip:: next
