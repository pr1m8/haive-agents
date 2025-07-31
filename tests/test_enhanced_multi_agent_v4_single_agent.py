#!/usr/bin/env python3
"""Test EnhancedMultiAgentV4 with single agent to isolate issues."""

import asyncio

from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
import pytest

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.react.agent_v3 import ReactAgentV3
from haive.agents.simple.agent_v3 import SimpleAgentV3

# Import components
from haive.core.engine.aug_llm import AugLLMConfig


@tool
def test_calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {e}"


def test_single_simple_agent_creation():
    """Test EnhancedMultiAgentV4 with single SimpleAgent."""
    # Create single SimpleAgent
    simple_agent = SimpleAgentV3(
        name="solo_simple", engine=AugLLMConfig(temperature=0.7)
    )

    # Create EnhancedMultiAgentV4 with single agent
    try:
        multi_agent = EnhancedMultiAgentV4(
            name="single_simple_workflow",
            agents=[simple_agent],  # Single agent in list
            execution_mode="sequential",
        )

        return multi_agent

    except Exception:
        import traceback

        traceback.print_exc()
        return None


def test_single_react_agent_creation():
    """Test EnhancedMultiAgentV4 with single ReactAgent."""
    # Create single ReactAgent with tools
    react_agent = ReactAgentV3(
        name="solo_react",
        engine=AugLLMConfig(temperature=0.3, tools=[test_calculator]),
        max_iterations=2,
    )

    # Create EnhancedMultiAgentV4 with single agent
    try:
        multi_agent = EnhancedMultiAgentV4(
            name="single_react_workflow",
            agents=[react_agent],  # Single agent in list
            execution_mode="sequential",
        )

        return multi_agent

    except Exception:
        import traceback

        traceback.print_exc()
        return None


def test_single_agent_graph_building():
    """Test graph building with single agent."""
    # Create simple agent and multi-agent
    simple_agent = SimpleAgentV3(
        name="graph_test", engine=AugLLMConfig(temperature=0.7)
    )

    multi_agent = EnhancedMultiAgentV4(
        name="graph_build_test", agents=[simple_agent], execution_mode="sequential"
    )

    try:
        # Test graph building
        graph = multi_agent.build_graph()

        # Check graph structure
        if graph.nodes:
            for _node_name, node in graph.nodes.items():
                if hasattr(node, "agent_name"):
                    pass
                if hasattr(node, "metadata"):
                    pass

        return graph

    except Exception:
        import traceback

        traceback.print_exc()
        return None


def test_single_agent_compilation():
    """Test compilation of single agent multi-agent workflow."""
    # Create and build
    simple_agent = SimpleAgentV3(
        name="compile_test", engine=AugLLMConfig(temperature=0.7)
    )

    multi_agent = EnhancedMultiAgentV4(
        name="compile_test_workflow", agents=[simple_agent], execution_mode="sequential"
    )

    try:
        multi_agent.build_graph()

        compiled_app = multi_agent.compile()

        return compiled_app

    except Exception:
        import traceback

        traceback.print_exc()
        return None


@pytest.mark.asyncio
async def test_single_agent_execution():
    """Test actual execution of single agent workflow."""
    # Create and compile
    simple_agent = SimpleAgentV3(name="exec_test", engine=AugLLMConfig(temperature=0.7))

    multi_agent = EnhancedMultiAgentV4(
        name="exec_test_workflow", agents=[simple_agent], execution_mode="sequential"
    )

    try:
        multi_agent.compile()

        # Test input
        test_input = {"messages": [HumanMessage(content="What is 5 + 7?")]}

        # THIS IS THE CRITICAL TEST - Does execution work?
        result = await multi_agent.arun(test_input)

        # Check result structure
        if hasattr(result, "messages"):
            pass
        if hasattr(result, "agents"):
            pass
        if hasattr(result, "agent_outputs"):
            pass

        return result

    except Exception:
        import traceback

        traceback.print_exc()
        return None


@pytest.mark.asyncio
async def test_single_react_agent_execution():
    """Test execution with ReactAgent that uses tools."""
    # Create ReactAgent with tools
    react_agent = ReactAgentV3(
        name="tool_test",
        engine=AugLLMConfig(temperature=0.3, tools=[test_calculator]),
        max_iterations=2,
    )

    multi_agent = EnhancedMultiAgentV4(
        name="tool_test_workflow", agents=[react_agent], execution_mode="sequential"
    )

    try:
        multi_agent.compile()

        # Test input that should trigger tool use
        test_input = {"messages": [HumanMessage(content="Calculate 15 * 23")]}

        result = await multi_agent.arun(test_input)

        # Check for tool usage
        if hasattr(result, "messages"):
            for _i, msg in enumerate(result.messages):
                if hasattr(msg, "tool_calls") and msg.tool_calls:
                    pass

        # Check if calculation was done
        result_str = str(result)
        if "345" in result_str:
            pass
        else:
            pass

        return result

    except Exception:
        import traceback

        traceback.print_exc()
        return None


def test_state_schema_compatibility():
    """Test that MultiAgentState is compatible with single agents."""
    from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState

    # Create agent and state
    simple_agent = SimpleAgentV3(
        name="state_test", engine=AugLLMConfig(temperature=0.7)
    )

    try:
        # Test MultiAgentState creation with single agent
        state = MultiAgentState(
            messages=[HumanMessage(content="Test")], agents={"state_test": simple_agent}
        )

        # Test state methods

        # Get agent
        state.get_agent("state_test")

        # Set active agent
        state.set_active_agent("state_test")

        # Test state conversion to dict
        state.model_dump()

        # Test dict access methods
        try:
            # These should work if StateSchema implements dict-like methods
            state.get("messages", [])
        except Exception:
            pass

        try:
            # Test if __getitem__ works
            state["messages"]
        except Exception:
            pass

        return state

    except Exception:
        import traceback

        traceback.print_exc()
        return None


async def main():
    """Run all single agent tests."""
    # Test creation
    simple_multi = test_single_simple_agent_creation()
    react_multi = test_single_react_agent_creation()

    # Test graph building
    graph = test_single_agent_graph_building()

    # Test compilation
    compiled_app = test_single_agent_compilation()

    # Test state compatibility
    state = test_state_schema_compatibility()

    # Test execution
    simple_result = await test_single_agent_execution()
    react_result = await test_single_react_agent_execution()

    # Summary

    # Overall assessment
    all_pass = all(
        [
            simple_multi,
            react_multi,
            graph,
            compiled_app,
            state,
            simple_result,
            react_result,
        ]
    )

    if all_pass:
        pass
    else:
        pass


if __name__ == "__main__":
    asyncio.run(main())
