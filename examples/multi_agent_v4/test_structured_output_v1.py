"""Test Structured Output with v1 (parser-based) approach

This tests the v1 structured output approach which uses parsers instead of tools.

Date: August 7, 2025
"""

import asyncio
from pydantic import BaseModel, Field
from typing import List
from langchain_core.messages import HumanMessage

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.core.engine.aug_llm import AugLLMConfig


# Define structured outputs
class AnalysisResult(BaseModel):
    """Analysis output."""

    findings: List[str] = Field(description="Key findings from analysis")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence level")
    summary: str = Field(description="Brief summary of analysis")


async def main():
    """Test v1 structured output."""

    print("Testing v1 (parser-based) structured output...")

    # Create agent with v1 structured output (default)
    analyzer = SimpleAgentV3(
        name="analyzer",
        engine=AugLLMConfig(
            temperature=0.3,
            max_tokens=300,
            system_message="You are a data analyst. Analyze the input and provide structured findings.",
            structured_output_model=AnalysisResult,
            # Note: NOT specifying structured_output_version, defaults to v1
        ),
        debug=False,
    )

    # Test single agent first
    print("\n1. Testing single agent with structured output...")
    result = await analyzer.arun(
        {
            "messages": [
                HumanMessage(content="Analyze the impact of AI on healthcare in 2025")
            ]
        }
    )

    print(f"\nResult type: {type(result).__name__}")
    print(
        f"Result keys: {list(result.keys()) if isinstance(result, dict) else 'Not a dict'}"
    )

    # Check if we got structured output
    if hasattr(result, "analyzer"):
        print(f"✅ Found 'analyzer' field: {type(result.analyzer).__name__}")
    else:
        print("❌ No 'analyzer' field found")

    # Now test in workflow
    print("\n\n2. Testing in multi-agent workflow...")

    # Second agent - plain text
    summarizer = SimpleAgentV3(
        name="summarizer",
        engine=AugLLMConfig(
            temperature=0.5,
            max_tokens=200,
            system_message="You are a summarizer. Create a brief summary from the analysis.",
        ),
        debug=False,
    )

    # Create workflow
    workflow = EnhancedMultiAgentV4(
        name="analysis_workflow",
        agents=[analyzer, summarizer],
        execution_mode="sequential",
    )

    # Execute workflow
    query = "Analyze the growth of renewable energy adoption in 2024-2025"
    print(f"\nQuery: {query}")

    result = await workflow.arun({"messages": [HumanMessage(content=query)]})

    print("\n" + "=" * 60)
    print("WORKFLOW RESULTS")
    print("=" * 60)

    print(f"\nResult type: {type(result).__name__}")

    # Check for structured output field
    if hasattr(result, "analyzer"):
        analysis = result.analyzer
        print(f"\n✅ Analyzer structured output found!")
        print(f"   Type: {type(analysis).__name__}")
        if hasattr(analysis, "findings"):
            print(f"   Findings: {len(analysis.findings)} items")
            for i, finding in enumerate(analysis.findings[:3], 1):
                print(f"     {i}. {finding}")
        if hasattr(analysis, "confidence"):
            print(f"   Confidence: {analysis.confidence}")
        if hasattr(analysis, "summary"):
            print(f"   Summary: {analysis.summary[:100]}...")
    else:
        print("\n❌ No 'analyzer' field in result")

    # Check messages
    if hasattr(result, "messages"):
        print(f"\n📬 Messages: {len(result.messages)} total")
        for i, msg in enumerate(result.messages[-3:]):
            print(f"  [{i}] {type(msg).__name__}: {str(msg.content)[:80]}...")

    print("\n" + "=" * 60)
    print("KEY OBSERVATION")
    print("=" * 60)
    print("With v1 (parser-based), structured output should work differently")
    print("than v2 (tool-based). Let's see what happens!")


if __name__ == "__main__":
    print("Structured Output v1 Test")
    print("=" * 50 + "\n")
    asyncio.run(main())
