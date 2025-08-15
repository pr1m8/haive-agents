clean_dynamic_supervisor
========================

.. py:module:: clean_dynamic_supervisor

.. autoapi-nested-parse::

   Clean Dynamic Supervisor Implementation.

   A dynamic supervisor that can add/remove agents at runtime and
   adapt routing based on agent capabilities.


   .. autolink-examples:: clean_dynamic_supervisor
      :collapse:


Attributes
----------

.. autoapisummary::

   clean_dynamic_supervisor.logger


Classes
-------

.. autoapisummary::

   clean_dynamic_supervisor.DynamicSupervisor
   clean_dynamic_supervisor.DynamicSupervisorState


Module Contents
---------------

.. py:class:: DynamicSupervisor

   Bases: :py:obj:`haive.agents.react.agent.ReactAgent`


   Dynamic supervisor with runtime agent management.

   Key features:
   - Add/remove agents at runtime
   - Automatic graph rebuilding
   - Tool aggregation from agents
   - Intelligent routing with history


   .. autolink-examples:: DynamicSupervisor
      :collapse:

   .. py:method:: _add_management_tools() -> None

      Add tools for agent management.


      .. autolink-examples:: _add_management_tools
         :collapse:


   .. py:method:: _aggregate_agent_tools() -> None

      Aggregate tools from all registered agents.


      .. autolink-examples:: _aggregate_agent_tools
         :collapse:


   .. py:method:: _mark_for_rebuild() -> None

      Mark that graph needs rebuilding.


      .. autolink-examples:: _mark_for_rebuild
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build dynamic supervisor graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: create_with_agents(agents: list[tuple[str, haive.agents.base.Agent, str]], name: str = 'dynamic_supervisor', **kwargs) -> DynamicSupervisor
      :classmethod:


      Create dynamic supervisor with initial agents.

      :param agents: List of (name, agent, capability) tuples
      :param name: Supervisor name
      :param \*\*kwargs: Additional arguments

      :returns: Configured DynamicSupervisor


      .. autolink-examples:: create_with_agents
         :collapse:


   .. py:method:: register_agent(name: str, agent: haive.agents.base.Agent, capability: str) -> None

      Register an agent dynamically.

      :param name: Unique agent name
      :param agent: Agent instance
      :param capability: Capability description


      .. autolink-examples:: register_agent
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup dynamic supervisor with management tools.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:method:: unregister_agent(name: str) -> bool

      Remove an agent dynamically.

      :param name: Agent name to remove

      :returns: True if removed, False if not found


      .. autolink-examples:: unregister_agent
         :collapse:


   .. py:attribute:: agent_capabilities
      :type:  dict[str, str]
      :value: None



   .. py:attribute:: auto_rebuild
      :type:  bool
      :value: None



   .. py:attribute:: enable_tool_aggregation
      :type:  bool
      :value: None



   .. py:attribute:: registered_agents
      :type:  dict[str, haive.agents.base.Agent]
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel]
      :value: None



.. py:class:: DynamicSupervisorState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Enhanced state for dynamic supervisor.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DynamicSupervisorState
      :collapse:

   .. py:attribute:: agent_capabilities
      :type:  dict[str, str]
      :value: None



   .. py:attribute:: messages
      :type:  list[Any]
      :value: None



   .. py:attribute:: needs_rebuild
      :type:  bool
      :value: None



   .. py:attribute:: registered_agents
      :type:  dict[str, haive.agents.base.Agent]
      :value: None



   .. py:attribute:: routing_history
      :type:  list[dict[str, Any]]
      :value: None



.. py:data:: logger

