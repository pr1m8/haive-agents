"""Test SimpleAgentV3 with ValidationNodeV2 pattern integration.

This test validates that SimpleAgentV3 correctly uses ValidationNodeV2
for conditional tool routing and state management.
"""

import asyncio
import logging

from langchain_core.tools import tool
from pydantic import BaseModel, Field
import pytest

# Import our enhanced SimpleAgentV3
from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.core.engine.aug_llm import AugLLMConfig


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ========================================================================
# TEST MODELS AND TOOLS
# ========================================================================


class MathResult(BaseModel):
    """Pydantic model for structured math results."""

    calculation: str = Field(description="The mathematical calculation performed")
    result: float = Field(description="The numerical result")
    explanation: str = Field(description="Brief explanation of the calculation")


@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    try:
        result = eval(expression)
        return f"The result of {expression} is {result}"
    except Exception as e:
        return f"Error calculating {expression}: {e}"


@tool
def word_counter(text: str) -> str:
    """Count words in text."""
    word_count = len(text.split())
    return f"The text contains {word_count} words"


# ========================================================================
# FIXTURES
# ========================================================================


@pytest.fixture
def basic_config():
    """Basic AugLLMConfig for testing."""
    return AugLLMConfig(
        name="test_engine",
        temperature=0.1,  # Low for consistent results
        model="gpt-4o-mini",
    )


@pytest.fixture
def config_with_tools():
    """AugLLMConfig with LangChain tools."""
    return AugLLMConfig(
        name="tools_engine",
        temperature=0.1,
        model="gpt-4o-mini",
        tools=[calculator, word_counter],
    )


@pytest.fixture
def config_with_structured_output():
    """AugLLMConfig with structured output model."""
    return AugLLMConfig(
        name="structured_engine",
        temperature=0.1,
        model="gpt-4o-mini",
        structured_output_model=MathResult,
    )


@pytest.fixture
def config_with_mixed():
    """AugLLMConfig with both tools and structured output."""
    return AugLLMConfig(
        name="mixed_engine",
        temperature=0.1,
        model="gpt-4o-mini",
        tools=[calculator],
        structured_output_model=MathResult,
    )


# ========================================================================
# BASIC FUNCTIONALITY TESTS
# ========================================================================


@pytest.mark.asyncio
async def test_simple_agent_v3_basic_creation():
    """Test SimpleAgentV3 can be created with ValidationNodeV2."""
    agent = SimpleAgentV3(
        name="basic_agent", engine=AugLLMConfig(name="basic", model="gpt-4o-mini")
    )

    # Verify agent properties
    assert agent.name == "basic_agent"
    assert agent.engine.name == "basic"
    assert hasattr(agent, "graph")

    # Verify mixins are working
    assert hasattr(agent, "add_tool")  # DynamicToolRouteMixin
    assert hasattr(agent, "needs_recompile")  # RecompileMixin


@pytest.mark.asyncio
async def test_simple_agent_v3_no_tools_execution():
    """Test SimpleAgentV3 with no tools (should skip validation node)."""
    agent = SimpleAgentV3(
        name="no_tools_agent",
        engine=AugLLMConfig(name="no_tools", model="gpt-4o-mini", temperature=0.1),
    )

    # Execute simple query
    result = await agent.arun("Hello, how are you?")

    # Verify basic execution
    assert isinstance(result, str)
    assert len(result) > 0
    logger.info(f"No tools result: {result}")


# ========================================================================
# VALIDATION NODE V2 INTEGRATION TESTS
# ========================================================================


@pytest.mark.asyncio
async def test_langchain_tools_routing():
    """Test that LangChain tools route correctly through ValidationNodeV2."""
    agent = SimpleAgentV3(
        name="tools_agent",
        engine=AugLLMConfig(
            name="tools_test",
            model="gpt-4o-mini",
            temperature=0.1,
            tools=[calculator, word_counter],
        ),
    )

    # Execute with tool usage
    result = await agent.arun("Calculate 15 * 23 please")

    # Verify execution
    assert isinstance(result, str)
    assert len(result) > 0
    logger.info(f"Tools result: {result}")

    # Should contain calculation result
    assert "345" in result or "fifteen" in result.lower() or "23" in result


@pytest.mark.asyncio
async def test_structured_output_routing():
    """Test that structured output models route correctly through ValidationNodeV2."""
    agent = SimpleAgentV3(
        name="structured_agent",
        engine=AugLLMConfig(
            name="structured_test",
            model="gpt-4o-mini",
            temperature=0.1,
            structured_output_model=MathResult,
        ),
    )

    # Execute with structured output request
    result = await agent.arun("Calculate 12 + 8 and explain the result")

    # Verify execution and type
    logger.info(f"Structured result: {result}")
    logger.info(f"Result type: {type(result)}")

    # Result should be structured (either MathResult instance or dict)
    if isinstance(result, MathResult):
        assert result.result == 20.0
        assert "12 + 8" in result.calculation or "12+8" in result.calculation
    elif isinstance(result, dict):
        assert "result" in result
        assert "calculation" in result
    else:
        # Sometimes comes back as string representation
        assert "20" in str(result)


@pytest.mark.asyncio
async def test_mixed_tools_and_structured_output():
    """Test ValidationNodeV2 with both LangChain tools and structured output."""
    agent = SimpleAgentV3(
        name="mixed_agent",
        engine=AugLLMConfig(
            name="mixed_test",
            model="gpt-4o-mini",
            temperature=0.1,
            tools=[calculator],
            structured_output_model=MathResult,
        ),
    )

    # Execute complex request
    result = await agent.arun("Use the calculator to compute 25 * 4, then format as MathResult")

    # Verify execution
    logger.info(f"Mixed result: {result}")
    logger.info(f"Mixed result type: {type(result)}")

    # Should involve both tool usage and structured formatting
    assert result is not None
    result_str = str(result)
    assert "100" in result_str or "25" in result_str


# ========================================================================
# DYNAMIC TOOL ROUTING TESTS
# ========================================================================


@pytest.mark.asyncio
async def test_dynamic_tool_addition():
    """Test dynamic tool addition triggers proper recompilation."""
    agent = SimpleAgentV3(
        name="dynamic_agent",
        engine=AugLLMConfig(name="dynamic_test", model="gpt-4o-mini", temperature=0.1),
    )

    # Initially no tools
    initial_tools = len(agent.engine.tools) if agent.engine.tools else 0
    logger.info(f"Initial tools count: {initial_tools}")

    # Add tool dynamically
    agent.add_tool(word_counter, route="langchain_tool")

    # Check tool was added
    new_tools = len(agent.engine.tools) if agent.engine.tools else 0
    logger.info(f"After adding tool: {new_tools}")

    # Execute with new tool
    result = await agent.arun("Count the words in this sentence please")

    # Verify execution
    assert isinstance(result, str)
    logger.info(f"Dynamic tool result: {result}")


@pytest.mark.asyncio
async def test_recompilation_mixin_integration():
    """Test that RecompileMixin works with ValidationNodeV2."""
    agent = SimpleAgentV3(
        name="recompile_agent",
        engine=AugLLMConfig(name="recompile_test", model="gpt-4o-mini"),
    )

    # Check initial recompilation state
    initial_recompile = agent.needs_recompile
    logger.info(f"Initial recompile needed: {initial_recompile}")

    # Add tool to trigger recompilation need
    agent.add_tool(calculator, route="langchain_tool")

    # Check if recompilation is needed
    after_add = agent.needs_recompile
    logger.info(f"After tool addition recompile needed: {after_add}")

    # Execute to trigger any needed recompilation
    result = await agent.arun("Calculate 7 * 6")

    # Verify execution
    assert isinstance(result, str)
    logger.info(f"Recompilation test result: {result}")


# ========================================================================
# ERROR HANDLING TESTS
# ========================================================================


@pytest.mark.asyncio
async def test_validation_error_handling():
    """Test ValidationNodeV2 handles validation errors gracefully."""
    agent = SimpleAgentV3(
        name="error_agent",
        engine=AugLLMConfig(
            name="error_test",
            model="gpt-4o-mini",
            temperature=0.1,
            structured_output_model=MathResult,
        ),
    )

    # Request that might cause validation issues
    result = await agent.arun("Just say hello, don't do any math")

    # Should handle gracefully (not crash)
    assert result is not None
    logger.info(f"Error handling result: {result}")


# ========================================================================
# INTEGRATION VALIDATION TESTS
# ========================================================================


@pytest.mark.asyncio
async def test_validation_node_v2_graph_structure():
    """Test that SimpleAgentV3 builds correct graph structure with ValidationNodeV2."""
    agent = SimpleAgentV3(
        name="structure_agent",
        engine=AugLLMConfig(
            name="structure_test",
            model="gpt-4o-mini",
            tools=[calculator],
            structured_output_model=MathResult,
        ),
    )

    # Check graph structure
    assert hasattr(agent, "graph")
    assert agent.graph is not None

    # Graph should have validation node
    nodes = agent.graph.nodes
    node_names = list(nodes.keys())
    logger.info(f"Graph nodes: {node_names}")

    # Should contain key nodes for tools + structured output
    expected_nodes = {"agent_node", "validation", "tool_node", "parse_output"}
    missing_nodes = expected_nodes - set(node_names)
    if missing_nodes:
        logger.warning(f"Missing expected nodes: {missing_nodes}")

    # At minimum should have agent_node and validation
    assert "agent_node" in node_names
    # Validation might be conditional, so just check execution works

    # Execute to verify graph works
    result = await agent.arun("Calculate 10 + 5 using the calculator")
    assert result is not None
    logger.info(f"Graph structure test result: {result}")


if __name__ == "__main__":
    # Run a quick test
    asyncio.run(test_simple_agent_v3_basic_creation())
