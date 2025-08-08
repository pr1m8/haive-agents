"""Test the planner agent implementation."""

import asyncio

from haive.agents.planning_v2 import Plan, PlannerAgent, Task


def test_basic_plan():
    """Test basic plan creation."""
    print("=== Testing Basic Plan Creation ===\n")

    # Create planner
    planner = PlannerAgent()

    # Create a plan
    plan = planner.create_plan(objective="Build a REST API for user management")

    # Display the plan
    print(f"Objective: {plan.objective}\n")
    print(f"Total Steps: {plan.total_steps}")
    print(f"Status: {plan.status}")
    print(f"Progress: {plan.progress_percentage:.1f}%\n")

    print("Steps:")
    for i, step in enumerate(plan.steps, 1):
        if isinstance(step, Task):
            print(f"{i}. {step.objective}")
            print(f"   Status: {step.status}")
            if step.result:
                print(f"   Result: {step.result}")
        elif isinstance(step, Plan):
            print(f"{i}. [SUBPLAN] {step.objective}")
            print(f"   Sub-steps: {len(step.steps)}")

    print("\n" + "=" * 50 + "\n")
    return plan


def test_detailed_plan():
    """Test detailed plan creation with requirements."""
    print("=== Testing Detailed Plan Creation ===\n")

    planner = PlannerAgent()

    plan = planner.create_detailed_plan(
        objective="Launch e-commerce website",
        requirements=[
            "Support for 10,000 concurrent users",
            "Payment processing with Stripe",
            "Mobile responsive design",
            "Multi-language support (EN, ES, FR)",
        ],
        constraints=["3 month timeline", "Budget of $50,000", "Team of 4 developers"],
        resources=[
            "AWS cloud infrastructure",
            "React/Next.js frontend stack",
            "PostgreSQL database",
            "Redis for caching",
        ],
        success_criteria=[
            "Page load time under 2 seconds",
            "99.9% uptime",
            "Conversion rate above 2%",
            "Mobile traffic > 50%",
        ],
    )

    print(f"Objective: {plan.objective}\n")
    print(f"Total Steps: {plan.total_steps}\n")

    print("Plan Structure:")
    for i, step in enumerate(plan.steps, 1):
        print(f"{i}. {step.objective}")

    print("\n" + "=" * 50 + "\n")
    return plan


def test_no_context():
    """Test plan creation without context."""
    print("=== Testing Plan Without Context ===\n")

    planner = PlannerAgent()

    # Simple objective with no context
    plan = planner.create_plan(objective="Set up continuous integration pipeline")

    print(f"Objective: {plan.objective}\n")
    print("Steps:")
    for i, step in enumerate(plan.steps, 1):
        print(f"{i}. {step.objective}")

    print("\n" + "=" * 50 + "\n")
    return plan


async def test_async_plan():
    """Test async plan creation."""
    print("=== Testing Async Plan Creation ===\n")

    planner = PlannerAgent()

    plan = await planner.acreate_plan(
        objective="Migrate monolith to microservices architecture",
        context="Current monolith has 500k lines of code, serves 1M daily users",
    )

    print(f"Objective: {plan.objective}\n")
    print(f"Total Steps: {plan.total_steps}\n")

    # Show first 5 steps
    print("First 5 steps:")
    for i, step in enumerate(plan.steps[:5], 1):
        print(f"{i}. {step.objective}")

    if len(plan.steps) > 5:
        print(f"... and {len(plan.steps) - 5} more steps")

    print("\n" + "=" * 50 + "\n")
    return plan


def main():
    """Run all tests."""
    print("Testing PlannerAgent Implementation\n")
    print("=" * 50 + "\n")

    # Test 1: Basic plan
    plan1 = test_basic_plan()

    # Test 2: Detailed plan with requirements
    plan2 = test_detailed_plan()

    # Test 3: No context
    plan3 = test_no_context()

    # Test 4: Async
    plan4 = asyncio.run(test_async_plan())

    print("All tests completed!")

    # Show computed properties
    print("\nComputed Properties Example (from first plan):")
    print(f"Current step: {plan1.current_step}")
    print(f"Completed steps: {len(plan1.completed_steps)}")
    print(f"Remaining steps: {len(plan1.steps_remaining)}")
    print(f"Has failures: {plan1.has_failures}")
    print(f"Is complete: {plan1.is_complete}")


if __name__ == "__main__":
    main()
