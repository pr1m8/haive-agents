"""State models for supervisor agents.

This module defines the state schemas and data models used by supervisor agents
for managing multi-agent systems.
"""

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class AgentMetadata(BaseModel):
    """Metadata for a registered agent."""

    name: str = Field(..., description="Agent name/identifier")
    description: str = Field(..., description="Description of agent capabilities")
    agent_type: str = Field(..., description="Type/class of the agent")
    capabilities: list[str] = Field(
        default_factory=list, description="List of agent capabilities"
    )
    created_at: str = Field(..., description="Creation timestamp")
    last_used: str | None = Field(None, description="Last usage timestamp")
    is_active: bool = Field(default=True, description="Whether agent is active")
    metadata: dict[str, Any] = Field(
        default_factory=dict, description="Additional metadata"
    )


class SerializedAgent(BaseModel):
    """Serialized representation of an agent for storage/transfer."""

    name: str = Field(..., description="Agent name")
    agent_class: str = Field(..., description="Agent class name")
    config: dict[str, Any] = Field(..., description="Agent configuration")
    state: dict[str, Any] = Field(default_factory=dict, description="Agent state")
    tools: list[str] = Field(default_factory=list, description="Available tools")


class ToolMapping(BaseModel):
    """Mapping between tools and agents."""

    tool_name: str = Field(..., description="Tool identifier")
    agent_name: str = Field(..., description="Agent that provides this tool")
    description: str = Field(..., description="Tool description")
    parameters: dict[str, Any] = Field(
        default_factory=dict, description="Tool parameters schema"
    )


class ExecutionContext(BaseModel):
    """Context for agent execution."""

    task_id: str = Field(..., description="Unique task identifier")
    requester: str = Field(..., description="Who requested the task")
    priority: int = Field(default=5, ge=1, le=10, description="Task priority (1-10)")
    context: dict[str, Any] = Field(
        default_factory=dict, description="Execution context"
    )
    started_at: str = Field(..., description="Task start timestamp")
    completed_at: str | None = Field(None, description="Task completion timestamp")
    status: str = Field(default="pending", description="Task status")
    result: str | None = Field(None, description="Task result")
    error: str | None = Field(None, description="Error message if failed")


class SupervisorState(BaseModel):
    """State model for supervisor agents."""

    agents: dict[str, AgentMetadata] = Field(
        default_factory=dict, description="Registered agents"
    )
    current_context: dict[str, Any] = Field(
        default_factory=dict, description="Current execution context"
    )
    execution_history: list[ExecutionContext] = Field(
        default_factory=list, description="Execution history"
    )
    active_agent: str | None = Field(None, description="Currently active agent")
    tool_mappings: list[ToolMapping] = Field(
        default_factory=list, description="Tool to agent mappings"
    )
    supervisor_config: dict[str, Any] = Field(
        default_factory=dict, description="Supervisor configuration"
    )

    def add_execution(
        self, agent_name: str, task: str, task_id: str | None = None
    ) -> ExecutionContext:
        """Add a new execution context.

        Args:
            agent_name: Name of the executing agent
            task: Task description
            task_id: Optional task ID (generated if not provided)

        Returns:
            The created execution context
        """
        if task_id is None:
            task_id = f"task_{len(self.execution_history) + 1}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        execution = ExecutionContext(
            task_id=task_id,
            requester=agent_name,
            context={"task": task, "agent": agent_name},
            started_at=datetime.now().isoformat(),
            status="running",
        )

        self.execution_history.append(execution)
        return execution

    def complete_execution(
        self, task_id: str, result: str, error: str | None = None
    ) -> bool:
        """Complete an execution context.

        Args:
            task_id: Task identifier
            result: Execution result
            error: Optional error message

        Returns:
            True if execution was found and updated
        """
        for execution in self.execution_history:
            if execution.task_id == task_id:
                execution.completed_at = datetime.now().isoformat()
                execution.result = result
                execution.error = error
                execution.status = "error" if error else "completed"
                return True
        return False

    def get_recent_executions(self, limit: int = 10) -> list[ExecutionContext]:
        """Get recent executions.

        Args:
            limit: Maximum number of executions to return

        Returns:
            List of recent execution contexts
        """
        return self.execution_history[-limit:] if self.execution_history else []

    def get_agent_statistics(self) -> dict[str, Any]:
        """Get statistics about agents and executions.

        Returns:
            Dictionary with agent statistics
        """
        total_executions = len(self.execution_history)
        successful_executions = len(
            [e for e in self.execution_history if e.status == "completed"]
        )
        failed_executions = len(
            [e for e in self.execution_history if e.status == "error"]
        )

        agent_usage = {}
        for execution in self.execution_history:
            agent = execution.requester
            if agent not in agent_usage:
                agent_usage[agent] = {"total": 0, "successful": 0, "failed": 0}
            agent_usage[agent]["total"] += 1
            if execution.status == "completed":
                agent_usage[agent]["successful"] += 1
            elif execution.status == "error":
                agent_usage[agent]["failed"] += 1

        return {
            "total_agents": len(self.agents),
            "active_agents": len([a for a in self.agents.values() if a.is_active]),
            "total_executions": total_executions,
            "successful_executions": successful_executions,
            "failed_executions": failed_executions,
            "success_rate": (
                successful_executions / total_executions if total_executions > 0 else 0
            ),
            "agent_usage": agent_usage,
        }


class DynamicSupervisorState(SupervisorState):
    """Extended state model for dynamic supervisors."""

    agent_creation_enabled: bool = Field(
        default=False, description="Whether dynamic agent creation is enabled"
    )
    agent_templates: dict[str, dict[str, Any]] = Field(
        default_factory=dict, description="Templates for creating new agents"
    )
    created_agents: list[str] = Field(
        default_factory=list, description="List of dynamically created agent names"
    )
    creation_history: list[dict[str, Any]] = Field(
        default_factory=list, description="History of agent creation attempts"
    )

    def add_agent_template(self, name: str, template: dict[str, Any]) -> None:
        """Add a template for agent creation.

        Args:
            name: Template name
            template: Template configuration
        """
        self.agent_templates[name] = template

    def record_agent_creation(
        self, agent_name: str, success: bool, error: str | None = None
    ) -> None:
        """Record an agent creation attempt.

        Args:
            agent_name: Name of the agent being created
            success: Whether creation was successful
            error: Error message if creation failed
        """
        record = {
            "agent_name": agent_name,
            "success": success,
            "timestamp": datetime.now().isoformat(),
            "error": error,
        }
        self.creation_history.append(record)

        if success:
            self.created_agents.append(agent_name)

    def get_creation_statistics(self) -> dict[str, Any]:
        """Get statistics about agent creation.

        Returns:
            Creation statistics
        """
        total_attempts = len(self.creation_history)
        successful_creations = len([r for r in self.creation_history if r["success"]])
        failed_creations = total_attempts - successful_creations

        return {
            "total_creation_attempts": total_attempts,
            "successful_creations": successful_creations,
            "failed_creations": failed_creations,
            "success_rate": (
                successful_creations / total_attempts if total_attempts > 0 else 0
            ),
            "created_agents_count": len(self.created_agents),
            "available_templates": len(self.agent_templates),
        }
