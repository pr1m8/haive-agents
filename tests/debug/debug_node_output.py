#!/usr/bin/env python3
"""Debug what the node is actually outputting."""

import sys

sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")


def debug_node_actual_output():
    """Show exactly what the node outputs."""
    print("🔍 DEBUGGING: Exact Node Output")

    try:
        from haive.core.graph.node.agent_node_v3 import create_agent_node_v3

        from haive.agents.reasoning_and_critique.self_discover.v2.agent import (
            self_discovery,
        )

        # Get the first agent
        first_agent_name = list(self_discovery.agents.keys())[0]
        first_agent = self_discovery.agents[first_agent_name]

        print(f"🔍 Testing agent: {first_agent_name}")

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

        print(f"📝 Input state keys: {list(test_state.keys())}")

        print("\n🚀 CALLING NODE DIRECTLY...")
        node_result = node_config(test_state)

        print("\n📋 NODE OUTPUT ANALYSIS:")
        print(f"✅ Result type: {type(node_result)}")
        print(f"✅ Result repr: {node_result!r}")

        if hasattr(node_result, "update"):
            print("\n🔍 Command.update:")
            print(f"  Type: {type(node_result.update)}")
            print(f"  Content: {node_result.update}")

            if isinstance(node_result.update, dict):
                print(f"  Keys: {list(node_result.update.keys())}")
                for key, value in node_result.update.items():
                    print(f"    {key}: {type(value)} = {value}")

        if hasattr(node_result, "goto"):
            print(f"\n🔍 Command.goto: {node_result.goto}")

        # Now let's see what happens if we try to use it in a LangGraph-like context
        print("\n🔍 TESTING: What LangGraph expects")

        # Simulate what LangGraph does
        try:
            # This is what LangGraph's _get_updates does - it expects a dict
            if hasattr(node_result, "update"):
                update_dict = node_result.update
                print(f"✅ Command.update is dict: {isinstance(update_dict, dict)}")

                if isinstance(update_dict, dict):
                    print("✅ Would work with LangGraph - it's a proper dict")
                else:
                    print(f"❌ Problem: update is {type(update_dict)}, not dict")
            else:
                print("❌ Problem: No 'update' attribute found")

        except Exception as e:
            print(f"❌ Simulation failed: {e}")

        # Test what the actual multiagent does
        print("\n🔍 TESTING: Full MultiAgent Path")
        try:
            # Build the graph to see what nodes look like
            graph = self_discovery.build_graph()
            print(f"✅ Graph built: {type(graph)}")

            # Check the nodes
            if hasattr(graph, "nodes"):
                print(
                    f"✅ Graph nodes: {list(graph.nodes.keys()) if hasattr(graph.nodes, 'keys') else 'N/A'}"
                )

                # Get the first node
                if hasattr(graph.nodes, "items"):
                    for node_name, node_func in list(graph.nodes.items())[:1]:
                        print(f"\n🔍 Testing node: {node_name}")
                        print(f"  Node type: {type(node_func)}")

                        # Try calling it
                        try:
                            node_output = node_func(test_state)
                            print(f"  ✅ Node output type: {type(node_output)}")
                            print(f"  ✅ Node output: {node_output}")

                            # Check if it returns Command or dict
                            if hasattr(node_output, "update"):
                                print("  ✅ Has update attribute")
                                print(f"  ✅ Update type: {type(node_output.update)}")
                                print(f"  ✅ Update content: {node_output.update}")
                            elif isinstance(node_output, dict):
                                print("  ✅ Returns plain dict")
                                print(f"  ✅ Dict keys: {list(node_output.keys())}")
                            else:
                                print(f"  ❌ Unknown return type: {type(node_output)}")

                        except Exception as e:
                            print(f"  ❌ Node call failed: {e}")
                            import traceback

                            traceback.print_exc()

        except Exception as e:
            print(f"❌ Graph test failed: {e}")
            import traceback

            traceback.print_exc()

    except Exception as e:
        print(f"❌ Debug failed: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    print("🚀 Node Output Debugger")
    print("=" * 50)
    debug_node_actual_output()
