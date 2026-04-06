"""LLM Compiler Agent - DAG-based parallel task execution with structured planning.

Architecture (Kim et al., enhanced with Pydantic structured output):
  1. Planner: LLM generates a DAGPlan (Pydantic model) from user query
  2. Task Executor: Runs tasks in parallel as dependencies resolve (async)
  3. Joiner: Inspects results via JoinerDecision model, answers or replans

The planner uses AugLLMConfig's structured_output_model to get a proper
DAGPlan back from the LLM - no text parsing needed.
"""

import asyncio
import logging
import traceback
from concurrent.futures import ThreadPoolExecutor
from typing import Any

from langchain_core.messages import AIMessage
from langchain_core.tools import BaseTool
from langgraph.graph import END, START, StateGraph
from pydantic import Field, PrivateAttr

from haive.agents.base.agent import Agent
from haive.core.engine.aug_llm import AugLLMConfig

from .dag_models import DAGPlan, DAGTask, JoinerDecision
from .state import CompilerState

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------

PLANNER_SYSTEM = """You are a task planner that creates execution DAGs.

Available tools:
{tool_descriptions}

Given a user query, create a plan as a DAG of tasks:
- Each task calls one tool with specific arguments
- IMPORTANT: The 'args' dict MUST include the tool's required parameters with actual values
  For example, a calculator tool needs args like expression="99*77"
  A search tool needs args like query="what is Python"
- Tasks with no dependencies run in parallel (maximize this!)
- Use '$N' in argument values to reference task N's output
- The last task should be tool='join' to aggregate results
- Keep plans minimal"""

REPLANNER_SYSTEM = """You are improving a failed execution plan.

Available tools:
{tool_descriptions}

Previous execution results:
{feedback}

Create a NEW plan that:
- Does NOT repeat successful steps
- Fixes what went wrong
- Starts task IDs from {next_idx}
- Ends with a 'join' task"""

JOINER_SYSTEM = """You analyze execution results and decide the next action.

If results are sufficient to answer the query: action='answer', provide the response.
If results are insufficient or errored: action='replan', explain what's missing."""


class LLMCompilerAgent(Agent):
    """LLM Compiler: structured DAG planner + async parallel executor + joiner.

    Uses Pydantic structured output for both planning (DAGPlan) and
    joining (JoinerDecision). No text parsing needed.

    Graph: START -> planner -> executor -> joiner --(replan)--> planner
                                                   --(done)---> END
    """

    engine: AugLLMConfig | None = Field(
        default_factory=lambda: AugLLMConfig(name="llm_compiler_main"),
    )

    tools: list[Any] = Field(default_factory=list, description="Tools available to the compiler")
    max_execution_time: float = Field(default=60.0, description="Max seconds per task")
    max_replans: int = Field(default=3, description="Max replan attempts")
    planner_temperature: float = Field(default=0.3, description="Planner LLM temperature")
    joiner_temperature: float = Field(default=0.2, description="Joiner LLM temperature")

    _tool_map: dict[str, BaseTool] = PrivateAttr(default_factory=dict)
    _planner: Any = PrivateAttr(default=None)
    _replanner: Any = PrivateAttr(default=None)
    _joiner: Any = PrivateAttr(default=None)

    def model_post_init(self, __context: Any) -> None:
        super().model_post_init(__context)
        self._tool_map = {t.name: t for t in self.tools}
        # LLMs are built lazily on first compile/run to avoid blocking import

    def _build_llms(self) -> None:
        """Create planner/joiner LLMs with structured output."""
        from langchain_openai import ChatOpenAI
        from langchain_core.prompts import ChatPromptTemplate

        tool_desc = self._format_tool_descriptions()
        base_llm = ChatOpenAI(model="gpt-4o-mini")

        # Planner: system prompt with tools -> structured DAGPlan output
        planner_prompt = ChatPromptTemplate.from_messages([
            ("system", PLANNER_SYSTEM.format(tool_descriptions=tool_desc)),
            ("human", "{query}"),
        ])
        self._planner = planner_prompt | base_llm.with_structured_output(DAGPlan, method="function_calling")

        # Joiner: system prompt -> structured JoinerDecision output
        joiner_prompt = ChatPromptTemplate.from_messages([
            ("system", JOINER_SYSTEM),
            ("human", "{input}"),
        ])
        self._joiner = joiner_prompt | base_llm.with_structured_output(JoinerDecision, method="function_calling")

    # ------------------------------------------------------------------
    # Compile override (same pattern as DynamicSupervisor)
    # ------------------------------------------------------------------

    def compile(self, **kwargs) -> Any:
        # Build LLMs lazily on first compile
        if self._planner is None:
            self._build_llms()
        if not self._is_compiled or kwargs:
            if not hasattr(self, "graph") or self.graph is None:
                self._graph_built = False
                self._build_initial_graph()
            if not self.graph:
                raise RuntimeError("No graph to compile")
            self._app = self.graph.compile(
                checkpointer=self.checkpointer, store=self.store, **kwargs
            )
            self._compiled_graph = self._app
            self._is_compiled = True
        return self._compiled_graph or self._app

    # ------------------------------------------------------------------
    # Graph
    # ------------------------------------------------------------------

    def build_graph(self) -> StateGraph:
        """Build: planner -> executor -> joiner (-> replan loop)."""
        graph = StateGraph(CompilerState)

        graph.add_node("planner", self._plan_node)
        graph.add_node("execute_tasks", self._execute_node)
        graph.add_node("join", self._join_node)

        graph.add_edge(START, "planner")
        graph.add_edge("planner", "execute_tasks")

        graph.add_conditional_edges(
            "execute_tasks",
            self._route_after_execute,
            {"execute_tasks": "execute_tasks", "join": "join", "planner": "planner"},
        )

        graph.add_conditional_edges(
            "join",
            self._route_after_join,
            {True: "planner", False: END},
        )

        return graph

    # ------------------------------------------------------------------
    # Node 1: Planner (structured output -> DAGPlan)
    # ------------------------------------------------------------------

    def _plan_node(self, state: CompilerState) -> dict[str, Any]:
        """Generate a DAGPlan using structured output."""
        is_replan = state.replan_count > 0

        if is_replan:
            # Build replanner with context
            tool_desc = self._format_tool_descriptions()
            feedback = self._format_results(state)
            next_idx = max((s.id for s in state.plan.steps), default=0) + 1 if state.plan else 1

            replanner_cfg = AugLLMConfig(
                name="compiler_replanner",
                temperature=self.planner_temperature,
                system_message=REPLANNER_SYSTEM.format(
                    tool_descriptions=tool_desc,
                    feedback=feedback,
                    next_idx=next_idx,
                ),
                structured_output_model=DAGPlan,
            )
            llm = replanner_cfg.create_runnable()
            logger.info(f"Replanning (attempt {state.replan_count})")
        else:
            llm = self._planner
            logger.info("Planning new DAG")

        try:
            dag_plan: DAGPlan = llm.invoke({"query": state.query})

            logger.info(f"Plan: {len(dag_plan.tasks)} tasks, reasoning: {dag_plan.reasoning[:60]}")
            return {"dag_plan": dag_plan}

        except Exception as e:
            logger.warning(f"Planning failed: {e}")
            fallback = DAGPlan(
                tasks=[
                    DAGTask(id=1, tool=self._find_search_tool() or "join",
                            args={"query": state.query} if self._find_search_tool() else {},
                            thought="Fallback search"),
                    DAGTask(id=2, tool="join", depends_on=[1], thought="Aggregate"),
                ],
                reasoning=f"Fallback plan due to: {e}",
            )
            return {"dag_plan": fallback}

    # ------------------------------------------------------------------
    # Node 2: Async DAG Executor
    # ------------------------------------------------------------------

    def _execute_node(self, state: CompilerState) -> dict[str, Any]:
        """Execute DAG tasks in parallel as dependencies resolve."""
        dag = state.dag_plan
        if not dag or not dag.tasks:
            return {}

        # Find executable tasks (deps satisfied, not already done)
        executable = [
            t for t in dag.tasks
            if t.id not in state.results
            and t.tool != "join"
            and all(d in state.results for d in t.depends_on)
        ]

        if not executable:
            return {}

        # Execute in parallel
        new_results: dict[int, Any] = {}
        with ThreadPoolExecutor(max_workers=min(len(executable), 8)) as pool:
            futures = {}
            for task in executable:
                # Resolve $N references in args
                resolved_args = self._resolve_args(task.args, state.results)
                futures[task.id] = pool.submit(self._run_tool, task.tool, resolved_args)

            for task_id, future in futures.items():
                try:
                    new_results[task_id] = future.result(timeout=self.max_execution_time)
                except Exception as e:
                    new_results[task_id] = f"ERROR: {e}"

        results = {**state.results, **new_results}
        logger.info(f"Executed {len(new_results)} tasks ({len(results)} total)")
        return {"results": results}

    def _run_tool(self, tool_name: str, args: dict[str, Any]) -> Any:
        """Execute a single tool."""
        tool = self._tool_map.get(tool_name)
        if not tool:
            return f"ERROR: Tool '{tool_name}' not found. Available: {list(self._tool_map.keys())}"
        try:
            return tool.invoke(args)
        except Exception as e:
            return f"ERROR: {e}\n{traceback.format_exc()}"

    @staticmethod
    def _resolve_args(args: dict[str, Any], results: dict[int, Any]) -> dict[str, Any]:
        """Replace $N references with actual results."""
        import re
        resolved = {}
        for k, v in args.items():
            if isinstance(v, str):
                def replacer(m):
                    ref_id = int(m.group(1))
                    return str(results.get(ref_id, m.group(0)))
                resolved[k] = re.sub(r'\$(\d+)', replacer, v)
            else:
                resolved[k] = v
        return resolved

    # ------------------------------------------------------------------
    # Node 3: Joiner (structured output -> JoinerDecision)
    # ------------------------------------------------------------------

    def _join_node(self, state: CompilerState) -> dict[str, Any]:
        """Decide: answer or replan."""
        if not state.results:
            if state.replan_count >= self.max_replans:
                return {"messages": [AIMessage(content="Unable to produce results.")], "done": True}
            return {"replan_count": state.replan_count + 1}

        # Format results for joiner
        result_lines = []
        for task in (state.dag_plan.tasks if state.dag_plan else []):
            if task.id in state.results:
                result_lines.append(f"Task {task.id} ({task.tool}): {state.results[task.id]}")

        prompt = f"Query: {state.query}\n\nResults:\n" + "\n".join(result_lines)

        try:
            decision: JoinerDecision = self._joiner.invoke({"input": prompt})

            if isinstance(decision, JoinerDecision):
                if decision.action == "answer":
                    return {"messages": [AIMessage(content=decision.response)], "done": True}
                else:
                    if state.replan_count >= self.max_replans:
                        return {"messages": [AIMessage(content=f"Max replans reached. Best answer: {decision.feedback}")], "done": True}
                    return {"replan_count": state.replan_count + 1}

            # Fallback if not proper JoinerDecision
            return {"messages": [AIMessage(content=str(decision))], "done": True}

        except Exception as e:
            logger.warning(f"Joiner failed: {e}")
            summary = "\n".join(f"- {v}" for v in state.results.values())
            return {"messages": [AIMessage(content=f"Results:\n{summary}")], "done": True}

    # ------------------------------------------------------------------
    # Routing
    # ------------------------------------------------------------------

    def _route_after_execute(self, state: CompilerState) -> str:
        if not state.dag_plan:
            return "planner"
        # Check if all non-join tasks are done
        non_join = [t for t in state.dag_plan.tasks if t.tool != "join"]
        all_done = all(t.id in state.results for t in non_join)
        if all_done:
            return "join"
        # Check if more tasks can execute
        executable = [
            t for t in state.dag_plan.tasks
            if t.id not in state.results and t.tool != "join"
            and all(d in state.results for d in t.depends_on)
        ]
        return "execute_tasks" if executable else "join"

    @staticmethod
    def _route_after_join(state: CompilerState) -> bool:
        """True = replan, False = done."""
        if getattr(state, "done", False):
            return False  # Joiner said we're done
        if state.messages:
            return False  # We have a final answer
        # Only replan if joiner explicitly asked for it
        return state.replan_count > 0

    def _plan_from_text(self, text: str, query: str) -> DAGPlan:
        """Create a DAGPlan from LLM text output when structured output fails."""
        # Simple heuristic: use first available tool with the query
        tasks = []
        for i, t in enumerate(self.tools):
            tasks.append(DAGTask(id=i+1, tool=t.name, args={"query": query}, thought=f"Use {t.name}"))
        tasks.append(DAGTask(id=len(tasks)+1, tool="join", depends_on=[t.id for t in tasks], thought="Aggregate"))
        return DAGPlan(tasks=tasks, reasoning=f"Plan from text: {text[:50]}")

    # ------------------------------------------------------------------
    # Convenience
    # ------------------------------------------------------------------

    def run_query(self, query: str) -> str:
        """Run the compiler on a query string."""
        if not self._is_compiled:
            self.compile()
        import uuid
        state = CompilerState(query=query)
        config = {"configurable": {"thread_id": str(uuid.uuid4())}, "recursion_limit": 30}
        final = self._app.invoke(state.model_dump(), config=config)
        return self._extract_answer(final)

    async def arun_query(self, query: str) -> str:
        """Run the compiler asynchronously."""
        if not self._is_compiled:
            self.compile()
        import uuid
        state = CompilerState(query=query)
        config = {"configurable": {"thread_id": str(uuid.uuid4())}, "recursion_limit": 30}
        final = await self._app.ainvoke(state.model_dump(), config=config)
        return self._extract_answer(final)

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _format_tool_descriptions(self) -> str:
        lines = []
        for i, t in enumerate(self.tools):
            line = f"{i+1}. {t.name}: {t.description}"
            if hasattr(t, "args_schema") and t.args_schema:
                try:
                    schema = t.args_schema.model_json_schema()
                    props = schema.get("properties", {})
                    if props:
                        arg_strs = [f"{k} ({v.get('type', 'str')})" for k, v in props.items()]
                        line += "\n   Args: " + ", ".join(arg_strs)
                except Exception:
                    pass
            lines.append(line)
        return "\n".join(lines)

    def _format_results(self, state: CompilerState) -> str:
        if not state.results:
            return "No results."
        return "\n".join(f"Task {k}: {v}" for k, v in state.results.items())

    def _find_search_tool(self) -> str | None:
        return next((t.name for t in self.tools if "search" in t.name.lower()), None)

    @staticmethod
    def _extract_answer(final_state) -> str:
        if isinstance(final_state, dict) and final_state.get("messages"):
            for msg in reversed(final_state["messages"]):
                if isinstance(msg, AIMessage):
                    return msg.content
        return "No answer produced."

    class Config:
        arbitrary_types_allowed = True
