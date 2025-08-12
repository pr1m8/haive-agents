#!/usr/bin/env python3
"""Test SimpleAgent.run with debug=True to see actual graph flow."""


from pydantic import BaseModel, Field

from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


class Task(BaseModel):
    description: str = Field(description="Task description")

class Plan[T](BaseModel):
    objective: str = Field(description="Plan objective")
    steps: list[T] = Field(description="Plan steps", max_length=2)

def test_simple_agent_debug_run():
    """Test SimpleAgent.run with debug=True to see graph flow."""
    print("=== TESTING SimpleAgent.run(debug=True) ===\n")

    # Create SimpleAgent with structured output
    agent = SimpleAgent(
        name="debug_planner",
        engine=AugLLMConfig(
            structured_output_model=Plan[Task],
            temperature=0.1
        ),
        debug=True
    )

    print("1. Graph structure before execution:")
    print(f"   Nodes: {list(agent.graph.nodes.keys())}")

    if hasattr(agent.graph, "branches"):
        print("   Branches (conditional edges):")
        for branch_id, branch in agent.graph.branches.items():
            print(f"     {branch.source_node} → {branch.destinations}")

    print(f"   Tool routes: {agent.engine.tool_routes}")

    print("\n2. Executing with debug=True...")
    print("   Expected flow: START → agent_node → validation → parse_output → END")
    print("   Should be 3-4 steps maximum!\n")

    try:
        # Run with debug to see graph execution
        result = agent.run("Create a plan for organizing a workshop", debug=True)

        print("\n3. ✅ EXECUTION COMPLETE!")
        print(f"   Result type: {type(result)}")
        print(f"   Result: {result}")

        return True

    except Exception as e:
        print(f"\n3. ❌ EXECUTION FAILED: {type(e).__name__}: {str(e)[:200]}...")
        return False

if __name__ == "__main__":
    success = test_simple_agent_debug_run()
    if success and "step" in str(success).lower():
        print("\n⚠️  TOO MANY STEPS - FIX NOT WORKING PROPERLY")
    else:
        print(f"\n{'🎉 SUCCESS!' if success else '💥 FAILED'}")
