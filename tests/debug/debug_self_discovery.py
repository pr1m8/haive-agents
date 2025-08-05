#!/usr/bin/env python3
"""Debug script for self-discovery agent with breakpoints."""

import pdb
import sys
import traceback


sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")


def debug_agent_structure():
    """Debug the agent structure and setup."""
    # Check if it's a ProperMultiAgent
    from haive.agents.multi.proper_base import ProperMultiAgent
    from haive.agents.reasoning_and_critique.self_discover.v2.agent import (
        self_discovery,
    )

    isinstance(self_discovery, ProperMultiAgent)

    # Check the agents structure
    if isinstance(self_discovery.agents, dict):
        for _name, _agent in self_discovery.agents.items():
            pass

    # Check the graph/app structure
    if hasattr(self_discovery, "_app"):
        pass
    else:
        pass

    return self_discovery


def debug_input_preparation():
    """Debug input preparation for the agent."""
    problem = "Lisa has 10 apples. She gives 3 apples to her friend and then buys 5 more apples from the store. How many apples does Lisa have now?"

    # Test different input formats

    # Format 1: Simple string (like the examples)
    input1 = problem

    # Format 2: Dict with task_description
    input2 = {"task_description": problem}

    # Format 3: Dict with messages (like ProperMultiAgent might expect)
    input3 = {"messages": [], "task_description": problem}

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

    return problem, input1, input2, input3, input4


def debug_with_breakpoints():
    """Run the debugging with strategic breakpoints."""
    try:
        # Step 1: Check agent structure
        agent = debug_agent_structure()

        # Step 2: Prepare inputs
        problem, input1, input2, input3, input4 = debug_input_preparation()

        # Step 3: Try to run with different input formats

        # Set a breakpoint before execution
        pdb.set_trace()  # Breakpoint 1: Before testing inputs

        for _i, test_input in enumerate([input2, input3, input4], 1):
            try:
                # Another breakpoint before each run attempt
                pdb.set_trace()  # Breakpoint 2: Before each run

                agent.run(test_input)
                break  # If successful, stop testing

            except Exception:
                # Breakpoint on error to examine
                pdb.set_trace()  # Breakpoint 3: On error

                continue

    except Exception:
        traceback.print_exc()

        # Final breakpoint for critical errors
        pdb.set_trace()  # Breakpoint 4: Critical error


def debug_graph_structure():
    """Debug the internal graph structure that's causing the error."""
    from haive.agents.reasoning_and_critique.self_discover.v2.agent import (
        self_discovery,
    )

    # Check if the agent has been built
    if hasattr(self_discovery, "_app") and self_discovery._app:
        # Try to examine the graph structure
        try:
            graph = self_discovery._app

            if hasattr(graph, "nodes"):
                pass

            if hasattr(graph, "channels"):
                pass

        except Exception:
            pass
    else:
        # Try to manually build the graph
        try:
            if hasattr(self_discovery, "build_graph"):
                graph = self_discovery.build_graph()
            else:
                pass
        except Exception:
            pass


if __name__ == "__main__":
    # First check the graph structure
    debug_graph_structure()

    # Then run the main debugging session
    debug_with_breakpoints()
