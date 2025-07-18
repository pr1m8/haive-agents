"""Document Grading Module.

Standalone document grading and quality assessment agents.
"""

from haive.agents.rag.document_grading.agent import (
    DocumentGradingAgent,
    DocumentGradingRAGAgent,
)

__all__ = ["DocumentGradingAgent", "DocumentGradingRAGAgent"]
