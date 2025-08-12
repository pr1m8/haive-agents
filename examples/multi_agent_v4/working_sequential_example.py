"""Working Sequential Multi-Agent Example.

This shows the correct pattern for sequential multi-agent workflows
with proper structured output handling.

Date: August 7, 2025
"""

import asyncio

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.simple.agent_v3 import SimpleAgentV3


# Define structured outputs
class AnalysisResult(BaseModel):
    """Analysis output."""

    findings: list[str] = Field(description="Key findings")
    confidence: float = Field(ge=0.0, le=1.0)
    summary: str = Field(description="Brief summary")


class FinalReport(BaseModel):
    """Final report output."""

    title: str = Field(description="Report title")
    executive_summary: str = Field(description="Executive summary")
    recommendations: list[str] = Field(description="Recommendations")


async def main():
    """Run working sequential workflow."""
    print("Creating agents...")

    # First agent - analyzer WITHOUT structured output initially
    # We'll let it output plain text first
    analyzer = SimpleAgentV3(
        name="analyzer",
        engine=AugLLMConfig(
            temperature=0.3,
            max_tokens=200,
            system_message="You are a data analyst. Analyze the input and provide findings.",
        ),
        debug=False,  # Turn off debug for cleaner output
    )

    # Second agent - report writer WITH structured output
    report_writer = SimpleAgentV3(
        name="report_writer",
        engine=AugLLMConfig(
            temperature=0.5,
            max_tokens=300,
            system_message="You are a report writer. Create a structured report from the analysis.",
            structured_output_model=FinalReport,  # This agent outputs structured data
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                (
                    "human",
                    "Based on the analysis, create a report. Previous messages: {messages}",
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
    query = "Analyze the growth of AI adoption in enterprises during 2024-2025."

    print(f"\nInput Query: {query}")
    print("\nExecuting workflow...")

    # Execute
    result = await workflow.arun({"messages": [HumanMessage(content=query)]})

    print("\n" + "=" * 60)
    print("WORKFLOW EXECUTION COMPLETE")
    print("=" * 60)

    # Show state analysis
    print("\n📊 STATE ANALYSIS:")
    print(f"Result type: {type(result).__name__}")

    # Messages
    if hasattr(result, "messages"):
        print(f"\n📬 Messages ({len(result.messages)}):")
        for i, msg in enumerate(result.messages):
            sender = type(msg).__name__
            content = (
                msg.content[:100] + "..." if len(msg.content) > 100 else msg.content
            )
            print(f"  [{i}] {sender}: {content}")

    # Check for structured output field
    print("\n🏗️ Structured Output Fields:")
    if hasattr(result, "report_writer"):
        report = result.report_writer
        print("  ✅ report_writer field found!")
        print(f"     Type: {type(report).__name__}")
        print(f"     Title: {report.title}")
        print(f"     Summary: {report.executive_summary[:100]}...")
        print(f"     Recommendations: {len(report.recommendations)} items")
        for i, rec in enumerate(report.recommendations[:3], 1):
            print(f"       {i}. {rec}")
    else:
        print("  ❌ No report_writer field found")

    # Agent states
    if hasattr(result, "agent_states"):
        print(f"\n🤖 Agent States: {list(result.agent_states.keys())}")

    # Execution order
    if hasattr(result, "agent_execution_order"):
        print(f"\n📋 Execution Order: {result.agent_execution_order or 'Not tracked'}")

    # Show the actual workflow
    print("\n" + "=" * 60)
    print("WORKFLOW PATTERN DEMONSTRATED")
    print("=" * 60)
    print("1. Analyzer (plain text) → Analyzes the query")
    print("2. Report Writer (structured) → Creates FinalReport object")
    print("3. State contains 'report_writer' field with typed data")
    print(
        "\n✅ This is the correct pattern for structured output in multi-agent workflows!"
    )


if __name__ == "__main__":
    print("Working Sequential Multi-Agent Example")
    print("=" * 40 + "\n")
    asyncio.run(main())
