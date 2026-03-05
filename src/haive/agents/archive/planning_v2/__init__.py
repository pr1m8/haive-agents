"""Planning V2 - Clean planning agent implementation.

This module provides a reorganized planning agent architecture with:
- Simple generic Plan models with TypeVar support
- Tree-based planning using enhanced tree_leaf structure
- Prebuilt MessagesState for agent state management
- PlannerAgent with comprehensive prompting and structured output
- Clean separation between models, state, and agents
"""

# Export base components
from haive.agents.planning_v2.base import (  # Simple models; Tree models; State; Planner agent
    MessagesState,
    Plan,
    PlanContent,
    PlanLeaf,
    PlannerAgent,
    PlanResult,
    PlanStatus,
    PlanTree,
    SimplePlanTree,
    Status,
    StepType,
    Task,
    TaskPlan,
    create_phased_plan,
    create_planner_prompt,
    create_simple_plan,
    planner_prompt,
)

__all__ = [
    # Simple models
    "Status",
    "Task",
    "Plan",
    "StepType",
    # Tree models
    "PlanStatus",
    "PlanContent",
    "PlanResult",
    "PlanLeaf",
    "PlanTree",
    "SimplePlanTree",
    "TaskPlan",
    "create_simple_plan",
    "create_phased_plan",
    # State
    "MessagesState",
    # Planner agent
    "PlannerAgent",
    "create_planner_prompt",
    "planner_prompt",
]
