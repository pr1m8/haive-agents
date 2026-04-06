"""ReWOO Agent - Reasoning WithOut Observation.

Unlike ReAct (reason-act-observe loop), ReWOO plans ALL steps upfront,
executes them, then synthesizes the final answer. This reduces LLM calls.

Composes:
- Planner: SimpleAgent with structured output (plan all steps)
- Executor: parallel tool execution (no LLM needed)
- Solver: SimpleAgent synthesizes answer from all results

Graph: START -> plan -> execute -> solve -> END
"""

import logging
import re
from concurrent.futures import ThreadPoolExecutor
from typing import Any

from langchain_core.messages import AIMessage
from langgraph.graph import END, START
from pydantic import BaseModel, ConfigDict, Field, PrivateAttr

from haive.agents.base.agent import Agent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.state_graph.base_graph2 import BaseGraph

logger = logging.getLogger(__name__)


# -- Models --

class ReWOOStep(BaseModel):
    """A single step in the ReWOO plan."""
    id: int = Field(description="Step ID")
    tool: str = Field(description="Tool to call")
    args: dict[str, Any] = Field(default_factory=dict, description="Tool arguments. Use #N to reference step N output.")
    thought: str = Field(default="", description="Why this step is needed")


class ReWOOPlan(BaseModel):
    """Complete plan with all steps."""
    steps: list[ReWOOStep] = Field(description="All steps to execute")
    reasoning: str = Field(default="", description="Overall planning reasoning")


# -- State --

class ReWOOState(BaseModel):
    """State for ReWOO graph."""
    query: str = ""
    plan: ReWOOPlan | None = None
    results: dict[int, Any] = Field(default_factory=dict)
    answer: str = ""
    messages: list[Any] = Field(default_factory=list)

    class Config:
        arbitrary_types_allowed = True


# -- Prompts --

PLANNER_PROMPT = """You are a strategic planner. Given a question, create a complete plan
of tool calls needed to answer it. Plan ALL steps upfront - don't wait for results.

Available tools:
{tool_descriptions}

Use #N in arguments to reference the output of step N.
Keep plans minimal and efficient."""

SOLVER_PROMPT = """You are a problem solver. Given the original question and the results
from executing a plan, synthesize a clear, complete answer.

Be concise and directly answer the question using the evidence provided."""


class ReWOOAgent(Agent):
    """Reasoning WithOut Observation agent.

    Plans all steps upfront (one LLM call), executes tools in parallel,
    then synthesizes answer (one more LLM call). Only 2 LLM calls total.

    Composes:
    - Planner: SimpleAgent -> ReWOOPlan (structured output)
    - Executor: ThreadPoolExecutor (no LLM)
    - Solver: SimpleAgent (free-form answer)
    """

    tools: list[Any] = Field(default_factory=list)
    model: str = Field(default="gpt-4o-mini")
    temperature: float = Field(default=0.3)
    max_execution_time: float = Field(default=60.0)

    _planner: Any = PrivateAttr(default=None)
    _solver: Any = PrivateAttr(default=None)
    _tool_map: dict = PrivateAttr(default_factory=dict)

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def _ensure_agents(self) -> None:
        if self._planner is not None:
            return

        from langchain_openai import ChatOpenAI
        from langchain_core.prompts import ChatPromptTemplate

        self._tool_map = {t.name: t for t in self.tools}
        tool_desc = "\n".join(
            f"{i+1}. {t.name}: {t.description}" for i, t in enumerate(self.tools)
        )

        llm = ChatOpenAI(model=self.model, temperature=self.temperature)

        # Planner: structured -> ReWOOPlan
        plan_prompt = ChatPromptTemplate.from_messages([
            ("system", PLANNER_PROMPT.format(tool_descriptions=tool_desc)),
            ("human", "{query}"),
        ])
        self._planner = plan_prompt | llm.with_structured_output(ReWOOPlan, method="function_calling")

        # Solver: free-form answer
        from haive.agents.simple.agent import SimpleAgent
        self._solver = SimpleAgent(
            name=f"{self.name}_solver",
            engine=AugLLMConfig(temperature=0.3, system_message=SOLVER_PROMPT),
        )

    # -- Graph nodes --

    def _plan(self, state: ReWOOState) -> dict[str, Any]:
        try:
            plan: ReWOOPlan = self._planner.invoke({"query": state.query})
            logger.info(f"ReWOO plan: {len(plan.steps)} steps")
            return {"plan": plan}
        except Exception as e:
            logger.warning(f"Planning failed: {e}")
            tasks = [ReWOOStep(id=1, tool="join", thought=f"Fallback: {e}")]
            return {"plan": ReWOOPlan(steps=tasks, reasoning=str(e))}

    def _execute(self, state: ReWOOState) -> dict[str, Any]:
        if not state.plan:
            return {}

        results = dict(state.results)

        # Execute in dependency waves
        for _ in range(len(state.plan.steps)):
            executable = [
                s for s in state.plan.steps
                if s.id not in results and s.tool != "join"
                and all(
                    ref_id in results
                    for ref_id in [int(m) for m in re.findall(r'#(\d+)', str(s.args))]
                )
            ]
            if not executable:
                break

            with ThreadPoolExecutor(max_workers=min(len(executable), 8)) as pool:
                futures = {}
                for step in executable:
                    resolved = self._resolve_args(step.args, results)
                    futures[step.id] = pool.submit(self._run_tool, step.tool, resolved)
                for sid, future in futures.items():
                    try:
                        results[sid] = future.result(timeout=self.max_execution_time)
                    except Exception as e:
                        results[sid] = f"ERROR: {e}"

        return {"results": results}

    def _solve(self, state: ReWOOState) -> dict[str, Any]:
        # Build context from plan + results
        lines = [f"Question: {state.query}", "", "Execution Results:"]
        if state.plan:
            for step in state.plan.steps:
                if step.id in state.results:
                    lines.append(f"Step {step.id} ({step.tool}): {state.results[step.id]}")
        context = "\n".join(lines)

        result = self._solver.run(context, debug=False)
        answer = ""
        if hasattr(result, "messages") and result.messages:
            answer = result.messages[-1].content
        return {"answer": answer, "messages": [AIMessage(content=answer)]}

    # -- Graph --

    def build_graph(self) -> BaseGraph:
        graph = BaseGraph(name=f"{self.name}_rewoo", state_schema=ReWOOState)
        graph.add_node("planner", self._plan)
        graph.add_node("executor", self._execute)
        graph.add_node("solve", self._solve)
        graph.add_edge(START, "planner")
        graph.add_edge("planner", "executor")
        graph.add_edge("executor", "solve")
        graph.add_edge("solve", END)
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
                lg = self.graph.to_langgraph(state_schema=ReWOOState)
            else:
                lg = self.graph
            self._app = lg.compile(checkpointer=self.checkpointer, store=self.store, **kwargs)
            self._compiled_graph = self._app
            self._is_compiled = True
        return self._compiled_graph or self._app

    def run(self, input_data: str | dict, **kwargs) -> Any:
        if isinstance(input_data, str):
            input_data = ReWOOState(query=input_data).model_dump()
        if not self._is_compiled:
            self.compile()
        import uuid
        config = {"configurable": {"thread_id": str(uuid.uuid4())}, "recursion_limit": 10}
        return self._app.invoke(input_data, config=config)

    def run_query(self, query: str) -> str:
        result = self.run(query)
        return result.get("answer", "") if isinstance(result, dict) else str(result)

    # -- Helpers --

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
                resolved[k] = re.sub(r'#(\d+)', lambda m: str(results.get(int(m.group(1)), m.group(0))), v)
            else:
                resolved[k] = v
        return resolved


def create_rewoo_agent(tools=None, model="gpt-4o-mini", **kwargs):
    return ReWOOAgent(tools=tools or [], model=model, **kwargs)
