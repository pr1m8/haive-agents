#!/usr/bin/env python3
"""Debug script to trace structured output behavior.

This script investigates why structured output returns AddableValuesDict
instead of the Pydantic model directly.

Date: August 7, 2025
"""

import asyncio
import pdb
from typing import List

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.react.agent_v4 import ReactAgentV4


# Define structured output model
class AnalysisResult(BaseModel):
    """Analysis result with structured fields."""

    topic: str = Field(description="Topic being analyzed")
    findings: List[str] = Field(description="Key findings")
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


async def debug_structured_output():
    """Debug structured output execution flow."""

    print("🔍 DEBUGGING STRUCTURED OUTPUT FLOW")
    print("=" * 60)

    # Create ReactAgent with structured_output_model
    print("Creating ReactAgent with structured_output_model...")
    agent = ReactAgentV4(
        name="debug_agent",
        engine=AugLLMConfig(
            temperature=0.7,
            system_message="You are an analytical assistant. Use tools to gather information.",
        ),
        tools=[calculator, analyzer],
        structured_output_model=AnalysisResult,
        verbose=True,
        debug=True,  # Enable debug mode
    )

    print(f"\n📋 Agent Configuration:")
    print(f"  - Name: {agent.name}")
    print(f"  - Type: {type(agent).__name__}")
    print(f"  - Has structured_output_model: {agent.structured_output_model}")
    print(
        f"  - Needs wrapper: {getattr(agent, '_needs_structured_output_wrapper', False)}"
    )

    # Check graph structure
    if hasattr(agent, "graph") and agent.graph:
        print(f"\n📊 Graph Info:")
        print(f"  - Graph type: {type(agent.graph).__name__}")
        print(
            f"  - Graph nodes: {list(agent.graph.nodes.keys()) if hasattr(agent.graph, 'nodes') else 'N/A'}"
        )

    # Let's check the compiled graph
    print("\n🔧 Compiling graph...")
    try:
        compiled_graph = agent.compile()
        print(f"  - Compiled graph type: {type(compiled_graph).__name__}")
    except Exception as e:
        print(f"  - Compilation error: {e}")
        compiled_graph = None

    query = "Analyze the impact of AI on productivity. Calculate the potential 25% improvement on a baseline of 100 units."

    print(f"\n📋 Query: {query}")
    print("\n" + "=" * 60)
    print("🚀 EXECUTING WITH DEBUG=TRUE")
    print("=" * 60)

    # Set a breakpoint here to step through execution
    print("\n⏸️  Setting breakpoint for debugging...")
    print("   Use 'n' to step through, 'c' to continue")
    print("   Inspect 'result' variable after execution")

    # pdb.set_trace()  # Uncomment to enable breakpoint

    try:
        # Execute with debug=True
        result = await agent.arun(
            {"messages": [HumanMessage(content=query)]},
            debug=True,  # Pass debug flag to execution
        )

        print("\n✅ EXECUTION COMPLETED!")
        print("=" * 60)

        # Detailed result inspection
        print(f"\n🔎 Result Analysis:")
        print(f"  - Type: {type(result).__name__}")
        print(f"  - Is dict: {isinstance(result, dict)}")
        print(f"  - Is BaseModel: {isinstance(result, BaseModel)}")
        print(f"  - Is AnalysisResult: {isinstance(result, AnalysisResult)}")

        if isinstance(result, dict):
            print(f"\n  Dictionary Keys: {list(result.keys())}")

            # Check for structured output fields
            if "analysis_result" in result:
                analysis = result["analysis_result"]
                print(f"\n  'analysis_result' field:")
                print(f"    - Type: {type(analysis).__name__}")
                print(
                    f"    - Is AnalysisResult: {isinstance(analysis, AnalysisResult)}"
                )

                if isinstance(analysis, AnalysisResult):
                    print(f"    - Topic: {analysis.topic}")
                    print(f"    - Confidence: {analysis.confidence}")
                    print(f"    - Findings: {len(analysis.findings)} items")

        # Check execution path
        print(f"\n🛤️  Execution Path Analysis:")

        # Look at the agent's internal state
        if hasattr(agent, "_compiled_graph") and agent._compiled_graph:
            print("  - Has compiled graph")

        # Check if it went through multi-agent wrapper
        if hasattr(agent, "graph"):
            graph = agent.graph
            if hasattr(graph, "_underlying_graph"):
                print("  - Graph has underlying graph (multi-agent)")

        # Trace the source
        print(f"\n📍 Tracing Result Source:")
        print(
            f"  - Result module: {result.__class__.__module__ if hasattr(result, '__class__') else 'N/A'}"
        )
        print(
            f"  - Result class: {result.__class__.__name__ if hasattr(result, '__class__') else 'N/A'}"
        )

        # Check if it's from LangGraph
        if result.__class__.__module__.startswith("langgraph"):
            print("  - Result is from LangGraph (AddableValuesDict)")
            print("  - This is the standard return type from LangGraph execution")

    except Exception as e:
        print(f"\n❌ EXECUTION FAILED: {type(e).__name__}: {e}")
        import traceback

        traceback.print_exc()

    print("\n" + "=" * 60)
    print("💡 FINDINGS")
    print("=" * 60)
    print("1. LangGraph returns AddableValuesDict by default")
    print("2. This is a dict-like object that supports graph operations")
    print("3. Structured output is nested inside as a field")
    print("4. This is expected behavior for graph-based execution")
    print("\nTo get the Pydantic model directly:")
    print("  result['analysis_result']  # Access the nested field")


async def trace_execution_path():
    """Trace the exact execution path for structured output."""

    print("\n" + "=" * 60)
    print("🔬 TRACING EXECUTION PATH")
    print("=" * 60)

    # Create a minimal agent
    agent = ReactAgentV4(
        name="trace_agent",
        engine=AugLLMConfig(temperature=0.1),
        tools=[calculator],
        structured_output_model=AnalysisResult,
        debug=True,
    )

    # Inspect the graph structure
    print("\n📊 Graph Structure:")
    if hasattr(agent, "graph") and agent.graph:
        graph = agent.graph
        print(f"  - Graph class: {graph.__class__.__name__}")
        print(f"  - From module: {graph.__class__.__module__}")

        # Check nodes
        if hasattr(graph, "nodes"):
            print(f"\n  Nodes in graph:")
            for node_name in graph.nodes:
                print(f"    - {node_name}")

        # Check if it's wrapped
        if hasattr(graph, "_agents"):
            print(f"\n  Multi-agent detected:")
            print(
                f"    - Number of agents: {len(graph._agents) if hasattr(graph, '_agents') else 'N/A'}"
            )

    # Simple execution
    result = await agent.arun({"messages": [HumanMessage(content="Quick analysis")]})

    print(f"\n📦 Result Structure:")
    print(f"  - Type: {type(result)}")
    print(
        f"  - Keys: {list(result.keys()) if isinstance(result, dict) else 'Not a dict'}"
    )

    # Check where AddableValuesDict comes from
    print(f"\n🔍 AddableValuesDict Source:")
    print("  - This is LangGraph's standard return type")
    print("  - It allows graph nodes to add values to the state")
    print("  - The structured output is embedded within it")

    return result


if __name__ == "__main__":
    print("Starting debug session...\n")

    # Run main debug
    asyncio.run(debug_structured_output())

    # Run execution path trace
    asyncio.run(trace_execution_path())

    print("\n✅ Debug session complete!")
