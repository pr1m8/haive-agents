"""Test Self-Discover pattern with unified MultiAgent - unit tests only."""

from typing import Any

import pytest
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema import StateSchema
from pydantic import Field

from haive.agents.multi.clean import MultiAgent
from haive.agents.simple import SimpleAgent


class SelfDiscoverState(StateSchema):
    """State for self-discover workflow."""

    task_description: str = Field(default="")
    selected_modules: str | None = Field(default=None)
    adapted_modules: str | None = Field(default=None)
    reasoning_plan: str | None = Field(default=None)
    final_answer: str | None = Field(default=None)


class TestSelfDiscoverMultiAgent:
    """Test suite for Self-Discover pattern using MultiAgent."""

    def test_sequential_multiagent_creation(self):
        """Test creating a sequential multi-agent for self-discover."""
        # Create mock agents (no real LLM calls)
        agents = [
            SimpleAgent(name="selector", engine=AugLLMConfig()),
            SimpleAgent(name="adapter", engine=AugLLMConfig()),
            SimpleAgent(name="planner", engine=AugLLMConfig()),
            SimpleAgent(name="reasoner", engine=AugLLMConfig()),
        ]

        # Create multi-agent
        multi_agent = MultiAgent(
            name="self_discover",
            agents=agents,
            state_schema=SelfDiscoverState,
            execution_mode="sequential",
        )

        # Verify structure
        assert multi_agent.name == "self_discover"
        assert len(multi_agent.agents) == 4
        assert list(multi_agent.agents.keys()) == [
            "selector",
            "adapter",
            "planner",
            "reasoner",
        ]
        assert multi_agent.execution_mode == "sequential"
        assert multi_agent.state_schema == SelfDiscoverState

    def test_multiagent_with_explicit_routing(self):
        """Test self-discover with explicit edge routing."""
        # Create agents
        agents = {
            "select": SimpleAgent(name="select", engine=AugLLMConfig()),
            "adapt": SimpleAgent(name="adapt", engine=AugLLMConfig()),
            "structure": SimpleAgent(name="structure", engine=AugLLMConfig()),
            "reason": SimpleAgent(name="reason", engine=AugLLMConfig()),
        }

        # Create multi-agent with entry point
        multi_agent = MultiAgent(agents=agents, entry_point="select")

        # Define explicit flow
        multi_agent.add_edge("select", "adapt")
        multi_agent.add_edge("adapt", "structure")
        multi_agent.add_edge("structure", "reason")

        # Verify routing
        assert multi_agent.entry_point == "select"
        assert len(multi_agent.branches) == 3
        assert multi_agent.branches["select"]["type"] == "direct"
        assert multi_agent.branches["select"]["target"] == "adapt"
        assert multi_agent.branches["structure"]["target"] == "reason"

    def test_multiagent_with_error_handling(self):
        """Test self-discover with conditional error handling."""
        # Create agents including error handler
        agents = [
            SimpleAgent(name="selector", engine=AugLLMConfig()),
            SimpleAgent(name="adapter", engine=AugLLMConfig()),
            SimpleAgent(name="planner", engine=AugLLMConfig()),
            SimpleAgent(name="reasoner", engine=AugLLMConfig()),
            SimpleAgent(name="error_handler", engine=AugLLMConfig()),
        ]

        # Create multi-agent
        multi_agent = MultiAgent(agents=agents, entry_point="selector")

        # Main flow
        multi_agent.add_edge("selector", "adapter")
        multi_agent.add_edge("adapter", "planner")

        # Conditional routing from planner
        def check_plan_validity(state: dict[str, Any]) -> str:
            if state.get("error") or not state.get("reasoning_plan"):
                return "error"
            return "continue"

        multi_agent.add_conditional_routing(
            "plannef",
            check_plan_validity,
            {"error": "error_handler", "continue": "reasoner"},
        )

        # Verify
        assert len(multi_agent.agents) == 5
        assert "error_handler" in multi_agent.agents
        assert multi_agent.branches["planner"]["type"] == "conditional"

    def test_multiagent_graph_building(self):
        """Test that the graph builds correctly for self-discover."""
        # Simple sequential agents
        agents = [
            SimpleAgent(name="stage1", engine=AugLLMConfig()),
            SimpleAgent(name="stage2", engine=AugLLMConfig()),
            SimpleAgent(name="stage3", engine=AugLLMConfig()),
            SimpleAgent(name="stage4", engine=AugLLMConfig()),
        ]

        multi_agent = MultiAgent(
            name="self_discover_graph", agents=agents, state_schema=SelfDiscoverState
        )

        # Build graph - this validates the configuration
        graph = multi_agent.build_graph()

        assert graph is not None
        assert graph.name == "self_discover_graph_graph"
        assert graph.state_schema == SelfDiscoverState

    def test_multiagent_with_parallel_analysis(self):
        """Test self-discover variant with parallel module selection."""
        # Create analyzers that work in parallel
        agents = [
            SimpleAgent(name="module_analyzer1", engine=AugLLMConfig()),
            SimpleAgent(name="module_analyzer2", engine=AugLLMConfig()),
            SimpleAgent(name="module_analyzer3", engine=AugLLMConfig()),
            SimpleAgent(name="module_selector", engine=AugLLMConfig()),
            SimpleAgent(name="adapter", engine=AugLLMConfig()),
            SimpleAgent(name="planner", engine=AugLLMConfig()),
        ]

        multi_agent = MultiAgent(agents=agents)

        # Parallel analysis followed by selection
        multi_agent.add_parallel_group(
            ["module_analyzer1", "module_analyzer2", "module_analyzer3"],
            next_agent="module_selector",
        )

        # Continue with normal flow
        multi_agent.add_edge("module_selector", "adapter")
        multi_agent.add_edge("adapter", "planner")

        # Verify parallel configuration
        parallel_key = next(k for k in multi_agent.branches if "parallel" in k)
        assert multi_agent.branches[parallel_key]["type"] == "parallel"
        assert len(multi_agent.branches[parallel_key]["agents"]) == 3
        assert multi_agent.branches[parallel_key]["next"] == "module_selector"

    def test_multiagent_backward_compatibility(self):
        """Test backward compatibility with add_conditional_edges."""
        agents = {
            "classifier": SimpleAgent(name="classifier", engine=AugLLMConfig()),
            "easy_path": SimpleAgent(name="easy_path", engine=AugLLMConfig()),
            "hard_path": SimpleAgent(name="hard_path", engine=AugLLMConfig()),
            "finalizer": SimpleAgent(name="finalizer", engine=AugLLMConfig()),
        }

        multi_agent = MultiAgent(agents=agents, entry_point="classifier")

        # Use backward-compatible method
        def route_by_difficulty(state: dict[str, Any]) -> str:
            difficulty = state.get("difficulty", "medium")
            if difficulty == "easy":
                return "easy_path"
            if difficulty == "hard":
                return "hard_path"
            return "easy_path"  # default

        multi_agent.add_conditional_edges("classifier", route_by_difficulty)

        # Both paths lead to finalizer
        multi_agent.add_edge("easy_path", "finalizer")
        multi_agent.add_edge("hard_path", "finalizer")

        # Verify
        assert multi_agent.branches["classifier"]["type"] == "conditional_direct"
        assert "path_fn" in multi_agent.branches["classifier"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
