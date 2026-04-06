"""Plan and Execute Agent v2 using MultiAgent pattern.

Flow: Planner → Executor → Replanner (loop until complete or max iterations)
"""

from typing import Any

from pydantic import Field

from haive.core.engine.aug_llm import AugLLMConfig
from haive.agents.multi.agent import MultiAgent
from haive.agents.planning.plan_and_execute.v2.models import Act, Plan, Response
from haive.agents.planning.plan_and_execute.v2.prompts import (
    PLANNER_PROMPT,
    EXECUTOR_PROMPT,
    REPLANNER_PROMPT,
)
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent


class PlanAndExecuteAgent(MultiAgent):
    """Plan and Execute agent using multi-agent sequential pattern.

    Flow: Planner → Executor → Replanner (loop until complete)

    Usage:
        agent = PlanAndExecuteAgent.create(tools=[search, calculator])
        result = agent.run("Research AI safety and write a summary")
    """

    @classmethod
    def create(cls, tools: list | None = None, name: str = "plan_and_execute", **kwargs):
        """Create P&E agent with default configuration."""
        planner = SimpleAgent(
            name="planner",
            engine=AugLLMConfig(
                temperature=0.7,
                system_message=PLANNER_PROMPT,
            ),
        )

        executor = ReactAgent(
            name="executor",
            engine=AugLLMConfig(
                temperature=0.3,
                system_message=EXECUTOR_PROMPT,
                tools=tools or [],
            ),
            max_iterations=5,
        )

        replanner = SimpleAgent(
            name="replanner",
            engine=AugLLMConfig(
                temperature=0.5,
                system_message=REPLANNER_PROMPT,
            ),
        )

        return cls(
            name=name,
            agents=[planner, executor, replanner],
            execution_mode="sequential",
            **kwargs,
        )
