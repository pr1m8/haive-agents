
:py:mod:`multi_agent_v4`
========================

.. py:module:: multi_agent_v4

MultiAgent V4 - Clean implementation using enhanced base agent.

This implementation follows the V4 pattern with:
- Enhanced base agent integration
- MultiAgentState usage
- AgentNodeV3 execution
- Simple list initialization
- Incremental build-up approach

Start small, test incrementally, build up features.


.. autolink-examples:: multi_agent_v4
   :collapse:

Classes
-------

.. autoapisummary::

   multi_agent_v4.MultiAgentV4


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiAgentV4:

   .. graphviz::
      :align: center

      digraph inheritance_MultiAgentV4 {
        node [shape=record];
        "MultiAgentV4" [label="MultiAgentV4"];
        "haive.agents.base.agent.Agent" -> "MultiAgentV4";
      }

.. autoclass:: multi_agent_v4.MultiAgentV4
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: multi_agent_v4
   :collapse:
   
.. autolink-skip:: next
