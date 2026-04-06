"""Perplexity-style deep research agent.

Multi-agent composition:
  QueryAnalyzer (SimpleAgent) -> Researcher (ReactAgent + search tools) -> Synthesizer (SimpleAgent)

Usage:
    from haive.agents.research.perplexity_agent import create_research_agent
    agent = create_research_agent()
    result = agent.run("What are the latest advances in quantum computing?")
"""

from __future__ import annotations

import logging
from typing import Any

from langchain_core.tools import tool
from pydantic import Field

from haive.agents.multi.agent import MultiAgent
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Search tool – uses Tavily when available, otherwise a lightweight fallback
# ---------------------------------------------------------------------------

@tool
def web_search(query: str) -> str:
    """Search the web for information on a topic."""
    return (
        f"[mock search] No live results available. "
        f"Pretend you found comprehensive information about: {query}"
    )


def _make_tavily_tool() -> Any | None:
    """Try to create a Tavily search tool. Returns None on failure."""
    # Try newer langchain_tavily package first
    try:
        from langchain_tavily import TavilySearch  # type: ignore[import-untyped]

        return TavilySearch(max_results=5)
    except Exception:
        pass
    # Try legacy langchain_community path
    try:
        from langchain_community.tools.tavily_search import TavilySearchResults  # type: ignore[import-untyped]

        return TavilySearchResults(max_results=5)
    except Exception:
        pass
    return None


def _default_search_tools() -> list:
    """Return the best available search tools.

    Tries Tavily first, falls back to a mock web_search tool.
    """
    tavily = _make_tavily_tool()
    if tavily is not None:
        # Smoke-test that AugLLMConfig can accept this tool
        try:
            AugLLMConfig(tools=[tavily])
            return [tavily]
        except Exception:
            logger.warning("Tavily tool incompatible with AugLLMConfig, using mock")
    return [web_search]


# ---------------------------------------------------------------------------
# Sub-agent factories
# ---------------------------------------------------------------------------

def _build_query_analyzer(name: str) -> SimpleAgent:
    return SimpleAgent(
        name=f"{name}_query_analyzer",
        engine=AugLLMConfig(
            system_message=(
                "You are a query analysis expert. Given a user question, produce a "
                "clear, concise research plan: restate the core question, list 2-4 "
                "targeted search queries that would cover the topic thoroughly, and "
                "note any ambiguities to resolve. Be brief and actionable."
            ),
            temperature=0.2,
        ),
    )


def _build_researcher(
    name: str,
    tools: list | None = None,
    max_iterations: int = 6,
) -> ReactAgent:
    search_tools = tools or _default_search_tools()
    return ReactAgent(
        name=f"{name}_researcher",
        engine=AugLLMConfig(
            system_message=(
                "You are a thorough web researcher. Use the search tools to gather "
                "information relevant to the research plan in the conversation. "
                "Run multiple searches to cover different angles. After gathering "
                "enough evidence, summarize your raw findings with source attributions."
            ),
            tools=search_tools,
            temperature=0.3,
        ),
        max_iterations=max_iterations,
    )


def _build_synthesizer(name: str) -> SimpleAgent:
    return SimpleAgent(
        name=f"{name}_synthesizer",
        engine=AugLLMConfig(
            system_message=(
                "You are a synthesis expert. Given raw research findings in the "
                "conversation, produce a comprehensive, well-structured answer. "
                "Include inline citations like [1], [2] where possible. End with "
                "a 'Sources' section listing the references. Write clearly and "
                "concisely, covering the key points without unnecessary filler."
            ),
            temperature=0.4,
        ),
    )


# ---------------------------------------------------------------------------
# ResearchAgent – composed MultiAgent
# ---------------------------------------------------------------------------


class ResearchAgent(MultiAgent):
    """Perplexity-style research agent using MultiAgent sequential composition.

    Pipeline: QueryAnalyzer -> Researcher -> Synthesizer

    Example::

        agent = ResearchAgent(name="researcher")
        result = agent.run("What is quantum computing?")
    """

    max_search_iterations: int = Field(
        default=6,
        ge=1,
        le=20,
        description="Maximum search iterations for the researcher sub-agent.",
    )

    search_tools: list[Any] = Field(
        default_factory=list,
        description="Custom search tools. Falls back to Tavily or mock.",
    )


# ---------------------------------------------------------------------------
# Factory function
# ---------------------------------------------------------------------------


def create_research_agent(
    name: str = "perplexity",
    tools: list | None = None,
    max_search_iterations: int = 6,
) -> ResearchAgent:
    """Create a Perplexity-style research agent.

    Args:
        name: Agent name.
        tools: Custom search tools (defaults to Tavily if installed, else mock).
        max_search_iterations: Max reasoning loops for the researcher.

    Returns:
        ResearchAgent ready for execution.
    """
    analyzer = _build_query_analyzer(name)
    researcher = _build_researcher(name, tools=tools, max_iterations=max_search_iterations)
    synthesizer = _build_synthesizer(name)

    agent = ResearchAgent(
        name=name,
        agents=[analyzer, researcher, synthesizer],
        execution_mode="sequential",
        max_search_iterations=max_search_iterations,
        search_tools=tools or _default_search_tools(),
    )

    logger.info(
        f"Created ResearchAgent '{name}' with sub-agents: "
        f"{[a.name for a in agent.agents]}"
    )
    return agent
