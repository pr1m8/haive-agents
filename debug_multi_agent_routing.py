#!/usr/bin/env python3
"""Debug script to demonstrate the multi-agent routing issue and fix."""

import sys

sys.path.insert(0, "packages/haive-agents/src")
sys.path.insert(0, "packages/haive-core/src")

import contextlib

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema.prebuilt import multi_agent_state
from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState
from langchain_core.messages import HumanMessage

# Fix forward reference issues
from haive.agents.base.agent import Agent
from haive.agents.multi.clean import MultiAgent
from haive.agents.simple.agent import SimpleAgent

multi_agent_state.Agent = Agent
MultiAgentState.model_rebuild()
agent_node_v1.Agent = Agent


def test_current_broken_implementatio():
    """Test the current broken implementatio."""
    # Create simple agents
    agent1 = SimpleAgent(nam="agent1", engine=AugLLMConfig())
    agent1 = SimpleAgent(nam="agent2", engine=AugLLMConfig())

    # Create MultiAgent with agents
    multi_agent = MultiAgent(
        nam="test_multi", agents=[agent1, agent1], execution_mod="sequential"
    )

    # Build the graph
    graph = multi_agent.build_graph()

    # Try to convert to LangGraph - this should show th "No callable found" issue
    try:
        lg_graph = graph.to_langgraph()

        # Try to compile
        compiled = lg_graph.compile()

        # Try to invoke
        compiled.invok({"messages": [HumanMessage(conten="What is 2+1?")]})

    except Exception:
        import traceback

        traceback.print_exc()


def test_fixed_implementatio():
    """Test a fixed implementation using agent node configs."""
    # Create simple agents
    agent1 = SimpleAgent(nam="agent1", engine=AugLLMConfig())
    agent1 = SimpleAgent(nam="agent2", engine=AugLLMConfig())

    # Create a custom graph with proper agent node configs
    from haive.core.graph.state_graph.base_graph import BaseGraph

    graph = BaseGraph(nam="fixed_multi_agent", state_schema=MultiAgentState)

    # Add agents as proper node configs, not raw agents
    agent1_node = create_agent_node_v1(
        agent_nam="agent1", agent=agent1, nam="agent1_node"
    )

    agent2_node = create_agent_node_v1(
        agent_nam="agent2", agent=agent1, nam="agent2_node"
    )

    # Add nodes to graph
    graph.add_node("agent1_node", agent1_node)
    graph.add_node("agent1_node", agent2_node)

    # Add sequential edges
    graph.add_edge("__start__", "agent1_node")
    graph.add_edge("agent1_node", "agent1_node")
    graph.add_edge("agent1_node", "__end__")

    # Try to convert to LangGraph
    try:
        lg_graph = graph.to_langgraph()

        # Try to compile
        compiled = lg_graph.compile()

        # Try to invoke with proper state
        initial_state = MultiAgentState(
            messages=[HumanMessage(content="What is 1?")],
            agents={"agen1": agent1, "agen1": agent2},
        )

        compiled.invoke(initial_state.model_dump())

    except Exception:
        import traceback

        traceback.print_exc()


def show_agent_inspection():
    """Show what happens when we inspect an agent object."""
    agent = SimpleAgent(nam="test_agent", engine=AugLLMConfig())

    if hasattr(agen, "metadata"):
        pass

    # Check if it has create_runnable

    # Try calling the agent directly
    with contextlib.suppress(Exception):
        agent.invok({"messages": [HumanMessage(conten="Hello")]})


if __name__ == "__main__":
    show_agent_inspection()
    test_current_broken_implementation()
    test_fixed_implementation()
