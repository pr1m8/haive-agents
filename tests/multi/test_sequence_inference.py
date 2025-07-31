#!/usr/bin/env python3
"""Test sequence inference and branching in MultiAgent."""

import asyncio

# Create a simple calculator tool for testing
from langchain_core.tools import tool

from haive.agents.multi.clean import MultiAgent
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"


async def test_sequence_inference():
    """Test automatic sequence inference from agent naming patterns."""
    # Create agents with clear naming patterns
    planner = SimpleAgent(
        name="planner",
        engine=AugLLMConfig(
            prompt_template="Create a plan for: {input}", temperature=0.7
        ),
    )

    executor = SimpleAgent(
        name="executor",
        engine=AugLLMConfig(
            prompt_template="Execute this plan: {input}", temperature=0.3
        ),
    )

    reviewer = SimpleAgent(
        name="reviewer",
        engine=AugLLMConfig(
            prompt_template="Review the execution: {input}", temperature=0.1
        ),
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


async def test_agent_type_inference():
    """Test sequence inference from agent types."""
    # Create agents with different types
    simple_agent = SimpleAgent(
        name="processor",
        engine=AugLLMConfig(prompt_template="Process: {input}", temperature=0.5),
    )

    react_agent = ReactAgent(
        name="reasoner",
        engine=AugLLMConfig(prompt_template="Reason about: {input}", temperature=0.7),
        tools=[calculator],
    )

    # Create multi-agent
    multi_agent = MultiAgent.create(
        agents=[simple_agent, react_agent],  # SimpleAgent first
        name="type_inference_test",
        execution_mode="infer",
    )

    # Test type-based inference
    sequence = multi_agent._infer_agent_sequence()

    # Should be: ReactAgent -> SimpleAgent (reasoning before processing)
    assert sequence[0] == "reasoner", f"Expected reasoner first, got {sequence[0]}"
    assert sequence[1] == "processor", f"Expected processor second, got {sequence[1]}"

    return sequence


async def test_branch_configuration():
    """Test branch configuration and routing."""
    # Create agents for branching
    analyzer = SimpleAgent(
        name="analyzer",
        engine=AugLLMConfig(prompt_template="Analyze: {input}", temperature=0.3),
    )

    success_handler = SimpleAgent(
        name="success_handler",
        engine=AugLLMConfig(prompt_template="Handle success: {input}", temperature=0.2),
    )

    error_handler = SimpleAgent(
        name="error_handler",
        engine=AugLLMConfig(prompt_template="Handle error: {input}", temperature=0.1),
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

    # Test graph building
    graph = multi_agent.build_graph()

    assert "analyzer" in graph.nodes
    assert "success_handler" in graph.nodes
    assert "error_handler" in graph.nodes

    return multi_agent


async def test_manual_sequence_override():
    """Test manual sequence setting."""
    # Create agents
    step1 = SimpleAgent(
        name="step1", engine=AugLLMConfig(prompt_template="Step 1: {input}")
    )
    step2 = SimpleAgent(
        name="step2", engine=AugLLMConfig(prompt_template="Step 2: {input}")
    )
    step3 = SimpleAgent(
        name="step3", engine=AugLLMConfig(prompt_template="Step 3: {input}")
    )

    # Create multi-agent
    multi_agent = MultiAgent.create(
        agents=[step3, step1, step2], name="manual_sequence_test"  # Out of order
    )

    # Set manual sequence
    multi_agent.set_sequence(["step1", "step2", "step3"])

    # Should be in the set order
    agent_names = list(multi_agent.agents.keys())
    assert agent_names[:3] == ["step1", "step2", "step3"]
    assert multi_agent.execution_mode == "sequential"
    assert not multi_agent.infer_sequence

    return multi_agent


async def test_plan_and_execute_inference():
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


async def main():
    """Run all sequence inference and branching tests."""
    try:
        # Test 1: Naming pattern inference
        await test_sequence_inference()

        # Test 2: Agent type inference
        await test_agent_type_inference()

        # Test 3: Branch configuration
        await test_branch_configuration()

        # Test 4: Manual sequence override
        await test_manual_sequence_override()

        # Test 5: Plan and Execute inference
        await test_plan_and_execute_inference()

    except Exception:
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
