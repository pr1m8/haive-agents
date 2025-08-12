#!/usr/bin/env python3
"""Debug the actual graph structure to see edges."""

from pydantic import BaseModel, Field

from haive.agents.react.agent import ReactAgent
from haive.core.engine.aug_llm import AugLLMConfig


class SimpleResult(BaseModel):
    """Simple structured result."""
    answer: str = Field(description="The answer")


def test_graph_structure():
    """Check the actual graph edges."""
    
    print("🔍 Testing ReactAgent graph structure...")
    
    # Create engine with structured output
    engine = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.3,
        system_message="You are a helpful assistant."
    )
    
    print(f"   ✅ Engine tool_routes: {engine.tool_routes}")
    
    # Create ReactAgent
    agent = ReactAgent(
        name="graph_test",
        engine=engine,
        tools=[],
        max_iterations=2,
        debug=True
    )
    
    print(f"   ✅ Agent created")
    
    # Get the graph
    graph = agent.graph
    print(f"   ✅ Graph nodes: {list(graph.nodes.keys())}")
    
    # Check all edges
    print("   ✅ Graph edges:")
    edges = graph.get_edges()
    for source, target in edges:
        print(f"     {source} → {target}")
    
    # Check specifically for parse_output edges
    parse_output_edges = [target for source, target in edges if source == "parse_output"]
    print(f"   🎯 parse_output → {parse_output_edges}")
    
    # Check if END is in the parse_output targets
    if "__end__" in parse_output_edges:
        print("   ✅ parse_output → __end__ edge EXISTS")
    else:
        print("   ❌ parse_output → __end__ edge MISSING")
        
    if "agent_node" in parse_output_edges:
        print("   ❌ parse_output → agent_node edge EXISTS (causing loop)")
    else:
        print("   ✅ parse_output → agent_node edge does NOT exist")
    
    # Check tool_node edges too
    tool_node_edges = [target for source, target in edges if source == "tool_node"]
    print(f"   🎯 tool_node → {tool_node_edges}")
    
    if "__end__" in tool_node_edges:
        print("   ❌ tool_node → __end__ edge EXISTS (should loop to agent_node)")
    else:
        print("   ✅ tool_node → __end__ edge does NOT exist")
        
    if "agent_node" in tool_node_edges:
        print("   ✅ tool_node → agent_node edge EXISTS (correct for ReAct)")
    else:
        print("   ❌ tool_node → agent_node edge MISSING")
    
    return graph


if __name__ == "__main__":
    test_graph_structure()