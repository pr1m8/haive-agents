"""Tools for supervisor agents.

This module provides the tools that supervisor agents can use to manage
other agents, delegate tasks, and coordinate multi-agent workflows.
"""

from typing import Any, Dict, List, Optional
from langchain_core.tools import Tool, tool
from pydantic import BaseModel, Field

from haive.agents.experiments.supervisor.state_models import AgentMetadata, ExecutionContext


class AgentHandoffInput(BaseModel):
    """Input model for agent handoff tool."""

    agent_name: str = Field(..., description="Name of the agent to delegate to")
    task: str = Field(..., description="Task description for the agent")
    context: Optional[Dict[str, Any]] = Field(None, description="Additional context")


class AgentCreationInput(BaseModel):
    """Input model for agent creation tool."""

    name: str = Field(..., description="Name for the new agent")
    description: str = Field(..., description="Description of agent capabilities")
    agent_type: str = Field(default="simple", description="Type of agent to create")
    config: Optional[Dict[str, Any]] = Field(None, description="Agent configuration")


class ListAgentsInput(BaseModel):
    """Input model for listing agents."""

    include_inactive: bool = Field(default=False, description="Include inactive agents")
    filter_by_type: Optional[str] = Field(None, description="Filter by agent type")


def create_supervisor_handoff_tool(supervisor) -> Tool:
    """Create a tool for delegating tasks to agents.

    Args:
        supervisor: The supervisor instance

    Returns:
        Tool for agent task delegation
    """

    def delegate_to_agent(
        agent_name: str, task: str, context: Optional[Dict[str, Any]] = None
    ) -> str:
        """Delegate a task to a specific agent.

        Args:
            agent_name: Name of the agent to delegate to
            task: Task description
            context: Optional additional context

        Returns:
            Result from the delegated agent
        """
        try:
            # Check if agent exists
            if agent_name not in supervisor.supervisor_state.agents:
                available_agents = list(supervisor.supervisor_state.agents.keys())
                return f"Agent '{agent_name}' not found. Available agents: {available_agents}"

            # Delegate the task
            result = supervisor.delegate_task(agent_name, task)
            return f"Task delegated to {agent_name}. Result: {result}"

        except Exception as e:
            return f"Error delegating task to {agent_name}: {str(e)}"

    return Tool(
        name="delegate_task",
        description="Delegate a task to a specific agent by name",
        func=delegate_to_agent,
    )


def create_list_agents_tool(supervisor) -> Tool:
    """Create a tool for listing available agents.

    Args:
        supervisor: The supervisor instance

    Returns:
        Tool for listing agents
    """

    def list_agents(include_inactive: bool = False, filter_by_type: Optional[str] = None) -> str:
        """List all available agents.

        Args:
            include_inactive: Include inactive agents
            filter_by_type: Filter by agent type

        Returns:
            Formatted list of agents
        """
        try:
            agents = supervisor.list_agents()

            if not agents:
                return "No agents registered."

            # Apply filters
            filtered_agents = {}
            for name, metadata in agents.items():
                # Filter by active status
                if not include_inactive and not metadata.is_active:
                    continue

                # Filter by type
                if filter_by_type and metadata.agent_type.lower() != filter_by_type.lower():
                    continue

                filtered_agents[name] = metadata

            if not filtered_agents:
                return "No agents match the specified criteria."

            # Format output
            agent_list = []
            for name, metadata in filtered_agents.items():
                status = "Active" if metadata.is_active else "Inactive"
                agent_list.append(
                    f"- {name} ({metadata.agent_type}): {metadata.description} [{status}]"
                )

            return f"Available agents ({len(filtered_agents)}):\n" + "\n".join(agent_list)

        except Exception as e:
            return f"Error listing agents: {str(e)}"

    return Tool(
        name="list_agents",
        description="List all available agents with their capabilities",
        func=list_agents,
    )


def create_execution_status_tool(supervisor) -> Tool:
    """Create a tool for checking execution status.

    Args:
        supervisor: The supervisor instance

    Returns:
        Tool for checking execution status
    """

    def get_execution_status() -> str:
        """Get current execution status and recent activity.

        Returns:
            Formatted execution status
        """
        try:
            status = supervisor.get_execution_status()

            output = []
            output.append(f"Active Agent: {status.get('active_agent', 'None')}")
            output.append(f"Total Agents: {status.get('total_agents', 0)}")

            recent = status.get("recent_executions", [])
            if recent:
                output.append(f"\nRecent Executions ({len(recent)}):")
                for exec_data in recent[-3:]:  # Show last 3
                    agent = exec_data.get("agent", "Unknown")
                    task = (
                        exec_data.get("task", "Unknown")[:50] + "..."
                        if len(exec_data.get("task", "")) > 50
                        else exec_data.get("task", "")
                    )
                    timestamp = exec_data.get("timestamp", "Unknown")
                    output.append(f"- {agent}: {task} [{timestamp}]")
            else:
                output.append("\nNo recent executions.")

            return "\n".join(output)

        except Exception as e:
            return f"Error getting execution status: {str(e)}"

    return Tool(
        name="execution_status",
        description="Get current execution status and recent activity",
        func=get_execution_status,
    )


def create_agent_creation_tool(supervisor) -> Tool:
    """Create a tool for dynamic agent creation.

    Args:
        supervisor: The supervisor instance (must support dynamic creation)

    Returns:
        Tool for creating new agents
    """

    def create_agent(
        name: str,
        description: str,
        agent_type: str = "simple",
        config: Optional[Dict[str, Any]] = None,
    ) -> str:
        """Create a new agent dynamically.

        Args:
            name: Name for the new agent
            description: Description of agent capabilities
            agent_type: Type of agent to create
            config: Optional agent configuration

        Returns:
            Result of agent creation
        """
        try:
            # Check if supervisor supports dynamic creation
            if not hasattr(supervisor, "create_agent"):
                return "This supervisor does not support dynamic agent creation."

            if (
                not hasattr(supervisor, "agent_creation_enabled")
                or not supervisor.agent_creation_enabled
            ):
                return "Dynamic agent creation is not enabled for this supervisor."

            # Check if agent already exists
            if name in supervisor.supervisor_state.agents:
                return f"Agent '{name}' already exists."

            # Create the agent
            success = supervisor.create_agent(name, description, agent_type)

            if success:
                return f"Successfully created agent '{name}' of type '{agent_type}'"
            else:
                return f"Failed to create agent '{name}'"

        except Exception as e:
            return f"Error creating agent: {str(e)}"

    return Tool(
        name="create_agent",
        description="Create a new agent with specified name, description, and type",
        func=create_agent,
    )


def build_supervisor_tools(supervisor) -> List[Tool]:
    """Build all standard supervisor tools.

    Args:
        supervisor: The supervisor instance

    Returns:
        List of supervisor tools
    """
    tools = [
        create_supervisor_handoff_tool(supervisor),
        create_list_agents_tool(supervisor),
        create_execution_status_tool(supervisor),
    ]

    # Add agent creation tool if supervisor supports it
    if hasattr(supervisor, "create_agent"):
        tools.append(create_agent_creation_tool(supervisor))

    return tools


def sync_tools_with_state(supervisor, tools: List[Tool]) -> None:
    """Synchronize tools with supervisor state.

    This function updates the supervisor's tool mappings based on available tools.

    Args:
        supervisor: The supervisor instance
        tools: List of tools to synchronize
    """
    try:
        from haive.agents.experiments.supervisor.state_models import ToolMapping

        # Clear existing tool mappings
        supervisor.supervisor_state.tool_mappings = []

        # Add mappings for each tool
        for tool in tools:
            mapping = ToolMapping(
                tool_name=tool.name,
                agent_name=supervisor.name,
                description=tool.description,
                parameters=getattr(tool, "args_schema", {}),
            )
            supervisor.supervisor_state.tool_mappings.append(mapping)

    except Exception as e:
        # Silently handle errors to avoid breaking supervisor functionality
        pass
