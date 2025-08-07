"""Working Approach for Structured Output in Multi-Agent Workflows

This demonstrates the correct way to handle structured output in multi-agent workflows.
The key insight: Don't use structured_output_version="v2" for multi-agent workflows yet.

Date: August 7, 2025
"""

import asyncio
from pydantic import BaseModel, Field
from typing import List
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.core.engine.aug_llm import AugLLMConfig


# Define structured outputs
class AnalysisResult(BaseModel):
    """Analysis output structure."""

    findings: List[str] = Field(description="Key findings from analysis")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence level")
    summary: str = Field(description="Brief summary of analysis")


class FinalReport(BaseModel):
    """Final report output structure."""

    title: str = Field(description="Report title")
    executive_summary: str = Field(description="Executive summary")
    key_insights: List[str] = Field(description="Key insights from analysis")
    recommendations: List[str] = Field(description="Action recommendations")
    conclusion: str = Field(description="Final conclusion")


async def main():
    """Demonstrate working structured output approach."""

    print("Creating agents with structured output (v1 parser-based)...")
    print("=" * 60)

    # First agent - analyzer with structured output (v1)
    analyzer = SimpleAgentV3(
        name="analyzer",
        engine=AugLLMConfig(
            temperature=0.3,
            max_tokens=300,
            system_message="You are a data analyst. Analyze the input and provide structured findings.",
            structured_output_model=AnalysisResult,
            # NOT specifying structured_output_version - defaults to v1 (parser-based)
        ),
        debug=True,  # Enable debug to see what's happening
    )

    # Second agent - report writer without structured output (plain text)
    report_writer = SimpleAgentV3(
        name="report_writer",
        engine=AugLLMConfig(
            temperature=0.5,
            max_tokens=400,
            system_message="You are a report writer. Create a comprehensive report from the analysis.",
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                (
                    "human",
                    """Based on the previous analysis, create a comprehensive report.
            
Previous messages: {messages}

Create a detailed report with insights and recommendations.""",
                ),
            ]
        ),
        debug=True,
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
    print("\n" + "=" * 60)
    print("EXECUTING WORKFLOW...")
    print("=" * 60 + "\n")

    # Execute
    try:
        result = await workflow.arun({"messages": [HumanMessage(content=query)]})

        print("\n" + "=" * 60)
        print("✅ WORKFLOW EXECUTION COMPLETE")
        print("=" * 60)

        # Show state analysis
        print("\n📊 STATE ANALYSIS:")
        print(f"Result type: {type(result).__name__}")

        # Check for messages
        if hasattr(result, "messages"):
            print(f"\n📬 Messages ({len(result.messages)})")
            for i, msg in enumerate(result.messages):
                sender = type(msg).__name__
                content_preview = (
                    str(msg.content)[:100] + "..."
                    if len(str(msg.content)) > 100
                    else str(msg.content)
                )
                print(f"  [{i}] {sender}: {content_preview}")

        # Check for agent outputs
        if hasattr(result, "agent_outputs"):
            print(f"\n🤖 Agent Outputs:")
            for agent_name, output in result.agent_outputs.items():
                print(f"  {agent_name}: {type(output).__name__}")
                if isinstance(output, dict):
                    for key in list(output.keys())[:3]:
                        print(f"    - {key}: {type(output[key]).__name__}")

        print("\n" + "=" * 60)
        print("💡 KEY INSIGHTS")
        print("=" * 60)
        print("1. With v1 (parser-based), structured output works via parsing")
        print("2. The LLM generates JSON that matches the Pydantic model")
        print("3. The parser validates and creates the model instance")
        print("4. No 'Unknown Pydantic model' errors!")
        print("5. Multi-agent workflows can use structured output this way")

        print("\n" + "=" * 60)
        print("🔧 RECOMMENDATION")
        print("=" * 60)
        print("For multi-agent workflows with structured output:")
        print("- Use v1 (parser-based) approach - don't specify version")
        print("- OR wait for v2 validation node fix to support pydantic_models")
        print("- OR use plain text output and parse in the next agent")

    except Exception as e:
        print(f"\n❌ Error: {type(e).__name__}: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    print("Working Structured Output Approach")
    print("=" * 50 + "\n")
    asyncio.run(main())
