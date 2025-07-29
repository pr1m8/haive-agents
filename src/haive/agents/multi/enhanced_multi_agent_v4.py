"""Enhanced MultiAgent V4 - Advanced multi-agent orchestration with enhanced base agent pattern.

This module provides the EnhancedMultiAgentV4 class, which represents the next generation
of multi-agent coordination in the Haive framework. It leverages the enhanced base agent
pattern to provide sophisticated agent orchestration with clean, intuitive APIs.

The EnhancedMultiAgentV4 extends the base Agent class and implements the required
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
    The EnhancedMultiAgentV4 follows a hierarchical architecture:

    1. **Agent Layer**: Individual agents with their own state and logic
    2. **Orchestration Layer**: Coordination logic and routing decisions
    3. **State Layer**: MultiAgentState for shared and private state management
    4. **Execution Layer**: AgentNodeV3 for proper state projection

Example:
    Basic sequential workflow::

        >>> from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
        >>> from haive.agents.simple import SimpleAgent
        >>> from haive.agents.react import ReactAgent
        >>>
        >>> # Create individual agents
        >>> analyzer = ReactAgent(name="analyzer", tools=[...])
        >>> formatter = SimpleAgent(name="formatter")
        >>>
        >>> # Create multi-agent workflow
        >>> workflow = EnhancedMultiAgentV4(
        ...     name="analysis_pipeline",
        ...     agents=[analyzer, formatter],
        ...     execution_mode="sequential"
        ... )
        >>>
        >>> # Execute workflow
        >>> result = await workflow.arun({"task": "Analyze this data"})

See Also:
    - :class:`haive.agents.base.agent.Agent`: Base agent class
    - :class:`haive.core.schema.prebuilt.multi_agent_state.MultiAgentState`: State management
    - :mod:`haive.core.graph.node.agent_node_v3`: AgentNodeV3 for state projection
    - :class:`haive.core.graph.state_graph.base_graph2.BaseGraph`: Graph building
"""

from __future__ import annotations

import logging
from collections.abc import Callable
from typing import TYPE_CHECKING, Any, Literal

try:
    from typing import Self
except ImportError:
    pass

from haive.core.graph.node.agent_node_v3 import create_agent_node_v3
from haive.core.graph.state_graph.base_graph2 import BaseGraph
from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState
from langgraph.graph import END, START
from pydantic import Field

from haive.agents.base.enhanced_agent import Agent

if TYPE_CHECKING:
    from haive.agents.base.enhanced_agent import Agent

logger = logging.getLogger(__name__)

# Import Agent for runtime


class EnhancedMultiAgentV4(Agent):
    """Enhanced MultiAgent V4 using enhanced base agent pattern.

    This class properly extends the enhanced base Agent class and implements
    the build_graph() abstract method. It provides clean initialization with
    direct list support and flexible execution modes.

    Example:
        >>> # Simple sequential
        >>> workflow = EnhancedMultiAgentV4(
        ...     name="my_workflow",
        ...     agents=[planner, executor, reviewer],
        ...     execution_mode="sequential"
        ... )
        >>>
        >>> # With conditional branching
        >>> workflow = EnhancedMultiAgentV4(
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
    """

    # ========================================================================
    # CORE FIELDS - Enhanced base agent integration
    # ========================================================================

    state_schema: type = Field(
        default=MultiAgentState,
        description="State schema for multi-agent coordination. Defaults to MultiAgentState which "
        "provides agent isolation and shared state management.",
    )

    agents: list[Agent] = Field(
        default_factory=list,
        description="List of Agent instances to coordinate. Agents are automatically converted to "
        "a dictionary keyed by name for efficient lookup during execution.",
    )

    execution_mode: Literal["sequential", "parallel", "conditional", "manual"] = Field(
        default="sequential",
        description="Execution mode determining how agents are connected: "
        "'sequential' - agents run one after another, "
        "'parallel' - all agents run simultaneously, "
        "'conditional' - agents run based on routing logic, "
        "'manual' - user adds edges explicitly",
    )

    build_mode: Literal["auto", "manual", "lazy"] = Field(
        default="auto",
        description="When to build the execution graph: "
        "'auto' - build immediately on initialization, "
        "'manual' - user must call build() explicitly, "
        "'lazy' - build on first execution",
    )

    entry_point: str | None = Field(
        default=None,
        description="Name of the agent to start execution. If None, uses the first agent "
        "in the list. Only relevant for sequential and conditional modes.",
    )

    agent_dict: dict[str, Agent] = Field(
        default_factory=dict,
        description="Internal dictionary mapping agent names to instances. Automatically "
        "populated from the agents list during initialization. Do not set directly.",
    )

    conditional_edges: list[dict[str, Any]] = Field(
        default_factory=list,
        description="Configuration for conditional edges. Each dict should contain: "
        "'from_agent' (source), 'condition' (callable), 'destinations' (routing map), "
        "and optional 'default' (fallback destination).",
    )

    # ========================================================================
    # ENHANCED BASE AGENT SETUP
    # ========================================================================

    def setup_agent(self) -> None:
        """Set up multi-agent configuration before graph building.

        This method is called BEFORE schema generation and graph building,
        allowing us to convert agents list to dict properly.
        """
        # Convert agents list to dict
        if self.agents:
            self.agent_dict = self._convert_agents_to_dict(self.agents)
            logger.info(f"Converted {len(self.agents)} agents to dict")

        # Ensure state schema is MultiAgentState (already set as default)
        if self.state_schema != MultiAgentState:
            logger.warning(
                f"State schema overridden from {
                    self.state_schema} to MultiAgentState"
            )
            self.state_schema = MultiAgentState

    def _convert_agents_to_dict(self, agents: list[Agent]) -> dict[str, Agent]:
        """Convert agent list to dictionary keyed by name.

        This internal method handles the conversion from the user-friendly list
        format to the internal dictionary format used for efficient agent lookup.

        Args:
            agents: List of Agent instances to convert.

        Returns:
            Dict[str, Agent]: Dictionary mapping agent names to agent instances.

        Raises:
            ValueError: If any agent lacks a name attribute.

        Warning:
            If duplicate agent names are found, they are automatically renamed
            with an index suffix (e.g., "agent_1", "agent_2").
        """
        agent_dict = {}

        for i, agent in enumerate(agents):
            if not hasattr(agent, "name") or not agent.name:
                raise ValueError(f"Agent at index {i} must have a name")

            if agent.name in agent_dict:
                # Handle duplicates by adding index
                agent_dict[f"{agent.name}_{i}"] = agent
                logger.warning(
                    f"Duplicate agent name '{
                        agent.name}', using '{
                        agent.name}_{i}'"
                )
            else:
                agent_dict[agent.name] = agent

        return agent_dict

    # ========================================================================
    # ABSTRACT METHOD IMPLEMENTATION - build_graph()
    # ========================================================================

    def build_graph(self) -> BaseGraph:
        """Build the computational graph for multi-agent orchestration.

        This method implements the abstract build_graph() from the base Agent class,
        fulfilling the enhanced base agent pattern. It constructs a BaseGraph that
        defines how agents are connected and how data flows between them.

        The graph structure depends on the execution_mode:
        - **sequential**: Agents execute one after another in order
        - **parallel**: All agents execute simultaneously
        - **conditional**: Agents execute based on conditional routing
        - **manual**: User must add edges manually after creation

        Returns:
            BaseGraph: The constructed graph ready for compilation and execution.

        Raises:
            ValueError: If no agents are available to build the graph.

        Note:
            This method is called automatically based on build_mode:
            - auto: Called during initialization
            - manual: Must be called explicitly via build()
            - lazy: Called on first execution

        Example:
            >>> # Manual build mode
            >>> workflow = EnhancedMultiAgentV4(
            ...     name="custom",
            ...     agents=[agent1, agent2],
            ...     build_mode="manual"
            ... )
            >>> graph = workflow.build_graph()  # Build explicitly
            >>> workflow.add_edge("agent1", "agent2")  # Add custom edges
        """
        if not self.agent_dict:
            raise ValueError("No agents to build graph with")

        logger.info(
            f"Building {self.execution_mode} graph with {len(self.agent_dict)} agents"
        )

        # Create BaseGraph with MultiAgentState
        graph = BaseGraph(
            name=f"{
                self.name}_graph",
            state_schema=self.state_schema or MultiAgentState,
        )

        # Add all agents as nodes using AgentNodeV3
        self._add_agent_nodes(graph)

        # Add edges based on execution mode
        if self.execution_mode == "sequential":
            self._add_sequential_edges(graph)
        elif self.execution_mode == "parallel":
            self._add_parallel_edges(graph)
        elif self.execution_mode == "conditional":
            self._add_conditional_edges(graph)
        elif self.execution_mode == "manual":
            # Manual mode - user adds edges manually
            self._add_manual_edges(graph)

        logger.info("Successfully built multi-agent graph")
        return graph

    def _add_agent_nodes(self, graph: BaseGraph) -> None:
        """Add all agents as nodes to the graph using AgentNodeV3.

        This method creates an AgentNodeV3 for each agent, which provides:
        - Proper state projection from MultiAgentState to agent-specific state
        - Direct field updates for structured output agents
        - Recompilation tracking for dynamic workflows

        Args:
            graph: The BaseGraph instance to add nodes to.

        Note:
            AgentNodeV3 is crucial for maintaining state isolation between agents
            while allowing shared state access through MultiAgentState.
        """
        for agent_name, agent in self.agent_dict.items():
            # Create AgentNodeV3 for proper state projection
            node_config = create_agent_node_v3(agent_name=agent_name, agent=agent)
            graph.add_node(agent_name, node_config)
            logger.debug(f"Added AgentNodeV3 for: {agent_name}")

    def _add_sequential_edges(self, graph: BaseGraph) -> None:
        """Add sequential edges: START -> agent1 -> agent2 -> ... -> END.

        Args:
            graph: The BaseGraph instance to add edges to.
        """
        agent_names = list(self.agent_dict.keys())

        if not agent_names:
            return

        # Determine entry point
        start_agent = (
            self.entry_point if self.entry_point in agent_names else agent_names[0]
        )

        # START -> first agent
        graph.add_edge(START, start_agent)

        # Chain agents sequentially
        for i in range(len(agent_names) - 1):
            current = agent_names[i]
            next_agent = agent_names[i + 1]
            graph.add_edge(current, next_agent)

        # Last agent -> END
        graph.add_edge(agent_names[-1], END)

        logger.info(f"Added sequential edges for {len(agent_names)} agents")

    def _add_parallel_edges(self, graph: BaseGraph) -> None:
        """Add parallel edges: START -> all agents -> END.

        Args:
            graph: The BaseGraph instance to add edges to.
        """
        agent_names = list(self.agent_dict.keys())

        # START -> all agents in parallel
        for agent_name in agent_names:
            graph.add_edge(START, agent_name)
            graph.add_edge(agent_name, END)

        logger.info(f"Added parallel edges for {len(agent_names)} agents")

    def _add_conditional_edges(self, graph: BaseGraph) -> None:
        """Add conditional edges using BaseGraph2.add_conditional_edges().

        Args:
            graph: The BaseGraph instance to add edges to.
        """
        # Start with entry point or first agent
        agent_names = list(self.agent_dict.keys())
        start_agent = (
            self.entry_point if self.entry_point in agent_names else agent_names[0]
        )
        graph.add_edge(START, start_agent)

        # Add configured conditional edges
        for edge_config in self.conditional_edges:
            from_agent = edge_config["from_agent"]
            condition = edge_config["condition"]
            destinations = edge_config["destinations"]
            default = edge_config.get("default", END)

            # Use BaseGraph2's add_conditional_edges
            graph.add_conditional_edges(
                source_node=from_agent,
                condition=condition,
                destinations=destinations,
                default=default,
            )

            logger.debug(f"Added conditional edge from {from_agent}")

        # Ensure unconnected agents go to END
        for agent_name in agent_names:
            # Check if agent has outgoing edges configured
            has_outgoing = any(
                edge["from_agent"] == agent_name for edge in self.conditional_edges
            )
            if not has_outgoing and agent_name != start_agent:
                graph.add_edge(agent_name, END)

        logger.info(f"Added conditional edges for {self.execution_mode} mode")

    def _add_manual_edges(self, graph: BaseGraph) -> None:
        """Manual mode - minimal setup, user adds edges.

        Args:
            graph: The BaseGraph instance to add edges to.
        """
        # Just ensure START connects to entry point
        agent_names = list(self.agent_dict.keys())
        start_agent = (
            self.entry_point if self.entry_point in agent_names else agent_names[0]
        )
        graph.add_edge(START, start_agent)

        logger.info(
            "Manual mode - user must add edges with add_edge() or add_conditional_edge()"
        )

    # ========================================================================
    # USER-FRIENDLY EDGE METHODS
    # ========================================================================

    def add_edge(self, from_agent: str, to_agent: str) -> None:
        """Add a direct edge between two agents in the graph.

        This method creates a simple connection from one agent to another,
        useful for building custom execution flows in manual mode.

        Args:
            from_agent: Name of the source agent.
            to_agent: Name of the destination agent (or END for termination).

        Raises:
            ValueError: If from_agent doesn't exist or to_agent is invalid.

        Example:
            >>> workflow = EnhancedMultiAgentV4(
            ...     agents=[agent1, agent2, agent3],
            ...     execution_mode="manual"
            ... )
            >>> workflow.add_edge("agent1", "agent2")
            >>> workflow.add_edge("agent2", "agent3")
            >>> workflow.add_edge("agent3", END)

        Note:
            If the graph is already built, the edge is added immediately.
            Otherwise, it will be added when the graph is built.
        """
        if from_agent not in self.agent_dict:
            raise ValueError(f"Agent '{from_agent}' not found")
        if to_agent not in self.agent_dict and to_agent != END:
            raise ValueError(f"Agent '{to_agent}' not found")

        # If graph is built, add edge directly
        if hasattr(self, "graph") and self.graph:
            self.graph.add_edge(from_agent, to_agent)
            logger.info(f"Added direct edge: {from_agent} -> {to_agent}")
        else:
            logger.warning("Graph not built yet, edge will be added on build")

    def add_conditional_edge(
        self,
        from_agent: str,
        condition: Callable[[Any], bool],
        true_agent: str,
        false_agent: str = END,
    ) -> None:
        """Add a conditional edge that routes based on a boolean condition.

        This method creates a branching point in the workflow where execution
        can take different paths based on the result of a condition function.

        Args:
            from_agent: Name of the agent where the condition is evaluated.
            condition: Callable that takes the state and returns True or False.
            true_agent: Agent to route to when condition returns True.
            false_agent: Agent to route to when condition returns False (default: END).

        Raises:
            ValueError: If from_agent doesn't exist.

        Example:
            >>> def check_complexity(state):
            ...     return state.get("complexity", 0) > 0.7
            ...
            >>> workflow.add_conditional_edge(
            ...     from_agent="analyzer",
            ...     condition=check_complexity,
            ...     true_agent="complex_processor",
            ...     false_agent="simple_processor"
            ... )

        Note:
            The condition function receives the full MultiAgentState and should
            return a boolean value. For more complex routing, use add_multi_conditional_edge.
        """
        if from_agent not in self.agent_dict:
            raise ValueError(f"Agent '{from_agent}' not found")

        # Store configuration
        edge_config = {
            "from_agent": from_agent,
            "condition": condition,
            "destinations": {True: true_agent, False: false_agent},
            "default": false_agent,
        }
        self.conditional_edges.append(edge_config)

        # If graph is built, add edge directly
        if hasattr(self, "graph") and self.graph:
            self.graph.add_conditional_edges(
                source_node=from_agent,
                condition=condition,
                destinations={True: true_agent, False: false_agent},
                default=false_agent,
            )
            logger.info(f"Added conditional edge from {from_agent}")

        logger.info(
            f"Configured conditional edge: {from_agent} -> {true_agent}/{false_agent}"
        )

    def add_multi_conditional_edge(
        self,
        from_agent: str,
        condition: Callable[[Any], str],
        routes: dict[str, str],
        default: str = END,
    ) -> None:
        """Add multi-way conditional edge with multiple destinations.

        This method creates a branching point where the condition function
        returns a string key that maps to different destination agents.

        Args:
            from_agent: Name of the agent where routing decision is made.
            condition: Callable that returns a route key string.
            routes: Dictionary mapping route keys to agent names.
            default: Default agent when condition returns unmatched key.

        Raises:
            ValueError: If from_agent doesn't exist.

        Example:
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
        """
        if from_agent not in self.agent_dict:
            raise ValueError(f"Agent '{from_agent}' not found")

        # Store configuration
        edge_config = {
            "from_agent": from_agent,
            "condition": condition,
            "destinations": routes,
            "default": default,
        }
        self.conditional_edges.append(edge_config)

        # If graph is built, add edge directly
        if hasattr(self, "graph") and self.graph:
            self.graph.add_conditional_edges(
                source_node=from_agent,
                condition=condition,
                destinations=routes,
                default=default,
            )

        logger.info(
            f"Configured multi-conditional edge from {from_agent} with {len(routes)} routes"
        )

    # ========================================================================
    # UTILITY METHODS
    # ========================================================================

    def get_agent_names(self) -> list[str]:
        """Get list of all agent names in the workflow.

        Returns:
            List[str]: Names of all registered agents.

        Example:
            >>> names = workflow.get_agent_names()
            >>> print(names)  # ['analyzer', 'processor', 'formatter']
        """
        return list(self.agent_dict.keys())

    def get_agent(self, name: str) -> Agent | None:
        """Retrieve an agent instance by name.

        Args:
            name: The name of the agent to retrieve.

        Returns:
            Optional[Agent]: The agent instance if found, None otherwise.

        Example:
            >>> agent = workflow.get_agent("analyzer")
            >>> if agent:
            ...     print(f"Found agent: {agent.name}")
        """
        return self.agent_dict.get(name)

    def add_agent(self, agent: Agent) -> None:
        """Add an agent dynamically to the workflow.

        This method allows adding agents after initialization. If build_mode
        is 'auto', the graph will be automatically rebuilt.

        Args:
            agent: The Agent instance to add.

        Raises:
            ValueError: If agent lacks a name or name already exists.

        Example:
            >>> new_agent = SimpleAgent(name="validator")
            >>> workflow.add_agent(new_agent)

        Note:
            In 'auto' build mode, this triggers graph recompilation.
            In other modes, you must rebuild the graph manually.
        """
        if not agent.name:
            raise ValueError("Agent must have a name")

        if agent.name in self.agent_dict:
            raise ValueError(f"Agent '{agent.name}' already exists")

        self.agent_dict[agent.name] = agent
        self.agents.append(agent)

        # Rebuild graph if auto mode and already built
        if self.build_mode == "auto" and hasattr(self, "graph") and self.graph:
            self.rebuild_graph()

        logger.info(f"Added agent: {agent.name}")

    def display_info(self) -> None:
        """Display detailed information about the workflow configuration.

        This method prints a formatted summary of the workflow including:
        - Execution and build modes
        - Registered agents and their types
        - Number of conditional edges
        - Graph build status

        Example:
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
        """
        for _i, (_name, agent) in enumerate(self.agent_dict.items(), 1):
            type(agent).__name__

    # ========================================================================
    # ENHANCED BASE AGENT INTEGRATION
    # ========================================================================

    # The enhanced base agent provides:
    # - Automatic graph building based on build_mode
    # - Schema generation and management
    # - Persistence capabilities
    # - Standard run/arun interface
    # - All mixin functionality (execution, state, persistence, etc.)

    # We just implement build_graph() and the enhanced base agent handles the
    # rest!
