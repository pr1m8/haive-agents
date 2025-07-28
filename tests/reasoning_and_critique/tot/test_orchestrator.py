"""Test the Tree of Thoughts Orchestrator with EnhancedMultiAgentV4."""

import asyncio
import pytest
from typing import List

from haive.agents.reasoning_and_critique.tot.orchestrator import (
    TreeOfThoughtsOrchestrator,
    TOTResult,
    create_tot_solver
)
from haive.core.engine.aug_llm import AugLLMConfig


class TestTreeOfThoughtsOrchestrator:
    """Test suite for the TOT Orchestrator."""
    
    @pytest.mark.asyncio
    async def test_basic_tot_solving(self):
        """Test basic TOT problem solving."""
        orchestrator = TreeOfThoughtsOrchestrator(
            name="test_tot",
            beam_width=3,
            max_iterations=2,
            temperature_generate=0.7,
            temperature_score=0.3
        )
        
        problem = "Find three positive integers that sum to 15"
        
        result = await orchestrator.solve(problem)
        
        # Verify result structure
        assert isinstance(result, TOTResult)
        assert isinstance(result.best_solution, str)
        assert 0.0 <= result.score <= 1.0
        assert result.iterations > 0
        assert isinstance(result.all_solutions, list)
        
        # Should find at least one solution
        assert result.score > 0.5, f"Should find valid solution, got: {result.best_solution}"
        
        print(f"\nBest solution: {result.best_solution}")
        print(f"Score: {result.score}")
        print(f"Reasoning: {result.reasoning}")
        print(f"Explored {len(result.all_solutions)} total solutions")
    
    @pytest.mark.asyncio
    async def test_game_of_24(self):
        """Test solving Game of 24 with TOT."""
        orchestrator = await create_tot_solver(
            beam_width=5,
            max_iterations=3,
            temperature_generate=0.8
        )
        
        problem = "Use the numbers 3, 3, 8, 8 with operations +, -, *, / to make 24. Each number must be used exactly once."
        
        result = await orchestrator.solve(
            problem,
            initial_seed="Try combining the numbers in different ways"
        )
        
        print(f"\nGame of 24 result:")
        print(f"Best: {result.best_solution} (score: {result.score})")
        print(f"Iterations: {result.iterations}")
        
        # Check if a valid solution was found
        # The correct answer is 8 / (3 - 8/3) = 24
        assert result.score > 0.0, "Should find at least partial solutions"
        
        # Print top solutions
        if result.all_solutions:
            print("\nTop solutions explored:")
            sorted_solutions = sorted(
                result.all_solutions,
                key=lambda x: x['score'],
                reverse=True
            )[:5]
            for sol in sorted_solutions:
                print(f"  - {sol['solution']} (score: {sol['score']:.2f})")
    
    @pytest.mark.asyncio
    async def test_creative_problem(self):
        """Test TOT on a creative problem."""
        orchestrator = TreeOfThoughtsOrchestrator(
            name="creative_tot",
            beam_width=4,
            max_iterations=2
        )
        
        problem = "Design a simple game that can be played with just pencil and paper"
        
        result = await orchestrator.solve(
            problem,
            context="The game should be fun for 2 players and take about 5 minutes"
        )
        
        assert result.best_solution
        assert len(result.all_solutions) > 0
        
        print(f"\nCreative problem result:")
        print(f"Best game idea: {result.best_solution}")
        print(f"Score: {result.score}")
        print(f"Total ideas generated: {len(result.all_solutions)}")
    
    @pytest.mark.asyncio
    async def test_early_termination(self):
        """Test that TOT terminates early on excellent solutions."""
        orchestrator = TreeOfThoughtsOrchestrator(
            name="early_term_tot",
            beam_width=3,
            max_iterations=5  # Set high, but should terminate early
        )
        
        # Simple problem that should find perfect solution quickly
        problem = "What is 2 + 2?"
        
        result = await orchestrator.solve(problem)
        
        # Should terminate early (not use all 5 iterations)
        assert result.iterations < 5, "Should terminate early on simple problem"
        assert result.score > 0.9, "Should find near-perfect solution"
        assert "4" in result.best_solution
    
    @pytest.mark.asyncio
    async def test_with_initial_seed(self):
        """Test TOT with an initial seed solution."""
        orchestrator = TreeOfThoughtsOrchestrator(
            name="seeded_tot",
            beam_width=3,
            max_iterations=2
        )
        
        problem = "Write a haiku about programming"
        initial_seed = "Code flows like water / ??? / ???"
        
        result = await orchestrator.solve(
            problem,
            initial_seed=initial_seed
        )
        
        assert result.best_solution
        assert len(result.all_solutions) > 0
        
        print(f"\nHaiku result:")
        print(f"Best haiku:\n{result.best_solution}")
        print(f"Score: {result.score}")


# Run tests if executed directly
if __name__ == "__main__":
    async def run_tests():
        """Run all orchestrator tests."""
        test = TestTreeOfThoughtsOrchestrator()
        
        print("Testing basic TOT solving...")
        await test.test_basic_tot_solving()
        print("✓ Basic TOT test passed")
        
        print("\nTesting Game of 24...")
        await test.test_game_of_24()
        print("✓ Game of 24 test passed")
        
        print("\nTesting creative problem...")
        await test.test_creative_problem()
        print("✓ Creative problem test passed")
        
        print("\nTesting early termination...")
        await test.test_early_termination()
        print("✓ Early termination test passed")
        
        print("\nTesting with initial seed...")
        await test.test_with_initial_seed()
        print("✓ Seeded TOT test passed")
        
        print("\n✨ All orchestrator tests passed!")
    
    asyncio.run(run_tests())