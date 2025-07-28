"""Test the NodeSelector agent for LATS v3."""

import os
import sys

import pytest

# Add the src directory to Python path to avoid import issues
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../../../src"))

from haive.agents.reasoning_and_critique.lats.v3.agents.node_selector import (
    NodeSelector,
)
from haive.agents.reasoning_and_critique.lats.v3.models.evaluation_models import (
    UCBSelection,
)
from haive.agents.reasoning_and_critique.lats.v3.models.tree_models import LATSNode


class TestNodeSelector:
    """Test the NodeSelector agent."""

    @pytest.mark.asyncio
    async def test_node_selector_creation(self):
        """Test that NodeSelector can be created properly."""
        selector = NodeSelector(name="test_selector")
        assert selector.name == "test_selector"
        assert selector.exploration_weight == 1.4
        assert selector.agent is not None
        assert selector.agent.name == "test_selector"

    @pytest.mark.asyncio
    async def test_node_selector_with_custom_exploration_weight(self):
        """Test NodeSelector with custom exploration weight."""
        selector = NodeSelector(name="test_selector", exploration_weight=2.0)
        assert selector.exploration_weight == 2.0

    @pytest.mark.asyncio
    async def test_select_single_node(self):
        """Test selecting when there's only one node."""
        selector = NodeSelector(name="test_selector")

        # Create a single node
        root = LATSNode(
            action="Initial state",
            state_description="Starting the problem solving process",
            visits=5,
            reward_sum=3.5,
            reflection_score=0.7,
            reflection_reasoning="Good starting point",
        )

        nodes = {root.node_id: root}
        problem = "Find the best path through a maze"

        # Execute selection
        result = await selector.select_node(nodes, problem)

        # Verify result structure
        assert isinstance(result, UCBSelection)
        assert result.selected_node_id == root.node_id
        assert isinstance(result.selection_reasoning, str)
        assert len(result.selection_reasoning) > 0
        assert result.ucb_score > 0
        assert result.exploitation_component >= 0
        assert result.exploration_component >= 0

    @pytest.mark.asyncio
    async def test_select_from_multiple_nodes(self):
        """Test selecting from multiple nodes with different UCB scores."""
        selector = NodeSelector(name="test_selector")

        # Create multiple nodes with different statistics
        node1 = LATSNode(
            action="Take the left path",
            state_description="Exploring the left branch of the maze",
            visits=10,
            reward_sum=7.0,  # Average: 0.7
            reflection_score=0.7,
            reflection_reasoning="Promising direction with moderate complexity",
        )

        node2 = LATSNode(
            action="Take the right path",
            state_description="Exploring the right branch of the maze",
            visits=5,
            reward_sum=4.0,  # Average: 0.8
            reflection_score=0.8,
            reflection_reasoning="Shorter path but with obstacles",
        )

        node3 = LATSNode(
            action="Go straight ahead",
            state_description="Following the main corridor",
            visits=0,  # Unvisited - should have infinite UCB
            reward_sum=0.0,
            reflection_score=0.0,
            reflection_reasoning="Not yet explored",
        )

        nodes = {node1.node_id: node1, node2.node_id: node2, node3.node_id: node3}

        problem = "Find the optimal path through a complex maze"

        # Execute selection
        result = await selector.select_node(nodes, problem)

        # Verify result
        assert isinstance(result, UCBSelection)
        # Should select node3 due to infinite UCB (unvisited)
        assert result.selected_node_id == node3.node_id
        assert (
            "unvisited" in result.selection_reasoning.lower()
            or "unexplored" in result.selection_reasoning.lower()
        )
        assert result.ucb_score == float("inf")

    @pytest.mark.asyncio
    async def test_select_with_all_visited_nodes(self):
        """Test selection when all nodes have been visited."""
        selector = NodeSelector(name="test_selector", exploration_weight=1.4)

        # Create nodes that have all been visited
        # Parent has 20 total visits across children

        node1 = LATSNode(
            action="Option A: Direct approach",
            state_description="Taking the direct but risky path",
            visits=8,
            reward_sum=6.4,  # Average: 0.8
            reflection_score=0.8,
            reflection_reasoning="High risk, high reward approach",
        )

        node2 = LATSNode(
            action="Option B: Cautious approach",
            state_description="Taking the safer but longer path",
            visits=12,
            reward_sum=8.4,  # Average: 0.7
            reflection_score=0.7,
            reflection_reasoning="Lower risk, consistent progress",
        )

        # Update node UCB scores based on parent visits
        node1.parent_id = "parent_node"
        node2.parent_id = "parent_node"

        nodes = {node1.node_id: node1, node2.node_id: node2}

        problem = "Balance risk vs reward in pathfinding"

        # Calculate expected UCB scores manually
        # Node1: 0.8 + 1.4 * sqrt(ln(20)/8) ≈ 0.8 + 1.4 * 0.5 = 1.5
        # Node2: 0.7 + 1.4 * sqrt(ln(20)/12) ≈ 0.7 + 1.4 * 0.4 = 1.26

        result = await selector.select_node(nodes, problem)

        # Should select node1 due to higher UCB score
        assert isinstance(result, UCBSelection)
        assert result.selected_node_id in [node1.node_id, node2.node_id]
        assert result.ucb_score > 0
        assert result.exploitation_component > 0
        assert result.exploration_component > 0

    @pytest.mark.asyncio
    async def test_create_selection_prompt(self):
        """Test the prompt creation for node selection."""
        selector = NodeSelector(name="test_selector")

        # Create test nodes
        node1 = LATSNode(
            action="Test action",
            state_description="Test state",
            visits=5,
            reward_sum=3.0,
            reflection_score=0.6,
            reflection_reasoning="Test reasoning",
        )

        nodes = {node1.node_id: node1}
        problem = "Test problem"

        # Create prompt
        prompt = selector.create_selection_prompt(nodes, problem)

        # Verify prompt content
        assert "UCB" in prompt
        assert "Upper Confidence Bound" in prompt
        assert problem in prompt
        assert node1.action in prompt
        assert str(node1.ucb_score()) in prompt
        assert "exploitation" in prompt.lower()
        assert "exploration" in prompt.lower()
