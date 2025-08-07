#!/usr/bin/env python3
"""Compare different approaches for handling structured output in Haive agents.

This script tests multiple approaches and shows real outputs for comparison.

Date: August 7, 2025
"""

import asyncio
import os
import time
from typing import Any, List, Optional

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.base.structured_output_handler import StructuredOutputHandler
from haive.agents.react.agent_v4 import ReactAgentV4
from haive.agents.simple.agent_v3 import SimpleAgentV3


# Define our structured output model
class AnalysisResult(BaseModel):
    """Analysis result with structured fields."""

    topic: str = Field(description="Topic being analyzed")
    findings: List[str] = Field(description="Key findings (2-3 items)")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence score")
    recommendation: str = Field(description="Main recommendation")


# Simple tool
@tool
def word_counter(text: str) -> str:
    """Count words in text."""
    return f"Word count: {len(text.split())} words"


# ========== APPROACH 1: Direct Field Access ==========
async def approach_1_direct_access():
    """Approach 1: Direct dictionary access to structured output field."""
    print("\n" + "=" * 80)
    print("APPROACH 1: Direct Field Access")
    print("=" * 80)

    start_time = time.time()

    # Create agent
    agent = SimpleAgentV3(
        name="direct_agent",
        engine=AugLLMConfig(temperature=0.1),
        structured_output_model=AnalysisResult,
    )

    # Execute
    result = await agent.arun(
        {
            "messages": [
                HumanMessage(
                    content="Analyze the benefits of remote work for productivity"
                )
            ]
        }
    )

    # Direct access
    analysis = result.get("analysis_result")

    execution_time = time.time() - start_time

    print(f"✅ Execution time: {execution_time:.2f}s")
    print(f"📦 Result type: {type(result).__name__}")
    print(f"🔑 Result keys: {list(result.keys())}")

    if analysis:
        print(f"\n✅ Successfully extracted AnalysisResult:")
        print(f"   Topic: {analysis.topic}")
        print(f"   Confidence: {analysis.confidence:.2f}")
        print(f"   Findings: {analysis.findings}")
        print(f"   Recommendation: {analysis.recommendation[:80]}...")
    else:
        print("❌ Failed to extract structured output")

    # Pros and Cons
    print("\n📊 Evaluation:")
    print("✅ Pros: Simple, direct, no extra dependencies")
    print("❌ Cons: No validation, hardcoded field name, no error handling")

    return analysis, execution_time


# ========== APPROACH 2: StructuredOutputHandler ==========
async def approach_2_handler_class():
    """Approach 2: Using StructuredOutputHandler for robust extraction."""
    print("\n" + "=" * 80)
    print("APPROACH 2: StructuredOutputHandler Class")
    print("=" * 80)

    start_time = time.time()

    # Create agent
    agent = SimpleAgentV3(
        name="handler_agent",
        engine=AugLLMConfig(temperature=0.1),
        structured_output_model=AnalysisResult,
    )

    # Create handler
    handler = StructuredOutputHandler(AnalysisResult)

    # Execute
    result = await agent.arun(
        {
            "messages": [
                HumanMessage(content="Analyze the impact of AI on software development")
            ]
        }
    )

    # Extract with handler
    analysis = handler.extract(result)

    execution_time = time.time() - start_time

    print(f"✅ Execution time: {execution_time:.2f}s")
    print(f"🔍 Handler searched fields: {handler.expected_fields}")

    if analysis:
        print(f"\n✅ Successfully extracted AnalysisResult:")
        print(f"   Topic: {analysis.topic}")
        print(f"   Confidence: {analysis.confidence:.2f}")
        print(f"   Findings: {analysis.findings}")
        print(f"   Recommendation: {analysis.recommendation[:80]}...")

    # Try with wrong field name to show robustness
    result_fake = {"wrong_field": analysis}
    found = handler.extract(result_fake)
    print(
        f"\n🧪 Robustness test (wrong field): {'✅ Still found!' if found else '❌ Not found'}"
    )

    print("\n📊 Evaluation:")
    print("✅ Pros: Robust, handles multiple field names, reusable")
    print("❌ Cons: Extra import, slight overhead")

    return analysis, execution_time


# ========== APPROACH 3: Custom Agent Method ==========
class StructuredAgent(SimpleAgentV3):
    """Agent with built-in structured output method."""

    async def get_analysis(self, input_data: dict) -> Optional[AnalysisResult]:
        """Run agent and return structured output directly."""
        result = await self.arun(input_data)
        return result.get("analysis_result")


async def approach_3_custom_agent():
    """Approach 3: Custom agent class with built-in extraction."""
    print("\n" + "=" * 80)
    print("APPROACH 3: Custom Agent with Built-in Method")
    print("=" * 80)

    start_time = time.time()

    # Create custom agent
    agent = StructuredAgent(
        name="custom_agent",
        engine=AugLLMConfig(temperature=0.1),
        structured_output_model=AnalysisResult,
    )

    # Get structured output directly
    analysis = await agent.get_analysis(
        {"messages": [HumanMessage(content="Analyze the future of electric vehicles")]}
    )

    execution_time = time.time() - start_time

    print(f"✅ Execution time: {execution_time:.2f}s")
    print(f"🎯 Direct return type: {type(analysis).__name__ if analysis else 'None'}")

    if analysis:
        print(f"\n✅ Successfully got AnalysisResult directly:")
        print(f"   Topic: {analysis.topic}")
        print(f"   Confidence: {analysis.confidence:.2f}")
        print(f"   Findings: {analysis.findings}")
        print(f"   Recommendation: {analysis.recommendation[:80]}...")

    print("\n📊 Evaluation:")
    print("✅ Pros: Clean API, type-safe, encapsulated")
    print("❌ Cons: Requires custom class, more setup")

    return analysis, execution_time


# ========== APPROACH 4: Post-processing in Agent ==========
class PostProcessingAgent(SimpleAgentV3):
    """Agent that modifies execution mixin behavior."""

    def _process_output(self, output_data: Any) -> Any:
        """Override to return structured output directly if available."""
        # Call parent to get normal processing
        result = super()._process_output(output_data)

        # If we have structured output, return it directly
        if isinstance(result, dict) and "analysis_result" in result:
            return result["analysis_result"]

        return result


async def approach_4_post_processing():
    """Approach 4: Override _process_output to return structured output directly."""
    print("\n" + "=" * 80)
    print("APPROACH 4: Post-processing Override")
    print("=" * 80)

    start_time = time.time()

    # Create agent with post-processing
    agent = PostProcessingAgent(
        name="postprocess_agent",
        engine=AugLLMConfig(temperature=0.1),
        structured_output_model=AnalysisResult,
    )

    # Execute - should return AnalysisResult directly
    analysis = await agent.arun(
        {
            "messages": [
                HumanMessage(
                    content="Analyze the role of quantum computing in cryptography"
                )
            ]
        }
    )

    execution_time = time.time() - start_time

    print(f"✅ Execution time: {execution_time:.2f}s")
    print(f"🎯 Direct return type: {type(analysis).__name__}")
    print(f"📦 Is AnalysisResult: {isinstance(analysis, AnalysisResult)}")

    if isinstance(analysis, AnalysisResult):
        print(f"\n✅ Got AnalysisResult directly (no extraction needed!):")
        print(f"   Topic: {analysis.topic}")
        print(f"   Confidence: {analysis.confidence:.2f}")
        print(f"   Findings: {analysis.findings}")
        print(f"   Recommendation: {analysis.recommendation[:80]}...")

    print("\n📊 Evaluation:")
    print("✅ Pros: Returns structured output directly, no extraction needed")
    print("❌ Cons: Loses access to messages/state, breaks LangGraph conventions")

    return analysis, execution_time


# ========== APPROACH 5: Wrapper Function ==========
async def analyze_with_structure(query: str) -> AnalysisResult:
    """Wrapper function that handles all the complexity."""
    agent = SimpleAgentV3(
        name="wrapper_agent",
        engine=AugLLMConfig(temperature=0.1),
        structured_output_model=AnalysisResult,
    )

    result = await agent.arun({"messages": [HumanMessage(content=query)]})

    handler = StructuredOutputHandler(AnalysisResult)
    return handler.extract_or_raise(result)


async def approach_5_wrapper_function():
    """Approach 5: Clean wrapper function hiding complexity."""
    print("\n" + "=" * 80)
    print("APPROACH 5: Wrapper Function")
    print("=" * 80)

    start_time = time.time()

    # Simple one-line usage
    analysis = await analyze_with_structure("Analyze the benefits of renewable energy")

    execution_time = time.time() - start_time

    print(f"✅ Execution time: {execution_time:.2f}s")
    print(f"🎯 Clean API: analysis = await analyze_with_structure(query)")

    print(f"\n✅ Got result with one line:")
    print(f"   Topic: {analysis.topic}")
    print(f"   Confidence: {analysis.confidence:.2f}")
    print(f"   Findings: {analysis.findings}")
    print(f"   Recommendation: {analysis.recommendation[:80]}...")

    print("\n📊 Evaluation:")
    print("✅ Pros: Super clean API, hides complexity, reusable")
    print("❌ Cons: Less flexible, creates new agent each time")

    return analysis, execution_time


# ========== COMPARISON ==========
async def run_comparison():
    """Run all approaches and compare results."""
    print("🔬 COMPARING STRUCTURED OUTPUT APPROACHES")
    print("=" * 80)
    print("Testing different ways to handle LangGraph's AddableValuesDict return type")

    results = []

    # Run all approaches
    for approach_func in [
        approach_1_direct_access,
        approach_2_handler_class,
        approach_3_custom_agent,
        approach_4_post_processing,
        approach_5_wrapper_function,
    ]:
        try:
            analysis, exec_time = await approach_func()
            results.append(
                {
                    "approach": approach_func.__name__,
                    "success": analysis is not None,
                    "execution_time": exec_time,
                    "has_direct_return": isinstance(analysis, AnalysisResult),
                }
            )
        except Exception as e:
            print(f"❌ Error in {approach_func.__name__}: {e}")
            results.append(
                {
                    "approach": approach_func.__name__,
                    "success": False,
                    "execution_time": 0,
                    "error": str(e),
                }
            )

    # Summary comparison
    print("\n" + "=" * 80)
    print("📊 FINAL COMPARISON")
    print("=" * 80)

    print("\n🏆 Performance Summary:")
    for result in results:
        status = "✅" if result["success"] else "❌"
        print(f"{status} {result['approach']:30} - {result['execution_time']:.2f}s")

    print("\n🎯 Recommendations:")
    print(
        """
1. **For Simple Use Cases**: Approach 1 (Direct Access)
   - When you know the field name
   - Don't need error handling
   - Want minimal code

2. **For Production Code**: Approach 2 (StructuredOutputHandler)
   - Robust extraction with fallbacks
   - Good error messages
   - Reusable across projects

3. **For Clean APIs**: Approach 3 (Custom Agent)
   - When building a library
   - Want type-safe methods
   - Users shouldn't see complexity

4. **For Direct Returns**: Approach 4 (Post-processing)
   - If you really need direct returns
   - Willing to break LangGraph conventions
   - Don't need access to state

5. **For Quick Scripts**: Approach 5 (Wrapper Function)
   - One-off analysis tasks
   - Don't need agent reuse
   - Maximum simplicity
"""
    )


async def main():
    """Main entry point."""
    # Reduce logging
    os.environ["HAIVE_LOG_LEVEL"] = "ERROR"

    await run_comparison()


if __name__ == "__main__":
    asyncio.run(main())
