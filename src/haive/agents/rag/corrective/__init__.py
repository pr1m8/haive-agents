"""Corrective RAG Module.

Self-correcting retrieval with quality assessment.
"""

try:
    from haive.agents.rag.corrective.agent import CorrectiveRAGAgent
except ImportError:
    CorrectiveRAGAgent = None

from haive.agents.rag.corrective.agent_v2 import CorrectiveRAGAgentV2

__all__ = ["CorrectiveRAGAgent", "CorrectiveRAGAgentV2"]
