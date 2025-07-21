#!/usr/bin/env python3
"""Answer generator components for SimpleRAG."""

from .models import RAGAnswer
from .prompts import RAG_CHAT_TEMPLATE

__all__ = ["RAG_CHAT_TEMPLATE", "RAGAnswer"]
