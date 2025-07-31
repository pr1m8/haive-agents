"""Generic MetaAgent class for agent composition and recompilation management."""

import asyncio
from typing import Any, Generic, TypeVar

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph import BaseGraph
from haive.core.schema import StateSchema
from haive.core.schema.prebuilt.meta_state import MetaStateSchema
from pydantic import Field

from haive.agents.base.agent import Agent

# Type variable for the wrapped agent type
TAgent = TypeVar("TAgent", bound=Agent)


class MetaAgentState(StateSchema):
    """State for generic meta agents."""

    # Meta state for embedded agent
    meta_state: MetaStateSchema = Field(
        default_factory=MetaStateSchema,
        description="Meta state managing embedded agent",
    )

    # Tracking
    execution_count: int = Field(default=0)
    last_result: dict[str, Any] | None = Field(default=None)

    # Recompilation tracking
    recompilation_count: int = Field(default=0)
    last_recompilation_reason: str = Field(default="")

    # Store the wrapped agent reference
    wrapped_agent_ref: Any | None = Field(
        default=None,
        description="Reference to wrapped agent",
        exclude=True,  # Exclude from serialization
    )


class MetaAgent(Agent, Generic[TAgent]):
    """Generic meta agent that can wrap any agent type.

    This provides a generic wrapper around any agent, adding:
    - Recompilation tracking and management
    - Graph composition capabilities
    - Nested execution with state management
    - Dynamic agent modification

    Usage:
        .. code-block:: python

            # Wrap any agent type
            simple_agent = SimpleAgent(name="worker", engine=engine)
            meta_simple = MetaAgent[SimpleAgent](wrapped_agent=simple_agent)

            # Execute through meta layer
            result = await meta_simple.execute()

            # Check recompilation
            if meta_simple.needs_recompilation():
            meta_simple.recompile()

    """

    def __init__(
        self,
        wrapped_agent: TAgent,
        name: str | None = None,
        engine: AugLLMConfig | None = None,
        **kwargs,
    ):
        """Initialize meta agent with wrapped agent.

        Args:
            wrapped_agent: The agent to wrap with meta capabilities
            name: Optional name (defaults to "meta_{wrapped_agent.name}")
            engine: Optional engine (uses wrapped agent's engine if not provided)
            **kwargs: Additional arguments for Agent base class
        """
        # Store wrapped agent using object.__setattr__ to bypass Pydantic
        object.__setattr__(self, "_wrapped_agent", wrapped_agent)

        # Use wrapped agent's engine if not provided
        if engine is None and hasattr(wrapped_agent, "engine"):
            engine = wrapped_agent.engine
        elif engine is None:
            engine = AugLLMConfig()

        # Generate name if not provided
        if name is None:
            wrapped_name = getattr(wrapped_agent, "name", "agent")
            name = f"meta_{wrapped_name}"

        # Force state schema
        kwargs["state_schema"] = MetaAgentState

        super().__init__(name=name, engine=engine, **kwargs)

    def setup_agent(self) -> None:
        """Setup meta agent with wrapped agent."""
        super().setup_agent()

        # Store wrapped agent in state
        wrapped = self.wrapped_agent
        if wrapped and hasattr(self, "state"):
            self.state.wrapped_agent_ref = wrapped

            # Initialize meta state with wrapped agent
            self.state.meta_state = MetaStateSchema.from_agent(
                agent=wrapped,
                initial_state={"meta_agent": self.name},
                graph_context={
                    "wrapper_type": "MetaAgent",
                    "wrapped_type": type(wrapped).__name__,
                },
            )

    def build_graph(self) -> Any:
        """Build graph for meta agent execution.

        The meta agent delegates to the wrapped agent's graph.
        """
        # For meta agent, we can use a simple pass-through graph
        # or delegate to wrapped agent's graph
        wrapped = self.wrapped_agent
        if wrapped and hasattr(wrapped, "_app") and wrapped._app:
            return wrapped._app
        if wrapped and hasattr(wrapped, "build_graph"):
            return wrapped.build_graph()
        # Build a minimal graph that executes through meta state

        graph = BaseGraph()

        # Add a single node that executes through meta state
        def meta_execute(state: dict[str, Any]):
            # Execute wrapped agent through meta state
            result = self.state.meta_state.execute_agent(
                input_data=state, update_state=True
            )
            return result

        graph.add_node("execute", meta_execute)
        graph.set_entry_point("execute")
        graph.set_finish_point("execute")

        return graph.compile()

    @property
    def wrapped_agent(self) -> TAgent:
        """Get the wrapped agent."""
        # Try multiple methods to get the wrapped agent

        # Method 1: Direct attribute access
        try:
            return object.__getattribute__(self, "_wrapped_agent")
        except AttributeError:
            pass

        # Method 2: From __dict__
        wrapped = self.__dict__.get("_wrapped_agent")
        if wrapped:
            return wrapped

        # Method 3: From state if available
        if hasattr(self, "state") and hasattr(self.state, "wrapped_agent_ref"):
            return self.state.wrapped_agent_ref

        return None

    def needs_recompilation(self) -> bool:
        """Check if wrapped agent needs recompilation."""
        return self.state.meta_state.check_agent_recompilation()

    def recompile(self, reason: str = "Manual recompilation") -> dict[str, Any]:
        """Recompile the wrapped agent if needed."""
        result = {
            "needed_recompilation": self.needs_recompilation(),
            "recompiled": False,
            "reason": reason,
        }

        if self.needs_recompilation():
            # Mark meta state for recompilation
            self.state.meta_state.mark_for_recompile(reason)

            # If wrapped agent has recompile method, call it
            wrapped = self.wrapped_agent
            if wrapped and hasattr(wrapped, "recompile"):
                wrapped.recompile()

            # Update tracking
            self.state.recompilation_count += 1
            self.state.last_recompilation_reason = reason

            result["recompiled"] = True

        return result

    async def arun(self, *args, **kwargs) -> Any:
        """Execute wrapped agent through meta layer."""
        # Execute through meta state for tracking
        input_data = {"args": args, "kwargs": kwargs}

        if args and isinstance(args[0], str):
            # Simple string input
            input_data = {"messages": [{"role": "user", "content": args[0]}]}

        # Execute through meta state
        execution_result = self.state.meta_state.execute_agent(
            input_data=input_data, config=kwargs.get("config", {}), update_state=True
        )

        # Update tracking
        self.state.execution_count += 1
        self.state.last_result = execution_result

        # Return the actual output
        return execution_result.get("output", execution_result)

    def run(self, *args, **kwargs) -> Any:
        """Sync version of arun."""
        return asyncio.run(self.arun(*args, **kwargs))

    def update_wrapped_agent(self, new_agent: TAgent) -> None:
        """Update the wrapped agent dynamically."""
        object.__setattr__(self, "_wrapped_agent", new_agent)
        self.state.meta_state.update_agent(new_agent)

    def get_summary(self) -> dict[str, Any]:
        """Get execution and recompilation summary."""
        wrapped = self.wrapped_agent
        return {
            "meta_agent": self.name,
            "wrapped_agent": wrapped.name if wrapped else "None",
            "wrapped_type": type(wrapped).__name__ if wrapped else "None",
            "execution_count": self.state.execution_count,
            "recompilation_count": self.state.recompilation_count,
            "needs_recompilation": self.needs_recompilation(),
            "meta_state_summary": self.state.meta_state.get_execution_summary(),
        }

    @classmethod
    def wrap(cls, agent: TAgent, **kwargs) -> "MetaAgent[TAgent]":
        """Factory method to wrap any agent with meta capabilities.

        Args:
            agent: The agent to wrap
            **kwargs: Additional arguments for MetaAgent

        Returns:
            MetaAgent wrapping the provided agent
        """
        return cls(wrapped_agent=agent, **kwargs)

    def __repr__(self) -> str:
        """String representation."""
        wrapped = self.wrapped_agent
        wrapped_info = (
            f"{type(wrapped).__name__}({wrapped.name})" if wrapped else "None"
        )
        return f"MetaAgent[{wrapped_info}](name={
            self.name}, executions={
            self.state.execution_count})"
