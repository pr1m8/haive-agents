"""LATS tree state."""

from typing import Any

from typing_extensions import TypedDict

from haive.agents.reasoning_and_critique.lats.models import Node


class TreeState(TypedDict):
    """State for the LATS tree search graph."""
    root: Node
    input: str
    messages: list[Any]
    output: str
