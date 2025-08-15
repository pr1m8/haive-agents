agents.supervisor.state.dynamic_state
=====================================

.. py:module:: agents.supervisor.state.dynamic_state

.. autoapi-nested-parse::

   Enhanced state schema for dynamic supervisor operations.

   This module provides an enhanced state management system for dynamic supervisor
   agents that can add/remove agents at runtime and adapt their responses based
   on agent configuration and execution context.


   .. autolink-examples:: agents.supervisor.state.dynamic_state
      :collapse:


Classes
-------

.. autoapisummary::

   agents.supervisor.state.dynamic_state.AgentExecutionConfig
   agents.supervisor.state.dynamic_state.AgentExecutionResult
   agents.supervisor.state.dynamic_state.DynamicSupervisorState
   agents.supervisor.state.dynamic_state.SupervisorDecision


Module Contents
---------------

.. py:class:: AgentExecutionConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for agent execution within supervisor context.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgentExecutionConfig
      :collapse:

   .. py:attribute:: agent_name
      :type:  str
      :value: None



   .. py:attribute:: agent_type
      :type:  str | None
      :value: None



   .. py:attribute:: capability_description
      :type:  str
      :value: None



   .. py:attribute:: created_at
      :type:  float
      :value: None



   .. py:attribute:: custom_params
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: error_count
      :type:  int
      :value: None



   .. py:attribute:: execution_timeout
      :type:  float | None
      :value: None



   .. py:attribute:: handoff_back
      :type:  bool
      :value: None



   .. py:attribute:: last_used_at
      :type:  float | None
      :value: None



   .. py:attribute:: max_retries
      :type:  int
      :value: None



   .. py:attribute:: output_mode
      :type:  str
      :value: None



   .. py:attribute:: priority
      :type:  int
      :value: None



   .. py:attribute:: retry_count
      :type:  int
      :value: None



   .. py:attribute:: state_adapters
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: success_count
      :type:  int
      :value: None



.. py:class:: AgentExecutionResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result of agent execution with metadata.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgentExecutionResult
      :collapse:

   .. py:attribute:: agent_name
      :type:  str
      :value: None



   .. py:attribute:: duration
      :type:  float | None
      :value: None



   .. py:attribute:: end_time
      :type:  float | None
      :value: None



   .. py:attribute:: error
      :type:  str | None
      :value: None



   .. py:attribute:: execution_id
      :type:  str
      :value: None



   .. py:attribute:: messages
      :type:  list[langchain_core.messages.BaseMessage]
      :value: None



   .. py:attribute:: output
      :type:  Any | None
      :value: None



   .. py:attribute:: start_time
      :type:  float
      :value: None



   .. py:attribute:: state_changes
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: success
      :type:  bool
      :value: None



   .. py:attribute:: token_usage
      :type:  dict[str, int] | None
      :value: None



   .. py:attribute:: tool_calls
      :type:  list[dict[str, Any]]
      :value: None



.. py:class:: DynamicSupervisorState

   Bases: :py:obj:`haive.core.schema.state_schema.StateSchema`


   Enhanced state schema for dynamic supervisor operations.

   This state schema provides comprehensive tracking of agent execution,
   dynamic configuration, and adaptive response handling for supervisor agents.


   .. autolink-examples:: DynamicSupervisorState
      :collapse:

   .. py:method:: adapt_response_for_agent(agent_name: str, response: Any) -> Any

      Apply adaptation rules to agent response.


      .. autolink-examples:: adapt_response_for_agent
         :collapse:


   .. py:method:: add_agent_config(agent_name: str, config: AgentExecutionConfig) -> None

      Add or update agent configuration.


      .. autolink-examples:: add_agent_config
         :collapse:


   .. py:method:: add_execution_result(result: AgentExecutionResult) -> None

      Add execution result to history.


      .. autolink-examples:: add_execution_result
         :collapse:


   .. py:method:: add_routing_decision(decision: SupervisorDecision) -> None

      Add routing decision to history.


      .. autolink-examples:: add_routing_decision
         :collapse:


   .. py:method:: cleanup_old_history(max_history: int = 100) -> None

      Clean up old execution history to prevent memory bloat.


      .. autolink-examples:: cleanup_old_history
         :collapse:


   .. py:method:: get_agent_config(agent_name: str) -> AgentExecutionConfig | None

      Get agent configuration by name.


      .. autolink-examples:: get_agent_config
         :collapse:


   .. py:method:: get_agent_performance(agent_name: str) -> dict[str, Any]

      Get performance metrics for specific agent.


      .. autolink-examples:: get_agent_performance
         :collapse:


   .. py:method:: get_available_agents() -> list[str]

      Get list of available agent names.


      .. autolink-examples:: get_available_agents
         :collapse:


   .. py:method:: get_high_priority_agents() -> list[str]

      Get agents sorted by priority (highest first).


      .. autolink-examples:: get_high_priority_agents
         :collapse:


   .. py:method:: get_recent_decisions(limit: int = 5) -> list[SupervisorDecision]

      Get recent routing decisions.


      .. autolink-examples:: get_recent_decisions
         :collapse:


   .. py:method:: increment_retry_count(agent_name: str) -> None

      Increment retry count for agent.


      .. autolink-examples:: increment_retry_count
         :collapse:


   .. py:method:: remove_agent_config(agent_name: str) -> bool

      Remove agent configuration.


      .. autolink-examples:: remove_agent_config
         :collapse:


   .. py:method:: reset_retry_count(agent_name: str) -> None

      Reset retry count for agent.


      .. autolink-examples:: reset_retry_count
         :collapse:


   .. py:method:: should_retry_agent(agent_name: str) -> bool

      Determine if agent should be retried based on configuration.


      .. autolink-examples:: should_retry_agent
         :collapse:


   .. py:method:: update_agent_stats(agent_name: str, success: bool, duration: float) -> None

      Update agent execution statistics.


      .. autolink-examples:: update_agent_stats
         :collapse:


   .. py:property:: active_agent_count
      :type: int


      Number of currently registered agents.

      .. autolink-examples:: active_agent_count
         :collapse:


   .. py:attribute:: adaptation_rules
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: agent_execution_history
      :type:  list[AgentExecutionResult]
      :value: None



   .. py:attribute:: auto_adapt_responses
      :type:  bool
      :value: None



   .. py:attribute:: conversation_complete
      :type:  bool
      :value: None



   .. py:attribute:: conversation_metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: current_decision
      :type:  SupervisorDecision | None
      :value: None



   .. py:attribute:: current_execution
      :type:  AgentExecutionResult | None
      :value: None



   .. py:attribute:: execution_queue
      :type:  list[str]
      :value: None



   .. py:property:: last_execution_time
      :type: float | None


      Timestamp of last agent execution.

      .. autolink-examples:: last_execution_time
         :collapse:


   .. py:attribute:: messages
      :type:  list[langchain_core.messages.BaseMessage]
      :value: None



   .. py:property:: most_used_agent
      :type: str | None


      Name of most frequently used agent.

      .. autolink-examples:: most_used_agent
         :collapse:


   .. py:attribute:: parallel_execution_enabled
      :type:  bool
      :value: None



   .. py:attribute:: registered_agents
      :type:  dict[str, AgentExecutionConfig]
      :value: None



   .. py:attribute:: requires_human_intervention
      :type:  bool
      :value: None



   .. py:attribute:: routing_decisions
      :type:  list[SupervisorDecision]
      :value: None



   .. py:attribute:: session_stats
      :type:  dict[str, Any]
      :value: None



   .. py:property:: success_rate
      :type: float


      Success rate of agent executions.

      .. autolink-examples:: success_rate
         :collapse:


   .. py:attribute:: supervisor_config
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: task_context
      :type:  dict[str, Any]
      :value: None



.. py:class:: SupervisorDecision(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a supervisor routing decision with reasoning.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SupervisorDecision
      :collapse:

   .. py:attribute:: alternatives
      :type:  list[dict[str, float]]
      :value: None



   .. py:attribute:: available_agents
      :type:  list[str]
      :value: None



   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: decision_id
      :type:  str
      :value: None



   .. py:attribute:: input_analysis
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: previous_context
      :type:  str | None
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: target_agent
      :type:  str | None
      :value: None



   .. py:attribute:: timestamp
      :type:  float
      :value: None



