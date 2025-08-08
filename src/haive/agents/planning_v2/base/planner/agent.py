"""Planner agent - just prompt template + structured output model."""

from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from pydantic import Field

from haive.agents.planning_v2.base.planner.models import TaskPlan
from haive.agents.planning_v2.base.planner.prompts import planner_prompt
from haive.agents.simple import SimpleAgent


class PlannerAgent(SimpleAgent):
    """Planner agent = ChatPromptTemplate + TaskPlan structured output."""

    name: str = Field(default="planner")

    engine: AugLLMConfig = Field(
        default_factory=lambda: AugLLMConfig(
            temperature=0.3,
            structured_output_model=TaskPlan,  # Use concrete class, not generic
        )
    )

    prompt_template: Any = Field(default_factory=lambda: planner_prompt)
