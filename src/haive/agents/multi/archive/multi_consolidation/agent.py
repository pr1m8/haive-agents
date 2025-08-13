"""Core Multi-Agent implementation.

This module provides the main MultiAgent class that serves as the foundation
for all multi-agent systems in Haive. It combines multiple agents and coordinates
their execution with various modes and strategies.
"""

from __future__ import annotations

import logging
from enum import Enum
from typing import Any

from haive.core.engine.agent import Agent, AgentConfig
from haive.core.schema.state_schema import StateSchema
from langchain_core.messages import BaseMessage
from pydantic import Field, field_validator

logger = logging.getLogger(__name__)


class ExecutionMode(str, Enum):
    """Execution modes for multi-agent systems."""

    SEQUENTIAL = "sequential"
    PARALLEL = "parallel"
    CONDITIONAL = "conditional"
    ROUND_ROBIN = "round_robin"
    HIERARCHICAL = "hierarchical"


class MultiAgentState(StateSchema):
    """State schema for multi-agent execution."""

    messages: list[BaseMessage] = Field(
        default_factory=list, description="Message history"
    )
    current_agent: str | None = Field(
        default=None, description="Currently executing agent"
    )
    agent_results: dict[str, Any] = Field(
        default_factory=dict, description="Results from each agent"
    )
    execution_order: list[str] = Field(
        default_factory=list, description="Order of agent execution"
    )
    iteration_count: int = Field(default=0, description="Current iteration count")
    max_iterations: int = Field(default=10, description="Maximum iterations allowed")
    completed_agents: list[str] = Field(
        default_factory=list, description="List of completed agents"
    )
    failed_agents: list[str] = Field(
        default_factory=list, description="List of failed agents"
    )
    execution_complete: bool = Field(
        default=False, description="Whether execution is complete"
    )


class MultiAgentConfig(AgentConfig):
    """Configuration for MultiAgent systems."""

    agents: dict[str, Agent] = Field(
        default_factory=dict, description="Dictionary of agents"
    )
    execution_mode: ExecutionMode = Field(
        default=ExecutionMode.SEQUENTIAL, description="Execution mode"
    )
    max_iterations: int = Field(default=10, description="Maximum iterations")
    timeout: float | None = Field(default=None, description="Timeout for execution")
    error_handling: str = Field(
        default="continue", description="Error handling strategy"
    )
    coordination_strategy: str | None = Field(
        default=None, description="Coordination strategy"
    )

    @field_validator("agents")
    @classmethod
    def validate_agents(cls, v: dict[str, Agent]) -> dict[str, Agent]:
        """Validate that all agents have proper names."""
        for name, agent in v.items():
            if not hasattr(agent, "name") or not agent.name:
                if hasattr(agent, "config") and hasattr(agent.config, "name"):
                    agent.name = agent.config.name
                else:
                    agent.name = name
        return v


class MultiAgent(Agent):
    """Multi-agent system that coordinates execution of multiple agents.

    This class provides a flexible framework for combining multiple agents
    with different execution modes, coordination strategies, and error handling.

    Examples:
        Basic sequential execution::

            agents = {
                "planner": PlannerAgent(config=planner_config),
                "executor": ExecutorAgent(config=executor_config)
            }

            multi_config = MultiAgentConfig(
                name="workflow",
                agents=agents,
                execution_mode=ExecutionMode.SEQUENTIAL
            )

            multi_agent = MultiAgent(multi_config)
            result = multi_agent.run("Create and execute a plan")

        Parallel execution::

            multi_config = MultiAgentConfig(
                name="parallel_workflow",
                agents=agents,
                execution_mode=ExecutionMode.PARALLEL
            )
    """

    def __init__(self, config: MultiAgentConfig):
        self.agents = config.agents
        self.execution_mode = config.execution_mode
        self.max_iterations = config.max_iterations
        self.timeout = config.timeout
        self.error_handling = config.error_handling
        self.coordination_strategy = config.coordination_strategy
        self.state_schema = MultiAgentState
        super().__init__(config)

    def setup_workflow(self) -> None:
        """Set up the multi-agent workflow."""
        logger.info(f"Setting up multi-agent workflow with {len(self.agents)} agents")
        logger.info(f"Execution mode: {self.execution_mode}")

        # Set up coordination based on execution mode
        if self.execution_mode == ExecutionMode.SEQUENTIAL:
            self._setup_sequential_workflow()
        elif self.execution_mode == ExecutionMode.PARALLEL:
            self._setup_parallel_workflow()
        elif self.execution_mode == ExecutionMode.CONDITIONAL:
            self._setup_conditional_workflow()
        elif self.execution_mode == ExecutionMode.ROUND_ROBIN:
            self._setup_round_robin_workflow()
        elif self.execution_mode == ExecutionMode.HIERARCHICAL:
            self._setup_hierarchical_workflow()
        else:
            logger.warning(
                f"Unknown execution mode: {self.execution_mode}, using sequential"
            )
            self._setup_sequential_workflow()

    def _setup_sequential_workflow(self) -> None:
        """Set up sequential execution workflow."""
        agent_names = list(self.agents.keys())
        logger.info(f"Sequential execution order: {' → '.join(agent_names)}")

    def _setup_parallel_workflow(self) -> None:
        """Set up parallel execution workflow."""
        agent_names = list(self.agents.keys())
        logger.info(f"Parallel execution of agents: {', '.join(agent_names)}")

    def _setup_conditional_workflow(self) -> None:
        """Set up conditional execution workflow."""
        logger.info(
            "Conditional execution workflow - agents selected based on conditions"
        )

    def _setup_round_robin_workflow(self) -> None:
        """Set up round-robin execution workflow."""
        logger.info("Round-robin execution - agents take turns")

    def _setup_hierarchical_workflow(self) -> None:
        """Set up hierarchical execution workflow."""
        logger.info("Hierarchical execution - supervisor coordinates sub-agents")

    def run(self, input_data: Any, **kwargs) -> Any:
        """Run the multi-agent system."""
        logger.info(f"Starting multi-agent execution with {len(self.agents)} agents")

        state = MultiAgentState(
            messages=(
                input_data.get("messages", []) if isinstance(input_data, dict) else []
            ),
            max_iterations=self.max_iterations,
        )

        try:
            if self.execution_mode == ExecutionMode.SEQUENTIAL:
                return self._execute_sequential(input_data, state, **kwargs)
            if self.execution_mode == ExecutionMode.PARALLEL:
                return self._execute_parallel(input_data, state, **kwargs)
            if self.execution_mode == ExecutionMode.CONDITIONAL:
                return self._execute_conditional(input_data, state, **kwargs)
            if self.execution_mode == ExecutionMode.ROUND_ROBIN:
                return self._execute_round_robin(input_data, state, **kwargs)
            if self.execution_mode == ExecutionMode.HIERARCHICAL:
                return self._execute_hierarchical(input_data, state, **kwargs)
            return self._execute_sequential(input_data, state, **kwargs)

        except Exception as e:
            logger.error(f"Multi-agent execution failed: {e}")
            if self.error_handling == "raise":
                raise
            return {"error": str(e), "partial_results": state.agent_results}

    def _execute_sequential(
        self, input_data: Any, state: MultiAgentState, **kwargs
    ) -> Any:
        """Execute agents sequentially."""
        current_input = input_data
        results = []

        for agent_name, agent in self.agents.items():
            try:
                logger.info(f"Executing agent: {agent_name}")
                state.current_agent = agent_name

                if hasattr(agent, "run"):
                    result = agent.run(current_input, **kwargs)
                    results.append(result)
                    state.agent_results[agent_name] = result
                    state.completed_agents.append(agent_name)

                    # Pass result to next agent
                    current_input = result
                else:
                    error_msg = f"Agent {agent_name} does not have run method"
                    logger.error(error_msg)
                    state.failed_agents.append(agent_name)
                    if self.error_handling == "raise":
                        raise RuntimeError(error_msg)

            except Exception as e:
                error_msg = f"Agent {agent_name} failed: {e}"
                logger.error(error_msg)
                state.failed_agents.append(agent_name)
                if self.error_handling == "raise":
                    raise
                if self.error_handling == "stop":
                    break
                # "continue" mode keeps going

        state.execution_complete = True
        return {
            "final_result": results[-1] if results else None,
            "all_results": results,
            "state": state.model_dump(),
            "completed_agents": state.completed_agents,
            "failed_agents": state.failed_agents,
        }

    def _execute_parallel(
        self, input_data: Any, state: MultiAgentState, **kwargs
    ) -> Any:
        """Execute agents in parallel."""
        import concurrent.futures

        results = {}

        def run_agent(agent_name: str, agent: Agent) -> tuple[str, Any]:
            try:
                if hasattr(agent, "run"):
                    result = agent.run(input_data, **kwargs)
                    return agent_name, result
                return agent_name, {
                    "error": f"Agent {agent_name} does not have run method"
                }
            except Exception as e:
                return agent_name, {"error": str(e)}

        # Use ThreadPoolExecutor for parallel execution
        with concurrent.futures.ThreadPoolExecutor(
            max_workers=len(self.agents)
        ) as executor:
            future_to_agent = {
                executor.submit(run_agent, name, agent): name
                for name, agent in self.agents.items()
            }

            for future in concurrent.futures.as_completed(future_to_agent):
                agent_name = future_to_agent[future]
                try:
                    name, result = future.result(timeout=self.timeout)
                    results[name] = result
                    state.agent_results[name] = result
                    if "error" not in result:
                        state.completed_agents.append(name)
                    else:
                        state.failed_agents.append(name)
                except Exception as e:
                    logger.error(f"Agent {agent_name} execution failed: {e}")
                    state.failed_agents.append(agent_name)
                    results[agent_name] = {"error": str(e)}

        state.execution_complete = True
        return {
            "results": results,
            "state": state.model_dump(),
            "completed_agents": state.completed_agents,
            "failed_agents": state.failed_agents,
        }

    def _execute_conditional(
        self, input_data: Any, state: MultiAgentState, **kwargs
    ) -> Any:
        """Execute agents based on conditions."""
        # Simplified conditional execution - select first agent that matches
        # In a real implementation, this would have sophisticated condition checking

        for agent_name, agent in self.agents.items():
            # Simple condition: execute if agent has required capability
            if self._should_execute_agent(agent, input_data):
                try:
                    logger.info(f"Conditionally executing agent: {agent_name}")
                    result = agent.run(input_data, **kwargs)
                    state.agent_results[agent_name] = result
                    state.completed_agents.append(agent_name)
                    state.execution_complete = True
                    return {
                        "result": result,
                        "selected_agent": agent_name,
                        "state": state.model_dump(),
                    }
                except Exception as e:
                    logger.error(f"Conditional agent {agent_name} failed: {e}")
                    state.failed_agents.append(agent_name)
                    continue

        # No agent was selected/succeeded
        state.execution_complete = True
        return {
            "error": "No agent met the execution conditions",
            "state": state.model_dump(),
        }

    def _execute_round_robin(
        self, input_data: Any, state: MultiAgentState, **kwargs
    ) -> Any:
        """Execute agents in round-robin fashion."""
        agent_names = list(self.agents.keys())
        current_input = input_data
        results = []

        for iteration in range(self.max_iterations):
            state.iteration_count = iteration
            for agent_name in agent_names:
                agent = self.agents[agent_name]
                try:
                    logger.info(
                        f"Round-robin iteration {iteration}, agent: {agent_name}"
                    )
                    result = agent.run(current_input, **kwargs)
                    results.append(
                        {"agent": agent_name, "iteration": iteration, "result": result}
                    )
                    state.agent_results[f"{agent_name}_{iteration}"] = result
                    current_input = result

                    # Check if we should stop (simplified)
                    if self._should_stop_round_robin(result, iteration):
                        state.execution_complete = True
                        return {
                            "final_result": result,
                            "all_results": results,
                            "iterations": iteration + 1,
                            "state": state.model_dump(),
                        }

                except Exception as e:
                    logger.error(f"Round-robin agent {agent_name} failed: {e}")
                    state.failed_agents.append(f"{agent_name}_{iteration}")
                    if self.error_handling == "raise":
                        raise

        state.execution_complete = True
        return {
            "final_result": results[-1]["result"] if results else None,
            "all_results": results,
            "iterations": self.max_iterations,
            "state": state.model_dump(),
        }

    def _execute_hierarchical(
        self, input_data: Any, state: MultiAgentState, **kwargs
    ) -> Any:
        """Execute agents in hierarchical fashion."""
        # Simplified hierarchical execution - assume first agent is supervisor
        agent_names = list(self.agents.keys())
        if not agent_names:
            return {"error": "No agents available"}

        supervisor_name = agent_names[0]
        subordinate_names = agent_names[1:]

        supervisor = self.agents[supervisor_name]
        subordinates = {name: self.agents[name] for name in subordinate_names}

        try:
            # Execute supervisor with access to subordinates
            logger.info(f"Hierarchical execution - supervisor: {supervisor_name}")

            # Add subordinates to supervisor context (simplified)
            enhanced_input = input_data
            if isinstance(input_data, dict):
                enhanced_input = input_data.copy()
                enhanced_input["subordinate_agents"] = subordinates

            result = supervisor.run(enhanced_input, **kwargs)
            state.agent_results[supervisor_name] = result
            state.completed_agents.append(supervisor_name)
            state.execution_complete = True

            return {
                "result": result,
                "supervisor": supervisor_name,
                "subordinates": subordinate_names,
                "state": state.model_dump(),
            }

        except Exception as e:
            logger.error(f"Hierarchical supervisor {supervisor_name} failed: {e}")
            state.failed_agents.append(supervisor_name)
            return {"error": str(e), "state": state.model_dump()}

    def _should_execute_agent(self, agent: Agent, input_data: Any) -> bool:
        """Determine if an agent should be executed based on conditions."""
        # Simplified condition checking
        # In a real implementation, this would analyze agent capabilities vs requirements
        return True

    def _should_stop_round_robin(self, result: Any, iteration: int) -> bool:
        """Determine if round-robin execution should stop."""
        # Simplified stopping condition
        # In a real implementation, this would analyze result quality/completion
        return iteration >= 2  # Stop after 3 rounds maximum

    def add_agent(self, name: str, agent: Agent) -> None:
        """Add an agent to the multi-agent system."""
        self.agents[name] = agent
        logger.info(f"Added agent: {name}")

    def remove_agent(self, name: str) -> Agent | None:
        """Remove an agent from the multi-agent system."""
        if name in self.agents:
            agent = self.agents.pop(name)
            logger.info(f"Removed agent: {name}")
            return agent
        return None

    def get_agent(self, name: str) -> Agent | None:
        """Get an agent by name."""
        return self.agents.get(name)

    def list_agents(self) -> list[str]:
        """List all agent names."""
        return list(self.agents.keys())


# Factory functions for common multi-agent patterns


def create_sequential_multi_agent(
    agents: list[Agent], name: str = "sequential_multi_agent"
) -> MultiAgent:
    """Create a sequential multi-agent system."""
    agent_dict = {f"agent_{i}": agent for i, agent in enumerate(agents)}
    config = MultiAgentConfig(
        name=name, agents=agent_dict, execution_mode=ExecutionMode.SEQUENTIAL
    )
    return MultiAgent(config)


def create_parallel_multi_agent(
    agents: list[Agent], name: str = "parallel_multi_agent"
) -> MultiAgent:
    """Create a parallel multi-agent system."""
    agent_dict = {f"agent_{i}": agent for i, agent in enumerate(agents)}
    config = MultiAgentConfig(
        name=name, agents=agent_dict, execution_mode=ExecutionMode.PARALLEL
    )
    return MultiAgent(config)


def create_hierarchical_multi_agent(
    supervisor: Agent, subordinates: list[Agent], name: str = "hierarchical_multi_agent"
) -> MultiAgent:
    """Create a hierarchical multi-agent system."""
    agent_dict = {"supervisor": supervisor}
    agent_dict.update(
        {f"subordinate_{i}": agent for i, agent in enumerate(subordinates)}
    )

    config = MultiAgentConfig(
        name=name, agents=agent_dict, execution_mode=ExecutionMode.HIERARCHICAL
    )
    return MultiAgent(config)


# Export main classes and functions
__all__ = [
    "ExecutionMode",
    "MultiAgent",
    "MultiAgentConfig",
    "MultiAgentState",
    "create_hierarchical_multi_agent",
    "create_parallel_multi_agent",
    "create_sequential_multi_agent",
]
