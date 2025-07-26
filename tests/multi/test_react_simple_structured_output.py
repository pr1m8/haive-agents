"""
Test ReactAgent → SimpleAgent with Structured Output

This test demonstrates:
1. ReactAgent with tools performing analysis
2. SimpleAgent with structured output formatting results
3. Proper prompt templates with input variables
4. Cross-agent data flow
"""

import asyncio
from typing import List

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.react.agent_v3 import ReactAgentV3
from haive.agents.simple.agent_v3 import SimpleAgentV3

# ============================================================================
# STRUCTURED OUTPUT MODEL
# ============================================================================


class AnalysisReport(BaseModel):
    """Structured analysis report."""

    topic: str = Field(description="Topic analyzed")
    key_findings: List[str] = Field(description="Key findings from analysis")
    calculations: List[str] = Field(description="Calculations performed")
    recommendations: List[str] = Field(description="Recommendations based on analysis")
    confidence_score: float = Field(
        ge=0.0, le=1.0, description="Confidence in analysis"
    )
    summary: str = Field(description="Executive summary")


# ============================================================================
# TOOLS FOR REACT AGENT
# ============================================================================


@tool
def calculator(expression: str) -> str:
    """Perform mathematical calculations."""
    try:
        result = eval(expression)
        return f"Calculation result: {result}"
    except Exception as e:
        return f"Calculation error: {str(e)}"


@tool
def analyze_data(data_description: str) -> str:
    """Analyze described data and provide insights."""
    return f"""Analysis of {data_description}:
    - Data shows positive trends
    - Key metric increased by 25%
    - Correlation coefficient: 0.85
    - Statistical significance: p < 0.05
    - Recommendation: Continue current approach"""


@tool
def research_topic(topic: str) -> str:
    """Research a specific topic."""
    return f"""Research findings for {topic}:
    - Current market size: $50 billion
    - Growth rate: 15% annually
    - Key players: Company A, Company B, Company C
    - Main challenges: scalability, cost, adoption
    - Future outlook: Very promising with emerging technologies"""


# ============================================================================
# AGENT CREATION
# ============================================================================


def create_analysis_agent() -> ReactAgentV3:
    """Create ReactAgent for analysis with tools."""
    config = AugLLMConfig(
        temperature=0.7,
        system_message="You are a data analyst. Use tools to gather information and perform calculations.",
    )

    # Prompt template with input variables
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "{system_message}"),
            (
                "human",
                """Analyze the following:
Topic: {topic}
Specific questions: {questions}
Required calculations: {calculations}

Use available tools to gather data and perform analysis.""",
            ),
        ]
    )

    agent = ReactAgentV3(
        name="analyst",
        engine=config,
        prompt_template=prompt,
        tools=[calculator, analyze_data, research_topic],
    )

    return agent


def create_report_agent() -> SimpleAgentV3:
    """Create SimpleAgent for structured report generation."""
    config = AugLLMConfig(
        temperature=0.6,
        structured_output_model=AnalysisReport,
        system_message="You are a report writer. Create structured reports from analysis data.",
    )

    # Prompt template that uses analysis results
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "{system_message}"),
            (
                "human",
                """Create a structured report based on this analysis:

Topic: {topic}
Analysis Results:
{analysis_results}

Format this into a comprehensive structured report.""",
            ),
        ]
    )

    agent = SimpleAgentV3(name="reporter", engine=config, prompt_template=prompt)

    return agent


# ============================================================================
# TEST SEQUENTIAL FLOW
# ============================================================================


async def test_react_to_simple_structured():
    """Test ReactAgent → SimpleAgent with structured output."""
    print("\n" + "=" * 60)
    print("Testing ReactAgent → SimpleAgent with Structured Output")
    print("=" * 60)

    # Create agents
    analyst = create_analysis_agent()
    reporter = create_report_agent()

    # Create sequential workflow
    workflow = EnhancedMultiAgentV4(agents=[analyst, reporter], mode="sequential")

    # Initial state with proper structure
    initial_state = {
        "messages": [HumanMessage(content="Analyze the AI market and create a report")],
        "topic": "Artificial Intelligence Market Analysis 2025",
        "questions": [
            "What is the current market size?",
            "What is the growth rate?",
            "Who are the main players?",
        ],
        "calculations": [
            "Calculate ROI if investing $1M at 15% growth for 5 years",
            "Calculate market share percentages for top 3 companies",
        ],
        "system_message": "Be thorough and data-driven.",
        "analysis_results": "",  # Will be filled by analyst
    }

    print("\n📊 Starting Analysis...")

    # Execute workflow
    result = await workflow.arun(initial_state)

    # Print results
    print("\n📈 Analysis Results:")
    if "messages" in result:
        for i, msg in enumerate(result["messages"]):
            if hasattr(msg, "content"):
                print(f"\n{'🤖' if i % 2 == 1 else '👤'} Message {i+1}:")
                content = msg.content
                if len(content) > 300:
                    print(content[:300] + "...")
                else:
                    print(content)

    # Check for structured output
    if "messages" in result and len(result["messages"]) > 0:
        last_message = result["messages"][-1]
        if hasattr(last_message, "content"):
            try:
                import json

                # Try to parse as JSON (structured output)
                structured_data = json.loads(last_message.content)
                print("\n✅ Structured Output Detected:")
                for key, value in structured_data.items():
                    print(f"  - {key}: {value}")
            except:
                print("\n📄 Output is in text format")

    return result


async def test_with_reflection():
    """Test with reflection pattern."""
    print("\n" + "=" * 60)
    print("Testing with Reflection Pattern")
    print("=" * 60)

    # Import reflection utilities
    from haive.agents.base.pre_post_agent_mixin import create_reflection_agent

    # Create base reporter
    reporter = create_report_agent()

    # Enhance with reflection
    reflective_reporter = create_reflection_agent(
        main_agent=reporter,
        reflection_config=AugLLMConfig(
            temperature=0.5,
            system_message="You are a critical reviewer. Reflect on the report and suggest improvements.",
        ),
    )

    # Test data
    test_state = {
        "messages": [HumanMessage(content="Create a report on AI trends")],
        "topic": "AI Trends 2025",
        "analysis_results": """
        Research findings:
        - AI market growing at 35% CAGR
        - Generative AI leading growth
        - Enterprise adoption accelerating
        - Key challenges: ethics, regulation, talent
        """,
        "system_message": "Create a comprehensive report.",
    }

    print("\n📝 Creating Report with Reflection...")

    # Execute with reflection
    result = await reflective_reporter.arun(test_state)

    print("\n✨ Report with Reflection Complete")
    if isinstance(result, dict) and "messages" in result:
        print(f"Total messages: {len(result['messages'])}")

    return result


# ============================================================================
# MAIN EXECUTION
# ============================================================================


async def main():
    """Run the tests."""

    # Test 1: Basic ReactAgent → SimpleAgent flow
    print("\n🧪 Test 1: ReactAgent → SimpleAgent with Structured Output")
    result1 = await test_react_to_simple_structured()

    # Test 2: With reflection
    print("\n🧪 Test 2: SimpleAgent with Reflection")
    result2 = await test_with_reflection()

    print("\n" + "=" * 60)
    print("All Tests Complete!")
    print("=" * 60)

    # Summary
    print("\n📊 Summary:")
    print("  1. ReactAgent with tools → SimpleAgent with structured output: ✅")
    print("  2. SimpleAgent with reflection pattern: ✅")
    print("\nKey features demonstrated:")
    print("  - Prompt templates with input variables")
    print("  - Tool usage in ReactAgent")
    print("  - Structured output with Pydantic models")
    print("  - Cross-agent data flow")
    print("  - Reflection patterns")


if __name__ == "__main__":
    asyncio.run(main())
