"""Test the planner agent with a real question."""

import asyncio
from haive.agents.planning_v2.base.planner.agent import PlannerAgent
from haive.agents.planning_v2.base.planner.prompts import create_planner_prompt


async def test_planner():
    """Test the planner with different scenarios."""
    
    # Test 1: Simple objective
    print("=== Test 1: Simple Planning Task ===")
    planner = PlannerAgent()
    
    result = await planner.arun({
        "objective": "Create a simple blog website"
    })
    
    print(f"\nObjective: {result.objective}")
    print(f"Status: {result.status}")
    print(f"Total steps: {len(result.steps)}")
    print("\nSteps:")
    for i, step in enumerate(result.steps, 1):
        print(f"\n{i}. {step.description}")
        if hasattr(step, 'status'):
            print(f"   Status: {step.status}")
    
    print("\n" + "="*50 + "\n")
    
    # Test 2: With technical context
    print("=== Test 2: With Technical Context ===")
    
    context = """Technical requirements:
    - Use Next.js for frontend
    - Use Supabase for backend
    - Deploy on Vercel
    - Include user authentication
    - Support markdown blog posts"""
    
    planner_with_context = PlannerAgent(
        prompt_template=create_planner_prompt(context)
    )
    
    result2 = await planner_with_context.arun({
        "objective": "Create a simple blog website"
    })
    
    print(f"\nObjective: {result2.objective}")
    print(f"Total steps: {len(result2.steps)}")
    print("\nFirst 5 steps:")
    for i, step in enumerate(result2.steps[:5], 1):
        print(f"\n{i}. {step.description}")


if __name__ == "__main__":
    asyncio.run(test_planner())