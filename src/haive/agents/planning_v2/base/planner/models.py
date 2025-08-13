"""Concrete plan models for the planner agent."""

from haive.agents.planning_v2.base.models import Plan, Task


class TaskPlan(Plan[Task]):
    """Concrete plan implementation using Task steps.

    This is needed because OpenAI's function calling doesn't accept
    generic class names like Plan[Task] - it needs a simple name.
    """


# Force model rebuild to resolve forward references
TaskPlan.model_rebuild()
