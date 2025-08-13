
:py:mod:`agent`
===============

.. py:module:: agent

Core Multi-Agent implementation.

This module provides the main MultiAgent class that serves as the foundation
for all multi-agent systems in Haive. It combines multiple agents and coordinates
their execution with various modes and strategies.


.. autolink-examples:: agent
   :collapse:

Classes
-------

.. autoapisummary::

   agent.ExecutionMode
   agent.MultiAgent
   agent.MultiAgentConfig
   agent.MultiAgentState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ExecutionMode:

   .. graphviz::
      :align: center

      digraph inheritance_ExecutionMode {
        node [shape=record];
        "ExecutionMode" [label="ExecutionMode"];
        "str" -> "ExecutionMode";
        "enum.Enum" -> "ExecutionMode";
      }

.. autoclass:: agent.ExecutionMode
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ExecutionMode** is an Enum defined in ``agent``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_MultiAgent {
        node [shape=record];
        "MultiAgent" [label="MultiAgent"];
        "haive.core.engine.agent.Agent" -> "MultiAgent";
      }

.. autoclass:: agent.MultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_MultiAgentConfig {
        node [shape=record];
        "MultiAgentConfig" [label="MultiAgentConfig"];
        "haive.core.engine.agent.AgentConfig" -> "MultiAgentConfig";
      }

.. autoclass:: agent.MultiAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiAgentState:

   .. graphviz::
      :align: center

      digraph inheritance_MultiAgentState {
        node [shape=record];
        "MultiAgentState" [label="MultiAgentState"];
        "haive.core.schema.state_schema.StateSchema" -> "MultiAgentState";
      }

.. autoclass:: agent.MultiAgentState
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agent.create_hierarchical_multi_agent
   agent.create_parallel_multi_agent
   agent.create_sequential_multi_agent

.. py:function:: create_hierarchical_multi_agent(supervisor: haive.core.engine.agent.Agent, subordinates: list[haive.core.engine.agent.Agent], name: str = 'hierarchical_multi_agent') -> MultiAgent

   Create a hierarchical multi-agent system.


   .. autolink-examples:: create_hierarchical_multi_agent
      :collapse:

.. py:function:: create_parallel_multi_agent(agents: list[haive.core.engine.agent.Agent], name: str = 'parallel_multi_agent') -> MultiAgent

   Create a parallel multi-agent system.


   .. autolink-examples:: create_parallel_multi_agent
      :collapse:

.. py:function:: create_sequential_multi_agent(agents: list[haive.core.engine.agent.Agent], name: str = 'sequential_multi_agent') -> MultiAgent

   Create a sequential multi-agent system.


   .. autolink-examples:: create_sequential_multi_agent
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agent
   :collapse:
   
.. autolink-skip:: next
