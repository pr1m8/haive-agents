#!/usr/bin/env python3
"""Advanced example of Dynamic Supervisor V2.

This example demonstrates:
- Structured output with agents
- Custom discovery configuration
- Agent lifecycle management
- Complex multi-step workflows
- Error handling and recovery
"""

import asyncio
import logging
from datetime import datetime

from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.dynamic_supervisor_v2 import (
    AgentDiscoveryMode,
    AgentSpec,
    DiscoveryConfig,
    DynamicSupervisor,
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


# Define structured output models
class ResearchResult(BaseModel):
    """Structured output for research tasks."""

    topic: str = Field(description="Research topic")
    summary: str = Field(description="Executive summary")
    key_findings: list[str] = Field(description="Key findings list")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence score")
    sources: list[str] = Field(default_factory=list, description="Information sources")


class ProjectPlan(BaseModel):
    """Structured output for project planning."""

    project_name: str = Field(description="Project name")
    objectives: list[str] = Field(description="Project objectives")
    phases: list[str] = Field(description="Project phases")
    timeline: str = Field(description="Estimated timeline")
    risks: list[str] = Field(description="Identified risks")
    success_criteria: list[str] = Field(description="Success criteria")


class CodeReview(BaseModel):
    """Structured output for code reviews."""

    overall_quality: str = Field(description="Overall code quality assessment")
    strengths: list[str] = Field(description="Code strengths")
    issues: list[str] = Field(description="Identified issues")
    suggestions: list[str] = Field(description="Improvement suggestions")
    security_concerns: list[str] = Field(default_factory=list)
    score: int = Field(ge=1, le=10, description="Quality score")


# Define advanced tools
@tool
def advanced_search(query: str, sources: list[str] = None) -> str:
    """Advanced search with source filtering."""
    sources = sources or ["web", "academic", "news"]
    return f"""Search results for '{query}' from {', '.join(sources)}:
    
1. Recent breakthrough in {query} technology (Nature, 2025)
2. Industry report on {query} market trends (Gartner, 2025)
3. {query} implementation best practices (IEEE, 2024)
4. Future of {query}: Expert predictions (MIT Tech Review, 2025)
"""


@tool
def code_analyzer(code: str, language: str = "python") -> str:
    """Analyze code for quality and security issues."""
    lines = code.strip().split("\n")
    return f"""Code Analysis Report:

Language: {language}
Lines of code: {len(lines)}
Complexity: Medium

Issues found:
- Line 3: Consider using type hints
- Line 7: Potential SQL injection vulnerability
- Line 12: Function exceeds recommended length

Security scan: 1 high, 2 medium issues
Performance: Could benefit from caching
"""


@tool
def project_tracker(action: str, project_name: str, data: str = "") -> str:
    """Track project progress and milestones."""
    timestamp = datetime.now().isoformat()

    if action == "create":
        return f"Project '{project_name}' created at {timestamp}"
    if action == "update":
        return f"Project '{project_name}' updated: {data}"
    if action == "status":
        return f"""Project '{project_name}' Status:
- Phase: Implementation
- Progress: 65%
- Next milestone: Beta release
- Days remaining: 15
"""
    return f"Unknown action: {action}"


def create_advanced_specs() -> list[AgentSpec]:
    """Create advanced agent specifications."""
    return [
        AgentSpec(
            name="senior_researcher",
            agent_type="ReactAgent",
            description="Senior research analyst with structured output",
            specialties=["research", "analysis", "synthesis", "academic"],
            tools=[advanced_search],
            config={
                "temperature": 0.4,
                "system_message": (
                    "You are a senior research analyst. Provide comprehensive, "
                    "well-structured research with proper citations."
                ),
                "structured_output_model": ResearchResult,
            },
            priority=20,
        ),
        AgentSpec(
            name="project_manager",
            agent_type="ReactAgent",
            description="Project planning and management expert",
            specialties=["project", "planning", "management", "timeline", "risk"],
            tools=[project_tracker],
            config={
                "temperature": 0.3,
                "system_message": (
                    "You are an experienced project manager. Create detailed, "
                    "actionable project plans with clear objectives and timelines."
                ),
                "structured_output_model": ProjectPlan,
            },
            priority=15,
        ),
        AgentSpec(
            name="code_reviewer",
            agent_type="ReactAgent",
            description="Expert code reviewer and security analyst",
            specialties=["code", "review", "security", "quality", "programming"],
            tools=[code_analyzer],
            config={
                "temperature": 0.2,
                "system_message": (
                    "You are an expert code reviewer. Focus on code quality, "
                    "security vulnerabilities, and best practices."
                ),
                "structured_output_model": CodeReview,
            },
            priority=15,
        ),
        AgentSpec(
            name="technical_writer",
            agent_type="SimpleAgentV3",
            description="Technical documentation specialist",
            specialties=["documentation", "technical", "writing", "api", "guide"],
            config={
                "temperature": 0.6,
                "system_message": (
                    "You are a technical writer. Create clear, comprehensive "
                    "documentation with examples and best practices."
                ),
            },
        ),
    ]


class WorkflowOrchestrator:
    """Orchestrate complex multi-agent workflows."""

    def __init__(self, supervisor: DynamicSupervisor):
        self.supervisor = supervisor

    async def research_and_plan_workflow(self, topic: str) -> dict:
        """Execute a research and planning workflow."""
        logger.info(f"Starting research and plan workflow for: {topic}")

        # Step 1: Research
        research_task = f"Research the current state and future trends of {topic}"
        research_result = await self.supervisor.arun(research_task)

        # Step 2: Project Planning
        plan_task = f"""Create a project plan for implementing a {topic} solution
        based on the research findings: {research_result}"""
        project_plan = await self.supervisor.arun(plan_task)

        # Step 3: Documentation
        doc_task = f"""Write technical documentation for the {topic} project
        based on the plan: {project_plan}"""
        documentation = await self.supervisor.arun(doc_task)

        return {
            "research": research_result,
            "plan": project_plan,
            "documentation": documentation,
        }

    async def code_review_workflow(self, code: str) -> dict:
        """Execute a code review workflow."""
        logger.info("Starting code review workflow")

        # Step 1: Code Review
        review_task = f"Review this code:\n```python\n{code}\n```"
        review_result = await self.supervisor.arun(review_task)

        # Step 2: Documentation
        doc_task = f"""Write documentation for the reviewed code
        considering the review findings: {review_result}"""
        documentation = await self.supervisor.arun(doc_task)

        return {
            "review": review_result,
            "documentation": documentation,
        }


async def demonstrate_lifecycle_management(supervisor: DynamicSupervisor):
    """Demonstrate agent lifecycle management."""
    print("\n" + "-" * 60)
    print("Agent Lifecycle Management Demo")
    print("-" * 60 + "\n")

    # Initial state
    initial_agents = len(supervisor._state["active_agents"])
    print(f"Initial active agents: {initial_agents}")

    # Force creation of multiple agents
    tasks = [
        "Research quantum computing applications",
        "Create a project plan for AI deployment",
        "Review this code: def hello(): print('world')",
        "Write API documentation for REST endpoints",
    ]

    for task in tasks:
        print(f"\nProcessing: {task[:50]}...")
        await supervisor.arun(task)

    # Check agent creation
    final_agents = len(supervisor._state["active_agents"])
    print(f"\nFinal active agents: {final_agents}")
    print(f"Agents created: {final_agents - initial_agents}")

    # Display agent states
    print("\nAgent States:")
    for name, agent in supervisor._state["active_agents"].items():
        print(f"  - {name}: {agent.state} (tasks: {agent.task_count})")


async def main():
    """Run the advanced example."""
    print("\n" + "=" * 60)
    print("Dynamic Supervisor V2 - Advanced Example")
    print("=" * 60 + "\n")

    # Create advanced configuration
    discovery_config = DiscoveryConfig(
        mode=AgentDiscoveryMode.MANUAL,
        cache_discoveries=True,
        discovery_timeout=30.0,
        max_discoveries_per_request=3,
    )

    # Create supervisor with advanced specs
    supervisor = DynamicSupervisor(
        name="advanced_coordinator",
        agent_specs=create_advanced_specs(),
        discovery_config=discovery_config,
        max_agents=15,
        auto_discover=True,
        include_management_tools=True,
    )

    print("✅ Advanced Dynamic Supervisor created\n")

    # Test structured output
    print("Testing Structured Output:")
    print("-" * 40)

    research_result = await supervisor.arun(
        "Research the impact of artificial intelligence on healthcare"
    )
    print(f"Research Result Type: {type(research_result).__name__}")
    if isinstance(research_result, ResearchResult):
        print(f"Topic: {research_result.topic}")
        print(f"Confidence: {research_result.confidence}")
        print(f"Key Findings: {len(research_result.key_findings)}")
    print()

    # Run workflow orchestration
    orchestrator = WorkflowOrchestrator(supervisor)

    print("\nExecuting Research and Plan Workflow:")
    print("=" * 40)

    workflow_result = await orchestrator.research_and_plan_workflow(
        "blockchain in supply chain"
    )

    for step, result in workflow_result.items():
        print(f"\n{step.title()} Result:")
        print("-" * 20)
        if isinstance(result, BaseModel):
            print(f"Structured output: {type(result).__name__}")
        else:
            print(f"Output preview: {str(result)[:200]}...")

    # Demonstrate lifecycle management
    await demonstrate_lifecycle_management(supervisor)

    # Final metrics
    print("\n" + "=" * 60)
    print("Final Performance Report")
    print("=" * 60 + "\n")

    metrics = supervisor.get_metrics()
    sup_metrics = metrics["supervisor"]

    print("Supervisor Performance:")
    print(f"  Total tasks: {sup_metrics['total_tasks']}")
    print(f"  Success rate: {sup_metrics['success_rate']:.1%}")
    print(f"  Discovery success: {sup_metrics['discovery_success_rate']:.1%}")
    print(f"  Total execution time: {sup_metrics['total_execution_time']:.2f}s")
    print(f"  Agent creations: {sup_metrics['agent_creations']}")

    print("\nTop Performing Agents:")
    sorted_agents = sorted(
        metrics["agents"].items(),
        key=lambda x: x[1]["task_count"],
        reverse=True,
    )

    for agent_name, stats in sorted_agents[:3]:
        print(f"\n  {agent_name}:")
        print(f"    Tasks: {stats['task_count']}")
        print(f"    Success rate: {stats['success_rate']:.1%}")
        print(f"    Avg time: {stats['avg_execution_time']:.2f}s")

    print("\n" + "=" * 60)
    print("Advanced example completed!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    asyncio.run(main())
