"""Simple planner agent - just prompt + structured output."""

from haive.core.engine.aug_llm import AugLLMConfig
from pydantic import Field

from haive.agents.planning_v2.base.models import Plan, Task
from haive.agents.planning_v2.base.planner.prompts import planner_prompt
from haive.agents.simple import SimpleAgent


class PlannerAgent(SimpleAgent):
    """Planner agent - literally just prompt template + structured output model."""

    name: str = Field(default="planner")

    engine: AugLLMConfig = Field(
        default_factory=lambda: AugLLMConfig(
            temperature=0.3, structured_output_model=Plan[Task]
        )
    )

    prompt_template: Any = Field(default_factory=lambda: planner_prompt)


# That's it. The agent is just:
# 1. ChatPromptTemplate (from prompts.py)
# 2. Structured output model (Plan[Task])
# 3. SimpleAgent base class
