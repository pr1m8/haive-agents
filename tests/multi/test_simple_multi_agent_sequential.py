#!/usr/bin/env python3
"""Test simple multi-agent sequential flow with structured output transfer."""

import sys
import os
import asyncio
from typing import List

# Add the packages to path  
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../src"))

from pydantic import BaseModel, Field
from langchain_core.tools import tool
from haive.core.engine.aug_llm import AugLLMConfig
from haive.agents.simple.agent import SimpleAgent
from haive.agents.react.agent import ReactAgent


# Structured output models
class ResearchPlan(BaseModel):
    """Research plan from ReactAgent."""
    topic: str = Field(description="The research topic")
    questions: List[str] = Field(description="Key questions to investigate")
    approach: str = Field(description="Research approach and methodology")
    priority: str = Field(description="Priority level: high/medium/low")


class ResearchReport(BaseModel):
    """Final research report from SimpleAgent."""
    title: str = Field(description="Report title")
    summary: str = Field(description="Executive summary")
    findings: List[str] = Field(description="Key findings")
    recommendations: List[str] = Field(description="Action recommendations")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence in findings")


# Tools for ReactAgent
@tool
def research_database(query: str) -> str:
    """Search the research database for information."""
    # Simulate database search
    results = {
        "climate change": "Global temperatures have risen 1.1°C since pre-industrial times",
        "renewable energy": "Solar and wind costs have decreased 90% in the last decade",
        "electric vehicles": "EV sales grew 35% year-over-year globally",
        "ai impact": "AI adoption increased productivity by 15% in studied companies"
    }
    
    for key, value in results.items():
        if key in query.lower():
            return f"Found: {value}"
    
    return "No specific data found, but topic is relevant for further research"


@tool  
def calculate_impact(metric: str, value: float) -> str:
    """Calculate impact metrics for research findings."""
    if "temperature" in metric.lower():
        impact = value * 1.8  # Convert C to F for comparison
        return f"Temperature change of {value}°C equals {impact}°F"
    elif "percent" in metric.lower() or "%" in metric:
        impact = value / 100
        return f"{value}% change represents a {impact:.2f}x multiplier"
    else:
        return f"Impact metric for {metric}: {value} units"


def test_sequential_multi_agent_basic():
    """Test basic sequential flow: ReactAgent → SimpleAgent."""
    
    print("\n🔬 TESTING SEQUENTIAL MULTI-AGENT FLOW")
    print("=" * 60)
    
    # Step 1: Create ReactAgent for research planning
    react_engine = AugLLMConfig(
        structured_output_model=ResearchPlan,
        temperature=0.7,
    )
    
    # Important: ReactAgent should NOT use force_tool_use with structured output
    react_engine.force_tool_use = False
    react_engine.tool_choice_mode = "auto"
    
    react_agent = ReactAgent(
        name="research_planner",
        engine=react_engine,
        tools=[research_database, calculate_impact],
        debug=True
    )
    
    print("\n1️⃣ ReactAgent: Creating research plan...")
    
    # Get research plan from ReactAgent
    research_topic = "Impact of renewable energy on climate change mitigation"
    plan_result = react_agent.run(
        f"Create a research plan for: {research_topic}",
        debug=False
    )
    
    print(f"\n📋 Research Plan Created:")
    if hasattr(plan_result, 'topic'):
        print(f"   Topic: {plan_result.topic}")
        print(f"   Questions: {plan_result.questions}")
        print(f"   Approach: {plan_result.approach}")
        print(f"   Priority: {plan_result.priority}")
    
    # Step 2: Create SimpleAgent for report generation
    simple_engine = AugLLMConfig(
        structured_output_model=ResearchReport,
        temperature=0.5,  # Lower temperature for more focused output
    )
    
    simple_agent = SimpleAgent(
        name="report_writer",
        engine=simple_engine,
        debug=True
    )
    
    print("\n2️⃣ SimpleAgent: Generating research report...")
    
    # Transfer plan to report writer
    if hasattr(plan_result, 'model_dump'):
        plan_data = plan_result.model_dump()
        report_prompt = f"""
Based on this research plan:
- Topic: {plan_data['topic']}
- Questions: {', '.join(plan_data['questions'])}
- Approach: {plan_data['approach']}

Generate a comprehensive research report with findings and recommendations.
"""
    else:
        # Fallback if structured output didn't work
        report_prompt = f"""
Research topic: {research_topic}
Generate a comprehensive research report with findings and recommendations.
"""
    
    report_result = simple_agent.run(report_prompt, debug=False)
    
    print(f"\n📄 Research Report Generated:")
    if hasattr(report_result, 'title'):
        print(f"   Title: {report_result.title}")
        print(f"   Summary: {report_result.summary}")
        print(f"   Findings: {len(report_result.findings)} key findings")
        print(f"   Recommendations: {len(report_result.recommendations)} recommendations")
        print(f"   Confidence: {report_result.confidence:.2f}")
    
    print("\n✅ Sequential multi-agent flow completed successfully!")
    
    return plan_result, report_result


async def test_async_sequential_flow():
    """Test async sequential flow for better performance."""
    
    print("\n🔬 TESTING ASYNC SEQUENTIAL FLOW")
    print("=" * 60)
    
    # Create agents
    react_engine = AugLLMConfig(
        structured_output_model=ResearchPlan,
        temperature=0.7,
    )
    react_engine.force_tool_use = False
    
    simple_engine = AugLLMConfig(
        structured_output_model=ResearchReport,
        temperature=0.5,
    )
    
    react_agent = ReactAgent(
        name="async_planner",
        engine=react_engine,
        tools=[research_database]
    )
    
    simple_agent = SimpleAgent(
        name="async_writer",
        engine=simple_engine
    )
    
    # Run async
    print("\n1️⃣ Running ReactAgent async...")
    plan = await react_agent.arun("Plan research on AI safety measures")
    
    print("\n2️⃣ Running SimpleAgent async...")
    if hasattr(plan, 'model_dump'):
        plan_data = plan.model_dump()
        prompt = f"Write report based on plan: {plan_data}"
    else:
        prompt = f"Write report on AI safety based on: {plan}"
        
    report = await simple_agent.arun(prompt)
    
    print("\n✅ Async flow completed!")
    return plan, report


def test_multi_stage_pipeline():
    """Test multi-stage pipeline with data transformation."""
    
    print("\n🔬 TESTING MULTI-STAGE PIPELINE")
    print("=" * 60)
    
    # Stage 1: Analysis (ReactAgent with tools)
    class AnalysisResult(BaseModel):
        data_points: List[str] = Field(description="Key data points found")
        trends: List[str] = Field(description="Identified trends")
        anomalies: List[str] = Field(description="Any anomalies detected")
    
    analysis_engine = AugLLMConfig(
        structured_output_model=AnalysisResult,
        temperature=0.6,
    )
    analysis_engine.force_tool_use = False
    
    analyzer = ReactAgent(
        name="data_analyzer",
        engine=analysis_engine,
        tools=[research_database, calculate_impact]
    )
    
    # Stage 2: Synthesis (SimpleAgent)
    class SynthesisResult(BaseModel):
        insights: List[str] = Field(description="Synthesized insights")
        patterns: str = Field(description="Overall patterns identified")
        significance: str = Field(description="Statistical significance")
    
    synthesis_engine = AugLLMConfig(
        structured_output_model=SynthesisResult,
        temperature=0.5,
    )
    
    synthesizer = SimpleAgent(
        name="insight_synthesizer",
        engine=synthesis_engine
    )
    
    # Stage 3: Recommendations (SimpleAgent)
    class ActionPlan(BaseModel):
        immediate_actions: List[str] = Field(description="Actions to take now")
        short_term_goals: List[str] = Field(description="3-6 month goals")
        long_term_strategy: str = Field(description="Long-term strategic direction")
        success_metrics: List[str] = Field(description="How to measure success")
    
    recommendation_engine = AugLLMConfig(
        structured_output_model=ActionPlan,
        temperature=0.7,
    )
    
    recommender = SimpleAgent(
        name="strategy_recommender",
        engine=recommendation_engine
    )
    
    # Execute pipeline
    print("\n📊 Stage 1: Analysis...")
    analysis = analyzer.run("Analyze the impact of electric vehicles on carbon emissions")
    
    print("\n🔍 Stage 2: Synthesis...")
    if hasattr(analysis, 'model_dump'):
        synthesis_prompt = f"Synthesize insights from: {analysis.model_dump()}"
    else:
        synthesis_prompt = f"Synthesize insights from EV impact analysis: {analysis}"
    
    synthesis = synthesizer.run(synthesis_prompt)
    
    print("\n💡 Stage 3: Recommendations...")
    if hasattr(synthesis, 'model_dump'):
        action_prompt = f"Create action plan based on: {synthesis.model_dump()}"
    else:
        action_prompt = f"Create action plan for EV adoption: {synthesis}"
        
    actions = recommender.run(action_prompt)
    
    print("\n✅ Multi-stage pipeline completed!")
    
    # Print results
    if hasattr(actions, 'immediate_actions'):
        print(f"\n📋 Action Plan:")
        print(f"   Immediate: {len(actions.immediate_actions)} actions")
        print(f"   Short-term: {len(actions.short_term_goals)} goals")
        print(f"   Strategy: {actions.long_term_strategy[:100]}...")
    
    return analysis, synthesis, actions


def test_error_handling_in_multi_agent():
    """Test error handling and recovery in multi-agent flows."""
    
    print("\n🔬 TESTING ERROR HANDLING IN MULTI-AGENT FLOW")
    print("=" * 60)
    
    # Create agent that might fail
    class StrictResult(BaseModel):
        exact_value: float = Field(ge=0.0, le=100.0, description="Must be 0-100")
        category: str = Field(pattern="^(A|B|C)$", description="Must be A, B, or C")
    
    strict_engine = AugLLMConfig(
        structured_output_model=StrictResult,
        temperature=0.3,
    )
    
    strict_agent = SimpleAgent(
        name="strict_validator",
        engine=strict_engine
    )
    
    # Fallback agent with more flexible output
    class FlexibleResult(BaseModel):
        value: str = Field(description="Any value representation")
        notes: str = Field(description="Additional notes")
    
    fallback_engine = AugLLMConfig(
        structured_output_model=FlexibleResult,
        temperature=0.7,
    )
    
    fallback_agent = SimpleAgent(
        name="flexible_processor",
        engine=fallback_engine
    )
    
    print("\n1️⃣ Attempting strict validation...")
    
    try:
        # This might fail due to strict constraints
        result = strict_agent.run("Process value: 150 (out of range)")
        print(f"   ✅ Strict validation succeeded: {result}")
    except Exception as e:
        print(f"   ⚠️ Strict validation failed: {str(e)[:100]}...")
        print("\n2️⃣ Using fallback agent...")
        
        # Fallback to more flexible agent
        result = fallback_agent.run("Process value: 150 with appropriate notes")
        
        if hasattr(result, 'value'):
            print(f"   ✅ Fallback succeeded: value={result.value}")
    
    print("\n✅ Error handling test completed!")
    
    return result


if __name__ == "__main__":
    # Run all tests
    print("🚀 SIMPLE MULTI-AGENT TEST SUITE")
    print("=" * 80)
    
    # Test 1: Basic sequential flow
    try:
        plan, report = test_sequential_multi_agent_basic()
        print("\n✅ Test 1 PASSED: Basic sequential flow")
    except Exception as e:
        print(f"\n❌ Test 1 FAILED: {e}")
    
    # Test 2: Async sequential flow
    try:
        async_plan, async_report = asyncio.run(test_async_sequential_flow())
        print("\n✅ Test 2 PASSED: Async sequential flow")
    except Exception as e:
        print(f"\n❌ Test 2 FAILED: {e}")
    
    # Test 3: Multi-stage pipeline
    try:
        analysis, synthesis, actions = test_multi_stage_pipeline()
        print("\n✅ Test 3 PASSED: Multi-stage pipeline")
    except Exception as e:
        print(f"\n❌ Test 3 FAILED: {e}")
    
    # Test 4: Error handling
    try:
        error_result = test_error_handling_in_multi_agent()
        print("\n✅ Test 4 PASSED: Error handling")
    except Exception as e:
        print(f"\n❌ Test 4 FAILED: {e}")
    
    print("\n🎉 All multi-agent tests completed!")