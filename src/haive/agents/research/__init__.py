"""Research Agents - Advanced research and information gathering agents.

This module provides specialized agents for conducting research, gathering information,
and generating comprehensive reports on various topics.

Available Agents:
    - PersonResearchAgent: Comprehensive person research with multi-source data
    - OpenPerplexityAgent: Web search and research capabilities
    - STORMAgent: Structured research methodology (in development)

Example:
    Basic research usage::

        from haive.agents.research.person import PersonResearchAgent

        agent = PersonResearchAgent(
            name="researcher",
            research_topic="AI Safety"
        )

        result = await agent.ainvoke({"query": "Recent developments in AI safety"})
"""

from haive.agents.research.open_perplexity import ResearchAgent as OpenPerplexityAgent
from haive.agents.research.open_perplexity import ResearchAgentConfig as OpenPerplexityConfig
from haive.agents.research.person import PersonResearchAgent
from haive.agents.research.storm import STORMAgentConfig

# Import available research agents

# Import STORM config (agent implementation is still in development)

__all__ = [
    "OpenPerplexityAgent",
    "OpenPerplexityConfig",
    "PersonResearchAgent",
    "STORMAgentConfig",  # Config only - agent still in development
]
