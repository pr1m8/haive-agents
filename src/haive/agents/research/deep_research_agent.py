"""Deep Research Agent — advanced multi-stage research with RAG + search + analysis.

Uses multiple specialized agents composed via MultiAgent:
1. QueryPlanner (SimpleAgent) — decomposes question into sub-queries
2. WebResearcher (ReactAgent) — Tavily search + store findings
3. RAGAnalyzer (ReactAgent) — retrieves + analyzes stored findings with RAG tools
4. FactChecker (SimpleAgent) — validates consistency, flags contradictions
5. ReportWriter (SimpleAgent) — synthesizes into cited report

More thorough than perplexity_agent — designed for deep research tasks.

Usage:
    from haive.agents.research.deep_research_agent import create_deep_research_agent
    agent = create_deep_research_agent()
    result = agent.run("Compare transformer vs state space model architectures for LLMs")
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
# Shared research store (in-session document store for RAG)
# ---------------------------------------------------------------------------

class ResearchStore:
    """In-session document store for research findings."""

    def __init__(self):
        self.findings: list[dict] = []
        self.sources: list[dict] = []

    def add_finding(self, content: str, source: str = "web", query: str = "") -> int:
        self.findings.append({"content": content, "source": source, "query": query})
        return len(self.findings)

    def add_source(self, url: str, title: str = "", snippet: str = "") -> None:
        self.sources.append({"url": url, "title": title, "snippet": snippet})

    def search(self, query: str, limit: int = 10) -> list[dict]:
        q_lower = query.lower()
        scored = []
        for f in self.findings:
            score = sum(1 for w in q_lower.split() if w in f["content"].lower())
            if score > 0:
                scored.append((score, f))
        scored.sort(key=lambda x: -x[0])
        return [f for _, f in scored[:limit]] or self.findings[-limit:]

    def get_all(self) -> str:
        if not self.findings:
            return "No findings stored yet."
        lines = [f"[{i+1}] ({f['source']}) {f['content'][:200]}" for i, f in enumerate(self.findings)]
        return "\n".join(lines)


def _make_research_tools(store: ResearchStore) -> list[StructuredTool]:
    """Create tools bound to a shared research store."""

    def store_finding(content: str, source: str = "web", query: str = "") -> str:
        """Store a research finding for later analysis.

        Args:
            content: The finding or key information
            source: Where it came from (web, document, analysis)
            query: The search query that found this
        """
        n = store.add_finding(content, source, query)
        return f"Stored finding #{n}. Total: {len(store.findings)}"

    def search_findings(query: str) -> str:
        """Search stored research findings by relevance.

        Args:
            query: What to search for in stored findings
        """
        results = store.search(query)
        if not results:
            return "No relevant findings. Try storing some first."
        lines = [f"- [{r['source']}] {r['content'][:150]}" for r in results]
        return f"Found {len(lines)} relevant findings:\n" + "\n".join(lines)

    def get_all_findings() -> str:
        """Get all stored research findings."""
        return store.get_all()

    return [
        StructuredTool.from_function(store_finding, name="store_finding", description=store_finding.__doc__),
        StructuredTool.from_function(search_findings, name="search_findings", description=search_findings.__doc__),
        StructuredTool.from_function(get_all_findings, name="get_all_findings", description=get_all_findings.__doc__),
    ]


# ---------------------------------------------------------------------------
# Search tool
# ---------------------------------------------------------------------------

def _make_search_tool() -> Any:
    """Get best available search tool."""
    try:
        from langchain_community.tools.tavily_search import TavilySearchResults
        t = TavilySearchResults(max_results=5)
        AugLLMConfig(tools=[t])
        logger.info("Deep research using Tavily search")
        return t
    except Exception:
        pass

    @tool
    def web_search(query: str) -> str:
        """Search the web for information."""
        return f"[mock] Comprehensive results about: {query}"

    logger.info("Deep research using mock search (set TAVILY_API_KEY for real)")
    return web_search


# ---------------------------------------------------------------------------
# Sub-agents
# ---------------------------------------------------------------------------

def _build_planner(name: str) -> SimpleAgent:
    return SimpleAgent(
        name=f"{name}_planner",
        engine=AugLLMConfig(
            temperature=0.3,
            system_message=(
                "You are a research planning expert. Given a research question:\n"
                "1. Break it into 3-5 specific sub-questions that need answering\n"
                "2. For each, suggest what to search for\n"
                "3. Identify what comparisons or analyses are needed\n"
                "4. Note any definitions that should be clarified first\n"
                "Output a clear research plan."
            ),
        ),
    )


def _build_researcher(name: str, tools: list) -> ReactAgent:
    return ReactAgent(
        name=f"{name}_researcher",
        engine=AugLLMConfig(
            temperature=0.2,
            tools=tools,
            system_message=(
                "You are a thorough web researcher. Follow the research plan:\n"
                "1. Search each sub-question using web_search (3-5 searches minimum)\n"
                "2. Store every important finding with store_finding\n"
                "3. After searching, use search_findings to verify coverage\n"
                "4. Summarize what you found and what gaps remain\n"
                "Be systematic — cover each sub-question."
            ),
        ),
        max_iterations=10,
    )


def _build_analyzer(name: str, tools: list) -> ReactAgent:
    return ReactAgent(
        name=f"{name}_analyzer",
        engine=AugLLMConfig(
            temperature=0.2,
            tools=tools,
            system_message=(
                "You are a research analyst. Review all gathered findings:\n"
                "1. Use get_all_findings to see everything collected\n"
                "2. Use search_findings to find info on specific sub-topics\n"
                "3. Identify patterns, contradictions, and key insights\n"
                "4. Note which claims have strong vs weak evidence\n"
                "5. Produce a structured analysis with key takeaways"
            ),
        ),
        max_iterations=5,
    )


def _build_fact_checker(name: str) -> SimpleAgent:
    return SimpleAgent(
        name=f"{name}_fact_checker",
        engine=AugLLMConfig(
            temperature=0.1,
            system_message=(
                "You are a fact checker. Review the research analysis:\n"
                "1. Flag any contradictions between findings\n"
                "2. Note claims that lack sufficient evidence\n"
                "3. Rate overall confidence (high/medium/low) for each claim\n"
                "4. Suggest caveats the reader should know\n"
                "Be skeptical and thorough."
            ),
        ),
    )


def _build_writer(name: str) -> SimpleAgent:
    return SimpleAgent(
        name=f"{name}_writer",
        engine=AugLLMConfig(
            temperature=0.5,
            system_message=(
                "You are an expert report writer. Using all research and analysis:\n"
                "1. Write a comprehensive, well-structured report\n"
                "2. Use clear headings and sections\n"
                "3. Include inline citations [1], [2], etc.\n"
                "4. Add a confidence assessment section\n"
                "5. End with 'Sources' listing all references\n"
                "6. Keep it factual, clear, and well-organized"
            ),
        ),
    )


# ---------------------------------------------------------------------------
# DeepResearchAgent
# ---------------------------------------------------------------------------

class DeepResearchAgent(MultiAgent):
    """Advanced multi-stage research agent.

    Pipeline: Planner → Researcher → Analyzer → FactChecker → Writer
    """
    pass


def create_deep_research_agent(
    name: str = "deep_research",
    tools: list | None = None,
    max_search_iterations: int = 10,
    include_fact_check: bool = True,
) -> DeepResearchAgent:
    """Create a deep research agent with 5-stage pipeline.

    Args:
        name: Agent name
        tools: Custom search tools (defaults to Tavily or mock)
        max_search_iterations: Max search iterations for researcher
        include_fact_check: Include fact-checking stage

    Returns:
        DeepResearchAgent ready for execution
    """
    # Shared research store
    store = ResearchStore()
    research_tools_list = _make_research_tools(store)

    # Search tools
    search_tool = tools[0] if tools else _make_search_tool()
    researcher_tools = [search_tool] + research_tools_list
    analyzer_tools = research_tools_list  # Analyzer only needs store access

    # Build pipeline
    agents = [
        _build_planner(name),
        _build_researcher(name, researcher_tools),
        _build_analyzer(name, analyzer_tools),
    ]

    if include_fact_check:
        agents.append(_build_fact_checker(name))

    agents.append(_build_writer(name))

    agent = DeepResearchAgent(
        name=name,
        agents=agents,
        execution_mode="sequential",
    )

    logger.info(f"Created DeepResearchAgent '{name}': {[a.name for a in agent.agents]}")
    return agent
