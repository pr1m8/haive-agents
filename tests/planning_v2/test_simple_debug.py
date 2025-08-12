#!/usr/bin/env python3
"""Debug SimpleAgent validation routing."""


from pydantic import BaseModel, Field

from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


class Task(BaseModel):
    description: str = Field(description="Task description")

class Plan[T](BaseModel):
    objective: str = Field(description="Plan objective")
    steps: list[T] = Field(description="Plan steps", max_length=2)

def debug_simple_agent():
    """Debug SimpleAgent to see why validation routing isn't working."""
    print("\n=== DEBUGGING SIMPLE AGENT ===\n")

    # Create SimpleAgent with debug enabled
    agent = SimpleAgent(
        name="debug_planner",
        engine=AugLLMConfig(
            structured_output_model=Plan[Task],
            temperature=0.1
        ),
        debug=True  # Enable debug logging
    )

    print("1. Agent debug info:")
    print(f"   - force_tool_use: {agent.force_tool_use}")
    print(f"   - structured_output_model: {agent.structured_output_model}")
    print(f"   - engine.structured_output_model: {getattr(agent.engine, 'structured_output_model', None)}")
    print(f"   - _has_structured_output(): {agent._has_structured_output()}")
    print(f"   - _always_needs_validation(): {agent._always_needs_validation()}")

    print("\n2. Graph structure:")
    print(f"   Nodes: {list(agent.graph.nodes.keys())}")

    # Check all edges
    print(f"   All edges: {list(agent.graph.edges)}")

    # Check validation edges specifically
    validation_out_edges = []
    for edge in agent.graph.edges:
        if isinstance(edge, (list, tuple)) and len(edge) >= 2:
            source, target = edge[0], edge[1]
            if source == "validation":
                validation_out_edges.append(f"{source} → {target}")

    print(f"   Validation outgoing edges: {validation_out_edges}")

    # Check conditional edges
    if hasattr(agent.graph, "branches"):
        print(f"   Conditional edges (branches): {agent.graph.branches}")

    return agent

if __name__ == "__main__":
    debug_simple_agent()
