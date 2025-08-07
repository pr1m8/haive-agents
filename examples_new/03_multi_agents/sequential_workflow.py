#!/usr/bin/env python3
"""Sequential Multi-Agent Workflow Example.

Demonstrates ReactAgent → SimpleAgent sequential flow with structured output
for a complete research-to-report workflow.

Date: August 7, 2025
"""

import asyncio
import logging
import os
from datetime import datetime
from typing import List

# Suppress debug logging
logging.getLogger().setLevel(logging.WARNING)
os.environ["HAIVE_LOG_LEVEL"] = "WARNING"

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent_v3 import SimpleAgentV3


# Structured output models
class ResearchPlan(BaseModel):
    """Research planning output."""

    topic: str = Field(description="Research topic")
    objectives: List[str] = Field(description="Research objectives")
    search_queries: List[str] = Field(description="Specific queries to investigate")
    methodology: str = Field(description="Research methodology")


class ResearchData(BaseModel):
    """Research findings."""

    key_findings: List[str] = Field(description="Key research findings")
    data_points: List[str] = Field(description="Important data points")
    sources_cited: int = Field(ge=0, description="Number of sources")
    confidence_level: float = Field(ge=0.0, le=1.0)


class AnalysisResult(BaseModel):
    """Analysis output."""

    insights: List[str] = Field(description="Key insights")
    trends: List[str] = Field(description="Identified trends")
    recommendations: List[str] = Field(description="Recommendations")
    risk_factors: List[str] = Field(description="Potential risks")


class FinalReport(BaseModel):
    """Final formatted report."""

    title: str = Field(description="Report title")
    executive_summary: str = Field(description="Executive summary")
    sections: List[str] = Field(description="Main report sections")
    conclusion: str = Field(description="Report conclusion")
    word_count: int = Field(ge=0, description="Approximate word count")


# Tools for research
@tool
def search_academic_database(query: str) -> str:
    """Search academic papers and research."""
    return f"Found 12 relevant papers on '{query}' from top journals (2022-2025)"


@tool
def analyze_market_data(topic: str) -> str:
    """Analyze market data and trends."""
    return (
        f"Market data for '{topic}': Growth rate 15%, Market size $2.3B, Key players: 8"
    )


@tool
def statistical_analysis(data: str) -> str:
    """Perform statistical analysis on data."""
    return (
        "Statistical significance: p<0.05, Correlation: 0.78, Confidence interval: 95%"
    )


async def main():
    """Run sequential workflow example."""

    print("📊 Sequential Multi-Agent Workflow Example")
    print("=" * 60)
    print("\nWorkflow: Research → Analyze → Report")
    print("Each agent builds on the previous agent's output\n")

    # Create agents for each stage

    # Stage 1: Research Planning
    planner = SimpleAgentV3(
        name="research_planner",
        engine=AugLLMConfig(
            temperature=0.3,
            system_message="You are a research strategist. Create comprehensive research plans.",
            structured_output_model=ResearchPlan,
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                ("human", "Create a research plan for: {topic}"),
            ]
        ),
    )

    # Stage 2: Data Collection
    researcher = ReactAgent(
        name="data_researcher",
        engine=AugLLMConfig(
            temperature=0.2,
            system_message="You are a thorough researcher. Collect comprehensive data based on the research plan.",
            structured_output_model=ResearchData,
        ),
        tools=[search_academic_database, analyze_market_data],
    )

    # Stage 3: Analysis
    analyst = ReactAgent(
        name="data_analyst",
        engine=AugLLMConfig(
            temperature=0.4,
            system_message="You are a data analyst. Analyze research findings and extract insights.",
            structured_output_model=AnalysisResult,
        ),
        tools=[statistical_analysis],
    )

    # Stage 4: Report Writing
    writer = SimpleAgentV3(
        name="report_writer",
        engine=AugLLMConfig(
            temperature=0.6,
            system_message="You are a professional report writer. Create executive-level reports.",
            structured_output_model=FinalReport,
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                (
                    "human",
                    "Write a report based on:\n\nTopic: {topic}\n\nFindings: {findings}\n\nAnalysis: {analysis}",
                ),
            ]
        ),
    )

    # Test topic
    topic = "AI adoption in healthcare diagnostics"

    print(f"📋 Research Topic: {topic}")
    print("=" * 60)

    # Stage 1: Create Research Plan
    print("\n1️⃣ Stage 1: Research Planning")
    print("-" * 40)

    plan = await planner.arun({"topic": topic})

    print(f"✅ Research Plan Created:")
    print(f"   Topic: {plan.topic}")
    print(f"   Objectives: {len(plan.objectives)} defined")
    for obj in plan.objectives[:2]:
        print(f"   • {obj}")
    print(f"   Search Queries: {len(plan.search_queries)} prepared")
    print(f"   Methodology: {plan.methodology[:80]}...")

    # Stage 2: Collect Data
    print("\n2️⃣ Stage 2: Data Collection")
    print("-" * 40)

    # Pass the plan to the researcher
    research_context = f"""
    Research Plan:
    - Topic: {plan.topic}
    - Objectives: {', '.join(plan.objectives)}
    - Queries: {', '.join(plan.search_queries)}
    
    Please collect comprehensive data following this plan.
    """

    data = await researcher.arun({"messages": [HumanMessage(content=research_context)]})

    print(f"✅ Data Collected:")
    print(f"   Key Findings: {len(data.key_findings)} items")
    for finding in data.key_findings[:2]:
        print(f"   • {finding[:80]}...")
    print(f"   Data Points: {len(data.data_points)} collected")
    print(f"   Sources: {data.sources_cited} cited")
    print(f"   Confidence: {data.confidence_level:.0%}")

    # Stage 3: Analyze Data
    print("\n3️⃣ Stage 3: Data Analysis")
    print("-" * 40)

    # Pass findings to analyst
    analysis_context = f"""
    Analyze the following research data:
    
    Key Findings:
    {chr(10).join(f'- {finding}' for finding in data.key_findings)}
    
    Data Points:
    {chr(10).join(f'- {point}' for point in data.data_points)}
    
    Sources: {data.sources_cited} peer-reviewed sources
    """

    analysis = await analyst.arun(
        {"messages": [HumanMessage(content=analysis_context)]}
    )

    print(f"✅ Analysis Complete:")
    print(f"   Insights: {len(analysis.insights)} discovered")
    for insight in analysis.insights[:2]:
        print(f"   • {insight[:80]}...")
    print(f"   Trends: {len(analysis.trends)} identified")
    print(f"   Recommendations: {len(analysis.recommendations)} made")
    print(f"   Risk Factors: {len(analysis.risk_factors)} identified")

    # Stage 4: Write Report
    print("\n4️⃣ Stage 4: Report Writing")
    print("-" * 40)

    # Prepare findings summary for writer
    findings_summary = "\n".join(f"- {f}" for f in data.key_findings[:3])
    analysis_summary = {
        "insights": "\n".join(f"- {i}" for i in analysis.insights[:3]),
        "recommendations": "\n".join(f"- {r}" for r in analysis.recommendations[:3]),
    }

    report = await writer.arun(
        {
            "topic": topic,
            "findings": findings_summary,
            "analysis": f"Insights:\n{analysis_summary['insights']}\n\nRecommendations:\n{analysis_summary['recommendations']}",
        }
    )

    print(f"✅ Report Generated:")
    print(f"   Title: {report.title}")
    print(f"   Executive Summary: {report.executive_summary[:150]}...")
    print(f"   Sections: {len(report.sections)} sections")
    for i, section in enumerate(report.sections[:3], 1):
        print(f"   {i}. {section[:60]}...")
    print(f"   Word Count: ~{report.word_count} words")

    # Summary
    print("\n" + "=" * 60)
    print("✅ Sequential Workflow Complete!")
    print("=" * 60)

    print("\n📊 Workflow Summary:")
    print(
        f"1. Planning: {len(plan.objectives)} objectives → {len(plan.search_queries)} queries"
    )
    print(
        f"2. Research: {data.sources_cited} sources → {len(data.key_findings)} findings"
    )
    print(
        f"3. Analysis: {len(analysis.insights)} insights → {len(analysis.recommendations)} recommendations"
    )
    print(f"4. Report: {len(report.sections)} sections → ~{report.word_count} words")

    print("\n💡 Key Benefits Demonstrated:")
    print("1. Each agent builds on previous outputs")
    print("2. Structured data flows between agents")
    print("3. Type-safe state transfer")
    print("4. Progressive refinement of information")
    print("5. Clear workflow visualization")

    # Show state transfer
    print("\n🔄 State Transfer Visualization:")
    print(f"Topic → Plan ({len(plan.search_queries)} queries)")
    print(f"      ↓")
    print(f"Plan → Research ({data.sources_cited} sources)")
    print(f"      ↓")
    print(f"Data → Analysis ({len(analysis.insights)} insights)")
    print(f"      ↓")
    print(f"Analysis → Report (~{report.word_count} words)")


if __name__ == "__main__":
    asyncio.run(main())
