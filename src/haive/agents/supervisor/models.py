"""Data models for Dynamic Supervisor V2.

This module contains all the Pydantic models and enums used by the dynamic supervisor
for agent specifications, capabilities, and configuration.
"""

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, field_validator


class AgentDiscoveryMode(str, Enum):
    """Agent discovery modes for the dynamic supervisor.

    Attributes:
        MANUAL: Use manually provided agent specifications
        COMPONENT_DISCOVERY: Discover agents from installed components
        RAG_DISCOVERY: Use RAG to find relevant agent implementations
        MCP_DISCOVERY: Discover agents via Model Context Protocol
        HYBRID: Combine multiple discovery methods
    """

    MANUAL = "manual"
    COMPONENT_DISCOVERY = "component_discovery"
    RAG_DISCOVERY = "rag_discovery"
    MCP_DISCOVERY = "mcp_discovery"
    HYBRID = "hybrid"


class AgentCapability(BaseModel):
    """Rich metadata describing an agent's capabilities.

    This model captures comprehensive information about what an agent can do,
    enabling intelligent task-to-agent matching.

    Attributes:
        name: Unique identifier for the agent
        agent_type: Type of agent (e.g., SimpleAgentV3, ReactAgent)
        description: Human-readable description of agent's purpose
        specialties: List of task domains the agent excels at
        tools: Names of tools available to this agent
        active: Whether the agent is currently active
        performance_score: Historical performance metric (0-1)
        usage_count: Number of times this agent has been used
        last_used: Timestamp of last usage (ISO format)
        metadata: Additional custom metadata

    Examples:
        >>> capability = AgentCapability(
        ...     name="research_expert",
        ...     agent_type="ReactAgent",
        ...     description="Expert at research and information gathering",
        ...     specialties=["research", "analysis", "web search"],
        ...     tools=["web_search", "document_reader"]
        ... )
    """

    name: str = Field(..., description="Unique agent identifier")
    agent_type: str = Field(..., description="Type of agent implementation")
    description: str = Field(..., description="What this agent can do")
    specialties: list[str] = Field(
        default_factory=list, description="Areas of expertise (used for matching)"
    )
    tools: list[str] = Field(
        default_factory=list, description="Names of tools available to this agent"
    )
    active: bool = Field(default=True, description="Whether agent is currently active")
    performance_score: float = Field(
        default=1.0, ge=0.0, le=1.0, description="Historical performance metric"
    )
    usage_count: int = Field(default=0, description="Number of times used")
    last_used: str | None = Field(
        default=None, description="ISO timestamp of last usage"
    )
    metadata: dict[str, Any] = Field(
        default_factory=dict, description="Additional custom metadata"
    )

    @field_validator("specialties")
    @classmethod
    def validate_specialties(cls, v: list[str]) -> list[str]:
        """Ensure specialties are lowercase for consistent matching."""
        return [s.lower().strip() for s in v if s.strip()]

    def matches_task(self, task: str, threshold: float = 0.3) -> float:
        """Calculate match score between this agent's capabilities and a task.

        Args:
            task: The task description to match against
            threshold: Minimum score to consider a match (0-1)

        Returns:
            Match score between 0 and 1
        """
        task_lower = task.lower()
        score = 0.0

        # Check specialties (highest weight)
        for specialty in self.specialties:
            if specialty in task_lower:
                score += 0.4

        # Check description words
        desc_words = self.description.lower().split()
        for word in desc_words:
            if len(word) > 3 and word in task_lower:
                score += 0.1

        # Check tool names
        for tool in self.tools:
            if tool.replace("_", " ") in task_lower:
                score += 0.2

        # Cap at 1.0 and apply performance modifier
        score = min(score, 1.0) * self.performance_score

        return score if score >= threshold else 0.0


class AgentSpec(BaseModel):
    """Specification for creating an agent dynamically.

    This model defines everything needed to instantiate a new agent at runtime,
    including its type, configuration, and capabilities.

    Attributes:
        name: Unique identifier for the agent
        agent_type: Type of agent to create (e.g., "SimpleAgentV3", "ReactAgent")
        description: Human-readable description
        specialties: Task domains this agent should handle
        tools: Tool names or instances to provide to the agent
        config: Configuration dictionary for agent initialization
        priority: Priority level for agent selection (higher = preferred)
        enabled: Whether this spec can be used to create agents

    Examples:
        >>> spec = AgentSpec(
        ...     name="code_reviewer",
        ...     agent_type="ReactAgent",
        ...     description="Expert code reviewer and analyzer",
        ...     specialties=["code review", "analysis", "best practices"],
        ...     tools=["file_reader", "code_analyzer"],
        ...     config={
        ...         "temperature": 0.2,
        ...         "system_message": "You are an expert code reviewer."
        ...     }
        ... )
    """

    name: str = Field(..., description="Unique agent identifier")
    agent_type: str = Field(
        default="SimpleAgentV3", description="Type of agent to create"
    )
    description: str = Field(..., description="What this agent does")
    specialties: list[str] = Field(
        default_factory=list, description="Task domains for matching"
    )
    tools: list[Any] = Field(
        default_factory=list, description="Tool names or instances"
    )
    config: dict[str, Any] = Field(
        default_factory=dict, description="Agent initialization config"
    )
    priority: int = Field(
        default=0, description="Priority for selection (higher = preferred)"
    )
    enabled: bool = Field(default=True, description="Whether this spec can be used")

    @field_validator("specialties")
    @classmethod
    def validate_specialties(cls, v: list[str]) -> list[str]:
        """Ensure specialties are lowercase for consistent matching."""
        return [s.lower().strip() for s in v if s.strip()]

    def to_capability(self) -> AgentCapability:
        """Convert this spec to an AgentCapability."""
        return AgentCapability(
            name=self.name,
            agent_type=self.agent_type,
            description=self.description,
            specialties=self.specialties,
            tools=[
                t if isinstance(t, str) else getattr(t, "name", str(t))
                for t in self.tools
            ],
            active=False,  # Not active until created
        )


class DiscoveryConfig(BaseModel):
    """Configuration for agent discovery mechanisms.

    Attributes:
        mode: Discovery mode to use
        component_paths: Paths to search for component discovery
        rag_collection: Collection name for RAG discovery
        mcp_endpoints: MCP server endpoints for discovery
        cache_discoveries: Whether to cache discovered agents
        discovery_timeout: Timeout for discovery operations (seconds)
        max_discoveries_per_request: Maximum agents to discover per request
    """

    mode: AgentDiscoveryMode = Field(
        default=AgentDiscoveryMode.MANUAL, description="Discovery mode to use"
    )
    component_paths: list[str] = Field(
        default_factory=list, description="Paths for component discovery"
    )
    rag_collection: str | None = Field(
        default=None, description="RAG collection for discovery"
    )
    mcp_endpoints: list[str] = Field(
        default_factory=list, description="MCP endpoints for discovery"
    )
    cache_discoveries: bool = Field(default=True, description="Cache discovered agents")
    discovery_timeout: float = Field(
        default=30.0, description="Discovery timeout in seconds"
    )
    max_discoveries_per_request: int = Field(
        default=5, description="Max agents to discover per request"
    )
