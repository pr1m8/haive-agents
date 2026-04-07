"""Research agents — web search, deep research, and structured investigation.

Available agents:
    - ResearchAgent (Perplexity-style): 3-stage QueryAnalyzer → Researcher → Synthesizer
    - DeepResearchAgent: 5-stage pipeline with shared research store
    - OpenPerplexityAgent: Legacy, full research pipeline
    - PersonResearchAgent: Legacy, person-focused research
    - STORMAgentConfig: Structured research config (legacy)

Example:
    from haive.agents.research import create_research_agent
    agent = create_research_agent()
    result = agent.run("What is quantum computing?")
"""

# New multi-agent research implementations
from haive.agents.research.deep_research_agent import (
    DeepResearchAgent,
    create_deep_research_agent,
)
from haive.agents.research.perplexity_agent import (
    ResearchAgent,
    create_research_agent,
)

# Legacy research agents
from haive.agents.research.open_perplexity import ResearchAgent as OpenPerplexityAgent
from haive.agents.research.open_perplexity import (
    ResearchAgentConfig as OpenPerplexityConfig,
)
from haive.agents.research.person import PersonResearchAgent
from haive.agents.research.storm import STORMAgentConfig

__all__ = [
    # New multi-agent research
    "DeepResearchAgent",
    "ResearchAgent",
    "create_deep_research_agent",
    "create_research_agent",
    # Legacy
    "OpenPerplexityAgent",
    "OpenPerplexityConfig",
    "PersonResearchAgent",
    "STORMAgentConfig",
]
