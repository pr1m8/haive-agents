#!/usr/bin/env python3
"""Demonstrate the working approaches for structured output handling.

Shows real outputs and practical recommendations.

Date: August 7, 2025
"""

import asyncio
import os

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field

from haive.agents.base.structured_output_handler import (
    StructuredOutputHandler,
    extract_structured_output,
)
from haive.agents.simple.agent_v3 import SimpleAgentV3


# Our structured output model
class AnalysisResult(BaseModel):
    """Analysis result with structured fields."""

    topic: str = Field(description="Topic being analyzed")
    findings: list[str] = Field(description="Key findings (2-3 items)")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence score")
    recommendation: str = Field(description="Main recommendation")


async def demo_approach_1():
    """APPROACH 1: Simple Direct Access."""
    print("\n" + "=" * 60)
    print("APPROACH 1: Simple Direct Access")
    print("=" * 60)
    print("Code: result.get('analysis_result')")
    print("-" * 60)

    # Create and run agent
    agent = SimpleAgentV3(
        name="simple_agent",
        engine=AugLLMConfig(temperature=0.1),
        structured_output_model=AnalysisResult,
    )

    result = await agent.arun(
        {"messages": [HumanMessage(content="Analyze cloud computing benefits")]}
    )

    # Extract directly
    analysis = result.get("analysis_result")

    print(f"✅ Result type: {type(result).__name__}")
    print(f"✅ Keys in result: {list(result.keys())}")
    print(f"✅ Extracted type: {type(analysis).__name__ if analysis else 'None'}")

    if analysis:
        print("\n📊 Analysis Content:")
        print(f"  Topic: {analysis.topic}")
        print(f"  Confidence: {analysis.confidence:.2%}")
        print("  Findings:")
        for i, finding in enumerate(analysis.findings, 1):
            print(f"    {i}. {finding[:70]}...")
        print(f"  Recommendation: {analysis.recommendation[:80]}...")

    print("\n✅ Best for: Quick scripts, prototypes")
    print("⚠️  Limitation: No error handling, hardcoded field name")


async def demo_approach_2():
    """APPROACH 2: StructuredOutputHandler."""
    print("\n" + "=" * 60)
    print("APPROACH 2: StructuredOutputHandler (Recommended)")
    print("=" * 60)
    print("Code: handler = StructuredOutputHandler(AnalysisResult)")
    print("      analysis = handler.extract(result)")
    print("-" * 60)

    # Create and run agent
    agent = SimpleAgentV3(
        name="handler_agent",
        engine=AugLLMConfig(temperature=0.1),
        structured_output_model=AnalysisResult,
    )

    result = await agent.arun(
        {
            "messages": [
                HumanMessage(content="Analyze machine learning impact on business")
            ]
        }
    )

    # Use handler
    handler = StructuredOutputHandler(AnalysisResult)
    analysis = handler.extract(result)

    print(f"✅ Handler searches these fields: {handler.expected_fields[:4]}...")
    print(f"✅ Extraction successful: {analysis is not None}")

    if analysis:
        print("\n📊 Analysis Content:")
        print(f"  Topic: {analysis.topic}")
        print(f"  Confidence: {analysis.confidence:.2%}")
        print(f"  Total findings: {len(analysis.findings)}")

    # Show robustness
    print("\n🧪 Robustness Test:")
    test_results = {
        "wrong_key": {"data": analysis},
        "analysis_result": analysis,
        "output": analysis,
    }

    for key, test_result in test_results.items():
        found = handler.extract(test_result)
        print(f"  Field '{key}': {'✅ Found' if found else '❌ Not found'}")

    print("\n✅ Best for: Production code, libraries, reusable components")
    print("✅ Benefits: Multiple fallbacks, error handling, flexible")


async def demo_approach_3():
    """APPROACH 3: Convenience Function."""
    print("\n" + "=" * 60)
    print("APPROACH 3: Convenience Function")
    print("=" * 60)
    print("Code: analysis = extract_structured_output(result, AnalysisResult)")
    print("-" * 60)

    # Create and run agent
    agent = SimpleAgentV3(
        name="convenience_agent",
        engine=AugLLMConfig(temperature=0.1),
        structured_output_model=AnalysisResult,
    )

    result = await agent.arun(
        {"messages": [HumanMessage(content="Analyze renewable energy future")]}
    )

    # One-line extraction
    analysis = extract_structured_output(result, AnalysisResult)

    print(f"✅ One-line extraction: {analysis is not None}")

    if analysis:
        print("\n📊 Quick Access:")
        print(f"  {analysis.topic}")
        print(f"  {analysis.confidence:.0%} confidence")
        print(f"  {len(analysis.findings)} key findings")

    print("\n✅ Best for: Simple scripts, quick analysis")
    print("✅ Benefits: Clean, minimal code")


async def show_recommendation():
    """Show the overall recommendation."""
    print("\n" + "=" * 60)
    print("🎯 RECOMMENDATION: Use StructuredOutputHandler")
    print("=" * 60)

    print(
        """
For most use cases, we recommend using the StructuredOutputHandler:

```python
from haive.agents.base.structured_output_handler import StructuredOutputHandler

# Create handler once
handler = StructuredOutputHandler(YourOutputModel)

# Use it everywhere
result = await agent.arun(input)
output = handler.extract(result)  # or extract_or_raise(result)
```

Why?
✅ Robust - handles multiple field naming patterns
✅ Clear errors - tells you what went wrong
✅ Reusable - create once, use many times
✅ Type-safe - works with any Pydantic model
✅ Flexible - optional or required extraction

The AddableValuesDict is LangGraph's way of managing state across
graph nodes. Your structured output is safely nested inside, and
the handler makes it easy to extract.
"""
    )


async def main():
    """Run all demos."""
    os.environ["HAIVE_LOG_LEVEL"] = "ERROR"

    print("🔧 STRUCTURED OUTPUT HANDLING - Working Approaches")
    print("=" * 60)
    print("Demonstrating practical ways to handle LangGraph's")
    print("AddableValuesDict return type")

    await demo_approach_1()
    await demo_approach_2()
    await demo_approach_3()
    await show_recommendation()

    print("\n✅ All demos completed!")


if __name__ == "__main__":
    asyncio.run(main())
