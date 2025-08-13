
:py:mod:`clean_multi_agent`
===========================

.. py:module:: clean_multi_agent

Clean Multi-Agent Implementation using AgentNodeV3.

from typing import Any, Dict
This module provides a clean multi-agent system that:
- Uses AgentNodeV3 for proper state projection
- Emulates the engines dict pattern from base Agent
- Supports private state passing between agents
- Maintains type safety without schema flattening


.. autolink-examples:: clean_multi_agent
   :collapse:

Classes
-------

.. autoapisummary::

   clean_multi_agent.ConditionalAgent
   clean_multi_agent.ContainerMultiAgentState
   clean_multi_agent.MinimalMultiAgentState
   clean_multi_agent.MultiAgent
   clean_multi_agent.SequentialAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ConditionalAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ConditionalAgent {
        node [shape=record];
        "ConditionalAgent" [label="ConditionalAgent"];
        "MultiAgent" -> "ConditionalAgent";
      }

.. autoclass:: clean_multi_agent.ConditionalAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ContainerMultiAgentState:

   .. graphviz::
      :align: center

      digraph inheritance_ContainerMultiAgentState {
        node [shape=record];
        "ContainerMultiAgentState" [label="ContainerMultiAgentState"];
        "haive.core.schema.state_schema.StateSchema" -> "ContainerMultiAgentState";
      }

.. autoclass:: clean_multi_agent.ContainerMultiAgentState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MinimalMultiAgentState:

   .. graphviz::
      :align: center

      digraph inheritance_MinimalMultiAgentState {
        node [shape=record];
        "MinimalMultiAgentState" [label="MinimalMultiAgentState"];
        "typing_extensions.TypedDict" -> "MinimalMultiAgentState";
      }

.. autoclass:: clean_multi_agent.MinimalMultiAgentState
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
        "haive.agents.base.agent.Agent" -> "MultiAgent";
      }

.. autoclass:: clean_multi_agent.MultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SequentialAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SequentialAgent {
        node [shape=record];
        "SequentialAgent" [label="SequentialAgent"];
        "MultiAgent" -> "SequentialAgent";
      }

.. autoclass:: clean_multi_agent.SequentialAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: clean_multi_agent
   :collapse:
   
.. autolink-skip:: next
