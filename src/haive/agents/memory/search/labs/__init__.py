"""Labs Agent module.

Provides interactive project automation with tools and workflows.
Similar to Perplexity's Labs feature.
"""

from haive.agents.memory.search.labs.agent import LabsAgent
from haive.agents.memory.search.labs.models import LabsResponse

__all__ = ["LabsAgent", "LabsResponse"]
