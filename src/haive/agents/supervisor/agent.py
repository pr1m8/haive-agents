"""Dynamic Supervisor V2 - Main agent implementation.

This module contains the core DynamicSupervisor class that orchestrates
runtime agent discovery, creation, and task routing.
"""

import asyncio
import logging
from datetime import datetime
from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langgraph.graph import END, StateGraph
from pydantic import Field, field_validator

from haive.agents.react.agent import ReactAgent
from haive.agents.supervisor.models import (
    AgentDiscoveryMode,
    AgentSpec,
    DiscoveryConfig,
)
from haive.agents.supervisor.state import (
    ActiveAgent,
    DynamicSupervisorState,
    create_initial_state,
)
from haive.agents.supervisor.tools import (
    AgentManagementTools,
    create_agent_from_spec,
    discover_agents,
    find_matching_agent_specs,
)

logger = logging.getLogger(__name__)


class DynamicSupervisor(ReactAgent):
    """Advanced supervisor that discovers and creates agents at runtime.

    The DynamicSupervisor extends ReactAgent to provide intelligent task routing
    with the ability to discover, create, and manage specialized agents dynamically
    based on task requirements.

    Key capabilities:
        - Dynamic agent discovery from specifications
        - Runtime agent creation and lifecycle management
        - Intelligent task-to-agent matching
        - Performance tracking and optimization
        - Extensible discovery mechanisms

    Attributes:
        name: Supervisor identifier
        engine: LLM configuration for supervisor reasoning
        agent_specs: Initial specifications for creatable agents
        discovery_config: Configuration for agent discovery
        max_agents: Maximum number of active agents to maintain
        auto_discover: Whether to automatically discover new agents
        include_management_tools: Whether to include agent management tools

    Examples:
        Basic usage with predefined agent specs::

            supervisor = DynamicSupervisor(
                name="task_router",
                agent_specs=[
                    AgentSpec(
                        name="researcher",
                        agent_type="ReactAgent",
                        description="Research and analysis expert",
                        specialties=["research", "analysis"],
                        tools=[web_search_tool]
                    ),
                    AgentSpec(
                        name="writer",
                        agent_type="SimpleAgentV3",
                        description="Content creation expert",
                        specialties=["writing", "editing"]
                    )
                ]
            )

            result = await supervisor.arun(
                "Research quantum computing and write a summary"
            )
    """

    # Agent specifications and discovery
    agent_specs: list[AgentSpec] = Field(
        default_factory=list, description="Initial agent specifications"
    )
    discovery_config: DiscoveryConfig = Field(
        default_factory=DiscoveryConfig, description="Agent discovery configuration"
    )

    # Supervisor configuration
    max_agents: int = Field(
        default=10, ge=1, le=50, description="Maximum active agents to maintain"
    )
    auto_discover: bool = Field(
        default=True, description="Automatically discover agents for unknown tasks"
    )
    include_management_tools: bool = Field(
        default=True, description="Include agent management tools"
    )

    # Internal state (not in Field to avoid Pydantic issues)
    _state: DynamicSupervisorState
    _graph: StateGraph | None

    def __init__(self, **data):
        """Initialize the dynamic supervisor.

        Args:
            **data: Configuration parameters
        """
        # Ensure we have a proper engine config
        if "engine" not in data:
            data["engine"] = AugLLMConfig(
                temperature=0.3,
                system_message=(
                    "You are an intelligent task routing supervisor. "
                    "Analyze tasks and route them to appropriate specialized agents. "
                    "If no suitable agent exists, you can discover or create new ones."
                ),
            )

        # Initialize parent
        super().__init__(**data)

        # Initialize state
        self._state = create_initial_state(available_specs=self.agent_specs)
        self._graph = None

        # Add management tools if requested
        if self.include_management_tools:
            self._add_management_tools()

        # Build the supervisor graph
        self._build_graph()

    @field_validator("agent_specs")
    @classmethod
    def validate_agent_specs(cls, v: list[AgentSpec]) -> list[AgentSpec]:
        """Validate agent specifications have unique names."""
        names = [spec.name for spec in v]
        if len(names) != len(set(names)):
            raise ValueError("Agent specifications must have unique names")
        return v

    def _add_management_tools(self) -> None:
        """Add agent management tools to the supervisor."""

        def state_accessor():
            """State Accessor."""
            return self._state

        management_tools = [
            AgentManagementTools.create_list_agents_tool(state_accessor),
            AgentManagementTools.create_agent_stats_tool(state_accessor),
        ]

        # Add to existing tools
        current_tools = list(self.engine.tools or [])
        current_tools.extend(management_tools)
        self.engine.tools = current_tools

    def _build_graph(self) -> None:
        """Build the supervisor execution graph."""
        graph = StateGraph(DynamicSupervisorState)

        # Add nodes
        graph.add_node("supervisor", self._supervisor_node)
        graph.add_node("discovery", self._discovery_node)
        graph.add_node("agent_execution", self._agent_execution_node)

        # Add edges
        graph.set_entry_point("supervisor")

        # Supervisor can go to discovery or agent execution
        graph.add_conditional_edges(
            "supervisor",
            self._route_supervisor,
            {"discover": "discovery", "execute": "agent_execution", "end": END},
        )

        # Discovery always goes back to supervisor
        graph.add_edge("discovery", "supervisor")

        # Agent execution goes to END
        graph.add_edge("agent_execution", END)

        # Compile graph
        self._graph = graph.compile()

    async def _supervisor_node(self, state: DynamicSupervisorState) -> dict[str, Any]:
        """Supervisor reasoning node.

        Analyzes tasks and determines routing strategy.
        """
        # Get last user message
        user_message = None
        for msg in reversed(state["messages"]):
            if isinstance(msg, HumanMessage):
                user_message = msg.content
                break

        if not user_message:
            return {
                "messages": [AIMessage(content="No task provided.")],
                "workflow_state": "complete",
            }

        logger.info(f"Supervisor analyzing task: '{user_message}'")

        # Update metrics
        metrics = state["supervisor_metrics"]
        metrics.total_tasks += 1
        metrics.last_task_time = datetime.now()

        # Check for suitable active agent
        active_agents = state["active_agents"]
        best_match = None
        best_score = 0.0

        for agent_name, agent in active_agents.items():
            if agent.state == "idle":
                score = agent.capability.matches_task(user_message)
                if score > best_score:
                    best_score = score
                    best_match = agent_name

        if best_match and best_score > 0.5:
            logger.info(
                f"Found suitable active agent: {best_match} (score: {best_score:.2f})"
            )
            return {
                "messages": [AIMessage(content=f"Routing to {best_match}")],
                "current_agent": best_match,
                "agent_task": user_message,
                "workflow_state": "executing",
            }

        # Check available specs
        available_specs = state["available_specs"]
        matching_specs = find_matching_agent_specs(user_message, available_specs)

        if matching_specs:
            # Check if we need to create the agent
            best_spec = matching_specs[0]
            if best_spec.name not in active_agents:
                logger.info(f"Need to create agent: {best_spec.name}")
                return {
                    "messages": [AIMessage(content=f"Creating {best_spec.name}")],
                    "workflow_state": "discovering",
                }

        # No suitable agent found
        if self.auto_discover:
            logger.info("No suitable agent found, attempting discovery")
            return {
                "messages": [AIMessage(content="Discovering new agents")],
                "workflow_state": "discovering",
            }
        available_names = list(active_agents.keys())
        return {
            "messages": [
                AIMessage(
                    content=f"No suitable agent found. Available: {available_names}"
                )
            ],
            "workflow_state": "complete",
        }

    async def _discovery_node(self, state: DynamicSupervisorState) -> dict[str, Any]:
        """Agent discovery and creation node."""
        # Get the task
        user_message = None
        for msg in reversed(state["messages"]):
            if isinstance(msg, HumanMessage):
                user_message = msg.content
                break

        if not user_message:
            return {"workflow_state": "routing"}

        logger.info(f"Discovering agents for: '{user_message}'")

        # Update metrics
        metrics = state["supervisor_metrics"]
        metrics.discovery_attempts += 1

        # Try to find matching specs first
        available_specs = state["available_specs"]
        matching_specs = find_matching_agent_specs(user_message, available_specs)

        created_agent = None

        if matching_specs:
            # Create from existing spec
            spec = matching_specs[0]
            if spec.name not in state["active_agents"]:
                try:
                    agent = create_agent_from_spec(spec)
                    active_agent = ActiveAgent(
                        name=spec.name, instance=agent, capability=spec.to_capability()
                    )

                    state["active_agents"][spec.name] = active_agent
                    state["agent_capabilities"][spec.name] = active_agent.capability
                    state["discovered_agents"].add(spec.name)

                    metrics.agent_creations += 1
                    metrics.successful_discoveries += 1
                    created_agent = spec.name

                    logger.info(f"Created agent '{spec.name}' from specification")
                except Exception as e:
                    logger.error(f"Failed to create agent '{spec.name}': {e}")

        # Try discovery if enabled and no agent created
        if (
            not created_agent
            and self.discovery_config.mode != AgentDiscoveryMode.MANUAL
        ):
            discovered_specs = discover_agents(
                user_message, self.discovery_config, state["discovered_agents"]
            )

            if discovered_specs:
                # Add to available specs
                state["available_specs"].extend(discovered_specs)

                # Create the first discovered agent
                spec = discovered_specs[0]
                try:
                    agent = create_agent_from_spec(spec)
                    active_agent = ActiveAgent(
                        name=spec.name, instance=agent, capability=spec.to_capability()
                    )

                    state["active_agents"][spec.name] = active_agent
                    state["agent_capabilities"][spec.name] = active_agent.capability
                    state["discovered_agents"].add(spec.name)

                    metrics.agent_creations += 1
                    metrics.successful_discoveries += 1
                    created_agent = spec.name

                    logger.info(f"Created discovered agent '{spec.name}'")
                except Exception as e:
                    logger.error(
                        f"Failed to create discovered agent '{spec.name}': {e}"
                    )

        # Clean up if we're at max capacity
        if len(state["active_agents"]) > self.max_agents:
            self._cleanup_inactive_agents(state)

        # Update state for routing back to supervisor
        if created_agent:
            return {
                "messages": [AIMessage(content=f"Created agent: {created_agent}")],
                "workflow_state": "routing",
            }
        return {
            "messages": [AIMessage(content="No suitable agents discovered")],
            "workflow_state": "routing",
        }

    async def _agent_execution_node(
        self, state: DynamicSupervisorState
    ) -> dict[str, Any]:
        """Execute task with selected agent."""
        agent_name = state["current_agent"]
        task = state["agent_task"]

        if not agent_name or agent_name not in state["active_agents"]:
            return {
                "messages": [AIMessage(content="No agent selected for execution")],
                "workflow_state": "complete",
            }

        active_agent = state["active_agents"][agent_name]
        logger.info(f"Executing task with agent '{agent_name}'")

        # Update agent state
        active_agent.state = "busy"
        active_agent.last_task = task

        # Track execution time
        start_time = datetime.now()

        try:
            # Execute with agent
            agent = active_agent.instance

            # Run agent (handle both sync and async)
            if hasattr(agent, "arun"):
                result = await agent.arun(task)
            else:
                result = await asyncio.to_thread(agent.run, task)

            # Calculate execution time
            execution_time = (datetime.now() - start_time).total_seconds()

            # Update metrics
            active_agent.update_metrics(execution_time, success=True)
            state["supervisor_metrics"].successful_tasks += 1
            state["supervisor_metrics"].total_execution_time += execution_time

            # Update state
            active_agent.state = "idle"

            return {
                "messages": [AIMessage(content=str(result))],
                "agent_response": str(result),
                "workflow_state": "complete",
            }

        except Exception as e:
            logger.error(f"Agent '{agent_name}' failed: {e}")

            # Calculate execution time even for failures
            execution_time = (datetime.now() - start_time).total_seconds()

            # Update metrics
            active_agent.update_metrics(execution_time, success=False)
            active_agent.state = "error"
            state["supervisor_metrics"].failed_tasks += 1

            return {
                "messages": [AIMessage(content=f"Agent failed: {e!s}")],
                "workflow_state": "complete",
            }

    def _route_supervisor(self, state: DynamicSupervisorState) -> str:
        """Determine next node based on workflow state."""
        workflow_state = state.get("workflow_state", "routing")

        if workflow_state == "discovering":
            return "discover"
        if workflow_state == "executing":
            return "execute"
        return "end"

    def _cleanup_inactive_agents(self, state: DynamicSupervisorState) -> None:
        """Remove least recently used agents when at capacity."""
        active_agents = state["active_agents"]

        if len(active_agents) <= self.max_agents:
            return

        # Sort by last used time (least recent first)
        sorted_agents = sorted(
            active_agents.items(),
            key=lambda x: x[1].capability.last_used or "1970-01-01",
        )

        # Remove least recently used
        num_to_remove = len(active_agents) - self.max_agents + 1
        for agent_name, _ in sorted_agents[:num_to_remove]:
            logger.info(f"Removing inactive agent '{agent_name}' (capacity limit)")
            del active_agents[agent_name]
            del state["agent_capabilities"][agent_name]

    async def arun(self, input_data: str | dict[str, Any] | list[BaseMessage]) -> Any:
        """Run the supervisor asynchronously.

        Args:
            input_data: Task input (string, dict, or messages)

        Returns:
            Agent execution result
        """
        # Prepare input
        if isinstance(input_data, str):
            messages = [HumanMessage(content=input_data)]
        elif isinstance(input_data, dict) and "messages" in input_data:
            messages = input_data["messages"]
        elif isinstance(input_data, list):
            messages = input_data
        else:
            messages = [HumanMessage(content=str(input_data))]

        # Update state
        self._state["messages"] = messages
        self._state["workflow_state"] = "routing"

        # Execute graph
        result = await self._graph.ainvoke(self._state)

        # Extract response
        if result.get("agent_response"):
            return result["agent_response"]

        # Get last AI message
        for msg in reversed(result.get("messages", [])):
            if isinstance(msg, AIMessage):
                return msg.content

        return "No response generated"

    def run(self, input_data: str | dict[str, Any] | list[BaseMessage]) -> Any:
        """Run the supervisor synchronously.

        Args:
            input_data: Task input

        Returns:
            Agent execution result
        """
        return asyncio.run(self.arun(input_data))

    def get_metrics(self) -> dict[str, Any]:
        """Get supervisor performance metrics.

        Returns:
            Dictionary of metrics including agent stats
        """
        metrics = self._state["supervisor_metrics"]

        return {
            "supervisor": {
                "total_tasks": metrics.total_tasks,
                "success_rate": metrics.success_rate,
                "discovery_success_rate": metrics.discovery_success_rate,
                "total_execution_time": metrics.total_execution_time,
                "uptime_hours": metrics.uptime_hours,
                "agent_creations": metrics.agent_creations,
            },
            "agents": {
                agent_name: {
                    "task_count": agent.task_count,
                    "success_rate": agent.success_rate,
                    "avg_execution_time": agent.average_execution_time,
                    "state": agent.state,
                }
                for agent_name, agent in self._state["active_agents"].items()
            },
        }


def create_dynamic_supervisor(
    name: str = "dynamic_supervisor",
    agent_specs: list[AgentSpec] | None = None,
    discovery_mode: AgentDiscoveryMode = AgentDiscoveryMode.MANUAL,
    **kwargs,
) -> DynamicSupervisor:
    """Factory function to create a configured dynamic supervisor.

    Args:
        name: Supervisor name
        agent_specs: Initial agent specifications
        discovery_mode: How to discover new agents
        **kwargs: Additional configuration

    Returns:
        Configured DynamicSupervisor instance

    Examples:
        >>> supervisor = create_dynamic_supervisor(
        ...     name="task_router",
        ...     agent_specs=[math_spec, research_spec],
        ...     discovery_mode="manual",
        ...     max_agents=20
        ... )
    """
    discovery_config = DiscoveryConfig(mode=discovery_mode)

    return DynamicSupervisor(
        name=name,
        agent_specs=agent_specs or [],
        discovery_config=discovery_config,
        **kwargs,
    )
