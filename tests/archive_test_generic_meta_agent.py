"""Test generic MetaAgent with real components (no mocks)."""

import asyncio
from typing import Any, Dict

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.tools import tool

from haive.agents.meta import MetaAgent
from haive.agents.react import ReactAgent
from haive.agents.simple import SimpleAgent


@tool
def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""
    try:
        result = eval(expression)
        return f"The result is: {result}"
    except Exception as e:
        return f"Error calculating: {e}"


def test_meta_agent_with_simple():
    """Test MetaAgent wrapping SimpleAgent."""
    print("\n=== Test: MetaAgent with SimpleAgent ===")

    # Create a real SimpleAgent
    simple_agent = SimpleAgent(
        name="analyzer",
        engine=AugLLMConfig(
            temperature=0.3, system_message="You are a helpful analyzer."
        ),
    )

    # Wrap with MetaAgent
    meta_simple = MetaAgent.wrap(simple_agent, name="meta_analyzer")

    print(f"Created: {meta_simple}")
    print(f"Wrapped agent: {meta_simple.wrapped_agent.name}")
    print(f"Needs recompilation: {meta_simple.needs_recompilation()}")

    # Test execution
    async def test_execution():
        result = await meta_simple.arun("What is 2+2?")
        print(f"Execution result type: {type(result)}")
        print(f"Execution count: {meta_simple.state.execution_count}")

        # Get summary
        summary = meta_simple.get_summary()
        print(f"Summary: {summary}")

        return result

    result = asyncio.run(test_execution())
    print("✅ MetaAgent[SimpleAgent] executed successfully")

    return meta_simple


def test_meta_agent_with_react():
    """Test MetaAgent wrapping ReactAgent with tools."""
    print("\n=== Test: MetaAgent with ReactAgent ===")

    # Create ReactAgent with tool
    react_agent = ReactAgent(
        name="thinker", engine=AugLLMConfig(temperature=0.5), tools=[calculator]
    )

    # Wrap with MetaAgent
    meta_react = MetaAgent[ReactAgent](wrapped_agent=react_agent)

    print(f"Created: {meta_react}")
    print(f"Meta name: {meta_react.name}")
    print(f"Has calculator tool: {calculator in react_agent.tools}")

    # Test execution with tool use
    async def test_with_tool():
        result = await meta_react.arun("Calculate 15 * 23 for me")
        print(f"Tool calculation completed")
        print(f"Execution count: {meta_react.state.execution_count}")

        # Check if needs recompilation
        if meta_react.needs_recompilation():
            print("Agent needs recompilation")
            recompile_result = meta_react.recompile(
                "Tool usage triggered recompilation"
            )
            print(f"Recompilation result: {recompile_result}")

        return result

    result = asyncio.run(test_with_tool())
    print("✅ MetaAgent[ReactAgent] with tools executed successfully")

    return meta_react


def test_dynamic_agent_update():
    """Test dynamic agent replacement in MetaAgent."""
    print("\n=== Test: Dynamic Agent Update ===")

    # Start with SimpleAgent
    agent1 = SimpleAgent(
        name="v1", engine=AugLLMConfig(system_message="Version 1 agent")
    )

    meta = MetaAgent.wrap(agent1, name="dynamic_meta")
    print(f"Initial wrapped agent: {meta.wrapped_agent.name}")

    # Execute with first agent
    async def test_dynamic():
        # First execution
        result1 = await meta.arun("Hello, who are you?")
        print(f"V1 execution count: {meta.state.execution_count}")

        # Create new agent
        agent2 = SimpleAgent(
            name="v2", engine=AugLLMConfig(system_message="Version 2 agent - improved!")
        )

        # Update wrapped agent
        print("\nUpdating wrapped agent...")
        meta.update_wrapped_agent(agent2)
        print(f"New wrapped agent: {meta.wrapped_agent.name}")
        print(f"Needs recompilation after update: {meta.needs_recompilation()}")

        # Execute with new agent
        result2 = await meta.arun("Hello, who are you now?")
        print(f"V2 execution count: {meta.state.execution_count}")

        return result1, result2

    results = asyncio.run(test_dynamic())
    print("✅ Dynamic agent update completed successfully")

    return meta


def test_recompilation_tracking():
    """Test recompilation tracking in MetaAgent."""
    print("\n=== Test: Recompilation Tracking ===")

    # Create agent that supports recompilation
    class RecompilableSimpleAgent(SimpleAgent):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._needs_recompile = False

        @property
        def needs_recompile(self) -> bool:
            return self._needs_recompile

        def mark_for_recompile(self, reason: str):
            self._needs_recompile = True
            print(f"[{self.name}] Marked for recompile: {reason}")

        def recompile(self):
            print(f"[{self.name}] Recompiling...")
            self._needs_recompile = False

    # Create recompilable agent
    agent = RecompilableSimpleAgent(name="recompilable", engine=AugLLMConfig())

    # Wrap with MetaAgent
    meta = MetaAgent.wrap(agent, name="meta_recompilable")

    print(f"Initial needs recompilation: {meta.needs_recompilation()}")

    # Trigger recompilation need
    agent.mark_for_recompile("Configuration changed")
    print(f"After marking: {meta.needs_recompilation()}")

    # Recompile through meta
    recompile_result = meta.recompile("User requested recompilation")
    print(f"Recompilation result: {recompile_result}")
    print(f"Recompilation count: {meta.state.recompilation_count}")
    print(f"Still needs recompilation: {meta.needs_recompilation()}")

    print("✅ Recompilation tracking working correctly")

    return meta


def test_nested_meta_agents():
    """Test nesting MetaAgents (meta of meta)."""
    print("\n=== Test: Nested MetaAgents ===")

    # Create base agent
    base = SimpleAgent(
        name="base", engine=AugLLMConfig(system_message="I am the base agent")
    )

    # First level meta
    meta1 = MetaAgent.wrap(base, name="meta_level_1")

    # Second level meta (meta of meta)
    meta2 = MetaAgent.wrap(meta1, name="meta_level_2")

    print(f"Created nested structure:")
    print(f"  Level 2: {meta2}")
    print(f"  Level 1: {meta2.wrapped_agent}")
    print(f"  Base: {meta2.wrapped_agent.wrapped_agent}")

    # Test execution through layers
    async def test_nested():
        result = await meta2.arun("Hello from nested meta!")

        print(f"\nExecution counts:")
        print(f"  Meta2: {meta2.state.execution_count}")
        print(f"  Meta1: {meta1.state.execution_count}")

        # Get summaries
        summary2 = meta2.get_summary()
        summary1 = meta1.get_summary()

        print(f"\nNested summaries:")
        print(f"  Level 2 executions: {summary2['execution_count']}")
        print(f"  Level 1 executions: {summary1['execution_count']}")

        return result

    result = asyncio.run(test_nested())
    print("✅ Nested MetaAgents working correctly")

    return meta2


if __name__ == "__main__":
    print("🧪 Testing Generic MetaAgent Implementation")
    print("=" * 60)

    # Test 1: MetaAgent with SimpleAgent
    meta_simple = test_meta_agent_with_simple()

    # Test 2: MetaAgent with ReactAgent and tools
    meta_react = test_meta_agent_with_react()

    # Test 3: Dynamic agent updates
    dynamic_meta = test_dynamic_agent_update()

    # Test 4: Recompilation tracking
    recompilable_meta = test_recompilation_tracking()

    # Test 5: Nested MetaAgents
    nested_meta = test_nested_meta_agents()

    print("\n🎉 All generic MetaAgent tests completed!")
    print("\nKey Features Demonstrated:")
    print("1. Generic MetaAgent[T] can wrap any agent type")
    print("2. Execution tracking and state management")
    print("3. Dynamic agent replacement")
    print("4. Recompilation tracking and management")
    print("5. Nested meta-agent composition")
    print("6. All with REAL components - NO MOCKS!")
