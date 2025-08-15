dynamic_supervisor
==================

.. py:module:: dynamic_supervisor

.. autoapi-nested-parse::

   Dynamic LangGraph-style Supervisor Implementation.

   This module provides a dynamic supervisor agent that can add/remove agents at runtime,
   adapt agent responses, and handle complex multi-agent coordination patterns similar
   to LangGraph's supervisor package but with enhanced Haive-specific functionality.


   .. autolink-examples:: dynamic_supervisor
      :collapse:


Attributes
----------

.. autoapisummary::

   dynamic_supervisor.console
   dynamic_supervisor.logger


Classes
-------

.. autoapisummary::

   dynamic_supervisor.DynamicSupervisorAgent
   dynamic_supervisor.PerformanceMonitor


Module Contents
---------------

.. py:class:: DynamicSupervisorAgent(name: str = 'dynamic_supervisor', engine: haive.core.engine.aug_llm.AugLLMConfig | None = None, auto_rebuild_graph: bool = True, max_execution_history: int = 100, enable_parallel_execution: bool = False, **kwargs)

   Bases: :py:obj:`haive.agents.react.agent.ReactAgent`


   Dynamic supervisor agent with runtime agent management and adaptive responses.

   This supervisor extends the base haive Agent architecture to provide:
   - Runtime agent registration/deregistration
   - Dynamic graph rebuilding
   - Adaptive response handling
   - Performance monitoring and optimization
   - LangGraph-style coordination patterns

   Key features:
   - Hot-swappable agent configuration
   - Intelligent routing with reasoning
   - Response adaptation and filtering
   - Parallel and sequential execution modes
   - Comprehensive performance tracking

   Initialize dynamic supervisor agent.

   :param name: Supervisor agent name
   :param engine: LLM engine for routing decisions
   :param auto_rebuild_graph: Whether to automatically rebuild graph on agent changes
   :param max_execution_history: Maximum execution history to maintain
   :param enable_parallel_execution: Enable parallel agent execution
   :param \*\*kwargs: Additional Agent arguments


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DynamicSupervisorAgent
      :collapse:

   .. py:method:: _add_agent_nodes(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> None

      Add registered agents as graph nodes.


      .. autolink-examples:: _add_agent_nodes
         :collapse:


   .. py:method:: _aggregate_agent_tools() -> dict

      Aggregate tools from all registered agents into supervisor routing options.


      .. autolink-examples:: _aggregate_agent_tools
         :collapse:


   .. py:method:: _analyze_input(state: haive.agents.supervisor.dynamic_state.DynamicSupervisorState) -> dict[str, Any]
      :async:


      Analyze input messages for context and requirements.


      .. autolink-examples:: _analyze_input
         :collapse:


   .. py:method:: _create_coordinator_node() -> collections.abc.Callable

      Create coordination node for managing execution flow.


      .. autolink-examples:: _create_coordinator_node
         :collapse:


   .. py:method:: _create_dynamic_tool_choice() -> str

      Create dynamic routing choice that includes tools from registered agents.


      .. autolink-examples:: _create_dynamic_tool_choice
         :collapse:


   .. py:method:: _create_enhanced_agent_wrapper(agent_name: str) -> collections.abc.Callable

      Create enhanced agent wrapper with performance tracking.


      .. autolink-examples:: _create_enhanced_agent_wrapper
         :collapse:


   .. py:method:: _create_enhanced_decision_prompt(state: haive.agents.supervisor.dynamic_state.DynamicSupervisorState, input_analysis: dict[str, Any], available_agents: dict[str, dict[str, Any]], tool_info: dict[str, Any] | None = None) -> langchain_core.prompts.ChatPromptTemplate

      Create enhanced prompt with reasoning and context.


      .. autolink-examples:: _create_enhanced_decision_prompt
         :collapse:


   .. py:method:: _create_enhanced_supervisor_node() -> collections.abc.Callable

      Create enhanced supervisor node with reasoning and context.


      .. autolink-examples:: _create_enhanced_supervisor_node
         :collapse:


   .. py:method:: _create_response_adapter_node() -> collections.abc.Callable

      Create response adaptation node.


      .. autolink-examples:: _create_response_adapter_node
         :collapse:


   .. py:method:: _get_available_agents_with_context(state: haive.agents.supervisor.dynamic_state.DynamicSupervisorState) -> dict[str, dict[str, Any]]

      Get available agents with performance context.


      .. autolink-examples:: _get_available_agents_with_context
         :collapse:


   .. py:method:: _parse_decision_response(response: Any, available_agents: dict[str, Any]) -> dict[str, Any]

      Parse LLM decision response.


      .. autolink-examples:: _parse_decision_response
         :collapse:


   .. py:method:: _prepare_enhanced_agent_state(supervisor_state: haive.agents.supervisor.dynamic_state.DynamicSupervisorState, agent: haive.agents.base.agent.Agent) -> Any

      Prepare enhanced state for agent execution.


      .. autolink-examples:: _prepare_enhanced_agent_state
         :collapse:


   .. py:method:: _rebuild_graph() -> None
      :async:


      Rebuild the supervisor graph with current agents.


      .. autolink-examples:: _rebuild_graph
         :collapse:


   .. py:method:: _setup_conditional_routing(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> None

      Setup conditional routing from coordinator.


      .. autolink-examples:: _setup_conditional_routing
         :collapse:


   .. py:method:: _update_supervisor_tools() -> None

      Update supervisor's own engine tools with aggregated agent tools.


      .. autolink-examples:: _update_supervisor_tools
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build dynamic supervisor graph with enhanced routing.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: get_performance_summary() -> dict[str, Any]

      Get comprehensive performance summary.


      .. autolink-examples:: get_performance_summary
         :collapse:


   .. py:method:: print_supervisor_dashboard() -> None

      Print comprehensive supervisor dashboard.


      .. autolink-examples:: print_supervisor_dashboard
         :collapse:


   .. py:method:: register_agent(agent: haive.agents.base.agent.Agent, capability_description: str | None = None, execution_config: dict[str, Any] | None = None, rebuild_graph: bool | None = None) -> bool
      :async:


      Register an agent with enhanced configuration.

      :param agent: Agent instance to register
      :param capability_description: Description of agent capabilities
      :param execution_config: Custom execution configuration
      :param rebuild_graph: Whether to rebuild graph (uses auto_rebuild_graph if None)

      :returns: True if registration successful
      :rtype: bool


      .. autolink-examples:: register_agent
         :collapse:


   .. py:method:: unregister_agent(agent_name: str, rebuild_graph: bool | None = None) -> bool
      :async:


      Unregister an agent with graph rebuilding.

      :param agent_name: Name of agent to remove
      :param rebuild_graph: Whether to rebuild graph (uses auto_rebuild_graph if None)

      :returns: True if removal successful
      :rtype: bool


      .. autolink-examples:: unregister_agent
         :collapse:


   .. py:method:: update_agent_config(agent_name: str, config_updates: dict[str, Any]) -> bool
      :async:


      Update agent execution configuration at runtime.

      :param agent_name: Name of agent to update
      :param config_updates: Configuration updates to apply

      :returns: True if update successful
      :rtype: bool


      .. autolink-examples:: update_agent_config
         :collapse:


   .. py:attribute:: _execution_lock


   .. py:attribute:: _graph_built
      :value: False



   .. py:attribute:: _performance_monitor


   .. py:attribute:: agent_registry


   .. py:attribute:: auto_rebuild_graph
      :value: True



   .. py:attribute:: enable_parallel_execution
      :value: False



   .. py:attribute:: max_execution_history
      :value: 100



.. py:class:: PerformanceMonitor

   Simple performance monitoring for supervisor operations.


   .. autolink-examples:: PerformanceMonitor
      :collapse:

   .. py:method:: end_decision(target: str)


   .. py:method:: get_average_decision_time() -> float


   .. py:method:: start_decision() -> None


   .. py:attribute:: decision_count
      :value: 0



   .. py:attribute:: decision_start_time
      :value: None



   .. py:attribute:: total_decision_time
      :value: 0.0



.. py:data:: console

.. py:data:: logger

