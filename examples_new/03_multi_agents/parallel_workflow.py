#!/usr/bin/env python3
"""Parallel Multi-Agent Workflow Example.

Demonstrates parallel agent execution with aggregation for comprehensive
analysis from multiple perspectives simultaneously.

Date: August 7, 2025
"""

import asyncio
import logging
import os
import time
from typing import Any

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
class MarketAnalysis(BaseModel):
    """Market analysis results."""

    market_size: str = Field(description="Current market size")
    growth_rate: float = Field(description="Annual growth rate percentage")
    key_players: list[str] = Field(description="Major market players")
    opportunities: list[str] = Field(description="Market opportunities")
    market_score: float = Field(ge=0.0, le=10.0)


class TechnicalAnalysis(BaseModel):
    """Technical feasibility analysis."""

    feasibility_score: float = Field(ge=0.0, le=10.0)
    implementation_time: str = Field(description="Estimated implementation time")
    technical_challenges: list[str] = Field(description="Key technical challenges")
    required_resources: list[str] = Field(description="Required technical resources")
    innovation_level: str = Field(description="Level of innovation required")


class FinancialAnalysis(BaseModel):
    """Financial analysis results."""

    initial_investment: str = Field(description="Required initial investment")
    roi_timeline: str = Field(description="Expected ROI timeline")
    revenue_potential: str = Field(description="Revenue potential")
    cost_breakdown: dict[str, str] = Field(description="Major cost categories")
    financial_score: float = Field(ge=0.0, le=10.0)


class RiskAnalysis(BaseModel):
    """Risk assessment results."""

    risk_level: str = Field(description="Overall risk level")
    major_risks: list[str] = Field(description="Major identified risks")
    mitigation_strategies: list[str] = Field(description="Risk mitigation strategies")
    compliance_issues: list[str] = Field(description="Compliance considerations")
    risk_score: float = Field(ge=0.0, le=10.0)


class ComprehensiveReport(BaseModel):
    """Aggregated analysis report."""

    executive_summary: str = Field(description="Executive summary")
    overall_recommendation: str = Field(description="Go/No-go recommendation")
    combined_score: float = Field(ge=0.0, le=10.0)
    key_highlights: list[str] = Field(description="Key highlights from all analyses")
    action_items: list[str] = Field(description="Recommended action items")
    timeline: str = Field(description="Recommended implementation timeline")


# Tools for different analyses
@tool
def market_research_tool(query: str) -> str:
    """Access market research data."""
    return f"Market data for '{query}': Size $5.2B, CAGR 22%, Leaders: TechCorp, DataCo, AIFlow"


@tool
def technical_specs_tool(requirement: str) -> str:
    """Check technical specifications and requirements."""
    return f"Technical analysis for '{requirement}': Feasible with cloud infrastructure, 6-month timeline"


@tool
def financial_calculator(calculation: str) -> str:
    """Perform financial calculations."""
    return "Financial calculation: Initial cost $2.5M, Break-even 18 months, 5-year NPV $12M"


@tool
def risk_database(category: str) -> str:
    """Query risk assessment database."""
    return f"Risk assessment for '{category}': Medium risk, 3 major factors, compliance required"


async def run_parallel_analysis(project: str, agents: dict[str, Any]) -> dict[str, Any]:
    """Run all analysis agents in parallel."""
    start_time = time.time()

    # Create tasks for parallel execution
    tasks = {
        name: agent.arun(
            {
                "messages": [
                    HumanMessage(content=f"Analyze '{project}' from your perspective")
                ]
            }
        )
        for name, agent in agents.items()
    }

    # Execute all analyses in parallel
    print(f"\n🚀 Running {len(tasks)} analyses in parallel...")
    results = await asyncio.gather(*tasks.values())

    # Map results back to agent names
    named_results = dict(zip(tasks.keys(), results, strict=False))

    elapsed = time.time() - start_time
    print(f"✅ All analyses completed in {elapsed:.2f} seconds")

    return named_results


async def main():
    """Run parallel workflow example."""
    print("🔄 Parallel Multi-Agent Workflow Example")
    print("=" * 60)
    print("\nScenario: Comprehensive business analysis with 4 parallel agents")
    print("All agents analyze simultaneously, then results are aggregated\n")

    # Create specialized analysis agents

    # Market Analyst
    market_analyst = ReactAgent(
        name="market_analyst",
        engine=AugLLMConfig(
            temperature=0.3,
            system_message="You are a market analyst. Analyze market opportunities and competition.",
            structured_output_model=MarketAnalysis,
        ),
        tools=[market_research_tool],
    )

    # Technical Analyst
    tech_analyst = ReactAgent(
        name="technical_analyst",
        engine=AugLLMConfig(
            temperature=0.2,
            system_message="You are a technical analyst. Assess technical feasibility and requirements.",
            structured_output_model=TechnicalAnalysis,
        ),
        tools=[technical_specs_tool],
    )

    # Financial Analyst
    financial_analyst = ReactAgent(
        name="financial_analyst",
        engine=AugLLMConfig(
            temperature=0.2,
            system_message="You are a financial analyst. Evaluate financial viability and ROI.",
            structured_output_model=FinancialAnalysis,
        ),
        tools=[financial_calculator],
    )

    # Risk Analyst
    risk_analyst = ReactAgent(
        name="risk_analyst",
        engine=AugLLMConfig(
            temperature=0.4,
            system_message="You are a risk analyst. Identify and assess potential risks.",
            structured_output_model=RiskAnalysis,
        ),
        tools=[risk_database],
    )

    # Aggregator Agent
    aggregator = SimpleAgentV3(
        name="report_aggregator",
        engine=AugLLMConfig(
            temperature=0.5,
            system_message="You aggregate multiple analyses into comprehensive reports with actionable recommendations.",
            structured_output_model=ComprehensiveReport,
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                ("human", "Create a comprehensive report based on:\n\n{analyses}"),
            ]
        ),
    )

    # Project to analyze
    project = "AI-powered customer service platform for enterprise clients"

    print(f"📋 Project: {project}")
    print("=" * 60)

    # Run parallel analyses
    analysts = {
        "market": market_analyst,
        "technical": tech_analyst,
        "financial": financial_analyst,
        "risk": risk_analyst,
    }

    results = await run_parallel_analysis(project, analysts)

    # Display individual results
    print("\n📊 Individual Analysis Results:")
    print("-" * 60)

    # Market Analysis
    market = results["market"]
    print(f"\n1️⃣ Market Analysis (Score: {market.market_score}/10)")
    print(f"   Market Size: {market.market_size}")
    print(f"   Growth Rate: {market.growth_rate}%")
    print(f"   Key Players: {', '.join(market.key_players[:3])}")
    print(
        f"   Top Opportunity: {market.opportunities[0] if market.opportunities else 'N/A'}"
    )

    # Technical Analysis
    tech = results["technical"]
    print(f"\n2️⃣ Technical Analysis (Score: {tech.feasibility_score}/10)")
    print(f"   Implementation Time: {tech.implementation_time}")
    print(f"   Innovation Level: {tech.innovation_level}")
    print(
        f"   Main Challenge: {tech.technical_challenges[0] if tech.technical_challenges else 'N/A'}"
    )
    print(
        f"   Key Resource: {tech.required_resources[0] if tech.required_resources else 'N/A'}"
    )

    # Financial Analysis
    financial = results["financial"]
    print(f"\n3️⃣ Financial Analysis (Score: {financial.financial_score}/10)")
    print(f"   Initial Investment: {financial.initial_investment}")
    print(f"   ROI Timeline: {financial.roi_timeline}")
    print(f"   Revenue Potential: {financial.revenue_potential}")
    print(
        f"   Major Cost: {list(financial.cost_breakdown.items())[0] if financial.cost_breakdown else 'N/A'}"
    )

    # Risk Analysis
    risk = results["risk"]
    print(f"\n4️⃣ Risk Analysis (Score: {risk.risk_score}/10)")
    print(f"   Risk Level: {risk.risk_level}")
    print(f"   Major Risk: {risk.major_risks[0] if risk.major_risks else 'N/A'}")
    print(
        f"   Mitigation: {risk.mitigation_strategies[0] if risk.mitigation_strategies else 'N/A'}"
    )
    print(f"   Compliance: {len(risk.compliance_issues)} issues identified")

    # Aggregate results
    print("\n" + "=" * 60)
    print("📑 Aggregating Results...")
    print("=" * 60)

    # Prepare summary for aggregator
    analyses_summary = f"""
Market Analysis:
- Market Size: {market.market_size}
- Growth Rate: {market.growth_rate}%
- Score: {market.market_score}/10
- Key Opportunity: {market.opportunities[0] if market.opportunities else 'None'}

Technical Analysis:
- Feasibility Score: {tech.feasibility_score}/10
- Implementation Time: {tech.implementation_time}
- Innovation Required: {tech.innovation_level}
- Main Challenge: {tech.technical_challenges[0] if tech.technical_challenges else 'None'}

Financial Analysis:
- Initial Investment: {financial.initial_investment}
- ROI Timeline: {financial.roi_timeline}
- Revenue Potential: {financial.revenue_potential}
- Score: {financial.financial_score}/10

Risk Analysis:
- Risk Level: {risk.risk_level}
- Risk Score: {risk.risk_score}/10
- Major Risk: {risk.major_risks[0] if risk.major_risks else 'None'}
- Key Mitigation: {risk.mitigation_strategies[0] if risk.mitigation_strategies else 'None'}
"""

    # Generate comprehensive report
    report = await aggregator.arun({"analyses": analyses_summary})

    print("\n✅ Comprehensive Report Generated:")
    print(f"   Recommendation: {report.overall_recommendation}")
    print(f"   Combined Score: {report.combined_score}/10")
    print(f"   Timeline: {report.timeline}")
    print("\n   Executive Summary:")
    print(f"   {report.executive_summary[:200]}...")
    print("\n   Key Highlights:")
    for highlight in report.key_highlights[:3]:
        print(f"   • {highlight}")
    print("\n   Action Items:")
    for i, action in enumerate(report.action_items[:3], 1):
        print(f"   {i}. {action}")

    # Summary visualization
    print("\n" + "=" * 60)
    print("🎯 Workflow Visualization:")
    print("=" * 60)

    print("\n         Project Analysis Request")
    print("                    |")
    print("    +---------------+---------------+")
    print("    |               |               |")
    print("    ↓               ↓               ↓               ↓")
    print(" Market         Technical       Financial        Risk")
    print(" Analysis       Analysis        Analysis       Analysis")
    print(
        f" ({market.market_score}/10)        ({tech.feasibility_score}/10)         ({financial.financial_score}/10)        ({risk.risk_score}/10)"
    )
    print("    |               |               |               |")
    print("    +---------------+---------------+")
    print("                    |")
    print("                    ↓")
    print("            Report Aggregator")
    print(f"         (Combined: {report.combined_score}/10)")
    print("                    |")
    print("                    ↓")
    print(f"          {report.overall_recommendation}")

    print("\n💡 Key Benefits Demonstrated:")
    print("1. Parallel execution reduces total time")
    print("2. Multiple perspectives analyzed simultaneously")
    print("3. Structured outputs from each specialist")
    print("4. Intelligent aggregation of findings")
    print("5. Clear decision support with scores")

    # Performance stats
    avg_score = (
        market.market_score
        + tech.feasibility_score
        + financial.financial_score
        + risk.risk_score
    ) / 4
    print("\n📈 Performance Summary:")
    print(f"   Average Individual Score: {avg_score:.1f}/10")
    print(f"   Combined Score: {report.combined_score}/10")
    print("   Analyses Run in Parallel: 4")
    print("   Time Saved vs Sequential: ~75%")


if __name__ == "__main__":
    asyncio.run(main())
