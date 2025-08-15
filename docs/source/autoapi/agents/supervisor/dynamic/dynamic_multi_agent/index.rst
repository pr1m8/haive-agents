agents.supervisor.dynamic.dynamic_multi_agent
=============================================

.. py:module:: agents.supervisor.dynamic.dynamic_multi_agent

.. autoapi-nested-parse::

   Dynamic Multi-Agent Supervisor with Dynamic Execution Pattern.

   This implementation integrates with the MultiAgent base class and uses
   dynamic agent execution without graph rebuilding.


   .. autolink-examples:: agents.supervisor.dynamic.dynamic_multi_agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.supervisor.dynamic.dynamic_multi_agent.logger


Classes
-------

.. autoapisummary::

   agents.supervisor.dynamic.dynamic_multi_agent.DynamicMultiAgent


Functions
---------

.. autoapisummary::

   agents.supervisor.dynamic.dynamic_multi_agent.create_dynamic_multi_agent


Module Contents
---------------

.. py:class:: DynamicMultiAgent

   Bases: :py:obj:`haive.agents.multi.compatibility.BaseMultiAgent`


   Multi-agent system with dynamic agent execution capabilities.

   This extends MultiAgent to support:
   - Dynamic agent registration/unregistration at runtime
   - No graph rebuilding - uses executor pattern
   - Proper state extraction per agent schema
   - Agent capability-based routing
   - Performance tracking and selection


   .. autolink-examples:: DynamicMultiAgent
      :collapse:

   .. py:method:: _calculate_agent_score(agent_name: str, content: str, state: dict[str, Any]) -> float

      Calculate suitability score for an agent.


      .. autolink-examples:: _calculate_agent_score
         :collapse:


   .. py:method:: _create_dynamic_executor_node()

      Create executor node that dynamically runs selected agent.


      .. autolink-examples:: _create_dynamic_executor_node
         :collapse:


   .. py:method:: _create_dynamic_supervisor_node()

      Create supervisor node for dynamic agent selection.


      .. autolink-examples:: _create_dynamic_supervisor_node
         :collapse:


   .. py:method:: _extract_state_dict(state: Any) -> dict[str, Any]

      Extract state dict with proper message handling.


      .. autolink-examples:: _extract_state_dict
         :collapse:


   .. py:method:: _prepare_agent_input(agent_name: str, agent: haive.agents.base.agent.Agent, state: dict[str, Any]) -> dict[str, Any]

      Prepare input for agent following AgentNode patterns.


      .. autolink-examples:: _prepare_agent_input
         :collapse:


   .. py:method:: _process_agent_result(agent_name: str, agent: haive.agents.base.agent.Agent, result: Any, state: dict[str, Any]) -> dict[str, Any]

      Process agent result into state update.


      .. autolink-examples:: _process_agent_result
         :collapse:


   .. py:method:: _register_agent_capability(agent_name: str, agent: haive.agents.base.agent.Agent) -> None

      Register agent capabilities for routing.


      .. autolink-examples:: _register_agent_capability
         :collapse:


   .. py:method:: _route_from_supervisor(state: Any) -> str

      Route from supervisor node.


      .. autolink-examples:: _route_from_supervisor
         :collapse:


   .. py:method:: _select_best_agent_for_task(message: langchain_core.messages.BaseMessage, state: dict[str, Any]) -> str | None

      Select the best agent for the current task.


      .. autolink-examples:: _select_best_agent_for_task
         :collapse:


   .. py:method:: _should_end_conversation(messages: list[langchain_core.messages.BaseMessage], state: dict[str, Any]) -> bool

      Check if we should end to avoid loops.


      .. autolink-examples:: _should_end_conversation
         :collapse:


   .. py:method:: _update_performance_metrics(agent_name: str, success: bool, execution_time: float | None = None) -> None

      Update agent performance metrics.


      .. autolink-examples:: _update_performance_metrics
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build dynamic multi-agent graph with executor pattern.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: get_agent_capabilities() -> dict[str, str]

      Get all agent capabilities.


      .. autolink-examples:: get_agent_capabilities
         :collapse:


   .. py:method:: get_agent_performance(agent_name: str | None = None) -> dict[str, Any]

      Get performance metrics for agent(s).


      .. autolink-examples:: get_agent_performance
         :collapse:


   .. py:method:: get_execution_history(limit: int | None = None) -> list[dict[str, Any]]

      Get execution history.


      .. autolink-examples:: get_execution_history
         :collapse:


   .. py:method:: register_agent_dynamically(agent: haive.agents.base.agent.Agent, capability: str | None = None, agent_name: str | None = None) -> bool

      Register a new agent dynamically at runtime.

      :param agent: The agent to register
      :param capability: Description of agent capabilities
      :param agent_name: Optional name override

      :returns: Success status


      .. autolink-examples:: register_agent_dynamically
         :collapse:


   .. py:method:: setup_agent() -> None

      Set up the dynamic multi-agent system.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:method:: unregister_agent_dynamically(agent_name: str) -> bool

      Unregister an agent dynamically.

      :param agent_name: Name of agent to remove

      :returns: Success status


      .. autolink-examples:: unregister_agent_dynamically
         :collapse:


   .. py:attribute:: _capability_registry
      :type:  dict[str, str]
      :value: None



   .. py:attribute:: _execution_history
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: _performance_metrics
      :type:  dict[str, dict[str, Any]]
      :value: None



   .. py:attribute:: coordination_mode
      :type:  Literal['dynamic']
      :value: None



   .. py:attribute:: enable_capability_routing
      :type:  bool
      :value: None



   .. py:attribute:: track_performance
      :type:  bool
      :value: None



.. py:function:: create_dynamic_multi_agent(agents: list[haive.agents.base.agent.Agent], name: str = 'DynamicMultiAgent', **kwargs) -> DynamicMultiAgent

   Create a dynamic multi-agent system.

   :param agents: List of agents to include
   :param name: Name for the multi-agent system
   :param \*\*kwargs: Additional configuration

   :returns: DynamicMultiAgent instance


   .. autolink-examples:: create_dynamic_multi_agent
      :collapse:

.. py:data:: logger

