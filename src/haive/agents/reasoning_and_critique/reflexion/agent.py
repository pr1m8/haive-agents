"""Reflexion agent.

Composes ReactAgent (draft/revise with optional tools) and SimpleAgent
(reflection/grading with structured output) in an iterative improvement loop.

Graph: START -> draft_answer -> reflect_answer -> [should_continue] -> revise_answer -> reflect_answer -> ... -> finish_answer -> END

The drafter and reflector are real haive agents (ReactAgent, SimpleAgent)
that use our tested infrastructure for LLM calls, tool use, and structured output.
"""

import logging
from typing import Any

from langchain_core.messages import AIMessage
from langgraph.graph import END, START
from pydantic import ConfigDict, Field, PrivateAttr

from haive.agents.base.agent import Agent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.state_graph.base_graph2 import BaseGraph

from .models import Reflection
from .state import ReflexionState

logger = logging.getLogger(__name__)


class ReflexionAgent(Agent):
    """Reflexion: iterative draft-reflect-revise using ReactAgent + SimpleAgent.

    - Drafter: ReactAgent with optional tools for initial answer + revisions
    - Reflector: SimpleAgent with structured output (Reflection model)
    - Loop: draft -> reflect -> revise -> reflect -> ... until max_iterations
    """

    # ---- Config (user-facing Pydantic fields) ----
    tools: list[Any] = Field(default_factory=list, description="Tools for the drafter agent")
    model: str = Field(default="gpt-4o-mini", description="LLM model name")
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    max_iterations: int = Field(default=3, ge=1, description="Max draft-reflect-revise loops")
    system_prompt: str = Field(
        default=(
            "You are an expert researcher. Provide thorough, accurate, "
            "well-structured answers. When revising, incorporate the reflection "
            "feedback and cite your sources with numbered references."
        ),
    )
    reflection_prompt: str = Field(
        default=(
            "You are a critical grading assistant. Evaluate the candidate answer "
            "for accuracy, completeness, and clarity. Identify what is missing "
            "and what is superfluous. Score from 0-10."
        ),
    )

    # ---- Private runtime attrs (built lazily) ----
    _drafter: Any = PrivateAttr(default=None)
    _reflector: Any = PrivateAttr(default=None)

    model_config = ConfigDict(arbitrary_types_allowed=True)

    # ------------------------------------------------------------------
    # Lazy sub-agent construction
    # ------------------------------------------------------------------

    def _ensure_agents(self) -> None:
        """Build sub-agents lazily (avoids import-time side effects)."""
        if self._drafter is not None:
            return

        from haive.agents.react.agent import ReactAgent
        from haive.agents.simple.agent import SimpleAgent

        # Drafter: ReactAgent with tools for generating / revising answers
        self._drafter = ReactAgent(
            name=f"{self.name}_drafter",
            engine=AugLLMConfig(
                temperature=self.temperature,
                system_message=self.system_prompt,
            ),
            tools=self.tools,
        )

        # Reflector: SimpleAgent with structured output -> Reflection
        self._reflector = SimpleAgent(
            name=f"{self.name}_reflector",
            engine=AugLLMConfig(
                temperature=0.2,
                system_message=self.reflection_prompt,
                structured_output_model=Reflection,
            ),
        )

    # ------------------------------------------------------------------
    # Agent helpers
    # ------------------------------------------------------------------

    def _call_drafter(self, prompt: str) -> str:
        """Run the ReactAgent drafter and extract text."""
        result = self._drafter.run(prompt, debug=False)
        if hasattr(result, "messages") and result.messages:
            for msg in reversed(result.messages):
                if isinstance(msg, AIMessage) and msg.content:
                    return msg.content
        return str(result)

    def _call_reflector(self, query: str, draft: str) -> Reflection:
        """Run the SimpleAgent reflector and extract a Reflection."""
        prompt = (
            f"Original question: {query}\n\n"
            f"Candidate answer:\n{draft}\n\n"
            "Evaluate this answer. Identify what is missing and what is superfluous. "
            "Score it 0-10."
        )
        try:
            result = self._reflector.run(prompt, debug=False)
            if hasattr(result, "messages") and result.messages:
                last = result.messages[-1]
                if hasattr(last, "tool_calls") and last.tool_calls:
                    args = last.tool_calls[0].get("args", {})
                    return Reflection(**args)
                content = last.content if hasattr(last, "content") else str(last)
                return Reflection(missing=content, superfluous="", score=5)
            return Reflection(missing=str(result), superfluous="", score=5)
        except Exception as e:
            logger.warning(f"Reflection failed: {e}")
            return Reflection(missing=f"Error: {e}", superfluous="", score=1)

    # ------------------------------------------------------------------
    # Graph nodes
    # ------------------------------------------------------------------

    def _draft_node(self, state: ReflexionState) -> dict[str, Any]:
        """Generate the initial draft answer."""
        query = state["input"]
        draft = self._call_drafter(f"Answer this question thoroughly:\n\n{query}")
        return {"draft": draft, "reflections": [], "revision_count": 0}

    def _reflect_node(self, state: ReflexionState) -> dict[str, Any]:
        """Reflect on the current draft and produce critique."""
        query = state["input"]
        draft = state["draft"]
        reflection = self._call_reflector(query, draft)
        critique = (
            f"[Score: {reflection.score}/10] "
            f"Missing: {reflection.missing} | "
            f"Superfluous: {reflection.superfluous}"
        )
        reflections = list(state.get("reflections", []))
        reflections.append(critique)
        return {"reflections": reflections}

    def _revise_node(self, state: ReflexionState) -> dict[str, Any]:
        """Revise the draft incorporating reflection feedback."""
        query = state["input"]
        draft = state["draft"]
        reflections = state.get("reflections", [])
        latest_reflection = reflections[-1] if reflections else ""

        revise_prompt = (
            f"Original question: {query}\n\n"
            f"Your previous answer:\n{draft}\n\n"
            f"Critique/reflection:\n{latest_reflection}\n\n"
            "Revise your answer to address the critique. "
            "Add missing information, remove superfluous content, "
            "and include numbered references where possible."
        )
        revised = self._call_drafter(revise_prompt)
        revision_count = state.get("revision_count", 0) + 1
        return {"draft": revised, "revision_count": revision_count}

    def _should_continue(self, state: ReflexionState) -> str:
        """Decide whether to revise again or finish."""
        revision_count = state.get("revision_count", 0)
        if revision_count >= self.max_iterations:
            return "finish"
        return "revise"

    def _finish_node(self, state: ReflexionState) -> dict[str, Any]:
        """Terminal node - state already has the best draft."""
        return {}

    # ------------------------------------------------------------------
    # Graph (BaseGraph from haive.core)
    # ------------------------------------------------------------------

    def build_graph(self) -> BaseGraph:
        """Build the Reflexion graph.

        Flow: START -> draft_answer -> reflect_answer -> [revise_answer | finish_answer]
                                                            |               |
                                                            v               v
                                                       reflect_answer      END
        """
        graph = BaseGraph(name=f"{self.name}_reflexion", state_schema=ReflexionState)

        graph.add_node("draft_answer", self._draft_node)
        graph.add_node("reflect_answer", self._reflect_node)
        graph.add_node("revise_answer", self._revise_node)
        graph.add_node("finish_answer", self._finish_node)

        graph.add_edge(START, "draft_answer")
        graph.add_edge("draft_answer", "reflect_answer")
        graph.add_conditional_edges(
            "reflect_answer",
            self._should_continue,
            {"revise": "revise_answer", "finish": "finish_answer"},
        )
        graph.add_edge("revise_answer", "reflect_answer")
        graph.add_edge("finish_answer", END)

        return graph

    # ------------------------------------------------------------------
    # Compile
    # ------------------------------------------------------------------

    def compile(self, **kwargs) -> Any:
        """Compile: build agents lazily, use BaseGraph.to_langgraph()."""
        self._ensure_agents()
        if not self._is_compiled or kwargs:
            if not hasattr(self, "graph") or self.graph is None:
                self._graph_built = False
                self._build_initial_graph()
            if not self.graph:
                raise RuntimeError("No graph after _build_initial_graph")
            if hasattr(self.graph, "to_langgraph"):
                lg = self.graph.to_langgraph(state_schema=ReflexionState)
            else:
                lg = self.graph
            self._app = lg.compile(**kwargs)
            self._compiled_graph = self._app
            self._is_compiled = True
        return self._compiled_graph or self._app

    # ------------------------------------------------------------------
    # Run
    # ------------------------------------------------------------------

    def run(self, input_data: str | dict, **kwargs) -> Any:
        """Run reflexion. Accepts a string query or a dict with 'input' key."""
        if isinstance(input_data, str):
            input_data = {
                "input": input_data,
                "draft": "",
                "reflections": [],
                "revision_count": 0,
            }
        if not self._is_compiled:
            self.compile()
        return self._app.invoke(
            input_data,
            config={"recursion_limit": self.max_iterations * 3 + 10},
        )

    def get_answer(self, result: dict) -> str:
        """Extract the final answer from a run result."""
        return result.get("draft", "")


def create_reflexion_agent(tools=None, model="gpt-4o-mini", **kwargs):
    """Factory for ReflexionAgent."""
    return ReflexionAgent(tools=tools or [], model=model, **kwargs)


if __name__ == "__main__":
    agent = ReflexionAgent(name="test", tools=[])
    g = agent.compile()
    print(f"Compiled: {type(g).__name__}, nodes: {list(g.get_graph().nodes)}")
