#!/usr/bin/env python3
"""Check SimpleAgent graph structure."""

from typing import List
from pydantic import BaseModel, Field
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate

class Task(BaseModel):
    description: str = Field(description="Task")

class Plan[T](BaseModel):
    objective: str = Field(description="Objective")
    steps: List[T] = Field(description="Steps", max_length=2)

def test_graph_structure():
    """Check how SimpleAgent sets up its graph."""
    print("\n=== SIMPLE AGENT GRAPH STRUCTURE ===\n")
    
    config = AugLLMConfig(structured_output_model=Plan[Task])
    
    agent = SimpleAgent(
        name="test",
        engine=config,
        prompt_template=ChatPromptTemplate.from_messages([
            ("system", "You are a planner."),
            ("human", "{objective}")
        ])
    )
    
    print("1. Graph nodes:")
    for node in agent.graph.nodes:
        print(f"   - {node}")
    
    print("\n2. Graph edges:")
    if hasattr(agent.graph, 'edges'):
        for edge in agent.graph.edges:
            print(f"   {edge}")
    
    print("\n3. Check graph internals:")
    # Different ways to access graph structure
    if hasattr(agent.graph, '__dict__'):
        print("   Graph attributes:", list(agent.graph.__dict__.keys()))
    
    # Check if parse_output is connected
    print("\n4. Key question:")
    print("   - We have a 'parse_output' node")
    print("   - Validation router returns 'parse_output'") 
    print("   - But does the graph route from validation -> parse_output?")
    
    # Try to compile and check
    try:
        compiled = agent.graph.compile()
        print("\n5. Compiled graph info:")
        if hasattr(compiled, 'get_graph'):
            graph_info = compiled.get_graph()
            print(f"   Nodes: {graph_info.nodes if hasattr(graph_info, 'nodes') else 'N/A'}")
    except Exception as e:
        print(f"\n5. Compile error: {e}")

if __name__ == "__main__":
    test_graph_structure()