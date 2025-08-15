agents.experiments.supervisor.tools
===================================

.. py:module:: agents.experiments.supervisor.tools

.. autoapi-nested-parse::

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


Functions
---------

.. autoapisummary::

   agents.experiments.supervisor.tools.build_supervisor_tools
   agents.experiments.supervisor.tools.create_agent_creation_tool
   agents.experiments.supervisor.tools.create_execution_status_tool
   agents.experiments.supervisor.tools.create_list_agents_tool
   agents.experiments.supervisor.tools.create_supervisor_handoff_tool
   agents.experiments.supervisor.tools.sync_tools_with_state


Module Contents
---------------

.. py:class:: AgentCreationInput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Input model for agent creation tool.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgentCreationInput
      :collapse:

   .. py:attribute:: agent_type
      :type:  str
      :value: None



   .. py:attribute:: config
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



.. py:class:: AgentHandoffInput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Input model for agent handoff tool.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgentHandoffInput
      :collapse:

   .. py:attribute:: agent_name
      :type:  str
      :value: None



   .. py:attribute:: context
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: task
      :type:  str
      :value: None



.. py:class:: ListAgentsInput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Input model for listing agents.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ListAgentsInput
      :collapse:

   .. py:attribute:: filter_by_type
      :type:  str | None
      :value: None



   .. py:attribute:: include_inactive
      :type:  bool
      :value: None



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

