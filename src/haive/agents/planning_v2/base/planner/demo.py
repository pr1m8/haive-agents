"""Demo of the simplified planner agent with optional context."""

import asyncio

from haive.agents.planning_v2.base.planner.agent import PlannerAgent
from haive.agents.planning_v2.base.planner.prompts import create_planner_prompt


async def demo_planner():
    """Demonstrate the planner agent with and without context."""
    # Example 1: Basic planning without context
    print("=== Example 1: Planning without context ===")
    planner = PlannerAgent(name="basic_planner")

    result = await planner.arun(
        {"objective": "Build a REST API for a todo list application"}
    )

    print(f"Objective: {result.objective}")
    print(f"Number of steps: {len(result.steps)}")
    for i, step in enumerate(result.steps, 1):
        print(f"{i}. {step.description}")
    print()

    # Example 2: Planning with context
    print("=== Example 2: Planning with context ===")

    # Create a planner with context in the prompt
    context = """
    Technical constraints:
    - Must use Python with FastAPI
    - PostgreSQL database required
    - Deploy to AWS Lambda
    - Include authentication with JWT
    - Support real-time updates via WebSockets
    """

    # Create agent with contextualized prompt
    contextual_planner = PlannerAgent(
        name="contextual_planner", prompt_template=create_planner_prompt(context)
    )

    result_with_context = await contextual_planner.arun(
        {"objective": "Build a REST API for a todo list application"}
    )

    print(f"Objective: {result_with_context.objective}")
    print(f"Number of steps: {len(result_with_context.steps)}")
    for i, step in enumerate(result_with_context.steps, 1):
        print(f"{i}. {step.description}")
    print()

    # Example 3: Dynamic context with partial
    print("=== Example 3: Dynamic context approach ===")

    # You can also dynamically set context
    dynamic_planner = PlannerAgent(
        name="dynamic_planner",
        prompt_template=planner_prompt.partial(
            context_section="\nAdditional Context:\nThis is a microservices architecture with existing user service.\n"
        ),
    )

    result_dynamic = await dynamic_planner.arun(
        {"objective": "Add notification service to the system"}
    )

    print(f"Objective: {result_dynamic.objective}")
    print("First 3 steps:")
    for i, step in enumerate(result_dynamic.steps[:3], 1):
        print(f"{i}. {step.description}")


if __name__ == "__main__":
    # Run the demo
    asyncio.run(demo_planner())
