"""Test meta-agent integration using MetaStateSchema with real agents."""

import asyncio
from typing import Any, Dict, Type

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema import StateSchema
from haive.core.schema.prebuilt.meta_state import MetaStateSchema
from pydantic import Field

from haive.agents.base.agent import Agent
from haive.agents.react import ReactAgent
from haive.agents.simple import SimpleAgent


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
    print("\n=== Test: MetaStateSchema with SimpleAgent ===")

    # Create a real agent
    inner_agent = SimpleAgent(name="inner_agent", engine=AugLLMConfig(temperature=0.1))

    # Create meta state with embedded agent
    meta_state = MetaStateSchema(
        agent=inner_agent,
        agent_state={"initialized": True},
        graph_context={"test": "meta_state_basic"},
    )

    # Check initial state
    print(f"Meta state created: {meta_state}")
    print(f"Agent name: {meta_state.agent_name}")
    print(f"Agent type: {meta_state.agent_type}")
    print(f"Needs recompile: {meta_state.needs_recompile}")

    # Execute agent through meta state
    result = meta_state.execute_agent(
        input_data={"messages": [{"role": "user", "content": "Hello!"}]}
    )

    print(f"Execution result: {result['status']}")
    print(f"Execution count: {meta_state.graph_context.get('execution_count', 0)}")

    # Check recompilation
    if meta_state.check_agent_recompilation():
        print("Agent needs recompilation")
        meta_state.mark_for_recompile("Test recompilation")

    return meta_state


def test_simple_meta_agent():
    """Test SimpleAgent with meta capabilities."""
    print("\n=== Test: SimpleMetaAgent with Nested Agent ===")

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

    print(f"Created meta agent: {meta_agent.name}")
    print(
        f"Has meta state: {hasattr(meta_agent, 'state') and meta_agent.state.meta_state is not None}"
    )

    # Run async test
    async def run_test():
        # Process with nested execution
        result = await meta_agent.process_with_nested("Analyze the weather today")

        print(f"Combined execution: {result.get('combined', False)}")
        print(f"Main result available: {'main_result' in result}")
        print(f"Nested result available: {'nested_result' in result}")

        if result.get("combined"):
            print(f"Nested execution count: {meta_agent.state.nested_execution_count}")
            print(
                f"Nested agent status: {meta_agent.state.meta_state.execution_status}"
            )

    # Run the async test
    asyncio.run(run_test())

    return meta_agent


def test_react_agent_with_meta_state():
    """Test ReactAgent with embedded SimpleAgent via MetaStateSchema."""
    print("\n=== Test: ReactAgent with Embedded SimpleAgent ===")

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

    print(f"Created ReactAgent with embedded: {analysis_agent.name}")

    # Test execution
    async def test_execution():
        result = await react_meta.think_then_analyze(
            "What are the key factors in climate change?"
        )

        print(f"Execution method: {result.get('method')}")
        print(f"Has ReAct thinking: {'react_thinking' in result}")
        print(f"Has deep analysis: {'deep_analysis' in result}")

        if "deep_analysis" in result:
            print(f"Analysis status: {result['deep_analysis'].get('status')}")

    asyncio.run(test_execution())

    return react_meta


def test_agent_class_method_meta_creation():
    """Test creating meta-capable agents via class methods."""
    print("\n=== Test: Agent Class Method for Meta Creation ===")

    # Add class method to Agent base class for meta creation
    def create_as_meta(cls: Type[Agent], embedded_agent: Agent, **kwargs) -> Agent:
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

    print(f"Created SimpleAgent with meta: {hasattr(meta_simple.state, 'meta_state')}")
    print(f"Created ReactAgent with meta: {hasattr(meta_react.state, 'meta_state')}")

    # Test execution through meta state
    if hasattr(meta_simple.state, "meta_state"):
        result = meta_simple.state.meta_state.execute_agent(
            {"messages": [{"role": "user", "content": "Test"}]}
        )
        print(f"Embedded execution status: {result['status']}")
        meta_simple.state.meta_execution_count += 1
        print(f"Meta execution count: {meta_simple.state.meta_execution_count}")

    return meta_simple, meta_react


if __name__ == "__main__":
    print("🧪 Testing Meta-Agent Integration with Real Components")
    print("=" * 60)

    # Test 1: Basic MetaStateSchema with SimpleAgent
    meta_state = test_meta_state_with_simple_agent()
    print(f"\n✅ MetaStateSchema test complete")

    # Test 2: SimpleMetaAgent with nested composition
    simple_meta = test_simple_meta_agent()
    print(f"\n✅ SimpleMetaAgent test complete")

    # Test 3: ReactAgent with embedded SimpleAgent
    react_meta = test_react_agent_with_meta_state()
    print(f"\n✅ ReactAgent with meta test complete")

    # Test 4: Class method for meta creation
    meta_agents = test_agent_class_method_meta_creation()
    print(f"\n✅ Class method meta creation test complete")

    print("\n🎉 All meta-agent integration tests completed!")
    print("\nKey Patterns Demonstrated:")
    print("1. MetaStateSchema embeds agents in state for graph composition")
    print("2. Agents can have meta_state field for nested agent execution")
    print("3. Class methods can create meta-capable versions of any agent")
    print("4. Recompilation tracking works through MetaStateSchema")
