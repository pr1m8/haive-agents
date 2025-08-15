dynamic_agent_discovery_supervisor
==================================

.. py:module:: dynamic_agent_discovery_supervisor

.. autoapi-nested-parse::

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


Attributes
----------

.. autoapisummary::

   dynamic_agent_discovery_supervisor.logger


Classes
-------

.. autoapisummary::

   dynamic_agent_discovery_supervisor.AgentCapability
   dynamic_agent_discovery_supervisor.AgentDiscoveryMode
   dynamic_agent_discovery_supervisor.DynamicAgentDiscoverySupervisor


Module Contents
---------------

.. py:class:: AgentCapability(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Description of an agent's capabilities.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgentCapability
      :collapse:

   .. py:attribute:: agent_type
      :type:  str
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: requirements
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: specialties
      :type:  list[str]
      :value: None



   .. py:attribute:: tools
      :type:  list[str]
      :value: None



.. py:class:: AgentDiscoveryMode

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Enumeration of available agent discovery modes.

   .. attribute:: COMPONENT_DISCOVERY

      Use ComponentDiscoveryAgent for framework-based discovery

   .. attribute:: RAG_DISCOVERY

      Use RAG agent for document-based discovery

   .. attribute:: MCP_DISCOVERY

      Use MCP framework for external agent discovery

   .. attribute:: HYBRID

      Combine all discovery methods

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgentDiscoveryMode
      :collapse:

   .. py:attribute:: COMPONENT_DISCOVERY
      :value: 'component_discovery'



   .. py:attribute:: HYBRID
      :value: 'hybrid'



   .. py:attribute:: MCP_DISCOVERY
      :value: 'mcp_discovery'



   .. py:attribute:: RAG_DISCOVERY
      :value: 'rag_discovery'



.. py:class:: DynamicAgentDiscoverySupervisor

   Bases: :py:obj:`haive.agents.react.agent.ReactAgent`


   Supervisor with dynamic agent discovery and registration capabilities.

   This supervisor extends ReactAgent with the ability to dynamically discover
   new agents from multiple sources and add them to its agent registry. It analyzes
   tasks to determine what type of agents are needed and can discover specialists
   on-demand.

   The supervisor maintains a registry of discovered agents and can route tasks to
   newly discovered agents. Agent discovery happens automatically during task
   execution but can also be triggered manually.

   .. attribute:: discovery_mode

      Mode for agent discovery (default: HYBRID)

      :type: AgentDiscoveryMode

   .. attribute:: discovery_agent

      Agent for component discovery

      :type: Optional[ComponentDiscoveryAgent]

   .. attribute:: rag_discovery_agent

      RAG agent for document-based discovery

      :type: Optional[BaseRAGAgent]

   .. attribute:: mcp_framework

      MCP framework configuration

      :type: Optional[Dict[str, Any]]

   .. attribute:: discovered_agents

      Set of discovered agent names

      :type: Set[str]

   .. attribute:: agent_capabilities

      Registry of agent capabilities

      :type: Dict[str, AgentCapability]

   .. attribute:: max_discovery_attempts

      Maximum discovery attempts per task (default: 3)

      :type: int

   .. attribute:: agent_factory

      Registry of agent constructors

      :type: Dict[str, Type[Agent]]

   .. rubric:: Example

   Creating a supervisor with agent discovery::

       supervisor = DynamicAgentDiscoverySupervisor(
           name="main_supervisor",
           agents={
               "generalist": SimpleAgent(name="generalist", engine=config)
           },
           engine=AugLLMConfig(),
           discovery_mode=AgentDiscoveryMode.HYBRID
       )

       # Run task - specialist agents will be discovered as needed
       result = await supervisor.arun("Analyze market trends and write a report")

       # Check discovered agents
       print(f"Discovered agents: {supervisor.discovered_agents}")

   .. note::

      - Agent discovery is asynchronous and may take time
      - Discovered agents are cached to avoid redundant discovery
      - The supervisor includes a built-in 'discover_and_add_agents' tool


   .. autolink-examples:: DynamicAgentDiscoverySupervisor
      :collapse:

   .. py:method:: _add_discovery_tool() -> None

      Add the dynamic agent discovery tool.


      .. autolink-examples:: _add_discovery_tool
         :collapse:


   .. py:method:: _create_decision_prompt(state: haive.agents.supervisor.agent.SupervisorState) -> str

      Create prompt for routing decision.


      .. autolink-examples:: _create_decision_prompt
         :collapse:


   .. py:method:: _make_decision(state: haive.agents.supervisor.agent.SupervisorState) -> haive.agents.supervisor.dynamic_state.SupervisorDecision
      :async:


      Make routing decision with agent discovery awareness.

      This method extends the base supervisor's decision-making to consider
      available agents and discover new ones if needed for the task.

      :param state: Current supervisor state

      :returns: SupervisorDecision with routing information


      .. autolink-examples:: _make_decision
         :collapse:


   .. py:method:: _parse_decision_response(response: str, state: haive.agents.supervisor.agent.SupervisorState) -> haive.agents.supervisor.dynamic_state.SupervisorDecision

      Parse LLM response into routing decision.


      .. autolink-examples:: _parse_decision_response
         :collapse:


   .. py:method:: _register_discovered_agent(agent_data: dict[str, Any]) -> bool

      Register a discovered agent in the supervisor.

      :param agent_data: Dictionary containing agent information:
                         - name: Agent name
                         - agent_type: Type of agent to create
                         - description: Agent description
                         - config: Agent configuration

      :returns: True if agent was successfully registered


      .. autolink-examples:: _register_discovered_agent
         :collapse:


   .. py:method:: create_with_agent_specs(name: str, initial_agent_specs: list[dict[str, Any]], engine: haive.core.engine.aug_llm.AugLLMConfig, discovery_mode: AgentDiscoveryMode = AgentDiscoveryMode.HYBRID, **kwargs) -> DynamicAgentDiscoverySupervisor
      :classmethod:


      Create supervisor with initial agent specifications.

      :param name: Supervisor name
      :param initial_agent_specs: List of agent specifications
      :param engine: LLM configuration
      :param discovery_mode: Agent discovery mode
      :param \*\*kwargs: Additional arguments

      :returns: Configured supervisor

      .. rubric:: Example

      Create with agent specs::

          specs = [
              {
                  "name": "analyst",
                  "agent_type": "ReactAgent",
                  "description": "Data analysis expert",
                  "specialties": ["data", "statistics"],
                  "tools": ["calculator", "data_visualizer"]
              },
              {
                  "name": "writer",
                  "agent_type": "SimpleAgent",
                  "description": "Content writing specialist",
                  "specialties": ["writing", "editing"]
              }
          ]

          supervisor = DynamicAgentDiscoverySupervisor.create_with_agent_specs(
              name="team_supervisor",
              initial_agent_specs=specs,
              engine=config
          )


      .. autolink-examples:: create_with_agent_specs
         :collapse:


   .. py:method:: create_with_discovery(name: str, agents: dict[str, haive.agents.base.agent.Agent], engine: haive.core.engine.aug_llm.AugLLMConfig, discovery_mode: AgentDiscoveryMode = AgentDiscoveryMode.HYBRID, component_discovery_config: dict[str, Any] | None = None, rag_documents_path: str | None = None, mcp_config: dict[str, Any] | None = None, **kwargs) -> DynamicAgentDiscoverySupervisor
      :classmethod:


      Create supervisor with configured discovery sources.

      :param name: Supervisor name
      :param agents: Initial agents dictionary
      :param engine: LLM configuration
      :param discovery_mode: Agent discovery mode
      :param component_discovery_config: Config for component discovery
      :param rag_documents_path: Path to agent documentation
      :param mcp_config: MCP framework configuration
      :param \*\*kwargs: Additional supervisor arguments

      :returns: Configured supervisor with discovery capabilities

      .. rubric:: Example

      Create with all discovery sources::

          supervisor = DynamicAgentDiscoverySupervisor.create_with_discovery(
              name="full_discovery",
              agents={"generalist": SimpleAgent(...)},
              engine=config,
              discovery_mode=AgentDiscoveryMode.HYBRID,
              component_discovery_config={"registry_path": "./agents"},
              rag_documents_path="/docs/agent_specs",
              mcp_config={"endpoint": "http://mcp.example.com"}
          )


      .. autolink-examples:: create_with_discovery
         :collapse:


   .. py:method:: setup_supervisor() -> DynamicAgentDiscoverySupervisor

      Set up supervisor after initialization.


      .. autolink-examples:: setup_supervisor
         :collapse:


   .. py:attribute:: agent_capabilities
      :type:  dict[str, AgentCapability]
      :value: None



   .. py:attribute:: agent_factory
      :type:  dict[str, type[haive.agents.base.agent.Agent]]
      :value: None



   .. py:attribute:: agents
      :type:  dict[str, haive.agents.base.agent.Agent]
      :value: None



   .. py:attribute:: agents_to_register
      :type:  list[dict[str, Any]] | None
      :value: None



   .. py:attribute:: discovered_agents
      :type:  set[str]
      :value: None



   .. py:attribute:: discovery_agent
      :type:  haive.agents.discovery.component_discovery_agent.ComponentDiscoveryAgent | None
      :value: None



   .. py:attribute:: discovery_mode
      :type:  AgentDiscoveryMode
      :value: None



   .. py:attribute:: max_discovery_attempts
      :type:  int
      :value: None



   .. py:attribute:: mcp_framework
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: model_config


   .. py:attribute:: rag_discovery_agent
      :type:  Any | None
      :value: None



.. py:data:: logger

