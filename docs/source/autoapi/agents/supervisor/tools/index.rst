
:py:mod:`agents.supervisor.tools`
=================================

.. py:module:: agents.supervisor.tools

Tools and utilities for Dynamic Supervisor V2.

This module provides tools for agent creation, discovery, matching, and
workflow coordination.


.. autolink-examples:: agents.supervisor.tools
   :collapse:

Classes
-------

.. autoapisummary::

   agents.supervisor.tools.AgentManagementTools


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgentManagementTools:

   .. graphviz::
      :align: center

      digraph inheritance_AgentManagementTools {
        node [shape=record];
        "AgentManagementTools" [label="AgentManagementTools"];
      }

.. autoclass:: agents.supervisor.tools.AgentManagementTools
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.supervisor.tools.create_agent_from_spec
   agents.supervisor.tools.create_handoff_tool
   agents.supervisor.tools.discover_agents
   agents.supervisor.tools.find_matching_agent_specs

.. py:function:: create_agent_from_spec(spec: haive.agents.supervisor.models.AgentSpec) -> Any

   Create an agent instance from a specification.

   This function instantiates the appropriate agent type based on the spec,
   configuring it with the provided settings and tools.

   :param spec: Agent specification containing type, config, and tools

   :returns: Instantiated agent instance

   :raises ValueError: If agent_type is not supported

   .. rubric:: Example

   >>> spec = AgentSpec(
   ...     name="calculator",
   ...     agent_type="ReactAgent",
   ...     config={"temperature": 0.1}
   ... )
   >>> agent = create_agent_from_spec(spec)


   .. autolink-examples:: create_agent_from_spec
      :collapse:

.. py:function:: create_handoff_tool(agent_name: str, description: str) -> langchain_core.tools.BaseTool

   Create a tool for handing off tasks to a specific agent.

   :param agent_name: Name of the agent to hand off to
   :param description: Description of what the agent does

   :returns: Tool that can be used to route tasks to the agent

   .. rubric:: Example

   >>> tool = create_handoff_tool("math_expert", "Handles math problems")
   >>> result = tool.invoke({"task": "Calculate 2+2"})


   .. autolink-examples:: create_handoff_tool
      :collapse:

.. py:function:: discover_agents(task: str, discovery_config: haive.agents.supervisor.models.DiscoveryConfig, existing_agents: set[str] | None = None) -> list[haive.agents.supervisor.models.AgentSpec]

   Discover new agents based on task requirements.

   This function implements various discovery strategies to find or create
   agent specifications that can handle the given task.

   :param task: Task description requiring agents
   :param discovery_config: Configuration for discovery process
   :param existing_agents: Set of already discovered agent names to avoid duplicates

   :returns: List of discovered agent specifications

   .. note::

      Currently implements MANUAL mode. Other modes (COMPONENT_DISCOVERY,
      RAG_DISCOVERY, MCP_DISCOVERY) are planned for future releases.


   .. autolink-examples:: discover_agents
      :collapse:

.. py:function:: find_matching_agent_specs(task: str, available_specs: list[haive.agents.supervisor.models.AgentSpec], threshold: float = 0.3, max_results: int = 5) -> list[haive.agents.supervisor.models.AgentSpec]

   Find agent specifications that match a given task.

   Uses specialty matching and keyword analysis to find the most suitable
   agent specifications for a task.

   :param task: Task description to match against
   :param available_specs: List of available agent specifications
   :param threshold: Minimum match score (0-1) to include a spec
   :param max_results: Maximum number of results to return

   :returns: List of matching specs, sorted by relevance

   .. rubric:: Example

   >>> specs = [math_spec, research_spec, writing_spec]
   >>> matches = find_matching_agent_specs(
   ...     "Calculate the compound interest",
   ...     specs
   ... )
   >>> assert matches[0].name == "math_expert"


   .. autolink-examples:: find_matching_agent_specs
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.supervisor.tools
   :collapse:
   
.. autolink-skip:: next
