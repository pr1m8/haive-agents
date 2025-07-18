"""Quick Search Agent module.

Provides fast, basic search responses similar to Perplexity's Quick Search feature.
Optimized for speed and concise answers.
"""

from haive.agents.memory.search.quick_search.agent import QuickSearchAgent
from haive.agents.memory.search.quick_search.models import QuickSearchResponse

__all__ = ["QuickSearchAgent", "QuickSearchResponse"]
