#!/usr/bin/env python3
"""Test SimpleAgent validation fix for Plan[Task] structured output."""

from typing import List
from pydantic import BaseModel, Field
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig

class Task(BaseModel):
    description: str = Field(description="Task description")

class Plan[T](BaseModel):
    objective: str = Field(description="Plan objective")
    steps: List[T] = Field(description="Plan steps", max_length=2)

def test_simple_agent_validation_fix():
    """Test that SimpleAgent works with structured output after fix."""
    print("\n=== TESTING SIMPLE AGENT VALIDATION FIX ===\n")
    
    # Create SimpleAgent with structured output
    agent = SimpleAgent(
        name="planner",
        engine=AugLLMConfig(
            structured_output_model=Plan[Task],
            temperature=0.1  # Low for consistency
        )
    )
    
    print("1. Agent created successfully")
    print(f"   - Agent name: {agent.name}")
    print(f"   - Engine type: {type(agent.engine)}")
    print(f"   - Structured output model: {agent.engine.structured_output_model}")
    
    # Check tool routes
    print("\n2. Tool routes:")
    for name, route in agent.engine.tool_routes.items():
        print(f"   {name} → {route}")
    
    # Check graph structure
    print(f"\n3. Graph structure:")
    print(f"   Nodes: {list(agent.graph.nodes.keys())}")
    
    # Check edges FROM validation node
    validation_edges = []
    if hasattr(agent.graph, 'edges'):
        edges = agent.graph.edges
        if callable(edges):
            edges = edges()
        for edge in edges:
            if isinstance(edge, tuple) and len(edge) == 2:
                source, target = edge
                if source == "validation":
                    validation_edges.append(f"{source} → {target}")
    
    print(f"   Edges from validation: {validation_edges}")
    print(f"   All edges: {list(agent.graph.edges) if hasattr(agent.graph, 'edges') else 'No edges attr'}")
    
    # The critical test - try to execute with recursion limit
    print("\n4. Testing execution...")
    try:
        # Set recursion limit of 5 in the runnable config
        config = {"recursion_limit": 5}
        result = agent.invoke(
            {"messages": [{"role": "user", "content": "Create a simple plan with 2 tasks for organizing a workshop"}]},
            config=config
        )
        print(f"   ✅ SUCCESS! Result type: {type(result)}")
        if hasattr(result, 'get'):
            messages = result.get('messages', [])
            print(f"   Messages count: {len(messages)}")
            if messages:
                last_msg = messages[-1]
                print(f"   Last message type: {type(last_msg)}")
                print(f"   Last message content: {getattr(last_msg, 'content', 'No content')[:100]}...")
        return True
    except RecursionError as e:
        print(f"   ❌ RECURSION ERROR (hit limit): {e}")
        return False
    except Exception as e:
        print(f"   ❌ OTHER ERROR: {type(e).__name__}: {str(e)[:200]}...")
        return False

if __name__ == "__main__":
    success = test_simple_agent_validation_fix()
    if success:
        print("\n🎉 FIX SUCCESSFUL!")
    else:
        print("\n💥 FIX FAILED!")