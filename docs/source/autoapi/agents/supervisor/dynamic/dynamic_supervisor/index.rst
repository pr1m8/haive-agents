agents.supervisor.dynamic.dynamic_supervisor
============================================

.. py:module:: agents.supervisor.dynamic.dynamic_supervisor

.. autoapi-nested-parse::

   DynamicSupervisor - Advanced supervisor with runtime agent management.

   This module provides the DynamicSupervisor class, which extends SupervisorAgent
   with dynamic agent management capabilities. It allows adding and removing agents
   at runtime, with automatic graph rebuilding and tool discovery.

   **Current Status**: This is the **recommended dynamic supervisor** implementation.
   It provides the most complete feature set for runtime agent coordination. For
   basic routing without dynamic features, use SupervisorAgent.

   The DynamicSupervisor extends ReactAgent and adds sophisticated agent lifecycle
   management, making it ideal for adaptive workflows where agents need to be
   added or removed based on runtime conditions.

   Key Features:
       - **Runtime agent management**: Add/remove agents dynamically
       - **Automatic graph rebuilding**: Recompiles graph when agents change
       - **Dynamic tool discovery**: Aggregates tools from all registered agents
       - **Agent capability tracking**: Maintains descriptions of agent capabilities
       - **Performance monitoring**: Tracks routing decisions and agent usage
       - **History tracking**: Maintains routing history for analysis
       - **Hot-swapping**: Replace agents without restarting the supervisor

   Architecture:
       The DynamicSupervisor maintains a registry of agents and rebuilds its
       execution graph whenever agents are added or removed. Tools are dynamically
       discovered and prefixed to avoid conflicts.

   .. rubric:: Example

   Dynamic agent management::

       >>> from haive.agents.supervisor import DynamicSupervisor
       >>> from haive.agents.simple import SimpleAgent
       >>> from haive.core.engine.aug_llm import AugLLMConfig
       >>>
       >>> # Start with empty supervisor
       >>> supervisor = DynamicSupervisor(
       ...     name="dynamic_manager",
       ...     engine=AugLLMConfig(temperature=0.3)
       ... )
       >>>
       >>> # Add agents at runtime
       >>> analyst = SimpleAgent(name="analyst", engine=AugLLMConfig())
       >>> await supervisor.add_agent("analyst", analyst)
       >>>
       >>> # Agent's tools are automatically available
       >>> coder = SimpleAgent(name="coder", tools=[python_repl])
       >>> await supervisor.add_agent("coder", coder)
       >>>
       >>> # Execute task - supervisor routes appropriately
       >>> result = await supervisor.arun("Analyze data and write code")
       >>>
       >>> # Remove agent when no longer needed
       >>> await supervisor.remove_agent("analyst")
       >>>
       >>> # List current agents
       >>> agents = supervisor.list_agents()
       >>> print(f"Active agents: {agents}")

   With capability descriptions::

       >>> # Add agents with explicit capabilities
       >>> await supervisor.register_agent(
       ...     "data_analyst",
       ...     analyst_agent,
       ...     capability="Performs statistical analysis and data visualization"
       ... )
       >>>
       >>> await supervisor.register_agent(
       ...     "ml_engineer",
       ...     ml_agent,
       ...     capability="Builds and trains machine learning models"
       ... )

   .. seealso::

      - :class:`haive.agents.supervisor.SupervisorAgent`: Basic supervisor
      - :class:`haive.agents.supervisor.SimpleSupervisor`: Lightweight routing
      - :class:`haive.agents.react.agent.ReactAgent`: Base class
      - :mod:`haive.agents.supervisor.registry`: Agent registry utilities


   .. autolink-examples:: agents.supervisor.dynamic.dynamic_supervisor
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.supervisor.dynamic.dynamic_supervisor.logger


Classes
-------

.. autoapisummary::

   agents.supervisor.dynamic.dynamic_supervisor.DynamicSupervisor
   agents.supervisor.dynamic.dynamic_supervisor.DynamicSupervisorState


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

