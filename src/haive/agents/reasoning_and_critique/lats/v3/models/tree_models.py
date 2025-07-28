"""Tree data structures for LATS algorithm."""

import math
import uuid
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class LATSNode(BaseModel):
    """A node in the LATS Monte Carlo Tree Search.

    Each node represents a state in the search tree with:
    - Action that led to this state
    - Visits count for UCB calculation
    - Reward sum for scoring
    - Parent/child relationships
    """

    # Node identification
    node_id: str = Field(
        default_factory=lambda: str(uuid.uuid4()), description="Unique node identifier"
    )
    parent_id: Optional[str] = Field(default=None, description="Parent node ID")
    depth: int = Field(default=0, description="Depth in the tree")

    # Action and state
    action: str = Field(description="Action taken to reach this node")
    state_description: str = Field(description="Description of the state at this node")

    # MCTS statistics
    visits: int = Field(default=0, description="Number of times this node was visited")
    reward_sum: float = Field(
        default=0.0, description="Sum of all rewards from simulations"
    )

    # Tree structure (stored as IDs to avoid circular references)
    children_ids: List[str] = Field(default_factory=list, description="Child node IDs")

    # Solution status
    is_terminal: bool = Field(
        default=False, description="Whether this is a terminal/solution node"
    )
    is_solved: bool = Field(
        default=False, description="Whether this node represents a valid solution"
    )

    # Reflection data
    reflection_score: float = Field(
        default=0.0, description="Reflection/evaluation score (0.0-1.0)"
    )
    reflection_reasoning: str = Field(
        default="", description="Reasoning behind the reflection score"
    )

    def average_reward(self) -> float:
        """Calculate the average reward for this node."""
        if self.visits == 0:
            return 0.0
        return self.reward_sum / self.visits

    def ucb_score(
        self, exploration_weight: float = 1.4, parent_visits: int = 1
    ) -> float:
        """Calculate Upper Confidence Bound (UCB) score for node selection.

        Args:
            exploration_weight: Exploration vs exploitation balance (higher = more exploration)
            parent_visits: Number of times parent node was visited

        Returns:
            UCB score for this node
        """
        if self.visits == 0:
            return float("inf")  # Unvisited nodes have infinite priority

        exploitation = self.average_reward()
        exploration = exploration_weight * math.sqrt(
            math.log(parent_visits) / self.visits
        )

        return exploitation + exploration

    def update_statistics(self, reward: float) -> None:
        """Update node statistics after a simulation.

        Args:
            reward: Reward obtained from this simulation
        """
        self.visits += 1
        self.reward_sum += reward

    def add_child(self, child_id: str) -> None:
        """Add a child node ID to this node."""
        if child_id not in self.children_ids:
            self.children_ids.append(child_id)

    def is_leaf(self) -> bool:
        """Check if this node is a leaf (has no children)."""
        return len(self.children_ids) == 0


class TreeStatistics(BaseModel):
    """Statistics about the LATS search tree."""

    total_nodes: int = Field(description="Total number of nodes in the tree")
    max_depth: int = Field(description="Maximum depth reached in the tree")
    total_visits: int = Field(description="Total number of node visits")
    solutions_found: int = Field(description="Number of solution nodes found")

    # Per-depth statistics
    nodes_per_depth: Dict[int, int] = Field(
        default_factory=dict, description="Number of nodes at each depth"
    )

    # Search quality metrics
    best_solution_score: float = Field(
        default=0.0, description="Score of the best solution found"
    )
    average_node_score: float = Field(
        default=0.0, description="Average score across all nodes"
    )

    # Performance metrics
    iterations_completed: int = Field(
        default=0, description="Number of MCTS iterations completed"
    )
    time_elapsed: float = Field(default=0.0, description="Time elapsed in seconds")

    def update_depth_stats(self, depth: int) -> None:
        """Update statistics for a specific depth level."""
        if depth not in self.nodes_per_depth:
            self.nodes_per_depth[depth] = 0
        self.nodes_per_depth[depth] += 1

        if depth > self.max_depth:
            self.max_depth = depth
