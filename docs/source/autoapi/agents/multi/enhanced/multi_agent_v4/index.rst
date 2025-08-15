agents.multi.enhanced.multi_agent_v4
====================================

.. py:module:: agents.multi.enhanced.multi_agent_v4

.. autoapi-nested-parse::

   Enhanced MultiAgent V4 - Advanced multi-agent orchestration with enhanced base agent pattern.

   This module provides the MultiAgent class, which represents the **recommended**
   multi-agent coordination implementation in the Haive framework. It leverages the enhanced
   base agent pattern to provide sophisticated agent orchestration with clean, intuitive APIs.

   **Current Status**: This is the **most advanced and recommended** MultiAgent implementation
   for new projects. It provides the cleanest API, best performance, and most complete feature
   set for multi-agent coordination.

   The MultiAgent extends the base Agent class and implements the required
   build_graph() abstract method, enabling it to participate fully in the Haive ecosystem
   while providing advanced multi-agent capabilities.

   Key Features:
       - **Enhanced Base Agent Pattern**: Properly extends Agent and implements build_graph()
       - **Direct List Initialization**: Simple API with agents=[agent1, agent2, ...]
       - **Multiple Execution Modes**: Sequential, parallel, conditional, and manual orchestration
       - **AgentNodeV3 Integration**: Advanced state projection for clean agent isolation
       - **MultiAgentState Management**: Type-safe state handling across agents
       - **Dynamic Graph Building**: Auto, manual, and lazy build modes
       - **Conditional Routing**: Rich conditional edge support via BaseGraph2
       - **Hot Agent Addition**: Add agents dynamically with automatic recompilation

   Architecture:
       The MultiAgent follows a hierarchical architecture:

       1. **Agent Layer**: Individual agents with their own state and logic
       2. **Orchestration Layer**: Coordination logic and routing decisions
       3. **State Layer**: MultiAgentState for shared and private state management
       4. **Execution Layer**: AgentNodeV3 for proper state projection

   .. rubric:: Example

   Basic sequential workflow::

       >>> from haive.agents.multi.agent import MultiAgent
       >>> from haive.agents.simple import SimpleAgent
       >>> from haive.agents.react import ReactAgent
       >>>
       >>> # Create individual agents
       >>> analyzer = ReactAgent(name="analyzer", tools=[...])
       >>> formatter = SimpleAgent(name="formatter")
       >>>
       >>> # Create multi-agent workflow
       >>> workflow = MultiAgent(
       ...     name="analysis_pipeline",
       ...     agents=[analyzer, formatter],
       ...     execution_mode="sequential"
       ... )
       >>>
       >>> # Execute workflow
       >>> result = await workflow.arun({"task": "Analyze this data"})

   Advanced conditional routing::

       >>> # Create workflow with conditional execution
       >>> workflow = MultiAgent(
       ...     name="smart_processor",
       ...     agents=[classifier, simple_processor, complex_processor],
       ...     execution_mode="conditional"
       ... )
       >>>
       >>> # Add routing logic
       >>> workflow.add_conditional_edge(
       ...     from_agent="classifier",
       ...     condition=lambda state: state.get("complexity") > 0.7,
       ...     true_agent="complex_processor",
       ...     false_agent="simple_processor"
       ... )

   Parallel execution with convergence::

       >>> # Create parallel workflow
       >>> workflow = MultiAgent(
       ...     name="parallel_analysis",
       ...     agents=[analyzer1, analyzer2, analyzer3, aggregator],
       ...     execution_mode="manual"
       ... )
       >>>
       >>> # Configure parallel execution
       >>> workflow.add_edge(START, "analyzer1")
       >>> workflow.add_edge(START, "analyzer2")
       >>> workflow.add_edge(START, "analyzer3")
       >>> workflow.add_edge("analyzer1", "aggregator")
       >>> workflow.add_edge("analyzer2", "aggregator")
       >>> workflow.add_edge("analyzer3", "aggregator")
       >>> workflow.add_edge("aggregator", END)

   .. seealso::

      - :class:`haive.agents.base.agent.Agent`: Base agent class
      - :class:`haive.core.schema.prebuilt.multi_agent_state.MultiAgentState`: State management
      - :mod:`haive.core.graph.node.agent_node_v3`: AgentNodeV3 for state projection
      - :class:`haive.core.graph.state_graph.base_graph2.BaseGraph`: Graph building
      - :class:`haive.agents.multi.enhanced_multi_agent_v3.EnhancedMultiAgent`: V3 with generics
      - :class:`haive.agents.multi.clean.MultiAgent`: Current default (being replaced)

   .. note::

      This implementation is planned to become the default MultiAgent in a future release.
      It offers significant improvements over the current clean.py implementation including
      better type safety, cleaner API, and more powerful routing capabilities.


   .. autolink-examples:: agents.multi.enhanced.multi_agent_v4
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.multi.enhanced.multi_agent_v4.logger


Classes
-------

.. autoapisummary::

   agents.multi.enhanced.multi_agent_v4.MultiAgent


Module Contents
---------------

.. py:class:: MultiAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Enhanced MultiAgent V4 using enhanced base agent pattern.

   This class properly extends the enhanced base Agent class and implements
   the build_graph() abstract method. It provides clean initialization with
   direct list support and flexible execution modes.

   .. rubric:: Example

   >>> # Simple sequential
   >>> workflow = MultiAgent(
   ...     name="my_workflow",
   ...     agents=[planner, executor, reviewer],
   ...     execution_mode="sequential"
   ... )
   >>>
   >>> # With conditional branching
   >>> workflow = MultiAgent(
   ...     name="smart_workflow",
   ...     agents=[classifier, simple_processor, complex_processor],
   ...     execution_mode="conditional",
   ...     build_mode="manual"
   ... )
   >>>
   >>> # Add conditional edges
   >>> workflow.add_conditional_edge(
   ...     from_agent="classifier",
   ...     condition=lambda state: state.get("complexity") > 0.7,
   ...     true_agent="complex_processor",
   ...     false_agent="simple_processor"
   ... )
   >>>
   >>> # Build and execute
   >>> workflow.build()
   >>> result = await workflow.arun({"task": "Process this data"})


   .. autolink-examples:: MultiAgent
      :collapse:

   .. py:method:: _add_agent_nodes(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> None

      Add all agents as nodes to the graph using AgentNodeV3.

      This method creates an AgentNodeV3 for each agent, which provides:
      - Proper state projection from MultiAgentState to agent-specific state
      - Direct field updates for structured output agents
      - Recompilation tracking for dynamic workflows

      :param graph: The BaseGraph instance to add nodes to.

      .. note::

         AgentNodeV3 is crucial for maintaining state isolation between agents
         while allowing shared state access through MultiAgentState.


      .. autolink-examples:: _add_agent_nodes
         :collapse:


   .. py:method:: _add_conditional_edges(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> None

      Add conditional edges using BaseGraph2.add_conditional_edges().

      :param graph: The BaseGraph instance to add edges to.


      .. autolink-examples:: _add_conditional_edges
         :collapse:


   .. py:method:: _add_manual_edges(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> None

      Manual mode - minimal setup, user adds edges.

      :param graph: The BaseGraph instance to add edges to.


      .. autolink-examples:: _add_manual_edges
         :collapse:


   .. py:method:: _add_parallel_edges(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> None

      Add parallel edges: START -> all agents -> END.

      :param graph: The BaseGraph instance to add edges to.


      .. autolink-examples:: _add_parallel_edges
         :collapse:


   .. py:method:: _add_sequential_edges(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> None

      Add sequential edges: START -> agent1 -> agent2 -> ... -> END.

      :param graph: The BaseGraph instance to add edges to.


      .. autolink-examples:: _add_sequential_edges
         :collapse:


   .. py:method:: _convert_agents_to_dict(agents: list[haive.agents.base.agent.Agent]) -> dict[str, haive.agents.base.agent.Agent]

      Convert agent list to dictionary keyed by name.

      This internal method handles the conversion from the user-friendly list
      format to the internal dictionary format used for efficient agent lookup.

      :param agents: List of Agent instances to convert.

      :returns: Dictionary mapping agent names to agent instances.
      :rtype: Dict[str, Agent]

      :raises ValueError: If any agent lacks a name attribute.

      .. warning::

         If duplicate agent names are found, they are automatically renamed
         with an index suffix (e.g., "agent_1", "agent_2").


      .. autolink-examples:: _convert_agents_to_dict
         :collapse:


   .. py:method:: add_agent(agent: haive.agents.base.agent.Agent) -> None

      Add an agent dynamically to the workflow.

      This method allows adding agents after initialization. If build_mode
      is 'auto', the graph will be automatically rebuilt.

      :param agent: The Agent instance to add.

      :raises ValueError: If agent lacks a name or name already exists.

      .. rubric:: Example

      >>> new_agent = SimpleAgent(name="validator")
      >>> workflow.add_agent(new_agent)

      .. note::

         In 'auto' build mode, this triggers graph recompilation.
         In other modes, you must rebuild the graph manually.


      .. autolink-examples:: add_agent
         :collapse:


   .. py:method:: add_conditional_edge(from_agent: str, condition: collections.abc.Callable[[Any], bool], true_agent: str, false_agent: str = END) -> None

      Add a conditional edge that routes based on a boolean condition.

      This method creates a branching point in the workflow where execution
      can take different paths based on the result of a condition function.

      :param from_agent: Name of the agent where the condition is evaluated.
      :param condition: Callable that takes the state and returns True or False.
      :param true_agent: Agent to route to when condition returns True.
      :param false_agent: Agent to route to when condition returns False (default: END).

      :raises ValueError: If from_agent doesn't exist.

      .. rubric:: Example

      >>> def check_complexity(state):
      ...     return state.get("complexity", 0) > 0.7
      ...
      >>> workflow.add_conditional_edge(
      ...     from_agent="analyzer",
      ...     condition=check_complexity,
      ...     true_agent="complex_processor",
      ...     false_agent="simple_processor"
      ... )

      .. note::

         The condition function receives the full MultiAgentState and should
         return a boolean value. For more complex routing, use add_multi_conditional_edge.


      .. autolink-examples:: add_conditional_edge
         :collapse:


   .. py:method:: add_edge(from_agent: str, to_agent: str) -> None

      Add a direct edge between two agents in the graph.

      This method creates a simple connection from one agent to another,
      useful for building custom execution flows in manual mode.

      :param from_agent: Name of the source agent.
      :param to_agent: Name of the destination agent (or END for termination).

      :raises ValueError: If from_agent doesn't exist or to_agent is invalid.

      .. rubric:: Example

      >>> workflow = MultiAgent(
      ...     agents=[agent1, agent2, agent3],
      ...     execution_mode="manual"
      ... )
      >>> workflow.add_edge("agent1", "agent2")
      >>> workflow.add_edge("agent2", "agent3")
      >>> workflow.add_edge("agent3", END)

      .. note::

         If the graph is already built, the edge is added immediately.
         Otherwise, it will be added when the graph is built.


      .. autolink-examples:: add_edge
         :collapse:


   .. py:method:: add_multi_conditional_edge(from_agent: str, condition: collections.abc.Callable[[Any], str], routes: dict[str, str], default: str = END) -> None

      Add multi-way conditional edge with multiple destinations.

      This method creates a branching point where the condition function
      returns a string key that maps to different destination agents.

      :param from_agent: Name of the agent where routing decision is made.
      :param condition: Callable that returns a route key string.
      :param routes: Dictionary mapping route keys to agent names.
      :param default: Default agent when condition returns unmatched key.

      :raises ValueError: If from_agent doesn't exist.

      .. rubric:: Example

      >>> def categorize(state):
      ...     return state.get("category", "other")
      ...
      >>> workflow.add_multi_conditional_edge(
      ...     from_agent="categorizer",
      ...     condition=categorize,
      ...     routes={
      ...         "technical": "tech_agent",
      ...         "sales": "sales_agent",
      ...         "support": "support_agent"
      ...     },
      ...     default="general_agent"
      ... )


      .. autolink-examples:: add_multi_conditional_edge
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the computational graph for multi-agent orchestration.

      This method implements the abstract build_graph() from the base Agent class,
      fulfilling the enhanced base agent pattern. It constructs a BaseGraph that
      defines how agents are connected and how data flows between them.

      The graph structure depends on the execution_mode:
      - **sequential**: Agents execute one after another in order
      - **parallel**: All agents execute simultaneously
      - **conditional**: Agents execute based on conditional routing
      - **manual**: User must add edges manually after creation

      :returns: The constructed graph ready for compilation and execution.
      :rtype: BaseGraph

      :raises ValueError: If no agents are available to build the graph.

      .. note::

         This method is called automatically based on build_mode:
         - auto: Called during initialization
         - manual: Must be called explicitly via build()
         - lazy: Called on first execution

      .. rubric:: Example

      >>> # Manual build mode
      >>> workflow = MultiAgent(
      ...     name="custom",
      ...     agents=[agent1, agent2],
      ...     build_mode="manual"
      ... )
      >>> graph = workflow.build_graph()  # Build explicitly
      >>> workflow.add_edge("agent1", "agent2")  # Add custom edges


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: display_info() -> None

      Display detailed information about the workflow configuration.

      This method prints a formatted summary of the workflow including:
      - Execution and build modes
      - Registered agents and their types
      - Number of conditional edges
      - Graph build status

      .. rubric:: Example

      >>> workflow.display_info()
      === Enhanced MultiAgent V4: analysis_pipeline ===
      Execution Mode: sequential
      Build Mode: auto
      Entry Point: analyzer
      Agents (3):
        1. analyzer (ReactAgent)
        2. processor (SimpleAgent)
        3. formatter (SimpleAgent)
      Conditional Edges: 0
      Graph Built: Yes


      .. autolink-examples:: display_info
         :collapse:


   .. py:method:: get_agent(name: str) -> haive.agents.base.agent.Agent | None

      Retrieve an agent instance by name.

      :param name: The name of the agent to retrieve.

      :returns: The agent instance if found, None otherwise.
      :rtype: Optional[Agent]

      .. rubric:: Example

      >>> agent = workflow.get_agent("analyzer")
      >>> if agent:
      ...     print(f"Found agent: {agent.name}")


      .. autolink-examples:: get_agent
         :collapse:


   .. py:method:: get_agent_names() -> list[str]

      Get list of all agent names in the workflow.

      :returns: Names of all registered agents.
      :rtype: List[str]

      .. rubric:: Example

      >>> names = workflow.get_agent_names()
      >>> print(names)  # ['analyzer', 'processor', 'formatter']


      .. autolink-examples:: get_agent_names
         :collapse:


   .. py:method:: setup_agent() -> None

      Set up multi-agent configuration before graph building.

      This method is called BEFORE schema generation and graph building,
      allowing us to convert agents list to dict properly.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: agent_dict
      :type:  dict[str, haive.agents.base.agent.Agent]
      :value: None



   .. py:attribute:: agents
      :type:  list[haive.agents.base.agent.Agent]
      :value: None



   .. py:attribute:: build_mode
      :type:  Literal['auto', 'manual', 'lazy']
      :value: None



   .. py:attribute:: conditional_edges
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: entry_point
      :type:  str | None
      :value: None



   .. py:attribute:: execution_mode
      :type:  Literal['sequential', 'parallel', 'conditional', 'manual']
      :value: None



   .. py:attribute:: state_schema
      :type:  type
      :value: None



.. py:data:: logger

