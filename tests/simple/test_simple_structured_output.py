"""Simple example of using SimpleAgent with structured output."""

import asyncio
from typing import List, Optional

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from haive.agents.simple.agent import SimpleAgent


# Define structured output models
class TaskItem(BaseModel):
    """A single task item."""

    task: str = Field(description="The task description")
    priority: str = Field(description="Priority level", pattern="^(high|medium|low)$")
    estimated_hours: float = Field(
        description="Estimated hours to complete", ge=0.5, le=40.0
    )
    assigned_to: Optional[str] = Field(
        default=None, description="Person assigned to the task"
    )


class ProjectPlan(BaseModel):
    """A structured project plan."""

    project_name: str = Field(description="Name of the project")
    objective: str = Field(description="Main project objective")
    tasks: List[TaskItem] = Field(
        description="List of tasks", min_items=3, max_items=10
    )
    timeline: str = Field(description="Overall timeline estimate")
    total_hours: float = Field(description="Total estimated hours")
    risks: List[str] = Field(description="Identified risks", min_items=1, max_items=5)
    success_criteria: List[str] = Field(description="Success criteria", min_items=2)


# Another example - Analysis Report
class FindingItem(BaseModel):
    """A single finding from analysis."""

    finding: str = Field(description="The finding description")
    impact: str = Field(
        description="Impact level", pattern="^(critical|high|medium|low)$"
    )
    evidence: str = Field(description="Supporting evidence")
    recommendation: str = Field(description="Recommended action")


class AnalysisReport(BaseModel):
    """Structured analysis report."""

    subject: str = Field(description="What was analyzed")
    summary: str = Field(description="Executive summary")
    findings: List[FindingItem] = Field(
        description="Key findings", min_items=2, max_items=8
    )
    conclusion: str = Field(description="Overall conclusion")
    next_steps: List[str] = Field(
        description="Recommended next steps", min_items=2, max_items=5
    )
    confidence_score: float = Field(
        description="Confidence in analysis", ge=0.0, le=1.0
    )


async def test_project_planning():
    """Test SimpleAgent with structured project plan output."""
    print("\n=== Project Planning with Structured Output ===\n")

    # Create prompt for project planning
    project_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are an expert project manager. Create detailed project plans with clear tasks, 
timelines, and risk assessments. Be specific and actionable in your planning.""",
            ),
            (
                "human",
                """Create a project plan for: {project_description}

Consider:
- Breaking down into specific tasks
- Realistic time estimates
- Potential risks
- Clear success criteria""",
            ),
        ]
    )

    # Create SimpleAgent with structured output
    planner = SimpleAgent(
        name="project_planner",
        engine=AugLLMConfig(
            prompt_template=project_prompt,
            structured_output_model=ProjectPlan,
            structured_output_version="v2",
            temperature=0.7,
        ),
    )

    # Run the agent
    result = await planner.arun(
        {
            "project_description": "Develop a mobile app for tracking personal fitness goals with social features"
        }
    )

    print("📋 Project Plan Generated:")
    print(f"Project: {result.project_name}")
    print(f"Objective: {result.objective}")
    print(f"\nTasks ({len(result.tasks)}):")
    for i, task in enumerate(result.tasks, 1):
        print(f"  {i}. {task.task}")
        print(f"     Priority: {task.priority}, Hours: {task.estimated_hours}")
        if task.assigned_to:
            print(f"     Assigned to: {task.assigned_to}")

    print(f"\nTimeline: {result.timeline}")
    print(f"Total Hours: {result.total_hours}")

    print("\nRisks:")
    for risk in result.risks:
        print(f"  • {risk}")

    print("\nSuccess Criteria:")
    for criteria in result.success_criteria:
        print(f"  ✓ {criteria}")


async def test_analysis_report():
    """Test SimpleAgent with structured analysis report."""
    print("\n\n=== Analysis Report with Structured Output ===\n")

    # Create analysis prompt
    analysis_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are a business analyst. Analyze situations and provide structured reports with 
clear findings, evidence, and actionable recommendations.""",
            ),
            (
                "human",
                """Analyze the following situation:

{situation}

Provide a comprehensive analysis with findings, impacts, and recommendations.""",
            ),
        ]
    )

    # Create SimpleAgent with structured output
    analyst = SimpleAgent(
        name="business_analyst",
        engine=AugLLMConfig(
            prompt_template=analysis_prompt,
            structured_output_model=AnalysisReport,
            structured_output_version="v2",
            temperature=0.5,  # Lower for more consistent analysis
        ),
    )

    # Run the analysis
    result = await analyst.arun(
        {
            "situation": """Our e-commerce website has seen a 30% drop in conversion rates over the past month. 
Page load times have increased by 2 seconds, mobile traffic has grown to 70% of total traffic, 
and customer support tickets about checkout issues have tripled."""
        }
    )

    print("📊 Analysis Report:")
    print(f"Subject: {result.subject}")
    print(f"\nSummary: {result.summary}")

    print(f"\nFindings ({len(result.findings)}):")
    for i, finding in enumerate(result.findings, 1):
        print(f"\n{i}. {finding.finding}")
        print(f"   Impact: {finding.impact}")
        print(f"   Evidence: {finding.evidence}")
        print(f"   Recommendation: {finding.recommendation}")

    print(f"\nConclusion: {result.conclusion}")

    print("\nNext Steps:")
    for step in result.next_steps:
        print(f"  → {step}")

    print(f"\nConfidence Score: {result.confidence_score:.2f}")


async def test_simple_list_output():
    """Test with a simple list-based output model."""
    print("\n\n=== Simple List Output ===\n")

    class IdeaList(BaseModel):
        """A list of ideas."""

        topic: str = Field(description="Topic for the ideas")
        ideas: List[str] = Field(
            description="List of creative ideas", min_items=5, max_items=10
        )
        best_idea: str = Field(description="The best idea from the list")

    # Simple prompt
    idea_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a creative idea generator."),
            ("human", "Generate creative ideas for: {topic}"),
        ]
    )

    # Create agent
    idea_agent = SimpleAgent(
        name="idea_generator",
        engine=AugLLMConfig(
            prompt_template=idea_prompt,
            structured_output_model=IdeaList,
            structured_output_version="v2",
        ),
    )

    # Generate ideas
    result = await idea_agent.arun(
        {"topic": "team building activities for remote workers"}
    )

    print(f"💡 Ideas for: {result.topic}")
    print(f"\nGenerated {len(result.ideas)} ideas:")
    for i, idea in enumerate(result.ideas, 1):
        print(f"  {i}. {idea}")
    print(f"\n⭐ Best idea: {result.best_idea}")


async def main():
    """Run all examples."""
    await test_project_planning()
    await test_analysis_report()
    await test_simple_list_output()


if __name__ == "__main__":
    asyncio.run(main())
