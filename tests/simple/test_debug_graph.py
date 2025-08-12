"""Test SimpleAgent graph structure and routing with debug=True"""

import sys
import logging
from pydantic import BaseModel, Field
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


class SimpleResult(BaseModel):
    """Simple structured output."""
    response: str = Field(description="Response to the input")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence in response")


def test_simple_agent_graph_structure(caplog):
    """Test SimpleAgent graph structure and show edges/branches using pytest caplog"""
    
    # Set up logging to capture everything
    caplog.set_level(logging.DEBUG)
    
    # Create SimpleAgent with structured output
    simple_agent = SimpleAgent(
        name="debug_agent",
        engine=AugLLMConfig(
            structured_output_model=SimpleResult,
            temperature=0.1,
            max_tokens=50
        ),
        debug=False  # Turn off agent debug to see clean graph output
    )
    
    print(f"\n🔍 SimpleAgent Graph Analysis:")
    print(f"   - Name: {simple_agent.name}")
    print(f"   - Has structured_output_model: {bool(simple_agent.engine.structured_output_model)}")
    
    # Compile the agent to build the graph
    simple_agent.compile()
    
    # Show graph structure
    if hasattr(simple_agent, 'graph') and simple_agent.graph:
        try:
            print(f"\n📊 Graph Structure:")
            lg_graph = simple_agent.graph.to_langgraph(state_schema=simple_agent.state_schema)
            
            if hasattr(lg_graph, 'nodes'):
                nodes = list(lg_graph.nodes.keys())
                print(f"   - Nodes: {nodes}")
                
            if hasattr(lg_graph, 'edges'):
                edges = list(lg_graph.edges)
                print(f"   - Edges: {edges}")
                
            # Show conditional edges if any
            if hasattr(lg_graph, '_conditional_edges'):
                print(f"   - Conditional edges: {lg_graph._conditional_edges}")
                
            # Try to get more detailed graph info
            print(f"\n📋 Detailed Graph Information:")
            
            # Check if we can get edge information differently
            if hasattr(lg_graph, 'graph'):
                graph_info = lg_graph.graph
                print(f"   - Graph object: {type(graph_info)}")
                
                # Try to get edges from networkx graph
                if hasattr(graph_info, 'edges'):
                    all_edges = list(graph_info.edges())
                    print(f"   - All edges: {all_edges}")
                    
                if hasattr(graph_info, 'nodes'):
                    all_nodes = list(graph_info.nodes())
                    print(f"   - All nodes: {all_nodes}")
                
        except Exception as e:
            print(f"   - Could not inspect graph: {e}")
            import traceback
            traceback.print_exc()
    
    print(f"\n🚀 Running with agent.run(debug=True)...")
    print("="*80)
    
    # Run with debug=True to see the routing
    try:
        result = simple_agent.run("Say hello", debug=True)
        print(f"\n✅ Result: {result}")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
    
    # Write captured logs to file
    log_output = "\n".join([record.message for record in caplog.records])
    with open("simple_agent_debug.log", "w") as f:
        f.write("=== SimpleAgent Graph Debug Output ===\n\n")
        f.write("Captured stdout:\n")
        # This would capture print statements if we redirected stdout
        f.write("\nCaptured logs:\n")
        f.write(log_output)
        f.write("\n\n=== End Debug Output ===\n")
    
    print(f"\n📝 Debug output written to simple_agent_debug.log")


if __name__ == "__main__":
    test_simple_agent_graph_structure()