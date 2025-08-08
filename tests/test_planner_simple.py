"""Simple test of the planner agent."""

import asyncio

# Direct imports to avoid circular references
from haive.agents.simple import SimpleAgent
from haive.agents.planning_v2.base.models import Plan, Task
from haive.agents.planning_v2.base.planner.prompts import planner_prompt, create_planner_prompt
from haive.core.engine.aug_llm import AugLLMConfig


async def test_planner():
    """Test the planner by creating it directly."""
    
    print("Creating planner agent...")
    
    # Create engine with structured output
    engine = AugLLMConfig(
        temperature=0.3,
        structured_output_model=Plan[Task]
    )
    
    # Create planner using SimpleAgent directly
    planner = SimpleAgent(
        name="test_planner",
        engine=engine,
        prompt_template=planner_prompt
    )
    
    print("Running planner...")
    
    # Test without context
    result = await planner.arun({
        "objective": "Build a simple REST API"
    })
    
    print(f"\nPlan created!")
    print(f"Objective: {result.objective}")
    print(f"Status: {result.status}")
    print(f"Number of steps: {len(result.steps)}")
    
    print("\nSteps:")
    for i, step in enumerate(result.steps, 1):
        print(f"{i}. {step.description}")
        print(f"   Status: {step.status}")
    
    print("\n" + "="*50 + "\n")
    
    # Test with context
    print("Testing with context...")
    
    context = "Use FastAPI framework and include user authentication"
    planner_with_context = SimpleAgent(
        name="contextual_planner",
        engine=engine,
        prompt_template=create_planner_prompt(context)
    )
    
    result2 = await planner_with_context.arun({
        "objective": "Build a simple REST API"
    })
    
    print(f"\nWith context:")
    print(f"Number of steps: {len(result2.steps)}")
    print("\nFirst 3 steps:")
    for i, step in enumerate(result2.steps[:3], 1):
        print(f"{i}. {step.description}")


if __name__ == "__main__":
    asyncio.run(test_planner())