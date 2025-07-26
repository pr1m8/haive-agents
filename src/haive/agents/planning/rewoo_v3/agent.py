"""ReWOO V3 Agent using Enhanced MultiAgent V3 coordination.

This module implements the ReWOO (Reasoning WithOut Observation) methodology
using our proven patterns from Plan-and-Execute V3 success.

ReWOO Architecture:
1. Planner: Creates complete reasoning plan with evidence placeholders
2. Worker: Executes all tool calls to collect evidence
3. Solver: Synthesizes all evidence into final answer

Key advantages:
- Token efficiency (5x improvement over iterative methods)
- Parallel tool execution capability
- Robust to partial failures
- Fine-tuning friendly modular design
"""

import time

from haive.core.engine.aug_llm import AugLLMConfig

from haive.agents.multi.enhanced_multi_agent_v3 import EnhancedMultiAgent
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent

from .models import (
    EvidenceCollection,
    ReWOOPlan,
    ReWOOSolution,
    ReWOOV3Input,
    ReWOOV3Output,
)
from .prompts import planner_prompt, solver_prompt, worker_prompt
from .state import ReWOOV3State


class ReWOOV3Agent:
    """ReWOO V3 Agent using Enhanced MultiAgent V3 coordination.

    Implements ReWOO (Reasoning WithOut Observation) methodology:
    - Separates planning, execution, and synthesis phases
    - Plans complete solution upfront without tool observation
    - Executes all tool calls in batch/parallel
    - Synthesizes all evidence together for final answer

    This provides significant efficiency gains over traditional iterative
    agent approaches while maintaining high solution quality.
    """

    def __init__(
        self,
        name: str,
        config: AugLLMConfig,
        tools: list | None = None,
        max_steps: int = 10,
        **kwargs,
    ):
        """Initialize ReWOO V3 Agent.

        Args:
            name: Agent identifier
            config: Base LLM configuration for all sub-agents
            tools: Available tools for worker agent execution
            max_steps: Maximum planning steps allowed
            **kwargs: Additional configuration for Enhanced MultiAgent V3
        """
        self.name = name
        self.config = config
        self.tools = tools or []
        self.max_steps = max_steps

        # Create sub-agents using proven patterns
        self._setup_sub_agents()

        # Enhanced MultiAgent V3 coordination (sequential mode proven reliable)
        self.multi_agent = EnhancedMultiAgent(
            name=f"{name}_rewoo_coordinator",
            agents={
                "planner": self.planner,
                "worker": self.worker,
                "solver": self.solver,
            },
            execution_mode="sequential",  # planner → worker → solver
            state_schema=ReWOOV3State,
            **kwargs,
        )

        # Track execution statistics
        self.execution_stats = {
            "total_executions": 0,
            "average_execution_time": 0.0,
            "average_token_usage": 0,
            "success_rate": 0.0,
        }

    def _setup_sub_agents(self):
        """Create ReWOO sub-agents with proper prompt templates.

        CRITICAL: Uses prompt_template (NOT system_message) following
        proven Plan-and-Execute V3 pattern.
        """
        # Planner Agent: SimpleAgent with structured planning output
        planner_config = AugLLMConfig.model_copy(self.config)
        planner_config.prompt_template = planner_prompt  # NOT system_message!

        self.planner = SimpleAgent(
            name=f"{self.name}_planner",
            engine=planner_config,
            structured_output_model=ReWOOPlan,
        )

        # Worker Agent: ReactAgent with all available tools
        worker_config = AugLLMConfig.model_copy(self.config)
        worker_config.prompt_template = worker_prompt

        self.worker = ReactAgent(
            name=f"{self.name}_worker",
            engine=worker_config,
            tools=self.tools,
            structured_output_model=EvidenceCollection,
        )

        # Solver Agent: SimpleAgent for evidence synthesis
        solver_config = AugLLMConfig.model_copy(self.config)
        solver_config.prompt_template = solver_prompt

        self.solver = SimpleAgent(
            name=f"{self.name}_solver",
            engine=solver_config,
            structured_output_model=ReWOOSolution,
        )

    async def arun(
        self,
        query: str,
        context: str | None = None,
        max_steps: int | None = None,
        tools_preference: list[str] | None = None,
        **kwargs,
    ) -> ReWOOV3Output:
        """Execute ReWOO V3 workflow asynchronously.

        Args:
            query: User query to solve using ReWOO methodology
            context: Optional additional context
            max_steps: Override default max steps
            tools_preference: Preferred tools to use
            **kwargs: Additional arguments for Enhanced MultiAgent V3

        Returns:
            Structured output with complete ReWOO results and metadata
        """
        start_time = time.time()

        # Create ReWOO V3 input model
        ReWOOV3Input(
            query=query,
            context=context,
            max_steps=max_steps or self.max_steps,
            tools_preference=tools_preference,
        )

        # Create initial state with tool availability
        initial_state = ReWOOV3State(
            original_query=query,
            messages=[{"role": "user", "content": query}],
            tools_available=[
                tool.name if hasattr(tool, "name") else str(tool) for tool in self.tools
            ],
        )

        # Add context if provided
        if context:
            initial_state.execution_metadata["context"] = context

        try:
            # Enhanced MultiAgent V3 handles sequential coordination automatically
            # planner → worker → solver with automatic state transitions
            result = await self.multi_agent.arun(initial_state)

            # The result is the output schema, not the state itself
            # Get the actual state from the multi_agent
            if hasattr(self.multi_agent, "last_state"):
                result = self.multi_agent.last_state

            # Calculate execution timing
            total_time = time.time() - start_time
            planning_time = 0.0
            execution_time = 0.0
            solving_time = 0.0

            if (
                hasattr(result, "planning_completed_at")
                and result.planning_completed_at
            ):
                planning_time = (
                    result.planning_completed_at - result.started_at
                ).total_seconds()

            if (
                hasattr(result, "execution_completed_at")
                and result.execution_completed_at
            ):
                execution_time = (
                    result.execution_completed_at - result.planning_completed_at
                ).total_seconds()

            if hasattr(result, "solving_completed_at") and result.solving_completed_at:
                solving_time = (
                    result.solving_completed_at - result.execution_completed_at
                ).total_seconds()

            # Format structured output
            return self._format_output(
                result, query, total_time, planning_time, execution_time, solving_time
            )

        except Exception as e:
            # Handle errors gracefully
            return ReWOOV3Output(
                query=query,
                final_answer=f"ReWOO execution failed: {e!s}",
                confidence=0.0,
                steps_planned=0,
                evidence_collected=0,
                tools_used=[],
                total_execution_time=time.time() - start_time,
                planning_time=0.0,
                execution_time=0.0,
                solving_time=0.0,
                reasoning_process="Execution failed before completion",
                evidence_summary="No evidence collected due to error",
                limitations=[f"Execution error: {e!s}"],
                plan_id="error",
                solution_id="error",
            )

    def run(
        self,
        query: str,
        context: str | None = None,
        max_steps: int | None = None,
        tools_preference: list[str] | None = None,
        **kwargs,
    ) -> ReWOOV3Output:
        """Synchronous wrapper for ReWOO V3 execution.

        Args:
            query: User query to solve
            context: Optional additional context
            max_steps: Override default max steps
            tools_preference: Preferred tools to use
            **kwargs: Additional arguments

        Returns:
            Structured output with ReWOO results
        """
        import asyncio

        return asyncio.run(
            self.arun(query, context, max_steps, tools_preference, **kwargs)
        )

    def _format_output(
        self,
        result: ReWOOV3State,
        query: str,
        total_time: float,
        planning_time: float,
        execution_time: float,
        solving_time: float,
    ) -> ReWOOV3Output:
        """Format Enhanced MultiAgent V3 result into structured output.

        Args:
            result: Final state from Enhanced MultiAgent V3 execution
            query: Original query
            total_time: Total execution time
            planning_time: Time spent in planning phase
            execution_time: Time spent in execution phase
            solving_time: Time spent in solving phase

        Returns:
            Structured ReWOO V3 output with all results and metadata
        """
        # Extract final answer and confidence
        final_answer = "No solution generated"
        confidence = 0.0
        reasoning_process = "ReWOO workflow incomplete"
        plan_id = "unknown"
        solution_id = "unknown"

        if hasattr(result, "final_solution") and result.final_solution:
            try:
                solution = ReWOOSolution(**result.final_solution)
                final_answer = solution.final_answer
                confidence = solution.confidence
                reasoning_process = solution.reasoning
                solution_id = solution.solution_id
            except Exception as e:
                final_answer = f"Solution parsing error: {e}"

        # Extract planning information
        steps_planned = 0
        if hasattr(result, "reasoning_plan") and result.reasoning_plan:
            try:
                plan = ReWOOPlan(**result.reasoning_plan)
                steps_planned = plan.total_steps
                plan_id = plan.plan_id
            except Exception:
                pass

        # Extract evidence information
        evidence_collected = 0
        tools_used = []
        evidence_summary = "No evidence collected"

        if hasattr(result, "evidence_collection") and result.evidence_collection:
            try:
                collection = EvidenceCollection(**result.evidence_collection)
                evidence_collected = collection.success_count
                tools_used = collection.tools_used
                evidence_summary = collection.summary
            except Exception:
                pass

        # Update execution statistics
        self.execution_stats["total_executions"] += 1
        self.execution_stats["average_execution_time"] = (
            self.execution_stats["average_execution_time"]
            * (self.execution_stats["total_executions"] - 1)
            + total_time
        ) / self.execution_stats["total_executions"]

        # Calculate success rate
        if confidence > 0.5:  # Consider >0.5 confidence as success
            current_success_rate = self.execution_stats["success_rate"]
            total_executions = self.execution_stats["total_executions"]
            self.execution_stats["success_rate"] = (
                current_success_rate * (total_executions - 1) + 1.0
            ) / total_executions

        # Identify limitations
        limitations = []
        if confidence < 0.7:
            limitations.append(f"Low confidence solution ({confidence:.2f})")
        if evidence_collected == 0:
            limitations.append("No evidence successfully collected")
        if not tools_used:
            limitations.append("No tools were used in execution")
        if total_time > 60:
            limitations.append(f"Long execution time ({total_time:.2f}s)")

        return ReWOOV3Output(
            query=query,
            final_answer=final_answer,
            confidence=confidence,
            steps_planned=steps_planned,
            evidence_collected=evidence_collected,
            tools_used=tools_used,
            total_execution_time=total_time,
            planning_time=planning_time,
            execution_time=execution_time,
            solving_time=solving_time,
            reasoning_process=reasoning_process,
            evidence_summary=evidence_summary,
            limitations=limitations,
            plan_id=plan_id,
            solution_id=solution_id,
        )
