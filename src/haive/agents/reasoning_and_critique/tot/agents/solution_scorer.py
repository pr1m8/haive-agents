"""Solution Scorer agent for Tree of Thoughts.

This agent evaluates and scores candidate solutions in the TOT algorithm.
It provides numerical scores and reasoning for each candidate to guide
the beam search process.
"""

from haive.core.engine.aug_llm import AugLLMConfig
from pydantic import BaseModel, Field

from haive.agents.simple.agent_v3 import SimpleAgentV3


class ScoredSolution(BaseModel):
    """Individual scored solution with reasoning."""

    solution: str = Field(description="The solution being scored")
    score: float = Field(description="Score from 0.0 to 1.0", ge=0.0, le=1.0)
    reasoning: str = Field(description="Explanation for the score")
    is_complete: bool = Field(description="Whether this is a complete solution")
    has_errors: bool = Field(description="Whether this solution contains errors")


class SolutionScoring(BaseModel):
    """Structured output for solution scoring."""

    problem_understanding: str = Field(
        description="Brief understanding of what makes a good solution"
    )
    scored_solutions: list[ScoredSolution] = Field(
        description="List of scored solutions", min_items=1
    )
    ranking_rationale: str = Field(description="Overall explanation of the ranking")


class SolutionScorer:
    """Agent that scores candidate solutions for Tree of Thoughts."""

    def __init__(
        self,
        name: str = "solution_scorer",
        engine: AugLLMConfig | None = None,
        temperature: float = 0.3,  # Lower temperature for consistent scoring
    ):
        """Initialize the Solution Scorer agent.

        Args:
            name: Agent name
            engine: LLM configuration
            temperature: Temperature for generation (lower = more consistent)
        """
        if engine is None:
            engine = AugLLMConfig(temperature=temperature)

        # System prompt for scoring
        system_message = """You are a solution evaluator for the Tree of Thoughts algorithm.
Your role is to score candidate solutions based on their correctness, completeness, and quality.

Scoring Guidelines:
1. Score from 0.0 (completely wrong) to 1.0 (perfect solution)
2. Consider partial progress - even incomplete solutions can have value
3. Check for logical errors or violations of constraints
4. Reward creative but valid approaches
5. Be consistent in your scoring across similar solutions

For each solution:
- Identify what's correct and what's problematic
- Assess how close it is to a complete solution
- Give clear reasoning for your score
- Mark whether it's complete and error-free"""

        self.agent = SimpleAgentV3(
            name=name,
            engine=engine,
            system_message=system_message,
            structured_output_model=SolutionScoring)

    async def score_solutions(
        self,
        problem: str,
        candidates: list[str],
        context: str = "") -> SolutionScoring:
        """Score a list of candidate solutions.

        Args:
            problem: The original problem statement
            candidates: List of candidate solutions to score
            context: Additional context or constraints

        Returns:
            SolutionScoring with scores and reasoning
        """
        # Format the prompt
        candidates_text = "\n".join(
            [f"Candidate {i+1}: {candidate}" for i, candidate in enumerate(candidates)]
        )

        prompt = f"""Score the following candidate solutions for this problem:

Problem: {problem}

{f'Context: {context}' if context else ''}

Candidates to score:
{candidates_text}

Evaluate each candidate carefully and provide scores with clear reasoning."""

        # Get structured scores
        result = await self.agent.arun(prompt)

        # Extract structured output
        if hasattr(result, "output") and isinstance(result.output, SolutionScoring):
            return result.output
        if isinstance(result, SolutionScoring):
            return result
        # Fallback parsing if needed
        return self._parse_scoring_output(str(result), candidates)

    def _parse_scoring_output(
        self, output: str, candidates: list[str]
    ) -> SolutionScoring:
        """Parse scoring output as fallback."""
        # Simple fallback - assign default scores
        scored_solutions = []
        for _i, candidate in enumerate(candidates):
            scored_solutions.append(
                ScoredSolution(
                    solution=candidate,
                    score=0.5,  # Default middle score
                    reasoning="Unable to parse structured scoring",
                    is_complete=False,
                    has_errors=False)
            )

        return SolutionScoring(
            problem_understanding="Fallback scoring due to parsing error",
            scored_solutions=scored_solutions,
            ranking_rationale="Default scoring applied")

    async def get_best_solutions(
        self,
        problem: str,
        candidates: list[str],
        top_k: int = 3,
        context: str = "") -> list[tuple[str, float]]:
        """Get the top-k best solutions with their scores.

        Args:
            problem: The original problem
            candidates: List of candidate solutions
            top_k: Number of top solutions to return
            context: Additional context

        Returns:
            List of (solution, score) tuples, sorted by score descending
        """
        scoring = await self.score_solutions(problem, candidates, context)

        # Extract and sort by score
        solution_scores = [
            (scored.solution, scored.score) for scored in scoring.scored_solutions
        ]
        solution_scores.sort(key=lambda x: x[1], reverse=True)

        return solution_scores[:top_k]
