"""Simple test of TOT implementation without persistence."""

import asyncio
from haive.agents.reasoning_and_critique.tot.agents.candidate_generator import (
    CandidateGenerator,
    CandidateGeneration
)
from haive.agents.reasoning_and_critique.tot.agents.solution_scorer import (
    SolutionScorer,
    SolutionScoring
)


async def test_tot_components():
    """Test TOT components individually."""
    print("🌳 Testing Tree of Thoughts Components\n")
    
    # Test 1: Candidate Generator
    print("1. Testing Candidate Generator")
    print("-" * 50)
    
    generator = CandidateGenerator(name="test_generator", temperature=0.7)
    
    try:
        # Simple test - generate candidates for a math problem
        generation_result = await generator.generate_candidates(
            problem="Find two numbers that multiply to 20",
            num_candidates=4
        )
        
        print(f"✅ Generated {len(generation_result.candidates)} candidates:")
        for i, candidate in enumerate(generation_result.candidates, 1):
            print(f"   {i}. {candidate}")
        print(f"\nDiversity check: {generation_result.diversity_check}")
    except Exception as e:
        print(f"❌ Generator error: {e}")
    
    print()
    
    # Test 2: Solution Scorer
    print("2. Testing Solution Scorer")
    print("-" * 50)
    
    scorer = SolutionScorer(name="test_scorer", temperature=0.3)
    
    # Use some candidate solutions
    test_candidates = [
        "4 * 5 = 20",
        "2 * 10 = 20",
        "3 * 7 = 21",  # Wrong
        "20 * 1 = 20"
    ]
    
    try:
        scoring_result = await scorer.score_solutions(
            problem="Find two numbers that multiply to 20",
            candidates=test_candidates
        )
        
        print(f"✅ Scored {len(scoring_result.scored_solutions)} solutions:")
        print(f"\nProblem understanding: {scoring_result.problem_understanding}")
        print("\nScores:")
        for scored in scoring_result.scored_solutions:
            print(f"   - {scored.solution}")
            print(f"     Score: {scored.score:.2f}")
            print(f"     Reasoning: {scored.reasoning}")
            print(f"     Complete: {scored.is_complete}, Has errors: {scored.has_errors}")
            print()
        
        print(f"Ranking rationale: {scoring_result.ranking_rationale}")
    except Exception as e:
        print(f"❌ Scorer error: {e}")
    
    print()
    
    # Test 3: Combined workflow (without EnhancedMultiAgentV4)
    print("3. Testing Combined Workflow")
    print("-" * 50)
    
    problem = "Use the numbers 2, 3, 4, 5 to make 24 using +, -, *, /"
    
    try:
        # Generate candidates
        generation = await generator.generate_candidates(problem, num_candidates=5)
        print(f"Generated {len(generation.candidates)} candidates")
        
        # Score them
        scoring = await scorer.score_solutions(problem, generation.candidates)
        print(f"Scored all candidates")
        
        # Find best solution
        best_solution = None
        best_score = 0.0
        for scored in scoring.scored_solutions:
            if scored.score > best_score:
                best_score = scored.score
                best_solution = scored.solution
        
        print(f"\n🏆 Best solution: {best_solution}")
        print(f"   Score: {best_score:.2f}")
    except Exception as e:
        print(f"❌ Workflow error: {e}")


if __name__ == "__main__":
    # Disable persistence by setting environment variable
    import os
    os.environ["HAIVE_PERSISTENCE_DISABLED"] = "true"
    
    asyncio.run(test_tot_components())