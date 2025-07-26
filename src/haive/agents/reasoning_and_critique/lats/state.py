from typing_extensions import TypedDict

from haive.agents.reasoning_and_critique.lats.node import Node


class TreeState(TypedDict):
    # The full tree
    root: Node
    # The original input
    input: str
