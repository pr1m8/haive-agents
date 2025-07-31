"""Test the Candidate Generator agent."""

import asyncio

from haive.agents.reasoning_and_critique.tot.agents.candidate_generator import (
    CandidateGeneration,
    create_candidate_generator,
)


async def test_candidate_generator():
    """Test candidate generation for different problem types."""
    # Create generator
    generator = create_candidate_generator(expansion_count=5, temperature=0.7)

    # Test 1: Math problem (Game of 24)
    math_problem = "Using the numbers 4, 9, 10, 13 and operations +, -, *, /, create an expression that equals 24. Each number must be used exactly once."

    prompt = generator.create_prompt(math_problem)
    result = await generator.arun(prompt)

    for _i, _candidate in enumerate(result.candidates, 1):
        pass

    # Validate structured output
    assert isinstance(result, CandidateGeneration)
    assert len(result.candidates) >= 1
    assert len(result.candidates) <= 10

    # Test 2: With seed solution
    seed = "(9 - 4) * 10 - 13 = 37 (incorrect, too high)"

    prompt2 = generator.create_prompt(math_problem, seed_solution=seed)
    result2 = await generator.arun(prompt2)

    for _i, _candidate in enumerate(result2.candidates, 1):
        pass

    # Test 3: Logic puzzle
    logic_problem = """Three friends (Alice, Bob, Charlie) have different colored hats (red, blue, green).
    - Alice's hat is not red
    - The person with the blue hat sits between the other two
    - Charlie doesn't sit next to the person with the red hat
    What color hat does each person have?"""

    prompt3 = generator.create_prompt(logic_problem)
    result3 = await generator.arun(prompt3)

    for _i, _candidate in enumerate(result3.candidates, 1):
        pass

    return True


async def test_different_expansion_counts():
    """Test with different expansion counts."""
    problem = "Find three consecutive numbers that sum to 30."

    for count in [3, 5, 8]:
        generator = create_candidate_generator(expansion_count=count)

        prompt = generator.create_prompt(problem)
        result = await generator.arun(prompt)

        assert len(result.candidates) >= 1
        assert len(result.candidates) <= 10


if __name__ == "__main__":

    async def main():
        await test_candidate_generator()
        await test_different_expansion_counts()

    asyncio.run(main())
