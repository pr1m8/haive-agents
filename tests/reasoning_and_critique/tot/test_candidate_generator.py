"""Test the Candidate Generator agent."""

import asyncio
from haive.agents.reasoning_and_critique.tot.agents.candidate_generator import (
    CandidateGenerator,
    CandidateGeneration,
    create_candidate_generator
)


async def test_candidate_generator():
    """Test candidate generation for different problem types."""
    
    print("🧪 Testing TOT Candidate Generator")
    print("=" * 80)
    
    # Create generator
    generator = create_candidate_generator(expansion_count=5, temperature=0.7)
    
    # Test 1: Math problem (Game of 24)
    print("\n📊 Test 1: Math Problem (Game of 24)")
    math_problem = "Using the numbers 4, 9, 10, 13 and operations +, -, *, /, create an expression that equals 24. Each number must be used exactly once."
    
    prompt = generator.create_prompt(math_problem)
    result = await generator.arun(prompt)
    
    print(f"Reasoning: {result.reasoning[:200]}...")
    print(f"Generated {len(result.candidates)} candidates:")
    for i, candidate in enumerate(result.candidates, 1):
        print(f"  {i}. {candidate}")
    print(f"Diversity check: {result.diversity_check}")
    
    # Validate structured output
    assert isinstance(result, CandidateGeneration)
    assert len(result.candidates) >= 1
    assert len(result.candidates) <= 10
    
    # Test 2: With seed solution
    print("\n\n📊 Test 2: Expansion from Seed")
    seed = "(9 - 4) * 10 - 13 = 37 (incorrect, too high)"
    
    prompt2 = generator.create_prompt(math_problem, seed_solution=seed)
    result2 = await generator.arun(prompt2)
    
    print(f"Seed: {seed}")
    print(f"New candidates based on seed:")
    for i, candidate in enumerate(result2.candidates, 1):
        print(f"  {i}. {candidate}")
    
    # Test 3: Logic puzzle
    print("\n\n📊 Test 3: Logic Puzzle")
    logic_problem = """Three friends (Alice, Bob, Charlie) have different colored hats (red, blue, green).
    - Alice's hat is not red
    - The person with the blue hat sits between the other two
    - Charlie doesn't sit next to the person with the red hat
    What color hat does each person have?"""
    
    prompt3 = generator.create_prompt(logic_problem)
    result3 = await generator.arun(prompt3)
    
    print(f"Generated {len(result3.candidates)} logic solutions:")
    for i, candidate in enumerate(result3.candidates, 1):
        print(f"  {i}. {candidate[:100]}...")
    
    print("\n✅ All tests passed!")
    return True


async def test_different_expansion_counts():
    """Test with different expansion counts."""
    
    print("\n\n🧪 Testing Different Expansion Counts")
    print("=" * 80)
    
    problem = "Find three consecutive numbers that sum to 30."
    
    for count in [3, 5, 8]:
        print(f"\n📊 Testing with expansion_count={count}")
        generator = create_candidate_generator(expansion_count=count)
        
        prompt = generator.create_prompt(problem)
        result = await generator.arun(prompt)
        
        print(f"Requested: {count}, Got: {len(result.candidates)} candidates")
        assert len(result.candidates) >= 1
        assert len(result.candidates) <= 10
    
    print("\n✅ Expansion count tests passed!")


if __name__ == "__main__":
    async def main():
        await test_candidate_generator()
        await test_different_expansion_counts()
    
    asyncio.run(main())