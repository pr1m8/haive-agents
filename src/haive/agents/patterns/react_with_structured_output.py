"""ReactAgent with Structured Output Pattern.

This pattern demonstrates ReactAgent → SimpleAgentV3 sequential execution
using the generalized hook system for structured output workflows.

Pattern: ReactAgent (reasoning/tools) → SimpleAgentV3 (structured output)
Use Cases:
- Analysis with structured results
- Research with formatted reports
- Problem-solving with structured solutions
- Tool-based workflows with typed outputs
"""

import asyncio
import traceback
from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.base.hooks import HookContext
from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent_v3 import SimpleAgentV3


# Example structured output models
class AnalysisResult(BaseModel):
    """Structured analysis result."""

    summary: str = Field(description="Brief summary of analysis")
    key_findings: list[str] = Field(description="Main findings from analysis")
    confidence_score: float = Field(
        ge=0.0, le=1.0, description="Confidence in analysis"
    )
    recommendations: list[str] = Field(description="Recommended actions")
    supporting_evidence: list[str] = Field(
        default_factory=list, description="Evidence supporting findings"
    )


class ResearchReport(BaseModel):
    """Structured research report."""

    title: str = Field(description="Report title")
    executive_summary: str = Field(description="Executive summary")
    methodology: str = Field(description="Research methodology used")
    findings: list[dict[str, Any]] = Field(description="Detailed findings")
    conclusions: list[str] = Field(description="Main conclusions")
    sources: list[str] = Field(description="Sources consulted")
    confidence_level: str = Field(description="High/Medium/Low confidence")


class ProblemSolution(BaseModel):
    """Structured problem solution."""

    problem_statement: str = Field(description="Clear problem statement")
    root_causes: list[str] = Field(description="Identified root causes")
    proposed_solutions: list[dict[str, Any]] = Field(
        description="Proposed solutions with details"
    )
    implementation_steps: list[str] = Field(description="Step-by-step implementation")
    success_metrics: list[str] = Field(description="How to measure success")
    risks_and_mitigation: list[dict[str, str]] = Field(
        description="Risks and mitigation strategies"
    )


class ReactWithStructuredOutput(EnhancedMultiAgentV4):
    """ReactAgent → SimpleAgentV3 with structured output pattern.

    This pattern uses ReactAgent for reasoning and tool usage, then
    SimpleAgentV3 for converting the results to structured output.
    """

    # Configuration fields
    reasoning_agent: ReactAgent = Field(
        ..., description="Agent for reasoning and tool usage"
    )
    structuring_agent: SimpleAgentV3 = Field(
        ..., description="Agent for structured output"
    )
    structured_output_model: type[BaseModel] = Field(
        ..., description="Pydantic model for output structure"
    )

    # Processing configuration
    preserve_reasoning: bool = Field(
        default=True, description="Preserve reasoning details in output"
    )
    include_tool_calls: bool = Field(
        default=True, description="Include tool call information"
    )

    def __init__(self, **data):
        """Initialize the pattern with agents."""
        # Set up agents list for EnhancedMultiAgentV4
        if "agents" not in data:
            data["agents"] = [
                data.get("reasoning_agent"),
                data.get("structuring_agent"),
            ]

        if "execution_mode" not in data:
            data["execution_mode"] = "sequential"

        super().__init__(**data)

        # Set up hooks for monitoring
        self._setup_pattern_hooks()

    def _setup_pattern_hooks(self):
        """Set up hooks for monitoring the pattern execution."""

        @self.before_run
        def log_pattern_start(context: HookContext):
            pass

        @self.after_run
        def log_pattern_completion(context: HookContext):
            pass

        # Hook into the reasoning agent
        @self.reasoning_agent.after_run
        def track_reasoning_completion(context: HookContext):
            if context.output_data and isinstance(context.output_data, dict):
                context.output_data.get("messages", [])

        # Hook into the structuring agent
        @self.structuring_agent.before_structured_output
        def track_structuring_start(context: HookContext):
            pass

        @self.structuring_agent.after_structured_output
        def track_structuring_completion(context: HookContext):
            if context.structured_data:
                pass

    @classmethod
    def create_analysis_pattern(
        cls,
        name: str = "analysis_workflow",
        tools: list | None = None,
        reasoning_config: AugLLMConfig | None = None,
        structuring_config: AugLLMConfig | None = None) -> "ReactWithStructuredOutput":
        """Create a ReactAgent → StructuredOutput pattern for analysis tasks.

        Args:
            name: Name for the workflow
            tools: Tools for the ReactAgent
            reasoning_config: Configuration for reasoning agent
            structuring_config: Configuration for structuring agent

        Returns:
            Configured ReactWithStructuredOutput instance
        """
        if not reasoning_config:
            reasoning_config = AugLLMConfig(
                system_message="You are an expert analyst. Use available tools to gather information and perform thorough analysis.",
                temperature=0.3)

        if not structuring_config:
            structuring_config = AugLLMConfig(
                system_message="You are a structured output specialist. Convert analysis results into well-formatted structured data.",
                structured_output_model=AnalysisResult,
                temperature=0.1)

        reasoning_agent = ReactAgent(
            name=f"{name}_reasoner", engine=reasoning_config, tools=tools or []
        )

        structuring_agent = SimpleAgentV3(
            name=f"{name}_structurer",
            engine=structuring_config,
            prompt_template=ChatPromptTemplate.from_messages(
                [
                    (
                        "system",
                        "Convert the following analysis into structured format."),
                    (
                        "human",
                        """Analysis Results:
{reasoning_output}

Convert this analysis into a structured format with:
- Summary of the analysis
- Key findings (as a list)
- Confidence score (0.0 to 1.0)
- Recommendations (as a list)
- Supporting evidence (as a list)

Ensure all fields are properly filled based on the analysis."""),
                ]
            ))

        return cls(
            name=name,
            reasoning_agent=reasoning_agent,
            structuring_agent=structuring_agent,
            structured_output_model=AnalysisResult)

    @classmethod
    def create_research_pattern(
        cls,
        name: str = "research_workflow",
        tools: list | None = None,
        reasoning_config: AugLLMConfig | None = None,
        structuring_config: AugLLMConfig | None = None) -> "ReactWithStructuredOutput":
        """Create a ReactAgent → StructuredOutput pattern for research tasks."""
        if not reasoning_config:
            reasoning_config = AugLLMConfig(
                system_message="You are a thorough researcher. Use available tools to gather comprehensive information on the topic.",
                temperature=0.4)

        if not structuring_config:
            structuring_config = AugLLMConfig(
                system_message="You are a research report specialist. Format research findings into professional reports.",
                structured_output_model=ResearchReport,
                temperature=0.2)

        reasoning_agent = ReactAgent(
            name=f"{name}_researcher", engine=reasoning_config, tools=tools or []
        )

        structuring_agent = SimpleAgentV3(
            name=f"{name}_formatter",
            engine=structuring_config,
            prompt_template=ChatPromptTemplate.from_messages(
                [
                    ("system", "Format research findings into a structured report."),
                    (
                        "human",
                        """Research Findings:
{reasoning_output}

Create a comprehensive research report with:
- Title for the research
- Executive summary
- Methodology used
- Detailed findings (as structured data)
- Main conclusions
- Sources consulted
- Confidence level assessment

Ensure the report is professional and well-structured."""),
                ]
            ))

        return cls(
            name=name,
            reasoning_agent=reasoning_agent,
            structuring_agent=structuring_agent,
            structured_output_model=ResearchReport)

    @classmethod
    def create_problem_solving_pattern(
        cls,
        name: str = "problem_solving_workflow",
        tools: list | None = None,
        reasoning_config: AugLLMConfig | None = None,
        structuring_config: AugLLMConfig | None = None) -> "ReactWithStructuredOutput":
        """Create a ReactAgent → StructuredOutput pattern for problem-solving tasks."""
        if not reasoning_config:
            reasoning_config = AugLLMConfig(
                system_message="You are an expert problem solver. Analyze problems systematically and develop comprehensive solutions.",
                temperature=0.3)

        if not structuring_config:
            structuring_config = AugLLMConfig(
                system_message="You are a solution architect. Structure problem-solving results into actionable plans.",
                structured_output_model=ProblemSolution,
                temperature=0.1)

        reasoning_agent = ReactAgent(
            name=f"{name}_solver", engine=reasoning_config, tools=tools or []
        )

        structuring_agent = SimpleAgentV3(
            name=f"{name}_architect",
            engine=structuring_config,
            prompt_template=ChatPromptTemplate.from_messages(
                [
                    (
                        "system",
                        "Structure problem-solving results into actionable solutions."),
                    (
                        "human",
                        """Problem Analysis:
{reasoning_output}

Create a structured solution with:
- Clear problem statement
- Root causes identified
- Proposed solutions with details
- Step-by-step implementation plan
- Success metrics
- Risks and mitigation strategies

Make the solution actionable and comprehensive."""),
                ]
            ))

        return cls(
            name=name,
            reasoning_agent=reasoning_agent,
            structuring_agent=structuring_agent,
            structured_output_model=ProblemSolution)


# Factory functions for common patterns


def create_react_analysis_workflow(
    name: str = "react_analysis", tools: list | None = None
) -> ReactWithStructuredOutput:
    """Create a ReactAgent analysis workflow with structured output.

    Args:
        name: Workflow name
        tools: Tools for analysis (web search, calculators, etc.)

    Returns:
        Configured analysis workflow
    """
    return ReactWithStructuredOutput.create_analysis_pattern(name=name, tools=tools)


def create_react_research_workflow(
    name: str = "react_research", tools: list | None = None
) -> ReactWithStructuredOutput:
    """Create a ReactAgent research workflow with structured output.

    Args:
        name: Workflow name
        tools: Tools for research (web search, document analysis, etc.)

    Returns:
        Configured research workflow
    """
    return ReactWithStructuredOutput.create_research_pattern(name=name, tools=tools)


def create_react_problem_solving_workflow(
    name: str = "react_problem_solver", tools: list | None = None
) -> ReactWithStructuredOutput:
    """Create a ReactAgent problem-solving workflow with structured output.

    Args:
        name: Workflow name
        tools: Tools for problem-solving (analysis tools, simulators, etc.)

    Returns:
        Configured problem-solving workflow
    """
    return ReactWithStructuredOutput.create_problem_solving_pattern(
        name=name, tools=tools
    )


# Example tools for demonstration
@tool
def web_search(query: str) -> str:
    """Search the web for information."""
    return f"Web search results for '{query}': [Simulated results with relevant information]"


@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    try:
        result = eval(expression)
        return f"Calculation result: {expression} = {result}"
    except Exception as e:
        return f"Calculation error: {e}"


@tool
def data_analyzer(data: str) -> str:
    """Analyze data and provide insights."""
    return f"Data analysis of '{data[:50]}...': [Simulated analysis with trends and patterns]"


# Example usage patterns
async def example_analysis_workflow():
    """Example: ReactAgent analysis with structured output."""
    # Create analysis workflow
    workflow = create_react_analysis_workflow(
        name="market_analysis", tools=[web_search, calculator, data_analyzer]
    )

    # Execute analysis
    result = await workflow.arun(
        "Analyze the current AI market trends and provide structured insights"
    )

    if isinstance(result, AnalysisResult):
        pass

    return result


async def example_research_workflow():
    """Example: ReactAgent research with structured report."""
    # Create research workflow
    workflow = create_react_research_workflow(
        name="ai_safety_research", tools=[web_search, data_analyzer]
    )

    # Execute research
    result = await workflow.arun(
        "Research the latest developments in AI safety and create a comprehensive report"
    )

    if isinstance(result, ResearchReport):
        pass

    return result


async def example_problem_solving_workflow():
    """Example: ReactAgent problem-solving with structured solution."""
    # Create problem-solving workflow
    workflow = create_react_problem_solving_workflow(
        name="efficiency_optimizer", tools=[calculator, data_analyzer]
    )

    # Execute problem-solving
    result = await workflow.arun(
        "How can we improve the efficiency of our customer service process by 30%?"
    )

    if isinstance(result, ProblemSolution):
        pass

    return result


if __name__ == "__main__":

    async def main():
        """Run all workflow examples."""
        try:
            await example_analysis_workflow()
            await example_research_workflow()
            await example_problem_solving_workflow()

        except Exception:

            traceback.print_exc()

    asyncio.run(main())
