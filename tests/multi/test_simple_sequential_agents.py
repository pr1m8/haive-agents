#!/usr/bin/env python3
"""Simple test to verify multi-agent sequential execution works."""

import sys
import os

# Add the packages to path  
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../src"))

from pydantic import BaseModel, Field
from langchain_core.tools import tool
from haive.core.engine.aug_llm import AugLLMConfig
from haive.agents.simple.agent import SimpleAgent


class AnalysisResult(BaseModel):
    """Analysis result from first agent."""
    topic: str = Field(description="The analyzed topic")
    key_points: list[str] = Field(description="Key points identified")
    confidence: float = Field(ge=0.0, le=1.0, description="Analysis confidence")


class FinalReport(BaseModel):
    """Final report from second agent."""
    title: str = Field(description="Report title")
    summary: str = Field(description="Summary of findings")
    recommendations: list[str] = Field(description="Action recommendations")
    priority: str = Field(description="Priority level: high/medium/low")


def test_simple_sequential_agents():
    """Test SimpleAgent → SimpleAgent sequential flow."""
    
    print("\n🔬 SIMPLE SEQUENTIAL AGENTS TEST")
    print("=" * 50)
    
    # Agent 1: Analyzer
    analyzer_engine = AugLLMConfig(
        structured_output_model=AnalysisResult,
        temperature=0.7,
    )
    
    analyzer = SimpleAgent(
        name="analyzer",
        engine=analyzer_engine,
        debug=False
    )
    
    print("\n1️⃣ Running Analyzer Agent...")
    analysis = analyzer.run("Analyze the benefits of automated testing in software development")
    
    if hasattr(analysis, 'topic'):
        print(f"✅ Analysis completed:")
        print(f"   Topic: {analysis.topic}")
        print(f"   Points: {len(analysis.key_points)} key points")
        print(f"   Confidence: {analysis.confidence:.2f}")
    else:
        print(f"⚠️ Analysis returned: {analysis}")
    
    # Agent 2: Report Writer  
    writer_engine = AugLLMConfig(
        structured_output_model=FinalReport,
        temperature=0.5,
    )
    
    writer = SimpleAgent(
        name="report_writer",
        engine=writer_engine,
        debug=False
    )
    
    print("\n2️⃣ Running Report Writer Agent...")
    
    # Transfer data between agents
    if hasattr(analysis, 'model_dump'):
        analysis_data = analysis.model_dump()
        report_prompt = f"""
Based on this analysis:
- Topic: {analysis_data['topic']}
- Key Points: {', '.join(analysis_data['key_points'][:3])}
- Confidence: {analysis_data['confidence']}

Create a final report with recommendations.
"""
    else:
        report_prompt = f"Create a report based on: {analysis}"
    
    report = writer.run(report_prompt)
    
    if hasattr(report, 'title'):
        print(f"✅ Report completed:")
        print(f"   Title: {report.title}")
        print(f"   Summary: {report.summary[:100]}...")
        print(f"   Recommendations: {len(report.recommendations)}")
        print(f"   Priority: {report.priority}")
    else:
        print(f"⚠️ Report returned: {report}")
    
    print("\n✅ Sequential execution completed!")
    return analysis, report


def test_three_agent_pipeline():
    """Test three agents in sequence."""
    
    print("\n🔬 THREE AGENT PIPELINE TEST")
    print("=" * 50)
    
    # Define output models
    class Research(BaseModel):
        findings: list[str] = Field(description="Research findings")
        sources: int = Field(description="Number of sources consulted")
    
    class Analysis(BaseModel):
        insights: list[str] = Field(description="Key insights")
        trend: str = Field(description="Overall trend identified")
    
    class Decision(BaseModel):
        recommendation: str = Field(description="Final recommendation")
        rationale: str = Field(description="Decision rationale")
        confidence: float = Field(ge=0.0, le=1.0)
    
    # Create three agents
    researcher = SimpleAgent(
        name="researcher",
        engine=AugLLMConfig(structured_output_model=Research, temperature=0.7)
    )
    
    analyst = SimpleAgent(
        name="analyst", 
        engine=AugLLMConfig(structured_output_model=Analysis, temperature=0.6)
    )
    
    decider = SimpleAgent(
        name="decider",
        engine=AugLLMConfig(structured_output_model=Decision, temperature=0.4)
    )
    
    # Execute pipeline
    print("\n1️⃣ Researching...")
    research = researcher.run("Research current trends in AI automation")
    
    print("\n2️⃣ Analyzing...")
    if hasattr(research, 'findings'):
        analysis_prompt = f"Analyze these findings: {research.findings[:2]}"
    else:
        analysis_prompt = f"Analyze: {research}"
    analysis = analyst.run(analysis_prompt)
    
    print("\n3️⃣ Deciding...")
    if hasattr(analysis, 'insights'):
        decision_prompt = f"Make recommendation based on insights: {analysis.insights[:2]}"
    else:
        decision_prompt = f"Make recommendation based on: {analysis}"
    decision = decider.run(decision_prompt)
    
    if hasattr(decision, 'recommendation'):
        print(f"\n✅ Final Decision:")
        print(f"   Recommendation: {decision.recommendation}")
        print(f"   Confidence: {decision.confidence:.2f}")
    
    print("\n✅ Three-agent pipeline completed!")
    return research, analysis, decision


def test_data_transformation_flow():
    """Test data transformation between agents."""
    
    print("\n🔬 DATA TRANSFORMATION FLOW TEST")
    print("=" * 50)
    
    # Raw data model
    class RawData(BaseModel):
        values: list[float] = Field(description="Raw numerical values")
        unit: str = Field(description="Unit of measurement")
    
    # Processed data model
    class ProcessedData(BaseModel):
        mean: float = Field(description="Average value")
        max_value: float = Field(description="Maximum value")
        min_value: float = Field(description="Minimum value")
        unit: str = Field(description="Unit of measurement")
    
    # Summary model
    class DataSummary(BaseModel):
        interpretation: str = Field(description="Data interpretation")
        significance: str = Field(description="Statistical significance")
        action_needed: bool = Field(description="Whether action is needed")
    
    # Create agents
    collector = SimpleAgent(
        name="data_collector",
        engine=AugLLMConfig(structured_output_model=RawData, temperature=0.3)
    )
    
    processor = SimpleAgent(
        name="data_processor",
        engine=AugLLMConfig(structured_output_model=ProcessedData, temperature=0.2)
    )
    
    interpreter = SimpleAgent(
        name="data_interpreter",
        engine=AugLLMConfig(structured_output_model=DataSummary, temperature=0.5)
    )
    
    # Execute flow
    print("\n1️⃣ Collecting data...")
    raw = collector.run("Collect temperature readings for the last week in Celsius")
    
    print("\n2️⃣ Processing data...")
    if hasattr(raw, 'values') and hasattr(raw, 'unit'):
        process_prompt = f"Process these values: {raw.values}, unit: {raw.unit}"
    else:
        process_prompt = f"Process data: {raw}"
    processed = processor.run(process_prompt)
    
    print("\n3️⃣ Interpreting results...")
    if hasattr(processed, 'mean'):
        interpret_prompt = f"Interpret: mean={processed.mean}, max={processed.max_value}, min={processed.min_value} {processed.unit}"
    else:
        interpret_prompt = f"Interpret: {processed}"
    summary = interpreter.run(interpret_prompt)
    
    if hasattr(summary, 'interpretation'):
        print(f"\n✅ Data Analysis Complete:")
        print(f"   Interpretation: {summary.interpretation}")
        print(f"   Action needed: {summary.action_needed}")
    
    print("\n✅ Data transformation flow completed!")
    return raw, processed, summary


if __name__ == "__main__":
    print("🚀 SIMPLE SEQUENTIAL AGENTS TEST SUITE")
    print("=" * 70)
    
    # Test 1: Two agents
    try:
        print("\n=== TEST 1: Two Agent Sequential ===")
        analysis, report = test_simple_sequential_agents()
        print("✅ TEST 1 PASSED")
    except Exception as e:
        print(f"❌ TEST 1 FAILED: {e}")
    
    # Test 2: Three agents
    try:
        print("\n=== TEST 2: Three Agent Pipeline ===")
        research, analysis, decision = test_three_agent_pipeline()
        print("✅ TEST 2 PASSED")
    except Exception as e:
        print(f"❌ TEST 2 FAILED: {e}")
    
    # Test 3: Data transformation
    try:
        print("\n=== TEST 3: Data Transformation ===")
        raw, processed, summary = test_data_transformation_flow()
        print("✅ TEST 3 PASSED")
    except Exception as e:
        print(f"❌ TEST 3 FAILED: {e}")
    
    print("\n🎉 All tests completed!")