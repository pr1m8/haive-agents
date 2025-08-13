
:py:mod:`agents.supervisor.dynamic.dynamic_supervisor`
======================================================

.. py:module:: agents.supervisor.dynamic.dynamic_supervisor

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

Classes
-------

.. autoapisummary::

   agents.supervisor.dynamic.dynamic_supervisor.DynamicSupervisor
   agents.supervisor.dynamic.dynamic_supervisor.DynamicSupervisorState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DynamicSupervisor:

   .. graphviz::
      :align: center

      digraph inheritance_DynamicSupervisor {
        node [shape=record];
        "DynamicSupervisor" [label="DynamicSupervisor"];
        "haive.agents.react.agent.ReactAgent" -> "DynamicSupervisor";
      }

.. autoclass:: agents.supervisor.dynamic.dynamic_supervisor.DynamicSupervisor
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DynamicSupervisorState:

   .. graphviz::
      :align: center

      digraph inheritance_DynamicSupervisorState {
        node [shape=record];
        "DynamicSupervisorState" [label="DynamicSupervisorState"];
        "pydantic.BaseModel" -> "DynamicSupervisorState";
      }

.. autopydantic_model:: agents.supervisor.dynamic.dynamic_supervisor.DynamicSupervisorState
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. rubric:: Related Links

.. autolink-examples:: agents.supervisor.dynamic.dynamic_supervisor
   :collapse:
   
.. autolink-skip:: next
