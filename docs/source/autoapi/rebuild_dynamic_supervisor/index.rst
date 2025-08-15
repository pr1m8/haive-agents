rebuild_dynamic_supervisor
==========================

.. py:module:: rebuild_dynamic_supervisor

.. autoapi-nested-parse::

   Dynamic Supervisor with Proper Graph Rebuilding.

   This implementation correctly rebuilds the graph when agents are added/removed,
   following the Agent base class patterns.


   .. autolink-examples:: rebuild_dynamic_supervisor
      :collapse:


Attributes
----------

.. autoapisummary::

   rebuild_dynamic_supervisor.logger


Classes
-------

.. autoapisummary::

   rebuild_dynamic_supervisor.RebuildDynamicSupervisor
   rebuild_dynamic_supervisor.TestAgent


Module Contents
---------------

.. py:class:: RebuildDynamicSupervisor

   Bases: :py:obj:`haive.agents.react.agent.ReactAgent`


   Dynamic supervisor that properly rebuilds graphs when agents change.

   Key approach:
   1. Maintain agent registry
   2. When agents are added/removed, clear the graph
   3. Let the Agent base class rebuild on next invocation
   4. Each agent gets its own node in the graph


   .. autolink-examples:: RebuildDynamicSupervisor
      :collapse:

   .. py:method:: _create_agent_node(agent_name: str, agent: Any)

      Create node for a specific agent with proper state handling.


      .. autolink-examples:: _create_agent_node
         :collapse:


   .. py:method:: _create_supervisor_node()

      Create supervisor decision node.


      .. autolink-examples:: _create_supervisor_node
         :collapse:


   .. py:method:: _prepare_agent_input(agent: Any, state: dict[str, Any]) -> dict[str, Any]

      Prepare input for agent based on its state schema.


      .. autolink-examples:: _prepare_agent_input
         :collapse:


   .. py:method:: _process_agent_result(result: Any, state: dict[str, Any], agent_name: str) -> dict[str, Any]

      Process agent result into state update.


      .. autolink-examples:: _process_agent_result
         :collapse:


   .. py:method:: _route_from_supervisor(state: Any) -> str

      Routing function from supervisor.


      .. autolink-examples:: _route_from_supervisor
         :collapse:


   .. py:method:: _select_best_agent(content: str) -> str | None

      Select best agent for the given content.


      .. autolink-examples:: _select_best_agent
         :collapse:


   .. py:method:: _trigger_rebuild()

      Trigger graph rebuild by clearing current graph.

      This forces the Agent base class to rebuild on next invocation.


      .. autolink-examples:: _trigger_rebuild
         :collapse:


   .. py:method:: ainvoke(input: Any, config: Any | None = None, **kwargs) -> Any
      :async:


      Override to check for rebuild before invocation.


      .. autolink-examples:: ainvoke
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build supervisor graph with all registered agents as nodes.

      Graph structure:
      - supervisor: Makes routing decisions
      - agent nodes: One per registered agent
      - Conditional routing from supervisor to agents
      - Agents route back to supervisor


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: invoke(input: Any, config: Any | None = None, **kwargs) -> Any

      Override to check for rebuild before invocation.


      .. autolink-examples:: invoke
         :collapse:


   .. py:method:: register_agent(agent: Any, capability: str | None = None, agent_name: str | None = None) -> bool

      Register an agent and mark for rebuild.

      :param agent: Agent instance to register
      :param capability: Description of agent capabilities
      :param agent_name: Optional name override

      :returns: Success status


      .. autolink-examples:: register_agent
         :collapse:


   .. py:method:: unregister_agent(agent_name: str) -> bool

      Unregister an agent and mark for rebuild.


      .. autolink-examples:: unregister_agent
         :collapse:


   .. py:attribute:: _agent_capabilities
      :type:  dict[str, str]
      :value: None



   .. py:attribute:: _agent_registry
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: _needs_rebuild
      :type:  bool
      :value: None



   .. py:attribute:: auto_rebuild
      :type:  bool
      :value: None



.. py:class:: TestAgent(name: str)

   .. py:method:: ainvoke(state: dict[str, Any]) -> dict[str, Any]
      :async:



   .. py:attribute:: name


.. py:data:: logger

