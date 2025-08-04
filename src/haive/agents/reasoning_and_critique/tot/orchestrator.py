"""Tree of Thoughts Orchestrator using EnhancedMultiAgentV4.

This module implements the Tree of Thoughts algorithm using a multi-agent
approach with EnhancedMultiAgentV4 coordinating the Candidate Generator
and Solution Scorer agents.
"""

import logging
from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from pydantic import BaseModel, Field

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.reasoning_and_critique.tot.agents.candidate_generator import (
    CandidateGenerator)
from haive.agents.reasoning_and_critique.tot.agents.solution_scorer import (
    SolutionScorer)

logger = logging.getLogger(__name__)


class TOTResult(BaseModel):
    """Result from Tree of Thoughts execution."""

    best_solution: str = Field(description="The highest-scoring solution found")
    score: float = Field(description="Score of the best solution", ge=0.0, le=1.0)
    reasoning: str = Field(description="Explanation of why this is the best solution")
    iterations: int = Field(description="Number of iterations performed")
    all_solutions: list[dict[str, Any]] = Field(
        description="All solutions explored with scores", default_factory=list
    )


class TreeOfThoughtsOrchestrator:
    """Orchestrates Tree of Thoughts algorithm using multiple agents."""

    def __init__(
        self,
        name: str = "tot_orchestrator",
        engine: AugLLMConfig | None = None,
        beam_width: int = 5,
        max_iterations: int = 3,
        temperature_generate: float = 0.7,
        temperature_score: float = 0.3):
        """Initialize the Tree of Thoughts orchestrator.

        Args:
            name: Name for the orchestrator
            engine: LLM configuration for the coordinator
            beam_width: Number of top solutions to keep at each iteration
            max_iterations: Maximum number of expansion iterations
            temperature_generate: Temperature for candidate generation
            temperature_score: Temperature for solution scoring
        """
        self.name = name
        self.beam_width = beam_width
        self.max_iterations = max_iterations

        if engine is None:
            engine = AugLLMConfig()

        # Create the agents
        self.generator = CandidateGenerator(
            name="tot_generator", temperature=temperature_generate
        )

        self.scorer = SolutionScorer(name="tot_scorer", temperature=temperature_score)

        # Create the multi-agent coordinator
        self.coordinator = EnhancedMultiAgentV4(
            name=name,
            engine=engine,
            agents={"generator": self.generator.agent, "scorer": self.scorer.agent},
            flow_type="sequential",  # Generator → Scorer flow
            system_message="""You are coordinating a Tree of Thoughts search.

Your role is to:
1. Use the generator to create candidate solutions
2. Use the scorer to evaluate them
3. Keep the best solutions (beam search)
4. Iterate until a satisfactory solution is found

The flow is: Generate candidates → Score them → Select best → Repeat or finish""")

    async def solve(
        self,
        problem: str,
        initial_seed: str | None = None,
        context: str = "") -> TOTResult:
        """Solve a problem using Tree of Thoughts.

        Args:
            problem: The problem to solve
            initial_seed: Optional initial solution seed
            context: Additional context or constraints

        Returns:
            TOTResult with the best solution found
        """
        all_solutions = []
        current_candidates = []

        # Initial seed
        if initial_seed:
            current_candidates = [initial_seed]

        best_solution = None
        best_score = 0.0
        best_reasoning = ""

        for iteration in range(self.max_iterations):
            logger.info(f"TOT Iteration {iteration + 1}/{self.max_iterations}")

            # Step 1: Generate new candidates
            if current_candidates:
                # Expand from current best
                seed_text = "\n".join(current_candidates[:3])  # Top 3 as seeds
                generation_prompt = f"""
Problem: {problem}

Current best approaches:
{seed_text}

Based on these approaches, generate new candidate solutions that:
1. Build upon what works
2. Fix any issues
3. Explore variations
4. Complete partial solutions"""
            else:
                # Initial generation
                generation_prompt = f"""
Problem: {problem}
{f'Context: {context}' if context else ''}

Generate diverse candidate solutions to solve this problem."""

            # Use coordinator to run generator
            generation_result = await self.coordinator.arun(
                f"Use the generator agent to: {generation_prompt}",
                agent_selection_strategy="generator",  # Force generator
            )

            # Extract candidates from generation
            new_candidates = self._extract_candidates(generation_result)

            # Step 2: Score all candidates
            all_candidates = current_candidates + new_candidates

            if all_candidates:
                scoring_prompt = f"""
Problem: {problem}

Score these candidate solutions:
{chr(10).join(f'- {c}' for c in all_candidates)}

Evaluate each one carefully."""

                # Use coordinator to run scorer
                scoring_result = await self.coordinator.arun(
                    f"Use the scorer agent to: {scoring_prompt}",
                    agent_selection_strategy="scorer",  # Force scorer
                )

                # Extract scores
                scored_solutions = self._extract_scores(scoring_result, all_candidates)

                # Track all solutions
                for sol, score, reason in scored_solutions:
                    all_solutions.append(
                        {
                            "solution": sol,
                            "score": score,
                            "reasoning": reason,
                            "iteration": iteration + 1,
                        }
                    )

                # Update best solution
                for sol, score, reason in scored_solutions:
                    if score > best_score:
                        best_solution = sol
                        best_score = score
                        best_reasoning = reason

                # Beam search: keep top solutions
                scored_solutions.sort(key=lambda x: x[1], reverse=True)
                current_candidates = [
                    sol for sol, _, _ in scored_solutions[: self.beam_width]
                ]

                # Check for early termination
                if best_score >= 0.95:  # Near-perfect solution
                    logger.info(
                        f"Found excellent solution (score: {best_score}), terminating early"
                    )
                    break

        # Return result
        return TOTResult(
            best_solution=best_solution or "No solution found",
            score=best_score,
            reasoning=best_reasoning or "No valid solutions generated",
            iterations=iteration + 1,
            all_solutions=all_solutions)

    def _extract_candidates(self, generation_result: Any) -> list[str]:
        """Extract candidate solutions from generator output."""
        candidates = []

        # Try to extract from structured output
        if hasattr(generation_result, "output"):
            output = generation_result.output
            if hasattr(output, "candidates"):
                return output.candidates

        # Fallback: parse from text
        result_text = str(generation_result)

        # Look for numbered lists or bullet points
        lines = result_text.split("\n")
        for line in lines:
            line = line.strip()
            # Check for numbered items (1., 2., etc) or bullets (-, *, •)
            if any(
                line.startswith(prefix)
                for prefix in ["1.", "2.", "3.", "4.", "5.", "-", "*", "•"]
            ):
                # Extract the content after the marker
                for prefix in ["1.", "2.", "3.", "4.", "5.", "-", "*", "•"]:
                    if line.startswith(prefix):
                        candidate = line[len(prefix) :].strip()
                        if candidate:
                            candidates.append(candidate)
                        break

        return candidates

    def _extract_scores(
        self, scoring_result: Any, candidates: list[str]
    ) -> list[tuple[str, float, str]]:
        """Extract scores from scorer output."""
        scored = []

        # Try structured output first
        if hasattr(scoring_result, "output"):
            output = scoring_result.output
            if hasattr(output, "scored_solutions"):
                for scored_sol in output.scored_solutions:
                    scored.append(
                        (scored_sol.solution, scored_sol.score, scored_sol.reasoning)
                    )
                return scored

        # Fallback: assign default scores
        for candidate in candidates:
            scored.append((candidate, 0.5, "Could not parse score"))

        return scored


async def create_tot_solver(
    beam_width: int = 5, max_iterations: int = 3, **kwargs
) -> TreeOfThoughtsOrchestrator:
    """Factory function to create a Tree of Thoughts solver.

    Args:
        beam_width: Number of solutions to keep at each iteration
        max_iterations: Maximum iterations to perform
        **kwargs: Additional arguments for the orchestrator

    Returns:
        Configured TreeOfThoughtsOrchestrator instance
    """
    return TreeOfThoughtsOrchestrator(
        beam_width=beam_width, max_iterations=max_iterations, **kwargs
    )
