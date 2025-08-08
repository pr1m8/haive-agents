"""Test the planner agent structure without LLM calls."""

from haive.agents.planning_v2 import (
    Plan,
    PlannerAgent,
    Status,
    Task,
)
from haive.agents.planning_v2.base.planner.prompts import (
    planner_prompt_no_context,
    planner_prompt_with_context,
)


def test_agent_structure():
    """Test agent creation and structure."""
    print("=== Testing PlannerAgent Structure ===\n")

    # Create planner
    planner = PlannerAgent()

    print(f"Agent name: {planner.name}")
    print(f"Engine temperature: {planner.engine.temperature}")
    print(f"Structured output model: {planner.engine.structured_output_model}")
    print(f"Prompt template type: {type(planner.prompt_template)}")

    # Show that engine has Plan[Task] as structured output
    print(
        f"\nStructured output is Plan[Task]: {planner.engine.structured_output_model == Plan[Task]}"
    )

    print("\n" + "=" * 50 + "\n")


def test_plan_model():
    """Test the Plan model structure."""
    print("=== Testing Plan Model ===\n")

    # Create a plan manually
    plan = Plan[Task](objective="Build a REST API for user management")

    # Add some tasks
    plan.add_step(Task(objective="Set up project structure"))
    plan.add_step(Task(objective="Design database schema"))
    plan.add_step(Task(objective="Implement user model"))
    plan.add_step(Task(objective="Create CRUD endpoints"))
    plan.add_step(Task(objective="Add authentication"))
    plan.add_step(Task(objective="Write tests"))
    plan.add_step(Task(objective="Deploy to staging"))

    print(f"Plan objective: {plan.objective}")
    print(f"Status: {plan.status}")
    print(f"Total steps: {plan.total_steps}")
    print(f"Progress: {plan.progress_percentage:.1f}%")

    print("\nSteps:")
    for i, step in enumerate(plan.steps, 1):
        print(f"  {i}. {step.objective} [{step.status.value}]")

    # Mark some as complete
    plan.steps[0].status = Status.COMPLETED
    plan.steps[1].status = Status.COMPLETED
    plan.steps[2].status = Status.IN_PROGRESS

    print("\nAfter marking some complete:")
    print(f"  Completed: {plan.completed_count}")
    print(f"  Remaining: {plan.remaining_count}")
    print(f"  Progress: {plan.progress_percentage:.1f}%")
    print(
        f"  Current step: {plan.current_step.objective if plan.current_step else None}"
    )

    print("\n" + "=" * 50 + "\n")


def test_nested_plan():
    """Test nested plan structure."""
    print("=== Testing Nested Plan ===\n")

    # Create main plan
    main_plan = Plan[Task](objective="Launch e-commerce website")

    # Create sub-plan for backend
    backend_plan = main_plan.create_subplan("Develop backend services")
    backend_plan.add_step(Task(objective="Set up database"))
    backend_plan.add_step(Task(objective="Create API endpoints"))
    backend_plan.add_step(Task(objective="Implement business logic"))

    # Create sub-plan for frontend
    frontend_plan = main_plan.create_subplan("Build frontend application")
    frontend_plan.add_step(Task(objective="Design UI/UX"))
    frontend_plan.add_step(Task(objective="Implement components"))
    frontend_plan.add_step(Task(objective="Add state management"))

    # Add some direct tasks
    main_plan.add_step(Task(objective="Deploy to production"))
    main_plan.add_step(Task(objective="Monitor and optimize"))

    print(f"Main plan: {main_plan.objective}")
    print(f"Total steps (including nested): {main_plan.total_steps}")

    print("\nStructure:")
    for i, step in enumerate(main_plan.steps, 1):
        if isinstance(step, Plan):
            print(f"  {i}. [SUBPLAN] {step.objective}")
            for j, substep in enumerate(step.steps, 1):
                print(f"     {i}.{j}. {substep.objective}")
        else:
            print(f"  {i}. {step.objective}")

    print("\n" + "=" * 50 + "\n")


def test_prompts():
    """Test prompt templates."""
    print("=== Testing Prompt Templates ===\n")

    # Test with context
    print("Prompt WITH context:")
    messages_with = planner_prompt_with_context.format_messages(
        objective="Deploy new feature",
        context="Production environment with high traffic",
    )
    print(f"Number of messages: {len(messages_with)}")
    print(f"System message length: {len(messages_with[0].content)} chars")
    print(f"User message preview: {messages_with[1].content[:200]}...")

    print("\nPrompt WITHOUT context:")
    messages_without = planner_prompt_no_context.format_messages(
        objective="Deploy new feature"
    )
    print(f"Number of messages: {len(messages_without)}")
    print(f"System message length: {len(messages_without[0].content)} chars")
    print(f"User message preview: {messages_without[1].content[:200]}...")

    print("\n" + "=" * 50 + "\n")


def test_parallel_steps():
    """Test parallel step creation."""
    print("=== Testing Parallel Steps ===\n")

    plan = Plan[Task](objective="Process data pipeline")

    # Sequential steps
    plan.add_step(Task(objective="Download data"))
    plan.add_step(Task(objective="Validate format"))

    # Parallel steps
    parallel_tasks = [
        Task(objective="Process dataset A"),
        Task(objective="Process dataset B"),
        Task(objective="Process dataset C"),
    ]
    plan.add_parallel_steps(parallel_tasks)

    # More sequential
    plan.add_step(Task(objective="Merge results"))
    plan.add_step(Task(objective="Generate report"))

    print(f"Plan: {plan.objective}")
    print(f"Total steps: {plan.total_steps}")

    print("\nStep indices (parallel have same parent):")
    for step in plan.steps:
        print(f"  {step.objective}")
        print(f"    Index: {step._index}, Parent: {step._parent_index}")

    print("\n" + "=" * 50 + "\n")


def main():
    """Run all structure tests."""
    print("\nTesting PlannerAgent Structure (No LLM Calls)\n")
    print("=" * 50 + "\n")

    test_agent_structure()
    test_plan_model()
    test_nested_plan()
    test_prompts()
    test_parallel_steps()

    print("All structure tests completed!")

    # Show example of what the agent would produce
    print("\n=== Example Output Structure ===\n")
    print("When called with objective 'Build REST API', the agent would return:")
    print("A Plan[Task] object with fields like:")
    print("- objective: 'Build REST API for user management'")
    print("- status: Status.PENDING")
    print("- steps: List[Task] with each task having:")
    print("  - objective: 'Set up project structure'")
    print("  - status: Status.PENDING")
    print("  - result: None")
    print(
        "\nThe system message is {} lines with detailed planning instructions.".format(
            len(planner_prompt_with_context.messages[0].prompt.template.split("\n"))
        )
    )


if __name__ == "__main__":
    main()
