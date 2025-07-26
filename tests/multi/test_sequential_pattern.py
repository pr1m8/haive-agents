"""Test sequential agent pattern with structured output."""

import asyncio
from datetime import datetime
from typing import List, Optional

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.patterns.sequential_with_structured_output import (
    SequentialAgentWithStructuredOutput,
    SequentialHooks,
    create_analysis_to_report,
    create_react_to_structured,
)
from haive.agents.simple.agent import SimpleAgent


# Example 1: React → Structured Research Report
class ResearchSource(BaseModel):
    """A source used in research."""

    title: str = Field(description="Source title or name")
    url: Optional[str] = Field(default=None, description="Source URL if available")
    relevance: float = Field(description="Relevance score 0-1", ge=0, le=1)
    key_points: List[str] = Field(description="Key points from this source")


class ResearchReport(BaseModel):
    """Structured research report output."""

    topic: str = Field(description="Research topic")
    executive_summary: str = Field(description="Brief executive summary")

    key_findings: List[str] = Field(
        description="Main findings from the research", min_items=3, max_items=10
    )

    sources: List[ResearchSource] = Field(description="Sources used in the research")

    methodology: str = Field(description="Research methodology used")

    limitations: Optional[List[str]] = Field(
        default=None, description="Research limitations or caveats"
    )

    recommendations: List[str] = Field(description="Recommendations based on findings")

    confidence_level: str = Field(
        description="Overall confidence in findings", pattern="^(high|medium|low)$"
    )

    timestamp: datetime = Field(
        default_factory=datetime.now, description="When research was completed"
    )


# Example 2: Analysis → Business Report
class MarketAnalysis(BaseModel):
    """Market analysis structure."""

    segment: str = Field(description="Market segment analyzed")
    size: str = Field(description="Market size estimate")
    growth_rate: str = Field(description="Growth rate projection")
    key_players: List[str] = Field(description="Major players in the market")


class BusinessReport(BaseModel):
    """Structured business report."""

    title: str = Field(description="Report title")
    executive_summary: str = Field(description="Executive summary")

    market_analysis: MarketAnalysis = Field(description="Market analysis section")

    opportunities: List[str] = Field(description="Business opportunities identified")

    risks: List[str] = Field(description="Potential risks and challenges")

    action_items: List[str] = Field(description="Recommended action items")

    timeline: str = Field(description="Suggested timeline for implementation")

    budget_estimate: Optional[str] = Field(
        default=None, description="Rough budget estimate if applicable"
    )


# Example tools for ReactAgent
@tool
def search_web(query: str) -> str:
    """Search the web for information."""
    # Simulated web search
    return f"Found information about {query}: Recent studies show significant developments in this area. Market reports indicate growing interest and investment."


@tool
def analyze_data(data: str) -> str:
    """Analyze provided data."""
    # Simulated data analysis
    return f"Analysis of {data}: Trends show positive growth with 15% year-over-year increase. Key indicators suggest continued expansion."


@tool
def get_market_info(market: str) -> str:
    """Get market information."""
    # Simulated market data
    return f"Market info for {market}: Size estimated at $10B, growing at 20% annually. Top players include Company A, Company B, and Company C."


async def test_react_to_research_report():
    """Test ReactAgent → Research Report pattern."""
    print("\n=== Test 1: ReactAgent → Research Report ===\n")

    # Create custom hooks
    def transform_react_output(react_result):
        """Transform React output for research report."""
        # Extract content from React result
        if hasattr(react_result, "messages"):
            content = react_result.messages[-1].content if react_result.messages else ""
        else:
            content = str(react_result)

        return {
            "input_data": {
                "research_content": content,
                "tools_used": "web search, data analysis",
            },
            "context": {"research_type": "market research", "depth": "comprehensive"},
        }

    hooks = SequentialHooks(intermediate_transform=transform_react_output)

    # Create the sequential pattern
    sequential = create_react_to_structured(
        tools=[search_web, analyze_data, get_market_info],
        structured_output_model=ResearchReport,
        name="research_pipeline",
        react_config={"temperature": 0.7},
        hooks=hooks,
        debug=True,
    )

    # Run the pipeline
    result = await sequential.arun(
        "Research the AI market opportunity for small businesses"
    )

    print("\n📊 Research Report Generated:"d:")
    print(f"Topic: {result.topic}")
    print(f"Executive Summary: {result.executive_summary[:200]}...")
    print(f"Key Findings: {len(result.key_findings)} findings")
    print(f"Sources: {len(result.sources)} sources")
    print(f"Confidence Level: {result.confidence_level}")
    print(f"Recommendations: {len(result.recommendations)} recommendations")


async def test_analysis_to_business_report():
    """Test Analysis → Business Report pattern."""
    print("\n\n=== Test 2: Analysis → Business Report ===\n")

    # Analysis prompt
    analysis_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are a business analyst specializing in market analysis and strategic planning.
Analyze the provided business scenario and identify opportunities, risks, and recommendations.""",
            ),
            (
                "human",
                """Analyze the following business scenario:

{scenario}

Provide a comprehensive analysis including:
- Market assessment
- Opportunities and risks
- Strategic recommendations
- Implementation considerations""",
            ),
        ]
    )

    # Business report structuring prompt
    report_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are a business report specialist. Transform analysis into structured business reports.""",
            ),
            (
                "human",
                """Create a structured business report from the following analysis:

{input_data}

Ensure the report is professional, actionable, and includes all required sections.""",
            ),
        ]
    )

    # Create the pipeline
    sequential = create_analysis_to_report(
        analysis_prompt=analysis_prompt,
        report_model=BusinessReport,
        name="business_report",
        report_prompt=report_prompt,
        debug=True,
    )

    # Run the pipeline
    result = await sequential.arun(
        {
            "scenario": "A startup wants to enter the AI-powered customer service market with a focus on small retail businesses"
        }
    )

    print("\n📈 Business Report Generated:"d:")
    print(f"Title: {result.title}")
    print(f"Market Segment: {result.market_analysis.segment}")
    print(f"Market Size: {result.market_analysis.size}")
    print(f"Growth Rate: {result.market_analysis.growth_rate}")
    print(f"Opportunities: {len(result.opportunities)} identified")
    print(f"Risks: {len(result.risks)} identified")
    print(f"Action Items: {len(result.action_items)} items")
    print(f"Timeline: {result.timeline}")


async def test_custom_sequential():
    """Test custom sequential pattern with specific agents."""
    print("\n\n=== Test 3: Custom Sequential Pattern ===\n")

    # Custom structured output model
    class TechnicalSummary(BaseModel):
        """Technical summary of findings."""

        problem_statement: str = Field(description="Clear problem statement")
        technical_approach: str = Field(description="Technical approach taken")
        implementation_steps: List[str] = Field(description="Implementation steps")
        technologies_used: List[str] = Field(description="Technologies involved")
        complexity_rating: str = Field(pattern="^(simple|moderate|complex)$")
        estimated_effort: str = Field(description="Effort estimate")

    # First agent: Technical analyzer
    tech_agent = SimpleAgent(
        name="tech_analyzer",
        engine=AugLLMConfig(
            prompt_template=ChatPromptTemplate.from_messages(
                [
                    (
                        "system",
                        "You are a technical architect. Analyze technical problems and propose solutions.",
                    ),
                    ("human", "Analyze this technical challenge: {query}"),
                ]
            ),
            temperature=0.7,
        ),
    )

    # Custom hooks with error handling
    def handle_error(e: Exception):
        """Handle errors gracefully."""
        return TechnicalSummary(
            problem_statement="Error occurred during analysis",
            technical_approach="Unable to complete analysis",
            implementation_steps=["Error: " + str(e)],
            technologies_used=["N/A"],
            complexity_rating="complex",
            estimated_effort="Unknown",
        )

    hooks = SequentialHooks(
        error_handler=handle_error,
        post_process=lambda result: result,  # Could add post-processing here
    )

    # Create sequential pattern
    sequential = SequentialAgentWithStructuredOutput(
        first_agent=tech_agent,
        structured_output_model=TechnicalSummary,
        hooks=hooks,
        name="tech_summary",
        debug=True,
    )

    # Run the pipeline
    result = await sequential.arun(
        {
            "query": "How to implement a real-time data pipeline for processing 1M events per second?"
        }
    )

    print("\n🔧 Technical Summary Generated:"d:")
    print(f"Problem: {result.problem_statement}")
    print(f"Approach: {result.technical_approach[:200]}...")
    print(f"Steps: {len(result.implementation_steps)} steps")
    print(f"Technologies: {', '.join(result.technologies_used[:3])}...")
    print(f"Complexity: {result.complexity_rating}")
    print(f"Effort: {result.estimated_effort}")


async def main():
    """Run all test examples."""
    await test_react_to_research_report()
    await test_analysis_to_business_report()
    await test_custom_sequential()


if __name__ == "__main__":
    asyncio.run(main())
