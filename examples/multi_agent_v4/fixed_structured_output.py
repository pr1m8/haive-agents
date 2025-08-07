"""Fixed Sequential Multi-Agent Example with Structured Output Version

This shows the correct pattern with structured_output_version specified.

Date: August 7, 2025
"""

import asyncio
from typing import List

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.simple.agent_v3 import SimpleAgentV3


# Define structured outputs
class AnalysisResult(BaseModel):
    """Analysis output."""

    findings: List[str] = Field(description="Key findings from analysis")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence level")
    summary: str = Field(description="Brief summary of analysis")


class FinalReport(BaseModel):
    """Final report output."""

    title: str = Field(description="Report title")
    executive_summary: str = Field(description="Executive summary")
    key_insights: List[str] = Field(description="Key insights from analysis")
    recommendations: List[str] = Field(description="Action recommendations")
    conclusion: str = Field(description="Final conclusion")


async def main():
    """Run working sequential workflow with proper structured output."""

    print("Creating agents with structured output v2...")

    # First agent - analyzer WITH structured output v2
    analyzer = SimpleAgentV3(
        name="analyzer",
        engine=AugLLMConfig(
            temperature=0.3,
            max_tokens=300,
            system_message="You are a data analyst. Analyze the input and provide structured findings.",
            structured_output_model=AnalysisResult,
            structured_output_version="v2",  # <-- SPECIFY VERSION!
        ),
        debug=False,
    )

    # Second agent - report writer WITH structured output v2
    report_writer = SimpleAgentV3(
        name="report_writer",
        engine=AugLLMConfig(
            temperature=0.5,
            max_tokens=400,
            system_message="You are a report writer. Create a comprehensive structured report from the analysis.",
            structured_output_model=FinalReport,
            structured_output_version="v2",  # <-- SPECIFY VERSION!
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                (
                    "human",
                    """Based on the previous analysis, create a comprehensive report.
            
Previous analysis findings: {analyzer.findings}
Analysis confidence: {analyzer.confidence}
Analysis summary: {analyzer.summary}

Create a detailed report with insights and recommendations.""",
                ),
            ]
        ),
        debug=False,
    )

    # Create workflow
    print("\nCreating sequential workflow...")
    workflow = EnhancedMultiAgentV4(
        name="analysis_workflow",
        agents=[analyzer, report_writer],
        execution_mode="sequential",
    )

    # Input
    query = "Analyze the growth of AI adoption in enterprises during 2024-2025, focusing on key trends, challenges, and opportunities."

    print(f"\nInput Query: {query}")
    print("\nExecuting workflow...")

    # Execute
    try:
        result = await workflow.arun({"messages": [HumanMessage(content=query)]})

        print("\n" + "=" * 60)
        print("WORKFLOW EXECUTION COMPLETE")
        print("=" * 60)

        # Show state analysis
        print("\n📊 STATE ANALYSIS:")
        print(f"Result type: {type(result).__name__}")

        # Check for analyzer structured output
        print("\n🔍 Analyzer Output:")
        if hasattr(result, "analyzer"):
            analysis = result.analyzer
            print(f"  ✅ 'analyzer' field found!")
            print(f"     Type: {type(analysis).__name__}")
            print(f"     Findings: {len(analysis.findings)} items")
            for i, finding in enumerate(analysis.findings[:3], 1):
                print(f"       {i}. {finding}")
            print(f"     Confidence: {analysis.confidence}")
            print(f"     Summary: {analysis.summary[:100]}...")
        else:
            print("  ❌ No 'analyzer' field found")

        # Check for report writer structured output
        print("\n📝 Report Writer Output:")
        if hasattr(result, "report_writer"):
            report = result.report_writer
            print(f"  ✅ 'report_writer' field found!")
            print(f"     Type: {type(report).__name__}")
            print(f"     Title: {report.title}")
            print(f"     Executive Summary: {report.executive_summary[:100]}...")
            print(f"     Key Insights: {len(report.key_insights)} items")
            for i, insight in enumerate(report.key_insights[:3], 1):
                print(f"       {i}. {insight}")
            print(f"     Recommendations: {len(report.recommendations)} items")
            for i, rec in enumerate(report.recommendations[:3], 1):
                print(f"       {i}. {rec}")
            print(f"     Conclusion: {report.conclusion[:100]}...")
        else:
            print("  ❌ No 'report_writer' field found")

        # Messages
        if hasattr(result, "messages"):
            print(f"\n📬 Messages ({len(result.messages)}):")
            for i, msg in enumerate(result.messages[-3:]):  # Last 3 messages
                sender = type(msg).__name__
                content = (
                    msg.content[:80] + "..."
                    if msg.content and len(msg.content) > 80
                    else msg.content
                )
                print(f"  [{i}] {sender}: {content}")

        # Show the pattern
        print("\n" + "=" * 60)
        print("KEY PATTERN DEMONSTRATED")
        print("=" * 60)
        print("1. Both agents use structured_output_version='v2'")
        print("2. Analyzer creates 'analyzer' field with AnalysisResult")
        print("3. Report writer can reference {analyzer.findings} in prompt")
        print("4. Report writer creates 'report_writer' field with FinalReport")
        print("5. Data flows through structured fields, not just messages!")

    except Exception as e:
        print(f"\n❌ Error: {type(e).__name__}: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    print("Fixed Multi-Agent Example with Structured Output v2")
    print("=" * 50 + "\n")
    asyncio.run(main())
