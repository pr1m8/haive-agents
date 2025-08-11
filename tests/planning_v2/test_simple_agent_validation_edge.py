#!/usr/bin/env python3
"""Test to confirm SimpleAgent validation node has no outgoing edges."""

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

def test_validation_edges():
    """Confirm validation node has no outgoing edges."""
    print("\n=== SIMPLE AGENT VALIDATION EDGE TEST ===\n")
    
    config = AugLLMConfig(structured_output_model=Plan[Task])
    
    agent = SimpleAgent(
        name="test",
        engine=config,
        prompt_template=ChatPromptTemplate.from_messages([
            ("system", "You are a planner."),
            ("human", "{objective}")
        ])
    )
    
    print("1. Graph analysis:")
    
    # Check edges
    edges = list(agent.graph.edges)
    print(f"\nAll edges ({len(edges)}):")
    for edge in edges:
        print(f"   {edge[0]} → {edge[1]}")
    
    # Check for edges FROM validation
    validation_outgoing = [edge for edge in edges if edge[0] == "validation"]
    print(f"\nEdges FROM validation: {len(validation_outgoing)}")
    if validation_outgoing:
        for edge in validation_outgoing:
            print(f"   {edge}")
    else:
        print("   ❌ NO EDGES FROM VALIDATION NODE!")
    
    # Check conditional edges if any
    if hasattr(agent.graph, '_branches'):
        print(f"\nConditional edges (branches): {len(agent.graph._branches)}")
        for node, branch in agent.graph._branches.items():
            print(f"   From {node}: {branch}")
    
    # Check what validation node is configured with
    validation_node = agent.graph.nodes.get("validation")
    if validation_node:
        print(f"\nValidation node config:")
        print(f"   Type: {type(validation_node)}")
        if hasattr(validation_node, 'tool_node'):
            print(f"   tool_node: {validation_node.tool_node}")
        if hasattr(validation_node, 'parser_node'):
            print(f"   parser_node: {validation_node.parser_node}")
        if hasattr(validation_node, 'command_goto'):
            print(f"   command_goto: {validation_node.command_goto}")
    
    print("\n2. THE PROBLEM:")
    print("   - SimpleAgent adds 'validation' as a regular node")
    print("   - It connects agent_node → validation")
    print("   - But NOTHING connects FROM validation to anywhere else!")
    print("   - The graph gets stuck at validation with no way forward")
    print("\n3. HOW V2 FIXES IT:")
    print("   - V2 adds 'validation_v2' as a node that updates state")
    print("   - Then uses validation_router_v2 as a CONDITIONAL EDGE")
    print("   - This allows proper routing: validation → parse_output")

if __name__ == "__main__":
    test_validation_edges()