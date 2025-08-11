#!/usr/bin/env python3
"""Test SimpleAgentV2 graph structure (which uses proper routing)."""

from typing import List
from pydantic import BaseModel, Field
from haive.agents.simple.archive.agent_v2 import SimpleAgentV2
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate

class Task(BaseModel):
    description: str = Field(description="Task")

class Plan[T](BaseModel):
    objective: str = Field(description="Objective")
    steps: List[T] = Field(description="Steps", max_length=2)

def test_v2_graph_structure():
    """Check how SimpleAgentV2 sets up its graph."""
    print("\n=== SIMPLE AGENT V2 GRAPH STRUCTURE ===\n")
    
    config = AugLLMConfig(structured_output_model=Plan[Task])
    
    agent = SimpleAgentV2(
        name="test_v2",
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
    
    print("\n3. Check conditional edges:")
    if hasattr(agent.graph, 'conditional_edges'):
        for node, condition in agent.graph.conditional_edges.items():
            print(f"   From {node}: {condition}")
    
    print("\n4. The key difference:")
    print("   - V2 uses validation_v2 node that updates state")
    print("   - Then uses validation_router_v2 as CONDITIONAL EDGE")
    print("   - This allows routing from validation -> parse_output")

if __name__ == "__main__":
    test_v2_graph_structure()