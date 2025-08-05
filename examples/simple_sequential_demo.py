#!/usr/bin/env python3
"""Simple Sequential Multi-Agent Demo - Direct usage without patterns module.

This demo shows how to use the core agent classes directly:
- SimpleAgentV3
- ReactAgent
- EnhancedMultiAgentV4

With structured output and prompt templates as requested.
"""

import asyncio

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent_v3 import SimpleAgentV3


# Structured output models
class MarketAnalysis(BaseModel):
    """Structured analysis output from ReactAgent."""

    market_name: str = Field(description="Name of the market analyzed")
    market_size: str = Field(description="Current market size estimate")
    growth_rate: float = Field(description="Annual growth rate percentage", ge=0, le=100)
    key_players: list[str] = Field(description="Major companies in the market")
    opportunities: list[str] = Field(description="Market opportunities identified")
    challenges: list[str] = Field(description="Market challenges identified")


class ExecutiveSummary(BaseModel):
    """Final structured output from SimpleAgent."""

    title: str = Field(description="Report title")
    executive_summary: str = Field(description="Brief executive summary")
    key_findings: list[str] = Field(description="Top 3-5 key findings")
    recommendations: list[str] = Field(description="Strategic recommendations")
    next_steps: list[str] = Field(description="Immediate next steps")


async def demo_react_to_simple():
    """Demo: ReactAgent with tools → SimpleAgent with structured output."""

    # Create tools for ReactAgent
    @tool
    def market_research(query: str) -> str:
        """Research market information."""
        return f"Market research for '{query}': The global market is valued at $50B with 15% annual growth. Key players include TechCorp, InnovateCo, and FutureTech."

    @tool
    def competitor_analysis(company: str) -> str:
        """Analyze competitor information."""
        return f"Analysis of {company}: Strong in enterprise segment, 30% market share, investing heavily in R&D."

    # 1. ReactAgent for market analysis
    react_agent = ReactAgent(
        name="market_analyst",
        engine=AugLLMConfig(
            temperature=0.5,
            system_message="You are a market research analyst. Use tools to gather information and provide comprehensive analysis.",
            tools=[market_research, competitor_analysis],
        ),
    )

    # 2. SimpleAgent for structured summary with prompt template
    summary_agent = SimpleAgentV3(
        name="report_writer",
        engine=AugLLMConfig(
            temperature=0.3,
            system_message="You are an executive report writer. Create clear, actionable summaries.",
            structured_output_model=ExecutiveSummary,
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                (
                    "human",
                    """Based on this market analysis:
{analysis_content}

Create an executive summary with:
- Clear title
- Brief summary (2-3 sentences)
- Top 3-5 key findings
- Strategic recommendations
- Immediate next steps

Target audience: C-level executives""",
                ),
            ]
        ),
    )

    # 3. Create sequential workflow
    workflow = EnhancedMultiAgentV4(
        name="market_report_pipeline",
        agents=[react_agent, summary_agent],
        execution_mode="sequential",
    )

    # Execute workflow
    task = "Analyze the AI assistant market for enterprise customers"

    try:
        # Run the workflow
        result = await workflow.arun(
            {
                "messages": [{"role": "user", "content": task}],
                "analysis_content": "",  # Will be populated by react_agent output
            }
        )

        # Check if we have results from both agents
        if isinstance(result, dict):
            # ReactAgent results
            if "market_analyst" in result:
                analyst_result = result["market_analyst"]
                if isinstance(analyst_result, dict):
                    for _key, _value in analyst_result.items():
                        pass
                else:
                    pass

            # SimpleAgent structured output
            if "report_writer" in result:
                report = result["report_writer"]
                if isinstance(report, dict | ExecutiveSummary):
                    pass

    except Exception:
        import traceback

        traceback.print_exc()


async def demo_with_hooks():
    """Demo: Multi-agent workflow with hooks for monitoring."""
    # Create agents
    analyzer = SimpleAgentV3(
        name="analyzer",
        engine=AugLLMConfig(
            temperature=0.4,
            system_message="You are a data analyzer. Break down complex problems.",
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                ("human", "Analyze this request: {request}\nFocus on: {focus_areas}"),
            ]
        ),
    )

    planner = SimpleAgentV3(
        name="planner",
        engine=AugLLMConfig(
            temperature=0.5,
            system_message="You are a strategic planner. Create actionable plans.",
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                (
                    "human",
                    "Based on analysis: {analysis}\nCreate a plan with timeline: {timeline}",
                ),
            ]
        ),
    )

    reviewer = SimpleAgentV3(
        name="reviewer",
        engine=AugLLMConfig(
            temperature=0.3,
            system_message="You are a quality reviewer. Ensure plans are complete and practical.",
        ),
    )

    # Create workflow
    workflow = EnhancedMultiAgentV4(
        name="planning_pipeline",
        agents=[analyzer, planner, reviewer],
        execution_mode="sequential",
    )

    # Add hooks to monitor execution
    execution_log = []

    def log_pre_execution(agent_name: str, state: dict):
        """Pre-execution hook."""
        execution_log.append(f"[PRE] Starting {agent_name}")

    def log_post_execution(agent_name: str, result: any):
        """Post-execution hook."""
        execution_log.append(f"[POST] Completed {agent_name}")
        if isinstance(result, dict):
            pass
        else:
            pass

    # Note: Hook registration would typically be done through the agent's hook system
    # For this demo, we'll show the concept

    # Execute
    try:
        result = await workflow.arun(
            {
                "request": "Develop a customer retention strategy",
                "focus_areas": "engagement, loyalty programs, personalization",
                "timeline": "3 months",
                "messages": [{"role": "user", "content": "Create strategy"}],
            }
        )

        for _log_entry in execution_log:
            pass

        if isinstance(result, dict):
            for _agent_name, agent_result in result.items():
                if isinstance(agent_result, dict):
                    for _key, _value in list(agent_result.items())[:3]:
                        pass
                else:
                    pass

    except Exception:
        import traceback

        traceback.print_exc()


async def demo_structured_output_chain():
    """Demo: Chain of agents with structured output at each stage."""

    # Define structured models for each stage
    class ProblemDefinition(BaseModel):
        problem_statement: str = Field(description="Clear problem statement")
        stakeholders: list[str] = Field(description="Affected stakeholders")
        constraints: list[str] = Field(description="Known constraints")
        success_criteria: list[str] = Field(description="Success criteria")

    class Solution(BaseModel):
        solution_name: str = Field(description="Name of the solution")
        description: str = Field(description="Solution description")
        implementation_steps: list[str] = Field(description="Implementation steps")
        required_resources: list[str] = Field(description="Required resources")
        timeline_weeks: int = Field(description="Timeline in weeks", ge=1, le=52)

    # Create agents with structured output
    problem_agent = SimpleAgentV3(
        name="problem_definer",
        engine=AugLLMConfig(
            temperature=0.3,
            system_message="You are an expert at defining problems clearly.",
            structured_output_model=ProblemDefinition,
        ),
    )

    solution_agent = SimpleAgentV3(
        name="solution_designer",
        engine=AugLLMConfig(
            temperature=0.6,
            system_message="You are a creative solution designer.",
            structured_output_model=Solution,
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                (
                    "human",
                    """Design a solution for:
Problem: {problem_statement}
Stakeholders: {stakeholders}
Constraints: {constraints}
Success Criteria: {success_criteria}

Create a practical, implementable solution.""",
                ),
            ]
        ),
    )

    # Create workflow
    workflow = EnhancedMultiAgentV4(
        name="problem_solution_pipeline",
        agents=[problem_agent, solution_agent],
        execution_mode="sequential",
    )

    # Execute
    try:
        result = await workflow.arun(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": "Help reduce employee turnover in tech companies",
                    }
                ]
            }
        )

        if isinstance(result, dict):
            # Problem Definition
            if "problem_definer" in result:
                problem = result["problem_definer"]
                if isinstance(problem, dict):
                    pass

            # Solution
            if "solution_designer" in result:
                solution = result["solution_designer"]
                if isinstance(solution, dict):
                    pass

    except Exception:
        import traceback

        traceback.print_exc()


async def main():
    """Run all demos."""
    # Run demos
    await demo_react_to_simple()
    await demo_with_hooks()
    await demo_structured_output_chain()


if __name__ == "__main__":
    # Run with: poetry run python simple_sequential_demo.py
    asyncio.run(main())
