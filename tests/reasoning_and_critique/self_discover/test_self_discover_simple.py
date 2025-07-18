"""Test the Self-Discover pattern with our unified MultiAgent - simplified version."""

from typing import Any, Dict, List, Optional

import pytest
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema import StateSchema
from langchain_core.prompts import PromptTemplate
from pydantic import Field

from haive.agents.multi.clean import MultiAgent
from haive.agents.simple import SimpleAgent


class SimpleSelfDiscoverState(StateSchema):
    """Simplified state for testing."""

    task: str = Field(default="", description="Task to solve")
    selected_modules: Optional[str] = Field(default=None)
    adapted_modules: Optional[str] = Field(default=None)
    reasoning_plan: Optional[str] = Field(default=None)
    final_answer: Optional[str] = Field(default=None)


def create_test_agents():
    """Create test agents for self-discover workflow."""
    # Simple selector agent
    selector = SimpleAgent(
        name="selector",
        engine=AugLLMConfig(
            temperature=0.1, system_message="Select reasoning modules for the task."
        ),
    )

    # Simple adapter agent
    adapter = SimpleAgent(
        name="adapter",
        engine=AugLLMConfig(
            temperature=0.1, system_message="Adapt modules to the specific task."
        ),
    )

    # Simple planner agent
    planner = SimpleAgent(
        name="planner",
        engine=AugLLMConfig(
            temperature=0.1, system_message="Create a step-by-step plan."
        ),
    )

    # Simple reasoner agent
    reasoner = SimpleAgent(
        name="reasoner",
        engine=AugLLMConfig(
            temperature=0.1, system_message="Execute the plan and provide an answer."
        ),
    )

    return [selector, adapter, planner, reasoner]


def test_multiagent_sequential_creation():
    """Test creating a sequential multi-agent system."""
    agents = create_test_agents()

    # Create multi-agent
    multi_agent = MultiAgent(
        name="self_discover_test",
        agents=agents,
        state_schema=SimpleSelfDiscoverState,
        execution_mode="sequential",
    )

    # Verify creation
    assert multi_agent.name == "self_discover_test"
    assert len(multi_agent.agents) == 4
    assert list(multi_agent.agents.keys()) == [
        "selector",
        "adapter",
        "planner",
        "reasoner",
    ]
    assert multi_agent.execution_mode == "sequential"
    assert multi_agent.state_schema == SimpleSelfDiscoverState


def test_multiagent_with_edges():
    """Test creating multi-agent with explicit edges."""
    agents = create_test_agents()

    # Create multi-agent with entry point
    multi_agent = MultiAgent(
        name="self_discover_edges", agents=agents, entry_point="selector"
    )

    # Add explicit edges
    multi_agent.add_edge("selector", "adapter")
    multi_agent.add_edge("adapter", "planner")
    multi_agent.add_edge("planner", "reasoner")

    # Verify routing
    assert len(multi_agent.branches) == 3
    assert multi_agent.branches["selector"]["type"] == "direct"
    assert multi_agent.branches["selector"]["target"] == "adapter"
    assert multi_agent.entry_point == "selector"


def test_multiagent_with_conditional():
    """Test multi-agent with conditional routing."""
    agents = create_test_agents()

    # Add an error handler
    error_handler = SimpleAgent(
        name="error_handler", engine=AugLLMConfig(system_message="Handle errors.")
    )
    agents.append(error_handler)

    # Create multi-agent
    multi_agent = MultiAgent(
        name="self_discover_conditional", agents=agents, entry_point="selector"
    )

    # Add main flow
    multi_agent.add_edge("selector", "adapter")
    multi_agent.add_edge("adapter", "planner")

    # Add conditional routing from planner
    def route_from_planner(state: Dict[str, Any]) -> str:
        if state.get("error"):
            return "error"
        return "continue"

    multi_agent.add_conditional_routing(
        "planner",
        route_from_planner,
        {"error": "error_handler", "continue": "reasoner"},
    )

    # Verify
    assert len(multi_agent.agents) == 5
    assert "error_handler" in multi_agent.agents
    assert multi_agent.branches["planner"]["type"] == "conditional"
    assert "condition_fn" in multi_agent.branches["planner"]


def test_multiagent_graph_building():
    """Test that the graph builds without errors."""
    agents = create_test_agents()

    multi_agent = MultiAgent(
        name="test_graph", agents=agents, execution_mode="sequential"
    )

    # Build graph
    graph = multi_agent.build_graph()

    # Verify graph
    assert graph is not None
    assert graph.name == "test_graph_graph"
    assert graph.state_schema is not None


def test_multiagent_with_parallel_group():
    """Test multi-agent with parallel execution."""
    # Create analyzers that run in parallel
    analyzer1 = SimpleAgent(name="analyzer1", engine=AugLLMConfig())
    analyzer2 = SimpleAgent(name="analyzer2", engine=AugLLMConfig())
    analyzer3 = SimpleAgent(name="analyzer3", engine=AugLLMConfig())
    aggregator = SimpleAgent(name="aggregator", engine=AugLLMConfig())

    # Create multi-agent
    multi_agent = MultiAgent(agents=[analyzer1, analyzer2, analyzer3, aggregator])

    # Configure parallel execution
    multi_agent.add_parallel_group(
        ["analyzer1", "analyzer2", "analyzer3"], next_agent="aggregator"
    )

    # Verify
    assert len(multi_agent.branches) == 1
    branch_key = list(multi_agent.branches.keys())[0]
    assert "parallel" in branch_key
    branch = multi_agent.branches[branch_key]
    assert branch["type"] == "parallel"
    assert branch["agents"] == ["analyzer1", "analyzer2", "analyzer3"]
    assert branch["next"] == "aggregator"


@pytest.mark.asyncio
async def test_multiagent_simple_execution():
    """Test simple execution (with mocked result for testing)."""
    # Create simple test agents
    agent1 = SimpleAgent(name="agent1", engine=AugLLMConfig(temperature=0.0))
    agent2 = SimpleAgent(name="agent2", engine=AugLLMConfig(temperature=0.0))

    # Create sequential multi-agent
    multi_agent = MultiAgent(agents=[agent1, agent2], execution_mode="sequential")

    # For now, just verify it's created correctly
    # Real execution would require actual LLM calls
    assert multi_agent is not None
    assert len(multi_agent.agents) == 2


if __name__ == "__main__":
    # Run tests
    pytest.main([__file__, "-v"])
