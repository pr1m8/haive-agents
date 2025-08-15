agents.experiments.dynamic_supervisor
=====================================

.. py:module:: agents.experiments.dynamic_supervisor

.. autoapi-nested-parse::

   Dynamic Supervisor Agent Experiment.

   from typing import Any
   This module contains experimental implementation of a dynamic supervisor
   that can select and execute agents based on runtime decisions.


   .. autolink-examples:: agents.experiments.dynamic_supervisor
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.experiments.dynamic_supervisor.logger
   agents.experiments.dynamic_supervisor.supervisor


Classes
-------

.. autoapisummary::

   agents.experiments.dynamic_supervisor.AgentRegistry
   agents.experiments.dynamic_supervisor.AgentRegistryEntry
   agents.experiments.dynamic_supervisor.DynamicSupervisorAgent
   agents.experiments.dynamic_supervisor.SupervisorState


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


Module Contents
---------------

.. py:class:: AgentRegistry

   Registry for managing available agents.


   .. autolink-examples:: AgentRegistry
      :collapse:

   .. py:method:: instantiate_agent(name: str) -> haive.agents.base.agent.Agent | None

      Instantiate an agent from the registry.


      .. autolink-examples:: instantiate_agent
         :collapse:


   .. py:method:: list_agents() -> dict[str, dict[str, Any]]

      List all registered agents with their metadata.


      .. autolink-examples:: list_agents
         :collapse:


   .. py:method:: register(name: str, description: str, agent_class: type[haive.agents.base.agent.Agent], config: dict[str, Any] | None = None, capabilities: list[str] | None = None) -> None

      Register an agent with the registry.


      .. autolink-examples:: register
         :collapse:


   .. py:method:: to_state_format() -> dict[str, dict[str, Any]]

      Convert registry to format suitable for SupervisorState.


      .. autolink-examples:: to_state_format
         :collapse:


   .. py:method:: unregister(name: str) -> None

      Remove an agent from the registry.


      .. autolink-examples:: unregister
         :collapse:


   .. py:attribute:: _instances
      :type:  dict[str, haive.agents.base.agent.Agent]


   .. py:attribute:: _registry
      :type:  dict[str, AgentRegistryEntry]


.. py:class:: AgentRegistryEntry(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Registry entry for an agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgentRegistryEntry
      :collapse:

   .. py:attribute:: agent_class
      :type:  type[haive.agents.base.agent.Agent]
      :value: None



   .. py:attribute:: capabilities
      :type:  list[str]
      :value: None



   .. py:attribute:: config
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: None



.. py:class:: DynamicSupervisorAgent

   Bases: :py:obj:`haive.agents.react.agent.ReactAgent`


   Dynamic supervisor that selects and executes agents at runtime.

   This agent inherits from ReactAgent to get the looping behavior needed
   for continuous agent selection and execution. It dynamically creates
   handoff tools for each agent in the registry.


   .. autolink-examples:: DynamicSupervisorAgent
      :collapse:

   .. py:method:: _create_dynamic_tools()

      Create tools dynamically based on agent registry.


      .. autolink-examples:: _create_dynamic_tools
         :collapse:


   .. py:method:: _create_end_supervision_tool()

      Create tool for ending supervision.


      .. autolink-examples:: _create_end_supervision_tool
         :collapse:


   .. py:method:: _create_system_message()

      Create system message with available agents.


      .. autolink-examples:: _create_system_message
         :collapse:


   .. py:method:: _prepare_input(input_data: Any) -> Any

      Prepare input data and sync registry to state.


      .. autolink-examples:: _prepare_input
         :collapse:


   .. py:method:: _sync_registry_to_state()

      Sync agent registry to state format.


      .. autolink-examples:: _sync_registry_to_state
         :collapse:


   .. py:method:: add_agent_to_registry(name: str, description: str, agent_class: type[haive.agents.base.agent.Agent], config: dict[str, Any] | None = None)

      Dynamically add an agent to the registry and update tools.


      .. autolink-examples:: add_agent_to_registry
         :collapse:


   .. py:method:: remove_agent_from_registry(name: str)

      Dynamically remove an agent from the registry and update tools.


      .. autolink-examples:: remove_agent_from_registry
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup supervisor with dynamic agent tools.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: agent_registry
      :type:  AgentRegistry
      :value: None



   .. py:attribute:: state_schema
      :type:  type[SupervisorState]


.. py:class:: SupervisorState

   Bases: :py:obj:`haive.core.schema.prebuilt.messages_state.MessagesState`


   State schema for dynamic supervisor agent.


   .. autolink-examples:: SupervisorState
      :collapse:

   .. py:attribute:: agent_registry
      :type:  dict[str, dict[str, Any]]
      :value: None



   .. py:property:: available_agents
      :type: list[str]


      Get list of available agent names from registry.

      .. autolink-examples:: available_agents
         :collapse:


   .. py:attribute:: completed_agents
      :type:  set[str]
      :value: None



   .. py:attribute:: current_agent_name
      :type:  str | None
      :value: None



   .. py:attribute:: current_iteration
      :type:  int
      :value: None



   .. py:attribute:: current_task
      :type:  str | None
      :value: None



   .. py:attribute:: execution_history
      :type:  list[dict[str, Any]]
      :value: None



   .. py:property:: is_at_max_iterations
      :type: bool


      Check if we've reached the maximum iteration limit.

      .. autolink-examples:: is_at_max_iterations
         :collapse:


   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:attribute:: task_complete
      :type:  bool
      :value: None



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

.. py:data:: logger

.. py:data:: supervisor

