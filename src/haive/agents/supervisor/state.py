"""State management for Dynamic Supervisor V2.

This module defines the state structures used by the dynamic supervisor to track
agents, tasks, metrics, and workflow execution.
"""

import operator
from collections.abc import Sequence
from datetime import datetime
from typing import Annotated, Any, TypedDict

from langchain_core.messages import BaseMessage
from pydantic import BaseModel, Field

from haive.agents.supervisor.models import AgentCapability, AgentSpec


class ActiveAgent(BaseModel):
    """Represents an active agent instance in the supervisor.

    Attributes:
        name: Unique identifier for the agent
        instance: The actual agent instance (excluded from serialization)
        capability: Full capability metadata for this agent
        created_at: When this agent was instantiated
        last_task: Description of the last task assigned
        task_count: Number of tasks completed
        total_execution_time: Cumulative execution time in seconds
        error_count: Number of errors encountered
        state: Current agent state (idle, busy, error)
    """

    name: str = Field(..., description="Agent identifier")
    instance: Any = Field(..., description="Agent instance", exclude=True)
    capability: AgentCapability = Field(..., description="Agent capabilities")
    created_at: datetime = Field(
        default_factory=datetime.now, description="Creation timestamp"
    )
    last_task: str | None = Field(None, description="Last assigned task")
    task_count: int = Field(0, description="Tasks completed")
    total_execution_time: float = Field(0.0, description="Total execution seconds")
    error_count: int = Field(0, description="Errors encountered")
    state: str = Field("idle", description="Current state: idle, busy, error")

    model_config = {"arbitrary_types_allowed": True}

    def update_metrics(self, execution_time: float, success: bool = True) -> None:
        """Update agent metrics after task execution.

        Args:
            execution_time: Time taken for the task in seconds
            success: Whether the task completed successfully
        """
        self.task_count += 1
        self.total_execution_time += execution_time
        if not success:
            self.error_count += 1

        # Update capability performance score
        success_rate = (self.task_count - self.error_count) / self.task_count
        self.capability.performance_score = success_rate
        self.capability.usage_count = self.task_count
        self.capability.last_used = datetime.now().isoformat()

    @property
    def average_execution_time(self) -> float:
        """Calculate average execution time per task."""
        if self.task_count == 0:
            return 0.0
        return self.total_execution_time / self.task_count

    @property
    def success_rate(self) -> float:
        """Calculate task success rate."""
        if self.task_count == 0:
            return 1.0
        return (self.task_count - self.error_count) / self.task_count


class SupervisorMetrics(BaseModel):
    """Metrics tracking for the supervisor's performance.

    Attributes:
        total_tasks: Total tasks processed
        successful_tasks: Tasks completed successfully
        failed_tasks: Tasks that failed
        agent_creations: Number of agents created
        discovery_attempts: Number of discovery attempts
        successful_discoveries: Successful discoveries
        total_execution_time: Total time spent on tasks
        start_time: When supervisor was created
        last_task_time: Timestamp of last task
    """

    total_tasks: int = Field(0, description="Total tasks processed")
    successful_tasks: int = Field(0, description="Successful completions")
    failed_tasks: int = Field(0, description="Failed tasks")
    agent_creations: int = Field(0, description="Agents created")
    discovery_attempts: int = Field(0, description="Discovery attempts")
    successful_discoveries: int = Field(0, description="Successful discoveries")
    total_execution_time: float = Field(0.0, description="Total execution seconds")
    start_time: datetime = Field(
        default_factory=datetime.now, description="Supervisor start time"
    )
    last_task_time: datetime | None = Field(None, description="Last task timestamp")

    @property
    def success_rate(self) -> float:
        """Calculate overall success rate."""
        if self.total_tasks == 0:
            return 1.0
        return self.successful_tasks / self.total_tasks

    @property
    def discovery_success_rate(self) -> float:
        """Calculate discovery success rate."""
        if self.discovery_attempts == 0:
            return 1.0
        return self.successful_discoveries / self.discovery_attempts

    @property
    def uptime_hours(self) -> float:
        """Calculate supervisor uptime in hours."""
        delta = datetime.now() - self.start_time
        return delta.total_seconds() / 3600


class DynamicSupervisorState(TypedDict):
    """State structure for dynamic supervisor execution.

    This TypedDict defines the state that flows through the supervisor's
    execution graph in LangGraph.

    Attributes:
        messages: Conversation history (LangGraph standard)
        active_agents: Currently instantiated agents
        agent_capabilities: All known agent capabilities
        discovered_agents: Set of agent names that have been discovered
        available_specs: Agent specifications that can be instantiated
        current_agent: Name of agent handling current task
        agent_task: Task assigned to current agent
        agent_response: Response from current agent
        next_agent: Next agent to route to
        supervisor_metrics: Performance metrics
        discovery_cache: Cache of discovery results
        workflow_state: Current workflow state (routing, executing, etc.)
    """

    # Standard LangGraph message history
    messages: Annotated[Sequence[BaseMessage], operator.add]

    # Agent management
    active_agents: dict[str, ActiveAgent]
    agent_capabilities: dict[str, AgentCapability]
    discovered_agents: set[str]
    available_specs: list[AgentSpec]

    # Task routing
    current_agent: str
    agent_task: str
    agent_response: str
    next_agent: str

    # Metrics and monitoring
    supervisor_metrics: SupervisorMetrics

    # Discovery and caching
    discovery_cache: dict[str, list[AgentSpec]]

    # Workflow control
    workflow_state: str  # "routing", "discovering", "executing", "complete"


def create_initial_state(
    available_specs: list[AgentSpec] | None = None,
    discovery_cache: dict[str, list[AgentSpec]] | None = None,
) -> DynamicSupervisorState:
    """Create initial state for dynamic supervisor.

    Args:
        available_specs: Initial agent specifications
        discovery_cache: Pre-populated discovery cache

    Returns:
        Initialized supervisor state
    """
    return {
        "messages": [],
        "active_agents": {},
        "agent_capabilities": {},
        "discovered_agents": set(),
        "available_specs": available_specs or [],
        "current_agent": "",
        "agent_task": "",
        "agent_response": "",
        "next_agent": "",
        "supervisor_metrics": SupervisorMetrics(),
        "discovery_cache": discovery_cache or {},
        "workflow_state": "routing",
    }
