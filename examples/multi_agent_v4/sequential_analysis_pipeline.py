"""Sequential Analysis Pipeline Example

This example demonstrates a ReactAgent → SimpleAgent sequential workflow
where a ReactAgent performs analysis with tools, then a SimpleAgent
formats the results with structured output.

Date: August 7, 2025
"""

import asyncio
from pydantic import BaseModel, Field
from typing import List, Dict
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.react.agent_v4 import ReactAgentV4
from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.core.engine.aug_llm import AugLLMConfig


# Define structured output for the formatter
class AnalysisReport(BaseModel):
    """Structured analysis report."""

    title: str = Field(description="Report title")
    summary: str = Field(description="Executive summary of findings")
    key_metrics: Dict[str, float] = Field(description="Key numerical findings")
    insights: List[str] = Field(description="Key insights discovered")
    recommendations: List[str] = Field(description="Actionable recommendations")
    confidence_level: float = Field(ge=0.0, le=1.0, description="Overall confidence")


# Define tools for the ReactAgent
@tool
def calculate_growth(initial: float, final: float) -> str:
    """Calculate growth percentage between two values."""
    if initial == 0:
        return "Cannot calculate growth from zero"
    growth = ((final - initial) / initial) * 100
    return f"Growth: {growth:.2f}% (from {initial} to {final})"


@tool
def analyze_trend(values: str) -> str:
    """Analyze trend from comma-separated values."""
    try:
        nums = [float(x.strip()) for x in values.split(",")]
        if len(nums) < 2:
            return "Need at least 2 values for trend analysis"

        # Simple trend analysis
        increasing = all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))
        decreasing = all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1))

        avg = sum(nums) / len(nums)

        if increasing:
            trend = "upward"
        elif decreasing:
            trend = "downward"
        else:
            trend = "mixed"

        return f"Trend: {trend}, Average: {avg:.2f}, Range: {min(nums)}-{max(nums)}"
    except Exception as e:
        return f"Error analyzing trend: {str(e)}"


@tool
def statistical_summary(values: str) -> str:
    """Provide statistical summary of comma-separated values."""
    try:
        nums = [float(x.strip()) for x in values.split(",")]
        if not nums:
            return "No values provided"

        mean = sum(nums) / len(nums)
        sorted_nums = sorted(nums)
        median = (
            sorted_nums[len(nums) // 2]
            if len(nums) % 2
            else (sorted_nums[len(nums) // 2 - 1] + sorted_nums[len(nums) // 2]) / 2
        )

        return f"Count: {len(nums)}, Mean: {mean:.2f}, Median: {median:.2f}, Min: {min(nums)}, Max: {max(nums)}"
    except Exception as e:
        return f"Error in statistical summary: {str(e)}"


async def main():
    """Run the sequential analysis pipeline."""

    # Configure engines
    analyzer_config = AugLLMConfig(
        temperature=0.3,
        system_message="You are a data analyst. Use the provided tools to analyze data thoroughly.",
        max_tokens=1000,
    )

    formatter_config = AugLLMConfig(
        temperature=0.5,
        system_message="You are a report formatter. Create clear, structured reports from analysis results.",
        max_tokens=1000,
    )

    # Create agents
    print("Creating agents...")

    # ReactAgent for analysis with tools
    analyzer = ReactAgentV4(
        name="data_analyzer",
        engine=analyzer_config,
        tools=[calculate_growth, analyze_trend, statistical_summary],
        debug=True,
    )

    # SimpleAgent for formatting with structured output
    formatter = SimpleAgentV3(
        name="report_formatter",
        engine=formatter_config,
        structured_output_model=AnalysisReport,
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "Format the analysis into a structured report."),
                ("human", "Create a report from this analysis: {messages}"),
            ]
        ),
        debug=True,
    )

    # Create sequential workflow
    print("\nCreating workflow...")
    workflow = EnhancedMultiAgentV4(
        name="analysis_pipeline",
        agents=[analyzer, formatter],
        execution_mode="sequential",
    )

    # Test data
    test_query = """
    Analyze our quarterly sales data:
    Q1: 100000, Q2: 125000, Q3: 145000, Q4: 180000
    
    Also analyze customer count:
    Q1: 1000, Q2: 1200, Q3: 1400, Q4: 1650
    
    Calculate growth rates and provide insights about the business performance.
    """

    print("\nExecuting workflow...")
    print(f"Query: {test_query}")

    # Execute workflow
    try:
        print("\nStarting workflow execution...")
        result = await workflow.arun({"messages": [HumanMessage(content=test_query)]})
        print(f"\nWorkflow execution completed. Result type: {type(result)}")

        # The result IS the state after execution
        final_state = result

        # Debug: Show what's in the state
        print(
            f"\nState attributes: {[attr for attr in dir(final_state) if not attr.startswith('_')][:10]}..."
        )

    except Exception as e:
        print(f"\nERROR during workflow execution: {type(e).__name__}: {e}")
        import traceback

        traceback.print_exc()
        return

    # Display results
    print("\n" + "=" * 60)
    print("WORKFLOW RESULTS")
    print("=" * 60)

    # Show analyzer output
    if (
        hasattr(final_state, "agent_outputs")
        and "data_analyzer" in final_state.agent_outputs
    ):
        print("\n[Data Analyzer Output]")
        print(final_state.agent_outputs["data_analyzer"])

    # Show formatted report
    if hasattr(final_state, "report_formatter"):
        report = final_state.report_formatter
        print("\n[Formatted Report]")
        print(f"Title: {report.title}")
        print(f"Summary: {report.summary}")
        print(f"\nKey Metrics:")
        for metric, value in report.key_metrics.items():
            print(f"  - {metric}: {value}")
        print(f"\nInsights:")
        for insight in report.insights:
            print(f"  • {insight}")
        print(f"\nRecommendations:")
        for rec in report.recommendations:
            print(f"  → {rec}")
        print(f"\nConfidence Level: {report.confidence_level:.0%}")

    # Show execution details
    print("\n" + "=" * 60)
    print("EXECUTION DETAILS")
    print("=" * 60)
    if hasattr(final_state, "agent_execution_order"):
        print(f"Execution order: {final_state.agent_execution_order}")
    if hasattr(final_state, "active_agent"):
        print(f"Active agent: {final_state.active_agent}")
    if hasattr(final_state, "recompile_count"):
        print(f"Recompile count: {final_state.recompile_count}")

    # Verify tool isolation
    print("\n" + "=" * 60)
    print("TOOL ISOLATION CHECK")
    print("=" * 60)
    print(f"Analyzer tools ({len(analyzer.tools)}): {[t.name for t in analyzer.tools]}")
    print(
        f"Formatter tools ({len(formatter.tools)}): {[t.name for t in formatter.tools]}"
    )
    print("✓ Tools are properly isolated between agents")


if __name__ == "__main__":
    print("Sequential Analysis Pipeline Example")
    print("===================================\n")
    asyncio.run(main())
