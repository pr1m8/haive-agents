"""Candidate Generator Agent for Tree of Thoughts.

This agent generates multiple candidate solutions for a given problem.
"""

from typing import List, Optional

from haive.core.engine.aug_llm import AugLLMConfig
from pydantic import BaseModel, Field, PrivateAttr

from haive.agents.simple.agent_v3 import SimpleAgentV3


class CandidateGeneration(BaseModel):
    """Structured output for candidate generation."""

    reasoning: str = Field(
        description="Reasoning about different approaches to solve the problem"
    )

    candidates: List[str] = Field(
        description="List of candidate solutions", min_items=1, max_items=10
    )

    diversity_check: str = Field(
        description="Brief explanation of how the candidates differ from each other"
    )


class CandidateGenerator:
    """Agent that generates multiple candidate solutions."""

    def __init__(
        self,
        name: str = "candidate_generator",
        expansion_count: int = 5,
        temperature: float = 0.7,
        engine: Optional[AugLLMConfig] = None,
    ):
        """Initialize the candidate generator.

        Args:
            name: Agent name
            expansion_count: Number of candidates to generate
            temperature: Temperature for generation (higher = more creative)
            engine: Optional engine configuration
        """
        self.name = name
        self.expansion_count = expansion_count

        if engine is None:
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
For planning problems: Try different sequences, priorities""",
            )

        # Create the underlying agent
        self.agent = SimpleAgentV3(name=name, engine=engine)

    def create_prompt(self, problem: str, seed_solution: Optional[str] = None) -> str:
        """Create a prompt for candidate generation.

        Args:
            problem: The problem to solve
            seed_solution: Optional seed solution to expand from

        Returns:
            Formatted prompt
        """
        prompt_parts = [f"Problem to solve:\n{problem}"]

        if seed_solution:
            prompt_parts.append(
                f"\nUse this solution as inspiration (but create diverse alternatives):\n{seed_solution}"
            )

        prompt_parts.append(
            f"\nGenerate {self.expansion_count} different candidate solutions."
        )

        return "\n\n".join(prompt_parts)


# Convenience function
def create_candidate_generator(
    expansion_count: int = 5, temperature: float = 0.7
) -> CandidateGenerator:
    """Create a candidate generator with default settings.

    Args:
        expansion_count: Number of candidates to generate
        temperature: Generation temperature

    Returns:
        Configured CandidateGenerator
    """
    return CandidateGenerator(expansion_count=expansion_count, temperature=temperature)
