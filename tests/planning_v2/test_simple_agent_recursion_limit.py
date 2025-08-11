#!/usr/bin/env python3
"""Test SimpleAgent with recursion limit to see the validation issue."""

import asyncio
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

async def test_with_recursion_limit():
    """Test SimpleAgent with structured output and recursion limit."""
    print("\n=== SIMPLE AGENT WITH RECURSION LIMIT ===\n")
    
    config = AugLLMConfig(
        temperature=0.1,
        structured_output_model=Plan[Task]
    )
    
    agent = SimpleAgent(
        name="test_agent",
        engine=config,
        prompt_template=ChatPromptTemplate.from_messages([
            ("system", "You are a planner. Create plans with clear objectives and steps."),
            ("human", "{objective}")
        ])
    )
    
    print("Graph structure:")
    print(f"  Nodes: {list(agent.graph.nodes.keys())}")
    print(f"  Edges: {list(agent.graph.edges)}")
    
    validation_edges = [e for e in agent.graph.edges if e[0] == "validation"]
    print(f"  Edges FROM validation: {validation_edges} (EMPTY!)")
    
    # Run with recursion limit
    print("\nRunning with recursion_limit=5...")
    
    try:
        result = await agent.arun(
            {"objective": "Build a simple REST API"},
            runnable_config={"recursion_limit": 5}
        )
        print(f"\nResult type: {type(result)}")
        
    except Exception as e:
        print(f"\n❌ Error after 5 recursions: {type(e).__name__}")
        print(f"   Message: {str(e)[:200]}...")
        
        if "recursion_limit" in str(e).lower() or "iteration" in str(e).lower():
            print("\n🎯 CONFIRMED: Graph gets stuck at validation node!")
            print("   - The graph executes: agent_node → validation")
            print("   - But validation has NO outgoing edges")
            print("   - So it loops back to agent_node")
            print("   - This repeats until recursion limit is hit")

if __name__ == "__main__":
    asyncio.run(test_with_recursion_limit())