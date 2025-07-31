#!/usr/bin/env python3
r"""Debug script to demonstrate the multi-agent routing issue and fix."""

import sys

sys.path.insert(0, "packages/haive-agents/src")
sys.path.insert(0, "packages/haive-core/src")

import contextlib

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.node import agent_node_v3
from haive.core.graph.node.agent_node_v3 import create_agent_node_v3
from haive.core.schema.prebuilt import multi_agent_state
from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState
from langchain_core.messages import HumanMessage

# Fix forward reference issues
from haive.agents.base.agent import Agent
from haive.agents.multi.clean import MultiAgent
from haive.agents.simple.agent import SimpleAgent

multi_agent_state.Agent = Agent
MultiAgentState.model_rebuild()
agent_node_v2.Agent = Agent


def test_current_broken_implementation():
    """Test the current broken implementation."""
    # Create simple agents
    agent1 = SimpleAgent(name="agent1", engine=AugLLMConfig())
    agent2 = SimpleAgent(name="agent2", engine=AugLLMConfig())

    # Create MultiAgent with agents
    multi_agent = MultiAgent(
        name="test_multi", agents=[agent1, agent2], execution_mode="sequential"
    )

    # Build the graph
    graph = multi_agent.build_graph()

    # Try to convert to LangGraph - this should show th\w+\s+"No callable found" issue
    try:
        lg_graph = graph.to_langgraph()

        # Try to compile
        compiled = lg_graph.compile()

        # Try to invoke
        compiled.invoke({"messages": [HumanMessage(content="What is 2+2?")]})

    except Exception:
        import traceback

        traceback.print_exc()


def test_fixed_implementation():
    """Test a fixed implementation using agent node config."""
    # Create simple agents
    agent1 = SimpleAgent(name="agent1", engine=AugLLMConfig())
    agent2 = SimpleAgent(name="agent2", engine=AugLLMConfig())

    # Create a custom graph with proper agent node configs
    from haive.core.graph.state_graph.base_graph import BaseGraph

    graph = BaseGraph(name="fixed_multi_agent", state_schema=MultiAgentState)

    # Add agents as proper node configs, not raw agents
    agent1_node = create_agent_node_v3(
        agent_name="agent1", agent=agent1, name="agent1_node"
    )

    agent2_node = create_agent_node_v3(
        agent_name="agent2", agent=agent2, name="agent2_node"
    )

    # Add nodes to graph
    graph.add_node("agent1_node", agent1_node)
    graph.add_node("agent2_node", agent2_node)

    # Add sequential edges
    graph.add_edge("__start__", "agent1_node")
    graph.add_edge("agent1_node", "agent2_node")
    graph.add_edge("agent2_node", "__end__")

    # Try to convert to LangGraph
    try:
        lg_graph = graph.to_langgraph()

        # Try to compile
        compiled = lg_graph.compile()

        # Try to invoke with proper state
        initial_state = MultiAgentState(
            messages=[HumanMessage(content="What is 2+2?")],
            agents={"agent1": agent1, "agent2": agent2},
        )

        compiled.invoke(initial_state.model_dump())

    except Exception:
        import traceback

        traceback.print_exc()


def show_agent_inspection():
    """Show what happens when we inspect an agent object."""
    agent = SimpleAgent(name="test_agent", engine=AugLLMConfig())

    if hasattr(agent, "metadata"):
        pass

    # Check if it has create_runnable

    # Try calling the agent directly
    with contextlib.suppress(Exception):
        agent.invoke({"messages": [HumanMessage(content="Hello")]})


if __name__ == "__main__":
    show_agent_inspection()
    test_current_broken_implementation()
    test_fixed_implementation()
