"""LLM Compiler Agent - DAG-based parallel task execution with joins and replanning.

Architecture (Kim et al.):
  1. Planner: LLM generates a task DAG from user query
  2. Task Executor: Runs tasks in parallel as dependencies resolve (async)
  3. Joiner: Inspects results, decides to answer or replan

The executor streams tasks through the DAG - as soon as a task's dependencies
are satisfied it launches, maximizing parallelism without waiting for full waves.
"""

import asyncio
import logging
import traceback
from typing import Any

from haive.core.engine.agent.agent import Agent as AgentArchitecture
from haive.core.engine.aug_llm import compose_runnable
from langchain_core.messages import AIMessage, SystemMessage
from langchain_core.tools import BaseTool
from langgraph.graph import END, START, StateGraph

from .config import LLMCompilerAgentConfig
from .models import CompilerPlan, CompilerStep, FinalResponse, JoinerOutput, Replan
from .output_parser import LLMCompilerPlanParser
from .state import CompilerState

logger = logging.getLogger(__name__)


class LLMCompilerAgent(AgentArchitecture):
    """LLM Compiler: DAG planner + async parallel executor + joiner/replanner.

    Graph:
        START -> planner -> executor -> joiner --(replan)--> planner
                                                --(done)---> END
    """

    def __init__(self, config: LLMCompilerAgentConfig):
        super().__init__(config)
        self.config = config
        self.tools = config.tool_instances
        self.tool_map = {tool.name: tool for tool in self.tools}
        self.parser = LLMCompilerPlanParser(tools=self.tools)

        self.planner_llm = compose_runnable(config.planner_config)
        self.replanner_llm = compose_runnable(config.replanner_config)
        self.joiner_llm = compose_runnable(config.joiner_config)
        self.graph = None

    # ------------------------------------------------------------------
    # Node 1: Planner / Replanner
    # ------------------------------------------------------------------

    def plan(self, state: CompilerState) -> dict[str, Any]:
        """Generate or regenerate the task DAG."""
        is_replan = state.replan_count > 0

        if is_replan:
            llm = self.replanner_llm
            past = self._format_past_results(state)
            next_idx = state.get_highest_step_id() + 1
            inputs = {
                "query": state.query,
                "feedback": past,
                "next_idx": next_idx,
                "next_idx_plus_one": next_idx + 1,
                "next_idx_plus_two": next_idx + 2,
            }
            logger.info(f"Replanning (attempt {state.replan_count}), continuing from step {next_idx}")
        else:
            llm = self.planner_llm
            inputs = {"query": state.query}
            logger.info("Planning new DAG for query")

        # Inject tool descriptions
        if hasattr(llm, "partial"):
            llm = llm.partial(
                tool_descriptions=self._format_tool_descriptions(),
                num_tools=len(self.tools) + 1,
            )

        try:
            raw = llm.invoke(inputs)
            plan = self.parser.parse(str(raw) if not isinstance(raw, str) else raw)
            logger.info(f"Plan generated: {len(plan) if isinstance(plan, list) else 'parsed'} tasks")
            return {"plan": plan}
        except Exception as e:
            logger.warning(f"Planning failed: {e}, using fallback")
            return {"plan": self._fallback_plan(state.query)}

    # ------------------------------------------------------------------
    # Node 2: Async DAG Executor
    # ------------------------------------------------------------------

    def execute_tasks(self, state: CompilerState) -> dict[str, Any]:
        """Execute all tasks in the DAG, launching each as soon as deps resolve.

        Uses asyncio to run independent tasks concurrently. Tasks whose
        dependencies are already satisfied launch immediately; others wait
        on asyncio.Event signals from their predecessors.
        """
        if not state.plan:
            return {}

        executable = state.get_executable_steps()
        if not executable:
            return {}

        try:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                # Already in async context - run directly
                import concurrent.futures
                with concurrent.futures.ThreadPoolExecutor() as pool:
                    new_results = self._execute_dag_sync(state)
            else:
                new_results = asyncio.run(self._execute_dag_async(state))
        except RuntimeError:
            new_results = asyncio.run(self._execute_dag_async(state))

        results = {**state.results, **new_results}

        # Mark completed steps
        for step_id, result in new_results.items():
            step = state.plan.get_step_by_id(step_id)
            if step:
                step.add_result(str(result))

        is_done = bool(
            state.plan.get_join_step()
            and state.plan.get_join_step().id in results
        )

        logger.info(f"Executed {len(new_results)} tasks, total results: {len(results)}, done: {is_done}")
        return {"results": results, "is_done": is_done}

    async def _execute_dag_async(self, state: CompilerState) -> dict[int, Any]:
        """Run all executable tasks concurrently, respecting DAG dependencies.

        Instead of wave-based execution, this creates an asyncio.Event for each
        step. As soon as a step completes, it signals its event so dependent
        steps can start immediately.
        """
        plan = state.plan
        all_results = dict(state.results)  # Start with existing results
        events: dict[int, asyncio.Event] = {}
        new_results: dict[int, Any] = {}

        # Create events for all steps
        for step in plan.steps:
            events[step.id] = asyncio.Event()
            # If step already has results, signal immediately
            if step.id in all_results:
                events[step.id].set()

        async def run_step(step: CompilerStep) -> None:
            """Wait for dependencies, then execute."""
            # Wait for all dependencies
            dep_ids = step.dependencies
            if dep_ids:
                await asyncio.gather(*(events[d].wait() for d in dep_ids if d in events))

            if step.task.is_join:
                new_results[step.id] = "join"
                events[step.id].set()
                return

            # Execute
            try:
                result = await asyncio.to_thread(
                    self._execute_step, step, {**all_results, **new_results}, self.tool_map
                )
            except asyncio.TimeoutError:
                result = f"ERROR: Step {step.id} timed out"
            except Exception as e:
                result = f"ERROR: {e}"

            new_results[step.id] = result
            all_results[step.id] = result
            events[step.id].set()
            logger.debug(f"Step {step.id} ({step.task.tool_name}) completed")

        # Launch all incomplete steps concurrently
        tasks = []
        for step in plan.steps:
            if step.id not in state.results and not step.is_complete():
                tasks.append(asyncio.create_task(
                    asyncio.wait_for(run_step(step), timeout=self.config.max_execution_time)
                ))

        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)

        return new_results

    def _execute_dag_sync(self, state: CompilerState) -> dict[int, Any]:
        """Fallback synchronous wave-based execution when already in async context."""
        from concurrent.futures import ThreadPoolExecutor

        new_results: dict[int, Any] = {}
        all_results = dict(state.results)

        # Execute in waves until no more executable steps
        for _ in range(50):  # Safety limit
            executable = [
                s for s in state.plan.steps
                if s.id not in all_results and not s.is_complete() and s.can_execute(all_results)
            ]
            if not executable:
                break

            with ThreadPoolExecutor(max_workers=min(len(executable), 8)) as pool:
                futures = {
                    s.id: pool.submit(self._execute_step, s, all_results, self.tool_map)
                    for s in executable
                }
                for step_id, future in futures.items():
                    try:
                        result = future.result(timeout=self.config.max_execution_time)
                    except Exception as e:
                        result = f"ERROR: {e}"
                    new_results[step_id] = result
                    all_results[step_id] = result

        return new_results

    @staticmethod
    def _execute_step(
        step: CompilerStep, results: dict[int, Any], tool_map: dict[str, BaseTool]
    ) -> Any:
        """Execute a single step."""
        try:
            return step.execute(tool_map, results)
        except Exception as e:
            return f"ERROR: {e}\n{traceback.format_exc()}"

    # ------------------------------------------------------------------
    # Node 3: Joiner (answer or replan)
    # ------------------------------------------------------------------

    def join(self, state: CompilerState) -> dict[str, Any]:
        """Inspect results and decide: final answer or replan."""
        if not state.plan or not state.results:
            return {"replan": True, "replan_count": state.replan_count + 1}

        # Format executed tasks
        executed = []
        for step in state.plan.steps:
            if step.id in state.results:
                args_str = ", ".join(f'{k}="{v}"' for k, v in step.task.arguments.items())
                executed.append(f"{step.id}. {step.task.tool_name}({args_str}) -> {state.results[step.id]}")

        joiner_inputs = {
            "query": state.query,
            "executed_tasks": "\n".join(executed),
            "results": "\n".join(f"Step {k}: {v}" for k, v in state.results.items()),
        }

        try:
            output: JoinerOutput = self.joiner_llm.invoke(joiner_inputs)

            if isinstance(output.action, FinalResponse):
                logger.info("Joiner decided: final answer")
                return {"messages": [AIMessage(content=output.action.response)], "done": True}

            if isinstance(output.action, Replan):
                if state.replan_count >= self.config.max_replanning_attempts:
                    logger.warning(f"Max replans ({self.config.max_replanning_attempts}) reached, forcing answer")
                    return {
                        "messages": [AIMessage(content=f"Based on available results: {output.action.feedback}")],
                        "done": True,
                    }
                logger.info(f"Joiner decided: replan (reason: {output.action.feedback[:80]})")
                return {"replan": True, "replan_count": state.replan_count + 1}

        except Exception as e:
            logger.warning(f"Joiner failed: {e}, generating fallback")

        # Fallback
        return {
            "messages": [AIMessage(content=self._fallback_response(state))],
            "done": True,
        }

    # ------------------------------------------------------------------
    # Routing
    # ------------------------------------------------------------------

    def should_execute_more(self, state: CompilerState, config: dict[str, Any] | None = None) -> str:
        """Route after task execution."""
        if not state.plan:
            return "planner"
        if state.all_steps_complete():
            return "join"
        if state.get_executable_steps():
            return "execute_tasks"
        # Check for errors
        for result in state.results.values():
            if isinstance(result, str) and result.startswith("ERROR"):
                return "join"
        return "execute_tasks"

    def should_replan(self, state: CompilerState, config: dict[str, Any] | None = None) -> bool:
        """Route after joiner: replan or finish."""
        if not state.messages:
            return False
        if not state.results:
            return False
        return isinstance(state.messages[-1], SystemMessage)

    # ------------------------------------------------------------------
    # Graph
    # ------------------------------------------------------------------

    def setup_workflow(self) -> Any:
        """Build the LangGraph: planner -> executor -> joiner (-> replan loop)."""
        self.graph = StateGraph(CompilerState)

        self.graph.add_node("planner", self.plan)
        self.graph.add_node("execute_tasks", self.execute_tasks)
        self.graph.add_node("join", self.join)

        self.graph.add_edge(START, "planner")
        self.graph.add_edge("planner", "execute_tasks")

        self.graph.add_conditional_edges(
            "execute_tasks",
            self.should_execute_more,
            {"planner": "planner", "execute_tasks": "execute_tasks", "join": "join"},
        )

        self.graph.add_conditional_edges(
            "join",
            self.should_replan,
            {True: "planner", False: END},
        )

    # ------------------------------------------------------------------
    # Convenience methods
    # ------------------------------------------------------------------

    def run(self, query: str):
        """Run the compiler synchronously."""
        if not self.graph:
            self.setup_workflow()
        state = CompilerState(query=query)
        final = self.app.invoke(state, config=self.config.runnable_config, debug=True)
        return self._extract_answer(final)

    async def arun(self, query: str):
        """Run the compiler asynchronously."""
        if not self.graph:
            self.setup_workflow()
        state = CompilerState(query=query)
        final = await self.app.ainvoke(state, config=self.config.runnable_config, debug=True)
        return self._extract_answer(final)

    def stream(self, query: str):
        """Stream execution steps."""
        if not self.graph:
            self.setup_workflow()
        state = CompilerState(query=query)
        yield from self.app.stream(state, config=self.config.runnable_config, debug=True)

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _format_tool_descriptions(self) -> str:
        descs = []
        for i, tool in enumerate(self.tools):
            d = f"{i + 1}. {tool.name}: {tool.description}"
            if hasattr(tool, "args_schema") and tool.args_schema:
                props = getattr(tool.args_schema, "schema", {}).get("properties", {})
                if props:
                    d += "\n  Parameters:"
                    for pname, pinfo in props.items():
                        d += f"\n    - {pname} ({pinfo.get('type', 'any')}): {pinfo.get('description', '')}"
            descs.append(d)
        return "\n\n".join(descs)

    def _format_past_results(self, state: CompilerState) -> str:
        if not state.plan or not state.results:
            return "No previous results."
        lines = ["Previous execution:"]
        for step in state.plan.steps:
            if step.id in state.results:
                args_str = ", ".join(f'{k}="{v}"' for k, v in step.task.arguments.items())
                lines.append(f"{step.id}. {step.task.tool_name}({args_str})")
                lines.append(f"   Result: {state.results[step.id]}")
        return "\n".join(lines)

    def _fallback_plan(self, query: str) -> CompilerPlan:
        plan = CompilerPlan(description=f"Fallback for: {query}", status="not_started")
        search = next((t.name for t in self.tools if "search" in t.name.lower()), None)
        if search:
            plan.add_compiler_step(1, "Search", search, {"query": query})
            plan.add_compiler_step(2, "Join", "join", {}, [1])
        else:
            plan.add_compiler_step(1, "Join", "join", {})
        return plan

    def _fallback_response(self, state: CompilerState) -> str:
        if state.results:
            parts = [f"Step {k}: {v}" for k, v in state.results.items()]
            return f"Based on execution results:\n" + "\n".join(parts)
        return "Execution failed - no results available."

    @staticmethod
    def _extract_answer(final_state) -> str:
        if isinstance(final_state, dict) and final_state.get("messages"):
            for msg in reversed(final_state["messages"]):
                if isinstance(msg, AIMessage):
                    return msg.content
        return "No answer produced."
