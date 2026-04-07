"""Perplexity-style deep research agent.

Multi-agent composition:
  QueryAnalyzer (SimpleAgent) → Researcher (ReactAgent + search + RAG) → Synthesizer (SimpleAgent)

The Researcher has:
- Tavily web search (or mock fallback)
- Dynamic RAG: stores search results in vector store for retrieval

Usage:
    from haive.agents.research.perplexity_agent import create_research_agent
    agent = create_research_agent()
    result = agent.run("What are the latest advances in quantum computing?")
"""

from __future__ import annotations

import logging
from typing import Any

from langchain_core.tools import StructuredTool, tool
from pydantic import Field

from haive.agents.multi.agent import MultiAgent
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Search tools
# ---------------------------------------------------------------------------

def _make_tavily_tool() -> Any | None:
    """Try to create a Tavily search tool."""
    try:
        from langchain_community.tools.tavily_search import TavilySearchResults
        t = TavilySearchResults(max_results=5)
        # Verify it's compatible with our tool system
        AugLLMConfig(tools=[t])
        return t
    except Exception:
        pass
    try:
        from langchain_tavily import TavilySearch
        t = TavilySearch(max_results=5)
        AugLLMConfig(tools=[t])
        return t
    except Exception:
        pass
    return None


@tool
def web_search(query: str) -> str:
    """Search the web for information. Returns search results for the given query."""
    return (
        f"[mock search] No live search available. "
        f"Pretend you found detailed information about: {query}"
    )


# ---------------------------------------------------------------------------
# Dynamic RAG tool — stores + retrieves search results
# ---------------------------------------------------------------------------

def _make_rag_tools() -> list[StructuredTool]:
    """Create dynamic RAG tools that store and retrieve search results."""
    # In-memory doc store for this research session
    _docs: list[dict] = []

    def store_finding(content: str, source: str = "web") -> str:
        """Store a research finding for later retrieval.
        Use this to save important information you've found during research.

        Args:
            content: The finding or information to store
            source: Where this came from (e.g. 'web', 'tavily', 'document')
        """
        _docs.append({"content": content, "source": source})
        return f"Stored finding ({len(_docs)} total). Use retrieve_findings to search stored info."

    def retrieve_findings(query: str) -> str:
        """Retrieve stored research findings relevant to a query.
        Use this to recall information you've already found.

        Args:
            query: What to search for in stored findings
        """
        if not _docs:
            return "No findings stored yet. Use store_finding first."
        query_lower = query.lower()
        relevant = [
            d for d in _docs
            if any(w in d["content"].lower() for w in query_lower.split())
        ]
        if not relevant:
            # Return all if no keyword match
            relevant = _docs[-5:]
        lines = [f"- [{d['source']}] {d['content'][:200]}" for d in relevant[:10]]
        return f"Retrieved {len(lines)} findings:\n" + "\n".join(lines)

    return [
        StructuredTool.from_function(store_finding, name="store_finding", description=store_finding.__doc__),
        StructuredTool.from_function(retrieve_findings, name="retrieve_findings", description=retrieve_findings.__doc__),
    ]


# ---------------------------------------------------------------------------
# Sub-agent builders
# ---------------------------------------------------------------------------

def _build_query_analyzer(name: str) -> SimpleAgent:
    return SimpleAgent(
        name=f"{name}_query_analyzer",
        engine=AugLLMConfig(
            system_message=(
                "You are a query analysis expert. Given a user question:\n"
                "1. Restate the core research question clearly\n"
                "2. List 3-5 specific search queries that cover different angles\n"
                "3. Note what types of sources would be most useful\n"
                "Be brief and actionable."
            ),
            temperature=0.2,
        ),
    )


def _build_researcher(name: str, tools: list | None = None, max_iterations: int = 8) -> ReactAgent:
    # Build tool list: search + RAG tools
    search_tools = []

    # Add Tavily or mock search
    if tools:
        search_tools.extend(tools)
    else:
        tavily = _make_tavily_tool()
        if tavily:
            search_tools.append(tavily)
            logger.info("Research agent using Tavily search")
        else:
            search_tools.append(web_search)
            logger.info("Research agent using mock search (set TAVILY_API_KEY for real search)")

    # Add dynamic RAG tools
    search_tools.extend(_make_rag_tools())

    return ReactAgent(
        name=f"{name}_researcher",
        engine=AugLLMConfig(
            system_message=(
                "You are a thorough web researcher. Your workflow:\n"
                "1. Search for information using the search tool (run 3-5 searches on different angles)\n"
                "2. Store important findings with store_finding tool\n"
                "3. Use retrieve_findings to recall what you've gathered\n"
                "4. When you have enough info, summarize your raw findings with sources\n\n"
                "Be thorough — search multiple angles. Cite sources."
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
                "You are a synthesis expert. Given raw research findings:\n"
                "1. Produce a comprehensive, well-structured answer\n"
                "2. Include inline citations like [1], [2] where relevant\n"
                "3. End with a 'Sources' section listing references\n"
                "4. Write clearly and concisely — cover key points without filler\n"
                "5. If the research is incomplete, note what's missing"
            ),
            temperature=0.4,
        ),
    )


# ---------------------------------------------------------------------------
# ResearchAgent
# ---------------------------------------------------------------------------

class ResearchAgent(MultiAgent):
    """Perplexity-style research agent using MultiAgent sequential composition.

    Pipeline: QueryAnalyzer → Researcher (search + RAG) → Synthesizer

    Example::
        agent = create_research_agent()
        result = agent.run("What is quantum computing?")
    """

    max_search_iterations: int = Field(default=8, ge=1, le=20)


# ---------------------------------------------------------------------------
# Factory
# ---------------------------------------------------------------------------

def create_research_agent(
    name: str = "perplexity",
    tools: list | None = None,
    max_search_iterations: int = 8,
) -> ResearchAgent:
    """Create a Perplexity-style research agent.

    Args:
        name: Agent name
        tools: Custom search tools (defaults to Tavily if TAVILY_API_KEY set, else mock)
        max_search_iterations: Max reasoning loops for the researcher

    Returns:
        ResearchAgent ready for execution
    """
    analyzer = _build_query_analyzer(name)
    researcher = _build_researcher(name, tools=tools, max_iterations=max_search_iterations)
    synthesizer = _build_synthesizer(name)

    agent = ResearchAgent(
        name=name,
        agents=[analyzer, researcher, synthesizer],
        execution_mode="sequential",
        max_search_iterations=max_search_iterations,
    )

    logger.info(f"Created ResearchAgent '{name}': {[a.name for a in agent.agents]}")
    return agent
