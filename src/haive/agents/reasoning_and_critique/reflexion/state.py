"""Reflexion agent state."""

from typing import Any

from typing_extensions import TypedDict


class ReflexionState(TypedDict):
    """State for the Reflexion graph.

    Fields:
        input: The original user query.
        draft: The current best answer text.
        reflections: List of reflection/critique strings from each iteration.
        revision_count: How many revise iterations have been completed.
    """

    input: str
    draft: str
    reflections: list[str]
    revision_count: int
