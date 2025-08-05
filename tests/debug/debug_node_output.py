#!/usr/bin/env python3
"""Debug what the node is actually outputting."""

import sys


sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")


def debug_node_actual_output():
    """Show exactly what the node outputs."""
    try:
        from haive.agents.reasoning_and_critique.self_discover.v2.agent import (
            self_discovery,
        )
        from haive.core.graph.node.agent_node_v3 import create_agent_node_v3

        # Get the first agent
        first_agent_name = next(iter(self_discovery.agents.keys()))
        first_agent = self_discovery.agents[first_agent_name]

        # Create a node config
        node_config = create_agent_node_v3(
            agent_name=first_agent_name,
            agent=first_agent,
            name=f"test_{first_agent_name}",
        )

        # Create test state that should work
        test_state = {
            "task_description": "Simple test task",
            "messages": [],
            "reasoning_modules": "Test modules",
            "selected_modules": None,
            "adapted_modules": None,
            "reasoning_structure": None,
            "answer": None,
            "error": None,
            "metadata": {},
        }

        node_result = node_config(test_state)

        if hasattr(node_result, "update") and isinstance(node_result.update, dict):
            for _key, _value in node_result.update.items():
                pass

        if hasattr(node_result, "goto"):
            pass

        # Now let's see what happens if we try to use it in a LangGraph-like context

        # Simulate what LangGraph does
        try:
            # This is what LangGraph's _get_updates does - it expects a dict
            if hasattr(node_result, "update"):
                update_dict = node_result.update

                if isinstance(update_dict, dict):
                    pass
                else:
                    pass
            else:
                pass

        except Exception:
            pass

        # Test what the actual multiagent does
        try:
            # Build the graph to see what nodes look like
            graph = self_discovery.build_graph()

            # Check the nodes
            if hasattr(graph, "nodes"):
                # Get the first node
                if hasattr(graph.nodes, "items"):
                    for _node_name, node_func in list(graph.nodes.items())[:1]:
                        # Try calling it
                        try:
                            node_output = node_func(test_state)

                            # Check if it returns Command or dict
                            if hasattr(node_output, "update") or isinstance(node_output, dict):
                                pass
                            else:
                                pass

                        except Exception:
                            import traceback

                            traceback.print_exc()

        except Exception:
            import traceback

            traceback.print_exc()

    except Exception:
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    debug_node_actual_output()
