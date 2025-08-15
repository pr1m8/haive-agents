integrated_supervisor
=====================

.. py:module:: integrated_supervisor

.. autoapi-nested-parse::

   Integrated Dynamic Multi-Agent Supervisor.

   This module provides a complete integration of:
   - DynamicSupervisorAgent capabilities
   - Multi-agent coordination state
   - Dynamic agent management tools
   - DynamicChoiceModel routing
   - Tool-based agent addition/removal


   .. autolink-examples:: integrated_supervisor
      :collapse:


Attributes
----------

.. autoapisummary::

   integrated_supervisor.console
   integrated_supervisor.logger


Classes
-------

.. autoapisummary::

   integrated_supervisor.IntegratedDynamicSupervisor


Module Contents
---------------

.. py:class:: IntegratedDynamicSupervisor(name: str = 'integrated_supervisor', engine: haive.core.engine.aug_llm.AugLLMConfig | None = None, enable_agent_management_tools: bool = True, coordination_mode: str = 'supervisor', **kwargs)

   Bases: :py:obj:`haive.agents.supervisor.dynamic_supervisor.DynamicSupervisorAgent`


   Integrated supervisor combining dynamic agent management and multi-agent coordination.

   This supervisor provides:
   - Dynamic agent addition/removal through tools
   - Multi-agent coordination patterns
   - DynamicChoiceModel integration for routing
   - Tool-based agent management
   - Enhanced state management

   Initialize integrated supervisor.

   :param name: Supervisor name
   :param engine: LLM engine for decisions
   :param enable_agent_management_tools: Whether to include agent management tools
   :param coordination_mode: Multi-agent coordination mode
   :param \*\*kwargs: Additional supervisor arguments


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: IntegratedDynamicSupervisor
      :collapse:

   .. py:method:: _check_for_agent_management_needs(state: haive.agents.supervisor.multi_agent_dynamic_state.MultiAgentDynamicSupervisorState) -> bool

      Check if the request needs agent management operations.


      .. autolink-examples:: _check_for_agent_management_needs
         :collapse:


   .. py:method:: _create_agent_management_node() -> Any

      Create node for processing agent management tool calls.


      .. autolink-examples:: _create_agent_management_node
         :collapse:


   .. py:method:: _create_enhanced_coordinator_node() -> Any

      Create enhanced coordination node with multi-agent support.


      .. autolink-examples:: _create_enhanced_coordinator_node
         :collapse:


   .. py:method:: _create_integrated_supervisor_node() -> Any

      Create supervisor node with agent management tool integration.


      .. autolink-examples:: _create_integrated_supervisor_node
         :collapse:


   .. py:method:: _setup_agent_management_tools() -> None

      Setup agent management tools.


      .. autolink-examples:: _setup_agent_management_tools
         :collapse:


   .. py:method:: _setup_integrated_conditional_routing(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> None

      Setup enhanced conditional routing with agent management.


      .. autolink-examples:: _setup_integrated_conditional_routing
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build integrated supervisor graph with agent management capabilities.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: end_coordination_session() -> dict[str, Any]

      End the current coordination session.


      .. autolink-examples:: end_coordination_session
         :collapse:


   .. py:method:: get_coordination_status() -> dict[str, Any]

      Get current coordination status.


      .. autolink-examples:: get_coordination_status
         :collapse:


   .. py:method:: print_integrated_dashboard() -> None

      Print comprehensive integrated supervisor dashboard.


      .. autolink-examples:: print_integrated_dashboard
         :collapse:


   .. py:method:: register_agent(agent: Any, capability_description: str | None = None, execution_config: dict[str, Any] | None = None, rebuild_graph: bool | None = None) -> bool
      :async:


      Enhanced agent registration with multi-agent state integration.


      .. autolink-examples:: register_agent
         :collapse:


   .. py:method:: register_agent_constructor(agent_type: str, constructor) -> None

      Register an agent constructor for dynamic creation.


      .. autolink-examples:: register_agent_constructor
         :collapse:


   .. py:method:: start_coordination_session(mode: str | None = None) -> str

      Start a new coordination session.


      .. autolink-examples:: start_coordination_session
         :collapse:


   .. py:method:: unregister_agent(agent_name: str, rebuild_graph: bool | None = None) -> bool
      :async:


      Enhanced agent unregistration with multi-agent state integration.


      .. autolink-examples:: unregister_agent
         :collapse:


   .. py:attribute:: agent_management_tools
      :value: []



   .. py:attribute:: coordination_mode
      :value: 'supervisor'



   .. py:attribute:: enable_agent_management_tools
      :value: True



   .. py:attribute:: registry_manager
      :value: None



.. py:data:: console

.. py:data:: logger

