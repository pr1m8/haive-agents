
:py:mod:`agents.experiments.dynamic_supervisor`
===============================================

.. py:module:: agents.experiments.dynamic_supervisor

Dynamic Supervisor Agent Experiment.

from typing import Any
This module contains experimental implementation of a dynamic supervisor
that can select and execute agents based on runtime decisions.


.. autolink-examples:: agents.experiments.dynamic_supervisor
   :collapse:

Classes
-------

.. autoapisummary::

   agents.experiments.dynamic_supervisor.AgentRegistry
   agents.experiments.dynamic_supervisor.AgentRegistryEntry
   agents.experiments.dynamic_supervisor.DynamicSupervisorAgent
   agents.experiments.dynamic_supervisor.SupervisorState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgentRegistry:

   .. graphviz::
      :align: center

      digraph inheritance_AgentRegistry {
        node [shape=record];
        "AgentRegistry" [label="AgentRegistry"];
      }

.. autoclass:: agents.experiments.dynamic_supervisor.AgentRegistry
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgentRegistryEntry:

   .. graphviz::
      :align: center

      digraph inheritance_AgentRegistryEntry {
        node [shape=record];
        "AgentRegistryEntry" [label="AgentRegistryEntry"];
        "pydantic.BaseModel" -> "AgentRegistryEntry";
      }

.. autopydantic_model:: agents.experiments.dynamic_supervisor.AgentRegistryEntry
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DynamicSupervisorAgent:

   .. graphviz::
      :align: center

      digraph inheritance_DynamicSupervisorAgent {
        node [shape=record];
        "DynamicSupervisorAgent" [label="DynamicSupervisorAgent"];
        "haive.agents.react.agent.ReactAgent" -> "DynamicSupervisorAgent";
      }

.. autoclass:: agents.experiments.dynamic_supervisor.DynamicSupervisorAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SupervisorState:

   .. graphviz::
      :align: center

      digraph inheritance_SupervisorState {
        node [shape=record];
        "SupervisorState" [label="SupervisorState"];
        "haive.core.schema.prebuilt.messages_state.MessagesState" -> "SupervisorState";
      }

.. autoclass:: agents.experiments.dynamic_supervisor.SupervisorState
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.experiments.dynamic_supervisor.create_dynamic_handoff_tool
   agents.experiments.dynamic_supervisor.create_forward_message_tool
   agents.experiments.dynamic_supervisor.create_list_agents_tool
   agents.experiments.dynamic_supervisor.create_test_registry
   agents.experiments.dynamic_supervisor.test_dynamic_tools
   agents.experiments.dynamic_supervisor.test_supervisor_basic
   agents.experiments.dynamic_supervisor.test_supervisor_workflow

.. py:function:: create_dynamic_handoff_tool(supervisor_instance, agent_name: str)

   Create a handoff tool for a specific agent.


   .. autolink-examples:: create_dynamic_handoff_tool
      :collapse:

.. py:function:: create_forward_message_tool(supervisor_name: str = 'supervisor')

   Create a tool to forward agent messages.


   .. autolink-examples:: create_forward_message_tool
      :collapse:

.. py:function:: create_list_agents_tool(supervisor_instance) -> Any

   Create a tool to list available agents.


   .. autolink-examples:: create_list_agents_tool
      :collapse:

.. py:function:: create_test_registry() -> AgentRegistry

   Create a test registry with some mock agents.


   .. autolink-examples:: create_test_registry
      :collapse:

.. py:function:: test_dynamic_tools() -> Any

   Test dynamic tool creation and handoff functionality.


   .. autolink-examples:: test_dynamic_tools
      :collapse:

.. py:function:: test_supervisor_basic() -> Any

   Basic test of supervisor functionality.


   .. autolink-examples:: test_supervisor_basic
      :collapse:

.. py:function:: test_supervisor_workflow() -> Any

   Test a complete supervisor workflow.


   .. autolink-examples:: test_supervisor_workflow
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.experiments.dynamic_supervisor
   :collapse:
   
.. autolink-skip:: next
