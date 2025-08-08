"""Simple example of using the PlannerAgent."""

import asyncio

from haive.agents.planning_v2.base.planner.agent import PlannerAgent
from haive.agents.planning_v2.base.planner.prompts import planner_prompt


async def main():
    """Show the simplest way to use the planner."""

    # Create planner - that's it!
    planner = PlannerAgent()

    # Plan something without context
    plan = await planner.arun(
        {"objective": "Create a Python package for data validation"}
    )

    print(f"Generated {len(plan.steps)} steps:")
    for i, step in enumerate(plan.steps, 1):
        print(f"{i}. {step.description}")

    print("\n---\n")

    # Plan with context by using partial
    planner_with_context = PlannerAgent(
        prompt_template=planner_prompt.partial(
            context_section="\nContext: Must be compatible with Python 3.8+ and use Pydantic for models.\n"
        )
    )

    plan2 = await planner_with_context.arun(
        {"objective": "Create a Python package for data validation"}
    )

    print(f"With context, generated {len(plan2.steps)} steps:")
    for i, step in enumerate(plan2.steps[:3], 1):
        print(f"{i}. {step.description}")
    print("...")


if __name__ == "__main__":
    asyncio.run(main())
