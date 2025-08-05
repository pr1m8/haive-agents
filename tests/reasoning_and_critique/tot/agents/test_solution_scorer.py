"""Test the Solution Scorer agent for Tree of Thoughts."""

import asyncio

import pytest

from haive.agents.reasoning_and_critique.tot.agents.solution_scorer import (
    SolutionScorer,
    SolutionScoring,
)


class TestSolutionScorer:
    """Test suite for the Solution Scorer agent."""

    @pytest.mark.asyncio
    async def test_score_math_solutions(self):
        """Test scoring math problem solutions."""
        scorer = SolutionScorer(
            name="math_scorer",
            temperature=0.3,  # Consistent scoring
        )

        problem = "Find three numbers that sum to 24"
        candidates = [
            "7 + 8 + 9 = 24",
            "10 + 10 + 4 = 24",
            "1 + 2 + 3 = 6 (incorrect)",
            "6 + 6 + 6 + 6 = 24",
            "20 + 2 + 2 = 24",
        ]

        scoring = await scorer.score_solutions(problem, candidates)

        # Verify structured output
        assert isinstance(scoring, SolutionScoring)
        assert len(scoring.scored_solutions) == len(candidates)

        # Check that correct solutions get higher scores
        for scored in scoring.scored_solutions:
            if "incorrect" in scored.solution or "= 6" in scored.solution:
                assert scored.score < 0.5, (
                    f"Incorrect solution should have low score: {scored.solution}"
                )
            elif "6 + 6 + 6 + 6" in scored.solution:
                # This uses 4 numbers instead of 3
                assert scored.score < 0.8, (
                    f"Solution with wrong number count should not be perfect: {scored.solution}"
                )
            else:
                # Correct solutions
                assert scored.score > 0.7, (
                    f"Correct solution should have high score: {scored.solution}"
                )

    @pytest.mark.asyncio
    async def test_score_game_of_24_solutions(self):
        """Test scoring Game of 24 solutions."""
        scorer = SolutionScorer(name="game24_scorer")

        problem = "Use the numbers 4, 5, 6, 7 with operations +, -, *, / to make 24"
        candidates = [
            "(7 - 5) * (6 + 4) = 2 * 10 = 20",  # Wrong answer
            "6 * 4 * (7 - 5) = 24 * 2 = 48",  # Wrong answer
            "(5 + 7) * (6 - 4) = 12 * 2 = 24",  # Correct!
            "4 * 6 + 7 - 5 = 24 + 2 = 26",  # Wrong answer
            "(7 - 4) * (6 + 5) = 3 * 11 = 33",  # Wrong answer
        ]

        scoring = await scorer.score_solutions(problem, candidates)

        # Find the correct solution
        correct_idx = 2  # We know the 3rd candidate is correct
        correct_score = scoring.scored_solutions[correct_idx].score

        # Verify correct solution has highest score
        for i, scored in enumerate(scoring.scored_solutions):
            if i != correct_idx:
                assert scored.score < correct_score, (
                    f"Incorrect solution scored higher than correct one: "
                    f"{scored.solution} (score: {scored.score})"
                )

    @pytest.mark.asyncio
    async def test_get_best_solutions(self):
        """Test getting top-k best solutions."""
        scorer = SolutionScorer(name="best_scorer")

        problem = "Find two numbers that multiply to 20"
        candidates = [
            "4 * 5 = 20",  # Correct
            "2 * 10 = 20",  # Correct
            "20 * 1 = 20",  # Correct but trivial
            "3 * 7 = 21",  # Wrong
            "6 * 3 = 18",  # Wrong
            "10 + 10 = 20",  # Wrong operation
        ]

        best_solutions = await scorer.get_best_solutions(problem, candidates, top_k=3)

        assert len(best_solutions) == 3

        # Check format
        for solution, score in best_solutions:
            assert isinstance(solution, str)
            assert isinstance(score, float)
            assert 0.0 <= score <= 1.0

        # Check ordering (descending by score)
        scores = [score for _, score in best_solutions]
        assert scores == sorted(scores, reverse=True)

    @pytest.mark.asyncio
    async def test_score_partial_solutions(self):
        """Test scoring partial/incomplete solutions."""
        scorer = SolutionScorer(name="partial_scorer")

        problem = "Write a Python function to calculate factorial"
        candidates = [
            "def factorial(n):\n    # TODO: implement",  # Incomplete
            "def factorial(n):\n    if n == 0:\n        return 1",  # Partial
            "def factorial(n):\n    if n == 0:\n        return 1\n    return n * factorial(n-1)",  # Complete
            "def fact(n):\n    result = 1\n    for i in range(1, n+1):\n        result *= i\n    return result",  # Complete, different approach
            "factorial = lambda n: 1 if n == 0 else n * factorial(n-1)",  # Complete, concise
        ]

        scoring = await scorer.score_solutions(problem, candidates)

        # Check that incomplete solutions are marked appropriately
        for scored in scoring.scored_solutions:
            if "TODO" in scored.solution:
                assert scored.score < 0.3
                assert not scored.is_complete
            elif (
                "if n == 0" in scored.solution
                and "return 1" in scored.solution
                and "factorial(n-1)" not in scored.solution
            ):
                # Partial solution
                assert 0.3 <= scored.score <= 0.7
                assert not scored.is_complete
            else:
                # Complete solutions
                assert scored.score > 0.7
                assert scored.is_complete


# Run tests if executed directly
if __name__ == "__main__":

    async def run_tests():
        """Run all tests."""
        test = TestSolutionScorer()

        await test.test_score_math_solutions()

        await test.test_score_game_of_24_solutions()

        await test.test_get_best_solutions()

        await test.test_score_partial_solutions()

    asyncio.run(run_tests())
