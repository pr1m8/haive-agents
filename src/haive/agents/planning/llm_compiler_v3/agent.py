"""LLM Compiler V3 Agent using Enhanced MultiAgent V3 Architecture.

This implementation modernizes the LLM Compiler pattern by using Enhanced MultiAgent V3
for simplified architecture, better maintainability, and consistent patterns.
"""

import asyncio
import time
from typing import Any

from haive.agents.multi.enhanced_multi_agent_v3 import EnhancedMultiAgent
from haive.agents.planning.llm_compiler_v3.config import LLMCompilerV3Config
from haive.agents.planning.llm_compiler_v3.models import (
    CompilerInput,
    CompilerOutput,
    CompilerPlan,
    CompilerTask,
    ParallelExecutionResult,
    ReplanRequest,
)
from haive.agents.planning.llm_compiler_v3.prompts import (
    LLM_COMPILER_V3_PROMPTS,
    get_executor_prompt,
    get_joiner_prompt,
    get_planner_prompt,
)
from haive.agents.planning.llm_compiler_v3.state import LLMCompilerStateSchema
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent


class LLMCompilerV3Agent:
    """LLM Compiler V3 Agent using Enhanced MultiAgent V3.

    This agent implements the LLM Compiler pattern with three specialized sub-agents:
    1. Planner - Decomposes tasks into parallelizable DAG
    2. Task Fetcher - Manages task coordination and dependency resolution
    3. Parallel Executor - Executes individual tasks with tools
    4. Joiner - Synthesizes results into final answer
    """

    def __init__(
        self,
        name: str = "llm_compiler_v3",
        config: LLMCompilerV3Config | None = None,
        tools: list | None = None,
        **kwargs,
    ):
        """Initialize LLM Compiler V3 Agent.

        Args:
            name: Agent name
            config: Configuration for the compiler
            tools: List of tools available for task execution
            **kwargs: Additional arguments for Enhanced MultiAgent V3
        """
        self.name = name
        self.config = config or LLMCompilerV3Config(name=name)
        self.tools = tools or []
        self.tool_map = {tool.name: tool for tool in self.tools}

        # Setup specialized sub-agents
        self._setup_agents()

        # Create Enhanced MultiAgent V3 coordinator
        self.multi_agent = EnhancedMultiAgent(
            name=name,
            agents=self.agents,
            execution_mode="conditional",  # Based on execution state
            state_schema=LLMCompilerStateSchema,
            **kwargs,
        )

    def _setup_agents(self):
        """Setup specialized sub-agents for the LLM Compiler pattern."""
        # Planner Agent - Creates execution DAG
        self.planner = SimpleAgent(
            name=f"{self.name}_planner",
            engine=self.config.planner_engine,
            structured_output_model=CompilerPlan,
            system_message=LLM_COMPILER_V3_PROMPTS["planner"],
        )

        # Task Fetcher Agent - Manages task coordination
        self.task_fetcher = ReactAgent(
            name=f"{self.name}_task_fetcher",
            engine=self.config.task_fetcher_engine,
            tools=[],  # No external tools needed for coordination
            system_message=LLM_COMPILER_V3_PROMPTS["task_fetcher"],
        )

        # Parallel Executor Agent - Executes individual tasks
        self.executor = ReactAgent(
            name=f"{self.name}_executor",
            engine=self.config.executor_engine,
            tools=self.tools,  # All available tools
            system_message=LLM_COMPILER_V3_PROMPTS["parallel_executor"],
        )

        # Joiner Agent - Synthesizes final results
        self.joiner = SimpleAgent(
            name=f"{self.name}_joiner",
            engine=self.config.joiner_engine,
            structured_output_model=CompilerOutput,
            system_message=LLM_COMPILER_V3_PROMPTS["joinef"],
        )

        # Agent registry for Enhanced MultiAgent V3
        self.agents = {
            "planner": self.planner,
            "task_fetcher": self.task_fetcher,
            "parallel_executor": self.executor,
            "joiner": self.joiner,
        }

    async def arun(
        self, query: str, context: dict[str, Any] | None = None, **kwargs
    ) -> CompilerOutput:
        """Execute LLM Compiler pattern asynchronously.

        Args:
            query: User query to process
            context: Additional context
            **kwargs: Additional execution parameters

        Returns:
            CompilerOutput with final results and execution details
        """
        # Create input model
        compiler_input = CompilerInput(
            query=query,
            context=context,
            execution_preferences=kwargs.get("execution_preferences"),
        )

        # Initialize state
        initial_state = LLMCompilerStateSchema(
            original_query=query,
            max_parallel_tasks=self.config.max_parallel_tasks,
            execution_start_time=time.time(),
        )

        # Execute the pattern through phases
        try:
            # Phase 1: Planning
            state = await self._planning_phase(initial_state, compiler_input)

            # Phase 2: Execution Loop
            state = await self._execution_phase(state)

            # Phase 3: Result Synthesis
            final_output = await self._synthesis_phase(state)

            return final_output

        except Exception as e:
            # Handle errors gracefully
            return self._create_error_output(str(e), initial_state)

    def run(
        self, query: str, context: dict[str, Any] | None = None, **kwargs
    ) -> CompilerOutput:
        """Execute LLM Compiler pattern synchronously."""
        return asyncio.run(self.arun(query, context, **kwargs))

    async def _planning_phase(
        self, state: LLMCompilerStateSchema, compiler_input: CompilerInput
    ) -> LLMCompilerStateSchema:
        """Execute planning phase to create task DAG."""
        # Generate contextual planner prompt
        planner_prompt = get_planner_prompt(
            query=compiler_input.query,
            available_tools=[tool.name for tool in self.tools],
        )

        # Execute planner agent
        plan_result = await self.planner.arun(planner_prompt)

        # Validate and store plan
        if isinstance(plan_result, CompilerPlan):
            state.current_plan = plan_result
        else:
            # Fallback parsing if needed
            state.current_plan = self._parse_plan_from_result(plan_result)

        # Validate plan dependencies
        validation_errors = state.current_plan.validate_dependencies()
        if validation_errors:
            # Handle validation errors - could trigger replanning
            state.execution_metadata["plan_validation_errors"] = validation_errors

        # Update task states
        state.update_ready_tasks()
        state.current_agent = "task_fetcher"
        state.next_agent = "parallel_executor"

        return state

    async def _execution_phase(
        self, state: LLMCompilerStateSchema
    ) -> LLMCompilerStateSchema:
        """Execute tasks with parallel coordination."""
        max_iterations = 20  # Prevent infinite loops
        iteration = 0

        while not state.is_execution_complete() and iteration < max_iterations:
            iteration += 1

            # Check if we should replan
            if (
                state.should_replan()
                and state.replan_count < self.config.max_replan_attempts
            ):
                state = await self._replan_phase(state)
                continue

            # Get next executable tasks
            next_tasks = state.get_next_executable_tasks()

            if not next_tasks:
                # No tasks ready - check if we're stuck
                if not state.currently_executing:
                    # Completely stuck - may need replanning or completion
                    break
                # Wait for current tasks to complete
                await asyncio.sleep(0.1)
                continue

            # Execute tasks in parallel
            await self._execute_parallel_tasks(state, next_tasks)

            # Update task states
            state.update_ready_tasks()

        return state

    async def _execute_parallel_tasks(
        self, state: LLMCompilerStateSchema, tasks: list[CompilerTask]
    ) -> None:
        """Execute multiple tasks in parallel."""
        # Limit tasks based on configuration
        tasks_to_execute = tasks[
            : state.max_parallel_tasks - len(state.currently_executing)
        ]

        if not tasks_to_execute:
            return

        # Mark tasks as executing
        for task in tasks_to_execute:
            state.mark_task_executing(task.task_id)

        # Create execution coroutines
        execution_tasks = [
            self._execute_single_task(state, task) for task in tasks_to_execute
        ]

        # Execute tasks concurrently
        results = await asyncio.gather(*execution_tasks, return_exceptions=True)

        # Process results
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                # Handle execution exception
                error_result = ParallelExecutionResult(
                    task_id=tasks_to_execute[i].task_id,
                    success=False,
                    result=None,
                    error_message=str(result),
                    execution_time=0.0,
                    tool_name=tasks_to_execute[i].tool_name,
                )
                state.add_execution_result(error_result)
            else:
                # Add successful result
                state.add_execution_result(result)

    async def _execute_single_task(
        self, state: LLMCompilerStateSchema, task: CompilerTask
    ) -> ParallelExecutionResult:
        """Execute a single task with timing and error handling."""
        start_time = time.time()

        try:
            # Resolve task arguments with dependencies
            resolved_args = state.resolve_task_arguments(task)

            # Handle join task specially
            if task.is_join_task:
                result = "join_completed"
            # Execute with appropriate tool
            elif task.tool_name in self.tool_map:
                tool = self.tool_map[task.tool_name]
                result = await self._execute_tool(tool, resolved_args)
            else:
                # Use executor agent for complex tool operations
                executor_prompt = get_executor_prompt(
                    current_task=task.model_dump(),
                    tool_name=task.tool_name,
                    resolved_arguments=resolved_args,
                    available_tools=list(self.tool_map.keys()),
                )
                result = await self.executor.arun(executor_prompt)

            execution_time = time.time() - start_time

            return ParallelExecutionResult(
                task_id=task.task_id,
                success=True,
                result=result,
                error_message=None,
                execution_time=execution_time,
                tool_name=task.tool_name,
                metadata={
                    "resolved_arguments": resolved_args,
                    "task_description": task.description,
                },
            )

        except Exception as e:
            execution_time = time.time() - start_time

            return ParallelExecutionResult(
                task_id=task.task_id,
                success=False,
                result=None,
                error_message=str(e),
                execution_time=execution_time,
                tool_name=task.tool_name,
                metadata={
                    "task_description": task.description,
                    "attempted_arguments": task.arguments,
                },
            )

    async def _execute_tool(self, tool, arguments: dict[str, Any]) -> Any:
        """Execute a tool with given arguments."""
        # Handle both sync and async tools
        if hasattr(tool, "ainvoke"):
            return await tool.ainvoke(arguments)
        # Run sync tool in thread pool to avoid blocking
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, tool.invoke, arguments)

    async def _synthesis_phase(self, state: LLMCompilerStateSchema) -> CompilerOutput:
        """Synthesize final results using joiner agent."""
        # Calculate total execution time
        total_time = time.time() - (
            state.execution_start_time.timestamp() if state.execution_start_time else 0
        )
        state.total_execution_time = total_time

        # Generate joiner prompt with all execution context
        joiner_prompt = get_joiner_prompt(
            original_query=state.original_query,
            execution_results=[r.model_dump() for r in state.execution_results],
            successful_tasks=[r.task_id for r in state.get_successful_results()],
            failed_tasks=[r.task_id for r in state.get_failed_results()],
        )

        # Execute joiner agent
        try:
            final_result = await self.joiner.arun(joiner_prompt)

            if isinstance(final_result, CompilerOutput):
                return final_result
            # Create output from string result
            return CompilerOutput(
                final_answer=str(final_result),
                execution_plan=state.current_plan,
                execution_results=state.execution_results,
                total_execution_time=total_time,
                tasks_executed=len(state.execution_results),
                reasoning_trace=[
                    f"Task {r.task_id}: {r.tool_name}" for r in state.execution_results
                ],
                metadata=state.execution_metadata,
            )

        except Exception as e:
            # Fallback synthesis
            return self._create_fallback_output(state, str(e))

    async def _replan_phase(
        self, state: LLMCompilerStateSchema
    ) -> LLMCompilerStateSchema:
        """Execute replanning when execution encounters issues."""
        # Create replan request
        replan_request = ReplanRequest(
            feedback=f"Replanning needed due to failed tasks: {state.failed_task_ids}",
            failed_tasks=state.failed_task_ids,
            partial_results=state.task_results,
        )

        state.replan_requests.append(replan_request)
        state.replan_count += 1

        # Generate new plan with feedback
        replanner_input = CompilerInput(
            query=state.original_query,
            context={
                "previous_plan": (
                    state.current_plan.model_dump() if state.current_plan else None
                ),
                "failed_tasks": state.failed_task_ids,
                "successful_results": {
                    r.task_id: r.result for r in state.get_successful_results()
                },
                "replan_feedback": replan_request.feedback,
            },
        )

        # Execute planning phase again
        state = await self._planning_phase(state, replanner_input)

        # Reset execution state for new plan
        state.currently_executing = []
        state.ready_tasks = []
        state.blocked_tasks = []

        return state

    def _parse_plan_from_result(self, result: Any) -> CompilerPlan:
        """Fallback parsing of plan from agent result."""
        # Implementation depends on how the agent returns results
        # This is a simplified version
        return CompilerPlan(
            plan_id=f"fallback_plan_{int(time.time())}",
            description="Fallback plan created from agent result",
            tasks=[],  # Would need parsing logic here
        )

    def _create_error_output(
        self, error_message: str, state: LLMCompilerStateSchema
    ) -> CompilerOutput:
        """Create error output when execution fails."""
        return CompilerOutput(
            final_answer=f"Execution failed: {error_message}",
            execution_plan=state.current_plan
            or CompilerPlan(plan_id="error_plan", description="Error plan", tasks=[]),
            execution_results=[],
            total_execution_time=0.0,
            tasks_executed=0,
            metadata={"error": error_message},
        )

    def _create_fallback_output(
        self, state: LLMCompilerStateSchema, error_message: str
    ) -> CompilerOutput:
        """Create fallback output when synthesis fails."""
        # Synthesize basic answer from successful results
        successful_results = state.get_successful_results()

        if successful_results:
            answer_parts = []
            for result in successful_results:
                answer_parts.append(f"{result.task_id}: {result.result}")
            final_answer = "\\n".join(answer_parts)
        else:
            final_answer = (
                f"Unable to complete task due to synthesis error: {error_message}"
            )

        return CompilerOutput(
            final_answer=final_answer,
            execution_plan=state.current_plan,
            execution_results=state.execution_results,
            total_execution_time=state.total_execution_time,
            tasks_executed=len(state.execution_results),
            metadata={"synthesis_error": error_message, "fallback_synthesis": True},
        )
