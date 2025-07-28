"""Tree of Thoughts (TOT) reasoning module for Haive.

This module implements the Tree of Thoughts algorithm using a multi-agent
approach with EnhancedMultiAgentV4. The implementation uses two specialized
agents:

1. CandidateGenerator - Generates diverse solution candidates
2. SolutionScorer - Evaluates and scores candidates

The TreeOfThoughtsOrchestrator coordinates these agents to perform
beam search through the solution space.

Example:
    ```python
    from haive.agents.reasoning_and_critique.tot import create_tot_solver

    # Create a TOT solver
    solver = await create_tot_solver(
        beam_width=5,
        max_iterations=3
    )

    # Solve a problem
    result = await solver.solve(
        problem="Use numbers 3, 3, 8, 8 to make 24",
        context="Each number must be used exactly once"
    )

    print(f"Best solution: {result.best_solution}")
    print(f"Score: {result.score}")
    ```
"""

# Import the legacy TOT implementation
try:
    from haive.agents.reasoning_and_critique.tot.agent import ToTAgent, setup_workflow
except ImportError:
    # Handle missing setup_workflow
    from haive.agents.reasoning_and_critique.tot.agent import ToTAgent

    setup_workflow = None
from haive.agents.reasoning_and_critique.tot.agents.candidate_generator import (
    CandidateGeneration as NewCandidateGeneration,
)
from haive.agents.reasoning_and_critique.tot.agents.candidate_generator import (
    CandidateGenerator,
)
from haive.agents.reasoning_and_critique.tot.agents.solution_scorer import (
    ScoredSolution,
    SolutionScorer,
    SolutionScoring,
)
from haive.agents.reasoning_and_critique.tot.config import (
    TOTAgentConfig,
)
from haive.agents.reasoning_and_critique.tot.models import (
    Candidate,
    CandidateEvaluation,
    CandidateGeneration,
    Equation,
    EquationGeneration,
    Score,
    ScoredCandidate,
    update_candidates,
)

# Import the new multi-agent TOT implementation
from haive.agents.reasoning_and_critique.tot.orchestrator import (
    TOTResult,
    TreeOfThoughtsOrchestrator,
    create_tot_solver,
)
from haive.agents.reasoning_and_critique.tot.state import (
    TOTInput,
    TOTOutput,
    TOTState,
)

# Build exports list dynamically
_exports = [
    # Legacy exports (kept for backward compatibility)
    "Candidate",
    "CandidateEvaluation",
    "CandidateGeneration",
    "Equation",
    "EquationGeneration",
    "Score",
    "ScoredCandidate",
    "TOTAgentConfig",
    "TOTInput",
    "TOTOutput",
    "TOTState",
    "ToTAgent",
    "update_candidates",
    # New multi-agent exports
    "TreeOfThoughtsOrchestrator",
    "TOTResult",
    "create_tot_solver",
    "CandidateGenerator",
    "NewCandidateGeneration",
    "SolutionScorer",
    "SolutionScoring",
    "ScoredSolution",
]

# Add setup_workflow only if it exists
if setup_workflow is not None:
    _exports.append("setup_workflow")

__all__ = _exports
