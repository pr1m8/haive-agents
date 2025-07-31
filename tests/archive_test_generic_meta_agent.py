"""Test generic MetaAgent with real components (no mocks)."""

import asyncio

from langchain_core.tools import tool

from haive.agents.meta import MetaAgent
from haive.agents.react import ReactAgent
from haive.agents.simple import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


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
    # Create a real SimpleAgent
    simple_agent = SimpleAgent(
        name="analyzer",
        engine=AugLLMConfig(
            temperature=0.3, system_message="You are a helpful analyzer."
        ),
    )

    # Wrap with MetaAgent
    meta_simple = MetaAgent.wrap(simple_agent, name="meta_analyzer")

    # Test execution
    async def test_execution():
        result = await meta_simple.arun("What is 2+2?")

        # Get summary
        meta_simple.get_summary()

        return result

    asyncio.run(test_execution())

    return meta_simple


def test_meta_agent_with_react():
    """Test MetaAgent wrapping ReactAgent with tools."""
    # Create ReactAgent with tool
    react_agent = ReactAgent(
        name="thinker", engine=AugLLMConfig(temperature=0.5), tools=[calculator]
    )

    # Wrap with MetaAgent
    meta_react = MetaAgent[ReactAgent](wrapped_agent=react_agent)

    # Test execution with tool use
    async def test_with_tool():
        result = await meta_react.arun("Calculate 15 * 23 for me")

        # Check if needs recompilation
        if meta_react.needs_recompilation():
            meta_react.recompile("Tool usage triggered recompilation")

        return result

    asyncio.run(test_with_tool())

    return meta_react


def test_dynamic_agent_update():
    """Test dynamic agent replacement in MetaAgent."""
    # Start with SimpleAgent
    agent1 = SimpleAgent(
        name="v1", engine=AugLLMConfig(system_message="Version 1 agent")
    )

    meta = MetaAgent.wrap(agent1, name="dynamic_meta")

    # Execute with first agent
    async def test_dynamic():
        # First execution
        result1 = await meta.arun("Hello, who are you?")

        # Create new agent
        agent2 = SimpleAgent(
            name="v2", engine=AugLLMConfig(system_message="Version 2 agent - improved!")
        )

        # Update wrapped agent
        meta.update_wrapped_agent(agent2)

        # Execute with new agent
        result2 = await meta.arun("Hello, who are you now?")

        return result1, result2

    asyncio.run(test_dynamic())

    return meta


def test_recompilation_tracking():
    """Test recompilation tracking in MetaAgent."""

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

        def recompile(self):
            self._needs_recompile = False

    # Create recompilable agent
    agent = RecompilableSimpleAgent(name="recompilable", engine=AugLLMConfig())

    # Wrap with MetaAgent
    meta = MetaAgent.wrap(agent, name="meta_recompilable")

    # Trigger recompilation need
    agent.mark_for_recompile("Configuration changed")

    # Recompile through meta
    meta.recompile("User requested recompilation")

    return meta


def test_nested_meta_agents():
    """Test nesting MetaAgents (meta of meta)."""
    # Create base agent
    base = SimpleAgent(
        name="base", engine=AugLLMConfig(system_message="I am the base agent")
    )

    # First level meta
    meta1 = MetaAgent.wrap(base, name="meta_level_1")

    # Second level meta (meta of meta)
    meta2 = MetaAgent.wrap(meta1, name="meta_level_2")

    # Test execution through layers
    async def test_nested():
        result = await meta2.arun("Hello from nested meta!")

        # Get summaries
        meta2.get_summary()
        meta1.get_summary()

        return result

    asyncio.run(test_nested())

    return meta2


if __name__ == "__main__":

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
