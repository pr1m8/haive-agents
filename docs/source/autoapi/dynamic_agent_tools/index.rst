dynamic_agent_tools
===================

.. py:module:: dynamic_agent_tools

.. autoapi-nested-parse::

   Dynamic Agent Management Tools for Supervisor.

   from typing import Any
   This module provides tools that allow the supervisor to dynamically add, remove,
   and manage agents at runtime through tool calls, integrating with DynamicChoiceModel
   for routing and state management.


   .. autolink-examples:: dynamic_agent_tools
      :collapse:


Attributes
----------

.. autoapisummary::

   dynamic_agent_tools.console
   dynamic_agent_tools.logger


Classes
-------

.. autoapisummary::

   dynamic_agent_tools.AddAgentInput
   dynamic_agent_tools.AddAgentTool
   dynamic_agent_tools.AgentDescriptor
   dynamic_agent_tools.AgentRegistryManager
   dynamic_agent_tools.AgentSelectorTool
   dynamic_agent_tools.ChangeAgentInput
   dynamic_agent_tools.ChangeAgentTool
   dynamic_agent_tools.ListAgentsInput
   dynamic_agent_tools.ListAgentsTool
   dynamic_agent_tools.RemoveAgentInput
   dynamic_agent_tools.RemoveAgentTool


Functions
---------

.. autoapisummary::

   dynamic_agent_tools.create_agent_management_tools
   dynamic_agent_tools.register_agent_constructor


Module Contents
---------------

.. py:class:: AddAgentInput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Input for adding a new agent to the supervisor.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AddAgentInput
      :collapse:

   .. py:attribute:: agent_descriptor
      :type:  AgentDescriptor
      :value: None



   .. py:attribute:: rebuild_graph
      :type:  bool
      :value: None



.. py:class:: AddAgentTool(registry_manager: AgentRegistryManager)

   Bases: :py:obj:`langchain_core.tools.BaseTool`


   Tool for dynamically adding agents to the supervisor.

   Initialize the tool.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AddAgentTool
      :collapse:

   .. py:method:: _arun(agent_descriptor: AgentDescriptor, rebuild_graph: bool = True) -> str
      :async:


      Add agent asynchronously.


      .. autolink-examples:: _arun
         :collapse:


   .. py:method:: _run(agent_descriptor: AgentDescriptor, rebuild_graph: bool = True) -> str

      Synchronous version - not implemented for async supervisor.


      .. autolink-examples:: _run
         :collapse:


   .. py:attribute:: args_schema
      :type:  type[pydantic.BaseModel] | None
      :value: None


      Pydantic model class to validate and parse the tool's input arguments.

      Args schema should be either:

      - A subclass of pydantic.BaseModel.
      or
      - A subclass of pydantic.v1.BaseModel if accessing v1 namespace in pydantic 2
      or
      - a JSON schema dict

      .. autolink-examples:: args_schema
         :collapse:


   .. py:attribute:: description
      :type:  str
      :value: Multiline-String

      .. raw:: html

         <details><summary>Show Value</summary>

      .. code-block:: python

         """Add a new agent to the supervisor's registry.
             This allows the supervisor to route requests to the new agent."""

      .. raw:: html

         </details>



      Used to tell the model how/when/why to use the tool.

      You can provide few-shot examples as a part of the description.

      .. autolink-examples:: description
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: 'add_agent'


      The unique name of the tool that clearly communicates its purpose.

      .. autolink-examples:: name
         :collapse:


   .. py:attribute:: registry_manager


.. py:class:: AgentDescriptor(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Descriptor for an agent that can be dynamically added.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgentDescriptor
      :collapse:

   .. py:attribute:: agent_type
      :type:  str
      :value: None



   .. py:attribute:: capability_description
      :type:  str
      :value: None



   .. py:attribute:: config
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: priority
      :type:  int
      :value: None



   .. py:attribute:: tools
      :type:  list[str]
      :value: None



.. py:class:: AgentRegistryManager(supervisor_agent: Any)

   Manages dynamic agent registry with tool integration.

   Initialize with supervisor agent reference.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgentRegistryManager
      :collapse:

   .. py:method:: create_agent_from_descriptor(descriptor: AgentDescriptor) -> haive.agents.base.agent.Agent | None

      Create an agent instance from descriptor.


      .. autolink-examples:: create_agent_from_descriptor
         :collapse:


   .. py:method:: get_agent_choice_model() -> haive.core.common.models.dynamic_choice_model.DynamicChoiceModel[str]

      Get current agent choice model.


      .. autolink-examples:: get_agent_choice_model
         :collapse:


   .. py:method:: register_agent_constructor(agent_type: str, constructor)

      Register an agent constructor function.


      .. autolink-examples:: register_agent_constructor
         :collapse:


   .. py:attribute:: agent_constructors


   .. py:attribute:: choice_model


   .. py:attribute:: supervisor


.. py:class:: AgentSelectorTool(registry_manager: AgentRegistryManager)

   Bases: :py:obj:`langchain_core.tools.BaseTool`


   Tool for selecting which agent to use for the next task.

   Initialize the tool.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgentSelectorTool
      :collapse:

   .. py:method:: _arun(choice: str) -> str
      :async:


      Select agent asynchronously.


      .. autolink-examples:: _arun
         :collapse:


   .. py:method:: _run(choice: str) -> str

      Synchronous version - not implemented for async supervisor.


      .. autolink-examples:: _run
         :collapse:


   .. py:method:: _update_args_schema()

      Update args schema with current agent choices.


      .. autolink-examples:: _update_args_schema
         :collapse:


   .. py:attribute:: args_schema
      :type:  type[pydantic.BaseModel] | None
      :value: None


      Pydantic model class to validate and parse the tool's input arguments.

      Args schema should be either:

      - A subclass of pydantic.BaseModel.
      or
      - A subclass of pydantic.v1.BaseModel if accessing v1 namespace in pydantic 2
      or
      - a JSON schema dict

      .. autolink-examples:: args_schema
         :collapse:


   .. py:attribute:: description
      :type:  str
      :value: Multiline-String

      .. raw:: html

         <details><summary>Show Value</summary>

      .. code-block:: python

         """Select a specific agent to handle the next user request.
             Use this when you want to explicitly route to a particular agent."""

      .. raw:: html

         </details>



      Used to tell the model how/when/why to use the tool.

      You can provide few-shot examples as a part of the description.

      .. autolink-examples:: description
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: 'select_agent'


      The unique name of the tool that clearly communicates its purpose.

      .. autolink-examples:: name
         :collapse:


   .. py:attribute:: registry_manager


.. py:class:: ChangeAgentInput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Input for changing/updating an existing agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ChangeAgentInput
      :collapse:

   .. py:attribute:: agent_name
      :type:  str
      :value: None



   .. py:attribute:: updates
      :type:  dict[str, Any]
      :value: None



.. py:class:: ChangeAgentTool(registry_manager: AgentRegistryManager)

   Bases: :py:obj:`langchain_core.tools.BaseTool`


   Tool for updating agent configuration.

   Initialize the tool.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ChangeAgentTool
      :collapse:

   .. py:method:: _arun(agent_name: str, updates: dict[str, Any]) -> str
      :async:


      Change agent configuration asynchronously.


      .. autolink-examples:: _arun
         :collapse:


   .. py:method:: _run(agent_name: str, updates: dict[str, Any]) -> str

      Synchronous version - not implemented for async supervisor.


      .. autolink-examples:: _run
         :collapse:


   .. py:attribute:: args_schema
      :type:  type[pydantic.BaseModel] | None
      :value: None


      Pydantic model class to validate and parse the tool's input arguments.

      Args schema should be either:

      - A subclass of pydantic.BaseModel.
      or
      - A subclass of pydantic.v1.BaseModel if accessing v1 namespace in pydantic 2
      or
      - a JSON schema dict

      .. autolink-examples:: args_schema
         :collapse:


   .. py:attribute:: description
      :type:  str
      :value: Multiline-String

      .. raw:: html

         <details><summary>Show Value</summary>

      .. code-block:: python

         """Update configuration of an existing agent.
             Can modify priority, timeout, and other execution parameters."""

      .. raw:: html

         </details>



      Used to tell the model how/when/why to use the tool.

      You can provide few-shot examples as a part of the description.

      .. autolink-examples:: description
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: 'change_agent'


      The unique name of the tool that clearly communicates its purpose.

      .. autolink-examples:: name
         :collapse:


   .. py:attribute:: registry_manager


.. py:class:: ListAgentsInput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Input for listing available agents.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ListAgentsInput
      :collapse:

   .. py:attribute:: include_performance
      :type:  bool
      :value: None



.. py:class:: ListAgentsTool(registry_manager: AgentRegistryManager)

   Bases: :py:obj:`langchain_core.tools.BaseTool`


   Tool for listing available agents and their capabilities.

   Initialize the tool.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ListAgentsTool
      :collapse:

   .. py:method:: _arun(include_performance: bool = True) -> str
      :async:


      List agents asynchronously.


      .. autolink-examples:: _arun
         :collapse:


   .. py:method:: _run(include_performance: bool = True) -> str

      Synchronous version - not implemented for async supervisor.


      .. autolink-examples:: _run
         :collapse:


   .. py:attribute:: args_schema
      :type:  type[pydantic.BaseModel] | None
      :value: None


      Pydantic model class to validate and parse the tool's input arguments.

      Args schema should be either:

      - A subclass of pydantic.BaseModel.
      or
      - A subclass of pydantic.v1.BaseModel if accessing v1 namespace in pydantic 2
      or
      - a JSON schema dict

      .. autolink-examples:: args_schema
         :collapse:


   .. py:attribute:: description
      :type:  str
      :value: Multiline-String

      .. raw:: html

         <details><summary>Show Value</summary>

      .. code-block:: python

         """List all available agents in the supervisor registry
             with their capabilities and performance metrics."""

      .. raw:: html

         </details>



      Used to tell the model how/when/why to use the tool.

      You can provide few-shot examples as a part of the description.

      .. autolink-examples:: description
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: 'list_agents'


      The unique name of the tool that clearly communicates its purpose.

      .. autolink-examples:: name
         :collapse:


   .. py:attribute:: registry_manager


.. py:class:: RemoveAgentInput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Input for removing an agent from the supervisor.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RemoveAgentInput
      :collapse:

   .. py:attribute:: agent_name
      :type:  str
      :value: None



   .. py:attribute:: rebuild_graph
      :type:  bool
      :value: None



.. py:class:: RemoveAgentTool(registry_manager: AgentRegistryManager)

   Bases: :py:obj:`langchain_core.tools.BaseTool`


   Tool for dynamically removing agents from the supervisor.

   Initialize the tool.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RemoveAgentTool
      :collapse:

   .. py:method:: _arun(agent_name: str, rebuild_graph: bool = True) -> str
      :async:


      Remove agent asynchronously.


      .. autolink-examples:: _arun
         :collapse:


   .. py:method:: _run(agent_name: str, rebuild_graph: bool = True) -> str

      Synchronous version - not implemented for async supervisor.


      .. autolink-examples:: _run
         :collapse:


   .. py:attribute:: args_schema
      :type:  type[pydantic.BaseModel] | None
      :value: None


      Pydantic model class to validate and parse the tool's input arguments.

      Args schema should be either:

      - A subclass of pydantic.BaseModel.
      or
      - A subclass of pydantic.v1.BaseModel if accessing v1 namespace in pydantic 2
      or
      - a JSON schema dict

      .. autolink-examples:: args_schema
         :collapse:


   .. py:attribute:: description
      :type:  str
      :value: Multiline-String

      .. raw:: html

         <details><summary>Show Value</summary>

      .. code-block:: python

         """Remove an agent from the supervisor's registry.
             The agent will no longer be available for routing."""

      .. raw:: html

         </details>



      Used to tell the model how/when/why to use the tool.

      You can provide few-shot examples as a part of the description.

      .. autolink-examples:: description
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: 'remove_agent'


      The unique name of the tool that clearly communicates its purpose.

      .. autolink-examples:: name
         :collapse:


   .. py:attribute:: registry_manager


.. py:function:: create_agent_management_tools(supervisor_agent: Any) -> list[langchain_core.tools.BaseTool]

   Create all agent management tools for a supervisor.


   .. autolink-examples:: create_agent_management_tools
      :collapse:

.. py:function:: register_agent_constructor(supervisor_agent: Any, agent_type: str, constructor)

   Register an agent constructor with the supervisor's registry manager.


   .. autolink-examples:: register_agent_constructor
      :collapse:

.. py:data:: console

.. py:data:: logger

