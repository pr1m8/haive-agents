#!/usr/bin/env python3
"""Final test of the planner with validation fix."""

import asyncio

from haive.agents.planning_v2.base.models import Plan, Task
from haive.agents.planning_v2.base.planner.prompts import planner_prompt
from haive.agents.simple import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


async def test_planner():
    """Test the planner with validation fix."""
    print("\n✨ TESTING PLANNER WITH VALIDATION FIX")
    print("="*60)

    # Create config
    config = AugLLMConfig(
        structured_output_model=Plan[Task],
        prompt_template=planner_prompt,
        temperature=0.3
    )

    # Create agent
    agent = SimpleAgent(name="planner", engine=config)

    print("Executing planner...")

    try:
        result = await agent.arun({
            "objective": "Build a simple REST API with user authentication"
        })

        print("\n✅ SUCCESS!")
        print(f"Result type: {type(result)}")

        if hasattr(result, "objective"):
            print(f"\nPlan objective: {result.objective}")
            print(f"Total steps: {result.total_steps}")
            print("\nSteps:")
            for i, step in enumerate(result.steps, 1):
                if hasattr(step, "objective"):
                    print(f"  {i}. {step.objective}")
                else:
                    print(f"  {i}. {step}")

    except Exception as e:
        print(f"\n❌ FAILED: {type(e).__name__}")
        print(f"Error: {e}")


async def main():
    """Run the test."""
    await test_planner()


if __name__ == "__main__":
    asyncio.run(main())
