#!/usr/bin/env python3
"""Comprehensive Web Research Agent Example

This example demonstrates a sophisticated research agent that:
- Conducts multi-source research with web search capabilities
- Assesses source credibility and reliability
- Synthesizes information from multiple sources
- Produces structured, well-documented research outputs
- Handles follow-up questions and research refinement

Features:
- ReactAgent with specialized research tools
- Source credibility scoring system
- Structured research output models
- Information synthesis and fact-checking
- Citation management and source tracking"""

import asyncio
from datetime import datetime

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.react.agent import ReactAgent

# ========== STRUCTURED OUTPUT MODELS ==========


class SourceCitation(BaseModel):
    """Represents a research source with credibility assessment."""

    url: str = Field(description="Source URL")
    title: str = Field(description="Source title")
    domain: str = Field(description="Domain name (e.g., wikipedia.org)")
    credibility_score: float = Field(
        ge=0.0, le=10.0, description="Credibility score 0-10 (10 = most credible)"
    )
    publication_date: str | None = Field(
        default=None, description="Publication date if available"
    )
    author: str | None = Field(default=None, description="Author if available")
    source_type: str = Field(
        description="Type: academic, news, government, commercial, blog, wiki"
    )
    relevance_score: float = Field(
        ge=0.0, le=10.0, description="Relevance to research query (0-10)"
    )
    key_points: list[str] = Field(
        description="Key information extracted from this source"
    )


class ResearchFinding(BaseModel):
    """Individual research finding with evidence."""

    claim: str = Field(description="The finding or claim")
    evidence_strength: str = Field(description="strong, moderate, weak, conflicting")
    supporting_sources: list[str] = Field(
        description="URLs of sources supporting this finding"
    )
    contradicting_sources: list[str] = Field(
        default_factory=list, description="URLs of sources contradicting this finding"
    )
    confidence_level: float = Field(
        ge=0.0, le=1.0, description="Confidence in this finding (0.0-1.0)"
    )
    category: str = Field(description="Category: fact, opinion, statistic, trend, etc.")


class ResearchSynthesis(BaseModel):
    """Complete research synthesis with structured findings."""

    query: str = Field(description="Original research query")
    executive_summary: str = Field(
        max_length=500, description="Brief executive summary of findings"
    )
    key_findings: list[ResearchFinding] = Field(
        description="Main research findings with evidence"
    )
    sources: list[SourceCitation] = Field(
        description="All sources used with credibility assessment"
    )
    research_gaps: list[str] = Field(description="Areas needing further research")
    methodology_notes: str = Field(
        description="Notes on research approach and limitations"
    )
    timestamp: str = Field(
        default_factory=lambda: datetime.now().isoformat(),
        description="Research completion timestamp",
    )
    total_sources: int = Field(description="Total number of sources consulted")
    avg_credibility: float = Field(description="Average credibility score of sources")


# ========== RESEARCH TOOLS ==========


@tool
def web_search(query: str, num_results: int = 10) -> str:
    """Search the web for information on a given query.

    Args:
        query: Search query string
        num_results: Number of results to return (default: 10)

    Returns:
        JSON string with search results including titles, URLs, and snippets"""
    # In a real implementation, this would use an actual search API
    # like Google Custom Search, Bing Search API, or SerpAPI

    # Mock search results with varied source types for demonstration
    mock_results = [
        {
            "title": "Artificial Intelligence in Healthcare: A Comprehensive Review",
            "url": "https://www.nature.com/articles/ai-healthcare-2024",
            "snippet": "AI technologies are transforming healthcare delivery through improved diagnostics, personalized treatment plans, and operational efficiency. Recent studies show 23% improvement in diagnostic accuracy.",
            "domain": "nature.com",
            "source_type": "academic",
        },
        {
            "title": "FDA Approves New AI-Powered Diagnostic Tool",
            "url": "https://www.fda.gov/news-events/press-announcements/fda-approves-ai-diagnostic",
            "snippet": "The Food and Drug Administration today approved the first AI-powered diagnostic tool for early cancer detection, showing 95% accuracy in clinical trials.",
            "domain": "fda.gov",
            "source_type": "government",
        },
        {
            "title": "Healthcare AI Market Expected to Reach $102B by 2028",
            "url": "https://www.healthcaremarketnews.com/ai-market-forecast-2028",
            "snippet": "The global healthcare AI market is projected to grow at 44% CAGR, driven by increasing adoption of AI diagnostic tools and predictive analytics.",
            "domain": "healthcaremarketnews.com",
            "source_type": "commercial",
        },
        {
            "title": "AI in Medicine: Benefits and Challenges - Mayo Clinic",
            "url": "https://www.mayoclinic.org/healthy-living/consumer-health/ai-medicine",
            "snippet": "While AI offers significant benefits for patient care, challenges remain including data privacy, algorithm bias, and integration with existing systems.",
            "domain": "mayoclinic.org",
            "source_type": "medical",
        },
        {
            "title": "Machine Learning Algorithms Transform Radiology",
            "url": "https://pubs.rsna.org/doi/ml-radiology-transformation",
            "snippet": "Deep learning algorithms now match radiologist performance in detecting breast cancer, with some studies showing superior accuracy in mammography screening.",
            "domain": "rsna.org",
            "source_type": "academic",
        },
    ]

    import json

    return json.dumps(mock_results[:num_results])


@tool
def assess_source_credibility(url: str, domain: str, source_type: str) -> str:
    """Assess the credibility of a source based on various factors.

    Args:
        url: Source URL
        domain: Domain name
        source_type: Type of source (academic, news, government, etc.)

    Returns:
        JSON string with credibility assessment"""
    # Mock credibility assessment based on source characteristics
    # In real implementation, this might check domain authority,
    # publication reputation, author credentials, etc.

    credibility_scores = {
        "academic": {"base": 8.5, "variance": 1.0},
        "government": {"base": 9.0, "variance": 0.5},
        "medical": {"base": 8.8, "variance": 0.7},
        "news": {"base": 7.0, "variance": 2.0},
        "commercial": {"base": 6.0, "variance": 1.5},
        "blog": {"base": 4.0, "variance": 2.0},
        "wiki": {"base": 6.5, "variance": 1.0},
    }

    base_score = credibility_scores.get(source_type, {"base": 5.0, "variance": 2.0})

    # Adjust based on domain reputation (mock logic)
    domain_bonuses = {
        "nature.com": 1.0,
        "nejm.org": 1.0,
        "fda.gov": 0.8,
        "who.int": 0.8,
        "mayoclinic.org": 0.7,
        "harvard.edu": 0.9,
        "stanford.edu": 0.9,
    }

    score = base_score["base"] + domain_bonuses.get(domain, 0.0)
    score = min(10.0, max(0.0, score))  # Clamp to 0-10 range

    assessment = {
        "credibility_score": round(score, 1),
        "factors": {
            "domain_authority": domain_bonuses.get(domain, 0.0) > 0,
            "source_type": source_type,
            "https_secure": url.startswith("https://"),
            "recent_publication": True,  # Mock - would check actual date
        },
        "trust_indicators": [],
    }

    if score >= 8.0:
        assessment["trust_indicators"].append("High authority domain")
    if source_type in ["academic", "government", "medical"]:
        assessment["trust_indicators"].append("Authoritative source type")
    if url.startswith("https://"):
        assessment["trust_indicators"].append("Secure connection")

    import json

    return json.dumps(assessment)


@tool
def extract_key_information(url: str, content_snippet: str, query: str) -> str:
    """Extract key information relevant to the research query from content.

    Args:
        url: Source URL
        content_snippet: Content snippet or summary
        query: Original research query

    Returns:
        JSON string with extracted key points and relevance score"""
    # Mock information extraction
    # In real implementation, this might use NLP techniques,
    # summarization models, or content analysis APIs

    key_points = []
    relevance_score = 8.5

    # Simple keyword-based extraction (mock)
    if "AI" in content_snippet or "artificial intelligence" in content_snippet.lower():
        key_points.append("Discusses AI applications and capabilities")
    if "diagnostic" in content_snippet.lower():
        key_points.append("Covers diagnostic applications and accuracy")
    if "%" in content_snippet or "accuracy" in content_snippet.lower():
        key_points.append("Provides quantitative metrics and performance data")
    if (
        "challenge" in content_snippet.lower()
        or "limitation" in content_snippet.lower()
    ):
        key_points.append("Identifies challenges and limitations")
    if "market" in content_snippet.lower() or "$" in content_snippet:
        key_points.append("Includes market and economic information")

    # Extract specific facts/numbers
    import re

    numbers = re.findall(r"\d+%", content_snippet)
    if numbers:
        key_points.append(f"Specific metrics: {', '.join(numbers)}")

    result = {
        "key_points": key_points,
        "relevance_score": relevance_score,
        "extracted_facts": numbers,
        "content_type": "informational",  # Could be: factual, opinion, statistical, etc.
    }

    import json

    return json.dumps(result)


@tool
def cross_reference_information(claim: str, sources_data: str) -> str:
    """Cross-reference a claim against multiple sources to assess consistency.

    Args:
        claim: The claim or finding to verify
        sources_data: JSON string containing multiple source data

    Returns:
        JSON string with cross-reference analysis"""
    # Mock cross-referencing logic
    # In real implementation, this would analyze consistency across sources,
    # detect contradictions, and assess evidence strength

    analysis = {
        "claim": claim,
        "evidence_strength": "strong",  # strong, moderate, weak, conflicting
        "supporting_count": 3,
        "contradicting_count": 0,
        "consensus_level": 0.85,
        "reliability_notes": [
            "Multiple authoritative sources confirm this finding",
            "Consistent across different source types",
            "Supported by quantitative data",
        ],
    }

    import json

    return json.dumps(analysis)


# ========== WEB RESEARCH AGENT ==========


class WebResearchAgent(ReactAgent):
    """Advanced web research agent with multi-source analysis and credibility assessment.

    This agent conducts comprehensive research by:
    1. Performing targeted web searches
    2. Assessing source credibility and reliability
    3. Extracting and synthesizing key information
    4. Cross-referencing findings across sources
    5. Producing structured research reports

    Features:
    - Multi-source information gathering
    - Automated credibility assessment
    - Information synthesis and fact-checking
    - Structured output with citations
    - Follow-up research capabilities"""

    def __init__(self, name: str = "web_researcher"):
        # Configure for research-focused prompting
        research_config = AugLLMConfig(
            temperature=0.3,  # Lower temperature for factual accuracy
            max_tokens=2000,
            structured_output_model=ResearchSynthesis,
            system_message="""You are an expert research analyst specializing in comprehensive web research and information synthesis.

Your approach:
1. THOROUGH SEARCH: Use multiple search queries to gather diverse sources
2. CREDIBILITY ASSESSMENT: Evaluate each source's reliability and authority
3. INFORMATION EXTRACTION: Extract key facts, statistics, and insights
4. SYNTHESIS: Combine information from multiple sources into coherent findings
5. CITATION: Properly attribute all information to credible sources

Research Standards:
- Prioritize authoritative sources (academic, government, medical institutions)
- Cross-reference claims across multiple sources
- Clearly distinguish facts from opinions
- Note any conflicting information or research gaps
- Provide confidence levels for findings

Always produce structured research reports with proper citations and credibility assessments.""",
        )

        # Initialize with research tools
        super().__init__(
            name=name,
            engine=research_config,
            tools=[
                web_search,
                assess_source_credibility,
                extract_key_information,
                cross_reference_information,
            ],
        )


# ========== USAGE EXAMPLES ==========


async def example_comprehensive_research():
    """Example: Comprehensive research on a complex topic."""
    print("🔬 Comprehensive Web Research Agent Example")
    print("=" * 50)

    # Create research agent
    researcher = WebResearchAgent(name="comprehensive_researcher")

    # Research query
    query = """Conduct comprehensive research on the current state of AI in healthcare,.
    focusing on diagnostic applications, regulatory approval status, and market projections. 
    Assess the credibility of all sources and provide a structured analysis."""

    print(f"Research Query: {query[:100]}...")
    print("\n🔍 Conducting research...")

    # Execute research
    research_result = await researcher.arun(query)

    print("\n📋 Research Results:")
    print("-" * 30)

    if hasattr(research_result, "executive_summary"):
        print(f"Executive Summary: {research_result.executive_summary}")
        print(f"\nKey Findings: {len(research_result.key_findings)}")
        print(f"Sources Consulted: {research_result.total_sources}")
        print(f"Average Source Credibility: {research_result.avg_credibility:.1f}/10")

        print("\n🎯 Top Findings:")
        for i, finding in enumerate(research_result.key_findings[:3], 1):
            print(f"{i}. {finding.claim}")
            print(
                f"   Evidence: {finding.evidence_strength} ({finding.confidence_level:.0%} confidence)"
            )
            print(f"   Sources: {len(finding.supporting_sources)} supporting")
    else:
        print(f"Research completed: {research_result}")


async def example_source_credibility_analysis():
    """Example: Focus on source credibility and reliability assessment."""
    print("\n🎯 Source Credibility Analysis Example")
    print("=" * 50)

    researcher = WebResearchAgent(name="credibility_analyst")

    query = """Research the safety and efficacy of a new medical treatment, paying special.
    attention to source credibility. Prioritize peer-reviewed studies, government health 
    agencies, and established medical institutions. Flag any questionable sources."""

    print("🔍 Analyzing source credibility...")

    result = await researcher.arun(query)
    print(f"Credibility analysis completed: {type(result).__name__}")


async def example_follow_up_research():
    """Example: Follow-up research based on initial findings."""
    print("\n🔄 Follow-up Research Example")
    print("=" * 50)

    researcher = WebResearchAgent(name="follow_up_researcher")

    # Initial research
    initial_query = "What are the main challenges facing AI adoption in healthcare?"
    print(f"Initial research: {initial_query}")

    await researcher.arun(initial_query)

    # Follow-up based on findings
    follow_up_query = """Based on the challenges identified, research specific solutions.
    and best practices that healthcare organizations are implementing to overcome 
    these AI adoption barriers. Focus on real-world case studies and success stories."""

    print(f"\nFollow-up research: {follow_up_query[:60]}...")

    follow_up_result = await researcher.arun(follow_up_query)
    print(f"Follow-up research completed: {type(follow_up_result).__name__}")


async def example_comparative_analysis():
    """Example: Comparative research across multiple topics."""
    print("\n⚖️ Comparative Analysis Example")
    print("=" * 50)

    researcher = WebResearchAgent(name="comparative_analyst")

    query = """Compare AI adoption rates and success factors across different healthcare.
    sectors (hospitals, diagnostics labs, pharmaceutical companies, telemedicine). 
    Analyze similarities, differences, and sector-specific challenges."""

    print("🔍 Conducting comparative analysis...")

    result = await researcher.arun(query)
    print(f"Comparative analysis completed: {type(result).__name__}")


# ========== MAIN EXECUTION ==========


async def main():
    """Run all web research agent examples."""
    print("🌐 Web Research Agent Examples")
    print("=" * 60)
    print("Demonstrating comprehensive research capabilities with")
    print("multi-source analysis and credibility assessment.")
    print()

    try:
        # Run examples
        await example_comprehensive_research()
        await example_source_credibility_analysis()
        await example_follow_up_research()
        await example_comparative_analysis()

        print("\n✅ All web research examples completed successfully!")

        print("\n🔧 Key Features Demonstrated:")
        print("- Multi-source web search and information gathering")
        print("- Automated source credibility assessment")
        print("- Information extraction and synthesis")
        print("- Cross-referencing and fact-checking")
        print("- Structured research outputs with citations")
        print("- Follow-up research capabilities")

    except Exception as e:
        print(f"\n❌ Error in web research examples: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
