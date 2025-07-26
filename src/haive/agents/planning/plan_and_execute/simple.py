"""Simple Plan and Execute Agent - clean and proper."""

from haive.core.engine.aug_llm import AugLLMConfig

from haive.agents.multi.clean import MultiAgent

# Import existing models, prompts, and state
from haive.agents.planning.plan_and_execute.v2.models import Act, ExecutionResult, Plan
from haive.agents.planning.plan_and_execute.v2.prompts import (
    EXECUTOR_PROMPT,
    PLANNER_PROMPT,
    REPLANNER_PROMPT,
    Any,
    Dict,
)
from haive.agents.planning.plan_and_execute.v2.state import PlanAndExecuteState
from haive.agents.simple.agent import SimpleAgent


class PlanAndExecuteAgent(MultiAgent):
    """Plan and Execute using MultiAgent with proper graph building."""

    @classmethod
    def create(
        cls, tools: list | None = None, name: str = "plan_and_execute", **kwargs
    ) -> "PlanAndExecuteAgent":
        """Create Plan and Execute agent with planner, executor, replanner."""
        # Create planner
        planner = SimpleAgent(
            name="planner",
            engine=AugLLMConfig(
                prompt_template=PLANNER_PROMPT,
                structured_output_model=Plan,
                structured_output_version="v2",
                temperature=0.7,
            ),
        )

        # Create executor
        executor = SimpleAgent(
            name="executor",
            engine=AugLLMConfig(
                prompt_template=EXECUTOR_PROMPT,
                structured_output_model=ExecutionResult,
                structured_output_version="v2",
                temperature=0.3,
            ),
            tools=tools or [],
        )

        # Create replanner
        replanner = SimpleAgent(
            name="replanner",
            engine=AugLLMConfig(
                prompt_template=REPLANNER_PROMPT,
                structured_output_model=Act,
                structured_output_version="v2",
                temperature=0.5,
            ),
        )

        return cls(
            name=name,
            agents=[planner, executor, replanner],
            state_schema=PlanAndExecuteState,
            **kwargs,
        )

    def build_graph(self) -> Any:
        """Build the plan-execute-replan graph using BaseGraph."""
        from haive.core.graph.state_graph.base_graph2 import BaseGraph

        # Create BaseGraph with state schema
        graph = BaseGraph(
            name=f"{
                self.name}_graph",
            state_schema=self.state_schema,
        )

        # Add nodes for each agent
        for agent_name, agent in self.agents.items():
            graph.add_node(agent_name, agent)

        # Plan and Execute flow
        from langgraph.graph import END, START

        graph.add_edge(START, "planner")
        graph.add_edge("planner", "executor")
        graph.add_edge("executor", "replanner")

        # Conditional edge from replanner
        def should_continue(state: Dict[str, Any]):
            return "executor" if not state.is_plan_complete() else END

        graph.add_conditional_edges(
            "replanner", should_continue, {"executor": "executor", END: END}
        )

        return graph
