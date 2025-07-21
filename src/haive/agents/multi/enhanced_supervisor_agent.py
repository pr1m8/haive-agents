"""Enhanced SupervisorAgent implementation using Agent[AugLLMConfig].

SupervisorAgent = Agent[AugLLMConfig] + worker management + delegation.
"""

import logging
from typing import Any, Dict, List, Literal, Optional

from haive.core.graph.node.engine_node import EngineNodeConfig
from haive.core.graph.state_graph.base_graph2 import BaseGraph
from langchain_core.messages import AIMessage
from langgraph.graph import END
from pydantic import Field, field_validator, model_validator

# Import base enhanced agent when available
# from haive.agents.base.enhanced_agent import Agent
# For now, using minimal base
from haive.agents.simple.enhanced_simple_real import EnhancedAgentBase as Agent

logger = logging.getLogger(__name__)


class SupervisorAgent(Agent):  # Will be Agent[AugLLMConfig] when imports fixed
    """Enhanced SupervisorAgent that coordinates multiple worker agents.

    SupervisorAgent = Agent[AugLLMConfig] + worker management + delegation.

    The Supervisor pattern allows:
    1. Managing a team of worker agents
    2. Delegating tasks to appropriate workers
    3. Coordinating results from multiple workers
    4. Making decisions based on worker outputs

    Attributes:
        workers: Dictionary of worker agents
        max_delegation_rounds: Maximum rounds of delegation
        delegation_strategy: How to choose workers (first, best, all)
        supervisor_prompt: Custom prompt for supervision

    Examples:
        Basic supervisor with workers::

            from haive.agents.simple import SimpleAgent
            from haive.agents.react import ReactAgent

            # Create workers
            analyst = SimpleAgent(name="analyst", engine=AugLLMConfig())
            researcher = ReactAgent(name="researcher", tools=[web_search])

            # Create supervisor
            supervisor = SupervisorAgent(
                name="supervisor",
                workers={"analyst": analyst, "researcher": researcher},
                engine=AugLLMConfig()
            )

            # Run delegation
            result = supervisor.run("Analyze the latest market trends")

        Custom delegation strategy::

            supervisor = SupervisorAgent(
                name="supervisor",
                workers=workers,
                delegation_strategy="best",  # Choose best worker for each task
                supervisor_prompt="You are a project manager..."
            )
    """

    # Worker management
    workers: Dict[str, Any] = Field(
        default_factory=dict,
        description="Dictionary of worker agents managed by this supervisor",
    )

    # Delegation configuration
    max_delegation_rounds: int = Field(
        default=3, description="Maximum number of delegation rounds", ge=1, le=10
    )

    delegation_strategy: Literal["first", "best", "all", "round-robin"] = Field(
        default="best", description="How to select workers for tasks"
    )

    # Prompting
    supervisor_prompt: Optional[str] = Field(
        default=None, description="Custom prompt for supervisor behavior"
    )

    # Tracking
    delegation_history: List[Dict[str, Any]] = Field(
        default_factory=list, description="History of delegations made"
    )

    @field_validator("workers")
    @classmethod
    def validate_workers(cls, v: Dict[str, Any]) -> Dict[str, Any]:
        """Validate that workers are proper agents."""
        if not v:
            logger.warning("SupervisorAgent created without workers")
        return v

    @model_validator(mode="after")
    def validate_supervisor_config(self) -> "SupervisorAgent":
        """Validate supervisor configuration."""
        # Ensure we have an engine for LLM-based coordination
        if not hasattr(self, "engine") or self.engine is None:
            raise ValueError("SupervisorAgent requires an engine (AugLLMConfig)")

        return self

    def build_graph(self) -> BaseGraph:
        """Build the supervisor delegation graph.

        Creates a graph with:
        1. Supervisor node - makes delegation decisions
        2. Worker nodes - execute delegated tasks
        3. Coordination node - aggregates results
        4. Decision routing - based on supervisor decisions
        """
        graph = BaseGraph(
            name=f"{self.name}_supervisor_graph", state_schema=self.state_schema
        )

        # Add supervisor node
        supervisor_node_config = EngineNodeConfig(
            engines={"supervisor": self.engine},
            system_message=self._get_supervisor_prompt(),
        )
        graph.add_node("supervisor", supervisor_node_config)

        # Add worker nodes
        for worker_name, worker_agent in self.workers.items():
            # Each worker is its own subgraph
            worker_graph = worker_agent.build_graph()
            graph.add_node(f"worker_{worker_name}", worker_graph)

        # Add coordination node for result aggregation
        coordination_config = EngineNodeConfig(
            engines={"coordinator": self.engine},
            system_message="Aggregate and summarize the results from all workers.",
        )
        graph.add_node("coordinator", coordination_config)

        # Set up routing
        graph.set_entry_point("supervisor")

        # Supervisor can delegate to any worker
        def route_to_worker(state: Dict[str, Any]) -> str:
            """Route based on supervisor's decision."""
            messages = state.get("messages", [])
            if messages and isinstance(messages[-1], AIMessage):
                content = messages[-1].content
                # Parse worker selection from supervisor response
                for worker_name in self.workers:
                    if worker_name.lower() in content.lower():
                        return f"worker_{worker_name}"

            # Default to first worker or coordinator
            if self.workers:
                return f"worker_{list(self.workers.keys())[0]}"
            return "coordinator"

        graph.add_conditional_edges("supervisor", route_to_worker)

        # All workers route back to coordinator
        for worker_name in self.workers:
            graph.add_edge(f"worker_{worker_name}", "coordinator")

        # Coordinator can go back to supervisor or end
        def should_continue(state: Dict[str, Any]) -> str:
            """Decide if more delegation is needed."""
            rounds = len(self.delegation_history)
            if rounds >= self.max_delegation_rounds:
                return END

            # Check if task is complete
            messages = state.get("messages", [])
            if messages and isinstance(messages[-1], AIMessage):
                if "complete" in messages[-1].content.lower():
                    return END

            return "supervisor"

        graph.add_conditional_edges("coordinator", should_continue)

        return graph

    def _get_supervisor_prompt(self) -> str:
        """Get the supervisor system prompt."""
        if self.supervisor_prompt:
            return self.supervisor_prompt

        worker_descriptions = "\n".join(
            [
                f"- {name}: {getattr(agent, 'description', 'A worker agent')}"
                for name, agent in self.workers.items()
            ]
        )

        return f"""You are a supervisor agent managing a team of workers.

Your workers are:
{worker_descriptions}

Your job is to:
1. Analyze the user's request
2. Decide which worker(s) should handle it
3. Delegate tasks appropriately
4. Review worker outputs
5. Provide a final response

Delegation strategy: {self.delegation_strategy}

When delegating, clearly state which worker should handle the task and why.
"""

    def delegate_task(
        self, task: str, worker_name: Optional[str] = None
    ) -> Dict[str, Any]:
        """Delegate a specific task to a worker.

        Args:
            task: The task to delegate
            worker_name: Specific worker to use (optional)

        Returns:
            Dict with delegation result
        """
        if worker_name and worker_name not in self.workers:
            raise ValueError(f"Unknown worker: {worker_name}")

        # Record delegation
        delegation = {
            "task": task,
            "worker": worker_name or "auto-selected",
            "strategy": self.delegation_strategy,
        }
        self.delegation_history.append(delegation)

        # If specific worker requested, use it directly
        if worker_name:
            worker = self.workers[worker_name]
            result = worker.run(task)
            delegation["result"] = result
            return delegation

        # Otherwise use delegation strategy
        if self.delegation_strategy == "all":
            # Delegate to all workers
            results = {}
            for name, worker in self.workers.items():
                results[name] = worker.run(task)
            delegation["result"] = results

        elif self.delegation_strategy == "first":
            # Use first available worker
            if self.workers:
                name = list(self.workers.keys())[0]
                delegation["worker"] = name
                delegation["result"] = self.workers[name].run(task)

        else:  # "best" or "round-robin"
            # Use LLM to decide best worker
            # This would be handled by the graph execution
            pass

        return delegation

    def get_delegation_summary(self) -> str:
        """Get a summary of all delegations made."""
        if not self.delegation_history:
            return "No delegations made yet."

        summary = f"Delegation Summary ({len(self.delegation_history)} total):\n"
        for i, delegation in enumerate(self.delegation_history, 1):
            summary += f"\n{i}. Task: {delegation['task'][:50]}...\n"
            summary += f"   Worker: {delegation['worker']}\n"
            summary += f"   Strategy: {delegation['strategy']}\n"

        return summary
