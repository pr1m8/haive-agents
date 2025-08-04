"""ReWOO Tree Agent V3 - Pure Agent Composition for Evidence-Based Planning.

This module provides the **recommended** implementation for research and evidence-based
planning tasks. It represents the latest and most elegant approach to the ReWOO
(Reasoning WithOut Observation) pattern using pure agent composition.

## Key Features

- **Pure Agent Composition**: No manual nodes - agents are automatically wrapped
- **Evidence-Based Planning**: Gather evidence before reasoning for better decisions
- **Parallel Execution**: Evidence collection can happen in parallel
- **Tool Aliasing**: Map abstract tool names to actual implementations
- **Type Safety**: Full Pydantic validation and type checking
- **Clean Architecture**: Leverages MultiAgent patterns for orchestration

## ReWOO Pattern

```
Problem Analysis
    ↓
Evidence Planning (what info needed?)
    ↓
Parallel Evidence Collection
    ↓
Reasoning with Evidence
    ↓
Final Answer
```

## Usage

### Basic Research Task
```python
from haive.agents.planning import create_rewoo_agent_with_tools_v3
from haive.tools import web_search_tool, calculator_tool

agent = create_rewoo_agent_with_tools_v3(
    name="researcher",
    tools=[web_search_tool, calculator_tool],
    model="gpt-4"
)

result = agent.run("What is the economic impact of renewable energy?")
```

### Advanced with Tool Aliases
```python
agent = ReWOOTreeAgent(
    name="advanced_researcher",
    available_tools=[web_search, db_query, api_call],
    tool_aliases={
        "research": ToolAlias(
            alias="research",
            actual_tool="web_search",
            force_choice=True
        ),
        "data": ToolAlias(
            alias="data",
            actual_tool="db_query",
            parameters={"limit": 100}
        )
    },
    max_parallelism=4
)
```

## When to Use

✅ **Use ReWOO V3 when**:
- You need evidence-based decision making
- Research tasks with multiple information sources
- Tasks benefit from parallel evidence gathering
- You want clean, maintainable code

❌ **Consider alternatives when**:
- Simple sequential tasks (use clean_plan_execute)
- No evidence gathering needed (use simple planning)
- Very simple single-step tasks (use ReactAgent directly)

## Advantages over V2

1. **Cleaner Code**: Pure agent composition, no manual node management
2. **Better Type Safety**: Proper Pydantic field initialization
3. **More Maintainable**: Follows framework patterns consistently
4. **Easier Testing**: Standard agent testing patterns apply

## Status: Recommended for Research Tasks

This is the preferred implementation for any task requiring evidence gathering
and research before making decisions.
"""

from enum import Enum
from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState
from langchain_core.tools import BaseTool
from pydantic import BaseModel, ConfigDict, Field, field_validator

from haive.agents.multi.clean import MultiAgent
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent


class TaskType(str, Enum):
    """Types of tasks in the planning tree."""

    RESEARCH = "research"
    ANALYSIS = "analysis"
    SYNTHESIS = "synthesis"
    EXECUTION = "execution"
    VALIDATION = "validation"
    PLANNING = "planning"


class ToolAlias(BaseModel):
    """Tool alias configuration for forced tool choice."""

    model_config = ConfigDict(
        str_strip_whitespace=True, validate_assignment=True, extra="forbid"
    )

    alias: str = Field(..., min_length=1, max_length=50)
    actual_tool: str = Field(..., min_length=1, max_length=50)
    force_choice: bool = Field(default=True)
    parameters: dict[str, Any] = Field(default_factory=dict)

    @field_validator("alias")
    @classmethod
    def validate_alias(cls, v: str) -> str:
        if not v.replace("_", "").isalnum():
            raise ValueError("Alias must be alphanumeric with underscores")
        return v


class ReWOOPlan(BaseModel):
    """Structured plan output."""

    model_config = ConfigDict(
        str_strip_whitespace=True, validate_assignment=True, extra="forbid"
    )

    plan_id: str = Field(..., min_length=1, max_length=100)
    name: str = Field(..., min_length=1, max_length=200)
    problem_analysis: str = Field(..., min_length=10, max_length=2000)
    approach_strategy: str = Field(..., min_length=10, max_length=1000)

    # Execution plan
    tasks: list[str] = Field(default_factory=list)
    dependencies: dict[str, list[str]] = Field(default_factory=dict)
    tool_assignments: dict[str, str] = Field(default_factory=dict)

    # Risk assessment
    risk_factors: list[str] = Field(default_factory=list)
    fallback_strategies: list[str] = Field(default_factory=list)


class ReWOOTreeState(MultiAgentState):
    """State for ReWOO tree execution."""

    current_plan: ReWOOPlan | None = None
    tool_aliases: dict[str, ToolAlias] = Field(default_factory=dict)
    planning_depth: int = Field(default=0, ge=0, le=10)
    task_results: dict[str, Any] = Field(default_factory=dict)


class ReWOOTreeAgent(MultiAgent):
    """ReWOO Tree Agent using pure MultiAgent composition.

    No manual nodes - everything is agents that get automatically wrapped.
    """

    # Pydantic fields
    available_tools: list[BaseTool] = Field(default_factory=list)
    tool_aliases: dict[str, ToolAlias] = Field(default_factory=dict)
    max_planning_depth: int = Field(default=3)
    max_parallelism: int = Field(default=4)

    def __init__(
        self,
        name: str = "rewoo_tree_agent",
        available_tools: list[BaseTool] | None = None,
        tool_aliases: dict[str, ToolAlias] | None = None,
        max_planning_depth: int = 3,
        max_parallelism: int = 4,
        **kwargs):
        # Create planner agent
        planner = SimpleAgent(
            name=f"{name}_planner",
            engine=AugLLMConfig(
                prompt_template="""
                You are a ReWOO Planner. Create a structured execution plan.

                Problem: {input}
                Available tools: {tools}

                Create a detailed plan with:
                - Problem analysis
                - Task breakdown
                - Tool assignments
                - Risk assessment
                """,
                temperature=0.3,
                structured_output_model=ReWOOPlan))

        # Create executor agents for parallelization
        executors = []
        for i in range(min(max_parallelism, 4)):
            executor = ReactAgent(
                name=f"{name}_executor_{i}",
                engine=AugLLMConfig(
                    prompt_template="""
                    You are a ReWOO Executor. Execute tasks efficiently.

                    Task: {input}
                    Available tools: {tools}
                    Context: {context}

                    Execute the task and return results.
                    """,
                    temperature=0.5),
                tools=available_tools or [])
            executors.append(executor)

        # Create coordinator
        coordinator = SimpleAgent(
            name=f"{name}_coordinator",
            engine=AugLLMConfig(
                prompt_template="""
                You are a task coordinator managing parallel execution.

                Plan: {plan}
                Completed: {completed}
                Results: {results}

                Coordinate the next phase of execution.
                """,
                temperature=0.3))

        # Create validator
        validator = SimpleAgent(
            name=f"{name}_validator",
            engine=AugLLMConfig(
                prompt_template="""
                You are a result validator.

                Task: {task}
                Result: {result}

                Validate the result and provide feedback.
                """,
                temperature=0.1))

        # Collect all agents
        all_agents = [planner, coordinator, validator, *executors]

        # Initialize MultiAgent with proper Pydantic fields
        super().__init__(
            name=name,
            agents=all_agents,
            available_tools=available_tools or [],
            tool_aliases=tool_aliases or {},
            max_planning_depth=max_planning_depth,
            max_parallelism=max_parallelism,
            execution_mode="infer",
            state_schema=ReWOOTreeState,
            **kwargs)

        # Configure execution flow using MultiAgent patterns
        self._configure_execution_flow()

    def _configure_execution_flow(self):
        """Configure execution flow using MultiAgent branching."""
        # Set up branching from planner to coordinator
        self.add_branch(
            source_agent=f"{self.name}_planner",
            condition="plan_created",
            target_agents=[f"{self.name}_coordinator"])

        # Set up branching from coordinator to executors
        executor_names = [
            f"{self.name}_executor_{i}" for i in range(min(self.max_parallelism, 4))
        ]
        self.add_branch(
            source_agent=f"{self.name}_coordinator",
            condition="tasks_assigned",
            target_agents=executor_names)

        # Set up branching from executors to validator
        for executor_name in executor_names:
            self.add_branch(
                source_agent=executor_name,
                condition="task_completed",
                target_agents=[f"{self.name}_validator"])

        # Set up completion or recursive planning
        self.add_branch(
            source_agent=f"{self.name}_validator",
            condition="validation_complete",
            target_agents=[f"{self.name}_coordinator", "__end__"])

    def add_tool_alias(
        self, alias: str, actual_tool: str, force_choice: bool = True, **params
    ):
        """Add a tool alias for forced tool choice."""
        tool_alias = ToolAlias(
            alias=alias,
            actual_tool=actual_tool,
            force_choice=force_choice,
            parameters=params)
        self.tool_aliases[alias] = tool_alias

        # Update executor agents with new alias
        for agent_name, agent in self.agents.items():
            if "executor" in agent_name and hasattr(agent, "tools"):
                # Update tool usage for this executor
                agent.engine.prompt_template += f"\nUse {alias} to access {actual_tool}"

    async def create_and_execute_plan(self, problem: str) -> dict[str, Any]:
        """Create and execute a plan using pure MultiAgent flow."""
        # Execute using MultiAgent - no manual nodes!
        result = await self.arun(problem)

        return {
            "status": "completed",
            "result": result,
            "agent_count": len(self.agents),
            "execution_mode": self.execution_mode,
            "parallelism": self.max_parallelism,
        }


class ParallelReWOOAgent(ReWOOTreeAgent):
    """Enhanced ReWOO agent with maximum parallelization."""

    def __init__(
        self, name: str = "parallel_rewoo", max_parallelism: int = 8, **kwargs
    ):
        super().__init__(name=name, max_parallelism=max_parallelism, **kwargs)

        # Configure for maximum parallelization
        self.execution_mode = "parallel"


def create_rewoo_agent_with_tools(
    tools: list[BaseTool],
    tool_aliases: dict[str, str] | None = None,
    max_parallelism: int = 4) -> ReWOOTreeAgent:
    """Factory function to create ReWOO agent with tools."""
    # Convert tool aliases to ToolAlias objects
    alias_objects = {}
    if tool_aliases:
        for alias, tool_name in tool_aliases.items():
            alias_objects[alias] = ToolAlias(
                alias=alias, actual_tool=tool_name, force_choice=True
            )

    return ReWOOTreeAgent(
        name="rewoo_agent",
        available_tools=tools,
        tool_aliases=alias_objects,
        max_parallelism=max_parallelism)
