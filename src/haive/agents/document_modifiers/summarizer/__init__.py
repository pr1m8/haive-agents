"""Summarizer document modifiers.

This module provides tools for summarizing documents using various strategies.
"""

# Import classes from submodules

try:
    from haive.agents.document_modifiers.summarizer.base import SummarizerAgent
    from haive.agents.document_modifiers.summarizer.iterative_refinement.iterative_summarizer import (
        IterativeSummarizer,
    )


except ImportError:
    SummarizerAgent = None

try:
except ImportError:
    IterativeSummarizer = None

__all__ = [
    "IterativeSummarizer",
    "SummarizerAgent",
]
