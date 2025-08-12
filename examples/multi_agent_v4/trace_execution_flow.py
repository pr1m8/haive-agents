#!/usr/bin/env python3
"""Trace execution flow to understand structured output behavior.

This creates a detailed log file showing the execution path.

Date: August 7, 2025
"""

import asyncio
import json
import os
from datetime import datetime
from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.react.agent_v4 import ReactAgentV4
from haive.agents.simple.agent_v3 import SimpleAgentV3


# Define structured output model
class AnalysisResult(BaseModel):
    """Analysis result with structured fields."""

    topic: str = Field(description="Topic being analyzed")
    findings: list[str] = Field(description="Key findings")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence score")
    recommendation: str = Field(description="Main recommendation")


# Simple tool
@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    try:
        result = eval(expression)
        return f"Result: {result}"
    except:
        return "Error: Invalid expression"


class ExecutionTracer:
    """Trace execution flow and log to file."""

    def __init__(self, log_file: str):
        self.log_file = log_file
        self.steps = []
        self.start_time = datetime.now()

    def log(self, step: str, data: dict[str, Any] = None):
        """Log a step in the execution."""
        entry = {
            "step_number": len(self.steps) + 1,
            "timestamp": datetime.now().isoformat(),
            "step": step,
            "data": data or {},
        }
        self.steps.append(entry)

        # Also print to console
        print(f"Step {entry['step_number']}: {step}")
        if data:
            for key, value in data.items():
                if isinstance(value, type):
                    print(f"  {key}: {value.__name__}")
                else:
                    print(f"  {key}: {value}")

    def save(self):
        """Save the trace to file."""
        trace_data = {
            "start_time": self.start_time.isoformat(),
            "end_time": datetime.now().isoformat(),
            "total_steps": len(self.steps),
            "steps": self.steps,
        }

        with open(self.log_file, "w") as f:
            json.dump(trace_data, f, indent=2, default=str)

        print(f"\n✅ Trace saved to: {self.log_file}")
        print(f"   Total steps: {len(self.steps)}")


async def trace_simple_agent(tracer: ExecutionTracer):
    """Trace SimpleAgentV3 with structured output."""
    tracer.log(
        "Creating SimpleAgentV3 with structured_output_model",
        {"agent_class": "SimpleAgentV3", "structured_output_model": AnalysisResult},
    )

    agent = SimpleAgentV3(
        name="simple_trace",
        engine=AugLLMConfig(
            temperature=0.1,
            system_message="Extract information into structured format.",
        ),
        structured_output_model=AnalysisResult,
        verbose=False,
        debug=False,
    )

    tracer.log(
        "Agent created - checking configuration",
        {
            "agent_type": type(agent).__name__,
            "has_structured_output_model": agent.structured_output_model is not None,
            "needs_wrapper": getattr(agent, "_needs_structured_output_wrapper", False),
        },
    )

    # Check graph
    if hasattr(agent, "graph"):
        tracer.log(
            "Checking graph structure",
            {
                "graph_type": type(agent.graph).__name__,
                "graph_nodes": (
                    list(agent.graph.nodes.keys())
                    if hasattr(agent.graph, "nodes")
                    else "N/A"
                ),
            },
        )

    # Execute
    tracer.log("Starting execution")

    result = await agent.arun(
        {
            "messages": [
                HumanMessage(
                    content="AI improves productivity by 25% from baseline 100 units"
                )
            ]
        }
    )

    tracer.log(
        "Execution completed - analyzing result",
        {
            "result_type": type(result).__name__,
            "result_module": type(result).__module__,
            "is_dict": isinstance(result, dict),
            "dict_keys": list(result.keys()) if isinstance(result, dict) else "N/A",
        },
    )

    # Check for structured output
    if isinstance(result, dict) and "analysis_result" in result:
        analysis = result["analysis_result"]
        tracer.log(
            "Found structured output in result",
            {
                "field_name": "analysis_result",
                "field_type": type(analysis).__name__,
                "is_expected_type": isinstance(analysis, AnalysisResult),
            },
        )

    return result


async def trace_react_agent(tracer: ExecutionTracer):
    """Trace ReactAgentV4 with structured output."""
    tracer.log(
        "Creating ReactAgentV4 with structured_output_model",
        {
            "agent_class": "ReactAgentV4",
            "structured_output_model": AnalysisResult,
            "with_tools": True,
        },
    )

    agent = ReactAgentV4(
        name="react_trace",
        engine=AugLLMConfig(
            temperature=0.1, system_message="Use tools to analyze the query."
        ),
        tools=[calculator],
        structured_output_model=AnalysisResult,
        verbose=False,
        debug=False,
    )

    tracer.log(
        "ReactAgent created - checking configuration",
        {
            "agent_type": type(agent).__name__,
            "has_structured_output_model": agent.structured_output_model is not None,
            "needs_wrapper": getattr(agent, "_needs_structured_output_wrapper", False),
            "num_tools": len(agent.tools) if hasattr(agent, "tools") else 0,
        },
    )

    # Check graph
    if hasattr(agent, "graph"):
        tracer.log(
            "Checking ReactAgent graph structure",
            {
                "graph_type": type(agent.graph).__name__,
                "graph_nodes": (
                    list(agent.graph.nodes.keys())
                    if hasattr(agent.graph, "nodes")
                    else "N/A"
                ),
            },
        )

    # Execute
    tracer.log("Starting ReactAgent execution")

    result = await agent.arun(
        {
            "messages": [
                HumanMessage(
                    content="Calculate 25% of 100 for AI productivity analysis"
                )
            ]
        }
    )

    tracer.log(
        "ReactAgent execution completed",
        {
            "result_type": type(result).__name__,
            "result_module": type(result).__module__,
            "dict_keys": list(result.keys()) if isinstance(result, dict) else "N/A",
        },
    )

    return result


async def main():
    """Main execution tracer."""
    # Create log file
    log_file = "structured_output_trace.json"
    tracer = ExecutionTracer(log_file)

    print("🔍 TRACING STRUCTURED OUTPUT EXECUTION")
    print("=" * 60)

    # Trace SimpleAgentV3
    print("\n1️⃣ TRACING SimpleAgentV3")
    print("-" * 40)
    await trace_simple_agent(tracer)

    # Trace ReactAgentV4
    print("\n2️⃣ TRACING ReactAgentV4")
    print("-" * 40)
    await trace_react_agent(tracer)

    # Summary
    tracer.log(
        "SUMMARY - Key findings",
        {
            "return_type": "AddableValuesDict",
            "return_module": "langgraph.pregel.io",
            "structured_output_location": "result['analysis_result']",
            "reason": "LangGraph always returns AddableValuesDict containing the full state",
        },
    )

    # Save trace
    tracer.save()

    print("\n" + "=" * 60)
    print("💡 KEY INSIGHTS")
    print("=" * 60)
    print("1. LangGraph execution always returns AddableValuesDict")
    print("2. This is the accumulated state from all graph nodes")
    print("3. Structured output is added as a field in the state")
    print("4. Access pattern: result['analysis_result']")
    print("\n📄 Full trace saved to: " + log_file)


if __name__ == "__main__":
    # Disable verbose logging
    os.environ["HAIVE_LOG_LEVEL"] = "ERROR"

    asyncio.run(main())
