"""LLM Compiler Agent - DAG-based parallel task execution.

Composes SimpleAgent (planner with structured DAGPlan output) +
parallel tool executor + SimpleAgent (joiner with JoinerDecision output).

Graph: START -> plan -> execute -> join --(replan)--> plan
                                       --(done)----> END

Uses BaseGraph from haive.core, follows the standard agent pattern.
"""

import logging
import re
import traceback
from concurrent.futures import ThreadPoolExecutor
from typing import Any

from langchain_core.messages import AIMessage
from langgraph.graph import END, START
from pydantic import ConfigDict, Field, PrivateAttr

from haive.agents.base.agent import Agent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.state_graph.base_graph2 import BaseGraph

from .dag_models import DAGPlan, DAGTask, JoinerDecision
from .state import CompilerState

logger = logging.getLogger(__name__)

# -- Prompts --
PLANNER_PROMPT = """You are a task planner that creates execution DAGs.

Available tools:
{tool_descriptions}

Create a plan as a DAG of tasks. Each task calls one tool with specific arguments.
The 'args' dict MUST include the tool's required parameters with actual values.
Tasks with no dependencies run in parallel. End with tool='join' to aggregate.
Keep plans minimal."""

JOINER_PROMPT = """You analyze execution results and decide the next action.

If results are sufficient: action='answer', provide the response.
If insufficient or errors: action='replan', explain what's missing."""


class LLMCompilerAgent(Agent):
    """DAG planner + parallel executor + joiner.

    Composes:
    - Planner: SimpleAgent with structured output (DAGPlan)
    - Executor: ThreadPoolExecutor running tools in parallel
    - Joiner: SimpleAgent with structured output (JoinerDecision)
    """

    # ---- Config ----
    tools: list[Any] = Field(default_factory=list, description="Tools for execution")
    model: str = Field(default="gpt-4o-mini")
    planner_temperature: float = Field(default=0.3)
    joiner_temperature: float = Field(default=0.2)
    max_execution_time: float = Field(default=60.0)
    max_replans: int = Field(default=3)

    # ---- Runtime ----
    _planner: Any = PrivateAttr(default=None)
    _joiner: Any = PrivateAttr(default=None)
    _tool_map: dict = PrivateAttr(default_factory=dict)

    model_config = ConfigDict(arbitrary_types_allowed=True)

    # ------------------------------------------------------------------
    # Lazy init
    # ------------------------------------------------------------------

    def _ensure_agents(self) -> None:
        if self._planner is not None:
            return

        from langchain_openai import ChatOpenAI
        from langchain_core.prompts import ChatPromptTemplate

        self._tool_map = {t.name: t for t in self.tools}
        tool_desc = self._format_tool_descriptions()

        llm = ChatOpenAI(model=self.model)

        # Planner: structured output -> DAGPlan
        planner_prompt = ChatPromptTemplate.from_messages([
            ("system", PLANNER_PROMPT.format(tool_descriptions=tool_desc)),
            ("human", "{query}"),
        ])
        self._planner = planner_prompt | llm.with_structured_output(
            DAGPlan, method="function_calling"
        )

        # Joiner: structured output -> JoinerDecision
        joiner_prompt = ChatPromptTemplate.from_messages([
            ("system", JOINER_PROMPT),
            ("human", "{input}"),
        ])
        self._joiner = joiner_prompt | llm.with_structured_output(
            JoinerDecision, method="function_calling"
        )

    # ------------------------------------------------------------------
    # Graph nodes
    # ------------------------------------------------------------------

    def _plan(self, state: CompilerState) -> dict[str, Any]:
        """Generate DAGPlan via structured output."""
        try:
            dag: DAGPlan = self._planner.invoke({"query": state.query})
            logger.info(f"Plan: {len(dag.tasks)} tasks")
            return {"dag_plan": dag}
        except Exception as e:
            logger.warning(f"Planning failed: {e}")
            # Fallback: use first tool with query
            tasks = []
            for i, t in enumerate(self.tools):
                tasks.append(DAGTask(id=i+1, tool=t.name, args={"query": state.query}))
            tasks.append(DAGTask(id=len(tasks)+1, tool="join", depends_on=[t.id for t in tasks]))
            return {"dag_plan": DAGPlan(tasks=tasks, reasoning=f"Fallback: {e}")}

    def _execute(self, state: CompilerState) -> dict[str, Any]:
        """Execute tasks in parallel as dependencies resolve."""
        dag = state.dag_plan
        if not dag:
            return {}

        executable = [
            t for t in dag.tasks
            if t.id not in state.results and t.tool != "join"
            and all(d in state.results for d in t.depends_on)
        ]
        if not executable:
            return {}

        new_results: dict[int, Any] = {}
        with ThreadPoolExecutor(max_workers=min(len(executable), 8)) as pool:
            futures = {}
            for task in executable:
                resolved = self._resolve_args(task.args, state.results)
                futures[task.id] = pool.submit(self._run_tool, task.tool, resolved)
            for tid, future in futures.items():
                try:
                    new_results[tid] = future.result(timeout=self.max_execution_time)
                except Exception as e:
                    new_results[tid] = f"ERROR: {e}"

        results = {**state.results, **new_results}
        logger.info(f"Executed {len(new_results)} tasks, {len(results)} total")
        return {"results": results}

    def _join(self, state: CompilerState) -> dict[str, Any]:
        """Decide: answer or replan."""
        if not state.results:
            if state.replan_count >= self.max_replans:
                return {"messages": [AIMessage(content="Unable to produce results.")], "done": True}
            return {"replan_count": state.replan_count + 1}

        # Format results
        lines = []
        for task in (state.dag_plan.tasks if state.dag_plan else []):
            if task.id in state.results:
                lines.append(f"Task {task.id} ({task.tool}): {state.results[task.id]}")
        prompt = f"Query: {state.query}\n\nResults:\n" + "\n".join(lines)

        try:
            decision: JoinerDecision = self._joiner.invoke({"input": prompt})
            if decision.action == "answer":
                return {"messages": [AIMessage(content=decision.response)], "done": True}
            if state.replan_count >= self.max_replans:
                return {"messages": [AIMessage(content=decision.feedback or "Max replans.")], "done": True}
            return {"replan_count": state.replan_count + 1}
        except Exception as e:
            summary = "\n".join(f"- {v}" for v in state.results.values())
            return {"messages": [AIMessage(content=f"Results:\n{summary}")], "done": True}

    # ------------------------------------------------------------------
    # Routing
    # ------------------------------------------------------------------

    @staticmethod
    def _route_after_execute(state: CompilerState) -> str:
        if not state.dag_plan:
            return "planner"
        non_join = [t for t in state.dag_plan.tasks if t.tool != "join"]
        if all(t.id in state.results for t in non_join):
            return "joiner"
        executable = [
            t for t in state.dag_plan.tasks
            if t.id not in state.results and t.tool != "join"
            and all(d in state.results for d in t.depends_on)
        ]
        return "executor" if executable else "joiner"

    @staticmethod
    def _route_after_join(state: CompilerState) -> str:
        if getattr(state, "done", False):
            return "end"
        if state.messages:
            return "end"
        return "planner"

    # ------------------------------------------------------------------
    # Graph (BaseGraph)
    # ------------------------------------------------------------------

    def build_graph(self) -> BaseGraph:
        graph = BaseGraph(name=f"{self.name}_compiler", state_schema=CompilerState)
        graph.add_node("planner", self._plan)
        graph.add_node("executor", self._execute)
        graph.add_node("joiner", self._join)
        graph.add_edge(START, "planner")
        graph.add_edge("planner", "executor")
        graph.add_conditional_edges("executor", self._route_after_execute,
            {"executor": "executor", "joiner": "joiner", "planner": "planner"})
        graph.add_conditional_edges("joiner", self._route_after_join,
            {"planner": "planner", "end": END})
        return graph

    def compile(self, **kwargs) -> Any:
        self._ensure_agents()
        if not self._is_compiled or kwargs:
            if not hasattr(self, "graph") or self.graph is None:
                self._graph_built = False
                self._build_initial_graph()
            if not self.graph:
                raise RuntimeError("No graph")
            if hasattr(self.graph, "to_langgraph"):
                lg = self.graph.to_langgraph(state_schema=CompilerState)
            else:
                lg = self.graph
            self._app = lg.compile(checkpointer=self.checkpointer, store=self.store, **kwargs)
            self._compiled_graph = self._app
            self._is_compiled = True
        return self._compiled_graph or self._app

    # ------------------------------------------------------------------
    # Run
    # ------------------------------------------------------------------

    def run(self, input_data: str | dict, **kwargs) -> Any:
        if isinstance(input_data, str):
            input_data = CompilerState(query=input_data).model_dump()
        if not self._is_compiled:
            self.compile()
        import uuid
        config = {"configurable": {"thread_id": str(uuid.uuid4())}, "recursion_limit": 30}
        return self._app.invoke(input_data, config=config)

    def run_query(self, query: str) -> str:
        """Convenience: run and extract answer string."""
        result = self.run(query)
        if isinstance(result, dict) and result.get("messages"):
            for msg in reversed(result["messages"]):
                if isinstance(msg, AIMessage):
                    return msg.content
        return "No answer produced."

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
                        args = [f"{k} ({v.get('type', 'str')})" for k, v in props.items()]
                        line += "\n   Args: " + ", ".join(args)
                except Exception:
                    pass
            lines.append(line)
        return "\n".join(lines)

    def _run_tool(self, tool_name: str, args: dict) -> Any:
        tool = self._tool_map.get(tool_name)
        if not tool:
            return f"ERROR: Tool '{tool_name}' not found"
        try:
            return tool.invoke(args)
        except Exception as e:
            return f"ERROR: {e}"

    @staticmethod
    def _resolve_args(args: dict, results: dict) -> dict:
        resolved = {}
        for k, v in args.items():
            if isinstance(v, str):
                resolved[k] = re.sub(r'\$(\d+)', lambda m: str(results.get(int(m.group(1)), m.group(0))), v)
            else:
                resolved[k] = v
        return resolved
