#!/usr/bin/env python3
"""ReactAgent → StructuredOutputAgent Sequential Pattern

This demonstrates the CORRECT way to use ReactAgentV4 with structured output:
1. ReactAgentV4 does reasoning and tool usage (NO structured output)
2. StructuredOutputAgent takes ReactAgent's output and formats it with structured model
3. No recursion loops because ReactAgent doesn't handle structured output internally

This fixes the recursion issue by separating concerns properly.

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
from haive.agents.structured.agent import StructuredOutputAgent


# Define structured output model
class ResearchAnalysis(BaseModel):
    """Structured research analysis output."""

    topic: str = Field(description="Research topic")
    key_findings: List[str] = Field(description="Main findings from research")
    evidence: List[str] = Field(description="Supporting evidence")
    confidence_score: float = Field(
        ge=0.0, le=1.0, description="Confidence in analysis"
    )
    recommendations: List[str] = Field(description="Action recommendations")
    summary: str = Field(description="Brief summary of analysis")


# Research tools for ReactAgent
@tool
def web_search(query: str) -> str:
    """Search for information on a topic."""
    # Mock web search results
    results = {
        "AI trends": "Recent AI trends include: 1) Increased enterprise adoption of LLMs, 2) Focus on AI safety and alignment, 3) Multimodal AI systems, 4) Edge AI deployment",
        "market analysis": "Current market shows: 1) 45% growth in AI services, 2) $50B market size, 3) Major players: OpenAI, Google, Microsoft, 4) Key sectors: healthcare, finance, retail",
        "technology": "Latest tech developments: 1) GPT-4 and Claude-3 models, 2) RAG systems, 3) Agent frameworks, 4) Automated reasoning systems",
    }

    for topic, info in results.items():
        if topic.lower() in query.lower():
            return f"Search results for '{query}': {info}"

    return f"Search results for '{query}': General information about emerging technologies and market trends."


@tool
def analyze_data(data_description: str) -> str:
    """Analyze data patterns and extract insights."""
    return f"Data analysis of '{data_description}' shows: Strong positive trends, 85% confidence level, key patterns in user adoption and market growth."


@tool
def fact_check(statement: str) -> str:
    """Verify facts and provide accuracy assessment."""
    return f"Fact-checking '{statement}': Verified as accurate based on recent industry reports and market data. Confidence: 90%"


async def main():
    """Demonstrate ReactAgent → StructuredOutputAgent sequential workflow."""

    print("🔬 ReactAgent → StructuredOutputAgent Sequential Pattern")
    print("=" * 60)

    # 1. Create ReactAgentV4 with tools (NO structured output)
    print("Creating ReactAgentV4 with research tools...")
    react_agent = ReactAgentV4(
        name="researcher",
        engine=AugLLMConfig(
            temperature=0.7,
            system_message="You are a research analyst. Use tools to gather information and provide detailed analysis.",
            # NO structured_output_model here - this prevents the loop!
        ),
        tools=[web_search, analyze_data, fact_check],
        debug=True,
    )

    # 2. Create StructuredOutputAgent to format the results
    print("Creating StructuredOutputAgent for formatting...")
    structured_agent = StructuredOutputAgent(
        name="formatter",
        structured_output_model=ResearchAnalysis,  # Use structured_output_model, not output_model
        custom_context="Extract and structure the research findings into a comprehensive analysis",
        engine=AugLLMConfig(temperature=0.3),  # Lower temp for consistent structuring
    )

    # 3. Create sequential workflow
    print("Creating sequential workflow...")
    workflow = EnhancedMultiAgentV4(
        name="research_workflow",
        agents=[react_agent, structured_agent],
        execution_mode="sequential",
    )

    # 4. Execute the workflow
    research_query = "Analyze the current state of AI adoption in enterprise environments, focusing on trends, challenges, and future opportunities."

    print(f"\n📋 Research Query:")
    print(f"{research_query}")
    print("\n" + "=" * 60)
    print("🚀 EXECUTING SEQUENTIAL WORKFLOW")
    print("=" * 60)

    try:
        result = await workflow.arun(
            {"messages": [HumanMessage(content=research_query)]}
        )

        print("\n✅ WORKFLOW COMPLETED SUCCESSFULLY!")
        print("=" * 60)

        # Show the results
        print("\n🔍 REACT AGENT OUTPUT:")
        if hasattr(result, "researcher"):
            researcher_output = result.researcher
            print(f"Raw research content: {str(researcher_output)[:200]}...")
        else:
            print("❌ No researcher output found")

        print("\n📊 STRUCTURED OUTPUT:")
        if hasattr(result, "formatter"):
            analysis = result.formatter
            print(f"✅ Successfully structured into ResearchAnalysis!")
            print(f"Topic: {analysis.topic}")
            print(f"Key Findings ({len(analysis.key_findings)}):")
            for i, finding in enumerate(analysis.key_findings, 1):
                print(f"  {i}. {finding}")

            print(f"\nEvidence ({len(analysis.evidence)}):")
            for i, evidence in enumerate(analysis.evidence, 1):
                print(f"  {i}. {evidence}")

            print(f"\nConfidence Score: {analysis.confidence_score:.2f}")
            print(f"Summary: {analysis.summary}")

            print(f"\nRecommendations ({len(analysis.recommendations)}):")
            for i, rec in enumerate(analysis.recommendations, 1):
                print(f"  {i}. {rec}")
        else:
            print("❌ No structured formatter output found")

        # Show the pattern benefits
        print("\n" + "=" * 60)
        print("🎯 PATTERN BENEFITS DEMONSTRATED")
        print("=" * 60)
        print("✅ ReactAgentV4 used tools for research (no recursion loop)")
        print("✅ StructuredOutputAgent converted output to Pydantic model")
        print("✅ Sequential execution with proper data flow")
        print("✅ Type-safe structured output without validation errors")
        print("✅ Clean separation of reasoning vs formatting concerns")

    except Exception as e:
        print(f"\n❌ WORKFLOW FAILED: {type(e).__name__}: {e}")
        import traceback

        traceback.print_exc()

        print(f"\n💡 If this still fails, the issue might be:")
        print(f"1. ValidationNodeConfigV2 routing logic")
        print(f"2. EnhancedMultiAgentV4 state transfer")
        print(f"3. Tool route configuration")


if __name__ == "__main__":
    print("ReactAgent → StructuredOutputAgent Sequential Pattern")
    print("=" * 50 + "\n")
    asyncio.run(main())
