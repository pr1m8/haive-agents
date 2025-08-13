
:py:mod:`proper_list_multi_agent`
=================================

.. py:module:: proper_list_multi_agent

Proper list multi-agent that uses MultiAgentState and AgentNodeV3.

from typing import Any
This implementation properly leverages the existing infrastructure:
- MultiAgentState for proper state management
- AgentNodeV3 for agent execution with state projection
- create_agent_node_v3 for creating agent nodes
- Proper engine syncing and recompilation tracking


.. autolink-examples:: proper_list_multi_agent
   :collapse:

Classes
-------

.. autoapisummary::

   proper_list_multi_agent.MetaListMultiAgent
   proper_list_multi_agent.ProperListMultiAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MetaListMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_MetaListMultiAgent {
        node [shape=record];
        "MetaListMultiAgent" [label="MetaListMultiAgent"];
        "haive.agents.base.agent.Agent" -> "MetaListMultiAgent";
        "haive.core.common.mixins.recompile_mixin.RecompileMixin" -> "MetaListMultiAgent";
        "collections.abc.Sequence[haive.agents.base.agent.Agent]" -> "MetaListMultiAgent";
      }

.. autoclass:: proper_list_multi_agent.MetaListMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ProperListMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ProperListMultiAgent {
        node [shape=record];
        "ProperListMultiAgent" [label="ProperListMultiAgent"];
        "haive.agents.base.agent.Agent" -> "ProperListMultiAgent";
        "haive.core.common.mixins.recompile_mixin.RecompileMixin" -> "ProperListMultiAgent";
        "collections.abc.Sequence[haive.agents.base.agent.Agent]" -> "ProperListMultiAgent";
      }

.. autoclass:: proper_list_multi_agent.ProperListMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   proper_list_multi_agent.meta_multi
   proper_list_multi_agent.sequential_multi

.. py:function:: meta_multi(*agents: haive.agents.base.agent.Agent, name: str = 'meta_multi') -> MetaListMultiAgent

   Create a meta multi-agent.


   .. autolink-examples:: meta_multi
      :collapse:

.. py:function:: sequential_multi(*agents: haive.agents.base.agent.Agent, name: str = 'sequential_multi') -> ProperListMultiAgent

   Create a sequential multi-agent.


   .. autolink-examples:: sequential_multi
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: proper_list_multi_agent
   :collapse:
   
.. autolink-skip:: next
