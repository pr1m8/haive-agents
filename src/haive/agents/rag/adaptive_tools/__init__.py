"""Adaptive RAG with Tools Integration.

Enhanced adaptive RAG that integrates search tools and ReAct patterns for dynamic tool usage.
Includes Google Search integration and intelligent tool routing.
"""

from haive.agents.rag.adaptive_tools.agent import (
    AdaptiveToolsRAGAgent,
    SearchIntegrationAgent,
    ToolSelectionAgent,
)

__all__ = ["AdaptiveToolsRAGAgent", "SearchIntegrationAgent", "ToolSelectionAgent"]
