"""Language Agent Tree Search (LATS) agent.

Composes ReactAgent (generation) + SimpleAgent (reflection) in a
Monte Carlo Tree Search loop:

  1. Generate initial candidate via ReactAgent (with tools)
  2. Reflect/score via SimpleAgent with structured output (Reflection)
  3. Select best leaf via UCB1
  4. Expand N candidates from best leaf
  5. Repeat until solved or max height

Graph: START -> generate_initial -> [expand <-> should_continue] -> finish -> END
"""

import logging
from collections import defaultdict
from typing import Any

from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableConfig
from langgraph.graph import END, START
from pydantic import ConfigDict, Field, PrivateAttr

from haive.agents.base.agent import Agent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.state_graph.base_graph2 import BaseGraph

from .models import Node, Reflection
from .state import TreeState

logger = logging.getLogger(__name__)


class LATSAgent(Agent):
    """Look-Ahead Tree Search agent.

    Uses ReactAgent for candidate generation and SimpleAgent for reflection,
    composed in a tree search loop with UCB1 selection.

    Compile without checkpointer (Node objects are not serializable).
    """

    # ---- Config fields ----
    tools: list[Any] = Field(default_factory=list, description="Tools for generation")
    model: str = Field(default="gpt-4o-mini", description="OpenAI model")
    temperature: float = Field(default=0.7)
    n_candidates: int = Field(default=3, description="Candidates per expansion")
    max_tree_height: int = Field(default=3, description="Max search depth")
    exploration_weight: float = Field(default=1.0, description="UCB1 exploration weight")
    system_prompt: str = Field(
        default="You are a helpful AI assistant. Provide thorough, accurate answers.",
    )
    reflection_prompt: str = Field(
        default="Reflect and grade the assistant response to the user question below.",
    )

    # ---- Runtime (lazy) ----
    _generator: Any = PrivateAttr(default=None)
    _reflector: Any = PrivateAttr(default=None)

    model_config = ConfigDict(arbitrary_types_allowed=True)

    # ------------------------------------------------------------------
    # Lazy init
    # ------------------------------------------------------------------

    def _ensure_chains(self) -> None:
        """Build generator + reflector chains lazily."""
        if self._generator is not None:
            return

        from langchain_openai import ChatOpenAI

        llm = ChatOpenAI(model=self.model, temperature=self.temperature)

        # Generator: system prompt + tools
        gen_prompt = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            ("user", "{input}"),
            MessagesPlaceholder(variable_name="messages", optional=True),
        ])
        self._generator = gen_prompt | llm.bind_tools(tools=self.tools)

        # Reflector: structured output -> Reflection
        ref_prompt = ChatPromptTemplate.from_messages([
            ("system", self.reflection_prompt),
            ("user", "{input}"),
            MessagesPlaceholder(variable_name="candidate"),
        ])
        self._reflector = (
            ref_prompt
            | llm.bind_tools(tools=[Reflection], tool_choice="Reflection")
        )

    # ------------------------------------------------------------------
    # Tree search helpers
    # ------------------------------------------------------------------

    def _select(self, root: Node) -> Node:
        """Select best leaf via UCB1."""
        node = root
        while node.children:
            node = max(node.children, key=lambda c: c.upper_confidence_bound(self.exploration_weight))
        return node

    @staticmethod
    def _is_solved(root: Node) -> bool:
        if root.is_solved:
            return True
        return any(LATSAgent._is_solved(c) for c in root.children)

    @staticmethod
    def _get_best_node(root: Node) -> Node:
        best = root
        best_score = root.reflection.normalized_score if root.reflection else 0
        for c in root.children:
            candidate = LATSAgent._get_best_node(c)
            score = candidate.reflection.normalized_score if candidate.reflection else 0
            if score > best_score:
                best, best_score = candidate, score
        return best

    def _reflect(self, user_input: str, candidate_messages: list) -> Reflection:
        """Score a candidate via the reflector chain."""
        from langchain_core.output_parsers.openai_tools import PydanticToolsParser
        parser = PydanticToolsParser(tools=[Reflection])
        result = self._reflector.invoke({"input": user_input, "candidate": candidate_messages})
        parsed = parser.invoke(result)
        return parsed[0] if parsed else Reflection(reflections="No reflection", score=1, found_solution=False)

    # ------------------------------------------------------------------
    # Graph nodes
    # ------------------------------------------------------------------

    def _generate_initial(self, state: TreeState) -> dict[str, Any]:
        """Generate first candidate + reflection -> root Node."""
        user_input = state["input"]

        res = self._generator.invoke({"input": user_input})
        output = [res]

        reflection = self._reflect(user_input, output)
        root = Node(messages=output, reflection=reflection)

        return {**state, "root": root}

    def _expand(self, state: TreeState, config: RunnableConfig) -> dict[str, Any]:
        """Expand tree from best leaf."""
        root = state["root"]
        user_input = state["input"]

        best = self._select(root)
        messages = best.get_trajectory()

        # Generate N candidates
        from langchain_openai import ChatOpenAI
        llm = ChatOpenAI(model=self.model, temperature=self.temperature)
        gen_prompt = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            ("user", "{input}"),
            MessagesPlaceholder(variable_name="messages", optional=True),
        ])

        bound = llm.bind_tools(tools=self.tools)
        result = llm.generate(
            [gen_prompt.invoke({"input": user_input, "messages": messages}).to_messages()],
            n=self.n_candidates,
            **bound.kwargs,
        )
        new_candidates = [gen.message for gen in result.generations[0]]

        # Reflect on each candidate
        for candidate_msg in new_candidates:
            candidate_output = [candidate_msg]
            try:
                reflection = self._reflect(user_input, candidate_output)
            except Exception:
                reflection = Reflection(reflections="Error", score=1, found_solution=False)
            child = Node(messages=candidate_output, parent=best, reflection=reflection)
            best.children.append(child)

        return state

    def _should_continue(self, state: TreeState) -> str:
        root = state["root"]
        if self._is_solved(root):
            return "finish"
        if root.height >= self.max_tree_height:
            return "finish"
        return "expand"

    def _get_best_response(self, state: TreeState) -> dict[str, Any]:
        root = state["root"]
        best = self._get_best_node(root)
        trajectory = best.get_trajectory(include_reflections=False)
        return {
            **state,
            "root": root,
            "messages": trajectory,
            "output": trajectory[-1].content if trajectory else "",
        }

    # ------------------------------------------------------------------
    # Graph
    # ------------------------------------------------------------------

    def build_graph(self) -> BaseGraph:
        """Build LATS graph using haive.core BaseGraph."""
        graph = BaseGraph(name=f"{self.name}_lats", state_schema=TreeState)
        graph.add_node("generate_initial", self._generate_initial)
        graph.add_node("expand", self._expand)
        graph.add_node("finish", self._get_best_response)
        graph.add_edge(START, "generate_initial")
        graph.add_conditional_edges("generate_initial", self._should_continue, {"expand": "expand", "finish": "finish"})
        graph.add_conditional_edges("expand", self._should_continue, {"expand": "expand", "finish": "finish"})
        graph.add_edge("finish", END)
        return graph

    def compile(self, **kwargs) -> Any:
        """Compile using BaseGraph.to_langgraph(), without checkpointer (Node not serializable)."""
        self._ensure_chains()
        if not self._is_compiled or kwargs:
            if not hasattr(self, "graph") or self.graph is None:
                self._graph_built = False
                self._build_initial_graph()
            if not self.graph:
                raise RuntimeError("No graph")
            if hasattr(self.graph, "to_langgraph"):
                lg = self.graph.to_langgraph(state_schema=TreeState)
            else:
                lg = self.graph
            # No checkpointer - Node objects can't be serialized
            self._app = lg.compile()
            self._compiled_graph = self._app
            self._is_compiled = True
        return self._compiled_graph or self._app

    # ------------------------------------------------------------------
    # Run
    # ------------------------------------------------------------------

    def run(self, input_data: str | dict, **kwargs) -> Any:
        if isinstance(input_data, str):
            input_data = {"input": input_data}
        if not self._is_compiled:
            self.compile()
        return self._app.invoke(input_data, config={"recursion_limit": self.max_tree_height * 3 + 5})

    def get_best_answer(self, result: dict) -> str:
        root = result.get("root")
        if not root:
            return ""
        best = self._get_best_node(root)
        traj = best.get_trajectory(include_reflections=False)
        return traj[-1].content if traj else ""


def create_lats_agent(tools=None, model="gpt-4o-mini", max_tree_height=3, n_candidates=3, **kwargs):
    """Factory for creating a LATS agent."""
    return LATSAgent(
        tools=tools or [], model=model, max_tree_height=max_tree_height,
        n_candidates=n_candidates, **kwargs
    )


if __name__ == "__main__":
    agent = LATSAgent(name="test", tools=[])
    g = agent.compile()
    print(f"Compiled: {type(g).__name__}, nodes: {list(g.get_graph().nodes)}")
