"""Demonstrate the planner agent output structure."""

from haive.agents.planning_v2.base.models import Plan, Status, Task
from haive.agents.planning_v2.base.planner.prompts import PLANNER_SYSTEM_MESSAGE


def show_prompt_details():
    """Show details about the comprehensive prompt."""
    print("=== PLANNER PROMPT DETAILS ===\n")

    lines = PLANNER_SYSTEM_MESSAGE.split("\n")
    print(
        f"System message: {len(lines)} lines, {len(PLANNER_SYSTEM_MESSAGE)} characters\n"
    )

    # Count sections
    sections = [line for line in lines if line.startswith("##")]
    print(f"Major sections ({len(sections)}):")
    for section in sections[:10]:
        print(f"  {section}")
    if len(sections) > 10:
        print(f"  ... and {len(sections) - 10} more sections")

    # Show examples
    example_count = PLANNER_SYSTEM_MESSAGE.count("### Example")
    print(f"\nContains {example_count} detailed examples")

    print("\n" + "=" * 70 + "\n")


def show_example_output():
    """Show what the planner agent would produce."""
    print("=== EXAMPLE PLANNER OUTPUT ===\n")

    # Create example plan that agent would produce
    plan = Plan[Task](
        objective="Build a REST API for user management system with authentication, authorization, and CRUD operations"
    )

    # Add comprehensive steps like the agent would
    steps = [
        # Planning & Design Phase
        Task(objective="Analyze requirements and define API specifications"),
        Task(objective="Design database schema for users, roles, and permissions"),
        Task(objective="Create API documentation with OpenAPI/Swagger specification"),
        Task(objective="Set up project structure and development environment"),
        # Infrastructure Setup
        Task(objective="Initialize Git repository and set up branching strategy"),
        Task(objective="Configure development, staging, and production environments"),
        Task(objective="Set up CI/CD pipeline with automated testing"),
        Task(objective="Configure logging, monitoring, and error tracking systems"),
        # Core Development
        Task(objective="Implement database models and migrations"),
        Task(objective="Create user registration endpoint with email verification"),
        Task(objective="Implement login endpoint with JWT token generation"),
        Task(objective="Build password reset functionality with secure tokens"),
        Task(objective="Develop user profile CRUD endpoints"),
        Task(objective="Implement role-based access control (RBAC) system"),
        Task(objective="Create admin endpoints for user management"),
        # Security Implementation
        Task(objective="Implement input validation and sanitization"),
        Task(objective="Add rate limiting and DDoS protection"),
        Task(objective="Configure CORS and security headers"),
        Task(objective="Implement audit logging for security events"),
        Task(objective="Set up encryption for sensitive data"),
        # Testing Phase
        Task(objective="Write unit tests for all models and utilities"),
        Task(objective="Create integration tests for API endpoints"),
        Task(objective="Implement end-to-end tests for critical user flows"),
        Task(objective="Perform security penetration testing"),
        Task(objective="Conduct load testing and performance optimization"),
        # Documentation & Deployment
        Task(objective="Write comprehensive API documentation"),
        Task(objective="Create deployment guides and runbooks"),
        Task(objective="Deploy to staging environment for UAT"),
        Task(objective="Perform final security audit"),
        Task(objective="Deploy to production with rollback plan"),
        Task(objective="Monitor post-deployment metrics and logs"),
        # Post-Launch
        Task(objective="Set up automated backups and disaster recovery"),
        Task(objective="Configure alerts for system health and security"),
        Task(objective="Create maintenance and update procedures"),
        Task(objective="Document lessons learned and improvements"),
    ]

    # Add all steps to plan
    for step in steps:
        plan.add_step(step)

    # Display the plan
    print(f"Objective: {plan.objective}\n")
    print(f"Total Steps: {plan.total_steps}")
    print(f"Status: {plan.status.value}")
    print(f"Progress: {plan.progress_percentage:.1f}%\n")

    print("Detailed Steps:")
    current_phase = ""
    for i, step in enumerate(plan.steps, 1):
        # Group by phase
        if i <= 4:
            phase = "Planning & Design"
        elif i <= 8:
            phase = "Infrastructure Setup"
        elif i <= 16:
            phase = "Core Development"
        elif i <= 21:
            phase = "Security Implementation"
        elif i <= 26:
            phase = "Testing Phase"
        elif i <= 31:
            phase = "Documentation & Deployment"
        else:
            phase = "Post-Launch"

        if phase != current_phase:
            current_phase = phase
            print(f"\n{phase}:")

        print(f"  {i:2d}. {step.objective}")

    # Show computed properties
    print(f"\nComputed Properties:")
    print(
        f"  - Current Step: {plan.current_step.objective if plan.current_step else 'None'}"
    )
    print(f"  - Completed Count: {plan.completed_count}")
    print(f"  - Remaining Count: {plan.remaining_count}")
    print(f"  - Failed Steps: {len(plan.failed_steps)}")
    print(f"  - Is Complete: {plan.is_complete}")

    print("\n" + "=" * 70 + "\n")
    return plan


def show_agent_configuration():
    """Show how the PlannerAgent is configured."""
    print("=== PLANNER AGENT CONFIGURATION ===\n")

    print("PlannerAgent extends SimpleAgent with:")
    print("  - Temperature: 0.3 (low for consistent, focused planning)")
    print("  - Structured Output: Plan[Task] model")
    print("  - System Message: Comprehensive planning instructions")
    print("  - Prompt Template: Adaptive based on context presence")

    print("\nKey Methods:")
    print("  - create_plan(objective, context) -> Plan[Task]")
    print("  - create_detailed_plan(...) -> Plan[Task]")
    print("  - refine_plan(plan, feedback) -> Plan[Task]")
    print("  - create_subplan(...) -> Plan[Task]")

    print("\nPrompt Handling:")
    print("  - WITH context: Uses planner_prompt_with_context")
    print("  - WITHOUT context: Uses planner_prompt_no_context")

    print("\n" + "=" * 70 + "\n")


def main():
    """Run the demonstration."""
    print("\n" + "=" * 70)
    print("PLANNER AGENT OUTPUT DEMONSTRATION")
    print("=" * 70 + "\n")

    show_prompt_details()
    show_agent_configuration()
    plan = show_example_output()

    # Simulate marking some complete
    print("=== SIMULATING EXECUTION ===\n")

    # Mark first 5 as complete
    for i in range(5):
        plan.steps[i].status = Status.COMPLETED
        plan.steps[i].result = "Successfully completed"

    # Mark current as in progress
    plan.steps[5].status = Status.IN_PROGRESS

    print(f"After completing first 5 steps:")
    print(f"  Progress: {plan.progress_percentage:.1f}%")
    print(f"  Current: {plan.current_step.objective if plan.current_step else 'None'}")
    print(f"  Completed: {plan.completed_count}/{plan.total_steps}")

    # Show completed steps
    print(f"\nCompleted Steps:")
    for step in plan.completed_steps:
        print(f"  ✓ {step.objective}")

    print("\n" + "=" * 70)
    print("This demonstrates the structured output the PlannerAgent produces")
    print("when given an objective. The actual LLM would generate similar")
    print("comprehensive, well-structured plans based on the 368-line prompt.")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
