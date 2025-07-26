# Plan and Execute Tutorial - LangGraph vs Haive Implementation

## Overview

The Plan and Execute pattern is a sophisticated agent architecture that separates strategic planning from tactical execution. This tutorial compares the LangGraph approach with Haive's implementation, showing how both frameworks achieve similar goals with different design philosophies.

## Core Concepts

### The Pattern

Plan and Execute involves three key phases:

1. **Planning**: Generate a multi-step plan for achieving an objective
2. **Execution**: Execute each step sequentially (or in parallel)
3. **Replanning**: Evaluate progress and adjust the plan as needed

### Benefits

- **Efficiency**: Faster execution as not every action requires the planner
- **Cost Savings**: Can use smaller models for execution
- **Better Performance**: Explicit planning improves task completion
- **Flexibility**: Plans can adapt based on intermediate results

## LangGraph Implementation

### State Definition

```python
from typing import List, Tuple, Annotated, TypedDict
import operator

class PlanExecute(TypedDict):
    input: str                                    # Original query
    plan: List[str]                              # List of steps
    past_steps: Annotated[List[Tuple], operator.add]  # Completed steps
    response: str                                # Final response
```

### Graph Construction

```python
from langgraph.graph import StateGraph, END

# Create workflow
workflow = StateGraph(PlanExecute)

# Add nodes
workflow.add_node("planner", plan_step)
workflow.add_node("agent", execute_step)
workflow.add_node("replan", replan_step)

# Set flow
workflow.set_entry_point("planner")
workflow.add_edge("planner", "agent")
workflow.add_edge("agent", "replan")

# Conditional routing
workflow.add_conditional_edges(
    "replan",
    should_end,
    {"True": END, "False": "agent"}
)

app = workflow.compile()
```

### Component Functions

```python
def plan_step(state: PlanExecute):
    """Generate initial plan."""
    plan = planner_llm.invoke([
        SystemMessage("You are a planner. Create a step-by-step plan."),
        HumanMessage(state["input"])
    ])
    return {"plan": plan.content.strip().split('\n')}

def execute_step(state: PlanExecute):
    """Execute next step."""
    plan = state["plan"]
    past_steps = state["past_steps"]
    current_step = plan[len(past_steps)]

    result = agent_executor.invoke({
        "objective": current_step,
        "context": past_steps
    })

    return {"past_steps": [(current_step, result["output"])]}

def replan_step(state: PlanExecute):
    """Decide whether to continue or finish."""
    if len(state["past_steps"]) >= len(state["plan"]):
        return {"response": "Plan complete"}
    return {}

def should_end(state: PlanExecute):
    """Check if execution should end."""
    return "response" in state
```

## Haive Implementation

### State Definition

```python
from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState
from pydantic import Field

class PlanAndExecuteState(MultiAgentState):
    """State for Plan and Execute Agent."""

    input: str = Field(..., description="Original objective")
    plan: Plan | None = Field(default=None, description="Current plan")
    past_steps: list[Step] = Field(default_factory=list)
    response: str | None = Field(default=None)
    final_response: str | None = Field(default=None)

    def is_plan_complete(self) -> bool:
        """Check if plan is complete."""
        return self.plan is not None and self.plan.status == "complete"
```

### Model Definitions

```python
from pydantic import BaseModel, Field
from typing import Literal

class Step(BaseModel):
    """Individual step in a plan."""
    id: int = Field(..., description="Step ID")
    description: str = Field(..., description="What to do")
    status: Literal["not_started", "in_progress", "complete"] = Field(default="not_started")
    result: str | None = Field(default=None)

    def is_complete(self) -> bool:
        return self.status == "complete"

class Plan(BaseModel):
    """Complete plan with steps."""
    description: str = Field(..., description="Plan overview")
    steps: list[Step] = Field(default_factory=list)
    status: Literal["not_started", "in_progress", "complete"] = Field(default="not_started")

    def get_next_step(self) -> Step | None:
        """Get next incomplete step."""
        for step in self.steps:
            if step.status != "complete":
                return step
        return None

class Act(BaseModel):
    """Action to take - either respond or replan."""
    action: Response | Plan = Field(..., description="Response or new plan")
```

### Agent Creation

```python
from haive.agents.multi.clean import MultiAgent
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig

class PlanAndExecuteAgent(MultiAgent):
    """Plan and Execute using MultiAgent pattern."""

    @classmethod
    def create(cls, tools=None, name="plan_and_execute"):
        """Create the three-agent system."""

        # Planner - creates initial plan
        planner = SimpleAgent(
            name="planner",
            engine=AugLLMConfig(
                prompt_template=PLANNER_PROMPT,
                structured_output_model=Plan,
                temperature=0.7
            )
        )

        # Executor - executes individual steps
        executor = SimpleAgent(
            name="executor",
            engine=AugLLMConfig(
                prompt_template=EXECUTOR_PROMPT,
                structured_output_model=ExecutionResult,
                temperature=0.3
            ),
            tools=tools or []
        )

        # Replanner - evaluates and adjusts
        replanner = SimpleAgent(
            name="replanner",
            engine=AugLLMConfig(
                prompt_template=REPLANNER_PROMPT,
                structured_output_model=Act,
                temperature=0.5
            )
        )

        return cls(
            name=name,
            agents=[planner, executor, replanner],
            state_schema=PlanAndExecuteState
        )
```

### Graph Building

```python
def build_graph(self) -> BaseGraph:
    """Build the execution graph."""
    from haive.core.graph.state_graph.base_graph2 import BaseGraph
    from langgraph.graph import START, END

    graph = BaseGraph(
        name=f"{self.name}_graph",
        state_schema=self.state_schema
    )

    # Add agent nodes
    for agent_name, agent in self.agents.items():
        graph.add_node(agent_name, agent)

    # Define flow
    graph.add_edge(START, "planner")
    graph.add_edge("planner", "executor")
    graph.add_edge("executor", "replanner")

    # Conditional routing
    def should_continue(state):
        return "executor" if not state.is_plan_complete() else END

    graph.add_conditional_edges(
        "replanner",
        should_continue,
        {"executor": "executor", END: END}
    )

    return graph
```

## Key Differences

### 1. State Management

**LangGraph**: Uses TypedDict with operator annotations for state updates

```python
past_steps: Annotated[List[Tuple], operator.add]  # Auto-appends
```

**Haive**: Uses Pydantic models with methods

```python
class PlanAndExecuteState(MultiAgentState):
    def update_past_steps(self, step: Step) -> None:
        """Explicit method for updates."""
```

### 2. Component Design

**LangGraph**: Function-based components

```python
def plan_step(state): ...
def execute_step(state): ...
workflow.add_node("planner", plan_step)
```

**Haive**: Agent-based components

```python
planner = SimpleAgent(name="planner", ...)
executor = SimpleAgent(name="executor", ...)
```

### 3. Type Safety

**LangGraph**: Runtime type checking

```python
class PlanExecute(TypedDict):
    plan: List[str]  # Simple types
```

**Haive**: Compile-time type safety with Pydantic

```python
class Plan(BaseModel):
    steps: list[Step]  # Rich models

    @field_validator('steps')
    def validate_steps(cls, v): ...
```

### 4. Structured Output

**LangGraph**: Manual parsing

```python
plan = llm.invoke(prompt)
steps = plan.content.strip().split('\n')
```

**Haive**: Automatic structured output

```python
engine=AugLLMConfig(
    structured_output_model=Plan,  # Direct to Pydantic
)
```

## Complete Example

### Using LangGraph Pattern

```python
# Define components
async def create_langgraph_plan_execute():
    from langgraph.graph import StateGraph, END
    from langchain_openai import ChatOpenAI

    llm = ChatOpenAI(model="gpt-4")

    def planner(state):
        messages = [
            SystemMessage("Create a step-by-step plan"),
            HumanMessage(state["input"])
        ]
        response = llm.invoke(messages)
        steps = response.content.strip().split('\n')
        return {"plan": steps}

    def executor(state):
        current_step = state["plan"][len(state["past_steps"])]
        # Execute with tools...
        result = f"Executed: {current_step}"
        return {"past_steps": [(current_step, result)]}

    def replanner(state):
        if len(state["past_steps"]) >= len(state["plan"]):
            summary = "\n".join([f"{s}: {r}" for s, r in state["past_steps"]])
            return {"response": f"Complete! Results:\n{summary}"}
        return {}

    # Build graph
    workflow = StateGraph(PlanExecute)
    workflow.add_node("planner", planner)
    workflow.add_node("executor", executor)
    workflow.add_node("replanner", replanner)

    workflow.set_entry_point("planner")
    workflow.add_edge("planner", "executor")
    workflow.add_edge("executor", "replanner")
    workflow.add_conditional_edges(
        "replanner",
        lambda s: "response" in s,
        {True: END, False: "executor"}
    )

    return workflow.compile()
```

### Using Haive Pattern

```python
# Create agent
from haive.agents.planning.plan_and_execute.simple import PlanAndExecuteAgent
from langchain_core.tools import tool

@tool
def search(query: str) -> str:
    """Search for information."""
    return f"Results for: {query}"

@tool
def calculate(expression: str) -> str:
    """Perform calculations."""
    return str(eval(expression))

# Create agent with tools
agent = PlanAndExecuteAgent.create(
    tools=[search, calculate],
    name="task_planner"
)

# Execute
result = await agent.arun({
    "input": "Research the population of Tokyo and calculate how many buses needed if each holds 50 people"
})

print(result.final_response)
```

## Advanced Patterns

### 1. Parallel Execution (LLM Compiler Pattern)

```python
class DAGPlan(BaseModel):
    """Plan with dependency graph."""
    steps: Dict[str, Step]
    dependencies: Dict[str, List[str]]  # step_id -> [dependency_ids]

    def get_executable_steps(self, completed: Set[str]) -> List[str]:
        """Get steps that can run now."""
        executable = []
        for step_id, deps in self.dependencies.items():
            if step_id not in completed and all(d in completed for d in deps):
                executable.append(step_id)
        return executable
```

### 2. Evidence-Based Planning (ReWOO Pattern)

```python
class EvidenceStep(Step):
    """Step that can reference previous evidence."""
    evidence_refs: List[str] = Field(default_factory=list)  # e.g., ["#E1", "#E2"]

class ReWOOState(PlanAndExecuteState):
    """State with evidence tracking."""
    evidence: Dict[str, str] = Field(default_factory=dict)  # "#E1" -> evidence
```

### 3. Adaptive Planning

```python
class AdaptivePlan(Plan):
    """Plan that can modify itself."""
    confidence_threshold: float = Field(default=0.7)
    adaptation_history: List[Dict] = Field(default_factory=list)

    def should_adapt(self, step_result: ExecutionResult) -> bool:
        """Check if plan needs adaptation."""
        return step_result.confidence < self.confidence_threshold
```

## Best Practices

### 1. Plan Quality

```python
PLANNER_PROMPT = """Create a plan that:
1. Has clear, actionable steps
2. Includes all necessary details
3. Avoids redundant steps
4. Orders steps logically
5. Makes the final step produce the answer

Bad: "Research Tokyo"
Good: "Search for current population of Tokyo metropolitan area"
"""
```

### 2. Execution Robustness

```python
class RobustExecutor(SimpleAgent):
    """Executor with error handling."""

    def execute_step_with_retry(self, step: Step, max_retries: int = 3):
        """Execute with retry logic."""
        for attempt in range(max_retries):
            try:
                result = self.run(step.description)
                if self.validate_result(result):
                    return result
            except Exception as e:
                if attempt == max_retries - 1:
                    raise
                continue
```

### 3. Efficient Replanning

```python
def smart_replanning(state: PlanAndExecuteState) -> Act:
    """Replan only when necessary."""

    # Check if on track
    if state.plan.progress_as_expected():
        return Act(action=Response(response=state.compile_results()))

    # Minor adjustment
    if state.plan.needs_minor_adjustment():
        state.plan.adjust_remaining_steps()
        return Act(action=state.plan)

    # Major replanning
    return Act(action=create_new_plan(state))
```

## Testing

### Unit Testing Components

```python
def test_planner_creates_valid_plan():
    """Test planner output."""
    planner = create_planner()
    result = planner.run({"input": "Simple task"})

    assert isinstance(result.plan, Plan)
    assert len(result.plan.steps) > 0
    assert all(step.description for step in result.plan.steps)

def test_executor_updates_state():
    """Test executor state updates."""
    executor = create_executor(tools=[calculator])
    step = Step(id=1, description="Calculate 2+2")

    result = executor.run({"step": step})
    assert result.step_completed
    assert "4" in result.result
```

### Integration Testing

```python
async def test_full_plan_execute_flow():
    """Test complete workflow."""
    agent = PlanAndExecuteAgent.create(tools=[search, calculate])

    result = await agent.arun({
        "input": "What's the square root of 144?"
    })

    # Verify plan was created and executed
    assert result.plan is not None
    assert len(result.past_steps) > 0
    assert "12" in result.final_response
```

## Troubleshooting

### Common Issues

1. **Infinite Replanning**

   ```python
   # Add maximum replan limit
   if state.replan_count > MAX_REPLANS:
       return Act(action=Response(response="Max replanning reached"))
   ```

2. **Vague Plans**

   ```python
   # Validate plan quality
   def validate_plan(plan: Plan) -> bool:
       return all(
           len(step.description) > 10 and
           step.description[0].isupper()
           for step in plan.steps
       )
   ```

3. **Lost Context**
   ```python
   # Include context in executor prompt
   EXECUTOR_PROMPT = """
   Original objective: {original_objective}
   Previous steps: {past_steps}
   Current step: {current_step}
   """
   ```

## Performance Optimization

### 1. Model Selection

```python
# Use appropriate models for each component
planner_llm = "gpt-4"        # Needs reasoning
executor_llm = "gpt-3.5"     # Can be smaller
replanner_llm = "gpt-3.5"    # Moderate complexity
```

### 2. Caching

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def get_cached_plan(objective: str) -> Plan:
    """Cache common plans."""
    return planner.run(objective)
```

### 3. Early Termination

```python
def should_terminate_early(state: PlanAndExecuteState) -> bool:
    """Stop if objective is clearly met."""
    if state.has_clear_answer():
        return True
    if state.cost_exceeds_limit():
        return True
    return False
```

## Conclusion

Both LangGraph and Haive provide powerful implementations of the Plan and Execute pattern:

- **LangGraph**: More flexible, function-based approach
- **Haive**: More structured, type-safe approach with agent composition

Choose based on your needs:

- Use LangGraph for rapid prototyping and custom flows
- Use Haive for production systems with strong typing and reusable components

The pattern itself remains powerful regardless of implementation, offering better performance than simple ReAct agents for complex, multi-step tasks.
