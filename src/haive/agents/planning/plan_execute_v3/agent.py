"""Plan-and-Execute V3 Agent - Enhanced MultiAgent V3 Implementation.

This agent implements the Plan-and-Execute methodology using Enhanced MultiAgent V3,
separating planning, execution, evaluation, and replanning into distinct sub-agents.

Key Features:
- SimpleAgent for planning with structured output (ExecutionPlan)
- ReactAgent for step execution with tools
- SimpleAgent for evaluation and decision-making (PlanEvaluation)
- SimpleAgent for replanning when needed (RevisedPlan)
- Enhanced MultiAgent V3 for coordination
- Real component testing (no mocks)
"""

import asyncio
import time
from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from langchain_core.tools import Tool

from haive.agents.multi.enhanced_multi_agent_v3 import EnhancedMultiAgent
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent

from .models import (
    ExecutionPlan,
    Optional,
    PlanEvaluation,
    PlanExecuteInput,
    PlanExecuteOutput,
    RevisedPlan,
    StepExecution,
    from,
    import,
    typing,
)
from .prompts import evaluator_prompt, executor_prompt, planner_prompt, replanner_prompt
from .state import PlanExecuteV3State


class PlanExecuteV3Agent:
    """Plan-and-Execute V3 Agent using Enhanced MultiAgent V3.

    This agent separates planning and execution into distinct phases:
    1. Planner: Creates detailed execution plans (SimpleAgent -> ExecutionPlan)
    2. Executor: Executes individual steps with tools (ReactAgent -> StepExecution)
    3. Evaluator: Evaluates progress and decides next action (SimpleAgent -> PlanEvaluation)
    4. Replanner: Creates revised plans when needed (SimpleAgent -> RevisedPlan)

    The Enhanced MultiAgent V3 coordinates these sub-agents using conditional routing
    based on plan progress and evaluation decisions.

    Attributes:
        name: Agent name
        config: LLM configuration
        tools: Available tools for execution
        max_iterations: Maximum planning iterations
        max_steps_per_plan: Maximum steps per plan
    """

    def __init__(
        self,
        name: str = "plan_execute_v3",
        config: Optional[AugLLMConfig] = None,
        tools: list[Tool] | None = None,
        max_iterations: int = 5,
        max_steps_per_plan: int = 10,
    ):
        """Initialize Plan-and-Execute V3 agent.

        Args:
            name: Agent name
            config: LLM configuration (uses default if None)
            tools: Available tools for execution
            max_iterations: Maximum planning iterations
            max_steps_per_plan: Maximum steps per plan
        """
        self.name = name
        self.config = config or AugLLMConfig()
        self.tools = tools or []
        self.max_iterations = max_iterations
        self.max_steps_per_plan = max_steps_per_plan

        # Create sub-agents with proper prompt templates
        planner_config = AugLLMConfig.model_copy(self.config)
        planner_config.prompt_template = planner_prompt
        self.planner = SimpleAgent(
            name=f"{name}_planner",
            engine=planner_config,
            structured_output_model=ExecutionPlan,
        )

        executor_config = AugLLMConfig.model_copy(self.config)
        executor_config.prompt_template = executor_prompt
        self.executor = ReactAgent(
            name=f"{name}_executor",
            engine=executor_config,
            tools=self.tools,
            structured_output_model=StepExecution,
        )

        evaluator_config = AugLLMConfig.model_copy(self.config)
        evaluator_config.prompt_template = evaluator_prompt
        self.evaluator = SimpleAgent(
            name=f"{name}_evaluator",
            engine=evaluator_config,
            structured_output_model=PlanEvaluation,
        )

        replanner_config = AugLLMConfig.model_copy(self.config)
        replanner_config.prompt_template = replanner_prompt
        self.replanner = SimpleAgent(
            name=f"{name}_replanner",
            engine=replanner_config,
            structured_output_model=RevisedPlan,
        )

        # Create Enhanced MultiAgent V3 coordinator
        self.multi_agent = EnhancedMultiAgent(
            name=f"{name}_coordinatof",
            agents={
                "planner": self.planner,
                "executor": self.executor,
                "evaluator": self.evaluator,
            },
            execution_mode="sequential",  # Sequential: planner -> executor -> evaluator
            entry_point="planner",
            performance_mode=True,
            debug_mode=True,
            state_schema=PlanExecuteV3State,
        )

    def _setup_routing(self) -> None:
        """Set up conditional routing between sub-agents.
        """
        # Commented out for now - using sequential mode for testing

        # TODO: Re-enable conditional routing once basic sequential flow works
        # # After planning: always go to executor
        # self.multi_agent.add_edge("planner", "executor")

        # # After execution: conditional routing based on plan state
        # def should_evaluate(state: dict) -> str:
        #     """Determine if we should evaluate or continue executing."""
        #     # Get plan from state dict
        #     plan = state.get("plan")
        #     if not plan:
        #         return "evaluator"  # No plan, need evaluation

        #     # Check if we should evaluate based on state
        #     should_eval = state.get("should_evaluate", False)
        #     if should_eval:
        #         return "evaluator"

        #     # Check if there's a next step to execute
        #     if plan and hasattr(plan, 'get_next_step'):
        #         next_step = plan.get_next_step()
        #         if next_step:
        #             return "executor"  # Continue executing

        #     return "evaluator"  # Plan complete or stuck, evaluate

    # State processing is handled automatically by Enhanced MultiAgent V3
    # Agents with structured_output_model automatically update state
    # No manual processing needed

    async def arun(
        self,
        input_data: str | dict[str, Any] | PlanExecuteInput,
        state: Optional[PlanExecuteV3State] = None,
    ) -> PlanExecuteOutput:
        """Execute the Plan-and-Execute agent asynchronously.

        Args:
            input_data: Input objective/request
            state: Optional existing state (creates new if None)

        Returns:
            PlanExecuteOutput with final results
        """
        start_time = time.time()

        # Process input
        if isinstance(input_data, str):
            objective = input_data
            context = None
        elif isinstance(input_data, dict):
            objective = input_data.get("objective", str(input_data))
            context = input_data.get("context")
        elif isinstance(input_data, PlanExecuteInput):
            objective = input_data.objective
            context = input_data.context
        else:
            objective = str(input_data)
            context = None

        # Initialize or update state
        if state is None:
            state = PlanExecuteV3State(
                messages=[HumanMessage(content=objective)])

        if context:
            state.context["user_context"] = context

        # Execute with Enhanced MultiAgent V3
        try:
            await self.multi_agent.arun(state)

            # Extract final answer from state
            final_answer = (
                state.final_answer
                or "Plan execution completed but no final answer provided"
            )

            # Calculate metrics
            end_time = time.time()
            total_time = end_time - start_time

            # Count completed steps
            completed_steps = 0
            total_steps = 0
            if state.plan:
                total_steps = len(state.plan.steps)
                completed_steps = len(
                    [s for s in state.plan.steps if s.status.value == "completed"]
                )

            # Extract key findings
            key_findings = state.key_findings or []

            # Create output
            return PlanExecuteOutput(
                objective=objective,
                final_answer=final_answer,
                execution_summary=state.execution_summary,
                steps_completed=completed_steps,
                total_steps=total_steps,
                revisions_made=state.revision_count,
                total_execution_time=total_time,
                key_findings=key_findings,
                confidence_score=0.85,  # Default confidence
            )

        except Exception as e:
            # Handle execution errors
            return PlanExecuteOutput(
                objective=objective,
                final_answer=f"Execution failed: {
                    e!s}",
                execution_summary=f"Error occurred during plan execution: {
                    e!s}",
                steps_completed=0,
                total_steps=0,
                revisions_made=0,
                total_execution_time=time.time() -
                start_time,
                key_findings=[
                    f"Error: {
                        e!s}"],
                confidence_score=0.0,
            )

    def run(
        self,
        input_data: str | dict[str, Any] | PlanExecuteInput,
        state: Optional[PlanExecuteV3State] = None,
    ) -> PlanExecuteOutput:
        """Execute the Plan-and-Execute agent synchronously.

        Args:
            input_data: Input objective/request
            state: Optional existing state

        Returns:
            PlanExecuteOutput with final results
        """
        return asyncio.run(self.arun(input_data, state))

    def get_capabilities(self) -> dict[str, Any]:
        """Get agent capabilities description.
        """
        return {
            "name": self.name,
            "type": "Plan-and-Execute V3",
            "description": "Advanced planning and execution agent with iterative refinement",
            "sub_agents": {
                "planner": "Creates detailed execution plans",
                "executor": "Executes individual steps with tools",
                "evaluator": "Evaluates progress and makes decisions",
                "replanner": "Creates improved plans when needed",
            },
            "features": [
                "Structured planning with dependencies",
                "Tool-enabled step execution",
                "Progress evaluation and decision making",
                "Plan revision and improvement",
                "Real component testing",
                "Enhanced MultiAgent V3 coordination",
            ],
            "tools_available": len(
                self.tools),
            "max_iterations": self.max_iterations,
            "max_steps_per_plan": self.max_steps_per_plan,
        }
