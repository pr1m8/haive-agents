# Tree of Thoughts (TOT) - Multi-Agent Implementation

A complete implementation of the Tree of Thoughts algorithm using multi-agent coordination in the Haive framework.

## 🌳 Overview

Tree of Thoughts is a problem-solving algorithm that systematically explores solution candidates through iterative generation, scoring, and beam search. This implementation provides multiple approaches:

### New Implementation (Recommended)

- **TreeOfThoughtsAgent**: Main orchestrator using composition pattern
- **CandidateGenerator**: Generates diverse solution candidates using creative reasoning
- **SolutionScorer**: Evaluates and scores candidates to guide beam search

### Legacy Implementation (Backward Compatible)

- **TreeOfThoughtsOrchestrator**: Original implementation using `EnhancedMultiAgentV4`
- Maintains compatibility with existing code

## Architecture

```
TreeOfThoughtsOrchestrator
├── CandidateGenerator (Agent)
│   └── Generates diverse solutions
├── SolutionScorer (Agent)
│   └── Evaluates and scores solutions
└── EnhancedMultiAgentV4 (Coordinator)
    └── Orchestrates the TOT algorithm
```

## Usage

### Basic Example

```python
from haive.agents.reasoning_and_critique.tot import create_tot_solver

# Create a TOT solver
solver = await create_tot_solver(
    beam_width=5,        # Keep top 5 solutions at each step
    max_iterations=3     # Maximum search depth
)

# Solve a problem
result = await solver.solve(
    problem="Find three numbers that sum to 24",
    context="Use positive integers only"
)

print(f"Best solution: {result.best_solution}")
print(f"Score: {result.score}")
print(f"Reasoning: {result.reasoning}")
```

### Game of 24 Example

```python
# Classic TOT problem
solver = await create_tot_solver(beam_width=5, max_iterations=4)

result = await solver.solve(
    problem="Use the numbers 3, 3, 8, 8 with +, -, *, / to make 24",
    initial_seed="Try grouping numbers differently"
)

# Explore all solutions found
for sol in result.all_solutions:
    print(f"{sol['solution']} (score: {sol['score']:.2f})")
```

### Custom Configuration

```python
from haive.agents.reasoning_and_critique.tot import TreeOfThoughtsOrchestrator
from haive.core.engine.aug_llm import AugLLMConfig

# Create with custom LLM configuration
orchestrator = TreeOfThoughtsOrchestrator(
    name="custom_tot",
    engine=AugLLMConfig(temperature=0.5),
    beam_width=7,
    max_iterations=5,
    temperature_generate=0.8,  # Higher for diverse candidates
    temperature_score=0.2      # Lower for consistent scoring
)

result = await orchestrator.solve(problem="Your complex problem here")
```

## Components

### CandidateGenerator

Generates diverse solution candidates using structured output:

```python
from haive.agents.reasoning_and_critique.tot import CandidateGenerator

generator = CandidateGenerator(temperature=0.7)
generation = await generator.generate_candidates(
    problem="Find factors of 24",
    num_candidates=5
)

for candidate in generation.candidates:
    print(f"- {candidate}")
```

### SolutionScorer

Evaluates and scores solutions:

```python
from haive.agents.reasoning_and_critique.tot import SolutionScorer

scorer = SolutionScorer(temperature=0.3)
scoring = await scorer.score_solutions(
    problem="Find factors of 24",
    candidates=["1 x 24", "2 x 12", "3 x 8", "4 x 6"]
)

for scored in scoring.scored_solutions:
    print(f"{scored.solution}: {scored.score:.2f} - {scored.reasoning}")
```

## Algorithm Flow

1. **Initialize**: Start with optional seed or generate initial candidates
2. **Generate**: Create new candidate solutions based on current best
3. **Score**: Evaluate all candidates for correctness and quality
4. **Select**: Keep top-k solutions (beam search)
5. **Iterate**: Repeat until solution found or max iterations reached

## Configuration Options

- `beam_width`: Number of top solutions to keep at each iteration (default: 5)
- `max_iterations`: Maximum number of search iterations (default: 3)
- `temperature_generate`: LLM temperature for candidate generation (default: 0.7)
- `temperature_score`: LLM temperature for solution scoring (default: 0.3)

## Testing

Run the test suite:

```bash
# Test individual components
poetry run pytest packages/haive-agents/tests/reasoning_and_critique/tot/agents/ -v

# Test the orchestrator
poetry run pytest packages/haive-agents/tests/reasoning_and_critique/tot/test_orchestrator.py -v

# Run all TOT tests
poetry run pytest packages/haive-agents/tests/reasoning_and_critique/tot/ -v
```

## Legacy Compatibility

This module maintains backward compatibility with the original TOT implementation. The legacy `ToTAgent` and related classes are still available for existing code.

## Performance Considerations

- **Beam Width**: Larger beam width explores more solutions but increases computation
- **Temperature**: Higher generation temperature creates more diverse candidates
- **Iterations**: More iterations allow deeper exploration but take more time
- **Early Termination**: TOT terminates early if a solution scores >= 0.95

## Examples

See the [examples/](examples/) directory for detailed usage examples:

- **Basic TOT**: Simple problem solving with default settings
- **Game of 24**: Classic Tree of Thoughts problem
- **Custom Configuration**: Advanced configuration options
- **Integration Examples**: Using TOT with other agents

## API Reference

### TreeOfThoughtsAgent

Main orchestrator for the Tree of Thoughts algorithm.

```python
class TreeOfThoughtsAgent:
    def __init__(
        self,
        name: str = "tree_of_thoughts",
        beam_size: int = 3,
        max_iterations: int = 3,
        generation_temperature: float = 0.7,
        scoring_temperature: float = 0.3,
        engine: Optional[AugLLMConfig] = None,
    )

    async def solve_problem(self, problem: str) -> Dict[str, Any]
```

### CandidateGenerator

Generates diverse solution candidates.

```python
class CandidateGenerator:
    def __init__(
        self,
        name: str = "candidate_generator",
        expansion_count: int = 5,
        temperature: float = 0.7,
        engine: Optional[AugLLMConfig] = None,
    )

    async def generate_candidates(self, problem: str, num_candidates: Optional[int] = None) -> CandidateGeneration
    async def expand_from_seed(self, problem: str, seed: str, num_candidates: Optional[int] = None) -> CandidateGeneration
```

### SolutionScorer

Evaluates and scores candidate solutions.

```python
class SolutionScorer:
    def __init__(
        self,
        name: str = "solution_scorer",
        engine: AugLLMConfig | None = None,
        temperature: float = 0.3,
    )

    async def score_solutions(self, problem: str, candidates: List[str]) -> SolutionScoring
```

## Structured Output Models

### CandidateGeneration

```python
class CandidateGeneration(BaseModel):
    reasoning: str = Field(description="Reasoning about different approaches")
    candidates: List[str] = Field(description="List of candidate solutions", min_items=1, max_items=10)
    diversity_check: str = Field(description="Explanation of how candidates differ")
```

### SolutionScoring

```python
class SolutionScoring(BaseModel):
    scored_solutions: List[ScoredSolution] = Field(description="Evaluated solutions with scores")
    ranking_rationale: str = Field(description="Explanation of ranking methodology")

class ScoredSolution(BaseModel):
    solution: str = Field(description="The candidate solution")
    score: float = Field(description="Quality score (0.0-1.0)", ge=0.0, le=1.0)
    reasoning: str = Field(description="Detailed evaluation reasoning")
    is_complete: bool = Field(description="Whether solution appears complete")
    has_errors: bool = Field(description="Whether solution contains obvious errors")
```

## Future Enhancements

- [ ] Parallel candidate evaluation for faster processing
- [ ] Adaptive beam width based on problem complexity
- [ ] Memory of previous solution attempts
- [ ] Integration with other reasoning strategies
- [ ] Dynamic iteration stopping based on solution quality
- [ ] Support for multi-modal problems (text + images)

## Contributing

See [CONTRIBUTING.md](../../../../CONTRIBUTING.md) for guidelines on contributing to the TOT implementation.

## License

See [LICENSE](../../../../LICENSE) for licensing information.
