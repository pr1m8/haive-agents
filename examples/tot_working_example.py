"""Working example of Tree of Thoughts without persistence issues."""

import asyncio
import os

# Disable persistence to avoid PostgreSQL issues
os.environ["HAIVE_PERSISTENCE_DISABLED"] = "true"

from haive.agents.reasoning_and_critique.tot.agents.candidate_generator import (
    CandidateGenerator,
)
from haive.agents.reasoning_and_critique.tot.agents.solution_scorer import (
    SolutionScorer,
)


async def demonstrate_tot():
    """Demonstrate Tree of Thoughts components working together."""
    print("🌳 Tree of Thoughts Demonstration\n")

    # Initialize agents
    generator = CandidateGenerator(name="tot_generator", temperature=0.7)
    scorer = SolutionScorer(name="tot_scorer", temperature=0.3)

    # Example 1: Simple Math Problem
    print("=" * 60)
    print("Example 1: Simple Math Problem")
    print("=" * 60)

    problem1 = "Find three positive integers that sum to 15"

    print(f"Problem: {problem1}\n")

    # Generate candidates
    print("Step 1: Generating candidate solutions...")
    gen_result = await generator.generate_candidates(problem1, num_candidates=5)

    print(f"Generated {len(gen_result.candidates)} candidates:")
    for i, candidate in enumerate(gen_result.candidates, 1):
        print(f"  {i}. {candidate}")

    print(f"\nDiversity check: {gen_result.diversity_check}\n")

    # Score candidates
    print("Step 2: Scoring candidate solutions...")
    score_result = await scorer.score_solutions(problem1, gen_result.candidates)

    print(f"Problem understanding: {score_result.problem_understanding}\n")

    print("Scores:")
    best_solution = None
    best_score = 0.0

    for scored in score_result.scored_solutions:
        print(f"  • {scored.solution}")
        print(
            f"    Score: {scored.score:.2f} | Complete: {scored.is_complete} | Has errors: {scored.has_errors}"
        )
        print(f"    Reasoning: {scored.reasoning}")
        print()

        if scored.score > best_score:
            best_score = scored.score
            best_solution = scored.solution

    print(f"🏆 Best solution: {best_solution} (score: {best_score:.2f})")
    print(f"Ranking rationale: {score_result.ranking_rationale}")

    # Example 2: Game of 24
    print("\n" + "=" * 60)
    print("Example 2: Game of 24")
    print("=" * 60)

    problem2 = "Use the numbers 2, 3, 4, 6 with operations +, -, *, / to make 24. Each number must be used exactly once."

    print(f"Problem: {problem2}\n")

    # Iteration 1
    print("Iteration 1: Initial candidates")
    print("-" * 40)

    candidates_1 = await generator.generate_candidates(problem2, num_candidates=5)
    print("Generated candidates:")
    for i, c in enumerate(candidates_1.candidates, 1):
        print(f"  {i}. {c}")

    scores_1 = await scorer.score_solutions(problem2, candidates_1.candidates)

    # Find top 3 for beam search
    scored_list = [(s.solution, s.score) for s in scores_1.scored_solutions]
    scored_list.sort(key=lambda x: x[1], reverse=True)
    top_candidates = [sol for sol, _ in scored_list[:3]]

    print(f"\nTop 3 solutions after iteration 1:")
    for i, (sol, score) in enumerate(scored_list[:3], 1):
        print(f"  {i}. {sol} (score: {score:.2f})")

    # Iteration 2: Expand from best
    print("\nIteration 2: Expanding from best solutions")
    print("-" * 40)

    expansion_prompt = f"Based on these approaches: {', '.join(top_candidates[:2])}, generate new variations"
    candidates_2 = await generator.expand_from_seed(
        problem2, seed=top_candidates[0], num_candidates=4
    )

    print("New candidates from expansion:")
    for i, c in enumerate(candidates_2.candidates, 1):
        print(f"  {i}. {c}")

    # Final scoring
    all_candidates = top_candidates + candidates_2.candidates
    final_scores = await scorer.score_solutions(problem2, all_candidates)

    print("\nFinal scores for all candidates:")
    final_best = None
    final_best_score = 0.0

    for scored in final_scores.scored_solutions:
        if scored.score > final_best_score:
            final_best_score = scored.score
            final_best = scored

    print(f"\n🎯 FINAL BEST SOLUTION:")
    print(f"Solution: {final_best.solution}")
    print(f"Score: {final_best.score:.2f}")
    print(f"Reasoning: {final_best.reasoning}")
    print(f"Complete: {final_best.is_complete}, Has errors: {final_best.has_errors}")

    # Example 3: Creative Problem
    print("\n" + "=" * 60)
    print("Example 3: Creative Problem Solving")
    print("=" * 60)

    problem3 = "Design a simple two-player game that can be played with just a pencil and paper in under 5 minutes"

    print(f"Problem: {problem3}\n")

    # Generate creative solutions
    creative_gen = CandidateGenerator(name="creative_gen", temperature=0.9)
    creative_candidates = await creative_gen.generate_candidates(
        problem3, num_candidates=4
    )

    print("Generated game ideas:")
    for i, idea in enumerate(creative_candidates.candidates, 1):
        print(f"\n{i}. {idea}")

    # Score them
    creative_scores = await scorer.score_solutions(
        problem3, creative_candidates.candidates
    )

    print(f"\nScoring rationale: {creative_scores.problem_understanding}")

    print("\nTop game idea:")
    top_game = max(creative_scores.scored_solutions, key=lambda x: x.score)
    print(f"🎮 {top_game.solution}")
    print(f"Score: {top_game.score:.2f}")
    print(f"Why it works: {top_game.reasoning}")


if __name__ == "__main__":
    # Run the demonstration
    asyncio.run(demonstrate_tot())
