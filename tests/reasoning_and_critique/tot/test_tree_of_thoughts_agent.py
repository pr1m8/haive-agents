"""Test Tree of Thoughts Agent with LangGraph routing and conditional edges."""

import asyncio
import os

import pytest


# Disable persistence for testing
os.environ["HAIVE_PERSISTENCE_DISABLED"] = "true"

from haive.agents.reasoning_and_critique.tot.tree_of_thoughts_agent import (
    create_tree_of_thoughts_agent,
)


@pytest.mark.asyncio
async def test_tree_of_thoughts_agent_creation():
    """Test that TreeOfThoughtsAgent can be created successfully."""
    agent = create_tree_of_thoughts_agent(
        beam_size=3,
        max_iterations=2,
        generation_temperature=0.7,
        scoring_temperature=0.3,
    )

    assert agent.name == "tree_of_thoughts"
    assert agent.beam_size == 3
    assert agent.max_iterations == 2
    assert "generator" in agent.agents
    assert "scorer" in agent.agents


@pytest.mark.asyncio
async def test_tree_of_thoughts_solve_simple_math():
    """Test TOT agent solving a simple math problem."""
    agent = create_tree_of_thoughts_agent(
        beam_size=2,
        max_iterations=2,
        generation_temperature=0.5,
        scoring_temperature=0.1,
    )

    problem = "Find three positive integers that sum to 15"

    result = await agent.solve_problem(problem)

    # Verify result structure
    assert "solution" in result
    assert "score" in result
    assert "reasoning" in result
    assert isinstance(result["score"], int | float)
    assert result["score"] >= 0.0

    # Verify solution is not empty
    assert len(result["solution"]) > 0


@pytest.mark.asyncio
async def test_tree_of_thoughts_game_of_24():
    """Test TOT agent on Game of 24 problem."""
    agent = create_tree_of_thoughts_agent(
        beam_size=3,
        max_iterations=2,
        generation_temperature=0.8,
        scoring_temperature=0.2,
    )

    problem = "Use the numbers 2, 3, 4, 6 with operations +, -, *, / to make 24. Each number must be used exactly once."

    result = await agent.solve_problem(problem)

    # Verify result
    assert "solution" in result
    assert "score" in result
    assert isinstance(result["score"], int | float)


@pytest.mark.asyncio
async def test_tree_of_thoughts_conditional_routing():
    """Test that TOT uses conditional routing correctly."""
    agent = create_tree_of_thoughts_agent(
        beam_size=2,
        max_iterations=1,  # Short test
    )

    # Mock state to test routing logic
    from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState

    # Test should_continue logic
    state_continue = MultiAgentState(
        tot_iteration={
            "iteration_number": 0,
            "max_iterations": 2,
            "scores": [0.5, 0.6],  # No perfect score
        }
    )

    result = agent.should_continue(state_continue)
    assert result == "continue"

    # Test finish condition (high score)
    state_finish = MultiAgentState(
        tot_iteration={
            "iteration_number": 1,
            "max_iterations": 2,
            "scores": [0.98, 0.95],  # Perfect score
        }
    )

    result = agent.should_continue(state_finish)
    assert result == "finish"


@pytest.mark.asyncio
async def test_tree_of_thoughts_beam_search():
    """Test that TOT properly implements beam search with top-k selection."""
    agent = create_tree_of_thoughts_agent(beam_size=3)

    # Test with a problem that should generate diverse candidates
    problem = "Design a simple two-player game that can be played with just pencil and paper"

    result = await agent.solve_problem(problem)

    # Verify beam search results
    assert "final_beam_size" in result
    assert result["final_beam_size"] <= 3  # Should respect beam size
    assert result["final_beam_size"] >= 1  # Should have at least one solution


if __name__ == "__main__":
    # Run tests directly
    async def run_tests():
        await test_tree_of_thoughts_agent_creation()

        await test_tree_of_thoughts_solve_simple_math()

        await test_tree_of_thoughts_game_of_24()

        await test_tree_of_thoughts_conditional_routing()

        await test_tree_of_thoughts_beam_search()

    asyncio.run(run_tests())
