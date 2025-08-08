"""Base supervisor implementation for multi-agent systems.

This module provides the core supervisor classes that can manage multiple agents,
handle tool synchronization, and support dynamic agent creation.
"""

from typing import Any, Dict, List, Optional, Union

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.tools import Tool
from pydantic import BaseModel, Field

from haive.agents.react.agent import ReactAgent


class AgentMetadata(BaseModel):
    """Metadata for a registered agent."""

    name: str = Field(..., description="Agent name/identifier")
    description: str = Field(..., description="Description of agent capabilities")
    agent_type: str = Field(..., description="Type/class of the agent")
    capabilities: List[str] = Field(
        default_factory=list, description="List of agent capabilities"
    )
    created_at: str = Field(..., description="Creation timestamp")
    last_used: Optional[str] = Field(None, description="Last usage timestamp")


class SupervisorState(BaseModel):
    """State model for supervisor agents."""

    agents: Dict[str, AgentMetadata] = Field(
        default_factory=dict, description="Registered agents"
    )
    current_context: Dict[str, Any] = Field(
        default_factory=dict, description="Current execution context"
    )
    execution_history: List[Dict[str, Any]] = Field(
        default_factory=list, description="Execution history"
    )
    active_agent: Optional[str] = Field(None, description="Currently active agent")


class BaseSupervisor(ReactAgent):
    """Base supervisor agent for managing multiple agents.

    This supervisor can register agents, delegate tasks, and coordinate
    multi-agent workflows.
    """

    def __init__(
        self,
        name: str,
        engine: AugLLMConfig,
        agents: Optional[Dict[str, Any]] = None,
        **kwargs,
    ):
        """Initialize the supervisor.

        Args:
            name: Supervisor name
            engine: LLM configuration
            agents: Optional initial agents to register
            **kwargs: Additional arguments passed to ReactAgent
        """
        # Initialize as ReactAgent
        super().__init__(name=name, engine=engine, **kwargs)

        # Initialize supervisor state
        self.supervisor_state = SupervisorState()

        # Register initial agents if provided
        if agents:
            for agent_name, agent in agents.items():
                self.register_agent(agent_name, f"Agent: {agent_name}", agent)

    def register_agent(self, name: str, description: str, agent: Any) -> None:
        """Register an agent with the supervisor.

        Args:
            name: Agent identifier
            description: Description of agent capabilities
            agent: The agent instance
        """
        import datetime

        metadata = AgentMetadata(
            name=name,
            description=description,
            agent_type=type(agent).__name__,
            capabilities=[],  # Could be extracted from agent
            created_at=datetime.datetime.now().isoformat(),
        )

        self.supervisor_state.agents[name] = metadata

        # Store actual agent instance (simplified approach)
        setattr(self, f"_agent_{name}", agent)

    def get_agent(self, name: str) -> Optional[Any]:
        """Get a registered agent by name.

        Args:
            name: Agent identifier

        Returns:
            The agent instance if found, None otherwise
        """
        if name in self.supervisor_state.agents:
            return getattr(self, f"_agent_{name}", None)
        return None

    def list_agents(self) -> Dict[str, AgentMetadata]:
        """List all registered agents.

        Returns:
            Dictionary of agent metadata
        """
        return self.supervisor_state.agents.copy()

    def delegate_task(self, agent_name: str, task: str) -> str:
        """Delegate a task to a specific agent.

        Args:
            agent_name: Name of the agent to delegate to
            task: Task description

        Returns:
            Result from the agent
        """
        agent = self.get_agent(agent_name)
        if not agent:
            return f"Agent '{agent_name}' not found"

        try:
            # Update state
            self.supervisor_state.active_agent = agent_name

            # Execute task
            if hasattr(agent, "run"):
                result = agent.run(task)
            elif hasattr(agent, "invoke"):
                result = agent.invoke(task)
            else:
                result = str(agent)

            # Record in history
            import datetime

            self.supervisor_state.execution_history.append(
                {
                    "agent": agent_name,
                    "task": task,
                    "result": (
                        str(result)[:200] + "..."
                        if len(str(result)) > 200
                        else str(result)
                    ),
                    "timestamp": datetime.datetime.now().isoformat(),
                }
            )

            return str(result)

        except Exception as e:
            return f"Error executing task with agent '{agent_name}': {str(e)}"

    def get_execution_status(self) -> Dict[str, Any]:
        """Get current execution status.

        Returns:
            Status information including active agent and recent history
        """
        return {
            "active_agent": self.supervisor_state.active_agent,
            "total_agents": len(self.supervisor_state.agents),
            "recent_executions": self.supervisor_state.execution_history[-5:],  # Last 5
            "context": self.supervisor_state.current_context,
        }


class DynamicSupervisor(BaseSupervisor):
    """Extended supervisor with dynamic agent creation capabilities.

    This supervisor can create new agents on demand based on requirements.
    """

    def __init__(self, *args, **kwargs):
        """Initialize dynamic supervisor."""
        super().__init__(*args, **kwargs)
        self.agent_creation_enabled = False

    def enable_agent_creation(self, enable: bool = True) -> None:
        """Enable or disable dynamic agent creation.

        Args:
            enable: Whether to enable agent creation
        """
        self.agent_creation_enabled = enable

    def create_agent(
        self, name: str, description: str, agent_type: str = "simple"
    ) -> bool:
        """Create a new agent dynamically.

        Args:
            name: Agent name
            description: Agent description
            agent_type: Type of agent to create

        Returns:
            True if agent was created successfully
        """
        if not self.agent_creation_enabled:
            return False

        try:
            # Create a simple agent (simplified approach)
            from haive.agents.simple.agent import SimpleAgent

            # Use basic engine config for simplicity
            new_agent = SimpleAgent(
                name=name,
                engine=AugLLMConfig(),  # Use default config
            )

            # Register the new agent
            self.register_agent(name, description, new_agent)
            return True

        except Exception:
            return False

    def get_capabilities(self) -> Dict[str, Any]:
        """Get supervisor capabilities.

        Returns:
            Dictionary describing supervisor capabilities
        """
        return {
            "agent_management": True,
            "task_delegation": True,
            "dynamic_creation": self.agent_creation_enabled,
            "total_agents": len(self.supervisor_state.agents),
            "supported_agent_types": ["simple", "react"],
        }
