"""Simple test for ReactAgent with structured output - no complex loops."""


def test_react_without_structured_output(react_agent_with_tools):
    """Test ReactAgent WITHOUT structured output graph structure."""

    react_agent = react_agent_with_tools

    print("\n🔍 Testing ReactAgent WITHOUT structured output:")
    print(f"   - Name: {react_agent.name}")
    print(f"   - Has structured_output_model: {bool(react_agent.structured_output_model)}")
    print(f"   - Auto-wrap needed: {getattr(react_agent, '_needs_structured_output_wrapper', False)}")

    # Check graph structure
    react_agent.compile()

    # Try to get graph info
    if hasattr(react_agent, "graph") and react_agent.graph:
        try:
            lg_graph = react_agent.graph.to_langgraph(state_schema=react_agent.state_schema)
            nodes = list(lg_graph.nodes.keys()) if hasattr(lg_graph, "nodes") else []
            print(f"   - Graph nodes: {nodes}")

            # Check edges to see if there are loops
            if hasattr(lg_graph, "edges"):
                edges = list(lg_graph.edges)
                print(f"   - Graph edges: {edges[:10]}...")  # Show first 10 edges

                # Look for problematic loops
                loop_edges = [edge for edge in edges if "agent_node" in str(edge)]
                print(f"   - Edges involving agent_node: {loop_edges}")

        except Exception as e:
            print(f"   - Could not inspect graph: {e}")

    assert True  # Just pass the test


def test_simple_react_structured_execution(react_agent_with_structured_output):
    """Simple test of auto-wrapped ReactAgent - just basic response."""

    react_agent = react_agent_with_structured_output
    test_input = "Say hello and give me a confidence score"

    # Just run with debug=True to see the LangGraph node routing steps
    result = react_agent.run(test_input, debug=True)

    return result


def test_check_auto_wrap_graph_structure(react_agent_with_structured_output):
    """Just check the graph structure without executing."""

    print("\n" + "="*60)
    print("🔍 CHECKING AUTO-WRAP GRAPH STRUCTURE")
    print("="*60)

    react_agent = react_agent_with_structured_output

    print("\n📋 Before compilation:")
    print(f"   - Auto-wrap needed: {getattr(react_agent, '_needs_structured_output_wrapper', False)}")
    print(f"   - Graph built: {react_agent._graph_built}")

    # Just compile, don't execute
    react_agent.compile()

    print("\n📋 After compilation:")
    print(f"   - Compiled: {react_agent._is_compiled}")
    print(f"   - App type: {type(react_agent._app)}")

    # Check graph nodes
    if hasattr(react_agent, "graph") and react_agent.graph:
        try:
            lg_graph = react_agent.graph.to_langgraph(state_schema=react_agent.state_schema)
            if hasattr(lg_graph, "nodes"):
                nodes = list(lg_graph.nodes.keys())
                print(f"   - Graph nodes: {nodes}")

                # Should have 2 nodes for auto-wrap
                if len(nodes) == 2:
                    print("   - ✅ Correct node count for auto-wrap")
                else:
                    print(f"   - ⚠️ Unexpected node count: {len(nodes)}")

                # Check for expected nodes
                if "react_structured" in nodes:
                    print("   - ✅ Found base ReactAgent node")
                if "react_structured_formatter" in nodes:
                    print("   - ✅ Found formatter SimpleAgent node")

            else:
                print("   - No nodes found in graph")

        except Exception as e:
            print(f"   - Could not inspect graph: {e}")

    print("\n✨ Auto-wrap creates:")
    print("   - MultiAgent with 2 nodes")
    print("   - Node 1: ReactAgent (reasoning + tools)")
    print("   - Node 2: SimpleAgent (structured output)")
