"""State management for supervisors."""

from haive.agents.supervisor.state.dynamic_state import (
    DynamicSupervisorState,
    SupervisorDecision,
)

# Re-export from the legacy state module (state.py is shadowed by this directory)
# These are needed by supervisor/agent.py
import operator
from collections.abc import Sequence
from datetime import datetime
from typing import Annotated, Any, TypedDict

from langchain_core.messages import BaseMessage
from pydantic import BaseModel, Field

from haive.agents.supervisor.models import AgentCapability, AgentSpec


class ActiveAgent(BaseModel):
    """Represents an active agent instance in the supervisor."""

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
        """Update agent metrics after task execution."""
        self.task_count += 1
        self.total_execution_time += execution_time
        if not success:
            self.error_count += 1
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
    """Metrics tracking for the supervisor's performance."""

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


class DynamicSupervisorStateTypedDict(TypedDict):
    """TypedDict state for dynamic supervisor execution graph."""

    messages: Annotated[Sequence[BaseMessage], operator.add]
    active_agents: dict[str, ActiveAgent]
    agent_capabilities: dict[str, AgentCapability]
    discovered_agents: set[str]
    available_specs: list[AgentSpec]
    current_agent: str
    agent_task: str
    agent_response: str
    next_agent: str
    supervisor_metrics: SupervisorMetrics
    discovery_cache: dict[str, list[AgentSpec]]
    workflow_state: str


def create_initial_state(
    available_specs: list[AgentSpec] | None = None,
    discovery_cache: dict[str, list[AgentSpec]] | None = None,
) -> DynamicSupervisorStateTypedDict:
    """Create initial state for dynamic supervisor."""
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


__all__ = [
    "ActiveAgent",
    "DynamicSupervisorState",
    "DynamicSupervisorStateTypedDict",
    "SupervisorDecision",
    "SupervisorMetrics",
    "create_initial_state",
]
