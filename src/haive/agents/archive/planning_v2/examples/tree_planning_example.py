"""Example of using tree-based planning with the new tree_leaf structure."""

from haive.agents.planning_v2 import (
    PlanContent,
    PlanStatus,
    TaskPlan,
    create_phased_plan,
    create_simple_plan,
)


def example_simple_plan():
    """Create a simple linear plan."""
    print("=== Simple Linear Plan ===")

    plan = create_simple_plan(
        "Complete Feature X", ["Write code", "Write tests", "Code review", "Deploy"]
    )

    print(plan.to_markdown())
    print(f"\nTotal tasks: {plan.total_nodes}")
    print(f"Progress: {plan.progress_percentage:.1f}%")


def example_hierarchical_plan():
    """Create a hierarchical plan with sub-plans."""
    print("\n=== Hierarchical Plan ===")

    # Create main plan
    project = TaskPlan(
        content=PlanContent(
            objective="Launch New Product",
            description="Q1 2024 Product Launch",
            priority=5,
        )
    )

    # Add development phase
    dev_phase = project.add_subplan(
        "Development Phase", "Build core features", priority=5
    )
    dev_phase.add_task("Design architecture", priority=5)
    dev_phase.add_task("Implement backend", priority=4)
    dev_phase.add_task("Implement frontend", priority=4)
    dev_phase.add_task("Integration testing", priority=5)

    # Add deployment phase with nested structure
    deploy_phase = project.add_subplan(
        "Deployment Phase", "Roll out to production", priority=4
    )

    # Staging sub-phase
    staging = deploy_phase.add_subplan("Staging Deployment")
    staging.add_task("Deploy to staging")
    staging.add_task("Run smoke tests")
    staging.add_task("Performance testing")

    # Production sub-phase
    prod = deploy_phase.add_subplan("Production Deployment")
    prod.add_task("Deploy to prod-east")
    prod.add_task("Deploy to prod-west")
    prod.add_task("Verify deployment")

    # Add marketing phase
    marketing = project.add_subplan("Marketing Phase", "Launch campaign", priority=3)
    marketing.add_task("Create launch materials")
    marketing.add_task("Schedule social media")
    marketing.add_task("Send newsletter")

    print(project.to_markdown())
    print(f"\nTotal tasks: {project.total_nodes}")
    print(f"Tree height: {project.height}")


def example_phased_plan():
    """Create a plan using the phased helper."""
    print("\n=== Phased Plan ===")

    plan = create_phased_plan(
        "Website Redesign",
        {
            "Research": [
                "User interviews",
                "Competitor analysis",
                "Requirements gathering",
            ],
            "Design": ["Wireframes", "Mockups", "Design review", "Finalize designs"],
            "Implementation": ["Frontend dev", "Backend dev", "Testing", "Bug fixes"],
            "Launch": ["Deploy staging", "UAT", "Deploy production", "Monitor"],
        },
    )

    print(plan.to_markdown())


def example_parallel_tasks():
    """Create a plan with parallel task execution."""
    print("\n=== Parallel Tasks Plan ===")

    plan = TaskPlan(content=PlanContent(objective="Process Data Pipeline", priority=4))

    # Sequential setup
    plan.add_task("Download raw data", priority=5)
    plan.add_task("Validate data format", priority=4)

    # Parallel processing
    parallel_tasks = [
        ("Process dataset A", 3),
        ("Process dataset B", 3),
        ("Process dataset C", 3),
    ]
    plan.add_parallel_tasks(parallel_tasks)

    # Sequential cleanup
    plan.add_task("Merge results", priority=4)
    plan.add_task("Generate report", priority=3)

    print(plan.to_markdown())
    print("\nParallel tasks have same parent index for concurrent execution")


def example_plan_execution():
    """Simulate plan execution with status updates."""
    print("\n=== Plan Execution Simulation ===")

    plan = TaskPlan(content=PlanContent(objective="Deploy Feature"))
    plan.add_task("Run tests", priority=5)
    plan.add_task("Build artifacts", priority=4)
    plan.add_task("Deploy", priority=5)
    plan.add_task("Verify", priority=4)

    print("Initial state:")
    print(plan.to_markdown())

    # Simulate execution
    steps = []

    # Step 1: Start first task
    current = plan.get_current_task()
    if current:
        current.content.status = PlanStatus.IN_PROGRESS
        steps.append(f"\n1. Started: {current.content.objective}")

    # Step 2: Complete first task
    plan.mark_current_completed("All tests passed")
    steps.append("2. Completed: Run tests")

    # Step 3: Start and complete second task
    current = plan.get_current_task()
    if current:
        current.content.status = PlanStatus.IN_PROGRESS
        steps.append(f"3. Started: {current.content.objective}")
        plan.mark_current_completed("Build successful")
        steps.append("4. Completed: Build artifacts")

    # Step 4: Third task fails
    current = plan.get_current_task()
    if current:
        current.content.status = PlanStatus.IN_PROGRESS
        steps.append(f"5. Started: {current.content.objective}")
        plan.mark_current_failed("Connection timeout")
        steps.append("6. Failed: Deploy")

    # Show execution log
    print("\nExecution steps:")
    for step in steps:
        print(step)

    # Show final state
    print("\nFinal state:")
    print(plan.to_markdown())
    print(f"\nProgress: {plan.progress_percentage:.1f}%")
    print(f"Has failures: {plan.has_failures}")


def example_priority_filtering():
    """Example of working with task priorities."""
    print("\n=== Priority-Based Task Management ===")

    plan = TaskPlan(content=PlanContent(objective="Sprint Tasks"))

    # Add tasks with different priorities
    plan.add_task("Fix critical bug", priority=5)
    plan.add_task("Implement new feature", priority=3)
    plan.add_task("Update documentation", priority=2)
    plan.add_task("Refactor old code", priority=1)

    # Add high-priority sub-plan
    urgent = plan.add_subplan("Urgent fixes", priority=5)
    urgent.add_task("Fix security issue", priority=5)
    urgent.add_task("Fix data corruption", priority=5)

    print("All tasks:")
    print(plan.to_markdown())

    # Get high-priority tasks
    high_priority = plan.get_tasks_by_priority(min_priority=4)
    print(f"\nHigh priority tasks (priority >= 4): {len(high_priority)}")
    for task in high_priority:
        print(f"  - {task.content.objective} (priority: {task.content.priority})")


def example_tree_navigation():
    """Example of navigating the tree structure."""
    print("\n=== Tree Navigation ===")

    plan = TaskPlan(content=PlanContent(objective="Main Project"))

    # Build structure
    phase1 = plan.add_subplan("Phase 1")
    task1 = phase1.add_task("Task 1.1")
    task2 = phase1.add_task("Task 1.2")

    phase2 = plan.add_subplan("Phase 2")
    task3 = phase2.add_task("Task 2.1")

    # Navigate by path
    found = plan.find_by_path(0, 1)  # First child's second child
    if found:
        print(f"Found by path [0,1]: {found.content.objective}")

    # Access node IDs
    print("\nNode IDs:")
    print(f"  Phase 1: {phase1.node_id}")
    print(f"  Task 1.1: {task1.node_id}")
    print(f"  Task 1.2: {task2.node_id}")
    print(f"  Phase 2: {phase2.node_id}")
    print(f"  Task 2.1: {task3.node_id}")

    # Tree metrics
    print("\nTree metrics:")
    print(f"  Total nodes: {plan.total_nodes}")
    print(f"  Tree height: {plan.height}")
    print(f"  Direct children: {plan.child_count}")
    print(f"  All descendants: {plan.descendant_count}")


if __name__ == "__main__":
    example_simple_plan()
    example_hierarchical_plan()
    example_phased_plan()
    example_parallel_tasks()
    example_plan_execution()
    example_priority_filtering()
    example_tree_navigation()
