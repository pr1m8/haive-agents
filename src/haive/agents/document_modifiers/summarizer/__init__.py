"""Summarizer document modifiers.

This module provides tools for summarizing documents using various strategies.
"""

# Import classes from submodules

try:
    from haive.agents.document_modifiers.summarizer.iterative_refinement.agent import (
        IterativeSummarizer,
    )
except ImportError:
    IterativeSummarizer = None

__all__ = [
    "IterativeSummarizer",
]
