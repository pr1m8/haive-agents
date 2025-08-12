#!/usr/bin/env python3
"""Test automatic structured output wrapping in enhanced base agent.

This tests the new feature where setting structured_output_model on any agent
automatically wraps it with a StructuredOutputAgent in a multi-agent workflow.

Date: August 7, 2025
"""

import asyncio

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.react.agent_v4 import ReactAgentV4


# Define structured output model
class AnalysisResult(BaseModel):
    """Analysis result with structured fields."""

    topic: str = Field(description="Topic being analyzed")
    findings: list[str] = Field(description="Key findings")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence score")
    recommendation: str = Field(description="Main recommendation")


# Simple tools
@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    try:
        result = eval(expression)
        return f"Result: {result}"
    except:
        return "Error: Invalid expression"


@tool
def analyzer(text: str) -> str:
    """Analyze text and provide insights."""
    word_count = len(text.split())
    return f"Analysis: {word_count} words, appears to be about technology and AI"


async def main():
    """Test automatic structured output wrapping."""
    print("🧪 Testing Automatic Structured Output Wrapping")
    print("=" * 60)

    # Create ReactAgent with structured_output_model set directly
    print("Creating ReactAgent with structured_output_model...")
    agent = ReactAgentV4(
        name="auto_wrapped_agent",
        engine=AugLLMConfig(
            temperature=0.7,
            system_message="You are an analytical assistant. Use tools to gather information.",
        ),
        tools=[calculator, analyzer],
        structured_output_model=AnalysisResult,  # This triggers automatic wrapping!
        verbose=True,  # Enable verbose logging
        debug=True,
    )

    print(f"✅ Agent created: {agent.name}")
    print(f"   Type: {type(agent).__name__}")
    print(f"   Has structured_output_model: {agent.structured_output_model}")
    print(
        f"   Needs wrapper: {getattr(agent, '_needs_structured_output_wrapper', False)}"
    )

    # The agent should automatically be wrapped when executed
    query = "Analyze the impact of AI on productivity. Calculate the potential 25% improvement on a baseline of 100 units."

    print(f"\n📋 Query: {query}")
    print("\n" + "=" * 60)
    print("🚀 EXECUTING AGENT")
    print("=" * 60)

    try:
        # This should work seamlessly, returning AnalysisResult
        result = await agent.arun({"messages": [HumanMessage(content=query)]})

        print("\n✅ EXECUTION COMPLETED!")
        print("=" * 60)

        print(f"Result type: {type(result).__name__}")

        # Check if we got structured output
        if isinstance(result, AnalysisResult):
            print("\n🎯 STRUCTURED OUTPUT RECEIVED!")
            print(f"Topic: {result.topic}")
            print(f"Confidence: {result.confidence:.2f}")
            print(f"Findings ({len(result.findings)}):")
            for i, finding in enumerate(result.findings, 1):
                print(f"  {i}. {finding}")
            print(f"Recommendation: {result.recommendation}")
        else:
            print(f"\n❌ Did not receive AnalysisResult, got: {type(result)}")
            print(f"Content: {result}")

        # Check the graph structure
        if hasattr(agent, "graph") and agent.graph:
            print("\n📊 Graph Structure:")
            print(
                f"   Nodes: {list(agent.graph.nodes.keys()) if hasattr(agent.graph, 'nodes') else 'N/A'}"
            )
            print(f"   Type: {type(agent.graph).__name__}")

    except Exception as e:
        print(f"\n❌ EXECUTION FAILED: {type(e).__name__}: {e}")
        import traceback

        traceback.print_exc()

        print("\n💡 Debug Info:")
        print(f"   Agent class: {agent.__class__.__name__}")
        print(
            f"   Has _needs_structured_output_wrapper: {hasattr(agent, '_needs_structured_output_wrapper')}"
        )
        print(f"   Value: {getattr(agent, '_needs_structured_output_wrapper', None)}")
        print(f"   Has graph: {hasattr(agent, 'graph')}")

    print("\n" + "=" * 60)
    print("🎯 EXPECTED BEHAVIOR")
    print("=" * 60)
    print("1. ReactAgent detects structured_output_model is set")
    print("2. Sets _needs_structured_output_wrapper = True")
    print("3. When building graph, creates multi-agent workflow:")
    print("   - ReactAgent (without structured output)")
    print("   - StructuredOutputAgent (with AnalysisResult)")
    print("4. Returns AnalysisResult instance seamlessly")


if __name__ == "__main__":
    asyncio.run(main())
