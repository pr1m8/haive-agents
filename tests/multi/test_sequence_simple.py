#!/usr/bin/env python3
"""Simple test for sequence inference and branching."""

from haive.agents.multi.clean import MultiAgent
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


def test_sequence_inference():
    """Test sequence inference synchronously."""
    # Create agents with clear naming patterns
    planner = SimpleAgent(
        name="planner",
        engine=AugLLMConfig(prompt_template="Create a plan for: {input}"),
    )

    executor = SimpleAgent(
        name="executor",
        engine=AugLLMConfig(prompt_template="Execute this plan: {input}"),
    )

    reviewer = SimpleAgent(
        name="reviewer",
        engine=AugLLMConfig(prompt_template="Review the execution: {input}"),
    )

    # Create multi-agent with inference (default mode)
    multi_agent = MultiAgent.create(
        agents=[executor, reviewer, planner],  # Intentionally out of order
        name="plan_execute_review",
        execution_mode="infer",
    )

    # Test sequence inference
    sequence = multi_agent._infer_agent_sequence()

    # Should be: planner -> executor -> reviewer
    assert sequence[0] == "planner", f"Expected planner first, got {sequence[0]}"
    assert sequence[1] == "executor", f"Expected executor second, got {sequence[1]}"
    assert sequence[2] == "reviewer", f"Expected reviewer third, got {sequence[2]}"

    return sequence


def test_branch_configuration():
    """Test branch configuration."""
    # Create agents for branching
    analyzer = SimpleAgent(name="analyzer", engine=AugLLMConfig(prompt_template="Analyze: {input}"))

    success_handler = SimpleAgent(
        name="success_handler",
        engine=AugLLMConfig(prompt_template="Handle success: {input}"),
    )

    error_handler = SimpleAgent(
        name="error_handler",
        engine=AugLLMConfig(prompt_template="Handle error: {input}"),
    )

    # Create multi-agent with branch mode
    multi_agent = MultiAgent.create(
        agents=[analyzer, success_handler, error_handler],
        name="branch_test",
        execution_mode="branch",
    )

    # Add branch configuration
    multi_agent.add_branch("analyzer", "if success", ["success_handler"])
    multi_agent.add_branch("analyzer", "if error", ["error_handler"])

    # Test graph building (without full setup)

    assert "analyzer" in multi_agent.agents
    assert "success_handler" in multi_agent.agents
    assert "error_handler" in multi_agent.agents

    return multi_agent


def test_plan_and_execute_inference():
    """Test that Plan and Execute gets proper sequence inference."""
    from haive.agents.planning.plan_and_execute.simple import PlanAndExecuteAgent

    # Create plan and execute agent
    agent = PlanAndExecuteAgent.create(name="inferred_planner")

    # Test the sequence inference
    sequence = agent._infer_agent_sequence()

    # Should be: planner -> executor -> replanner
    assert sequence[0] == "planner", f"Expected planner first, got {sequence[0]}"
    assert sequence[1] == "executor", f"Expected executor second, got {sequence[1]}"
    assert sequence[2] == "replanner", f"Expected replanner third, got {sequence[2]}"

    return agent


def main():
    """Run all tests synchronously."""
    try:
        # Test 1: Naming pattern inference
        test_sequence_inference()

        # Test 2: Branch configuration
        test_branch_configuration()

        # Test 3: Plan and Execute inference
        test_plan_and_execute_inference()

    except Exception:
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()
