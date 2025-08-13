r"""SimpleSupervisor - Lightweight supervisor for basic routing needs.

This module provides the SimpleSupervisor class, a lightweight alternative to
SupervisorAgent that extends MultiAgent instead of ReactAgent. It's designed
for scenarios where you need simple routing without the overhead of ReactAgent's
looping behavior.

**Current Status**: This is a **lightweight supervisor** for simple use cases.
For full-featured supervision with tool execution, use SupervisorAgent. For
dynamic agent management, use DynamicSupervisor.

The SimpleSupervisor uses an LLM to make routing decisions but executes in a
single pass without the continuous looping of ReactAgent-based supervisors.

Key Features:
    - **Lightweight design**: Extends MultiAgent for minimal overhead
    - **Single-pass execution**: No continuous looping
    - **LLM routing**: Intelligent agent selection
    - **Clean API**: Simple agent registration with descriptions
    - **Custom prompts**: Configurable routing prompts
    - **Direct execution**: Routes and executes in one step

Use Cases:
    - Simple request routing to specialized agents
    - One-shot task delegation
    - Lightweight agent coordination
    - When ReactAgent features aren't needed

Example:
    Basic routing setup::

        >>> from haive.agents.supervisor import SimpleSupervisor
        >>> from haive.agents.simple import SimpleAgent
        >>> from haive.core.engine.aug_llm import AugLLMConfig
        >>>
        >>> # Create specialized agents
        >>> calculator = SimpleAgent(name="calculator", engine=config)
        >>> writer = SimpleAgent(name="writer", engine=config)
        >>>
        >>> # Create simple supervisor
        >>> supervisor = SimpleSupervisor(
        ...     name="router",
        ...     engine=AugLLMConfig(temperature=0.3),
        ...     agents={
        ...         "calculator": AgentInfo(
        ...             agent=calculator,
        ...             description="Handles math and calculations"
        ...         ),
        ...         "writer": AgentInfo(
        ...             agent=writer,
        ...             description="Handles writing and content creation"
        ...         )
        ...     }
        ... )
        >>>
        >>> # Single-pass routing and execution
        >>> result = await supervisor.arun("Calculate 15% of 200")

    Custom routing prompt::

        >>> custom_prompt = ChatPromptTemplate.from_template(
        ...     "Route this request to the best agent: {query}\\n"
        ...     "Agents: {agent_descriptions}\\n"
        ...     "Choice:"
        ... )
        >>>
        >>> supervisor = SimpleSupervisor(
        ...     name="custom_router",
        ...     engine=config,
        ...     prompt_template=custom_prompt,
        ...     agents={...}
        ... )

See Also:
    - :class:`haive.agents.supervisor.SupervisorAgent`: Full-featured supervisor
    - :class:`haive.agents.supervisor.DynamicSupervisor`: Dynamic agent management
    - :class:`haive.agents.multi.MultiAgent`: Base class
"""

import logging
from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.node.agent_node_v3 import AgentNodeV3Config
from haive.core.graph.node.engine_node import EngineNodeConfig
from haive.core.graph.state_graph.base_graph2 import BaseGraph
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import END, START
from pydantic import BaseModel, Field

from haive.agents.base import Agent
from haive.agents.multi.archive.multi_agent import MultiAgent

logger = logging.getLogger(__name__)


# Default supervisor prompt
DEFAULT_SUPERVISOR_PROMPT = ChatPromptTemplate.from_template(
    """
You are a supervisor managing the following agents:

{agent_descriptions}

Current conversation:
{messages}

Based on the conversation, which agent should handle the next response?
Respond with ONLY the agent name or "END" if the task is complete.

Decision:"""
)


class AgentInfo(BaseModel):
    """Information about a registered agent."""

    agent: Agent = Field(..., description="The agent instance")
    description: str = Field(..., description="Agent capabilities description")


class SimpleSupervisor(MultiAgent):
    """Simple supervisor that routes between agents using LLM decisions.

    This supervisor:
    1. Accepts a user message
    2. Uses an LLM to decide which agent should handle it
    3. Routes to that agent
    4. Returns the agent's response

    The routing decision is based on agent descriptions and conversation context.
    """

    # ========================================================================
    # SUPERVISOR CONFIGURATION
    # ========================================================================

    supervisor_llm: AugLLMConfig | None = Field(
        default=None,
        description="LLM for routing decisions (uses default if not provided)",
    )

    supervisor_prompt: ChatPromptTemplate | None = Field(
        default=None, description="Prompt template for routing decisions"
    )

    agent_info: dict[str, AgentInfo] = Field(
        default_factory=dict, description="Information about registered agents"
    )

    # ========================================================================
    # SETUP
    # ========================================================================

    def setup_agent(self) -> None:
        """Setup supervisor with routing LLM."""
        # Ensure we have a supervisor LLM
        if not self.supervisor_llm:
            self.supervisor_llm = AugLLMConfig(temperature=0.1)

        # Set as coordinator config for parent class
        self.coordinator_config = self.supervisor_llm

        # Force conditional mode
        self.execution_mode = "conditional"

        # Extract agents from agent_info
        self.agents = {name: info.agent for name, info in self.agent_info.items()}

        # Call parent setup
        super().setup_agent()

    # ========================================================================
    # AGENT REGISTRATION
    # ========================================================================

    def register_agent(self, name: str, agent: Agent, description: str) -> None:
        """Register an agent with the supervisor.

        Args:
            name: Unique name for the agent
            agent: The agent instance
            description: Description of agent capabilities
        """
        self.agent_info[name] = AgentInfo(agent=agent, description=description)
        self.agents[name] = agent
        logger.info(f"Registered agent '{name}': {description}")

    # ========================================================================
    # CUSTOM GRAPH BUILDING
    # ========================================================================

    def build_graph(self) -> BaseGraph:
        """Build supervisor graph with dynamic routing."""
        graph = BaseGraph(name=self.name)

        if not self.agents:
            raise ValueError("No agents registered with supervisor")

        # Add supervisor decision node
        supervisor_node = EngineNodeConfig(
            name="supervisor", engine=self.supervisor_llm
        )
        graph.add_node("supervisor", supervisor_node)
        graph.add_edge(START, "supervisor")

        # Add agent nodes
        for name, agent in self.agents.items():
            node = AgentNodeV3Config(name=f"{name}_agent", agent=agent)
            graph.add_node(f"{name}_agent", node)
            graph.add_edge(f"{name}_agent", END)

        # Create routing function
        def route_to_agent(state: dict[str, Any]) -> str:
            """Route based on supervisor decision."""
            messages = state.get("messages", [])

            # Prepare agent descriptions
            descriptions = "\n".join(
                [
                    f"- {name}: {info.description}"
                    for name, info in self.agent_info.items()
                ]
            )

            # Use supervisor prompt
            prompt = self.supervisor_prompt or DEFAULT_SUPERVISOR_PROMPT
            prompt.format(agent_descriptions=descriptions, messages=messages)

            # Get supervisor decision
            if messages and hasattr(messages[-1], "content"):
                decision = messages[-1].content.strip().lower()

                # Check for END signal
                if decision == "end":
                    return END

                # Match agent name
                for agent_name in self.agents:
                    if agent_name.lower() in decision:
                        logger.info(f"Routing to agent: {agent_name}")
                        return f"{agent_name}_agent"

            # Default to first agent
            default_agent = next(iter(self.agents.keys()))
            logger.warning(f"No clear routing decision, defaulting to: {default_agent}")
            return f"{default_agent}_agent"

        # Create route map
        route_map = {f"{name}_agent": f"{name}_agent" for name in self.agents}
        route_map[END] = END

        # Add conditional routing
        graph.add_conditional_edges("supervisor", route_to_agent, route_map)

        return graph

    # ========================================================================
    # CONVENIENCE METHODS
    # ========================================================================

    @classmethod
    def create_with_agents(
        cls,
        agents: list[tuple[str, Agent, str]],
        name: str = "supervisor",
        supervisor_llm: AugLLMConfig | None = None,
        **kwargs,
    ) -> "SimpleSupervisor":
        """Create supervisor with a list of agents.

        Args:
            agents: List of (name, agent, description) tuples
            name: Supervisor name
            supervisor_llm: LLM for routing decisions
            **kwargs: Additional arguments

        Returns:
            SimpleSupervisor instance

        Example:
            supervisor = SimpleSupervisor.create_with_agents([
                ("writer", writer_agent, "Writes creative content"),
                ("coder", coder_agent, "Writes and reviews code"),
                ("analyst", analyst_agent, "Analyzes data and trends")
            ])
        """
        supervisor = cls(name=name, supervisor_llm=supervisor_llm, **kwargs)

        for agent_name, agent, description in agents:
            supervisor.register_agent(agent_name, agent, description)

        return supervisor
