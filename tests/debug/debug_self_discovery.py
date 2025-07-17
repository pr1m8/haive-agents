#!/usr/bin/env python3
"""Debug script for self-discovery agent with breakpoints."""

import pdb
import sys
import traceback

sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")


def debug_agent_structure():
    """Debug the agent structure and setup."""
    print("🔍 DEBUGGING: Agent Structure")

    from haive.agents.reasoning_and_critique.self_discover.v2.agent import (
        self_discovery,
    )

    print(f"✅ Agent: {self_discovery.name}")
    print(f"✅ Type: {type(self_discovery)}")
    print(f"✅ Schema: {self_discovery.state_schema.__name__}")

    # Check if it's a ProperMultiAgent
    from haive.agents.multi.proper_base import ProperMultiAgent

    is_multi_agent = isinstance(self_discovery, ProperMultiAgent)
    print(f"🔍 Is ProperMultiAgent: {is_multi_agent}")

    # Check the agents structure
    print(f"🔍 Agents type: {type(self_discovery.agents)}")
    if isinstance(self_discovery.agents, dict):
        print(f"🔍 Sub-agents: {list(self_discovery.agents.keys())}")
        for name, agent in self_discovery.agents.items():
            print(f"  - {name}: {type(agent)}")

    # Check the graph/app structure
    if hasattr(self_discovery, "_app"):
        print(f"🔍 Has _app: {self_discovery._app is not None}")
        print(f"🔍 App type: {type(self_discovery._app)}")
    else:
        print("❌ No _app found")

    return self_discovery


def debug_input_preparation():
    """Debug input preparation for the agent."""
    print("\n🔍 DEBUGGING: Input Preparation")

    problem = "Lisa has 10 apples. She gives 3 apples to her friend and then buys 5 more apples from the store. How many apples does Lisa have now?"

    # Test different input formats
    print(f"📝 Problem: {problem}")

    # Format 1: Simple string (like the examples)
    input1 = problem
    print(f"🔍 Input format 1 (string): {type(input1)}")

    # Format 2: Dict with task_description
    input2 = {"task_description": problem}
    print(f"🔍 Input format 2 (dict): {input2}")

    # Format 3: Dict with messages (like ProperMultiAgent might expect)
    input3 = {"messages": [], "task_description": problem}
    print(f"🔍 Input format 3 (messages): {input3}")

    # Format 4: Full SelfDiscoveryState dict
    input4 = {
        "messages": [],
        "task_description": problem,
        "reasoning_modules": "",
        "selected_modules": None,
        "adapted_modules": None,
        "reasoning_structure": None,
        "answer": None,
        "error": None,
        "metadata": {},
    }
    print(f"🔍 Input format 4 (full state): keys = {list(input4.keys())}")

    return problem, input1, input2, input3, input4


def debug_with_breakpoints():
    """Run the debugging with strategic breakpoints."""
    print("🚨 STARTING DEBUG SESSION WITH BREAKPOINTS")
    print("=" * 60)

    try:
        # Step 1: Check agent structure
        agent = debug_agent_structure()

        # Step 2: Prepare inputs
        problem, input1, input2, input3, input4 = debug_input_preparation()

        # Step 3: Try to run with different input formats
        print("\n🔍 DEBUGGING: Trying different input formats")

        # Set a breakpoint before execution
        print("\n🔴 BREAKPOINT: About to test input formats")
        pdb.set_trace()  # Breakpoint 1: Before testing inputs

        for i, test_input in enumerate([input2, input3, input4], 1):
            print(f"\n🔄 Testing input format {i + 1}: {type(test_input)}")
            try:
                # Another breakpoint before each run attempt
                print(f"🔴 BREAKPOINT: About to run with input format {i + 1}")
                pdb.set_trace()  # Breakpoint 2: Before each run

                result = agent.run(test_input)
                print(f"✅ SUCCESS with format {i + 1}: {result}")
                break  # If successful, stop testing

            except Exception as e:
                print(f"❌ FAILED with format {i + 1}: {e}")
                print(f"Error type: {type(e)}")

                # Breakpoint on error to examine
                print("🔴 BREAKPOINT: Error occurred, examining...")
                pdb.set_trace()  # Breakpoint 3: On error

                continue

        print("\n🏁 DEBUG SESSION COMPLETED")

    except Exception as e:
        print(f"\n💥 CRITICAL ERROR: {e}")
        print(f"Error type: {type(e)}")
        traceback.print_exc()

        # Final breakpoint for critical errors
        print("🔴 BREAKPOINT: Critical error examination")
        pdb.set_trace()  # Breakpoint 4: Critical error


def debug_graph_structure():
    """Debug the internal graph structure that's causing the error."""
    print("\n🔍 DEBUGGING: Graph Structure")

    from haive.agents.reasoning_and_critique.self_discover.v2.agent import (
        self_discovery,
    )

    # Check if the agent has been built
    if hasattr(self_discovery, "_app") and self_discovery._app:
        print("✅ Agent has compiled graph")

        # Try to examine the graph structure
        try:
            graph = self_discovery._app
            print(f"Graph type: {type(graph)}")

            if hasattr(graph, "nodes"):
                print(
                    f"Graph nodes: {list(graph.nodes.keys()) if hasattr(graph.nodes, 'keys') else 'N/A'}"
                )

            if hasattr(graph, "channels"):
                print(
                    f"Graph channels: {list(graph.channels.keys()) if hasattr(graph.channels, 'keys') else 'N/A'}"
                )

        except Exception as e:
            print(f"❌ Error examining graph: {e}")
    else:
        print("❌ Agent graph not compiled yet")

        # Try to manually build the graph
        try:
            print("🔄 Attempting to build graph...")
            if hasattr(self_discovery, "build_graph"):
                graph = self_discovery.build_graph()
                print(f"✅ Built graph: {type(graph)}")
            else:
                print("❌ No build_graph method found")
        except Exception as e:
            print(f"❌ Error building graph: {e}")


if __name__ == "__main__":
    print("🚀 Self-Discovery Agent Debugger")
    print("=" * 40)

    # First check the graph structure
    debug_graph_structure()

    # Then run the main debugging session
    debug_with_breakpoints()
