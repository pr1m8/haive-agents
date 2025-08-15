agents.experiments.supervisor.state_models
==========================================

.. py:module:: agents.experiments.supervisor.state_models

.. autoapi-nested-parse::

   State models for supervisor agents.

   This module defines the state schemas and data models used by supervisor agents
   for managing multi-agent systems.


   .. autolink-examples:: agents.experiments.supervisor.state_models
      :collapse:


Classes
-------

.. autoapisummary::

   agents.experiments.supervisor.state_models.AgentMetadata
   agents.experiments.supervisor.state_models.DynamicSupervisorState
   agents.experiments.supervisor.state_models.ExecutionContext
   agents.experiments.supervisor.state_models.SerializedAgent
   agents.experiments.supervisor.state_models.SupervisorState
   agents.experiments.supervisor.state_models.ToolMapping


Module Contents
---------------

.. py:class:: AgentMetadata(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Metadata for a registered agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgentMetadata
      :collapse:

   .. py:attribute:: agent_type
      :type:  str
      :value: None



   .. py:attribute:: capabilities
      :type:  list[str]
      :value: None



   .. py:attribute:: created_at
      :type:  str
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: is_active
      :type:  bool
      :value: None



   .. py:attribute:: last_used
      :type:  str | None
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



.. py:class:: DynamicSupervisorState(/, **data: Any)

   Bases: :py:obj:`SupervisorState`


   Extended state model for dynamic supervisors.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DynamicSupervisorState
      :collapse:

   .. py:method:: add_agent_template(name: str, template: dict[str, Any]) -> None

      Add a template for agent creation.

      :param name: Template name
      :param template: Template configuration


      .. autolink-examples:: add_agent_template
         :collapse:


   .. py:method:: get_creation_statistics() -> dict[str, Any]

      Get statistics about agent creation.

      :returns: Creation statistics


      .. autolink-examples:: get_creation_statistics
         :collapse:


   .. py:method:: record_agent_creation(agent_name: str, success: bool, error: str | None = None) -> None

      Record an agent creation attempt.

      :param agent_name: Name of the agent being created
      :param success: Whether creation was successful
      :param error: Error message if creation failed


      .. autolink-examples:: record_agent_creation
         :collapse:


   .. py:attribute:: agent_creation_enabled
      :type:  bool
      :value: None



   .. py:attribute:: agent_templates
      :type:  dict[str, dict[str, Any]]
      :value: None



   .. py:attribute:: created_agents
      :type:  list[str]
      :value: None



   .. py:attribute:: creation_history
      :type:  list[dict[str, Any]]
      :value: None



.. py:class:: ExecutionContext(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Context for agent execution.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ExecutionContext
      :collapse:

   .. py:attribute:: completed_at
      :type:  str | None
      :value: None



   .. py:attribute:: context
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: error
      :type:  str | None
      :value: None



   .. py:attribute:: priority
      :type:  int
      :value: None



   .. py:attribute:: requester
      :type:  str
      :value: None



   .. py:attribute:: result
      :type:  str | None
      :value: None



   .. py:attribute:: started_at
      :type:  str
      :value: None



   .. py:attribute:: status
      :type:  str
      :value: None



   .. py:attribute:: task_id
      :type:  str
      :value: None



.. py:class:: SerializedAgent(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Serialized representation of an agent for storage/transfer.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SerializedAgent
      :collapse:

   .. py:attribute:: agent_class
      :type:  str
      :value: None



   .. py:attribute:: config
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: state
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: tools
      :type:  list[str]
      :value: None



.. py:class:: SupervisorState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   State model for supervisor agents.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SupervisorState
      :collapse:

   .. py:method:: add_execution(agent_name: str, task: str, task_id: str | None = None) -> ExecutionContext

      Add a new execution context.

      :param agent_name: Name of the executing agent
      :param task: Task description
      :param task_id: Optional task ID (generated if not provided)

      :returns: The created execution context


      .. autolink-examples:: add_execution
         :collapse:


   .. py:method:: complete_execution(task_id: str, result: str, error: str | None = None) -> bool

      Complete an execution context.

      :param task_id: Task identifier
      :param result: Execution result
      :param error: Optional error message

      :returns: True if execution was found and updated


      .. autolink-examples:: complete_execution
         :collapse:


   .. py:method:: get_agent_statistics() -> dict[str, Any]

      Get statistics about agents and executions.

      :returns: Dictionary with agent statistics


      .. autolink-examples:: get_agent_statistics
         :collapse:


   .. py:method:: get_recent_executions(limit: int = 10) -> list[ExecutionContext]

      Get recent executions.

      :param limit: Maximum number of executions to return

      :returns: List of recent execution contexts


      .. autolink-examples:: get_recent_executions
         :collapse:


   .. py:attribute:: active_agent
      :type:  str | None
      :value: None



   .. py:attribute:: agents
      :type:  dict[str, AgentMetadata]
      :value: None



   .. py:attribute:: current_context
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: execution_history
      :type:  list[ExecutionContext]
      :value: None



   .. py:attribute:: supervisor_config
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: tool_mappings
      :type:  list[ToolMapping]
      :value: None



.. py:class:: ToolMapping(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Mapping between tools and agents.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ToolMapping
      :collapse:

   .. py:attribute:: agent_name
      :type:  str
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: parameters
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: tool_name
      :type:  str
      :value: None



