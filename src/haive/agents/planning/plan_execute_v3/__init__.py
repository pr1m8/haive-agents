"""Plan-and-Execute V3 Agent Package.

This package implements the Plan-and-Execute methodology using Enhanced MultiAgent V3,
providing a comprehensive solution for complex task planning and execution.

Key Components:
- PlanExecuteV3Agent: Main agent coordinator
- ExecutionPlan, StepExecution, PlanEvaluation: Structured output models
- PlanExecuteV3State: State management with computed fields
- System prompts for each sub-agent

Usage:
    from haive.agents.planning.plan_execute_v3 import PlanExecuteV3Agent

    agent = PlanExecuteV3Agent(tools=[search_tool, calculator])
    result = await agent.arun("Analyze market trends for renewable energy")
"""

from .agent import PlanExecuteV3Agent
from .models import (
    ExecutionPlan,
    PlanEvaluation,
    PlanExecuteInput,
    PlanExecuteOutput,
    PlanStep,
    RevisedPlan,
    StepExecution,
    StepStatus,
)
from .prompts import (
    EVALUATOR_SYSTEM_MESSAGE,
    EXECUTOR_SYSTEM_MESSAGE,
    PLANNER_SYSTEM_MESSAGE,
    REPLANNER_SYSTEM_MESSAGE,
    evaluator_prompt,
    executor_prompt,
    planner_prompt,
    replanner_prompt,
)
from .state import PlanExecuteV3State

__all__ = [
    "PlanExecuteV3Agent",
    "ExecutionPlan",
    "StepExecution",
    "PlanEvaluation",
    "RevisedPlan",
    "PlanExecuteInput",
    "PlanExecuteOutput",
    "PlanStep",
    "StepStatus",
    "PlanExecuteV3State",
    "planner_prompt",
    "executor_prompt",
    "evaluator_prompt",
    "replanner_prompt",
    "PLANNER_SYSTEM_MESSAGE",
    "EXECUTOR_SYSTEM_MESSAGE",
    "EVALUATOR_SYSTEM_MESSAGE",
    "REPLANNER_SYSTEM_MESSAGE",
]
