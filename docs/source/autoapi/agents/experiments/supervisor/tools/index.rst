
:py:mod:`agents.experiments.supervisor.tools`
=============================================

.. py:module:: agents.experiments.supervisor.tools

Tools for supervisor agents.

This module provides the tools that supervisor agents can use to manage
other agents, delegate tasks, and coordinate multi-agent workflows.


.. autolink-examples:: agents.experiments.supervisor.tools
   :collapse:

Classes
-------

.. autoapisummary::

   agents.experiments.supervisor.tools.AgentCreationInput
   agents.experiments.supervisor.tools.AgentHandoffInput
   agents.experiments.supervisor.tools.ListAgentsInput


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgentCreationInput:

   .. graphviz::
      :align: center

      digraph inheritance_AgentCreationInput {
        node [shape=record];
        "AgentCreationInput" [label="AgentCreationInput"];
        "pydantic.BaseModel" -> "AgentCreationInput";
      }

.. autopydantic_model:: agents.experiments.supervisor.tools.AgentCreationInput
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

   Inheritance diagram for AgentHandoffInput:

   .. graphviz::
      :align: center

      digraph inheritance_AgentHandoffInput {
        node [shape=record];
        "AgentHandoffInput" [label="AgentHandoffInput"];
        "pydantic.BaseModel" -> "AgentHandoffInput";
      }

.. autopydantic_model:: agents.experiments.supervisor.tools.AgentHandoffInput
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

   Inheritance diagram for ListAgentsInput:

   .. graphviz::
      :align: center

      digraph inheritance_ListAgentsInput {
        node [shape=record];
        "ListAgentsInput" [label="ListAgentsInput"];
        "pydantic.BaseModel" -> "ListAgentsInput";
      }

.. autopydantic_model:: agents.experiments.supervisor.tools.ListAgentsInput
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



Functions
---------

.. autoapisummary::

   agents.experiments.supervisor.tools.build_supervisor_tools
   agents.experiments.supervisor.tools.create_agent_creation_tool
   agents.experiments.supervisor.tools.create_execution_status_tool
   agents.experiments.supervisor.tools.create_list_agents_tool
   agents.experiments.supervisor.tools.create_supervisor_handoff_tool
   agents.experiments.supervisor.tools.sync_tools_with_state

.. py:function:: build_supervisor_tools(supervisor) -> list[langchain_core.tools.Tool]

   Build all standard supervisor tools.

   :param supervisor: The supervisor instance

   :returns: List of supervisor tools


   .. autolink-examples:: build_supervisor_tools
      :collapse:

.. py:function:: create_agent_creation_tool(supervisor) -> langchain_core.tools.Tool

   Create a tool for dynamic agent creation.

   :param supervisor: The supervisor instance (must support dynamic creation)

   :returns: Tool for creating new agents


   .. autolink-examples:: create_agent_creation_tool
      :collapse:

.. py:function:: create_execution_status_tool(supervisor) -> langchain_core.tools.Tool

   Create a tool for checking execution status.

   :param supervisor: The supervisor instance

   :returns: Tool for checking execution status


   .. autolink-examples:: create_execution_status_tool
      :collapse:

.. py:function:: create_list_agents_tool(supervisor) -> langchain_core.tools.Tool

   Create a tool for listing available agents.

   :param supervisor: The supervisor instance

   :returns: Tool for listing agents


   .. autolink-examples:: create_list_agents_tool
      :collapse:

.. py:function:: create_supervisor_handoff_tool(supervisor) -> langchain_core.tools.Tool

   Create a tool for delegating tasks to agents.

   :param supervisor: The supervisor instance

   :returns: Tool for agent task delegation


   .. autolink-examples:: create_supervisor_handoff_tool
      :collapse:

.. py:function:: sync_tools_with_state(supervisor, tools: list[langchain_core.tools.Tool]) -> None

   Synchronize tools with supervisor state.

   This function updates the supervisor's tool mappings based on available tools.

   :param supervisor: The supervisor instance
   :param tools: List of tools to synchronize


   .. autolink-examples:: sync_tools_with_state
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.experiments.supervisor.tools
   :collapse:
   
.. autolink-skip:: next
