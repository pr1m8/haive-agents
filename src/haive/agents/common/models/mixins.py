"""Mixins model module.

This module provides mixins functionality for the Haive framework.

Classes:
    Reasoning: Reasoning implementation.

Functions:
"""

from pydantic import RootModel


class Reasoning(RootModel):
    """A mixin for reasoning about the world."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.reasoning = []
