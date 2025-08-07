#!/usr/bin/env python3
"""Best practices for structured output with LangGraph agents.

This example demonstrates the recommended patterns for handling
structured output when using agents with LangGraph.

Date: August 7, 2025
"""

import asyncio
import os
from typing import List, Optional

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.base.structured_output_handler import (
    StructuredOutputHandler,
    extract_structured_output,
    require_structured_output,
)
from haive.agents.react.agent_v4 import ReactAgentV4
from haive.agents.simple.agent_v3 import SimpleAgentV3


# Define various structured output models
class AnalysisResult(BaseModel):
    """Analysis result with structured fields."""

    topic: str = Field(description="Topic being analyzed")
    findings: List[str] = Field(description="Key findings")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence score")
    recommendation: str = Field(description="Main recommendation")


class DecisionOutput(BaseModel):
    """Decision making output."""

    decision: str = Field(description="The decision made")
    reasoning: str = Field(description="Reasoning behind the decision")
    alternatives: List[str] = Field(description="Alternative options considered")
    risk_level: str = Field(description="Risk level: low/medium/high")


class ProcessingResult(BaseModel):
    """Data processing result."""

    processed_count: int = Field(description="Number of items processed")
    success_rate: float = Field(description="Success rate as percentage")
    errors: List[str] = Field(default_factory=list, description="List of errors")
    summary: str = Field(description="Processing summary")


# Tool for examples
@tool
def analyzer(text: str) -> str:
    """Analyze text and provide insights."""
    return f"Analysis complete: {len(text.split())} words analyzed"


# Pattern 1: Using StructuredOutputHandler directly
async def pattern_1_handler_class():
    """Pattern 1: Using the StructuredOutputHandler class."""
    print("\n" + "=" * 60)
    print("PATTERN 1: StructuredOutputHandler Class")
    print("=" * 60)

    # Create agent
    agent = SimpleAgentV3(
        name="analyzer",
        engine=AugLLMConfig(temperature=0.1),
        structured_output_model=AnalysisResult,
    )

    # Create handler
    handler = StructuredOutputHandler(AnalysisResult)

    # Run agent
    result = await agent.arun(
        {
            "messages": [
                HumanMessage(
                    content="Analyze the impact of renewable energy on economy"
                )
            ]
        }
    )

    print(f"Raw result type: {type(result).__name__}")
    print(f"Raw result keys: {list(result.keys())}")

    # Extract with handler
    analysis = handler.extract(result)

    if analysis:
        print(f"\n✅ Extracted successfully:")
        print(f"   Topic: {analysis.topic}")
        print(f"   Confidence: {analysis.confidence:.2f}")
        print(f"   Findings: {len(analysis.findings)} items")
        print(f"   Recommendation: {analysis.recommendation}")

    # Show expected fields
    print(f"\nHandler searches these fields: {handler.expected_fields}")


# Pattern 2: Using convenience functions
async def pattern_2_convenience_functions():
    """Pattern 2: Using convenience extraction functions."""
    print("\n" + "=" * 60)
    print("PATTERN 2: Convenience Functions")
    print("=" * 60)

    # Create agent with different output model
    agent = ReactAgentV4(
        name="decision_maker",
        engine=AugLLMConfig(temperature=0.3),
        tools=[analyzer],
        structured_output_model=DecisionOutput,
    )

    # Run agent
    result = await agent.arun(
        {
            "messages": [
                HumanMessage(content="Should we invest in solar panels for the office?")
            ]
        }
    )

    # Method 1: Optional extraction
    decision = extract_structured_output(result, DecisionOutput)
    if decision:
        print(f"✅ Decision: {decision.decision}")
        print(f"   Risk Level: {decision.risk_level}")
        print(f"   Reasoning: {decision.reasoning[:100]}...")

    # Method 2: Required extraction (will raise if not found)
    try:
        decision = require_structured_output(result, DecisionOutput)
        print(f"\n✅ Required extraction succeeded")
        print(f"   Alternatives considered: {len(decision.alternatives)}")
    except ValueError as e:
        print(f"❌ Extraction failed: {e}")


# Pattern 3: Custom agent with built-in extraction
class SmartAgent(SimpleAgentV3):
    """Agent with built-in structured output extraction."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.structured_output_model:
            self._output_handler = StructuredOutputHandler(self.structured_output_model)

    async def get_structured_output(self, input_data: dict):
        """Run and return structured output directly."""
        result = await self.arun(input_data)
        if hasattr(self, "_output_handler"):
            return self._output_handler.extract_or_raise(result)
        return result


async def pattern_3_custom_agent():
    """Pattern 3: Custom agent with built-in extraction."""
    print("\n" + "=" * 60)
    print("PATTERN 3: Custom Agent with Built-in Extraction")
    print("=" * 60)

    # Create custom agent
    agent = SmartAgent(
        name="processor",
        engine=AugLLMConfig(temperature=0.1),
        structured_output_model=ProcessingResult,
    )

    # Get structured output directly
    processing = await agent.get_structured_output(
        {"messages": [HumanMessage(content="Process batch of 1000 customer records")]}
    )

    print(f"✅ Direct structured output:")
    print(f"   Type: {type(processing).__name__}")
    print(f"   Processed: {processing.processed_count} items")
    print(f"   Success Rate: {processing.success_rate:.1f}%")
    print(f"   Errors: {len(processing.errors)}")
    print(f"   Summary: {processing.summary}")


# Pattern 4: Handling multiple output types
async def pattern_4_multiple_outputs():
    """Pattern 4: Agent that can return different output types."""
    print("\n" + "=" * 60)
    print("PATTERN 4: Multiple Output Types")
    print("=" * 60)

    # First execution - Analysis
    agent1 = SimpleAgentV3(
        name="multi_output_1",
        engine=AugLLMConfig(temperature=0.1),
        structured_output_model=AnalysisResult,
    )

    result1 = await agent1.arun(
        {"messages": [HumanMessage(content="Analyze market trends")]}
    )

    # Try to extract different types
    analysis = extract_structured_output(result1, AnalysisResult)
    decision = extract_structured_output(result1, DecisionOutput)

    print(f"Analysis found: {analysis is not None}")
    print(f"Decision found: {decision is not None}")

    if analysis:
        print(f"✅ Correct type extracted: {type(analysis).__name__}")


# Pattern 5: Error handling and debugging
async def pattern_5_error_handling():
    """Pattern 5: Proper error handling and debugging."""
    print("\n" + "=" * 60)
    print("PATTERN 5: Error Handling and Debugging")
    print("=" * 60)

    agent = SimpleAgentV3(
        name="test_agent",
        engine=AugLLMConfig(temperature=0.1),
        structured_output_model=AnalysisResult,
    )

    result = await agent.arun({"messages": [HumanMessage(content="Quick test")]})

    # Create handler with custom field names
    handler = StructuredOutputHandler(
        AnalysisResult,
        common_fields=["analysis", "output", "result", "analysis_result"],
    )

    # Try extraction with detailed error info
    try:
        analysis = handler.extract_or_raise(result)
        print(f"✅ Extraction successful: {type(analysis).__name__}")
    except ValueError as e:
        print(f"❌ Extraction failed: {e}")

        # Debug information
        print(f"\nDebug info:")
        print(f"  Result type: {type(result).__name__}")
        print(
            f"  Result keys: {list(result.keys()) if hasattr(result, 'keys') else 'N/A'}"
        )

        # Manual inspection
        if hasattr(result, "items"):
            for key, value in result.items():
                print(f"  {key}: {type(value).__name__}")


# Best practice summary
async def show_best_practices():
    """Show summary of best practices."""
    print("\n" + "=" * 60)
    print("BEST PRACTICES SUMMARY")
    print("=" * 60)

    print(
        """
1. **Understand the Return Type**
   - LangGraph always returns AddableValuesDict
   - Your structured output is nested inside
   - This is by design, not a bug

2. **Use StructuredOutputHandler**
   - Provides clean extraction interface
   - Handles various field naming patterns
   - Offers both optional and required extraction

3. **Create Abstractions**
   - Build custom agent classes for repeated patterns
   - Hide the extraction complexity from users
   - Provide direct access methods

4. **Handle Errors Gracefully**
   - Always check if extraction succeeded
   - Provide meaningful error messages
   - Include debugging information

5. **Field Naming Patterns**
   - Common: 'analysis_result', 'task_result', 'output'
   - Model-based: 'AnalysisResult' → 'analysis_result'
   - Custom: Specify your own field names

6. **Performance Considerations**
   - Extract once and reuse the result
   - Don't repeatedly search the same result
   - Cache handlers for the same model type
"""
    )


async def main():
    """Run all pattern examples."""
    print("🎯 STRUCTURED OUTPUT BEST PRACTICES")
    print("=" * 60)
    print("Demonstrating recommended patterns for handling")
    print("structured output with LangGraph agents.")

    # Run all patterns
    await pattern_1_handler_class()
    await pattern_2_convenience_functions()
    await pattern_3_custom_agent()
    await pattern_4_multiple_outputs()
    await pattern_5_error_handling()
    await show_best_practices()

    print("\n✅ All examples completed!")


if __name__ == "__main__":
    # Reduce logging noise
    os.environ["HAIVE_LOG_LEVEL"] = "ERROR"
    asyncio.run(main())
