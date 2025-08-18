from __future__ import annotations

import math
from collections import deque
from typing import Any

from langchain_core.messages import BaseMessage, HumanMessage
from pydantic import BaseModel, Field, computed_field, field_serializer


class Reflection(BaseModel):
    reflections: str = Field(..., description="Critique and reflection")
    score: int = Field(..., ge=0, le=10, description="0-10 score")
    found_solution: bool = Field(..., description="True if task was solved")

    def as_message(self) -> HumanMessage:
        """As Message.

        Returns:
            [TODO: Add return description]
        """
        return HumanMessage(
            content=f"Reasoning: {self.reflections}\nScore: {self.score}"
        )

    @property
    def normalized_score(self) -> float:
        """Normalized Score.

        Returns:
            [TODO: Add return description]
        """
        return self.score / 10.0


class TreeNode(BaseModel):
    messages: list[BaseMessage]
    reflection: Reflection
    parent: TreeNode | None = Field(default=None, exclude=True)
    children: list[TreeNode] = Field(default_factory=list)
    value: float = 0.0
    visits: int = 0
    depth: int = 1
    _is_solved: bool = False

    def __init__(self, **data: Any):
        """Init  ."""
        super().__init__(**data)
        self.depth = self.parent.depth + 1 if self.parent else 1
        self._is_solved = self.reflection.found_solution
        if self._is_solved:
            self._mark_tree_as_solved()
        self.backpropagate(self.reflection.normalized_score)

    def backpropagate(self, reward: float):
        """Backpropagate.

        Args:
            reward: [TODO: Add description]
        """
        node = self
        while node:
            node.visits += 1
            node.value = (node.value * (node.visits - 1) + reward) / node.visits
            node = node.parent

    def _mark_tree_as_solved(self):
        node = self.parent
        while node:
            node._is_solved = True
            node = node.parent

    def get_messages(self, include_reflections: bool = True) -> list[BaseMessage]:
        """Get Messages.

        Args:
            include_reflections: [TODO: Add description]

        Returns:
            [TODO: Add return description]
        """
        return self.messages + (
            [self.reflection.as_message()] if include_reflections else []
        )

    def get_trajectory(self, include_reflections: bool = True) -> list[BaseMessage]:
        """Get Trajectory.

        Args:
            include_reflections: [TODO: Add description]

        Returns:
            [TODO: Add return description]
        """
        node = self
        messages = []
        while node:
            messages.extend(reversed(node.get_messages(include_reflections)))
            node = node.parent
        return list(reversed(messages))

    def _get_all_children(self) -> list[TreeNode]:
        all_nodes = []
        nodes = deque([self])
        while nodes:
            node = nodes.popleft()
            all_nodes.extend(node.children)
            nodes.extend(node.children)
        return all_nodes

    def get_best_solution(self) -> TreeNode:
        """Get Best Solution.

        Returns:
            [TODO: Add return description]
        """
        all_nodes = [self, *self._get_all_children()]
        best = max(
            all_nodes,
            key=lambda node: int(node.is_terminal and node.is_solved) * node.value,
        )
        return best

    def upper_confidence_bound(self, exploration_weight=1.0) -> float:
        """Upper Confidence Bound.

        Args:
            exploration_weight: [TODO: Add description]

        Returns:
            [TODO: Add return description]
        """
        if self.parent is None:
            raise ValueError("Cannot obtain UCT from root node")
        if self.visits == 0:
            return self.value
        average_reward = self.value / self.visits
        exploration_term = math.sqrt(math.log(self.parent.visits) / self.visits)
        return average_reward + exploration_weight * exploration_term

    @property
    def is_solved(self) -> bool:
        """Is Solved.

        Returns:
            [TODO: Add return description]
        """
        return self._is_solved

    @property
    def is_terminal(self) -> bool:
        """Is Terminal.

        Returns:
            [TODO: Add return description]
        """
        return not self.children

    @property
    def best_child_score(self) -> float | None:
        """Best Child Score.

        Returns:
            [TODO: Add return description]
        """
        if not self.children:
            return None
        return max(child.value for child in self.children if child.is_solved)

    @computed_field
    @property
    def height(self) -> int:
        """Height.

        Returns:
            [TODO: Add return description]
        """
        if not self.children:
            return 1
        return 1 + max(child.height for child in self.children)

    @field_serializer("children", mode="wrap")
    def serialize_children(self, children, handler) -> Any:
        """Serialize Children.

        Args:
            children: [TODO: Add description]
            handler: [TODO: Add description]

        Returns:
            [TODO: Add return description]
        """
        try:
            return handler(children)
        except ValueError as exc:
            if "Circular reference" not in str(exc):
                raise
            return [{"depth": c.depth, "value": c.value} for c in children]


TreeNode.model_rebuild()
