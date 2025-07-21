"""Plan and Execute Agent v2 using ProperMultiAgent pattern."""

from haive.core.engine.aug_llm import AugLLMConfig

from haive.agents.multi.proper_base import ProperMultiAgent
from haive.agents.planning.plan_and_execute.v2.models import (
    Act,
    Any,
    ExecutionResult,
    Plan,
    Response,
    Step,
)
from haive.agents.planning.plan_and_execute.v2.prompts import (
    EXECUTOR_PROMPT,
    PLANNER_PROMPT,
    REPLANNER_PROMPT,
)
from haive.agents.planning.plan_and_execute.v2.state import PlanAndExecuteState
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent


class PlanAndExecuteAgent(ProperMultiAgent):
    """Plan and Execute agent using multi-agent sequential pattern.

    Flow: Planner → Executor → Replanner (loop until complete)
    """

    @classmethod
    def create_default(cls, tools: list = None, **kwargs):
        """Create P&E agent with default configuration."""

        # Create planner agent
        planner_agent = SimpleAgent(
            name="planner",
            engine=AugLLMConfig(
                name="planner",
                prompt_template=PLANNER_PROMPT,
                structured_output_model=Plan,
                structured_output_version="v2",
                temperature=0.7,
            ),
        )

        # Create executor agent (ReactAgent with tools)
        executor_agent = ReactAgent(
            name="executor",
            engine=AugLLMConfig(
                name="executor",
                prompt_template=EXECUTOR_PROMPT,
                structured_output_model=ExecutionResult,
                structured_output_version="v2",
                temperature=0.3,
            ),
            tools=tools or [],
        )

        # Create replanner agent
        replanner_agent = SimpleAgent(
            name="replanner",
            engine=AugLLMConfig(
                name="replanner",
                prompt_template=REPLANNER_PROMPT,
                structured_output_model=Act,
                structured_output_version="v2",
                temperature=0.5,
            ),
        )

        # Create sequential multi-agent
        name = kwargs.pop("name", "Plan and Execute Agent")
        return cls(
            name=name,
            agents=[planner_agent, executor_agent, replanner_agent],
            execution_mode="sequential",
            state_schema=PlanAndExecuteState,
            **kwargs
        )

    def should_continue_execution(self, state: PlanAndExecuteState) -> bool:
        """Check if execution should continue based on state."""
        if not state.plan:
            return False

        # Check if all steps are complete
        if all(step.status == "complete" for step in state.plan.steps):
            return False

        # Check if we have a final response
        if state.response and "final response" in state.response.lower():
            return False

        return True

    def get_next_action(self, state: PlanAndExecuteState) -> str:
        """Determine next action based on current state."""
        if not state.plan:
            return "planner"

        # Check if we have incomplete steps
        next_step = state.get_next_step()
        if next_step and next_step.status in ["not_started", "in_progress"]:
            return "executor"

        # Check if we need to replan
        if self.should_continue_execution(state):
            return "replanner"

        return "end"

    def process_execution_result(
        self, state: PlanAndExecuteState, result: ExecutionResult
    ) -> PlanAndExecuteState:
        """Process execution result and update state."""
        if result.step_id:
            # Find and update the step
            for step in state.plan.steps:
                if step.id == result.step_id:
                    step.add_result(result.result)
                    break

        # Update response
        state.response = result.result

        # Add to past steps if complete
        if result.step_completed:
            completed_step = state.get_next_step()
            if completed_step:
                state.update_past_steps(completed_step)

        return state

    def process_replan_result(
        self, state: PlanAndExecuteState, result: Act
    ) -> PlanAndExecuteState:
        """Process replanning result and update state."""
        if isinstance(result.action, Response):
            # Final response - we're done
            state.response = result.action.response
            state.final_response = result.action.response
        elif isinstance(result.action, Plan):
            # New plan - update steps
            state.plan = result.action
            state.plan.update_status()

        return state
