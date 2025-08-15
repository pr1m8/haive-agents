dynamic_tool_discovery_supervisor
=================================

.. py:module:: dynamic_tool_discovery_supervisor

.. autoapi-nested-parse::

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

.. py:class:: DynamicToolDiscoverySupervisor

   Bases: :py:obj:`haive.agents.supervisor.base_supervisor.BaseSupervisor`


   Supervisor with dynamic tool discovery and distribution capabilities.

   This supervisor extends BaseSupervisor with the ability to dynamically discover
   tools from multiple sources and distribute them to appropriate agents. It analyzes
   tasks to determine tool requirements and can discover new tools on-demand.

   The supervisor maintains a registry of discovered tools and can route tasks to
   agents based on their tool capabilities. Tool discovery happens automatically
   during task execution but can also be triggered manually.

   .. attribute:: discovery_mode

      Mode for tool discovery (default: HYBRID)

      :type: ToolDiscoveryMode

   .. attribute:: discovery_agent

      Agent for component discovery

      :type: Optional[ComponentDiscoveryAgent]

   .. attribute:: rag_tool_agent

      RAG agent for document-based discovery

      :type: Optional[BaseRAGAgent]

   .. attribute:: mcp_framework

      MCP framework configuration

      :type: Optional[Dict[str, Any]]

   .. attribute:: discovered_tools

      Set of discovered tool names

      :type: Set[str]

   .. attribute:: tool_registry

      Registry mapping tool names to Tool instances

      :type: Dict[str, Tool]

   .. attribute:: max_discovery_attempts

      Maximum discovery attempts per task (default: 3)

      :type: int

   .. attribute:: tools_to_register

      Initial tools for registration

      :type: Optional[List[Dict[str, Any]]]

   .. rubric:: Example

   Creating a supervisor with tool discovery::

       from haive.agents.supervisor.dynamic_tool_discovery_supervisor import (
           DynamicToolDiscoverySupervisor,
           ToolDiscoveryMode
       )

       # Basic creation
       supervisor = DynamicToolDiscoverySupervisor(
           name="main_supervisor",
           agents={
               "worker1": SimpleAgent(...),
               "worker2": ReactAgent(...)
           },
           engine=AugLLMConfig(),
           discovery_mode=ToolDiscoveryMode.HYBRID
       )

       # Run task - tools will be discovered as needed
       result = await supervisor.arun("Analyze data and create visualizations")

       # Check discovered tools
       print(f"Discovered tools: {supervisor.discovered_tools}")

   Using factory methods::

       # With discovery sources configured
       supervisor = DynamicToolDiscoverySupervisor.create_with_discovery(
           name="advanced_supervisor",
           agents=agents,
           engine=config,
           rag_documents_path="/path/to/docs",
           component_discovery_config={"scan_packages": ["haive.tools"]}
       )

       # With pre-configured agents and tools
       supervisor = DynamicToolDiscoverySupervisor.create_with_agents_and_tools(
           name="preset_supervisor",
           agent_configs=[
               {"type": "SimpleAgent", "name": "analyst"},
               {"type": "ReactAgent", "name": "executor"}
           ],
           engine=config,
           initial_tools=[math_tool, search_tool]
       )

   .. note::

      - Tool discovery is asynchronous and may take time for large document sets
      - Discovered tools are cached to avoid redundant discovery
      - Tools are distributed only to agents that support dynamic tool addition
      - The supervisor includes a built-in 'discover_and_load_tools' tool

   :raises ValueError: If invalid discovery mode is provided
   :raises RuntimeError: If discovery agents fail to initialize

   .. seealso::

      - :class:`ToolDiscoveryMode`: Available discovery modes
      - :class:`haive.agents.supervisor.base_supervisor.BaseSupervisor`: Base supervisor class
      - :meth:`create_with_discovery`: Factory method for discovery configuration
      - :meth:`create_with_agents_and_tools`: Factory method for preset configuration


   .. autolink-examples:: DynamicToolDiscoverySupervisor
      :collapse:

   .. py:method:: _add_discovery_tool() -> None

      Add the dynamic tool discovery tool.


      .. autolink-examples:: _add_discovery_tool
         :collapse:


   .. py:method:: _create_decision_prompt(state: haive.agents.supervisor.types.SupervisorState) -> str

      Create prompt for routing decision.


      .. autolink-examples:: _create_decision_prompt
         :collapse:


   .. py:method:: _make_decision(state: haive.agents.supervisor.types.SupervisorState) -> haive.agents.supervisor.types.SupervisorDecision
      :async:


      Make routing decision with tool discovery awareness.

      This method extends the base supervisor's decision-making to consider tool
      availability and discovery needs. It analyzes tasks to determine if tool
      discovery should happen before routing to agents.

      The decision process:
          1. Analyze if the task requires tools based on keywords
          2. Check if tool discovery has been attempted recently
          3. Route to self for tool discovery if needed
          4. Otherwise, make standard routing decision based on agent capabilities

      :param state: Current supervisor state containing messages and agent outputs

      :returns:     - next_agent: str of agent to route to (or self for discovery)
                    - reasoning: Explanation of the routing decision
                    - confidence: Confidence score (0.0-1.0)
                    - suggested_prompt: Optional prompt modification
      :rtype: SupervisorDecision containing

      .. rubric:: Example

      The method automatically detects tool needs::

          # Task: "Calculate the compound interest"
          # Decision: Routes to self first to discover calculator tools

          # Task: "Write a simple greeting"
          # Decision: Routes directly to appropriate agent

      .. note::

         Tool discovery is limited by max_discovery_attempts to prevent
         infinite discovery loops.


      .. autolink-examples:: _make_decision
         :collapse:


   .. py:method:: _parse_decision_response(response: str, state: haive.agents.supervisor.types.SupervisorState) -> haive.agents.supervisor.types.SupervisorDecision

      Parse LLM response into routing decision.


      .. autolink-examples:: _parse_decision_response
         :collapse:


   .. py:method:: _register_tool(tool_data: dict[str, Any]) -> None

      Register a tool in the supervisor's tool registry.

      This method creates a Tool instance from the provided data and registers it
      in both the tool registry and discovered tools set. If agents support dynamic
      tool addition, the tool is also added to them.

      :param tool_data: Dictionary containing tool information with keys:
                        - name (str): Tool name (required)
                        - description (str): Tool description
                        - func (Callable): Tool function (required if not a full tool config)
                        - Other Tool configuration parameters

      .. rubric:: Example

      Registering a tool internally::

          tool_data = {
              "name": "calculator",
              "description": "Performs calculations",
              "func": calculator_function
          }
          supervisor._register_tool(tool_data)

      .. note::

         This is an internal method. Use factory methods or the discover_and_load_tools
         tool for external tool registration.


      .. autolink-examples:: _register_tool
         :collapse:


   .. py:method:: create_with_agents_and_tools(name: str, agent_configs: list[dict[str, Any]], engine: haive.core.engine.aug_llm.AugLLMConfig, initial_tools: list[langchain_core.tools.Tool | dict[str, Any]] | None = None, discovery_mode: ToolDiscoveryMode = ToolDiscoveryMode.HYBRID, **kwargs) -> DynamicToolDiscoverySupervisor
      :classmethod:


      Create supervisor with agents and initial tools.

      :param name: Supervisor name
      :param agent_configs: List of agent configurations
      :param engine: LLM configuration
      :param initial_tools: Initial tools to register
      :param discovery_mode: Tool discovery mode
      :param \*\*kwargs: Additional arguments

      :returns: Configured supervisor


      .. autolink-examples:: create_with_agents_and_tools
         :collapse:


   .. py:method:: create_with_discovery(name: str, agents: dict[str, haive.agents.base.agent.Agent], engine: haive.core.engine.aug_llm.AugLLMConfig, discovery_mode: ToolDiscoveryMode = ToolDiscoveryMode.HYBRID, component_discovery_config: dict[str, Any] | None = None, rag_documents_path: str | None = None, mcp_config: dict[str, Any] | None = None, **kwargs) -> DynamicToolDiscoverySupervisor
      :classmethod:


      Create supervisor with configured discovery sources.

      This factory method creates a supervisor with specific discovery sources
      configured. It handles the setup of ComponentDiscoveryAgent, RAG agent,
      and MCP framework based on the provided configuration.

      :param name: Unique name for the supervisor
      :param agents: Dictionary mapping agent names to Agent instances
      :param engine: LLM configuration for supervisor decision-making
      :param discovery_mode: Tool discovery mode (default: HYBRID)
      :param component_discovery_config: Configuration for ComponentDiscoveryAgent:
                                         - registry_path (str): Path to component registry
                                         - scan_packages (List[str]): Packages to scan for tools
                                         - cache_results (bool): Whether to cache discovery results
      :param rag_documents_path: Path to documents for RAG-based discovery
      :param mcp_config: MCP framework configuration:
                         - endpoint (str): MCP server endpoint
                         - auth_token (str): Authentication token
                         - timeout (int): Request timeout in seconds
      :param \*\*kwargs: Additional arguments passed to supervisor constructor

      :returns: Fully configured DynamicToolDiscoverySupervisor instance

      :raises ValueError: If discovery_mode is invalid
      :raises RuntimeError: If discovery agent initialization fails
      :raises FileNotFoundError: If rag_documents_path doesn't exist

      .. rubric:: Example

      Create supervisor with all discovery sources::

          supervisor = DynamicToolDiscoverySupervisor.create_with_discovery(
              name="full_discovery_supervisor",
              agents={
                  "analyst": SimpleAgent(name="analyst", engine=config),
                  "executor": ReactAgent(name="executor", engine=config)
              },
              engine=AugLLMConfig(temperature=0.1),
              discovery_mode=ToolDiscoveryMode.HYBRID,
              component_discovery_config={
                  "registry_path": "./tool_registry",
                  "scan_packages": ["haive.tools", "custom_tools"]
              },
              rag_documents_path="/docs/tool_documentation",
              mcp_config={
                  "endpoint": "http://mcp.example.com",
                  "auth_token": "secret_token"
              }
          )

      Create with only RAG discovery::

          supervisor = DynamicToolDiscoverySupervisor.create_with_discovery(
              name="rag_supervisor",
              agents=agents,
              engine=config,
              discovery_mode=ToolDiscoveryMode.RAG_DISCOVERY,
              rag_documents_path="./tool_docs"
          )

      .. note::

         - Component discovery requires valid Python packages in scan_packages
         - RAG discovery creates an in-memory vector store from documents
         - MCP discovery requires a running MCP server at the endpoint


      .. autolink-examples:: create_with_discovery
         :collapse:


   .. py:method:: setup_supervisor() -> DynamicToolDiscoverySupervisor

      Set up supervisor after initialization.


      .. autolink-examples:: setup_supervisor
         :collapse:


   .. py:method:: validate_discovery_mode(v: str) -> str
      :classmethod:


      Validate discovery mode.


      .. autolink-examples:: validate_discovery_mode
         :collapse:


   .. py:attribute:: discovered_tools
      :type:  set[str]
      :value: None



   .. py:attribute:: discovery_agent
      :type:  haive.agents.react.dynamic_activation_supervisor.ComponentDiscoveryAgent | None
      :value: None



   .. py:attribute:: discovery_mode
      :type:  ToolDiscoveryMode
      :value: None



   .. py:attribute:: max_discovery_attempts
      :type:  int
      :value: None



   .. py:attribute:: mcp_framework
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: model_config


   .. py:attribute:: rag_tool_agent
      :type:  Any | None
      :value: None



   .. py:attribute:: tool_registry
      :type:  dict[str, langchain_core.tools.Tool]
      :value: None



   .. py:attribute:: tools_to_register
      :type:  list[dict[str, Any]] | None
      :value: None



.. py:class:: ToolDiscoveryMode

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Enumeration of available tool discovery modes.

   .. attribute:: COMPONENT_DISCOVERY

      Use ComponentDiscoveryAgent for framework-based discovery

   .. attribute:: RAG_DISCOVERY

      Use RAG agent for document-based discovery

   .. attribute:: MCP_DISCOVERY

      Use MCP framework for external tool discovery

   .. attribute:: HYBRID

      Combine all discovery methods

   .. rubric:: Example

   Setting discovery mode::

       supervisor = DynamicToolDiscoverySupervisor(
           name="supervisor",
           agents=agents,
           engine=config,
           discovery_mode=ToolDiscoveryMode.RAG_DISCOVERY
       )

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ToolDiscoveryMode
      :collapse:

   .. py:attribute:: COMPONENT_DISCOVERY
      :value: 'component_discovery'



   .. py:attribute:: HYBRID
      :value: 'hybrid'



   .. py:attribute:: MCP_DISCOVERY
      :value: 'mcp_discovery'



   .. py:attribute:: RAG_DISCOVERY
      :value: 'rag_discovery'



