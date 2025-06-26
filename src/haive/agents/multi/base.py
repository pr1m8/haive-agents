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
from enum import Enum
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Literal,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

from haive.core.engine.base import EngineType
from haive.core.graph.node.engine_node import EngineNodeConfig
from haive.core.graph.state_graph.base_graph2 import BaseGraph
from haive.core.schema.agent_schema_composer import AgentSchemaComposer, BuildMode
from haive.core.schema.state_schema import StateSchema
from langchain_core.messages import BaseMessage
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
    branches: Dict[str, Dict[str, Any]] = Field(
        default_factory=dict,
        description="Branch configurations keyed by source node name",
    )

    # Private state management
    _agent_private_states: Dict[str, Type[BaseModel]] = PrivateAttr(
        default_factory=dict
    )
    _agent_node_mapping: Dict[str, str] = PrivateAttr(default_factory=dict)

    @model_validator(mode="before")
    @classmethod
    def validate_agents(cls, values: Dict[str, Any]) -> Dict[str, Any]:
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
        source_agent: Union[str, Agent],
        condition: Callable[[Any], Union[str, bool]],
        destinations: Dict[Union[str, bool], Union[str, Agent]],
        default: Optional[Union[str, Agent]] = None,
    ) -> None:
        """
        Add a conditional edge between agents.

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

    def _get_node_name(self, agent: Union[str, Agent]) -> str:
        """Get the node name for an agent."""
        if isinstance(agent, str):
            # Could be agent name or id
            for a in self.agents:
                if getattr(a, "name", None) == agent or getattr(a, "id", None) == agent:
                    return self._get_agent_node_name(a)
            return agent  # Assume it's a node name
        elif isinstance(agent, Agent):
            return self._get_agent_node_name(agent)
        else:
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
            else:
                # Normal sequential edge
                if i == len(node_names) - 1:
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
        """
        Build a custom graph - must be implemented by subclasses if using CUSTOM mode.

        Args:
            graph: The graph to build on

        Returns:
            The modified graph
        """
        raise NotImplementedError(
            "Subclasses must implement build_custom_graph for CUSTOM mode"
        )

    def get_agent_by_name(self, name: str) -> Optional[Agent]:
        """Get an agent by name or id."""
        for agent in self.agents:
            if (
                getattr(agent, "name", None) == name
                or getattr(agent, "id", None) == name
            ):
                return agent
        return None

    def _serialize_tool_for_state(self, tool: Any) -> Dict[str, Any]:
        """
        Serialize a tool to a dict that can be stored in state and serialized by msgpack.
        """
        if hasattr(tool, "model_dump"):
            # It's a Pydantic model, serialize it
            try:
                tool_dict = tool.model_dump(mode="json", exclude_none=True)
                # Clean up args_schema - it's usually a Pydantic class
                if "args_schema" in tool_dict and tool_dict["args_schema"]:
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
        elif hasattr(tool, "__name__"):
            return {
                "name": tool.__name__,
                "description": getattr(tool, "__doc__", ""),
                "type": "function",
            }
        else:
            return {"name": str(tool), "type": "unknown"}

    def _serialize_engine_for_state(self, engine: Any) -> Dict[str, Any]:
        """
        Serialize an engine to a dict that can be stored in state and serialized by msgpack.

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
                    elif field == "structured_output_model":
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
        """
        Prepare input data for the multi-agent system.
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
        if "tools" in prepared_dict and prepared_dict["tools"]:
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
