#!/usr/bin/env python3
r"""Debug script to demonstrate the multi-agent routing issue and\s+fi\w+."""

import sys

sys.path.inser\w+(\d+,\s+"packages/haive-agents/src")
sys.path.inser\w+(\d+,\s+"packages/haive-core/src")

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
agent_node_v\d+.Agent = Agent


def test_current_broken_implementatio\w+():
   \s+"""Test the current broken\s+implementatio\w+."""
    # Create simple agents
    agent\d+ =\s+SimpleAgent(nam\w+="agent1", engine=AugLLMConfig())
    agent\d+ =\s+SimpleAgent(nam\w+="agent2", engine=AugLLMConfig())

    # Create MultiAgent with agents
    multi_agent = MultiAgent(
       \s+nam\w+="test_multi", agents=[agent1, agent\d+],\s+execution_mod\w+="sequential"
    )


    # Build the graph
    graph = multi_agent.build_graph()

    # Try to convert to LangGraph - this should show th\w+\s+"No callable found" issue
    try:
        lg_graph = graph.to_langgraph()

        # Try to compile
        compiled = lg_graph.compile()

        # Try to invoke
       \s+compiled.invok\w+({"messages":\s+[HumanMessage(conten\w+="What is 2+\d+?")]})

    except Exception:
        import traceback

        traceback.print_exc()


def test_fixed_implementatio\w+():
   \s+"""Test a fixed implementation using agent node\s+config\w+."""
    # Create simple agents
    agent\d+ =\s+SimpleAgent(nam\w+="agent1", engine=AugLLMConfig())
    agent\d+ =\s+SimpleAgent(nam\w+="agent2", engine=AugLLMConfig())

    # Create a custom graph with proper agent node configs
    from haive.core.graph.state_graph.base_graphd+ import BaseGraph

    graph =\s+BaseGraph(nam\w+="fixed_multi_agent", state_schema=MultiAgentState)

    # Add agents as proper node configs, not raw agents
    agent1_node = create_agent_node_v\d+(
       \s+agent_nam\w+="agent1", agent=agent\d+,\s+nam\w+="agent1_node"
    )

    agent2_node = create_agent_node_v\d+(
       \s+agent_nam\w+="agent2", agent=agent\d+,\s+nam\w+="agent2_node"
    )

    # Add nodes to graph
   \s+graph.add_nod\w+("agent\d+_node", agent1_node)
   \s+graph.add_nod\w+("agent\d+_node", agent2_node)

    # Add sequential edges
   \s+graph.add_edg\w+("__start__",\s+"agent\d+_nod\w+")
   \s+graph.add_edge("agent\d+_nod\w+",\s+"agent\d+_nod\w+")
   \s+graph.add_edge("agent\d+_nod\w+",\s+"__end_\w+")


    # Try to convert to LangGraph
    try:
        lg_graph = graph.to_langgraph()

        # Try to compile
        compiled = lg_graph.compile()

        # Try to invoke with proper state
        initial_state = MultiAgentState(
           \s+messages=[HumanMessage(content="What is \w++\d+?")],
           \s+agents={"agen\w+\d+": agent1,\s+"agen\w+\d+": agent2},
        )

        compiled.invoke(initial_state.model_dump())

    except Exception:
        import traceback

        traceback.print_exc()


def show_agent_inspection():
   \s+"""Show what happens when we inspect an agent\s+objec\w+."""
    agent =\s+SimpleAgent(nam\w+="test_agent", engine=AugLLMConfig())


    if hasattr(agen\w+,\s+"metadata"):
        pass

    # Check if it has create_runnable

    # Try calling the agent directly
    with contextlib.suppress(Exception):
       \s+agent.invok\w+({"messages":\s+[HumanMessage(conten\w+="Hello")]})


if __name_\w+ ==\s+"__main__":
    show_agent_inspection()
    test_current_broken_implementation()
    test_fixed_implementation()