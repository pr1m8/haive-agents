"""Debug script to trace structured output parsing."""

import asyncio
import pdb

from haive.core.engine.aug_llm import AugLLMConfig

from haive.agents.planning_v2.base.models import Plan, Status, Task
from haive.agents.planning_v2.base.planner.models import TaskPlan
from haive.agents.planning_v2.base.planner.prompts import planner_prompt
from haive.agents.simple import SimpleAgent


async def debug_planner():
    """Debug planner with breakpoints."""
    print("=== DEBUG: Testing Plan[Task] vs TaskPlan ===")

    # Test 1: Plan[Task] (like the failing test)
    print("\n1. Testing Plan[Task] (generic)...")
    engine1 = AugLLMConfig(temperature=0.3, structured_output_model=Plan[Task])

    planner1 = SimpleAgent(
        name="test_planner_generic", engine=engine1, prompt_template=planner_prompt
    )

    print(f"Engine structured_output_model: {engine1.structured_output_model}")
    print(
        f"Agent structured_output_model: {getattr(planner1, 'structured_output_model', None)}"
    )

    # Add breakpoint before execution
    pdb.set_trace()

    result1 = await planner1.arun(
        {"objective": "Build a simple REST API for a todo list"}
    )

    print(f"Result1 type: {type(result1)}")
    print(f"Result1 content: {result1}")

    # Test 2: TaskPlan (concrete)
    print("\n2. Testing TaskPlan (concrete)...")
    engine2 = AugLLMConfig(temperature=0.3, structured_output_model=TaskPlan)

    planner2 = SimpleAgent(
        name="test_planner_concrete", engine=engine2, prompt_template=planner_prompt
    )

    print(f"Engine structured_output_model: {engine2.structured_output_model}")
    print(
        f"Agent structured_output_model: {getattr(planner2, 'structured_output_model', None)}"
    )

    result2 = await planner2.arun(
        {"objective": "Build a simple REST API for a todo list"}
    )

    print(f"Result2 type: {type(result2)}")
    print(f"Result2 content: {result2}")


if __name__ == "__main__":
    asyncio.run(debug_planner())
