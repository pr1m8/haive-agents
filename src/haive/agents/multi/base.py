"""Multi-Agent Base Implementation for the Haive Framework.

This module provides the foundation for building sophisticated multi-agent systems
with flexible execution patterns, intelligent state management, and message
preservation. It serves as the base for all multi-agent implementations in Haive.

The MultiAgent base class and its concrete implementations (SequentialAgent,
ParallelAgent, ConditionalAgent) enable complex agent orchestration patterns
while maintaining proper state isolation and message flow between agents.

Key Features:
    - Multiple execution modes (sequential, parallel, conditional, hierarchical)
    - Automatic schema composition with intelligent field separation
    - Message preservation across agent boundaries (maintains tool_call_id)
    - Private agent state management
    - Conditional branching and routing
    - Engine isolation between agents

Example:
    Basic sequential multi-agent system::

        from haive.agents.multi.base import SequentialAgent
        from haive.agents.react.agent import ReactAgent
        from haive.agents.simple.agent import SimpleAgent

        # Create agents
        planner = SimpleAgent(name="Planner", engine=planning_engine)
        executor = ReactAgent(name="Executor", engine=execution_engine)

        # Create multi-agent system
        system = SequentialAgent(
            name="Planning and Execution System",
            agents=[planner, executor]
        )

        # Run the system
        result = system.run({
            "messages": [HumanMessage(content="Plan and execute: build a web app")]
        })

    Conditional routing example::

        system = ConditionalAgent(
            name="Smart Router",
            agents=[classifier, handler_a, handler_b],
            branches={
                "classifier": {
                    "condition": lambda s: "a" if "urgent" in str(s.messages[-1]) else "b",
                    "mapping": {"a": "handler_a", "b": "handler_b"}
                }
            }
        )

Attributes:
    logger: Module logger for debugging multi-agent execution
    console: Rich console for enhanced output formatting
    ExecutionMode: Enum defining available execution patterns

Note:
    This module uses AgentSchemaComposer with preserve_messages_reducer to ensure
    proper message handling across agent boundaries, preventing loss of fields
    like tool_call_id in ToolMessage objects.
"""

import logging
from abc import abstractmethod
from collections.abc import Sequence
from enum import Enum
from inspect import signature
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Literal,
)
from typing import Optional as Opt
from typing import (
    Set,
    Type,
    Union,
)

from haive.core.graph.state_graph.base_graph2 import BaseGraph
from haive.core.schema.agent_schema_composer import AgentSchemaComposer, BuildMode
from langgraph.graph import END, START
from pydantic import BaseModel, Field, PrivateAttr, model_validator
from rich.console import Console
from rich.tree import Tree

from haive.agents.base.agent import Agent

logger = logging.getLogger(__name__)
console = Console()


class ExecutionMode(str, Enum):
    """Execution modes defining how agents are orchestrated.

    Each mode represents a different pattern for agent coordination:

    Attributes:
        SEQUENCE: Agents execute one after another with state flowing between them.
            Best for step-by-step workflows where each agent depends on the previous.
        PARALLEL: All agents execute independently on the same input.
            Best for independent analysis or consensus building.
        CONDITIONAL: Dynamic routing based on conditions or agent outputs.
            Best for adaptive workflows with branching logic.
        HIERARCHICAL: Supervisor-worker patterns with parent-child relationships.
            Best for task delegation and hierarchical planning.
    """

    SEQUENCE = "sequence"  # Execute agents in order
    PARALLEL = "parallel"  # Execute agents in parallel
    CONDITIONAL = "conditional"  # Use conditional routing
    HIERARCHICAL = "hierarchical"  # Parent-child execution


class MultiAgent(Agent):
    """Abstract base class for sophisticated multi-agent systems.

    MultiAgent provides the foundation for building complex agent orchestration
    patterns with automatic state management, message preservation, and flexible
    execution modes. It handles the complexity of multi-agent coordination while
    maintaining clean abstractions for different patterns.

    Key capabilities:
        - Automatic schema composition from child agents with intelligent field separation
        - Multiple execution modes (sequential, parallel, conditional, hierarchical)
        - Private agent state management with proper isolation
        - Complex routing patterns via conditional edges and branching
        - Meta state for agent coordination and shared context
        - Message preservation ensuring tool_call_id and other fields remain intact
        - Engine isolation preventing tool contamination between agents

    The class uses AgentSchemaComposer to automatically build appropriate state
    schemas based on the agents and execution mode, ensuring proper field sharing
    and message flow between agents.

    Attributes:
        name: Name of the multi-agent system
        agents: Sequence of child agents to orchestrate
        execution_mode: How agents should be executed (sequence, parallel, etc.)
        include_meta: Whether to include MetaAgentState for coordination
        schema_separation: Strategy for field separation ("smart", "shared", "namespaced")
        branches: Configuration for conditional routing between agents

    Example:
        Creating a multi-agent system::

            # Define agents
            agents = [research_agent, analysis_agent, report_agent]

            # Create system
            system = SequentialAgent(
                name="Research Pipeline",
                agents=agents,
                schema_separation="smart"  # Intelligent field sharing
            )

            # The system automatically:
            # - Composes schemas from all agents
            # - Sets up message preservation
            # - Configures execution flow
            # - Manages state transitions

    Note:
        This is an abstract class. Use SequentialAgent, ParallelAgent,
        ConditionalAgent, or create a custom subclass for specific patterns.
    """

    # Configuration
    name: str = Field(
        default="Multi Agent", description="Name of the multi-agent system"
    )
    agents: Sequence[Agent] = Field(
        default_factory=list, description="List of agents in this multi-agent system"
    )
    execution_mode: ExecutionMode = Field(
        default=ExecutionMode.SEQUENCE, description="How agents should be executed"
    )

    # Schema configuration
    include_meta: bool = Field(
        default=True, description="Whether to include MetaAgentState for coordination"
    )
    schema_separation: Literal["smart", "shared", "namespaced"] = Field(
        default="smart", description="How to handle field separation in composed schema"
    )

    # Branching configuration
    branches: dict[str, dict[str, Any]] = Field(
        default_factory=dict,
        description="Branch configurations keyed by source node name",
    )

    # Private state management
    _agent_private_states: dict[str, type[BaseModel]] = PrivateAttr(
        default_factory=dict
    )
    _agent_node_mapping: dict[str, str] = PrivateAttr(default_factory=dict)

    @model_validator(mode="before")
    @classmethod
    def validate_agents(cls, values: dict[str, Any]) -> dict[str, Any]:
        """Ensure agents list is not empty."""
        if isinstance(values, dict):
            agents = values.get("agents", [])
            if not agents:
                raise ValueError("MultiAgent requires at least one agent")
        return values

    @model_validator(mode="after")
    def setup_multi_agent(self) -> "MultiAgent":
        """Set up the multi-agent system after initialization."""
        # Generate schema based on execution mode
        build_mode = self._get_build_mode()

        # Compose state schema from agents
        self.state_schema = AgentSchemaComposer.from_agents(
            agents=list(self.agents),
            name=f"{self.__class__.__name__}State",
            include_meta=self.include_meta,
            separation=self.schema_separation,
            build_mode=build_mode,
        )

        # Store private schemas for each agent
        for agent in self.agents:
            agent_id = getattr(agent, "id", agent.name)
            if hasattr(agent, "state_schema") and agent.state_schema:
                self._agent_private_states[agent_id] = agent.state_schema

        # Set input/output schemas
        self._setup_io_schemas()

        return self

    def _get_build_mode(self) -> BuildMode:
        """Map execution mode to schema build mode.

        Determines the appropriate schema composition strategy based on
        the multi-agent execution pattern. This ensures fields are properly
        shared or isolated based on how agents will interact.

        Returns:
            BuildMode enum value for schema composition

        Mapping:
            - SEQUENCE → BuildMode.SEQUENCE (fields flow between agents)
            - PARALLEL → BuildMode.PARALLEL (isolated execution)
            - CONDITIONAL → BuildMode.SEQUENCE (with branching)
            - HIERARCHICAL → BuildMode.HIERARCHICAL (parent-child)
        """
        mode_mapping = {
            ExecutionMode.SEQUENCE: BuildMode.SEQUENCE,
            ExecutionMode.PARALLEL: BuildMode.PARALLEL,
            ExecutionMode.CONDITIONAL: BuildMode.SEQUENCE,  # Use sequence for conditional
            ExecutionMode.HIERARCHICAL: BuildMode.HIERARCHICAL,
        }
        return mode_mapping.get(self.execution_mode, BuildMode.CUSTOM)

    def _setup_io_schemas(self) -> None:
        """Set up input and output schemas based on execution mode."""
        if self.execution_mode == ExecutionMode.SEQUENCE:
            # Input from first agent, output from last
            if self.agents:
                first_agent = self.agents[0]

                # Use first agent's input schema or derive from state
                if hasattr(first_agent, "input_schema") and first_agent.input_schema:
                    self.input_schema = first_agent.input_schema
                else:
                    self.input_schema = self.state_schema.derive_input_schema()

                # FIXED: Always use state schema for output, not individual agent's output schema
                # This ensures the output matches the actual state structure with messages
                self.output_schema = self.state_schema.derive_output_schema()
        else:
            # For other modes, derive from state schema
            self.input_schema = self.state_schema.derive_input_schema()
            self.output_schema = self.state_schema.derive_output_schema()

    def add_conditional_edge(
        self,
        source_agent: str | Agent,
        condition: Callable[[Any], str | bool],
        destinations: dict[str | bool, str | Agent],
        default: str | Agent | None = None,
    ) -> None:
        """Add a conditional edge between agents.

        Args:
            source_agent: Source agent or its name/id
            condition: Function that returns a routing key
            destinations: Mapping of condition results to target agents
            default: Default destination if no match
        """
        # Normalize source
        source_name = self._get_node_name(source_agent)

        # Normalize destinations
        normalized_dests = {}
        for key, dest in destinations.items():
            dest_name = self._get_node_name(dest) if dest != END else END
            normalized_dests[key] = dest_name

        # Store branch configuration
        self.branches[source_name] = {
            "condition": condition,
            "destinations": normalized_dests,
            "default": (
                self._get_node_name(default) if default and default != END else default
            ),
        }

    def _get_node_name(self, agent: str | Agent) -> str:
        """Get the node name for an agent."""
        if isinstance(agent, str):
            # Could be agent name or id
            for a in self.agents:
                if getattr(a, "name", None) == agent or getattr(a, "id", None) == agent:
                    return self._get_agent_node_name(a)
            return agent  # Assume it's a node name
        if isinstance(agent, Agent):
            return self._get_agent_node_name(agent)
        raise ValueError(f"Invalid agent reference: {agent}")

    def _get_agent_node_name(self, agent: Agent) -> str:
        """Get the unique node name for an agent."""
        base_name = getattr(agent, "name", agent.__class__.__name__)
        agent_id = getattr(agent, "id", base_name)

        # Ensure uniqueness
        if agent_id not in self._agent_node_mapping:
            node_name = base_name
            counter = 1
            while any(
                node_name == existing for existing in self._agent_node_mapping.values()
            ):
                node_name = f"{base_name}_{counter}"
                counter += 1
            self._agent_node_mapping[agent_id] = node_name

        return self._agent_node_mapping[agent_id]

    def build_graph(self) -> BaseGraph:
        """Build the graph based on execution mode."""
        graph = BaseGraph(name=self.name)

        # Build based on execution mode
        if self.execution_mode == ExecutionMode.SEQUENCE:
            self._build_sequence_graph(graph)
        elif self.execution_mode == ExecutionMode.PARALLEL:
            self._build_parallel_graph(graph)
        elif self.execution_mode == ExecutionMode.CONDITIONAL:
            self._build_conditional_graph(graph)
        elif self.execution_mode == ExecutionMode.HIERARCHICAL:
            self._build_hierarchical_graph(graph)
        else:
            # Custom mode - must be implemented by subclass
            graph = self.build_custom_graph(graph)

        return graph

    def _build_sequence_graph(self, graph: BaseGraph) -> None:
        """Build a sequential execution graph."""
        node_names = []

        # Add all agents as nodes
        for agent in self.agents:
            node_name = self._get_agent_node_name(agent)
            node_names.append(node_name)

            # Create agent node config
            from haive.core.graph.node.agent_node import AgentNodeConfig

            agent_node = AgentNodeConfig(
                name=node_name,
                agent=agent,
                private_state_schema=self._agent_private_states.get(
                    getattr(agent, "id", agent.name)
                ),
            )
            graph.add_node(node_name, agent_node)

        # Connect in sequence
        for i, node_name in enumerate(node_names):
            if i == 0:
                graph.add_edge(START, node_name)

            # Check for branches
            if node_name in self.branches:
                branch_config = self.branches[node_name]
                graph.add_conditional_edges(
                    node_name,
                    branch_config["condition"],
                    branch_config["destinations"],
                    default=branch_config.get(
                        "default",
                        END if i == len(node_names) - 1 else node_names[i + 1],
                    ),
                )
            # Normal sequential edge
            elif i == len(node_names) - 1:
                graph.add_edge(node_name, END)
            else:
                graph.add_edge(node_name, node_names[i + 1])

    def _build_parallel_graph(self, graph: BaseGraph) -> None:
        """Build a parallel execution graph."""
        # Create a coordinator node
        coordinator_name = f"{self.name}_coordinator"

        # Add coordinator that fans out
        from haive.core.graph.node.agent_node import CoordinatorNodeConfig

        coordinator = CoordinatorNodeConfig(
            name=coordinator_name, agents=list(self.agents), mode="fanout"
        )
        graph.add_node(coordinator_name, coordinator)
        graph.add_edge(START, coordinator_name)

        # Add all agents
        agent_nodes = []
        for agent in self.agents:
            node_name = self._get_agent_node_name(agent)
            agent_nodes.append(node_name)

            from haive.core.graph.node.agent_node import AgentNodeConfig

            agent_node = AgentNodeConfig(
                name=node_name,
                agent=agent,
                private_state_schema=self._agent_private_states.get(
                    getattr(agent, "id", agent.name)
                ),
            )
            graph.add_node(node_name, agent_node)
            graph.add_edge(coordinator_name, node_name)

        # Create aggregator node
        aggregator_name = f"{self.name}_aggregator"
        aggregator = CoordinatorNodeConfig(
            name=aggregator_name, agents=list(self.agents), mode="aggregate"
        )
        graph.add_node(aggregator_name, aggregator)

        # Connect all agents to aggregator
        for node_name in agent_nodes:
            graph.add_edge(node_name, aggregator_name)

        graph.add_edge(aggregator_name, END)

    def _build_conditional_graph(self, graph: BaseGraph) -> None:
        """Build a conditional execution graph."""
        # Start with sequence and add conditional edges
        self._build_sequence_graph(graph)
        # Conditional edges are already added in sequence building

    def _build_hierarchical_graph(self, graph: BaseGraph) -> None:
        """Build a hierarchical execution graph."""
        # Default implementation - can be overridden
        logger.warning("Hierarchical mode not fully implemented, using sequence")
        self._build_sequence_graph(graph)

    @abstractmethod
    def build_custom_graph(self, graph: BaseGraph) -> BaseGraph:
        """Build a custom graph - must be implemented by subclasses if using CUSTOM mode.

        Args:
            graph: The graph to build on

        Returns:
            The modified graph
        """
        raise NotImplementedError(
            "Subclasses must implement build_custom_graph for CUSTOM mode"
        )

    def get_agent_by_name(self, name: str) -> Agent | None:
        """Get an agent by name or id."""
        for agent in self.agents:
            if (
                getattr(agent, "name", None) == name
                or getattr(agent, "id", None) == name
            ):
                return agent
        return None

    def analyze_io_compatibility(self) -> Dict[str, Any]:
        """Analyze I/O schema compatibility between agents.

        Returns:
            Dict with compatibility analysis including:
            - compatible_pairs: List of (agent1, agent2) tuples with compatible I/O
            - schema_fields: Field mapping across agents
            - routing_suggestions: Suggested routing based on compatibility
        """
        compatible_pairs = []
        schema_fields = {}
        routing_suggestions = []

        for i, agent1 in enumerate(self.agents):
            for j, agent2 in enumerate(self.agents[i + 1 :], i + 1):
                compatibility = self._check_agent_compatibility(agent1, agent2)
                if compatibility["compatible"]:
                    compatible_pairs.append((agent1.name, agent2.name))

        # Analyze field mappings
        for agent in self.agents:
            agent_fields = self._extract_agent_fields(agent)
            schema_fields[agent.name] = agent_fields

        # Generate routing suggestions based on I/O compatibility
        routing_suggestions = self._generate_routing_suggestions(schema_fields)

        return {
            "compatible_pairs": compatible_pairs,
            "schema_fields": schema_fields,
            "routing_suggestions": routing_suggestions,
            "total_agents": len(self.agents),
            "compatibility_matrix": self._build_compatibility_matrix(),
        }

    def _check_agent_compatibility(
        self, agent1: Agent, agent2: Agent
    ) -> Dict[str, Any]:
        """Check if two agents have compatible I/O schemas.

        Args:
            agent1: First agent
            agent2: Second agent

        Returns:
            Dict with compatibility information
        """
        agent1_outputs = self._get_agent_output_fields(agent1)
        agent2_inputs = self._get_agent_input_fields(agent2)

        # Check for overlapping fields
        common_fields = agent1_outputs.intersection(agent2_inputs)

        # Always compatible if they share messages (base communication)
        has_messages = "messages" in common_fields

        # Check for structured output compatibility
        has_structured_overlap = len(common_fields - {"messages"}) > 0

        compatibility_score = len(common_fields) / max(len(agent2_inputs), 1)

        return {
            "compatible": has_messages or has_structured_overlap,
            "common_fields": list(common_fields),
            "compatibility_score": compatibility_score,
            "can_chain_directly": compatibility_score > 0.5,
            "requires_adapter": compatibility_score < 0.3 and compatibility_score > 0,
        }

    def _extract_agent_fields(self, agent: Agent) -> Dict[str, Set[str]]:
        """Extract input/output fields from an agent.

        Args:
            agent: Agent to analyze

        Returns:
            Dict with 'inputs' and 'outputs' field sets
        """
        inputs = self._get_agent_input_fields(agent)
        outputs = self._get_agent_output_fields(agent)

        return {
            "inputs": inputs,
            "outputs": outputs,
            "state_schema": (
                getattr(agent.state_schema, "__name__", "Unknown")
                if agent.state_schema
                else None
            ),
            "engine_types": [
                getattr(engine, "engine_type", "unknown")
                for engine in getattr(agent, "engines", {}).values()
            ],
        }

    def _get_agent_input_fields(self, agent: Agent) -> Set[str]:
        """Get input fields for an agent."""
        fields = set()

        # From input schema
        if hasattr(agent, "input_schema") and agent.input_schema:
            if hasattr(agent.input_schema, "model_fields"):
                fields.update(agent.input_schema.model_fields.keys())

        # From state schema
        if hasattr(agent, "state_schema") and agent.state_schema:
            if hasattr(agent.state_schema, "model_fields"):
                fields.update(agent.state_schema.model_fields.keys())

        # From engines
        if hasattr(agent, "engines"):
            for engine in agent.engines.values():
                if hasattr(engine, "get_input_fields"):
                    try:
                        engine_inputs = engine.get_input_fields()
                        fields.update(engine_inputs.keys())
                    except:
                        pass

        # Always assume messages as basic communication
        fields.add("messages")
        return fields

    def _get_agent_output_fields(self, agent: Agent) -> Set[str]:
        """Get output fields for an agent."""
        fields = set()

        # From output schema
        if hasattr(agent, "output_schema") and agent.output_schema:
            if hasattr(agent.output_schema, "model_fields"):
                fields.update(agent.output_schema.model_fields.keys())

        # From state schema
        if hasattr(agent, "state_schema") and agent.state_schema:
            if hasattr(agent.state_schema, "model_fields"):
                fields.update(agent.state_schema.model_fields.keys())

        # From engines
        if hasattr(agent, "engines"):
            for engine in agent.engines.values():
                if hasattr(engine, "get_output_fields"):
                    try:
                        engine_outputs = engine.get_output_fields()
                        fields.update(engine_outputs.keys())
                    except:
                        pass

        # Common output fields
        fields.update(["messages", "response", "generated_text"])
        return fields

    def _generate_routing_suggestions(
        self, schema_fields: Dict[str, Dict[str, Set[str]]]
    ) -> List[Dict[str, Any]]:
        """Generate routing suggestions based on schema compatibility."""
        suggestions = []

        agent_names = list(schema_fields.keys())

        for i, source in enumerate(agent_names):
            for j, target in enumerate(agent_names):
                if i != j:
                    source_outputs = schema_fields[source]["outputs"]
                    target_inputs = schema_fields[target]["inputs"]

                    common = source_outputs.intersection(target_inputs)
                    if len(common) > 1:  # More than just messages
                        suggestions.append(
                            {
                                "from": source,
                                "to": target,
                                "shared_fields": list(common),
                                "confidence": (
                                    len(common) / len(target_inputs)
                                    if target_inputs
                                    else 0
                                ),
                                "routing_type": (
                                    "direct" if len(common) > 2 else "conditional"
                                ),
                            }
                        )

        # Sort by confidence
        suggestions.sort(key=lambda x: x["confidence"], reverse=True)
        return suggestions[:10]  # Top 10 suggestions

    def _build_compatibility_matrix(self) -> List[List[float]]:
        """Build compatibility matrix between all agents."""
        n = len(self.agents)
        matrix = [[0.0 for _ in range(n)] for _ in range(n)]

        for i, agent1 in enumerate(self.agents):
            for j, agent2 in enumerate(self.agents):
                if i != j:
                    compatibility = self._check_agent_compatibility(agent1, agent2)
                    matrix[i][j] = compatibility["compatibility_score"]
                else:
                    matrix[i][j] = 1.0  # Self-compatibility

        return matrix

    def suggest_optimal_routing(self, start_agent: str, end_agent: str) -> List[str]:
        """Suggest optimal routing path between two agents.

        Args:
            start_agent: Starting agent name
            end_agent: Target agent name

        Returns:
            List of agent names forming the optimal path
        """
        compatibility = self.analyze_io_compatibility()
        matrix = compatibility["compatibility_matrix"]

        # Simple pathfinding based on compatibility scores
        agent_names = [agent.name for agent in self.agents]

        try:
            start_idx = agent_names.index(start_agent)
            end_idx = agent_names.index(end_agent)
        except ValueError:
            return [start_agent, end_agent]  # Fallback

        # Find path with highest cumulative compatibility
        # For now, simple direct connection or through best intermediate
        direct_score = matrix[start_idx][end_idx]

        best_path = [start_agent, end_agent]
        best_score = direct_score

        # Check single intermediate paths
        for i, intermediate in enumerate(agent_names):
            if i != start_idx and i != end_idx:
                score1 = matrix[start_idx][i]
                score2 = matrix[i][end_idx]
                total_score = score1 * score2  # Multiplicative score

                if total_score > best_score:
                    best_path = [start_agent, intermediate, end_agent]
                    best_score = total_score

        return best_path

    def create_adaptive_routing(
        self, routing_conditions: Dict[str, Callable[[Any], str]]
    ) -> Dict[str, Dict[str, Any]]:
        """Create adaptive routing based on I/O compatibility and conditions.

        Args:
            routing_conditions: Dict mapping agent names to condition functions

        Returns:
            Routing configuration for ConditionalAgent
        """
        compatibility = self.analyze_io_compatibility()
        routing_config = {}

        for agent_name, condition_func in routing_conditions.items():
            # Find compatible targets for this agent
            compatible_targets = []

            for suggestion in compatibility["routing_suggestions"]:
                if suggestion["from"] == agent_name:
                    compatible_targets.append(suggestion["to"])

            if compatible_targets:
                # Create routing mapping
                def create_router(targets, condition):
                    def router(state: Any) -> str:
                        result = condition(state)
                        if result in targets:
                            return result
                        return targets[0] if targets else "END"

                    return router

                routing_config[agent_name] = {
                    "condition": create_router(compatible_targets, condition_func),
                    "destinations": {target: target for target in compatible_targets},
                    "default": compatible_targets[0] if compatible_targets else "END",
                }

        return routing_config

    def replace_agent_by_compatibility(
        self,
        target_agent_name: str,
        replacement_agent: Agent,
        check_compatibility: bool = True,
    ) -> bool:
        """Replace an agent with another based on I/O compatibility.

        Args:
            target_agent_name: Name of agent to replace
            replacement_agent: New agent to use
            check_compatibility: Whether to verify compatibility

        Returns:
            True if replacement successful, False otherwise
        """
        target_idx = None
        for i, agent in enumerate(self.agents):
            if agent.name == target_agent_name:
                target_idx = i
                break

        if target_idx is None:
            return False

        if check_compatibility:
            # Check compatibility with neighbors
            old_agent = self.agents[target_idx]

            # Check with previous agent
            if target_idx > 0:
                prev_agent = self.agents[target_idx - 1]
                compat = self._check_agent_compatibility(prev_agent, replacement_agent)
                if not compat["compatible"]:
                    logger.warning(
                        f"Replacement agent {replacement_agent.name} not compatible with previous agent {prev_agent.name}"
                    )
                    return False

            # Check with next agent
            if target_idx < len(self.agents) - 1:
                next_agent = self.agents[target_idx + 1]
                compat = self._check_agent_compatibility(replacement_agent, next_agent)
                if not compat["compatible"]:
                    logger.warning(
                        f"Replacement agent {replacement_agent.name} not compatible with next agent {next_agent.name}"
                    )
                    return False

        # Perform replacement
        self.agents = list(self.agents)  # Convert to list if needed
        self.agents[target_idx] = replacement_agent

        # Update node mapping
        old_agent_id = getattr(self.agents[target_idx], "id", target_agent_name)
        if old_agent_id in self._agent_node_mapping:
            del self._agent_node_mapping[old_agent_id]

        # Regenerate schema
        build_mode = self._get_build_mode()
        self.state_schema = AgentSchemaComposer.from_agents(
            agents=list(self.agents),
            name=f"{self.__class__.__name__}State",
            include_meta=self.include_meta,
            separation=self.schema_separation,
            build_mode=build_mode,
        )

        logger.info(
            f"Successfully replaced agent {target_agent_name} with {replacement_agent.name}"
        )
        return True

    def optimize_agent_order(self) -> List[Agent]:
        """Optimize agent order based on I/O compatibility.

        Returns:
            Reordered list of agents for better flow
        """
        if len(self.agents) <= 2:
            return list(self.agents)

        compatibility = self.analyze_io_compatibility()
        matrix = compatibility["compatibility_matrix"]

        # Simple greedy optimization
        optimized = []
        remaining = list(range(len(self.agents)))

        # Start with agent that has highest total outgoing compatibility
        start_scores = [sum(matrix[i]) for i in range(len(self.agents))]
        current = start_scores.index(max(start_scores))

        optimized.append(self.agents[current])
        remaining.remove(current)

        # Greedily add most compatible next agent
        while remaining:
            best_next = None
            best_score = -1

            for candidate in remaining:
                score = matrix[current][candidate]
                if score > best_score:
                    best_score = score
                    best_next = candidate

            if best_next is not None:
                optimized.append(self.agents[best_next])
                remaining.remove(best_next)
                current = best_next
            else:
                # Add remaining in original order
                optimized.extend([self.agents[i] for i in remaining])
                break

        return optimized

    def _serialize_tool_for_state(self, tool: Any) -> dict[str, Any]:
        """Serialize a tool to a dict that can be stored in state and serialized by msgpack."""
        if hasattr(tool, "model_dump"):
            # It's a Pydantic model, serialize it
            try:
                tool_dict = tool.model_dump(mode="json", exclude_none=True)
                # Clean up args_schema - it's usually a Pydantic class
                if tool_dict.get("args_schema"):
                    if hasattr(tool_dict["args_schema"], "__name__"):
                        tool_dict["args_schema"] = (
                            f"<PydanticModel:{tool_dict['args_schema'].__name__}>"
                        )
                    else:
                        tool_dict["args_schema"] = None
                return tool_dict
            except Exception as e:
                logger.warning(f"Failed to serialize tool with model_dump: {e}")

        # Try to extract basic info
        if hasattr(tool, "name"):
            return {
                "name": tool.name,
                "description": getattr(tool, "description", ""),
                "type": "tool",
            }
        if hasattr(tool, "__name__"):
            return {
                "name": tool.__name__,
                "description": getattr(tool, "__doc__", ""),
                "type": "function",
            }
        return {"name": str(tool), "type": "unknown"}

    def _serialize_engine_for_state(self, engine: Any) -> dict[str, Any]:
        """Serialize an engine to a dict that can be stored in state and serialized by msgpack.

        The agent node can model validate this dict back to an engine if needed.
        """
        if not hasattr(engine, "model_dump"):
            # Not a Pydantic model, try to convert to dict
            return {"name": str(engine), "type": "unknown"}

        try:
            # Get base serialization with mode='json' to handle SecretStr and other special types
            engine_dict = engine.model_dump(
                mode="json",  # This converts SecretStr and other non-JSON types
                exclude={"input_schema", "output_schema"},  # These are already excluded
                exclude_none=True,
            )

            # Handle fields that contain Pydantic classes or other non-serializable objects
            # These fields typically contain ModelMetaclass objects
            fields_to_clean = [
                "tools",
                "schemas",
                "pydantic_tools",
                "structured_output_model",
            ]

            for field in fields_to_clean:
                if field in engine_dict:
                    value = engine_dict[field]
                    if value is None:
                        continue
                    if field == "structured_output_model":
                        # Convert Pydantic model class to string representation
                        if hasattr(value, "__name__"):
                            engine_dict[field] = f"<PydanticModel:{value.__name__}>"
                        else:
                            engine_dict[field] = None
                    elif isinstance(value, list):
                        # Convert list of Pydantic classes to string representations
                        cleaned_list = []
                        for item in value:
                            if hasattr(item, "__name__"):
                                cleaned_list.append(f"<PydanticModel:{item.__name__}>")
                            elif hasattr(item, "name"):
                                cleaned_list.append({"name": item.name, "type": "tool"})
                            else:
                                # Skip non-serializable items
                                continue
                        engine_dict[field] = cleaned_list
                    else:
                        # For other types, remove them
                        engine_dict[field] = None

            return engine_dict

        except Exception as e:
            logger.warning(
                f"Failed to serialize engine {getattr(engine, 'name', 'unknown')}: {e}"
            )
            # Return minimal engine info
            return {
                "id": getattr(engine, "id", str(id(engine))),
                "name": getattr(engine, "name", "unknown"),
                "engine_type": str(getattr(engine, "engine_type", "unknown")),
            }

    def _prepare_input(self, input_data: Any) -> Any:
        """Prepare input data for the multi-agent system.
        Ensures engines are properly populated in the state.
        """
        # Call parent's _prepare_input first
        prepared = super()._prepare_input(input_data)

        # Ensure prepared is a dict
        if hasattr(prepared, "model_dump"):
            prepared_dict = prepared.model_dump()
        elif isinstance(prepared, dict):
            prepared_dict = prepared
        else:
            prepared_dict = {"messages": []}

        # Collect all engines from all agents
        if "engines" not in prepared_dict or not prepared_dict["engines"]:
            all_engines = {}
            for agent in self.agents:
                if hasattr(agent, "engines") and agent.engines:
                    for engine_name, engine in agent.engines.items():
                        # Store engines but ensure they're serializable
                        # We'll use a custom serializer that handles Pydantic classes
                        serialized_engine = self._serialize_engine_for_state(engine)
                        if serialized_engine:
                            all_engines[engine_name] = serialized_engine
                            logger.debug(
                                f"Added serialized engine '{engine_name}' from agent '{agent.name}'"
                            )

            prepared_dict["engines"] = all_engines
            logger.info(
                f"Populated state with {len(all_engines)} engines from {len(self.agents)} agents"
            )

        # Serialize tools if they exist in prepared_dict to avoid msgpack errors
        if prepared_dict.get("tools"):
            serialized_tools = []
            for tool in prepared_dict["tools"]:
                if tool is not None:
                    serialized_tool = self._serialize_tool_for_state(tool)
                    serialized_tools.append(serialized_tool)
            prepared_dict["tools"] = serialized_tools
            logger.debug(f"Serialized {len(serialized_tools)} tools for state storage")

        # If we have a state schema, create an instance
        if self.state_schema:
            try:
                return self.state_schema(**prepared_dict)
            except Exception as e:
                logger.warning(f"Error creating state schema instance: {e}")
                return prepared_dict

        return prepared_dict

    def visualize_structure(self) -> None:
        """Visualize the multi-agent structure."""
        tree = Tree(f"[bold blue]{self.name}[/bold blue] ({self.execution_mode.value})")

        # Add agents
        agents_branch = tree.add("[green]Agents[/green]")
        for agent in self.agents:
            agent_name = getattr(agent, "name", agent.__class__.__name__)
            agent_info = f"{agent_name}"
            if hasattr(agent, "engine") and agent.engine:
                engine_type = getattr(agent.engine, "engine_type", "unknown")
                agent_info += f" (engine: {engine_type})"
            agents_branch.add(agent_info)

        # Add branches
        if self.branches:
            branches_branch = tree.add("[yellow]Conditional Branches[/yellow]")
            for source, config in self.branches.items():
                branch_info = f"{source} → "
                dests = config.get("destinations", {})
                branch_info += ", ".join(f"{k}: {v}" for k, v in dests.items())
                if config.get("default"):
                    branch_info += f" (default: {config['default']})"
                branches_branch.add(branch_info)

        # Add schema info
        schema_branch = tree.add("[cyan]Schema Info[/cyan]")
        if self.state_schema:
            schema_branch.add(
                f"State: {getattr(self.state_schema, '__name__', 'Unknown')}"
            )
        if self.input_schema:
            schema_branch.add(
                f"Input: {getattr(self.input_schema, '__name__', 'Unknown')}"
            )
        if self.output_schema:
            schema_branch.add(
                f"Output: {getattr(self.output_schema, '__name__', 'Unknown')}"
            )

        console.print(tree)


class SequentialAgent(MultiAgent):
    """Multi-agent system with sequential execution.

    Agents execute one after another in the order they were added, with
    state flowing from one agent to the next. This is ideal for pipeline
    processing where each agent builds on the work of the previous one.

    The state schema is automatically composed with intelligent field sharing,
    ensuring that outputs from one agent are available as inputs to the next
    while maintaining proper message preservation.

    Example:
        >>> # Create a document processing pipeline
        >>> pipeline = SequentialAgent(
        ...     name="Document Pipeline",
        ...     agents=[
        ...         extractor_agent,    # Extracts key information
        ...         analyzer_agent,     # Analyzes extracted data
        ...         summarizer_agent    # Creates final summary
        ...     ]
        ... )
        >>> result = pipeline.run({"messages": [doc_message]})

    Flow:
        Agent1 → Agent2 → Agent3 → Result

    Each agent receives the full state including messages from all previous
    agents, allowing it to build on prior work.
    """

    execution_mode: ExecutionMode = Field(
        default=ExecutionMode.SEQUENCE, description="Sequential execution mode"
    )

    def build_custom_graph(self, graph: BaseGraph) -> BaseGraph:
        """Not needed for sequential mode - handled by base class."""
        return graph


class ParallelAgent(MultiAgent):
    """Pre-configured parallel multi-agent."""

    execution_mode: ExecutionMode = Field(
        default=ExecutionMode.PARALLEL, description="Parallel execution mode"
    )

    def build_custom_graph(self, graph: BaseGraph) -> BaseGraph:
        """Not needed for parallel mode."""
        return graph


class ConditionalAgent(MultiAgent):
    """Pre-configured conditional multi-agent with branching."""

    execution_mode: ExecutionMode = Field(
        default=ExecutionMode.CONDITIONAL, description="Conditional execution mode"
    )

    def build_custom_graph(self, graph: BaseGraph) -> BaseGraph:
        """Not needed for conditional mode."""
        return graph
