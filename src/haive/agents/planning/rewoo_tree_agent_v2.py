"""ReWOO Tree-based Planning Agent V2 - Using MultiAgent Pattern.

This agent implements the ReWOO (Reasoning without Observation) methodology
using proper agent composition without manual node creation. All nodes are
created automatically by wrapping agents.

Key improvements:
- No manual node functions - everything is agents
- Uses MultiAgent pattern for composition
- Automatic parallelization through agent dependencies
- Tool aliasing and forced tool choice
- Structured output models with field validators
- Recursive planning through agent composition

Reference:
- ReWOO: https://langchain-ai.github.io/langgraph/tutorials/rewoo/rewoo/#solver
- LLM Compiler: https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/
"""

import logging
from datetime import datetime
from enum import Enum
from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState
from langchain_core.messages import HumanMessage
from langchain_core.tools import BaseTool
from pydantic import BaseModel, ConfigDict, Field, field_validator

from haive.agents.multi.clean import MultiAgent
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent

logger = logging.getLogger(__name__)


class TaskType(str, Enum):
    """Types of tasks in the planning tree."""

    RESEARCH = "research"
    ANALYSIS = "analysis"
    SYNTHESIS = "synthesis"
    EXECUTION = "execution"
    VALIDATION = "validation"
    PLANNING = "planning"


class TaskStatus(str, Enum):
    """Status of tasks in the planning tree."""

    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    BLOCKED = "blocked"


class TaskPriority(str, Enum):
    """Priority levels for tasks."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ToolAlias(BaseModel):
    """Tool alias configuration for forced tool choice."""

    model_config = ConfigDict(
        str_strip_whitespace=True, validate_assignment=True, extra="forbid"
    )

    alias: str = Field(
        ..., description="The alias name for the tool", min_length=1, max_length=50
    )

    actual_tool: str = Field(
        ..., description="The actual tool name to execute", min_length=1, max_length=50
    )

    force_choice: bool = Field(
        default=True, description="Whether to force this tool choice"
    )

    parameters: dict[str, Any] = Field(
        default_factory=dict, description="Default parameters for the tool"
    )

    @field_validator("alias")
    @classmethod
    def validate_alias(cls, v: str) -> str:
        """Validate alias format."""
        if not v.replace("_", "").isalnum():
            raise ValueError("Alias must be alphanumeric with underscores")
        return v


class PlanTask(BaseModel):
    """A task in the planning tree - simplified for agent-based execution."""

    model_config = ConfigDict(
        str_strip_whitespace=True, validate_assignment=True, extra="forbid"
    )

    # Identity
    id: str = Field(
        ..., description="Unique identifier for the task", min_length=1, max_length=100
    )

    name: str = Field(
        ...,
        description="Human-readable name for the task",
        min_length=1,
        max_length=200,
    )

    task_type: TaskType = Field(default=TaskType.EXECUTION, description="Type of task")

    description: str = Field(
        ...,
        description="Detailed description of the task",
        min_length=1,
        max_length=1000,
    )

    # Agent assignment
    agent_name: str = Field(..., description="Name of the agent to execute this task")

    tool_alias: str | None = Field(
        default=None, description="Tool alias to use for execution"
    )

    # Dependencies
    dependencies: list[str] = Field(
        default_factory=list, description="List of task IDs this task depends on"
    )

    # Results
    result: Any | None = Field(
        default=None, description="Result of executing this task"
    )

    status: TaskStatus = Field(
        default=TaskStatus.PENDING, description="Current status of the task"
    )

    @field_validator("id")
    @classmethod
    def validate_id(cls, v: str) -> str:
        """Validate task ID format."""
        if not v.replace("_", "").replace("-", "").isalnum():
            raise ValueError(
                "Task ID must be alphanumeric with underscores and hyphens"
            )
        return v


class ReWOOPlan(BaseModel):
    """Complete execution plan with tasks and dependencies."""

    model_config = ConfigDict(
        str_strip_whitespace=True, validate_assignment=True, extra="forbid"
    )

    plan_id: str = Field(
        ..., description="Unique identifier for the plan", min_length=1, max_length=100
    )

    name: str = Field(
        ...,
        description="Human-readable name for the plan",
        min_length=1,
        max_length=200,
    )

    problem_analysis: str = Field(
        ..., description="Analysis of the problem", min_length=10, max_length=2000
    )

    # Task management
    tasks: list[PlanTask] = Field(
        default_factory=list, description="List of tasks in the plan"
    )

    # Execution order (levels for parallelization)
    execution_levels: list[list[str]] = Field(
        default_factory=list, description="Task IDs organized by execution level"
    )

    # Tool requirements
    required_tools: list[str] = Field(
        default_factory=list, description="List of tools required for execution"
    )

    tool_aliases: dict[str, ToolAlias] = Field(
        default_factory=dict, description="Tool aliases for forced tool choice"
    )

    def add_task(self, task: PlanTask) -> None:
        """Add a task to the plan."""
        self.tasks.append(task)
        self._update_execution_levels()

    def _update_execution_levels(self) -> None:
        """Update execution levels based on dependencies."""
        # Create task lookup
        {task.id: task for task in self.tasks}

        # Calculate levels
        levels = []
        processed = set()

        while len(processed) < len(self.tasks):
            level_tasks = []

            for task in self.tasks:
                if task.id in processed:
                    continue

                # Check if all dependencies are processed
                deps_ready = all(dep_id in processed for dep_id in task.dependencies)

                if deps_ready:
                    level_tasks.append(task.id)

            if not level_tasks:
                # Handle circular dependencies by taking any unprocessed task
                for task in self.tasks:
                    if task.id not in processed:
                        level_tasks.append(task.id)
                        break

            levels.append(level_tasks)
            processed.update(level_tasks)

        self.execution_levels = levels

    def get_ready_tasks(self, completed_tasks: set[str]) -> list[PlanTask]:
        """Get tasks that are ready for execution."""
        ready = []
        for task in self.tasks:
            if task.status == TaskStatus.PENDING:
                deps_complete = all(
                    dep_id in completed_tasks for dep_id in task.dependencies
                )
                if deps_complete:
                    ready.append(task)
        return ready


class ReWOOTreeState(MultiAgentState):
    """State for ReWOO tree execution."""

    # Current plan
    current_plan: ReWOOPlan | None = None

    # Task tracking
    completed_tasks: set[str] = Field(default_factory=set)
    task_results: dict[str, Any] = Field(default_factory=dict)

    # Tool management
    tool_aliases: dict[str, ToolAlias] = Field(default_factory=dict)

    # Recursive planning
    planning_depth: int = Field(default=0, ge=0, le=10)

    # Execution metadata
    start_time: datetime | None = None
    end_time: datetime | None = None


class ReWOOPlannerAgent(SimpleAgent):
    """Specialized agent for creating ReWOO plans."""

    # Add as Pydantic field
    available_tools: list[BaseTool] = Field(default_factory=list)

    def __init__(
        self,
        name: str = "rewoo_planner",
        available_tools: list[BaseTool] | None = None,
        **kwargs,
    ):
        # Create planning-specific prompt
        prompt_template = """
        You are a ReWOO Planner that creates detailed execution plans.

        Your task is to:
        1. Analyze the problem thoroughly
        2. Break it down into specific tasks
        3. Identify dependencies between tasks
        4. Assign appropriate agents to each task
        5. Specify tool requirements

        Available tools: {tools}

        Create a structured plan with:
        - Clear task hierarchy
        - Dependency relationships
        - Agent assignments (use: researcher, analyzer, executor, validator)
        - Tool specifications

        Problem: {input}
        Context: {context}
        """

        # Configure for structured output
        engine = kwargs.get(
            "engine",
            AugLLMConfig(
                prompt_template=prompt_template,
                temperature=0.3,  # Lower for consistent planning
                structured_output_model=ReWOOPlan,
            ),
        )

        super().__init__(
            name=name, engine=engine, available_tools=available_tools or [], **kwargs
        )

    def create_plan(
        self, problem: str, context: dict[str, Any] | None = None
    ) -> ReWOOPlan:
        """Create a ReWOO plan for the given problem."""
        tools_list = [tool.name for tool in self.available_tools]

        input_data = {"input": problem, "tools": tools_list, "context": context or {}}

        result = self.run(input_data)

        if isinstance(result, ReWOOPlan):
            return result
        if isinstance(result, dict):
            return ReWOOPlan(**result)
        # Fallback plan
        return self._create_fallback_plan(problem)

    def _create_fallback_plan(self, problem: str) -> ReWOOPlan:
        """Create a simple fallback plan."""
        import uuid

        task = PlanTask(
            id=f"task_{uuid.uuid4().hex[:8]}",
            name="Execute Request",
            task_type=TaskType.EXECUTION,
            description=problem,
            agent_name="executor",
        )

        plan = ReWOOPlan(
            plan_id=f"plan_{uuid.uuid4().hex[:8]}",
            name="Fallback Plan",
            problem_analysis="Direct execution of request",
            tasks=[task],
            execution_levels=[[task.id]],
        )

        return plan


class ReWOOExecutorAgent(ReactAgent):
    """Agent that executes individual tasks with tool support."""

    # Add as Pydantic field
    tool_aliases: dict[str, ToolAlias] = Field(default_factory=dict)

    def __init__(
        self,
        name: str = "rewoo_executof",
        tools: list[BaseTool] | None = None,
        tool_aliases: dict[str, ToolAlias] | None = None,
        **kwargs,
    ):
        super().__init__(
            name=name, tools=tools or [], tool_aliases=tool_aliases or {}, **kwargs
        )

    def execute_task(
        self, task: PlanTask, context: dict[str, Any] | None = None
    ) -> Any:
        """Execute a single task."""
        # Check for tool alias
        if task.tool_alias and task.tool_alias in self.tool_aliases:
            alias = self.tool_aliases[task.tool_alias]
            # Force specific tool usage
            input_str = f"Use the {alias.actual_tool} tool to: {task.description}"
        else:
            input_str = task.description

        # Add context if provided
        if context:
            input_str += f"\n\nContext: {context}"

        return self.run(input_str)


class ReWOOTreeAgent(MultiAgent):
    """ReWOO Tree Agent using proper MultiAgent composition.

    This agent creates and executes tree-based plans using multiple specialized agents:
    - Planner: Creates structured execution plans
    - Executor: Executes individual tasks with tools
    - Coordinator: Manages parallel execution
    - Validator: Validates results
    """

    # Add as Pydantic fields
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
        **kwargs,
    ):

        # Create planner agent
        planner = ReWOOPlannerAgent(
            name=f"{name}_planner", available_tools=available_tools
        )

        # Create executor agents (multiple for parallelism)
        executors = []
        for i in range(min(max_parallelism, 4)):
            executor = ReWOOExecutorAgent(
                name=f"{name}_executor_{i}",
                tools=available_tools,
                tool_aliases=tool_aliases,
            )
            executors.append(executor)

        # Create coordinator agent
        coordinator = SimpleAgent(
            name=f"{name}_coordinator",
            engine=AugLLMConfig(
                prompt_template="""
                You are a task coordinator managing parallel execution.

                Current plan: {plan}
                Completed tasks: {completed}
                Task results: {results}

                Determine:
                1. Which tasks can execute next
                2. How to assign tasks to executors
                3. When to trigger replanning

                Respond with task assignments.
                """
            ),
        )

        # Create validator agent
        validator = SimpleAgent(
            name=f"{name}_validator",
            engine=AugLLMConfig(
                prompt_template="""
                You are a result validator.

                Task: {task}
                Result: {result}
                Expected output: {expected}

                Validate if the result meets requirements.
                Provide validation status and any issues found.
                """
            ),
        )

        # Initialize MultiAgent with all agents
        all_agents = [planner, coordinator, validator, *executors]

        # Set custom state schema
        if "state_schema" not in kwargs:
            kwargs["state_schema"] = ReWOOTreeState

        super().__init__(
            agents=all_agents,
            name=name,
            execution_mode="infer",  # Will use intelligent routing
            **kwargs,
        )

        # Store agent references using object.__setattr__ to bypass Pydantic
        object.__setattr__(self, "planner", planner)
        object.__setattr__(self, "executors", {e.name: e for e in executors})
        object.__setattr__(self, "coordinator", coordinator)
        object.__setattr__(self, "validator", validator)
        object.__setattr__(self, "available_tools", available_tools)
        object.__setattr__(self, "tool_aliases", tool_aliases)
        object.__setattr__(self, "max_planning_depth", max_planning_depth)
        object.__setattr__(self, "max_parallelism", max_parallelism)

        # Configure execution flow
        self._configure_execution_flow()

    def _configure_execution_flow(self):
        """Configure the execution flow with proper branching."""
        # The flow is:
        # 1. Planner creates plan
        # 2. Coordinator assigns tasks
        # 3. Executors run in parallel
        # 4. Validator checks results
        # 5. Loop back to coordinator or complete

        # Add branch from coordinator to executors
        self.add_branch(
            source_agent=self.coordinator.name,
            condition="task_assignment",
            target_agents=list(self.executors.keys()),
        )

        # Add branch from validator back to coordinator or end
        self.add_branch(
            source_agent=self.validator.name,
            condition="validation_result",
            target_agents=[self.coordinator.name, "__end__"],
        )

    def add_tool_alias(
        self, alias: str, actual_tool: str, force_choice: bool = True, **params
    ):
        """Add a tool alias for forced tool choice."""
        tool_alias = ToolAlias(
            alias=alias,
            actual_tool=actual_tool,
            force_choice=force_choice,
            parameters=params,
        )

        # Update tool_aliases dict
        if hasattr(self, "tool_aliases"):
            self.tool_aliases[alias] = tool_alias

        # Update executors with new alias
        if hasattr(self, "executors"):
            for executor in self.executors.values():
                executor.tool_aliases[alias] = tool_alias

    async def create_and_execute_plan(self, problem: str) -> dict[str, Any]:
        """Create and execute a plan for the given problem."""
        # Initialize state
        initial_state = {
            "messages": [HumanMessage(content=problem)],
            "tool_aliases": self.tool_aliases,
            "planning_depth": 0,
        }

        # Execute through MultiAgent
        result = await self.arun(initial_state)

        return self._format_result(result)

    def _format_result(self, raw_result: Any) -> dict[str, Any]:
        """Format the execution result."""
        # Extract key information from the result
        if isinstance(raw_result, dict):
            return raw_result

        # Basic formatting
        return {
            "status": "completed",
            "result": str(raw_result),
            "execution_time": None,
            "tasks_completed": 0,
        }


class ParallelReWOOAgent(ReWOOTreeAgent):
    """Enhanced ReWOO agent with advanced parallel execution capabilities.

    This version focuses on maximizing parallelization by:
    - Creating multiple executor instances dynamically
    - Using Send objects for true parallel execution
    - Optimizing task distribution
    - Real-time performance tracking
    """

    def __init__(
        self, name: str = "parallel_rewoo", max_parallelism: int = 8, **kwargs
    ):
        # Set higher parallelism
        super().__init__(name=name, max_parallelism=max_parallelism, **kwargs)

        # Add performance tracking
        self.performance_metrics = {
            "total_tasks": 0,
            "parallel_executions": 0,
            "average_task_time": 0.0,
            "parallelization_efficiency": 0.0,
        }

    def _configure_execution_flow(self):
        """Configure for maximum parallelization."""
        super()._configure_execution_flow()

        # Add parallel execution pattern
        self.execution_mode = "parallel"

        # Configure for Send-based parallelization
        self.branches[self.coordinator.name] = {
            "condition": "parallel_distribution",
            "targets": list(self.executors.keys()),
            "mode": "send",  # Use Send objects for true parallelism
        }


def create_rewoo_agent_with_tools(
    tools: list[BaseTool],
    tool_aliases: dict[str, str] | None = None,
    max_parallelism: int = 4,
) -> ReWOOTreeAgent:
    """Factory function to create a ReWOO agent with tools.

    Args:
        tools: List of tools available to the agent
        tool_aliases: Mapping of alias names to actual tool names
        max_parallelism: Maximum parallel executions

    Returns:
        Configured ReWOOTreeAgent
    """
    agent = ReWOOTreeAgent(
        name="rewoo_agent", available_tools=tools, max_parallelism=max_parallelism
    )

    # Add tool aliases
    if tool_aliases:
        for alias, tool_name in tool_aliases.items():
            agent.add_tool_alias(alias, tool_name)

    return agent
