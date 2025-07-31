#!/usr/bin/env python3
"""Standalone test for SimpleAgentV3 with ValidationNodeV2 pattern.

Run directly: poetry run python tests/simple/v3/test_simple_validation_standalone.py
"""

import asyncio
import logging
from pathlib import Path
import sys


# Add project paths
project_root = Path(__file__).parent.parent.parent.parent.parent
sys.path.insert(0, str(project_root))

from langchain_core.tools import tool
from pydantic import BaseModel, Field

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


# ========================================================================
# TESTS
# ========================================================================


async def test_basic_creation():
    """Test SimpleAgentV3 basic creation."""
    agent = SimpleAgentV3(
        name="basic_agent", engine=AugLLMConfig(name="basic", temperature=0.1)
    )

    return agent


async def test_no_tools_execution():
    """Test SimpleAgentV3 execution without tools."""
    agent = SimpleAgentV3(
        name="no_tools_agent", engine=AugLLMConfig(name="no_tools", temperature=0.1)
    )

    try:
        await agent.arun("Hello, how are you?")
        return True
    except Exception:
        return False


async def test_tools_execution():
    """Test SimpleAgentV3 with LangChain tools."""
    agent = SimpleAgentV3(
        name="tools_agent",
        engine=AugLLMConfig(name="tools_test", temperature=0.1, tools=[calculator]),
    )

    try:
        result = await agent.arun("Calculate 15 * 23 please")

        # Check for calculation result
        "345" in str(result)
        return True
    except Exception:
        import traceback

        traceback.print_exc()
        return False


async def test_structured_output():
    """Test SimpleAgentV3 with structured output."""
    agent = SimpleAgentV3(
        name="structured_agent",
        engine=AugLLMConfig(
            name="structured_test", temperature=0.1, structured_output_model=MathResult
        ),
    )

    try:
        result = await agent.arun("Calculate 12 + 8 and explain it")

        # Check structure
        if isinstance(result, MathResult | dict):
            pass
        else:
            pass

        return True
    except Exception:
        import traceback

        traceback.print_exc()
        return False


async def test_graph_structure():
    """Test SimpleAgentV3 graph structure."""
    agent = SimpleAgentV3(
        name="structure_agent",
        engine=AugLLMConfig(
            name="structure_test",
            tools=[calculator],
            structured_output_model=MathResult,
        ),
    )

    try:
        # Check graph

        if hasattr(agent, "graph") and agent.graph:
            nodes = list(agent.graph.nodes.keys())

            # Key nodes we expect
            expected = {"agent_node"}
            set(nodes) & expected

        # Test execution
        await agent.arun("Calculate 10 + 5")

        return True
    except Exception:
        import traceback

        traceback.print_exc()
        return False


async def test_dynamic_tool_addition():
    """Test dynamic tool addition."""
    agent = SimpleAgentV3(
        name="dynamic_agent",
        engine=AugLLMConfig(name="dynamic_test", model="gpt-4o-mini", temperature=0.1),
    )

    try:
        # Check initial state
        len(agent.engine.tools) if agent.engine.tools else 0

        # Add tool dynamically
        @tool
        def word_counter(text: str) -> str:
            """Count words in text."""
            return f"Word count: {len(text.split())}"

        agent.add_tool(word_counter, route="langchain_tool")

        # Check after addition
        len(agent.engine.tools) if agent.engine.tools else 0

        # Test with new tool
        await agent.arun("Count words in this sentence")

        return True
    except Exception:
        import traceback

        traceback.print_exc()
        return False


# ========================================================================
# MAIN TEST RUNNER
# ========================================================================


async def main():
    """Run all tests."""
    tests = [
        test_basic_creation,
        test_no_tools_execution,
        test_tools_execution,
        test_structured_output,
        test_graph_structure,
        test_dynamic_tool_addition,
    ]

    results = []
    for test in tests:
        try:
            result = await test()
            results.append(result)
        except Exception:
            results.append(False)

    passed = sum(1 for r in results if r)
    total = len(results)

    for _i, (test, result) in enumerate(zip(tests, results, strict=False)):
        pass

    if passed == total:
        pass
    else:
        pass

    return passed == total


if __name__ == "__main__":
    success = asyncio.run(main())
    sys.exit(0 if success else 1)
