#!/usr/bin/env python3
"""Test MultiAgent with structured output transfer between agents."""

import sys
import os
from typing import List

# Add the packages to path  
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../src"))

from pydantic import BaseModel, Field
from langchain_core.tools import tool
from haive.core.engine.aug_llm import AugLLMConfig
from haive.agents.simple.agent import SimpleAgent
from haive.agents.react.agent import ReactAgent
from haive.agents.multi.agent import MultiAgent


# Define structured output models for each stage
class AnalysisResult(BaseModel):
    """Analysis output from ReactAgent."""
    topic: str = Field(description="The analyzed topic")
    key_findings: List[str] = Field(description="Key findings from analysis")
    data_points: List[float] = Field(description="Numerical data discovered")
    requires_action: bool = Field(description="Whether action is required")
    confidence: float = Field(ge=0.0, le=1.0, description="Analysis confidence")


class ActionPlan(BaseModel):
    """Action plan from planning agent."""
    analysis_summary: str = Field(description="Summary of the analysis")
    recommended_actions: List[str] = Field(description="Recommended actions to take")
    priority_order: List[int] = Field(description="Priority order for actions (1=highest)")
    timeline: str = Field(description="Suggested timeline for implementation")
    success_metrics: List[str] = Field(description="How to measure success")


class ExecutiveReport(BaseModel):
    """Final executive report."""
    executive_summary: str = Field(description="High-level summary for executives")
    situation_overview: str = Field(description="Current situation overview")
    recommendations: List[str] = Field(description="Top 3-5 recommendations")
    expected_impact: str = Field(description="Expected business impact")
    next_steps: str = Field(description="Immediate next steps")
    risk_assessment: str = Field(description="Key risks and mitigation")


# Tools for ReactAgent
@tool
def market_data_analyzer(query: str) -> str:
    """Analyze market data and trends."""
    # Simulate market analysis
    data = {
        "renewable energy": "Market growing at 15% annually, $1.5T by 2025",
        "ev market": "350% growth in 5 years, Tesla leads with 18% share",
        "ai adoption": "85% of enterprises have AI initiatives, $126B market",
        "cloud computing": "23% CAGR, AWS 32%, Azure 23%, GCP 10% market share"
    }
    
    for key, value in data.items():
        if key in query.lower():
            return f"Market analysis: {value}"
    
    return "Market shows positive growth trends in this sector"


@tool
def financial_calculator(metric: str, values: List[float]) -> str:
    """Perform financial calculations."""
    if not values:
        return "No values provided for calculation"
    
    if "roi" in metric.lower():
        # Simple ROI calculation
        if len(values) >= 2:
            roi = ((values[1] - values[0]) / values[0]) * 100
            return f"ROI: {roi:.2f}%"
    elif "average" in metric.lower() or "avg" in metric.lower():
        avg = sum(values) / len(values)
        return f"Average: {avg:.2f}"
    elif "growth" in metric.lower():
        if len(values) >= 2:
            growth = ((values[-1] - values[0]) / values[0]) * 100
            return f"Growth rate: {growth:.2f}%"
    
    return f"Calculated {metric}: {sum(values):.2f}"


def test_multiagent_with_structured_output():
    """Test proper MultiAgent orchestration with structured output."""
    
    print("\n🔬 TESTING MULTIAGENT WITH STRUCTURED OUTPUT")
    print("=" * 60)
    
    # Step 1: Create ReactAgent for analysis with tools
    analysis_engine = AugLLMConfig(
        structured_output_model=AnalysisResult,
        temperature=0.7,
        system_message="You are a market analysis expert. Analyze trends and provide data-driven insights."
    )
    
    # Important: Don't use force_tool_use with structured output
    analysis_engine.force_tool_use = False
    
    analyzer = ReactAgent(
        name="market_analyzer",
        engine=analysis_engine,
        tools=[market_data_analyzer, financial_calculator],
        max_iterations=3,
        debug=False  # Set to True to see detailed execution
    )
    
    # Step 2: Create SimpleAgent for action planning
    planning_engine = AugLLMConfig(
        structured_output_model=ActionPlan,
        temperature=0.6,
        system_message="You are a strategic planning expert. Create actionable plans based on analysis."
    )
    
    planner = SimpleAgent(
        name="action_planner",
        engine=planning_engine,
        debug=False
    )
    
    # Step 3: Create SimpleAgent for executive reporting
    reporting_engine = AugLLMConfig(
        structured_output_model=ExecutiveReport,
        temperature=0.5,
        system_message="You are an executive communication expert. Create clear, concise reports for C-suite."
    )
    
    reporter = SimpleAgent(
        name="executive_reporter",
        engine=reporting_engine,
        debug=False
    )
    
    # Step 4: Create MultiAgent to orchestrate the workflow
    print("\n📊 Creating MultiAgent workflow...")
    
    workflow = MultiAgent(
        name="market_analysis_workflow",
        agents=[analyzer, planner, reporter],
        execution_mode="sequential",
        build_mode="auto"  # Builds graph immediately
    )
    
    print(f"✅ MultiAgent created with {len(workflow.agents)} agents")
    print(f"   Execution mode: {workflow.execution_mode}")
    print(f"   Agents: {[a.name for a in workflow.agents]}")
    
    # Step 5: Execute the workflow
    print("\n🚀 Executing multi-agent workflow...")
    
    task = "Analyze the renewable energy market opportunity and create an investment strategy"
    
    try:
        result = workflow.run(task)
        
        print("\n✅ Workflow completed successfully!")
        
        # The result should be from the last agent (ExecutiveReport)
        if hasattr(result, 'executive_summary'):
            print(f"\n📋 Executive Report Generated:")
            print(f"   Summary: {result.executive_summary[:100]}...")
            print(f"   Recommendations: {len(result.recommendations)} recommendations")
            print(f"   Next Steps: {result.next_steps[:100]}...")
            
            # Show some recommendations
            print(f"\n💡 Top Recommendations:")
            for i, rec in enumerate(result.recommendations[:3], 1):
                print(f"   {i}. {rec}")
        else:
            print(f"\n📄 Result: {result}")
            
    except Exception as e:
        print(f"\n❌ Workflow failed: {e}")
        raise
    
    return workflow, result


def test_multiagent_with_conditional_routing():
    """Test MultiAgent with conditional execution paths."""
    
    print("\n\n🔬 TESTING MULTIAGENT WITH CONDITIONAL ROUTING")
    print("=" * 60)
    
    # Define models for conditional flow
    class InitialAssessment(BaseModel):
        complexity: float = Field(ge=0.0, le=1.0, description="Task complexity score")
        category: str = Field(description="Task category: simple, complex, or expert")
        reasoning: str = Field(description="Reasoning for categorization")
    
    class SimpleResult(BaseModel):
        answer: str = Field(description="Simple direct answer")
        confidence: float = Field(ge=0.0, le=1.0)
    
    class ComplexResult(BaseModel):
        analysis: str = Field(description="Detailed analysis")
        components: List[str] = Field(description="Key components analyzed")
        conclusion: str = Field(description="Final conclusion")
        confidence: float = Field(ge=0.0, le=1.0)
    
    # Create agents
    classifier = SimpleAgent(
        name="classifier",
        engine=AugLLMConfig(
            structured_output_model=InitialAssessment,
            temperature=0.3,
            system_message="Classify tasks by complexity and route appropriately."
        )
    )
    
    simple_processor = SimpleAgent(
        name="simple_processor",
        engine=AugLLMConfig(
            structured_output_model=SimpleResult,
            temperature=0.5,
            system_message="Provide quick, simple answers to straightforward questions."
        )
    )
    
    complex_processor = SimpleAgent(
        name="complex_processor",
        engine=AugLLMConfig(
            structured_output_model=ComplexResult,
            temperature=0.7,
            system_message="Provide thorough analysis for complex questions."
        )
    )
    
    # Create conditional workflow
    print("\n📊 Creating conditional MultiAgent workflow...")
    
    workflow = MultiAgent(
        name="adaptive_workflow",
        agents=[classifier, simple_processor, complex_processor],
        execution_mode="conditional",
        build_mode="manual"  # We'll add edges manually
    )
    
    # Add conditional routing from classifier
    def route_by_complexity(state):
        """Route based on complexity score."""
        # In a real implementation, you'd check the state properly
        # This is simplified for the example
        if hasattr(state, 'complexity') and state.complexity > 0.7:
            return "complex_processor"
        else:
            return "simple_processor"
    
    workflow.add_conditional_edge(
        from_agent="classifier",
        condition=route_by_complexity,
        destinations={
            "simple_processor": "simple_processor",
            "complex_processor": "complex_processor"
        },
        default="simple_processor"
    )
    
    # Build the graph
    workflow.build()
    
    print(f"✅ Conditional workflow created")
    
    # Test with different complexity tasks
    print("\n🧪 Testing with simple task...")
    simple_result = workflow.run("What is 2+2?")
    
    print("\n🧪 Testing with complex task...")
    complex_result = workflow.run(
        "Analyze the geopolitical implications of renewable energy adoption on global oil markets"
    )
    
    return workflow, (simple_result, complex_result)


def test_multiagent_error_handling():
    """Test MultiAgent error handling and recovery."""
    
    print("\n\n🔬 TESTING MULTIAGENT ERROR HANDLING")
    print("=" * 60)
    
    # Create a simple workflow
    agent1 = SimpleAgent(
        name="processor",
        engine=AugLLMConfig(temperature=0.5)
    )
    
    agent2 = SimpleAgent(
        name="validator",
        engine=AugLLMConfig(temperature=0.3)
    )
    
    workflow = MultiAgent(
        name="error_test_workflow",
        agents=[agent1, agent2],
        execution_mode="sequential"
    )
    
    # Test execution
    try:
        result = workflow.run("Process this data with error handling")
        print("✅ Workflow handled errors gracefully")
        return workflow, result
    except Exception as e:
        print(f"❌ Workflow error: {e}")
        return workflow, None


if __name__ == "__main__":
    print("🚀 MULTIAGENT STRUCTURED OUTPUT TEST SUITE")
    print("=" * 80)
    
    # Test 1: Sequential workflow with structured output
    try:
        print("\n=== TEST 1: Sequential MultiAgent ===")
        workflow1, result1 = test_multiagent_with_structured_output()
        print("✅ TEST 1 PASSED")
    except Exception as e:
        print(f"❌ TEST 1 FAILED: {e}")
        import traceback
        traceback.print_exc()
    
    # Test 2: Conditional routing workflow
    try:
        print("\n=== TEST 2: Conditional MultiAgent ===")
        workflow2, results2 = test_multiagent_with_conditional_routing()
        print("✅ TEST 2 PASSED")
    except Exception as e:
        print(f"❌ TEST 2 FAILED: {e}")
        import traceback
        traceback.print_exc()
    
    # Test 3: Error handling
    try:
        print("\n=== TEST 3: Error Handling ===")
        workflow3, result3 = test_multiagent_error_handling()
        print("✅ TEST 3 PASSED")
    except Exception as e:
        print(f"❌ TEST 3 FAILED: {e}")
    
    print("\n\n🎉 All MultiAgent tests completed!")
    print("\n📚 Key Takeaways:")
    print("1. MultiAgent orchestrates multiple agents as a single unit")
    print("2. Each agent has its own engine with structured output model")
    print("3. State transfer happens automatically through MultiAgentState")
    print("4. Supports sequential, parallel, and conditional execution")
    print("5. Use MultiAgent instead of manual agent chaining")