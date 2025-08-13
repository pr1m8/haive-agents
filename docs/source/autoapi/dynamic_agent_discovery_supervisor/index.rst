
:py:mod:`dynamic_agent_discovery_supervisor`
============================================

.. py:module:: dynamic_agent_discovery_supervisor

Dynamic Agent Discovery Supervisor with multiple discovery sources.

This module provides DynamicAgentDiscoverySupervisor, an advanced supervisor that can
dynamically discover and add new agents from multiple sources during runtime.

The supervisor supports multiple discovery modes:
- Component Discovery: Framework-based agent discovery
- RAG Discovery: Document-based agent discovery using RAG
- MCP Discovery: External agent discovery via MCP framework
- Hybrid: Combines all discovery methods

.. rubric:: Example

Basic usage with agent discovery::

    from haive.agents.supervisor.dynamic_agent_discovery_supervisor import (
        DynamicAgentDiscoverySupervisor,
        AgentDiscoveryMode
    )
    from haive.core.engine.aug_llm import AugLLMConfig

    # Create supervisor with initial agents
    config = AugLLMConfig(temperature=0.1)
    initial_agents = {
        "basic_assistant": SimpleAgent(name="basic_assistant", engine=config)
    }

    supervisor = DynamicAgentDiscoverySupervisor(
        name="agent_supervisor",
        agents=initial_agents,
        engine=config,
        discovery_mode=AgentDiscoveryMode.HYBRID
    )

    # Run task - supervisor will discover needed agents
    result = await supervisor.arun("I need an expert to analyze financial data")

Using factory method with discovery sources::

    supervisor = DynamicAgentDiscoverySupervisor.create_with_discovery(
        name="discovery_supervisor",
        agents=initial_agents,
        engine=config,
        discovery_mode=AgentDiscoveryMode.HYBRID,
        component_discovery_config={"registry_path": "./agents"},
        rag_documents_path="/path/to/agent/docs",
        mcp_config={"endpoint": "http://localhost:8000"}
    )

.. note::

   This supervisor requires async execution. Agent discovery happens automatically
   based on task analysis, but can also be triggered manually using the built-in
   discover_and_add_agents tool.

.. seealso::

   - :class:`haive.agents.react.agent.ReactAgent`
   - :class:`haive.agents.supervisor.dynamic_activation_supervisor.DynamicActivationSupervisor`
   - :class:`haive.agents.react.dynamic_react_agent.DynamicReactAgent`


.. autolink-examples:: dynamic_agent_discovery_supervisor
   :collapse:

Classes
-------

.. autoapisummary::

   dynamic_agent_discovery_supervisor.AgentCapability
   dynamic_agent_discovery_supervisor.AgentDiscoveryMode
   dynamic_agent_discovery_supervisor.DynamicAgentDiscoverySupervisor


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgentCapability:

   .. graphviz::
      :align: center

      digraph inheritance_AgentCapability {
        node [shape=record];
        "AgentCapability" [label="AgentCapability"];
        "pydantic.BaseModel" -> "AgentCapability";
      }

.. autopydantic_model:: dynamic_agent_discovery_supervisor.AgentCapability
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





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgentDiscoveryMode:

   .. graphviz::
      :align: center

      digraph inheritance_AgentDiscoveryMode {
        node [shape=record];
        "AgentDiscoveryMode" [label="AgentDiscoveryMode"];
        "str" -> "AgentDiscoveryMode";
        "enum.Enum" -> "AgentDiscoveryMode";
      }

.. autoclass:: dynamic_agent_discovery_supervisor.AgentDiscoveryMode
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **AgentDiscoveryMode** is an Enum defined in ``dynamic_agent_discovery_supervisor``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DynamicAgentDiscoverySupervisor:

   .. graphviz::
      :align: center

      digraph inheritance_DynamicAgentDiscoverySupervisor {
        node [shape=record];
        "DynamicAgentDiscoverySupervisor" [label="DynamicAgentDiscoverySupervisor"];
        "haive.agents.react.agent.ReactAgent" -> "DynamicAgentDiscoverySupervisor";
      }

.. autoclass:: dynamic_agent_discovery_supervisor.DynamicAgentDiscoverySupervisor
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: dynamic_agent_discovery_supervisor
   :collapse:
   
.. autolink-skip:: next
