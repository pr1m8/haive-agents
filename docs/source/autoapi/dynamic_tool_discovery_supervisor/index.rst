
:py:mod:`dynamic_tool_discovery_supervisor`
===========================================

.. py:module:: dynamic_tool_discovery_supervisor

Dynamic Tool Discovery Supervisor with multiple discovery sources.

This module provides DynamicToolDiscoverySupervisor, an advanced supervisor that can
dynamically discover and load tools from multiple sources during runtime, then distribute
them to appropriate agents for task execution.

The supervisor supports multiple discovery modes:
- Component Discovery: Framework-based tool discovery
- RAG Discovery: Document-based tool discovery using RAG agents
- MCP Discovery: External tool discovery via MCP framework
- Hybrid: Combines all discovery methods

.. rubric:: Example

Basic usage with tool discovery::

    from haive.agents.supervisor.dynamic_tool_discovery_supervisor import (
        DynamicToolDiscoverySupervisor,
        ToolDiscoveryMode
    )
    from haive.agents.simple.agent import SimpleAgent
    from haive.agents.react.agent import ReactAgent
    from haive.core.engine.aug_llm import AugLLMConfig

    # Create supervisor with agents
    config = AugLLMConfig(temperature=0.1)
    agents = {
        "analyzer": SimpleAgent(name="analyzer", engine=config),
        "executor": ReactAgent(name="executor", engine=config, tools=[])
    }

    supervisor = DynamicToolDiscoverySupervisor(
        name="tool_supervisor",
        agents=agents,
        engine=config,
        discovery_mode=ToolDiscoveryMode.HYBRID
    )

    # Run task - supervisor will discover needed tools
    result = await supervisor.arun("Calculate compound interest and analyze the results")

Using factory method with discovery sources::

    supervisor = DynamicToolDiscoverySupervisor.create_with_discovery(
        name="discovery_supervisor",
        agents=agents,
        engine=config,
        discovery_mode=ToolDiscoveryMode.HYBRID,
        component_discovery_config={"registry_path": "./components"},
        rag_documents_path="/path/to/tool/docs",
        mcp_config={"endpoint": "http://localhost:8000"}
    )

With initial tools and agents::

    supervisor = DynamicToolDiscoverySupervisor.create_with_agents_and_tools(
        name="configured_supervisor",
        agent_configs=[
            {"type": "SimpleAgent", "name": "worker1"},
            {"type": "ReactAgent", "name": "worker2"}
        ],
        engine=config,
        initial_tools=[calculator_tool, search_tool],
        discovery_mode=ToolDiscoveryMode.COMPONENT_DISCOVERY
    )

.. note::

   This supervisor requires async execution. All main methods return awaitable objects.
   Tool discovery happens automatically based on task analysis, but can also be
   triggered manually using the built-in discover_and_load_tools tool.

.. seealso::

   - :class:`haive.agents.supervisor.base_supervisor.BaseSupervisor`
   - :class:`haive.agents.supervisor.dynamic_activation_supervisor.DynamicActivationSupervisor`
   - :class:`haive.agents.react.dynamic_react_agent.DynamicReactAgent`


.. autolink-examples:: dynamic_tool_discovery_supervisor
   :collapse:

Classes
-------

.. autoapisummary::

   dynamic_tool_discovery_supervisor.DynamicToolDiscoverySupervisor
   dynamic_tool_discovery_supervisor.ToolDiscoveryMode


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DynamicToolDiscoverySupervisor:

   .. graphviz::
      :align: center

      digraph inheritance_DynamicToolDiscoverySupervisor {
        node [shape=record];
        "DynamicToolDiscoverySupervisor" [label="DynamicToolDiscoverySupervisor"];
        "haive.agents.supervisor.base_supervisor.BaseSupervisor" -> "DynamicToolDiscoverySupervisor";
      }

.. autoclass:: dynamic_tool_discovery_supervisor.DynamicToolDiscoverySupervisor
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ToolDiscoveryMode:

   .. graphviz::
      :align: center

      digraph inheritance_ToolDiscoveryMode {
        node [shape=record];
        "ToolDiscoveryMode" [label="ToolDiscoveryMode"];
        "str" -> "ToolDiscoveryMode";
        "enum.Enum" -> "ToolDiscoveryMode";
      }

.. autoclass:: dynamic_tool_discovery_supervisor.ToolDiscoveryMode
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ToolDiscoveryMode** is an Enum defined in ``dynamic_tool_discovery_supervisor``.





.. rubric:: Related Links

.. autolink-examples:: dynamic_tool_discovery_supervisor
   :collapse:
   
.. autolink-skip:: next
