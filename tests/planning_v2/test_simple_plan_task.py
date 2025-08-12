#!/usr/bin/env python3
"""Test simple Plan[Task] execution with updated validation router."""

import asyncio
import logging

from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


# Enable INFO logging to see routing decisions
logging.basicConfig(level=logging.INFO, format="%(name)s - %(message)s")

class Task(BaseModel):
    """A single task."""
    description: str = Field(description="Task description")
    priority: int = Field(default=1, ge=1, le=5)

class Plan[T](BaseModel):
    """Generic plan container."""
    objective: str = Field(description="Overall objective")
    steps: list[T] = Field(description="List of steps")

async def test_plan_task():
    """Test Plan[Task] with the updated validation router."""
    print("\n" + "="*60)
    print("TESTING Plan[Task] WITH UPDATED VALIDATION ROUTER")
    print("="*60)

    # Create agent with Plan[Task]
    config = AugLLMConfig(
        temperature=0.1,
        structured_output_model=Plan[Task]
    )

    agent = SimpleAgent(
        name="planner",
        engine=config,
        prompt_template=ChatPromptTemplate.from_messages([
            ("system", "You are a helpful task planner. Create clear, actionable plans."),
            ("human", "Create a plan for: {objective}")
        ])
    )

    print(f"\nAgent created with structured output model: {config.structured_output_model}")
    print(f"Tool routes: {config.tool_routes}")

    # Test with a simple objective
    try:
        print("\nGenerating plan...")
        result = await agent.arun({
            "objective": "Organize a team meeting"
        })

        print("\n✅ Success! Generated plan:")
        print(f"  Objective: {result.objective}")
        print(f"  Steps: {len(result.steps)}")
        for i, step in enumerate(result.steps, 1):
            print(f"    {i}. {step.description} (priority: {step.priority})")

        return result

    except Exception as e:
        print(f"\n❌ Error: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    result = asyncio.run(test_plan_task())

    if result:
        print("\n" + "="*60)
        print("TEST PASSED - No recursion error!")
        print("="*60)
    else:
        print("\n" + "="*60)
        print("TEST FAILED - Check the error above")
        print("="*60)
