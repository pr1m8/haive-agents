agents.experiments.supervisor.base_supervisor
=============================================

.. py:module:: agents.experiments.supervisor.base_supervisor

.. autoapi-nested-parse::

   Base supervisor implementation for multi-agent systems.

   This module provides the core supervisor classes that can manage multiple agents,
   handle tool synchronization, and support dynamic agent creation.


   .. autolink-examples:: agents.experiments.supervisor.base_supervisor
      :collapse:


Classes
-------

.. autoapisummary::

   agents.experiments.supervisor.base_supervisor.AgentMetadata
   agents.experiments.supervisor.base_supervisor.BaseSupervisor
   agents.experiments.supervisor.base_supervisor.DynamicSupervisor
   agents.experiments.supervisor.base_supervisor.SupervisorState


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



   .. py:attribute:: last_used
      :type:  str | None
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



.. py:class:: BaseSupervisor(name: str, engine: haive.core.engine.aug_llm.AugLLMConfig, agents: dict[str, Any] | None = None, **kwargs)

   Bases: :py:obj:`haive.agents.react.agent.ReactAgent`


   Base supervisor agent for managing multiple agents.

   This supervisor can register agents, delegate tasks, and coordinate
   multi-agent workflows.

   Initialize the supervisor.

   :param name: Supervisor name
   :param engine: LLM configuration
   :param agents: Optional initial agents to register
   :param \*\*kwargs: Additional arguments passed to ReactAgent


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: BaseSupervisor
      :collapse:

   .. py:method:: delegate_task(agent_name: str, task: str) -> str

      Delegate a task to a specific agent.

      :param agent_name: Name of the agent to delegate to
      :param task: Task description

      :returns: Result from the agent


      .. autolink-examples:: delegate_task
         :collapse:


   .. py:method:: get_agent(name: str) -> Any | None

      Get a registered agent by name.

      :param name: Agent identifier

      :returns: The agent instance if found, None otherwise


      .. autolink-examples:: get_agent
         :collapse:


   .. py:method:: get_execution_status() -> dict[str, Any]

      Get current execution status.

      :returns: Status information including active agent and recent history


      .. autolink-examples:: get_execution_status
         :collapse:


   .. py:method:: list_agents() -> dict[str, AgentMetadata]

      List all registered agents.

      :returns: Dictionary of agent metadata


      .. autolink-examples:: list_agents
         :collapse:


   .. py:method:: register_agent(name: str, description: str, agent: Any) -> None

      Register an agent with the supervisor.

      :param name: Agent identifier
      :param description: Description of agent capabilities
      :param agent: The agent instance


      .. autolink-examples:: register_agent
         :collapse:


   .. py:attribute:: supervisor_state


.. py:class:: DynamicSupervisor(*args, **kwargs)

   Bases: :py:obj:`BaseSupervisor`


   Extended supervisor with dynamic agent creation capabilities.

   This supervisor can create new agents on demand based on requirements.

   Initialize dynamic supervisor.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DynamicSupervisor
      :collapse:

   .. py:method:: create_agent(name: str, description: str, agent_type: str = 'simple') -> bool

      Create a new agent dynamically.

      :param name: Agent name
      :param description: Agent description
      :param agent_type: Type of agent to create

      :returns: True if agent was created successfully


      .. autolink-examples:: create_agent
         :collapse:


   .. py:method:: enable_agent_creation(enable: bool = True) -> None

      Enable or disable dynamic agent creation.

      :param enable: Whether to enable agent creation


      .. autolink-examples:: enable_agent_creation
         :collapse:


   .. py:method:: get_capabilities() -> dict[str, Any]

      Get supervisor capabilities.

      :returns: Dictionary describing supervisor capabilities


      .. autolink-examples:: get_capabilities
         :collapse:


   .. py:attribute:: agent_creation_enabled
      :value: False



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
      :type:  list[dict[str, Any]]
      :value: None



