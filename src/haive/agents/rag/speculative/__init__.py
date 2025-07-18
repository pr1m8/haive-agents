"""Speculative RAG Module.

Speculative RAG with parallel hypothesis generation and verification.
Uses structured output models for complex reasoning and iterative processing.
"""

from haive.agents.rag.speculative.agent import (
    HypothesisGeneratorAgent,
    ParallelVerificationAgent,
    SpeculativeRAGAgent,
)

__all__ = [
    "HypothesisGeneratorAgent",
    "ParallelVerificationAgent",
    "SpeculativeRAGAgent",
]
