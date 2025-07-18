"""Deep Research Agent module.

Provides comprehensive research with multiple sources and detailed analysis.
Similar to Perplexity's Deep Research feature.
"""

from haive.agents.memory.search.deep_research.agent import DeepResearchAgent
from haive.agents.memory.search.deep_research.models import DeepResearchResponse

__all__ = ["DeepResearchAgent", "DeepResearchResponse"]
