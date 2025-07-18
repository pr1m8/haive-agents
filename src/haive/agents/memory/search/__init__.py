"""Search agents for Perplexity-style research system.

This module provides specialized search agents that mirror Perplexity's architecture:
- QuickSearchAgent: Fast, basic search responses
- ProSearchAgent: Deep, contextual search with preferences
- DeepResearchAgent: Comprehensive research with multiple sources
- LabsAgent: Interactive project automation with tools

All agents are built with:
- Prompt templates for consistent behavior
- Structured output models for predictable responses
- Optional tools for enhanced capabilities
- Memory integration for context retention
"""

from haive.agents.memory.search.deep_research.agent import DeepResearchAgent
from haive.agents.memory.search.labs.agent import LabsAgent
from haive.agents.memory.search.pro_search.agent import ProSearchAgent
from haive.agents.memory.search.quick_search.agent import QuickSearchAgent

__all__ = ["QuickSearchAgent", "ProSearchAgent", "DeepResearchAgent", "LabsAgent"]
