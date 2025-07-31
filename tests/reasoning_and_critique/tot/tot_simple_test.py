"""Simple test of TOT implementation without persistence."""

import asyncio

from haive.agents.reasoning_and_critique.tot.agents.candidate_generator import (
    CandidateGenerator,
)
from haive.agents.reasoning_and_critique.tot.agents.solution_scorer import (
    SolutionScorer,
)


async def test_tot_components():
    """Test TOT components individually."""
    # Test 1: Candidate Generator

    generator = CandidateGenerator(name="test_generator", temperature=0.7)

    try:
        # Simple test - generate candidates for a math problem
        generation_result = await generator.generate_candidates(
            problem="Find two numbers that multiply to 20", num_candidates=4
        )

        for _i, _candidate in enumerate(generation_result.candidates, 1):
            pass
    except Exception:
        pass

    # Test 2: Solution Scorer

    scorer = SolutionScorer(name="test_scorer", temperature=0.3)

    # Use some candidate solutions
    test_candidates = [
        "4 * 5 = 20",
        "2 * 10 = 20",
        "3 * 7 = 21",  # Wrong
        "20 * 1 = 20",
    ]

    try:
        scoring_result = await scorer.score_solutions(
            problem="Find two numbers that multiply to 20", candidates=test_candidates
        )

        for scored in scoring_result.scored_solutions:
            pass

    except Exception:
        pass

    # Test 3: Combined workflow (without EnhancedMultiAgentV4)

    problem = "Use the numbers 2, 3, 4, 5 to make 24 using +, -, *, /"

    try:
        # Generate candidates
        generation = await generator.generate_candidates(problem, num_candidates=5)

        # Score them
        scoring = await scorer.score_solutions(problem, generation.candidates)

        # Find best solution
        best_score = 0.0
        for scored in scoring.scored_solutions:
            best_score = max(best_score, scored.score)

    except Exception:
        pass


if __name__ == "__main__":
    # Disable persistence by setting environment variable
    import os

    os.environ["HAIVE_PERSISTENCE_DISABLED"] = "true"

    asyncio.run(test_tot_components())
