"""Language Agent Tree Search (LATS) agent.

Composes ReactAgent (candidate generation with tools) and SimpleAgent
(reflection/scoring with structured output) in a Monte Carlo Tree Search loop.

Graph: START -> generate -> [expand <-> should_continue] -> finish -> END

The generator and reflector are real haive agents (ReactAgent, SimpleAgent)
that use our tested infrastructure for LLM calls, tool use, and structured output.
"""

import logging
from typing import Any

from langchain_core.messages import AIMessage, HumanMessage
from langgraph.graph import END, START
from pydantic import ConfigDict, Field, PrivateAttr

from haive.agents.base.agent import Agent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.state_graph.base_graph2 import BaseGraph

from .models import Node, Reflection
from .state import TreeState

logger = logging.getLogger(__name__)


class LATSAgent(Agent):
    """Look-Ahead Tree Search using ReactAgent + SimpleAgent composition.

    - Generator: ReactAgent with tools for candidate creation
    - Reflector: SimpleAgent with structured output (Reflection model)
    - Tree logic: UCB1 selection, backpropagation, depth limiting
    """

    # ---- Config ----
    tools: list[Any] = Field(default_factory=list, description="Tools for the generator agent")
    model: str = Field(default="gpt-4o-mini", description="OpenAI model")
    temperature: float = Field(default=0.7)
    n_candidates: int = Field(default=3, description="Candidates per expansion")
    max_tree_height: int = Field(default=3, description="Max search depth")
    exploration_weight: float = Field(default=1.0, description="UCB1 exploration weight")
    system_prompt: str = Field(
        default="You are a helpful AI assistant. Provide thorough, accurate answers.",
    )
    reflection_prompt: str = Field(
        default=(
            "You are a grading assistant. Reflect on and score the candidate response "
            "to the user question. Evaluate accuracy, completeness, and helpfulness."
        ),
    )

    # ---- Sub-agents (built lazily) ----
    _generator: Any = PrivateAttr(default=None)
    _reflector: Any = PrivateAttr(default=None)

    model_config = ConfigDict(arbitrary_types_allowed=True)

    # ------------------------------------------------------------------
    # Build sub-agents lazily
    # ------------------------------------------------------------------

    def _ensure_agents(self) -> None:
        """Create the generator (ReactAgent) and reflector (SimpleAgent)."""
        if self._generator is not None:
            return

        from haive.agents.react.agent import ReactAgent
        from haive.agents.simple.agent import SimpleAgent

        # Generator: ReactAgent with tools
        self._generator = ReactAgent(
            name=f"{self.name}_generator",
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

    def _generate(self, query: str) -> list[AIMessage]:
        """Generate a candidate response using the ReactAgent."""
        result = self._generator.run(query, debug=False)
        if hasattr(result, "messages") and result.messages:
            return [msg for msg in result.messages if isinstance(msg, AIMessage)]
        return [AIMessage(content=str(result))]

    def _reflect(self, query: str, candidate_text: str) -> Reflection:
        """Score a candidate using the SimpleAgent reflector."""
        prompt = f"Question: {query}\n\nCandidate Answer:\n{candidate_text}\n\nScore this response 0-10."
        try:
            result = self._reflector.run(prompt, debug=False)
            # Extract Reflection from structured output
            if hasattr(result, "messages") and result.messages:
                last = result.messages[-1]
                if hasattr(last, "tool_calls") and last.tool_calls:
                    args = last.tool_calls[0].get("args", {})
                    return Reflection(**args)
                # Try parsing content
                content = last.content if hasattr(last, "content") else str(last)
                return Reflection(reflections=content, score=5, found_solution=False)
            return Reflection(reflections=str(result), score=5, found_solution=False)
        except Exception as e:
            logger.warning(f"Reflection failed: {e}")
            return Reflection(reflections=f"Error: {e}", score=1, found_solution=False)

    # ------------------------------------------------------------------
    # Tree search
    # ------------------------------------------------------------------

    def _select(self, root: Node) -> Node:
        """Select best leaf via UCB1."""
        node = root
        while node.children:
            node = max(node.children, key=lambda c: c.upper_confidence_bound(self.exploration_weight))
        return node

    @staticmethod
    def _is_solved(node: Node) -> bool:
        if node.is_solved:
            return True
        return any(LATSAgent._is_solved(c) for c in node.children)

    @staticmethod
    def _get_best_node(root: Node) -> Node:
        best, best_score = root, root.reflection.normalized_score if root.reflection else 0
        for c in root.children:
            candidate = LATSAgent._get_best_node(c)
            score = candidate.reflection.normalized_score if candidate.reflection else 0
            if score > best_score:
                best, best_score = candidate, score
        return best

    # ------------------------------------------------------------------
    # Graph nodes
    # ------------------------------------------------------------------

    def _generate_initial(self, state: TreeState) -> dict[str, Any]:
        """Generate first candidate + reflect -> root Node."""
        query = state["input"]
        messages = self._generate(query)
        candidate_text = messages[-1].content if messages else ""
        reflection = self._reflect(query, candidate_text)
        root = Node(messages=messages, reflection=reflection)
        return {**state, "root": root}

    def _expand(self, state: TreeState) -> dict[str, Any]:
        """Expand tree from best leaf: generate N candidates, reflect on each."""
        root = state["root"]
        query = state["input"]
        best = self._select(root)

        for _ in range(self.n_candidates):
            # Each candidate is a fresh generation
            messages = self._generate(query)
            candidate_text = messages[-1].content if messages else ""
            reflection = self._reflect(query, candidate_text)
            child = Node(messages=messages, parent=best, reflection=reflection)
            best.children.append(child)

        return state

    def _should_continue(self, state: TreeState) -> str:
        root = state["root"]
        if self._is_solved(root):
            return "finish"
        if root.height >= self.max_tree_height:
            return "finish"
        return "expand"

    def _finish(self, state: TreeState) -> dict[str, Any]:
        """Extract best response from tree."""
        root = state["root"]
        best = self._get_best_node(root)
        trajectory = best.get_trajectory(include_reflections=False)
        output = trajectory[-1].content if trajectory else ""
        return {**state, "root": root, "messages": trajectory, "output": output}

    # ------------------------------------------------------------------
    # Graph (BaseGraph from haive.core)
    # ------------------------------------------------------------------

    def build_graph(self) -> BaseGraph:
        """Build LATS graph using haive.core BaseGraph."""
        graph = BaseGraph(name=f"{self.name}_lats", state_schema=TreeState)
        graph.add_node("generate", self._generate_initial)
        graph.add_node("expand", self._expand)
        graph.add_node("finish", self._finish)
        graph.add_edge(START, "generate")
        graph.add_conditional_edges(
            "generate", self._should_continue,
            {"expand": "expand", "finish": "finish"},
        )
        graph.add_conditional_edges(
            "expand", self._should_continue,
            {"expand": "expand", "finish": "finish"},
        )
        graph.add_edge("finish", END)
        return graph

    def compile(self, **kwargs) -> Any:
        """Compile: build agents lazily, use BaseGraph.to_langgraph(), no checkpointer."""
        self._ensure_agents()
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
            self._app = lg.compile()  # No checkpointer (Node not serializable)
            self._compiled_graph = self._app
            self._is_compiled = True
        return self._compiled_graph or self._app

    # ------------------------------------------------------------------
    # Run
    # ------------------------------------------------------------------

    def run(self, input_data: str | dict, **kwargs) -> Any:
        """Run LATS. Accepts string or dict with 'input' key."""
        if isinstance(input_data, str):
            input_data = {"input": input_data}
        if not self._is_compiled:
            self.compile()
        return self._app.invoke(input_data, config={"recursion_limit": self.max_tree_height * 3 + 5})

    def get_best_answer(self, result: dict) -> str:
        """Extract best answer string from result."""
        root = result.get("root")
        if not root:
            return ""
        best = self._get_best_node(root)
        traj = best.get_trajectory(include_reflections=False)
        return traj[-1].content if traj else ""


def create_lats_agent(tools=None, model="gpt-4o-mini", **kwargs):
    """Factory for LATS agent."""
    return LATSAgent(tools=tools or [], model=model, **kwargs)


if __name__ == "__main__":
    agent = LATSAgent(name="test", tools=[])
    g = agent.compile()
    print(f"Compiled: {type(g).__name__}, nodes: {list(g.get_graph().nodes)}")
