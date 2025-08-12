#!/usr/bin/env python3
"""Simple debug to understand structured output return type."""

import asyncio
import os

# Disable verbose logging
os.environ["HAIVE_LOG_LEVEL"] = "ERROR"


from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field

from haive.agents.simple.agent_v3 import SimpleAgentV3


# Define structured output model
class AnalysisResult(BaseModel):
    """Analysis result with structured fields."""

    topic: str = Field(description="Topic being analyzed")
    findings: list[str] = Field(description="Key findings")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence score")
    recommendation: str = Field(description="Main recommendation")


async def main():
    """Debug why result is AddableValuesDict."""
    print("🔍 Simple Debug - Structured Output Return Type")
    print("=" * 60)

    # Create simple agent with structured output
    agent = SimpleAgentV3(
        name="test_agent",
        engine=AugLLMConfig(
            temperature=0.1,
            system_message="Extract information into structured format.",
        ),
        structured_output_model=AnalysisResult,
        verbose=False,  # Disable verbose
        debug=False,  # Disable debug
    )

    # Check if wrapping occurred
    print(f"Agent type: {type(agent).__name__}")
    print(f"Has structured_output_model: {agent.structured_output_model is not None}")
    print(f"Needs wrapper: {getattr(agent, '_needs_structured_output_wrapper', False)}")

    # Execute
    print("\nExecuting...")
    result = await agent.arun(
        {
            "messages": [
                HumanMessage(
                    content="AI improves productivity by 25% from baseline 100 units"
                )
            ]
        }
    )

    # Analyze result
    print("\n📦 Result Analysis:")
    print(f"  Type: {type(result).__name__}")
    print(f"  Module: {type(result).__module__}")

    if hasattr(result, "__dict__"):
        print(f"  Attributes: {list(result.__dict__.keys())[:5]}...")  # First 5 attrs

    if isinstance(result, dict):
        print(f"  Keys: {list(result.keys())}")

        # Check for analysis_result field
        if "analysis_result" in result:
            analysis = result["analysis_result"]
            print("\n  Found 'analysis_result':")
            print(f"    Type: {type(analysis).__name__}")
            print(f"    Is AnalysisResult: {isinstance(analysis, AnalysisResult)}")

            if isinstance(analysis, AnalysisResult):
                print(f"    Topic: {analysis.topic}")
                print(f"    Confidence: {analysis.confidence}")

    # The key finding
    print("\n💡 Key Finding:")
    print(f"  AddableValuesDict is from: {type(result).__module__}")
    print("  This is LangGraph's standard return type")
    print("  It allows nodes to 'add' values to the state")

    # Let's trace where this happens
    print("\n🔍 Tracing the source:")

    # Check the execution method
    if hasattr(agent, "_app"):
        print(f"  Agent._app type: {type(agent._app).__name__}")
        print(f"  From module: {type(agent._app).__module__}")

    # The return happens in ExecutionMixin
    print("\n📍 The return happens in:")
    print("  1. ExecutionMixin.arun() calls compiled_graph.ainvoke()")
    print("  2. LangGraph returns AddableValuesDict")
    print("  3. This is the final state after all nodes execute")

    return result


if __name__ == "__main__":
    result = asyncio.run(main())

    print("\n" + "=" * 60)
    print("📝 CONCLUSION")
    print("=" * 60)
    print("AddableValuesDict is the expected return type from LangGraph.")
    print("It contains the full graph execution state.")
    print("Structured output is nested inside as 'analysis_result'.")
    print("\nTo get the Pydantic model:")
    print("  result['analysis_result']  # Your AnalysisResult instance")
