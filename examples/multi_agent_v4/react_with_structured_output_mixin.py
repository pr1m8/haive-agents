#!/usr/bin/env python3
"""ReactAgent.with_structured_output() Pattern

This demonstrates using the StructuredOutputMixin pattern:
1. ReactAgent.with_structured_output() creates both agents automatically
2. Returns (react_agent, structured_agent) tuple
3. Designed for sequential multi-agent workflows

This is the cleanest pattern for ReactAgent + structured output.

Date: August 7, 2025
"""

import asyncio
from typing import List

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.react.agent_v4 import ReactAgentV4


# Define the output model
class MarketAnalysis(BaseModel):
    """Market analysis structured output."""

    market_name: str = Field(description="Name of the analyzed market")
    market_size: str = Field(description="Current market size")
    growth_rate: str = Field(description="Annual growth rate")
    key_players: List[str] = Field(description="Major companies in the market")
    opportunities: List[str] = Field(description="Growth opportunities")
    challenges: List[str] = Field(description="Market challenges")
    trends: List[str] = Field(description="Current market trends")
    forecast: str = Field(description="Future outlook")
    confidence_level: float = Field(ge=0.0, le=1.0, description="Analysis confidence")


# Analysis tools
@tool
def market_research(industry: str) -> str:
    """Research market data for an industry."""
    mock_data = {
        "AI": "AI market valued at $136B in 2024, growing 37% annually. Key players: OpenAI, Google, Microsoft, Meta. Challenges: regulation, ethics, competition.",
        "cloud": "Cloud market at $482B, 15% growth. Leaders: AWS, Azure, GCP. Trends: hybrid cloud, edge computing, serverless.",
        "fintech": "Fintech market $309B, 25% growth. Players: PayPal, Square, Stripe. Trends: embedded finance, BNPL, crypto integration.",
    }

    for key, data in mock_data.items():
        if key.lower() in industry.lower():
            return f"Market research for {industry}: {data}"

    return f"Market research for {industry}: Growing technology sector with significant investment and innovation opportunities."


@tool
def competitor_analysis(company_list: str) -> str:
    """Analyze competitors in the market."""
    return f"Competitor analysis of {company_list}: Market leaders show strong revenue growth, extensive R&D investment, and strategic partnerships. Competitive advantages include technology innovation, market reach, and customer loyalty."


@tool
def trend_analysis(sector: str) -> str:
    """Analyze current trends in a sector."""
    return f"Trend analysis for {sector}: Key trends include digital transformation, automation, sustainability focus, and customer experience optimization. Emerging technologies driving change."


async def main():
    """Demonstrate ReactAgent.with_structured_output() pattern."""

    print("🔬 ReactAgent.with_structured_output() Pattern")
    print("=" * 60)

    print("Using ReactAgentV4.with_structured_output() to create agent pair...")

    # Use the mixin to create both agents automatically
    react_agent, structured_agent = ReactAgentV4.with_structured_output(
        output_model=MarketAnalysis,
        name="market_analyzer",
        custom_context="Focus on quantitative data and market metrics",
        # ReactAgent configuration
        engine=AugLLMConfig(
            temperature=0.7,
            system_message="You are a market research analyst. Use tools to gather comprehensive market data and provide detailed analysis.",
        ),
        tools=[market_research, competitor_analysis, trend_analysis],
    )

    print(f"✅ Created ReactAgent: {react_agent.name}")
    print(f"✅ Created StructuredOutputAgent: {structured_agent.name}")

    # Create workflow with both agents
    print("\nCreating sequential workflow...")
    workflow = EnhancedMultiAgentV4(
        name="market_analysis_workflow",
        agents=[react_agent, structured_agent],
        execution_mode="sequential",
    )

    # Execute analysis
    query = "Provide a comprehensive market analysis of the artificial intelligence industry, including market size, key players, growth opportunities, and future outlook."

    print(f"\n📋 Market Analysis Query:")
    print(f"{query}")
    print("\n" + "=" * 60)
    print("🚀 EXECUTING WORKFLOW")
    print("=" * 60)

    try:
        result = await workflow.arun({"messages": [HumanMessage(content=query)]})

        print("\n✅ ANALYSIS COMPLETED!")
        print("=" * 60)

        # Show raw research output
        print(f"\n🔍 REACT AGENT RESEARCH:")
        if hasattr(result, react_agent.name):
            research_output = getattr(result, react_agent.name)
            print(f"Research findings: {str(research_output)[:200]}...")

        # Show structured analysis
        print(f"\n📊 STRUCTURED MARKET ANALYSIS:")
        if hasattr(result, structured_agent.name):
            analysis = getattr(result, structured_agent.name)
            print(f"✅ Successfully structured into MarketAnalysis!")
            print(f"Market: {analysis.market_name}")
            print(f"Size: {analysis.market_size}")
            print(f"Growth Rate: {analysis.growth_rate}")
            print(f"Confidence: {analysis.confidence_level:.2f}")

            print(f"\n🏢 Key Players ({len(analysis.key_players)}):")
            for i, player in enumerate(analysis.key_players, 1):
                print(f"  {i}. {player}")

            print(f"\n🚀 Opportunities ({len(analysis.opportunities)}):")
            for i, opp in enumerate(analysis.opportunities, 1):
                print(f"  {i}. {opp}")

            print(f"\n⚠️ Challenges ({len(analysis.challenges)}):")
            for i, challenge in enumerate(analysis.challenges, 1):
                print(f"  {i}. {challenge}")

            print(f"\n📈 Trends ({len(analysis.trends)}):")
            for i, trend in enumerate(analysis.trends, 1):
                print(f"  {i}. {trend}")

            print(f"\n🔮 Forecast:")
            print(f"  {analysis.forecast}")
        else:
            print(f"❌ No structured output found for {structured_agent.name}")

        # Show pattern advantages
        print("\n" + "=" * 60)
        print("🎯 PATTERN ADVANTAGES")
        print("=" * 60)
        print("✅ One method call creates both agents automatically")
        print("✅ Proper separation: ReactAgent does research, StructuredAgent formats")
        print("✅ No recursion loops - ReactAgent has no structured output")
        print("✅ Type-safe output with Pydantic model validation")
        print("✅ Reusable pattern for any ReactAgent + structured output need")
        print("✅ Clean API: just call .with_structured_output()")

    except Exception as e:
        print(f"\n❌ WORKFLOW FAILED: {type(e).__name__}: {e}")
        import traceback

        traceback.print_exc()

        print(f"\n💡 This pattern should work because:")
        print(f"1. ReactAgent has no structured_output_model (no parse_output loop)")
        print(f"2. StructuredOutputAgent handles all Pydantic formatting")
        print(f"3. Sequential execution with clear data flow")


if __name__ == "__main__":
    print("ReactAgent with_structured_output() Mixin Pattern")
    print("=" * 50 + "\n")
    asyncio.run(main())
