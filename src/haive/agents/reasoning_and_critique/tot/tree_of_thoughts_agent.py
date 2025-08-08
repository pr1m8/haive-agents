"""Tree of Thoughts Multi-Agent Implementation.

This implements the complete Tree of Thoughts algorithm using MultiAgent
with proper LangGraph routing, conditional edges, and send-based branching.
"""

from typing import Any, Literal

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState
from langgraph.constants import Send
from pydantic import BaseModel, Field

from haive.agents.reasoning_and_critique.tot.agents.candidate_generator import (
    CandidateGenerator,
)
from haive.agents.reasoning_and_critique.tot.agents.solution_scorer import (
    SolutionScorer,
)


class TOTCommand(BaseModel):
    """Commands for Tree of Thoughts routing."""

    action: Literal["generate", "score", "expand", "select_best", "finish"] = Field(
        description="Action to take in TOT workflow"
    )
    target_node: str | None = Field(
        default=None,
        description="Target node to route to (generate_candidates, score_solutions, etc.)",
    )
    data: dict[str, Any] = Field(
        default_factory=dict, description="Data to pass to the target node"
    )
    beam_size: int = Field(
        default=3, description="Number of best solutions to keep for beam search"
    )


class TOTIteration(BaseModel):
    """State for a single TOT iteration."""

    iteration_number: int = Field(description="Current iteration number")
    candidates: list[str] = Field(description="Current candidate solutions")
    scores: list[float] = Field(description="Scores for current candidates")
    best_candidates: list[str] = Field(description="Top candidates from beam search")
    problem: str = Field(description="Original problem statement")
    max_iterations: int = Field(default=3, description="Maximum iterations to run")
    beam_size: int = Field(default=3, description="Beam search size")


class TreeOfThoughtsAgent:
    """Tree of Thoughts agent using multi-agent coordination with conditional routing."""

    def __init__(
        self,
        name: str = "tree_of_thoughts",
        beam_size: int = 3,
        max_iterations: int = 3,
        generation_temperature: float = 0.7,
        scoring_temperature: float = 0.3,
        engine: AugLLMConfig | None = None,
    ):
        """Initialize Tree of Thoughts agent.

        Args:
            name: Agent name
            beam_size: Number of top solutions to keep in beam search
            max_iterations: Maximum TOT iterations
            generation_temperature: Temperature for candidate generation
            scoring_temperature: Temperature for solution scoring
            engine: Optional engine configuration
        """
        self.name = name
        self.beam_size = beam_size
        self.max_iterations = max_iterations

        # Create specialized agents
        self.candidate_generator = CandidateGenerator.create(
            name="tot_generator", expansion_count=5, temperature=generation_temperature
        )

        self.solution_scorer = SolutionScorer(
            name="tot_scorer", temperature=scoring_temperature
        )

        # Store engine for any coordination needs
        self.engine = engine or AugLLMConfig(temperature=0.5)

    def should_continue(self, state: MultiAgentState) -> str:
        """Determine if TOT should continue or finish.

        Returns:
            "continue" to keep iterating, "finish" to end
        """
        iteration_data = state.get("tot_iteration", {})

        if not iteration_data:
            return "continue"  # First iteration

        current_iter = iteration_data.get("iteration_number", 0)
        max_iter = iteration_data.get("max_iterations", self.max_iterations)

        # Check if we have a perfect solution (score >= 0.95)
        scores = iteration_data.get("scores", [])
        if scores and max(scores) >= 0.95:
            return "finish"

        # Check iteration limit
        if current_iter >= max_iter:
            return "finish"

        return "continue"

    def route_tot_action(self, state: MultiAgentState) -> list[Send]:
        """Route TOT actions using Send for parallel processing."""
        iteration_data = state.get("tot_iteration", {})
        current_iter = iteration_data.get("iteration_number", 0)

        if current_iter == 0:
            # First iteration: generate initial candidates
            return [Send("generate_candidates", state)]
        # Subsequent iterations: expand from best candidates
        best_candidates = iteration_data.get("best_candidates", [])
        sends = []

        # Create parallel expansion tasks
        for i, candidate in enumerate(best_candidates[:2]):  # Top 2 for expansion
            expansion_state = state.copy()
            expansion_state["expansion_seed"] = candidate
            expansion_state["expansion_id"] = i
            sends.append(Send("expand_candidates", expansion_state))

        return sends

    async def generate_candidates_node(self, state: MultiAgentState) -> dict[str, Any]:
        """Generate initial candidate solutions."""
        problem = state.get("problem", "")

        # Generate candidates using the generator agent
        result = await self.candidate_generator.generate_candidates(
            problem=problem, num_candidates=5
        )

        # Update state with candidates
        return {
            "candidates": result.candidates,
            "generation_reasoning": result.reasoning,
            "diversity_check": result.diversity_check,
        }

    async def expand_candidates_node(self, state: MultiAgentState) -> dict[str, Any]:
        """Expand candidates from a seed solution."""
        problem = state.get("problem", "")
        seed = state.get("expansion_seed", "")
        expansion_id = state.get("expansion_id", 0)

        # Expand from seed
        result = await self.candidate_generator.expand_from_seed(
            problem=problem, seed=seed, num_candidates=3
        )

        return {
            f"expanded_candidates_{expansion_id}": result.candidates,
            f"expansion_reasoning_{expansion_id}": result.reasoning,
        }

    async def score_solutions_node(self, state: MultiAgentState) -> dict[str, Any]:
        """Score all candidate solutions."""
        problem = state.get("problem", "")
        candidates = state.get("candidates", [])

        # Collect expanded candidates
        all_candidates = candidates.copy()
        for key, value in state.items():
            if key.startswith("expanded_candidates_"):
                all_candidates.extend(value)

        # Score all candidates
        result = await self.solution_scorer.score_solutions(
            problem=problem, candidates=all_candidates
        )

        # Extract scores and sort by score
        scored_solutions = [(s.solution, s.score) for s in result.scored_solutions]
        scored_solutions.sort(key=lambda x: x[1], reverse=True)

        # Select top candidates for beam search
        best_candidates = [sol for sol, _ in scored_solutions[: self.beam_size]]
        best_scores = [score for _, score in scored_solutions[: self.beam_size]]

        return {
            "all_scored_solutions": result.scored_solutions,
            "best_candidates": best_candidates,
            "best_scores": best_scores,
            "scoring_rationale": result.ranking_rationale,
        }

    async def update_iteration_node(self, state: MultiAgentState) -> dict[str, Any]:
        """Update iteration state and prepare for next iteration."""
        iteration_data = state.get("tot_iteration", {})
        current_iter = iteration_data.get("iteration_number", 0)

        # Update iteration data
        new_iteration = {
            "iteration_number": current_iter + 1,
            "candidates": state.get("best_candidates", []),
            "scores": state.get("best_scores", []),
            "best_candidates": state.get("best_candidates", []),
            "problem": state.get("problem", ""),
            "max_iterations": self.max_iterations,
            "beam_size": self.beam_size,
        }

        return {
            "tot_iteration": new_iteration,
        }

    async def finalize_result_node(self, state: MultiAgentState) -> dict[str, Any]:
        """Finalize the TOT result with the best solution."""
        best_candidates = state.get("best_candidates", [])
        best_scores = state.get("best_scores", [])
        all_scored = state.get("all_scored_solutions", [])

        if not best_candidates:
            return {"final_result": "No solution found"}

        # Get the best solution with full details
        best_solution = best_candidates[0]
        best_score = best_scores[0] if best_scores else 0.0

        # Find full details from scored solutions
        best_details = None
        for scored in all_scored:
            if scored.solution == best_solution:
                best_details = scored
                break

        result = {
            "solution": best_solution,
            "score": best_score,
            "is_complete": best_details.is_complete if best_details else False,
            "has_errors": best_details.has_errors if best_details else True,
            "reasoning": (
                best_details.reasoning if best_details else "No reasoning available"
            ),
            "all_candidates_explored": len(state.get("candidates", [])),
            "final_beam_size": len(best_candidates),
        }

        return {
            "final_result": result,
            "tot_completed": True,
        }

    def build_graph_config(self) -> dict[str, Any]:
        """Build the graph configuration with conditional edges and routing."""
        return {
            "nodes": {
                "start": self.start_node,
                "generate_candidates": self.generate_candidates_node,
                "expand_candidates": self.expand_candidates_node,
                "score_solutions": self.score_solutions_node,
                "update_iteration": self.update_iteration_node,
                "finalize_result": self.finalize_result_node,
            },
            "edges": {
                "start": ["generate_candidates"],
                "generate_candidates": ["score_solutions"],
                "expand_candidates": ["score_solutions"],
                "score_solutions": ["update_iteration"],
                "update_iteration": ["finalize_result"],  # Will be conditional
            },
            "conditional_edges": {
                "update_iteration": {
                    "condition": self.should_continue,
                    "mapping": {
                        "continue": self.route_tot_action,  # Returns Send objects
                        "finish": "finalize_result",
                    },
                }
            },
            "entry_point": "start",
            "finish_point": "finalize_result",
        }

    async def start_node(self, state: MultiAgentState) -> dict[str, Any]:
        """Initialize TOT state."""
        return {
            "tot_iteration": {
                "iteration_number": 0,
                "candidates": [],
                "scores": [],
                "best_candidates": [],
                "problem": state.get("problem", ""),
                "max_iterations": self.max_iterations,
                "beam_size": self.beam_size,
            }
        }

    async def solve_problem(self, problem: str) -> dict[str, Any]:
        """Solve a problem using Tree of Thoughts algorithm.

        Args:
            problem: Problem statement to solve

        Returns:
            Dictionary with the best solution and metadata
        """
        # Implementation: Direct orchestration of TOT algorithm
        results = {}

        # Phase 1: Generate initial candidates
        initial_candidates = await self.candidate_generator.generate_candidates(
            problem=problem, num_candidates=5
        )

        candidates = initial_candidates.candidates

        # Phase 2: Score initial candidates
        initial_scores = await self.solution_scorer.score_solutions(
            problem=problem, candidates=candidates
        )

        # Select top candidates for beam search
        scored_solutions = [
            (s.solution, s.score) for s in initial_scores.scored_solutions
        ]
        scored_solutions.sort(key=lambda x: x[1], reverse=True)

        best_candidates = [sol for sol, _ in scored_solutions[: self.beam_size]]
        best_scores = [score for _, score in scored_solutions[: self.beam_size]]

        # Phase 3: Iterative expansion (if multiple iterations)
        for iteration in range(1, self.max_iterations):
            # Check if we have a perfect solution
            if best_scores and max(best_scores) >= 0.95:
                break

            # Expand from top 2 candidates
            expanded_candidates = []
            for _i, seed_candidate in enumerate(best_candidates[:2]):
                expansion = await self.candidate_generator.expand_from_seed(
                    problem=problem, seed=seed_candidate, num_candidates=3
                )
                expanded_candidates.extend(expansion.candidates)

            # Combine with existing candidates
            all_candidates = best_candidates + expanded_candidates

            # Score all candidates
            all_scores = await self.solution_scorer.score_solutions(
                problem=problem, candidates=all_candidates
            )

            # Update beam search
            scored_solutions = [
                (s.solution, s.score) for s in all_scores.scored_solutions
            ]
            scored_solutions.sort(key=lambda x: x[1], reverse=True)

            best_candidates = [sol for sol, _ in scored_solutions[: self.beam_size]]
            best_scores = [score for _, score in scored_solutions[: self.beam_size]]

        # Phase 4: Return best solution
        if not best_candidates:
            return {"solution": "No solution found", "score": 0.0}

        best_solution = best_candidates[0]
        best_score = best_scores[0] if best_scores else 0.0

        # Find detailed info about best solution
        best_details = None
        for scored in initial_scores.scored_solutions:
            if scored.solution == best_solution:
                best_details = scored
                break

        result = {
            "solution": best_solution,
            "score": best_score,
            "is_complete": best_details.is_complete if best_details else False,
            "has_errors": best_details.has_errors if best_details else True,
            "reasoning": (
                best_details.reasoning if best_details else "No reasoning available"
            ),
            "all_candidates_explored": len(candidates),
            "final_beam_size": len(best_candidates),
            "iterations_completed": (
                min(iteration + 1, self.max_iterations)
                if "iteration" in locals()
                else 1
            ),
        }

        return result


# Convenience function
def create_tree_of_thoughts_agent(
    beam_size: int = 3,
    max_iterations: int = 3,
    generation_temperature: float = 0.7,
    scoring_temperature: float = 0.3,
) -> TreeOfThoughtsAgent:
    """Create a Tree of Thoughts agent with default settings.

    Args:
        beam_size: Number of top solutions to keep in beam search
        max_iterations: Maximum TOT iterations
        generation_temperature: Temperature for candidate generation
        scoring_temperature: Temperature for solution scoring

    Returns:
        Configured TreeOfThoughtsAgent
    """
    return TreeOfThoughtsAgent(
        beam_size=beam_size,
        max_iterations=max_iterations,
        generation_temperature=generation_temperature,
        scoring_temperature=scoring_temperature,
    )
