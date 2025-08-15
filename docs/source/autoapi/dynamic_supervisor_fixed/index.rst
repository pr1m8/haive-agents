dynamic_supervisor_fixed
========================

.. py:module:: dynamic_supervisor_fixed

.. autoapi-nested-parse::

   Fixed Dynamic Supervisor with Proper Graph Rebuilding.

   This implementation correctly handles dynamic agent addition after compilation
   based on BaseGraph2 limitations and requirements.


   .. autolink-examples:: dynamic_supervisor_fixed
      :collapse:


Attributes
----------

.. autoapisummary::

   dynamic_supervisor_fixed.logger


Classes
-------

.. autoapisummary::

   dynamic_supervisor_fixed.DynamicSupervisorFixed


Functions
---------

.. autoapisummary::

   dynamic_supervisor_fixed.test_dynamic_supervisor


Module Contents
---------------

.. py:class:: DynamicSupervisorFixed(**kwargs)

   Bases: :py:obj:`haive.agents.react.agent.ReactAgent`


   Fixed dynamic supervisor that properly rebuilds graphs at runtime.

   Key improvements:
   1. Proper graph rebuilding through Agent.create_runnable()
   2. Lazy recompilation on next invocation
   3. State preservation through checkpointer
   4. Dynamic routing that checks registry at runtime


   .. autolink-examples:: DynamicSupervisorFixed
      :collapse:

   .. py:method:: _create_agent_wrapper(agent_name: str, agent: Any) -> collections.abc.Callable

      Create wrapper function for agent execution.


      .. autolink-examples:: _create_agent_wrapper
         :collapse:


   .. py:method:: _create_dynamic_executor_node() -> collections.abc.Callable

      Create executor node that prepares for agent execution.


      .. autolink-examples:: _create_dynamic_executor_node
         :collapse:


   .. py:method:: _create_dynamic_supervisor_node() -> collections.abc.Callable

      Create supervisor node that routes based on dynamic registry.


      .. autolink-examples:: _create_dynamic_supervisor_node
         :collapse:


   .. py:method:: _rebuild_graph_properly() -> None

      Properly rebuild the graph using Agent's create_runnable method.


      .. autolink-examples:: _rebuild_graph_properly
         :collapse:


   .. py:method:: _route_supervisor(state: haive.agents.supervisor.dynamic_state.DynamicSupervisorState) -> str

      Route from supervisor based on state.


      .. autolink-examples:: _route_supervisor
         :collapse:


   .. py:method:: _route_to_agent(state: haive.agents.supervisor.dynamic_state.DynamicSupervisorState) -> str

      Route to specific agent from executor.


      .. autolink-examples:: _route_to_agent
         :collapse:


   .. py:method:: ainvoke(input: Any, config: Any | None = None, **kwargs) -> Any
      :async:


      Override ainvoke to handle lazy graph rebuilding.


      .. autolink-examples:: ainvoke
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build supervisor graph with registered agents.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: get_agent_info(agent_name: str) -> dict[str, Any] | None

      Get information about a registered agent.


      .. autolink-examples:: get_agent_info
         :collapse:


   .. py:method:: get_registered_agents() -> list[str]

      Get list of currently registered agents.


      .. autolink-examples:: get_registered_agents
         :collapse:


   .. py:method:: invoke(input: Any, config: Any | None = None, **kwargs) -> Any

      Override invoke to handle lazy graph rebuilding.


      .. autolink-examples:: invoke
         :collapse:


   .. py:method:: register_agent(agent: Any, capability: str | None = None, rebuild_immediately: bool = False) -> bool

      Register an agent for dynamic routing.

      :param agent: Agent to register
      :param capability: Description of agent's capabilities
      :param rebuild_immediately: Force immediate rebuild (vs lazy rebuild)

      :returns: Success status
      :rtype: bool


      .. autolink-examples:: register_agent
         :collapse:


   .. py:method:: unregister_agent(agent_name: str, rebuild_immediately: bool = False) -> bool

      Unregister an agent.

      :param agent_name: Name of agent to remove
      :param rebuild_immediately: Force immediate rebuild

      :returns: Success status
      :rtype: bool


      .. autolink-examples:: unregister_agent
         :collapse:


   .. py:attribute:: _agent_registry
      :type:  dict[str, Any]


   .. py:attribute:: _initial_build_complete
      :type:  bool
      :value: False



   .. py:attribute:: _needs_rebuild
      :type:  bool
      :value: False



   .. py:attribute:: auto_rebuild_graph
      :type:  bool
      :value: None



.. py:function:: test_dynamic_supervisor()
   :async:


   Test the fixed dynamic supervisor.


   .. autolink-examples:: test_dynamic_supervisor
      :collapse:

.. py:data:: logger

