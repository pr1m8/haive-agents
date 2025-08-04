"""Tree of Thoughts Multi-Agent Implementation.

This module implements Tree of Thoughts as a multi-agent system using EnhancedMultiAgentV4.
Each stage of the TOT algorithm is handled by a specialized agent.
"""

import asyncio
from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from pydantic import BaseModel, Field

from haive.agents.simple.agent_v3 import SimpleAgentV3

# ===================================
# Structured Output Models
# ===================================


class ProblemAnalysis(BaseModel):
    """Analysis of the problem to solve."""

    problem_type: str = Field(
        description="Type of problem (math, logic, planning, etc.)"
    )
    key_constraints: list[str] = Field(description="Important constraints to consider")
    success_criteria: str = Field(description="What constitutes a valid solution")
    approach_hints: list[str] = Field(description="Suggested approaches to try")


class CandidateGeneration(BaseModel):
    """Multiple candidate solutions."""

    reasoning: str = Field(description="Reasoning behind the candidates")
    candidates: list[str] = Field(
        description="List of candidate solutions", min_items=3, max_items=10
    )


class CandidateEvaluation(BaseModel):
    """Evaluation of a single candidate."""

    candidate: str = Field(description="The candidate being evaluated")
    score: float = Field(description="Score between 0 and 1", ge=0, le=1)
    strengths: list[str] = Field(description="What's good about this solution")
    weaknesses: list[str] = Field(description="What could be improved")
    feedback: str = Field(description="Overall evaluation feedback")


class BeamSelection(BaseModel):
    """Selection of best candidates for next iteration."""

    selected_candidates: list[dict[str, Any]] = Field(
        description="Top candidates with scores"
    )
    should_continue: bool = Field(description="Whether to continue searching")
    reasoning: str = Field(description="Reasoning for selection and continuation")


class FinalSolution(BaseModel):
    """Final synthesized solution."""

    solution: str = Field(description="The final solution")
    confidence: float = Field(description="Confidence in solution (0-1)", ge=0, le=1)
    explanation: str = Field(description="Explanation of the solution")
    search_summary: str = Field(description="Summary of the search process")


# ===================================
# TOT Multi-Agent System
# ===================================


class TreeOfThoughtsMultiAgent:
    """Tree of Thoughts implemented as a multi-agent system."""

    def __init__(
        self,
        max_depth: int = 3,
        beam_width: int = 3,
        threshold: float = 0.8,
        expansion_count: int = 5,
        temperature_config: dict[str, float] | None = None):
        """Initialize the TOT multi-agent system.

        Args:
            max_depth: Maximum search depth
            beam_width: Number of candidates to keep at each level
            threshold: Score threshold for accepting a solution
            expansion_count: Number of new candidates to generate
            temperature_config: Temperature settings for each agent
        """
        self.max_depth = max_depth
        self.beam_width = beam_width
        self.threshold = threshold
        self.expansion_count = expansion_count

        # Default temperature configuration
        temps = temperature_config or {
            "analyzer": 0.3,
            "generator": 0.7,
            "evaluator": 0.2,
            "selector": 0.1,
            "synthesizer": 0.4,
        }

        # Create specialized agents
        self.problem_analyzer = SimpleAgentV3(
            name="problem_analyzer",
            engine=AugLLMConfig(
                temperature=temps["analyzer"],
                structured_output_model=ProblemAnalysis,
                system_message="""You are a problem analysis expert. Analyze problems to understand:
                - What type of problem it is
                - Key constraints and requirements
                - Success criteria
                - Potential solution approaches"""))

        self.candidate_generator = SimpleAgentV3(
            name="candidate_generator",
            engine=AugLLMConfig(
                temperature=temps["generator"],
                structured_output_model=CandidateGeneration,
                system_message=f"""You are a creative solution generator. Generate {self.expansion_count} diverse candidate solutions.
                Be creative but ensure each candidate is distinct and could potentially solve the problem.
                Think step by step and explore different approaches."""))

        self.solution_evaluator = SimpleAgentV3(
            name="solution_evaluator",
            engine=AugLLMConfig(
                temperature=temps["evaluator"],
                structured_output_model=CandidateEvaluation,
                system_message="""You are a solution evaluator. Evaluate candidate solutions by:
                - Checking if they meet the problem requirements
                - Identifying strengths and weaknesses
                - Providing a score between 0 (terrible) and 1 (perfect)
                Be critical but fair in your evaluation."""))

        self.beam_selector = SimpleAgentV3(
            name="beam_selector",
            engine=AugLLMConfig(
                temperature=temps["selector"],
                structured_output_model=BeamSelection,
                system_message=f"""You are a search strategy expert. Select the top {self.beam_width} candidates for further exploration.
                Decide whether to continue searching based on:
                - Current best score vs threshold ({self.threshold})
                - Search depth vs maximum ({self.max_depth})
                - Diversity of candidates"""))

        self.solution_synthesizer = SimpleAgentV3(
            name="solution_synthesizer",
            engine=AugLLMConfig(
                temperature=temps["synthesizer"],
                structured_output_model=FinalSolution,
                system_message="""You are a solution synthesis expert. Create the final solution by:
                - Selecting the best candidate
                - Providing clear explanation
                - Summarizing the search process
                - Assessing confidence in the solution"""))

        # Track search state
        self.search_history = []
        self.best_solution = None
        self.problem_analysis = None

    async def solve(self, problem: str) -> dict[str, Any]:
        """Solve a problem using Tree of Thoughts multi-agent approach.

        Args:
            problem: The problem to solve

        Returns:
            Dictionary containing solution and search metadata
        """
        # Step 1: Analyze the problem
        self.problem_analysis = await self.problem_analyzer.arun(problem)

        # Initialize search with the problem as the first "candidate"
        current_candidates = [
            {"content": problem, "score": 0.0, "feedback": "Initial problem statement"}
        ]

        # Search loop
        for depth in range(self.max_depth):

            # Store candidates for this depth
            depth_candidates = []

            # Step 2: Generate candidates from each beam candidate
            for i, seed in enumerate(current_candidates[: self.beam_width]):

                # Create generation prompt with context
                generation_prompt = f"""
                Problem: {problem}

                Problem Analysis:
                - Type: {self.problem_analysis.problem_type}
                - Success Criteria: {self.problem_analysis.success_criteria}
                - Constraints: {', '.join(self.problem_analysis.key_constraints)}

                Current Seed Solution (score: {seed['score']}):
                {seed['content']}

                Feedback: {seed.get('feedback', 'N/A')}

                Generate {self.expansion_count} new candidate solutions that improve upon or explore different approaches from the seed.
                """

                generation_result = await self.candidate_generator.arun(
                    generation_prompt
                )

                # Step 3: Evaluate each generated candidate

                for _j, candidate in enumerate(generation_result.candidates):
                    eval_prompt = f"""
                    Problem: {problem}

                    Success Criteria: {self.problem_analysis.success_criteria}
                    Constraints: {', '.join(self.problem_analysis.key_constraints)}

                    Candidate Solution:
                    {candidate}

                    Evaluate this solution thoroughly.
                    """

                    evaluation = await self.solution_evaluator.arun(eval_prompt)

                    depth_candidates.append(
                        {
                            "content": candidate,
                            "score": evaluation.score,
                            "feedback": evaluation.feedback,
                            "strengths": evaluation.strengths,
                            "weaknesses": evaluation.weaknesses,
                            "depth": depth + 1,
                            "parent": i,
                        }
                    )

            # Step 4: Select best candidates for beam search

            selection_prompt = f"""
            Current search depth: {depth + 1}/{self.max_depth}
            Score threshold: {self.threshold}

            Candidates to consider:
            {self._format_candidates_for_selection(depth_candidates)}

            Select the top {self.beam_width} candidates for the next iteration.
            """

            selection = await self.beam_selector.arun(selection_prompt)

            # Update current candidates
            current_candidates = selection.selected_candidates
            self.search_history.append(
                {
                    "depth": depth + 1,
                    "candidates": depth_candidates,
                    "selected": selection.selected_candidates,
                }
            )

            # Check if we should stop
            if not selection.should_continue:
                break

            # Check if best score exceeds threshold
            best_score = max(c["score"] for c in current_candidates)
            if best_score >= self.threshold:
                break

        # Step 5: Synthesize final solution

        synthesis_prompt = f"""
        Problem: {problem}

        Search Summary:
        - Total candidates explored: {sum(len(d['candidates']) for d in self.search_history)}
        - Search depth reached: {len(self.search_history)}
        - Best candidates found:
        {self._format_best_candidates()}

        Create the final solution based on the search results.
        """

        final_solution = await self.solution_synthesizer.arun(synthesis_prompt)

        # Prepare result
        result = {
            "solution": final_solution.solution,
            "confidence": final_solution.confidence,
            "explanation": final_solution.explanation,
            "search_summary": final_solution.search_summary,
            "problem_analysis": self.problem_analysis.model_dump(),
            "search_history": self.search_history,
            "total_candidates": sum(len(d["candidates"]) for d in self.search_history),
            "search_depth": len(self.search_history),
        }

        self.best_solution = result
        return result

    def _format_candidates_for_selection(self, candidates: list[dict]) -> str:
        """Format candidates for the selector agent."""
        formatted = []
        for i, c in enumerate(candidates):
            formatted.append(
                f"""
Candidate {i+1}:
- Score: {c['score']:.2f}
- Content: {c['content'][:200]}...
- Strengths: {', '.join(c['strengths'][:2])}
- Weaknesses: {', '.join(c['weaknesses'][:2])}
"""
            )
        return "\n".join(formatted)

    def _format_best_candidates(self) -> str:
        """Format the best candidates from search history."""
        all_candidates = []
        for depth_data in self.search_history:
            all_candidates.extend(depth_data["candidates"])

        # Sort by score and get top 5
        sorted_candidates = sorted(
            all_candidates, key=lambda x: x["score"], reverse=True
        )[:5]

        formatted = []
        for i, c in enumerate(sorted_candidates):
            formatted.append(
                f"""
{i+1}. Score: {c['score']:.2f} (Depth: {c['depth']})
   Content: {c['content'][:300]}...
   Feedback: {c['feedback'][:200]}...
"""
            )
        return "\n".join(formatted)

    def visualize_search_tree(self) -> str:
        """Create a simple text visualization of the search tree."""
        if not self.search_history:
            return "No search history available"

        lines = ["🌳 Tree of Thoughts Search Visualization\n"]
        lines.append("Root: Problem Statement")

        for depth_data in self.search_history:
            depth = depth_data["depth"]
            lines.append(f"\n{'  ' * (depth-1)}Level {depth}:")

            for c in depth_data["candidates"]:
                score_bar = "█" * int(c["score"] * 10)
                lines.append(
                    f"{'  ' * depth}├─ [{c['score']:.2f}] {score_bar} {c['content'][:50]}..."
                )

        return "\n".join(lines)


# ===================================
# Convenience Functions
# ===================================


async def solve_with_tot_multi_agent(
    problem: str, max_depth: int = 3, beam_width: int = 3, threshold: float = 0.8
) -> dict[str, Any]:
    """Convenience function to solve a problem with TOT multi-agent.

    Args:
        problem: Problem to solve
        max_depth: Maximum search depth
        beam_width: Beam width for search
        threshold: Solution acceptance threshold

    Returns:
        Solution dictionary
    """
    tot = TreeOfThoughtsMultiAgent(
        max_depth=max_depth, beam_width=beam_width, threshold=threshold
    )
    return await tot.solve(problem)


# ===================================
# Example Usage
# ===================================

if __name__ == "__main__":

    async def main():
        # Example 1: Math problem (Game of 24)
        problem1 = "Using the numbers 4, 9, 10, 13 and basic operations (+, -, *, /), create an expression that equals 24. Each number must be used exactly once."

        tot = TreeOfThoughtsMultiAgent(max_depth=3, beam_width=3, threshold=0.9)
        await tot.solve(problem1)

        # Example 2: Logic puzzle
        problem2 = """
        Three friends (Alice, Bob, Charlie) have different colored hats (red, blue, green).
        - Alice's hat is not red
        - The person with the blue hat sits between the other two
        - Charlie doesn't sit next to the person with the red hat
        What color hat does each person have?
        """

        tot2 = TreeOfThoughtsMultiAgent(max_depth=2, beam_width=4, threshold=0.85)
        await tot2.solve(problem2)

    asyncio.run(main())
