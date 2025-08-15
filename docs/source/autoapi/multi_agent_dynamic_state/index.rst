multi_agent_dynamic_state
=========================

.. py:module:: multi_agent_dynamic_state

.. autoapi-nested-parse::

   Enhanced Multi-Agent State with Dynamic Agent Management.

   This module extends the DynamicSupervisorState to include multi-agent coordination
   capabilities, agent registry management, and dynamic choice model integration.


   .. autolink-examples:: multi_agent_dynamic_state
      :collapse:


Classes
-------

.. autoapisummary::

   multi_agent_dynamic_state.AgentRegistryState
   multi_agent_dynamic_state.MultiAgentCoordinationState
   multi_agent_dynamic_state.MultiAgentDynamicSupervisorState


Module Contents
---------------

.. py:class:: AgentRegistryState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   State for dynamic agent registry management.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgentRegistryState
      :collapse:

   .. py:method:: _update_choice_model_options() -> None

      Update choice model options based on current agents.


      .. autolink-examples:: _update_choice_model_options
         :collapse:


   .. py:method:: add_agent_change_request(request_type: str, agent_name: str, details: dict[str, Any] | None = None) -> None

      Track agent change requests.


      .. autolink-examples:: add_agent_change_request
         :collapse:


   .. py:method:: add_agent_to_registry(agent_name: str, agent_type: str, capability: str, tools: list[str] | None = None) -> None

      Add agent to registry state.


      .. autolink-examples:: add_agent_to_registry
         :collapse:


   .. py:method:: get_agent_for_tool(tool_name: str) -> str | None

      Get the agent that owns a specific tool.


      .. autolink-examples:: get_agent_for_tool
         :collapse:


   .. py:method:: get_tools_for_agent(agent_name: str) -> list[str]

      Get tools owned by a specific agent.


      .. autolink-examples:: get_tools_for_agent
         :collapse:


   .. py:method:: remove_agent_from_registry(agent_name: str) -> bool

      Remove agent from registry state.


      .. autolink-examples:: remove_agent_from_registry
         :collapse:


   .. py:attribute:: agent_capabilities
      :type:  dict[str, str]
      :value: None



   .. py:attribute:: agent_change_requests
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: agent_tools
      :type:  dict[str, list[str]]
      :value: None



   .. py:attribute:: available_agents
      :type:  dict[str, str]
      :value: None



   .. py:attribute:: choice_model_options
      :type:  list[str]
      :value: None



   .. py:attribute:: choice_model_version
      :type:  int
      :value: None



   .. py:attribute:: last_agent_change
      :type:  float | None
      :value: None



   .. py:attribute:: pending_agent_additions
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: pending_agent_removals
      :type:  list[str]
      :value: None



   .. py:attribute:: tool_to_agent_mapping
      :type:  dict[str, str]
      :value: None



.. py:class:: MultiAgentCoordinationState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   State for multi-agent coordination patterns.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MultiAgentCoordinationState
      :collapse:

   .. py:method:: add_agent_handoff(from_agent: str, to_agent: str, reason: str, context: dict[str, Any] | None = None) -> None

      Record agent handoff.


      .. autolink-examples:: add_agent_handoff
         :collapse:


   .. py:method:: add_to_execution_queue(agent_name: str, task: dict[str, Any], priority: int = 1) -> None

      Add agent execution to queue.


      .. autolink-examples:: add_to_execution_queue
         :collapse:


   .. py:method:: complete_agent_execution(agent_name: str) -> None

      Mark agent execution as completed.


      .. autolink-examples:: complete_agent_execution
         :collapse:


   .. py:method:: start_agent_execution(agent_name: str, execution_id: str) -> None

      Mark agent execution as started.


      .. autolink-examples:: start_agent_execution
         :collapse:


   .. py:attribute:: active_executions
      :type:  dict[str, dict[str, Any]]
      :value: None



   .. py:attribute:: agent_handoffs
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: agent_messages
      :type:  dict[str, list[langchain_core.messages.BaseMessage]]
      :value: None



   .. py:attribute:: coordination_mode
      :type:  str
      :value: None



   .. py:attribute:: coordination_session_id
      :type:  str
      :value: None



   .. py:attribute:: coordination_start_time
      :type:  float
      :value: None



   .. py:attribute:: current_active_agent
      :type:  str | None
      :value: None



   .. py:attribute:: execution_queue
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: shared_context
      :type:  dict[str, Any]
      :value: None



.. py:class:: MultiAgentDynamicSupervisorState

   Bases: :py:obj:`haive.agents.supervisor.dynamic_state.DynamicSupervisorState`


   Enhanced state combining dynamic supervisor and multi-agent capabilities.


   .. autolink-examples:: MultiAgentDynamicSupervisorState
      :collapse:

   .. py:method:: cleanup_old_coordination_data(max_history: int = 100) -> None

      Clean up old coordination data to prevent memory bloat.


      .. autolink-examples:: cleanup_old_coordination_data
         :collapse:


   .. py:method:: end_coordination_session() -> dict[str, Any]

      End the current coordination session and return summary.


      .. autolink-examples:: end_coordination_session
         :collapse:


   .. py:method:: get_coordination_status() -> dict[str, Any]

      Get current coordination status.


      .. autolink-examples:: get_coordination_status
         :collapse:


   .. py:method:: process_pending_agent_changes() -> dict[str, list[str]]

      Process all pending agent additions and removals.


      .. autolink-examples:: process_pending_agent_changes
         :collapse:


   .. py:method:: request_agent_addition(agent_name: str, agent_type: str, capability: str, tools: list[str] | None = None, config: dict[str, Any] | None = None) -> str

      Request addition of a new agent.


      .. autolink-examples:: request_agent_addition
         :collapse:


   .. py:method:: request_agent_removal(agent_name: str) -> str

      Request removal of an agent.


      .. autolink-examples:: request_agent_removal
         :collapse:


   .. py:method:: route_tool_to_agent(tool_name: str) -> str | None

      Route a tool call to the appropriate agent.


      .. autolink-examples:: route_tool_to_agent
         :collapse:


   .. py:method:: start_coordination_session(mode: str = 'supervisor') -> str

      Start a new multi-agent coordination session.


      .. autolink-examples:: start_coordination_session
         :collapse:


   .. py:method:: sync_with_choice_model(choice_model: haive.core.common.models.dynamic_choice_model.DynamicChoiceModel) -> None

      Synchronize state with a DynamicChoiceModel.


      .. autolink-examples:: sync_with_choice_model
         :collapse:


   .. py:property:: active_coordination_sessions
      :type: int


      Number of active coordination sessions.

      .. autolink-examples:: active_coordination_sessions
         :collapse:


   .. py:attribute:: agent_registry
      :type:  AgentRegistryState
      :value: None



   .. py:attribute:: choice_model_cache
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: coordination
      :type:  MultiAgentCoordinationState
      :value: None



   .. py:attribute:: coordination_active
      :type:  bool
      :value: None



   .. py:attribute:: dynamic_routing_enabled
      :type:  bool
      :value: None



   .. py:attribute:: dynamic_tool_routes
      :type:  dict[str, str]
      :value: None



   .. py:attribute:: registry_needs_sync
      :type:  bool
      :value: None



   .. py:attribute:: tool_usage_history
      :type:  list[dict[str, Any]]
      :value: None



   .. py:property:: total_available_tools
      :type: int


      Total number of available tools across all agents.

      .. autolink-examples:: total_available_tools
         :collapse:


   .. py:property:: total_registered_agents
      :type: int


      Total number of registered agents.

      .. autolink-examples:: total_registered_agents
         :collapse:


