
:py:mod:`agents.supervisor.dynamic.dynamic_agent_tools`
=======================================================

.. py:module:: agents.supervisor.dynamic.dynamic_agent_tools

Dynamic Agent Management Tools for Supervisor.

from typing import Any, Optional
This module provides tools that allow the supervisor to dynamically add, remove,
and manage agents at runtime through tool calls, integrating with DynamicChoiceModel
for routing and state management.


.. autolink-examples:: agents.supervisor.dynamic.dynamic_agent_tools
   :collapse:

Classes
-------

.. autoapisummary::

   agents.supervisor.dynamic.dynamic_agent_tools.AddAgentInput
   agents.supervisor.dynamic.dynamic_agent_tools.AddAgentTool
   agents.supervisor.dynamic.dynamic_agent_tools.AgentDescriptor
   agents.supervisor.dynamic.dynamic_agent_tools.AgentRegistryManager
   agents.supervisor.dynamic.dynamic_agent_tools.AgentSelectorTool
   agents.supervisor.dynamic.dynamic_agent_tools.ChangeAgentInput
   agents.supervisor.dynamic.dynamic_agent_tools.ChangeAgentTool
   agents.supervisor.dynamic.dynamic_agent_tools.ListAgentsInput
   agents.supervisor.dynamic.dynamic_agent_tools.ListAgentsTool
   agents.supervisor.dynamic.dynamic_agent_tools.RemoveAgentInput
   agents.supervisor.dynamic.dynamic_agent_tools.RemoveAgentTool


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AddAgentInput:

   .. graphviz::
      :align: center

      digraph inheritance_AddAgentInput {
        node [shape=record];
        "AddAgentInput" [label="AddAgentInput"];
        "pydantic.BaseModel" -> "AddAgentInput";
      }

.. autopydantic_model:: agents.supervisor.dynamic.dynamic_agent_tools.AddAgentInput
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

   Inheritance diagram for AddAgentTool:

   .. graphviz::
      :align: center

      digraph inheritance_AddAgentTool {
        node [shape=record];
        "AddAgentTool" [label="AddAgentTool"];
        "langchain_core.tools.BaseTool" -> "AddAgentTool";
      }

.. autoclass:: agents.supervisor.dynamic.dynamic_agent_tools.AddAgentTool
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgentDescriptor:

   .. graphviz::
      :align: center

      digraph inheritance_AgentDescriptor {
        node [shape=record];
        "AgentDescriptor" [label="AgentDescriptor"];
        "pydantic.BaseModel" -> "AgentDescriptor";
      }

.. autopydantic_model:: agents.supervisor.dynamic.dynamic_agent_tools.AgentDescriptor
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

   Inheritance diagram for AgentRegistryManager:

   .. graphviz::
      :align: center

      digraph inheritance_AgentRegistryManager {
        node [shape=record];
        "AgentRegistryManager" [label="AgentRegistryManager"];
      }

.. autoclass:: agents.supervisor.dynamic.dynamic_agent_tools.AgentRegistryManager
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgentSelectorTool:

   .. graphviz::
      :align: center

      digraph inheritance_AgentSelectorTool {
        node [shape=record];
        "AgentSelectorTool" [label="AgentSelectorTool"];
        "langchain_core.tools.BaseTool" -> "AgentSelectorTool";
      }

.. autoclass:: agents.supervisor.dynamic.dynamic_agent_tools.AgentSelectorTool
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ChangeAgentInput:

   .. graphviz::
      :align: center

      digraph inheritance_ChangeAgentInput {
        node [shape=record];
        "ChangeAgentInput" [label="ChangeAgentInput"];
        "pydantic.BaseModel" -> "ChangeAgentInput";
      }

.. autopydantic_model:: agents.supervisor.dynamic.dynamic_agent_tools.ChangeAgentInput
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

   Inheritance diagram for ChangeAgentTool:

   .. graphviz::
      :align: center

      digraph inheritance_ChangeAgentTool {
        node [shape=record];
        "ChangeAgentTool" [label="ChangeAgentTool"];
        "langchain_core.tools.BaseTool" -> "ChangeAgentTool";
      }

.. autoclass:: agents.supervisor.dynamic.dynamic_agent_tools.ChangeAgentTool
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ListAgentsInput:

   .. graphviz::
      :align: center

      digraph inheritance_ListAgentsInput {
        node [shape=record];
        "ListAgentsInput" [label="ListAgentsInput"];
        "pydantic.BaseModel" -> "ListAgentsInput";
      }

.. autopydantic_model:: agents.supervisor.dynamic.dynamic_agent_tools.ListAgentsInput
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

   Inheritance diagram for ListAgentsTool:

   .. graphviz::
      :align: center

      digraph inheritance_ListAgentsTool {
        node [shape=record];
        "ListAgentsTool" [label="ListAgentsTool"];
        "langchain_core.tools.BaseTool" -> "ListAgentsTool";
      }

.. autoclass:: agents.supervisor.dynamic.dynamic_agent_tools.ListAgentsTool
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RemoveAgentInput:

   .. graphviz::
      :align: center

      digraph inheritance_RemoveAgentInput {
        node [shape=record];
        "RemoveAgentInput" [label="RemoveAgentInput"];
        "pydantic.BaseModel" -> "RemoveAgentInput";
      }

.. autopydantic_model:: agents.supervisor.dynamic.dynamic_agent_tools.RemoveAgentInput
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

   Inheritance diagram for RemoveAgentTool:

   .. graphviz::
      :align: center

      digraph inheritance_RemoveAgentTool {
        node [shape=record];
        "RemoveAgentTool" [label="RemoveAgentTool"];
        "langchain_core.tools.BaseTool" -> "RemoveAgentTool";
      }

.. autoclass:: agents.supervisor.dynamic.dynamic_agent_tools.RemoveAgentTool
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.supervisor.dynamic.dynamic_agent_tools.create_agent_management_tools
   agents.supervisor.dynamic.dynamic_agent_tools.register_agent_constructor

.. py:function:: create_agent_management_tools(supervisor_agent: Any) -> list[langchain_core.tools.BaseTool]

   Create all agent management tools for a supervisor.


   .. autolink-examples:: create_agent_management_tools
      :collapse:

.. py:function:: register_agent_constructor(supervisor_agent: Any, agent_type: str, constructor)

   Register an agent constructor with the supervisor's registry manager.


   .. autolink-examples:: register_agent_constructor
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.supervisor.dynamic.dynamic_agent_tools
   :collapse:
   
.. autolink-skip:: next
