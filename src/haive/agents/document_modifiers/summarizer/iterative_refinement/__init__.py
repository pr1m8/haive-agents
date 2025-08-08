"""Module exports."""

from haive.agents.document_modifiers.base.utils import normalize_contents

from .agent import IterativeSummarizer
from .config import IterativeSummarizerConfig
from .state import (
    IterativeSummarizerInput,
    IterativeSummarizerOutput,
    IterativeSummarizerState,
)


# Create module-level function for compatibility
def should_refine(state: IterativeSummarizerState) -> str:
    """Check if the iterative summarization should continue."""
    return state.should_refine()


__all__ = [
    "IterativeSummarizer",
    "IterativeSummarizerConfig",
    "IterativeSummarizerInput",
    "IterativeSummarizerOutput",
    "IterativeSummarizerState",
    "normalize_contents",
    "should_refine",
]
