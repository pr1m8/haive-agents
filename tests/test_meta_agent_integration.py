"""Test meta-agent integration using MetaStateSchema with real agents."""

import asyncio
from typing import Any

from pydantic import Field

from haive.agents.base.agent import Agent
from haive.agents.react import ReactAgent
from haive.agents.simple import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema import StateSchema
from haive.core.schema.prebuilt.meta_state import MetaStateSchema


class MetaCapableAgentState(StateSchema):
    """State for agents with meta capabilities."""

    # Standard agent state
    messages: list[dict[str, Any]] = Field(default_factory=list)

    # Meta-agent specific fields
    meta_state: MetaStateSchema | None = Field(
        default=None, description="Embedded meta state for nested agent composition"
    )

    # Track nested executions
    nested_execution_count: int = Field(default=0)
    last_nested_result: dict[str, Any] | None = Field(default=None)


class MetaCapableAgent(Agent):
    """Base class for agents with meta capabilities.

    This demonstrates how to integrate MetaStateSchema into agents
    to enable nested agent composition and recompilation tracking.
    """

    def __init__(self, *args, **kwargs):
        # Extract meta_agent if provided
        self._meta_agent = kwargs.pop("meta_agent", None)
        # Force state schema
        kwargs["state_schema"] = MetaCapableAgentState
        super().__init__(*args, **kwargs)

    def setup_agent(self) -> None:
        """Setup agent with meta capabilities."""
        super().setup_agent()

        # If we have a meta_agent, create MetaStateSchema for it
        if self._meta_agent:
            self.state.meta_state = MetaStateSchema.from_agent(
                agent=self._meta_agent,
                initial_state={"parent_agent": self.name},
                graph_context={"composition_type": "embedded"},
            )

    async def execute_nested_agent(self, input_data: dict[str, Any]) -> dict[str, Any]:
        """Execute the nested agent through MetaStateSchema."""
        if not self.state.meta_state or not self.state.meta_state.agent:
            raise ValueError("No nested agent configured")

        # Execute through meta state
        result = self.state.meta_state.execute_agent(
            input_data=input_data, config={"parent_agent": self.name}, update_state=True
        )

        # Update our state
        self.state.nested_execution_count += 1
        self.state.last_nested_result = result

        return result

    def check_nested_recompilation(self) -> bool:
        """Check if nested agent needs recompilation."""
        if self.state.meta_state:
            return self.state.meta_state.check_agent_recompilation()
        return False

    @classmethod
    def with_meta_agent(
        cls, name: str, engine: AugLLMConfig, meta_agent: Agent, **kwargs
    ) -> "MetaCapableAgent":
        """Factory method to create agent with embedded meta capabilities."""
        return cls(
            name=name,
            engine=engine,
            meta_agent=meta_agent,
            state_schema=MetaCapableAgentState,
            **kwargs,
        )


class SimpleMetaAgent(SimpleAgent):
    """SimpleAgent with meta capabilities."""

    def __init__(self, *args, **kwargs):
        # Extract meta_agent if provided
        self._meta_agent = kwargs.pop("meta_agent", None)

        # Force state schema to MetaCapableAgentState
        kwargs["state_schema"] = MetaCapableAgentState

        super().__init__(*args, **kwargs)

    def setup_agent(self) -> None:
        """Setup with meta capabilities."""
        super().setup_agent()

        # Initialize meta state if we have a nested agent
        if self._meta_agent and hasattr(self, "state"):
            self.state.meta_state = MetaStateSchema.from_agent(
                agent=self._meta_agent,
                initial_state={"parent_agent": self.name},
                graph_context={
                    "composition_type": "simple_meta",
                    "parent_type": "SimpleAgent",
                },
            )

    async def process_with_nested(self, user_input: str) -> dict[str, Any]:
        """Process input using both main and nested agents."""
        # First process with main agent
        main_result = await self.arun(user_input)

        # Then process with nested agent if available
        if hasattr(self, "state") and self.state.meta_state:
            nested_input = {
                "messages": [{"role": "user", "content": user_input}],
                "context": {"main_result": main_result},
            }

            nested_result = self.state.meta_state.execute_agent(
                input_data=nested_input, update_state=True
            )

            # Update tracking
            self.state.nested_execution_count += 1
            self.state.last_nested_result = nested_result

            return {
                "main_result": main_result,
                "nested_result": nested_result,
                "combined": True,
            }

        return {"main_result": main_result, "combined": False}

    @classmethod
    def create_with_nested_agent(
        cls,
        name: str,
        nested_agent: Agent,
        engine: AugLLMConfig | None = None,
        **kwargs,
    ) -> "SimpleMetaAgent":
        """Create SimpleAgent with nested agent composition."""
        if engine is None:
            engine = AugLLMConfig()

        return cls(name=name, engine=engine, meta_agent=nested_agent, **kwargs)


def test_meta_state_with_simple_agent():
    """Test MetaStateSchema with a real SimpleAgent."""
    # Create a real agent
    inner_agent = SimpleAgent(name="inner_agent", engine=AugLLMConfig(temperature=0.1))

    # Create meta state with embedded agent
    meta_state = MetaStateSchema(
        agent=inner_agent,
        agent_state={"initialized": True},
        graph_context={"test": "meta_state_basic"},
    )

    # Check initial state

    # Execute agent through meta state
    meta_state.execute_agent(
        input_data={"messages": [{"role": "user", "content": "Hello!"}]}
    )

    # Check recompilation
    if meta_state.check_agent_recompilation():
        meta_state.mark_for_recompile("Test recompilation")

    return meta_state


def test_simple_meta_agent():
    """Test SimpleAgent with meta capabilities."""
    # Create nested agent
    nested_agent = SimpleAgent(
        name="analyzer",
        engine=AugLLMConfig(
            system_message="You are an analysis expert.", temperature=0.3
        ),
    )

    # Create meta-capable simple agent
    meta_agent = SimpleMetaAgent.create_with_nested_agent(
        name="coordinator",
        nested_agent=nested_agent,
        engine=AugLLMConfig(
            system_message="You are a coordination agent.", temperature=0.5
        ),
    )

    # Run async test
    async def run_test():
        # Process with nested execution
        result = await meta_agent.process_with_nested("Analyze the weather today")

        if result.get("combined"):
            pass

    # Run the async test
    asyncio.run(run_test())

    return meta_agent


def test_react_agent_with_meta_state():
    """Test ReactAgent with embedded SimpleAgent via MetaStateSchema."""
    # Create an analysis agent to embed
    analysis_agent = SimpleAgent(
        name="analyzer",
        engine=AugLLMConfig(
            system_message="You analyze data and provide insights.", temperature=0.2
        ),
    )

    # Create custom ReactAgent with meta capabilities
    class MetaReactAgent(ReactAgent):
        def __init__(self, *args, **kwargs):
            self._embedded_agent = kwargs.pop("embedded_agent", None)
            super().__init__(*args, **kwargs)

            # Add meta state after initialization
            if self._embedded_agent and hasattr(self, "state"):
                # Create a meta field in the state
                self.state.__dict__["meta_state"] = MetaStateSchema.from_agent(
                    agent=self._embedded_agent,
                    initial_state={"parent": self.name},
                    graph_context={"embedded_in": "ReactAgent"},
                )

        async def think_then_analyze(self, query: str) -> dict[str, Any]:
            """Use ReAct for planning, then embedded agent for analysis."""
            # First, use ReAct thinking
            react_result = await self.arun(query)

            # Then use embedded agent for deeper analysis
            if hasattr(self, "state") and hasattr(self.state, "meta_state"):
                analysis_input = {
                    "messages": [
                        {"role": "system", "content": "Analyze the following:"},
                        {
                            "role": "user",
                            "content": f"Query: {query}\nInitial thoughts: {react_result}",
                        },
                    ]
                }

                analysis = self.state.meta_state.execute_agent(analysis_input)

                return {
                    "react_thinking": react_result,
                    "deep_analysis": analysis,
                    "method": "think_then_analyze",
                }

            return {"react_thinking": react_result, "method": "react_only"}

    # Create the meta-capable ReactAgent
    react_meta = MetaReactAgent(
        name="thinker",
        engine=AugLLMConfig(temperature=0.7),
        embedded_agent=analysis_agent,
    )

    # Test execution
    async def test_execution():
        result = await react_meta.think_then_analyze(
            "What are the key factors in climate change?"
        )

        if "deep_analysis" in result:
            pass

    asyncio.run(test_execution())

    return react_meta


def test_agent_class_method_meta_creation():
    """Test creating meta-capable agents via class methods."""

    # Add class method to Agent base class for meta creation
    def create_as_meta(cls: type[Agent], embedded_agent: Agent, **kwargs) -> Agent:
        """Create this agent type with an embedded agent."""

        # Custom state with meta field
        class MetaEnabledState(cls.get_state_schema()):
            meta_state: MetaStateSchema | None = Field(default=None)
            meta_execution_count: int = Field(default=0)

        # Create agent with custom state
        agent = cls(state_schema=MetaEnabledState, **kwargs)

        # Add meta state after creation
        if hasattr(agent, "state"):
            agent.state.meta_state = MetaStateSchema.from_agent(
                agent=embedded_agent,
                initial_state={"created_via": "class_method"},
                graph_context={"parent_class": cls.__name__},
            )

        return agent

    # Monkey patch for demo (in real implementation, add to Agent base class)
    Agent.create_as_meta = classmethod(create_as_meta)

    # Create embedded agent
    embedded = SimpleAgent(
        name="embedded_processor", engine=AugLLMConfig(temperature=0.1)
    )

    # Create meta-capable agents using class method
    meta_simple = SimpleAgent.create_as_meta(
        embedded_agent=embedded,
        name="meta_simple_via_classmethod",
        engine=AugLLMConfig(),
    )

    meta_react = ReactAgent.create_as_meta(
        embedded_agent=embedded,
        name="meta_react_via_classmethod",
        engine=AugLLMConfig(),
    )

    # Test execution through meta state
    if hasattr(meta_simple.state, "meta_state"):
        meta_simple.state.meta_state.execute_agent(
            {"messages": [{"role": "user", "content": "Test"}]}
        )
        meta_simple.state.meta_execution_count += 1

    return meta_simple, meta_react


if __name__ == "__main__":

    # Test 1: Basic MetaStateSchema with SimpleAgent
    meta_state = test_meta_state_with_simple_agent()

    # Test 2: SimpleMetaAgent with nested composition
    simple_meta = test_simple_meta_agent()

    # Test 3: ReactAgent with embedded SimpleAgent
    react_meta = test_react_agent_with_meta_state()

    # Test 4: Class method for meta creation
    meta_agents = test_agent_class_method_meta_creation()
