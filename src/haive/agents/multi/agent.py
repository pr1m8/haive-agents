"""Enhanced MultiAgent V4 - Advanced multi-agent orchestration with enhanced base agent pattern.

This module provides the MultiAgent class, which represents the next generation
of multi-agent coordination in the Haive framework. It leverages the enhanced base agent
pattern to provide sophisticated agent orchestration with clean, intuitive APIs.

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

Example:
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

from langchain_core.messages import AIMessage, BaseMessage
from haive.core.graph.state_graph.base_graph2 import BaseGraph
from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState
from langgraph.graph import END, START
from pydantic import BaseModel, Field

from haive.agents.base.agent import Agent

if TYPE_CHECKING:
    pass

logger = logging.getLogger(__name__)


def _create_agent_wrapper(agent_name: str, agent: Agent) -> Callable:
    """Create a wrapper function that properly converts state between MultiAgentState and sub-agent.

    This wrapper handles the critical state conversion needed for sequential multi-agent
    execution. It extracts messages from the MultiAgentState, invokes the sub-agent's
    compiled graph, and converts the result back to a dict update compatible with
    MultiAgentState.

    The key problem this solves: sub-agents return their own state schema (e.g. LLMState)
    which may contain fields and types incompatible with MultiAgentState. The wrapper
    normalizes the result to only update shared fields (messages, agent_states, agent_outputs).

    Args:
        agent_name: Name of the agent (used for tracking in agent_states/agent_outputs).
        agent: The Agent instance to wrap.

    Returns:
        A callable that accepts (state, config) and returns a dict update for MultiAgentState.
    """

    def _invoke_agent(state: Any, config: Any = None) -> dict[str, Any]:
        """Invoke the sub-agent and return a MultiAgentState-compatible update dict."""
        # Extract messages from the state (handles both dict and Pydantic model)
        if isinstance(state, dict):
            messages = state.get("messages", [])
            agent_states = state.get("agent_states", {})
            agent_outputs = state.get("agent_outputs", {})
        else:
            messages = getattr(state, "messages", [])
            agent_states = getattr(state, "agent_states", {})
            agent_outputs = getattr(state, "agent_outputs", {})

        # Unwrap messages if they have a .root attribute (e.g. RootListModel)
        if hasattr(messages, "root"):
            messages = list(messages.root)
        elif not isinstance(messages, list):
            try:
                messages = list(messages)
            except (TypeError, ValueError):
                messages = []

        # Build the input for the sub-agent: just messages
        agent_input = {"messages": messages}

        # Invoke the sub-agent
        try:
            result = None
            if hasattr(agent, "_app") and agent._app:
                result = agent._app.invoke(agent_input, config)
            elif hasattr(agent, "invoke"):
                result = agent.invoke(agent_input, config)
            else:
                logger.error(f"Agent '{agent_name}' has no invoke method or compiled graph")
                return {"agent_outputs": {**agent_outputs, agent_name: {"error": "No invoke method"}}}
        except Exception as e:
            logger.exception(f"Agent '{agent_name}' execution failed: {e}")
            return {
                "agent_outputs": {**agent_outputs, agent_name: {"error": str(e)}},
                "agent_states": {**agent_states, agent_name: {"executed": True, "error": str(e)}},
            }

        # Extract messages from the result
        result_messages = _extract_messages_from_result(result)

        # Build the state update
        state_update: dict[str, Any] = {}

        # Always update messages if we got any from the result
        if result_messages:
            state_update["messages"] = result_messages

        # Update agent tracking
        state_update["agent_states"] = {
            **agent_states,
            agent_name: {"executed": True, "message_count": len(result_messages)},
        }

        # Store the raw result in agent_outputs for debugging/access
        if isinstance(result, dict):
            output_value = {k: v for k, v in result.items() if k != "messages"}
        elif isinstance(result, BaseModel):
            output_value = {"type": type(result).__name__}
        else:
            output_value = {"raw": str(result)[:500]}

        state_update["agent_outputs"] = {
            **agent_outputs,
            agent_name: output_value,
        }

        return state_update

    return _invoke_agent


def _extract_messages_from_result(result: Any) -> list[BaseMessage]:
    """Extract BaseMessage objects from an agent execution result.

    Handles multiple result formats:
    - dict with 'messages' key (standard LangGraph state output)
    - Pydantic BaseModel with 'messages' attribute
    - list of messages directly
    - string content (wrapped in AIMessage)
    - Any other type (wrapped in AIMessage with str representation)

    Args:
        result: The raw result from agent execution.

    Returns:
        A list of BaseMessage objects extracted from the result.
    """
    if result is None:
        return []

    # Dict result (most common from _app.invoke)
    if isinstance(result, dict):
        messages = result.get("messages", [])
        if messages:
            return _ensure_message_objects(messages)
        # If no messages key, check for content or other text fields
        content = result.get("content") or result.get("output") or result.get("result")
        if content and isinstance(content, str):
            return [AIMessage(content=content)]
        return []

    # Pydantic model result
    if isinstance(result, BaseModel):
        messages = getattr(result, "messages", None)
        if messages:
            return _ensure_message_objects(messages)
        # Try to get content from the model
        content = getattr(result, "content", None) or getattr(result, "output", None)
        if content and isinstance(content, str):
            return [AIMessage(content=content)]
        # Last resort: dump the model to a string
        try:
            return [AIMessage(content=result.model_dump_json())]
        except Exception:
            return [AIMessage(content=str(result))]

    # List of messages
    if isinstance(result, (list, tuple)):
        return _ensure_message_objects(result)

    # String result
    if isinstance(result, str):
        return [AIMessage(content=result)]

    # Fallback: convert to string
    return [AIMessage(content=str(result))]


def _ensure_message_objects(messages: Any) -> list[BaseMessage]:
    """Ensure all items in a messages list are BaseMessage objects.

    Args:
        messages: A list (or list-like) of messages, which may be BaseMessage objects,
            dicts, or other types.

    Returns:
        A list of BaseMessage objects.
    """
    if not messages:
        return []

    # Handle RootListModel or similar wrappers
    if hasattr(messages, "root"):
        messages = list(messages.root)

    result = []
    for msg in messages:
        if isinstance(msg, BaseMessage):
            result.append(msg)
        elif isinstance(msg, dict):
            # Try to convert dict to message
            try:
                from langchain_core.messages import messages_from_dict
                converted = messages_from_dict([msg])
                result.extend(converted)
            except Exception:
                # Fallback: create AIMessage from dict content
                content = msg.get("content", str(msg))
                result.append(AIMessage(content=content))
        elif isinstance(msg, str):
            result.append(AIMessage(content=msg))
        # Skip non-message objects silently
    return result

# Import Agent for runtime


class MultiAgent(Agent):
    """Enhanced MultiAgent V4 using enhanced base agent pattern.

    This class properly extends the enhanced base Agent class and implements
    the build_graph() abstract method. It provides clean initialization with
    direct list support and flexible execution modes.

    Example:
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
                f"State schema overridden from {self.state_schema} to MultiAgentState"
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
                    f"Duplicate agent name '{agent.name}', using '{agent.name}_{i}'"
                )
            else:
                agent_dict[agent.name] = agent

        return agent_dict

    # ========================================================================
    # DYNAMIC AGENT MANAGEMENT
    # ========================================================================

    def add_agent(self, agent: Agent, name: str | None = None) -> None:
        """Add an agent dynamically and rebuild the graph.

        Args:
            agent: Agent instance to add
            name: Override name (defaults to agent.name)
        """
        agent_name = name or getattr(agent, "name", f"agent_{len(self.agent_dict)}")
        self.agent_dict[agent_name] = agent
        self._rebuild()
        logger.info(f"Added agent '{agent_name}' to {self.name}")

    def remove_agent(self, name: str) -> None:
        """Remove an agent and rebuild the graph."""
        if name in self.agent_dict:
            del self.agent_dict[name]
            self._rebuild()
            logger.info(f"Removed agent '{name}' from {self.name}")

    def create_agent(
        self,
        name: str,
        system_message: str,
        description: str | None = None,
        tools: list | None = None,
        temperature: float = 0.7,
    ) -> Agent:
        """Create a new agent on the fly and add it.

        Args:
            name: Agent name
            system_message: System prompt
            description: Optional description
            tools: Optional tools (creates ReactAgent if provided)
            temperature: LLM temperature

        Returns:
            The created agent
        """
        from haive.core.engine.aug_llm import AugLLMConfig

        engine = AugLLMConfig(temperature=temperature, system_message=system_message)

        if tools:
            from haive.agents.react.agent import ReactAgent as RA
            agent = RA(name=name, engine=engine, tools=tools)
        else:
            from haive.agents.simple.agent import SimpleAgent
            agent = SimpleAgent(name=name, engine=engine)

        self.add_agent(agent)
        return agent

    def _rebuild(self) -> None:
        """Rebuild the graph after agent changes."""
        self._is_compiled = False
        self._graph_built = False
        self.graph = None
        self.compile()

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
            >>> workflow = MultiAgent(
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
            name=f"{self.name}_graph", state_schema=self.state_schema or MultiAgentState
        )

        # Add all agents as nodes using wrappers for state conversion
        self._add_agent_nodes(graph)

        # Add edges based on execution mode
        if self.execution_mode == "sequential":
            self._add_sequential_edges(graph)
        elif self.execution_mode == "parallel":
            self._add_parallel_edges(graph)
        elif self.execution_mode == "conditional":
            self._add_conditional_edges(graph)
        elif self.execution_mode == "manual":
            # Manual mode - user adds edges manually after creation
            agent_names = list(self.agent_dict.keys())
            if agent_names:
                graph.add_edge(START, agent_names[0])
                graph.add_edge(agent_names[-1], END)

        logger.info(f"Built {self.execution_mode} graph with {len(self.agent_dict)} agents")
        return graph

    def _add_agent_nodes(self, graph: BaseGraph) -> None:
        """Add all agents as nodes to the graph with proper state conversion.

        This method creates wrapper callables for each agent that handle the critical
        state conversion between MultiAgentState and individual agent state schemas.

        The wrapper ensures that:
        - Messages are properly extracted from MultiAgentState for each sub-agent
        - Agent results (which may be dicts, Pydantic models, strings, etc.) are
          normalized to proper message lists
        - State updates are always compatible with MultiAgentState fields
        - Agent execution is tracked in agent_states and agent_outputs

        Args:
            graph: The BaseGraph instance to add nodes to.
        """
        for agent_name, agent in self.agent_dict.items():
            # Create a wrapper callable that handles state conversion
            wrapper = _create_agent_wrapper(agent_name=agent_name, agent=agent)
            graph.add_node(agent_name, wrapper)
            logger.debug(f"Added agent wrapper node for: {agent_name}")

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
            >>> workflow = MultiAgent(
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

    # add_agent is defined above in DYNAMIC AGENT MANAGEMENT section

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
