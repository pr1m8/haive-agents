# tests/simple/test_enhanced_simple_agent.py

"""Test the enhanced SimpleAgent with engine-focused generics.

This test demonstrates that SimpleAgent is now essentially Agent[AugLLMConfig]
with proper type safety and clean design.
"""

import asyncio
from typing import Any

import pytest
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.tools import tool

from haive.agents.simple.enhanced_simple_agent import (
    EnhancedSimpleAgent,
    create_simple_agent,
)


class TestEnhancedSimpleAgent:
    """Test the enhanced SimpleAgent implementation."""

    def test_agent_creation_minimal(self):
        """Test creating agent with minimal config."""
        agent = EnhancedSimpleAgent(name="test_agent")

        # Should have default AugLLMConfig engine
        assert agent.engine is not None
        assert isinstance(agent.engine, AugLLMConfig)
        assert agent.name == "test_agent"

    def test_agent_creation_with_fields(self):
        """Test creating agent with convenience fields."""
        agent = EnhancedSimpleAgent(
            name="configured_agent",
            temperature=0.5,
            max_tokens=100,
            system_message="You are a test assistant",
        )

        # Fields should sync to engine
        assert agent.temperature == 0.5
        assert agent.max_tokens == 100
        assert agent.system_message == "You are a test assistant"

        # Engine should have these values
        assert agent.engine.temperature == 0.5
        assert agent.engine.max_tokens == 100
        assert agent.engine.system_message == "You are a test assistant"

    def test_agent_with_tools(self):
        """Test agent with tools."""

        @tool
        def calculator(expression: str) -> str:
            """Calculate mathematical expressions."""
            return str(eval(expression))

        agent = EnhancedSimpleAgent(name="math_agent", tools=[calculator])

        # Tools should be set
        assert len(agent.tools) == 1
        assert agent.tools[0].name == "calculator"

        # Engine should have tools
        assert len(agent.engine.tools) == 1

    def test_type_safe_engine_access(self):
        """Test type-safe engine access."""
        agent = EnhancedSimpleAgent(name="typed_agent", temperature=0.3)

        # Get typed engine
        aug_config = agent.get_aug_llm_config()
        assert isinstance(aug_config, AugLLMConfig)
        assert aug_config.temperature == 0.3

    def test_factory_function(self):
        """Test the factory function."""
        agent = create_simple_agent(
            name="factory_agent", temperature=0.8, system_message="Created by factory"
        )

        assert isinstance(agent, EnhancedSimpleAgent)
        assert agent.name == "factory_agent"
        assert agent.temperature == 0.8
        assert agent.system_message == "Created by factory"

    def test_update_methods(self):
        """Test update methods maintain sync."""
        agent = EnhancedSimpleAgent(name="update_test")

        # Update temperature
        agent.update_temperature(0.9)
        assert agent.temperature == 0.9
        assert agent.engine.temperature == 0.9

        # Update system message
        agent.update_system_message("New message")
        assert agent.system_message == "New message"
        assert agent.engine.system_message == "New message"

    def test_add_tool_method(self):
        """Test adding tools dynamically."""
        agent = EnhancedSimpleAgent(name="dynamic_tools")

        @tool
        def new_tool(input: str) -> str:
            """A new tool."""
            return f"Processed: {input}"

        # Add tool
        agent.add_tool(new_tool)

        assert len(agent.tools) == 1
        assert len(agent.engine.tools) == 1
        assert agent.tools[0].name == "new_tool"

    def test_graph_building(self):
        """Test graph building for different configurations."""
        # Without tools
        agent1 = EnhancedSimpleAgent(name="no_tools")
        graph1 = agent1.build_graph()
        assert "agent_node" in graph1.nodes
        assert "tool_node" not in graph1.nodes

        # With tools
        @tool
        def dummy_tool() -> str:
            """Dummy tool."""
            return "dummy"

        agent2 = EnhancedSimpleAgent(name="with_tools", tools=[dummy_tool])
        graph2 = agent2.build_graph()
        assert "agent_node" in graph2.nodes
        assert "tool_node" in graph2.nodes

    def test_enhanced_type_hints(self):
        """Test that type hints work correctly with generics."""
        # This test verifies the generic pattern works
        agent: EnhancedSimpleAgent = EnhancedSimpleAgent(name="typed")

        # Engine should be typed as AugLLMConfig
        engine: AugLLMConfig = agent.engine
        assert isinstance(engine, AugLLMConfig)

        # The agent is Agent[AugLLMConfig]
        assert agent.__class__.__name__ == "EnhancedSimpleAgent"

    @pytest.mark.asyncio
    async def test_agent_execution_with_real_llm(self):
        """Test agent execution with real LLM (no mocks)."""
        agent = EnhancedSimpleAgent(
            name="real_test",
            temperature=0.1,
            system_message="You are a helpful assistant. Be concise.",
        )

        # Execute with real LLM
        result = await agent.arun("Say hello in exactly 3 words")

        # Should get a response
        assert result is not None
        assert isinstance(result, str)
        assert len(result) > 0

    @pytest.mark.asyncio
    async def test_agent_with_tools_execution(self):
        """Test agent with tools execution."""

        @tool
        def word_counter(text: str) -> str:
            """Count words in text."""
            count = len(text.split())
            return f"The text contains {count} words"

        agent = EnhancedSimpleAgent(
            name="tool_test", temperature=0.1, tools=[word_counter]
        )

        # Execute with tool usage
        result = await agent.arun("Count the words in: The quick brown fox")

        # Should use the tool
        assert result is not None
        assert "4" in str(result) or "four" in str(result).lower()


# Run tests if executed directly
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
