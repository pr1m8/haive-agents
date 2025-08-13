#!/usr/bin/env python3
"""Debug ReactAgent graph structure to see if the fix is working."""

from pydantic import BaseModel, Field

from haive.agents.react.agent import ReactAgent
from haive.core.engine.aug_llm import AugLLMConfig


class SimpleResult(BaseModel):
    """Simple structured result."""
    answer: str = Field(description="The answer")


def debug_react_graph_structure():
    """Debug the ReactAgent graph structure to see edge connections."""
    
    print("🔍 Creating ReactAgent with structured output...")
    
    agent = ReactAgent(
        name="debug_react",
        engine=AugLLMConfig(
            structured_output_model=SimpleResult,
            temperature=0.3,
            system_message="You are a helpful assistant."
        ),
        tools=[],
        max_iterations=2,
        debug=True  # Enable debug to see graph building messages
    )
    
    print(f"   - Agent created: {agent.name}")
    print(f"   - Has structured output: {agent._has_structured_output()}")
    print(f"   - Engine structured model: {agent.engine.structured_output_model}")
    
    # Build the graph explicitly to see debug output
    print("\n🔧 Building graph...")
    graph = agent.build_graph()
    
    print(f"\n📊 Graph structure:")
    print(f"   - Nodes: {list(graph.nodes.keys())}")
    
    # Try different approaches to inspect graph edges
    print(f"\n🔗 Graph edges (multiple inspection methods):")
    
    # Method 1: Try to access internal graph structure
    try:
        if hasattr(graph, 'app') and graph.app:
            print("   - Method 1: Using compiled app structure")
            # Try to get the compiled graph
            compiled_graph = graph.app
            if hasattr(compiled_graph, 'graph'):
                internal_graph = compiled_graph.graph
                print(f"     - Internal graph type: {type(internal_graph)}")
                if hasattr(internal_graph, 'edges'):
                    print(f"     - Found {len(internal_graph.edges)} edges")
                    for edge in internal_graph.edges:
                        print(f"       - {edge}")
                else:
                    print("     - No edges attribute found")
            else:
                print("     - No graph attribute on app")
        else:
            print("   - Method 1: No compiled app found")
    except Exception as e:
        print(f"   - Method 1 failed: {e}")
    
    # Method 2: Try to inspect before compilation
    try:
        print("   - Method 2: Before compilation inspection")
        if hasattr(graph, '_graph'):
            print(f"     - Graph object type: {type(graph._graph)}")
            # Try to access nodes and edges directly
            if hasattr(graph._graph, 'nodes'):
                print(f"     - Nodes: {list(graph._graph.nodes.keys())}")
            if hasattr(graph._graph, 'edges'):
                print(f"     - Edges: {list(graph._graph.edges.keys())}")
                # Check parse_output specifically
                parse_edges = [edge for edge in graph._graph.edges.keys() if edge[0] == "parse_output"]
                if parse_edges:
                    print(f"     - parse_output edges: {parse_edges}")
                    for edge in parse_edges:
                        print(f"       - parse_output → {edge[1]}")
    except Exception as e:
        print(f"   - Method 2 failed: {e}")
    
    # Method 3: Try to trace the actual execution path
    try:
        print("   - Method 3: Execution tracing")
        # Build a simple state to trace execution
        from haive.core.schema.prebuilt.llm_state import LLMState
        test_state = LLMState(messages=[])
        
        # Try to see what happens if we set the state to parse_output
        test_state.next_node = "parse_output"
        print(f"     - Created test state with next_node: {test_state.next_node}")
        
    except Exception as e:
        print(f"   - Method 3 failed: {e}")
    
    # Specifically check for parse_output routing
    if "parse_output" in graph.nodes:
        print(f"\n🎯 parse_output node specific analysis:")
        try:
            # Check compiled graph structure
            if hasattr(graph, 'app') and graph.app and hasattr(graph.app, 'graph'):
                edges = graph.app.graph.edges
                parse_output_edges = [str(edge) for edge in edges if "parse_output" in str(edge)]
                if parse_output_edges:
                    print(f"   - Found parse_output edges: {parse_output_edges}")
                    
                    # Look for specific patterns
                    has_end = any("__end__" in edge.lower() or "end" in edge.lower() for edge in parse_output_edges)
                    has_agent = any("agent_node" in edge for edge in parse_output_edges)
                    
                    print(f"   - Has END edge: {has_end}")
                    print(f"   - Has agent_node edge: {has_agent}")
                    
                    if has_agent and not has_end:
                        print("   - ❌ ISSUE: parse_output loops to agent_node!")
                    elif has_end and not has_agent:
                        print("   - ✅ GOOD: parse_output goes to END")
                    elif has_end and has_agent:
                        print("   - ⚠️  BOTH: parse_output has both END and agent_node edges")
                    else:
                        print("   - ❓ UNKNOWN: parse_output edge pattern unclear")
                else:
                    print("   - No parse_output edges found in compiled graph")
            else:
                print("   - Cannot access compiled graph for analysis")
                
        except Exception as e:
            print(f"   - Error in parse_output analysis: {e}")
    else:
        print(f"\n⚠️  No parse_output node found in graph")
    
    return agent


if __name__ == "__main__":
    agent = debug_react_graph_structure()
    print(f"\n✅ Graph debug complete for {agent.name}")