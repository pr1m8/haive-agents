"""Tools and utilities for Dynamic Supervisor V2.

This module provides tools for agent creation, discovery, matching, and
workflow coordination.
"""

import logging
from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.tools import BaseTool, tool
from pydantic import BaseModel, Field

from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.agents.supervisor.models import (
    AgentDiscoveryMode,
    AgentSpec,
    DiscoveryConfig,
)

logger = logging.getLogger(__name__)


def create_agent_from_spec(spec: AgentSpec) -> Any:
    """Create an agent instance from a specification.

    This function instantiates the appropriate agent type based on the spec,
    configuring it with the provided settings and tools.

    Args:
        spec: Agent specification containing type, config, and tools

    Returns:
        Instantiated agent instance

    Raises:
        ValueError: If agent_type is not supported

    Example:
        >>> spec = AgentSpec(
        ...     name="calculator",
        ...     agent_type="ReactAgent",
        ...     config={"temperature": 0.1}
        ... )
        >>> agent = create_agent_from_spec(spec)
    """
    logger.info(f"Creating agent '{spec.name}' of type '{spec.agent_type}'")

    # Extract config
    config = spec.config.copy()

    # Create AugLLMConfig if not provided
    if "engine" not in config:
        engine_config = {}

        # Extract engine-specific configs
        for key in ["temperature", "max_tokens", "system_message", "model"]:
            if key in config:
                engine_config[key] = config.pop(key)

        # Add tools to engine config
        if spec.tools:
            engine_config["tools"] = spec.tools

        config["engine"] = AugLLMConfig(**engine_config)

    # Create agent based on type
    agent_type = spec.agent_type.lower()

    if agent_type in ["simpleagentv3", "simpleagent", "simple"]:
        return SimpleAgentV3(name=spec.name, **config)
    if agent_type in ["reactagent", "react"]:
        return ReactAgent(name=spec.name, **config)
    # Try to instantiate directly if it's a class name
    try:
        # Import from haive.agents namespace
        from haive.agents import react, simple

        # Check standard locations
        if hasattr(simple, spec.agent_type):
            agent_class = getattr(simple, spec.agent_type)
        elif hasattr(react, spec.agent_type):
            agent_class = getattr(react, spec.agent_type)
        else:
            raise ValueError(f"Unknown agent type: {spec.agent_type}")

        return agent_class(name=spec.name, **config)
    except Exception as e:
        logger.error(f"Failed to create agent of type '{spec.agent_type}': {e}")
        # Default to SimpleAgentV3
        logger.warning(f"Defaulting to SimpleAgentV3 for agent '{spec.name}'")
        return SimpleAgentV3(name=spec.name, **config)


def find_matching_agent_specs(
    task: str,
    available_specs: list[AgentSpec],
    threshold: float = 0.3,
    max_results: int = 5,
) -> list[AgentSpec]:
    """Find agent specifications that match a given task.

    Uses specialty matching and keyword analysis to find the most suitable
    agent specifications for a task.

    Args:
        task: Task description to match against
        available_specs: List of available agent specifications
        threshold: Minimum match score (0-1) to include a spec
        max_results: Maximum number of results to return

    Returns:
        List of matching specs, sorted by relevance

    Example:
        >>> specs = [math_spec, research_spec, writing_spec]
        >>> matches = find_matching_agent_specs(
        ...     "Calculate the compound interest",
        ...     specs
        ... )
        >>> assert matches[0].name == "math_expert"
    """
    task.lower()
    matches = []

    for spec in available_specs:
        if not spec.enabled:
            continue

        # Convert to capability for matching
        capability = spec.to_capability()
        score = capability.matches_task(task, threshold)

        if score > 0:
            matches.append((score, spec))

    # Sort by score (descending) and priority
    matches.sort(key=lambda x: (x[0], x[1].priority), reverse=True)

    # Return top matches
    return [spec for _, spec in matches[:max_results]]


def discover_agents(
    task: str,
    discovery_config: DiscoveryConfig,
    existing_agents: set[str] | None = None,
) -> list[AgentSpec]:
    """Discover new agents based on task requirements.

    This function implements various discovery strategies to find or create
    agent specifications that can handle the given task.

    Args:
        task: Task description requiring agents
        discovery_config: Configuration for discovery process
        existing_agents: Set of already discovered agent names to avoid duplicates

    Returns:
        List of discovered agent specifications

    Note:
        Currently implements MANUAL mode. Other modes (COMPONENT_DISCOVERY,
        RAG_DISCOVERY, MCP_DISCOVERY) are planned for future releases.
    """
    logger.info(
        f"Discovering agents for task: '{task}' using mode: {discovery_config.mode}"
    )

    existing = existing_agents or set()
    discovered_specs = []

    if discovery_config.mode == AgentDiscoveryMode.MANUAL:
        # Manual mode doesn't discover new agents
        logger.debug("Manual mode - no discovery performed")
        return []

    if discovery_config.mode == AgentDiscoveryMode.COMPONENT_DISCOVERY:
        # TODO: Implement component discovery
        # This would scan component_paths for agent implementations
        logger.warning("Component discovery not yet implemented")
        return []

    if discovery_config.mode == AgentDiscoveryMode.RAG_DISCOVERY:
        # TODO: Implement RAG-based discovery
        # This would use vector search to find relevant agent code/docs
        logger.warning("RAG discovery not yet implemented")
        return []

    if discovery_config.mode == AgentDiscoveryMode.MCP_DISCOVERY:
        # TODO: Implement MCP discovery
        # This would query MCP servers for available agents
        logger.warning("MCP discovery not yet implemented")
        return []

    if discovery_config.mode == AgentDiscoveryMode.HYBRID:
        # Combine multiple discovery methods
        for mode in [
            AgentDiscoveryMode.COMPONENT_DISCOVERY,
            AgentDiscoveryMode.RAG_DISCOVERY,
            AgentDiscoveryMode.MCP_DISCOVERY,
        ]:
            config_copy = discovery_config.model_copy()
            config_copy.mode = mode
            specs = discover_agents(task, config_copy, existing)
            discovered_specs.extend(specs)

    # Filter out duplicates
    unique_specs = []
    seen_names = set()

    for spec in discovered_specs:
        if spec.name not in seen_names and spec.name not in existing:
            unique_specs.append(spec)
            seen_names.add(spec.name)

    return unique_specs[: discovery_config.max_discoveries_per_request]


def create_handoff_tool(agent_name: str, description: str) -> BaseTool:
    """Create a tool for handing off tasks to a specific agent.

    Args:
        agent_name: Name of the agent to hand off to
        description: Description of what the agent does

    Returns:
        Tool that can be used to route tasks to the agent

    Example:
        >>> tool = create_handoff_tool("math_expert", "Handles math problems")
        >>> result = tool.invoke({"task": "Calculate 2+2"})
    """

    class HandoffInput(BaseModel):
        task: str = Field(..., description="Task to hand off")

    @tool(args_schema=HandoffInput)
    def handoff_to_agent(task: str) -> str:
        f"""Hand off task to {agent_name}: {description}"""
        return f"HANDOFF_TO_{agent_name.upper()}: {task}"

    # Set proper name and description
    handoff_to_agent.name = f"handoff_to_{agent_name}"
    handoff_to_agent.description = f"Hand off task to {agent_name}: {description}"

    return handoff_to_agent


class AgentManagementTools:
    """Collection of tools for managing agents in the supervisor.

    These tools can be provided to the supervisor to enable dynamic
    agent management capabilities.
    """

    @staticmethod
    def create_list_agents_tool(state_accessor) -> BaseTool:
        """Create a tool for listing available agents.

        Args:
            state_accessor: Function to access current state

        Returns:
            Tool for listing agents
        """

        @tool
        def list_available_agents() -> str:
            """List all available agents and their capabilities."""
            state = state_accessor()
            agents = state.get("active_agents", {})

            if not agents:
                return "No active agents available."

            agent_list = []
            for name, agent in agents.items():
                cap = agent.capability
                status = f"({agent.state})" if agent.state != "idle" else ""
                agent_list.append(
                    f"- {name} {status}: {cap.description} "
                    f"[specialties: {', '.join(cap.specialties)}]"
                )

            return "Available agents:\n" + "\n".join(agent_list)

        return list_available_agents

    @staticmethod
    def create_agent_stats_tool(state_accessor) -> BaseTool:
        """Create a tool for viewing agent statistics.

        Args:
            state_accessor: Function to access current state

        Returns:
            Tool for viewing agent stats
        """

        @tool
        def view_agent_statistics() -> str:
            """View performance statistics for all agents."""
            state = state_accessor()
            agents = state.get("active_agents", {})
            metrics = state.get("supervisor_metrics", {})

            stats = [f"Supervisor uptime: {metrics.uptime_hours:.1f} hours"]
            stats.append(f"Total tasks: {metrics.total_tasks}")
            stats.append(f"Success rate: {metrics.success_rate:.1%}\n")

            for name, agent in agents.items():
                stats.append(f"{name}:")
                stats.append(f"  Tasks: {agent.task_count}")
                stats.append(f"  Success rate: {agent.success_rate:.1%}")
                stats.append(f"  Avg time: {agent.average_execution_time:.2f}s")

            return "\n".join(stats)

        return view_agent_statistics
