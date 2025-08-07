"""Complex Data Flow Example

This example demonstrates a sophisticated multi-agent workflow where
data flows through structured outputs, enabling each agent to build
upon the previous agent's work. Similar to the Self-Discover pattern.

Date: August 7, 2025
"""

import asyncio
from typing import Any, Dict, List, Optional

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.react.agent_v4 import ReactAgentV4
from haive.agents.simple.agent_v3 import SimpleAgentV3


# Define structured outputs for each stage
class ResearchPhase(BaseModel):
    """Research phase output."""

    research_questions: List[str] = Field(description="Key questions to investigate")
    data_sources: List[str] = Field(description="Identified data sources")
    initial_findings: Dict[str, str] = Field(
        description="Initial findings per question"
    )
    confidence_scores: Dict[str, float] = Field(description="Confidence per finding")


class AnalysisPhase(BaseModel):
    """Analysis phase output building on research."""

    key_insights: List[str] = Field(description="Primary insights from research")
    data_patterns: Dict[str, Any] = Field(description="Identified patterns in data")
    statistical_summary: Dict[str, float] = Field(description="Statistical measures")
    correlations: List[Dict[str, Any]] = Field(description="Identified correlations")
    analysis_quality: float = Field(
        ge=0.0, le=1.0, description="Analysis quality score"
    )


class StrategyPhase(BaseModel):
    """Strategy phase building on analysis."""

    strategic_goals: List[str] = Field(description="Strategic goals based on insights")
    action_items: List[Dict[str, str]] = Field(description="Specific action items")
    risk_factors: List[str] = Field(description="Identified risks")
    success_metrics: Dict[str, str] = Field(description="KPIs for each goal")
    implementation_timeline: List[Dict[str, Any]] = Field(
        description="Timeline with milestones"
    )


class ValidationPhase(BaseModel):
    """Validation phase checking the strategy."""

    feasibility_score: float = Field(ge=0.0, le=1.0, description="Overall feasibility")
    validated_actions: List[str] = Field(description="Validated action items")
    concerns: List[str] = Field(description="Validation concerns")
    recommendations: List[str] = Field(description="Improvement recommendations")
    final_approval: bool = Field(description="Final approval status")


class ExecutiveSummary(BaseModel):
    """Final executive summary combining all phases."""

    executive_brief: str = Field(description="One paragraph executive summary")
    key_decisions: List[str] = Field(description="Key decisions to make")
    expected_outcomes: List[str] = Field(description="Expected outcomes")
    resource_requirements: Dict[str, Any] = Field(description="Required resources")
    next_steps: List[str] = Field(description="Immediate next steps")
    confidence_level: float = Field(ge=0.0, le=1.0, description="Overall confidence")


# Research tools
@tool
def search_market_data(query: str) -> str:
    """Search market data and trends."""
    # Mock market data
    market_data = {
        "ai": "AI market growing 35% YoY, $150B by 2025",
        "cloud": "Cloud adoption at 85% enterprises, $500B market",
        "security": "Cybersecurity spending up 12% YoY, critical priority",
    }
    query_lower = query.lower()
    relevant = [v for k, v in market_data.items() if k in query_lower]
    return f"Market data: {'; '.join(relevant) if relevant else 'General market growing 8% YoY'}"


@tool
def analyze_competitors(industry: str) -> str:
    """Analyze competitor landscape."""
    return f"Top 3 competitors in {industry}: Leader (35% share), Challenger (25% share), Innovator (15% share)"


# Analysis tools
@tool
def calculate_metrics(data_points: str) -> str:
    """Calculate statistical metrics from comma-separated values."""
    try:
        values = [float(x.strip()) for x in data_points.split(",")]
        if not values:
            return "No data provided"

        mean = sum(values) / len(values)
        growth = ((values[-1] - values[0]) / values[0] * 100) if len(values) > 1 else 0

        return f"Metrics: Mean={mean:.2f}, Growth={growth:.1f}%, Trend={'up' if growth > 0 else 'down'}"
    except:
        return "Invalid data format"


@tool
def identify_patterns(description: str) -> str:
    """Identify patterns in described data."""
    patterns = [
        "seasonal variation",
        "upward trend",
        "cyclic behavior",
        "correlation detected",
    ]
    return f"Pattern analysis: {patterns[hash(description) % len(patterns)]} observed"


# Strategy tools
@tool
def prioritize_actions(actions: str) -> str:
    """Prioritize list of actions."""
    action_list = actions.split(",")
    prioritized = sorted(action_list, key=lambda x: len(x.strip()))
    return f"Priority order: {' > '.join([a.strip() for a in prioritized[:3]])}"


@tool
def estimate_timeline(project_scope: str) -> str:
    """Estimate project timeline."""
    if "small" in project_scope.lower():
        return "Timeline: 2-3 months (Planning: 2 weeks, Execution: 6 weeks, Review: 2 weeks)"
    elif "large" in project_scope.lower():
        return "Timeline: 6-9 months (Planning: 1 month, Execution: 5 months, Review: 1 month)"
    else:
        return "Timeline: 3-6 months (Planning: 3 weeks, Execution: 3 months, Review: 3 weeks)"


async def main():
    """Run the complex data flow workflow."""

    print("Creating multi-stage workflow agents...")

    # Create research agent with tools
    researcher = ReactAgentV4(
        name="researcher",
        engine=AugLLMConfig(
            temperature=0.4,
            system_message="You are a research specialist. Investigate thoroughly using available tools.",
        ),
        tools=[search_market_data, analyze_competitors],
        structured_output_model=ResearchPhase,
        debug=True,
    )

    # Create analysis agent with tools and access to research
    analyst = ReactAgentV4(
        name="analyst",
        engine=AugLLMConfig(
            temperature=0.3,
            system_message="You are a data analyst. Analyze the research findings to extract insights.",
        ),
        tools=[calculate_metrics, identify_patterns],
        structured_output_model=AnalysisPhase,
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "Analyze the research findings and identify key insights."),
                (
                    "human",
                    """Based on this research:
Questions investigated: {researcher.research_questions}
Initial findings: {researcher.initial_findings}
Confidence scores: {researcher.confidence_scores}

Perform deep analysis and identify patterns, correlations, and insights.""",
                ),
            ]
        ),
        debug=True,
    )

    # Create strategy agent with tools and access to both research and analysis
    strategist = ReactAgentV4(
        name="strategist",
        engine=AugLLMConfig(
            temperature=0.5,
            system_message="You are a strategic planner. Develop actionable strategies based on insights.",
        ),
        tools=[prioritize_actions, estimate_timeline],
        structured_output_model=StrategyPhase,
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "Develop strategic plans based on research and analysis."),
                (
                    "human",
                    """Based on:
Key insights: {analyst.key_insights}
Data patterns: {analyst.data_patterns}
Statistical summary: {analyst.statistical_summary}
Analysis quality: {analyst.analysis_quality}

Develop a comprehensive strategy with goals, actions, and timeline.""",
                ),
            ]
        ),
        debug=True,
    )

    # Create validation agent (no tools, pure reasoning)
    validator = SimpleAgentV3(
        name="validator",
        engine=AugLLMConfig(
            temperature=0.2,
            system_message="You are a strategy validator. Critically evaluate proposed strategies.",
        ),
        structured_output_model=ValidationPhase,
        prompt_template=ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "Validate the proposed strategy for feasibility and completeness.",
                ),
                (
                    "human",
                    """Validate this strategy:
Goals: {strategist.strategic_goals}
Actions: {strategist.action_items}
Risks: {strategist.risk_factors}
Timeline: {strategist.implementation_timeline}

Consider feasibility, risks, and completeness.""",
                ),
            ]
        ),
        debug=True,
    )

    # Create executive summary agent with access to all previous outputs
    summarizer = SimpleAgentV3(
        name="summarizer",
        engine=AugLLMConfig(
            temperature=0.4,
            system_message="You are an executive communication expert. Create concise executive summaries.",
        ),
        structured_output_model=ExecutiveSummary,
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "Create an executive summary of the entire analysis."),
                (
                    "human",
                    """Synthesize into executive summary:

Research findings: {researcher.initial_findings}
Key insights: {analyst.key_insights}
Strategic goals: {strategist.strategic_goals}
Validation results: Feasibility {validator.feasibility_score}, Approved: {validator.final_approval}
Main concerns: {validator.concerns}

Create a concise executive summary with key decisions and next steps.""",
                ),
            ]
        ),
        debug=True,
    )

    # Create the workflow
    print("\nCreating complex data flow workflow...")
    workflow = EnhancedMultiAgentV4(
        name="strategic_planning_pipeline",
        agents=[researcher, analyst, strategist, validator, summarizer],
        execution_mode="sequential",
    )

    # Test scenario
    scenario = """
    Analyze the opportunity for launching a new AI-powered productivity tool for remote teams.
    Consider market conditions, competition, and implementation strategy.
    """

    print(f"\nScenario: {scenario.strip()}")
    print("\nExecuting multi-stage workflow...\n")

    # Execute workflow
    start_time = asyncio.get_event_loop().time()
    result = await workflow.arun({"messages": [HumanMessage(content=scenario)]})
    execution_time = asyncio.get_event_loop().time() - start_time

    # Display results from each phase
    print("\n" + "=" * 60)
    print("WORKFLOW RESULTS - DATA FLOW VISUALIZATION")
    print("=" * 60)

    # Research Phase
    if hasattr(workflow.state, "researcher"):
        research = workflow.state.researcher
        print("\n📚 [1. RESEARCH PHASE]")
        print(f"Questions investigated: {len(research.research_questions)}")
        for q in research.research_questions[:3]:
            print(f"  • {q}")
        print(f"Data sources: {', '.join(research.data_sources[:3])}")
        print(f"Findings: {len(research.initial_findings)} key findings")

    # Analysis Phase
    if hasattr(workflow.state, "analyst"):
        analysis = workflow.state.analyst
        print("\n📊 [2. ANALYSIS PHASE] ← builds on Research")
        print(f"Key insights: {len(analysis.key_insights)}")
        for insight in analysis.key_insights[:3]:
            print(f"  • {insight}")
        print(f"Patterns identified: {len(analysis.data_patterns)}")
        print(f"Analysis quality: {analysis.analysis_quality:.0%}")

    # Strategy Phase
    if hasattr(workflow.state, "strategist"):
        strategy = workflow.state.strategist
        print("\n🎯 [3. STRATEGY PHASE] ← builds on Analysis")
        print(f"Strategic goals: {len(strategy.strategic_goals)}")
        for goal in strategy.strategic_goals[:3]:
            print(f"  • {goal}")
        print(f"Action items: {len(strategy.action_items)}")
        print(f"Risk factors: {len(strategy.risk_factors)}")

    # Validation Phase
    if hasattr(workflow.state, "validator"):
        validation = workflow.state.validator
        print("\n✅ [4. VALIDATION PHASE] ← validates Strategy")
        print(f"Feasibility score: {validation.feasibility_score:.0%}")
        print(f"Validated actions: {len(validation.validated_actions)}")
        print(f"Concerns raised: {len(validation.concerns)}")
        if validation.concerns:
            print("  Top concerns:")
            for concern in validation.concerns[:2]:
                print(f"    ⚠️  {concern}")
        print(
            f"Final approval: {'✅ APPROVED' if validation.final_approval else '❌ NOT APPROVED'}"
        )

    # Executive Summary
    if hasattr(workflow.state, "summarizer"):
        summary = workflow.state.summarizer
        print("\n📋 [5. EXECUTIVE SUMMARY] ← synthesizes all phases")
        print(f"\nExecutive Brief:")
        print(f"  {summary.executive_brief}")
        print(f"\nKey Decisions Required:")
        for decision in summary.key_decisions[:3]:
            print(f"  □ {decision}")
        print(f"\nNext Steps:")
        for step in summary.next_steps[:3]:
            print(f"  → {step}")
        print(f"\nOverall Confidence: {summary.confidence_level:.0%}")

    # Show data flow
    print("\n" + "=" * 60)
    print("DATA FLOW TRACKING")
    print("=" * 60)
    print("Each agent accessed previous agents' structured outputs:")
    print("  researcher → (research_questions, findings, confidence)")
    print("       ↓")
    print("  analyst → (insights, patterns, statistics)")
    print("       ↓")
    print("  strategist → (goals, actions, timeline)")
    print("       ↓")
    print("  validator → (feasibility, concerns, approval)")
    print("       ↓")
    print("  summarizer → (executive summary, decisions, next steps)")

    # Performance and tools
    print(f"\n" + "=" * 60)
    print("EXECUTION METRICS")
    print(f"=" * 60)
    print(f"Total execution time: {execution_time:.2f}s")
    print(f"Agents executed: {len(workflow.state.agent_execution_order)}")
    print(f"Execution order: {' → '.join(workflow.state.agent_execution_order)}")

    # Tool usage verification
    print(f"\n" + "=" * 60)
    print("TOOL ISOLATION")
    print(f"=" * 60)
    print(f"Researcher tools: {[t.name for t in researcher.tools]}")
    print(f"Analyst tools: {[t.name for t in analyst.tools]}")
    print(f"Strategist tools: {[t.name for t in strategist.tools]}")
    print(f"Validator tools: {validator.tools}")  # Should be empty
    print(f"Summarizer tools: {summarizer.tools}")  # Should be empty
    print("✓ Each agent has only its specialized tools")


if __name__ == "__main__":
    print("Complex Data Flow Example")
    print("========================\n")
    asyncio.run(main())
