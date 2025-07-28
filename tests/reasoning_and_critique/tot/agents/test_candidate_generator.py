"""Test the Candidate Generator agent."""

import asyncio
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../../../src'))

from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.core.engine.aug_llm import AugLLMConfig
from pydantic import BaseModel, Field
from typing import List


class CandidateGeneration(BaseModel):
    """Structured output for candidate generation."""
    
    reasoning: str = Field(
        description="Reasoning about different approaches to solve the problem"
    )
    
    candidates: List[str] = Field(
        description="List of candidate solutions",
        min_items=1,
        max_items=10
    )
    
    diversity_check: str = Field(
        description="Brief explanation of how the candidates differ from each other"
    )


def create_candidate_generator(expansion_count: int = 5, temperature: float = 0.7) -> SimpleAgentV3:
    """Create a candidate generator agent."""
    
    engine = AugLLMConfig(
        temperature=temperature,
        structured_output_model=CandidateGeneration,
        system_message=f"""You are a creative problem solver who generates diverse candidate solutions.

Your task is to generate {expansion_count} different approaches to solve the given problem.

Guidelines:
1. Each candidate should be a complete solution attempt
2. Make candidates diverse - try different strategies
3. Be creative but stay within problem constraints
4. If given a "seed" solution, use it as inspiration but don't just make minor tweaks

For math problems: Try different operation orders, groupings, approaches
For logic problems: Try different reasoning paths, assumptions
For planning problems: Try different sequences, priorities"""
    )
    
    return SimpleAgentV3(name="candidate_generator", engine=engine)


def create_prompt(problem: str, seed_solution: str = None, expansion_count: int = 5) -> str:
    """Create a prompt for candidate generation."""
    prompt_parts = [f"Problem to solve:\n{problem}"]
    
    if seed_solution:
        prompt_parts.append(f"\nUse this solution as inspiration (but create diverse alternatives):\n{seed_solution}")
    
    prompt_parts.append(f"\nGenerate {expansion_count} different candidate solutions.")
    
    return "\n\n".join(prompt_parts)


async def test_candidate_generator():
    """Test candidate generation for different problem types."""
    
    print("🧪 Testing TOT Candidate Generator")
    print("=" * 80)
    
    # Create generator
    generator = create_candidate_generator(expansion_count=5, temperature=0.7)
    
    # Test 1: Math problem (Game of 24)
    print("\n📊 Test 1: Math Problem (Game of 24)")
    math_problem = "Using the numbers 4, 9, 10, 13 and operations +, -, *, /, create an expression that equals 24. Each number must be used exactly once."
    
    prompt = create_prompt(math_problem, expansion_count=5)
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
    
    prompt2 = create_prompt(math_problem, seed_solution=seed, expansion_count=5)
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
    
    prompt3 = create_prompt(logic_problem, expansion_count=3)
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
        
        prompt = create_prompt(problem, expansion_count=count)
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