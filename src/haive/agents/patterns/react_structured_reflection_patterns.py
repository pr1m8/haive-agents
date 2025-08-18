"""Comprehensive ReactAgent → SimpleAgent Patterns with V3, V4, and Enhanced Base Agent.

This demonstrates all variations of ReactAgent → SimpleAgent workflows:
1. V3: ReactAgent → SimpleAgent (structured output)
2. V4: MultiAgent composition
3. Enhanced Base: Using enhanced base agent with hooks
4. Reflection: ReactAgent → SimpleAgentV3 → ReflectionAgent
5. Graded Reflection: ReactAgent → GradingAgent → SimpleAgentV3 → ReflectionAgent

Each pattern showcases the generalized hook system and different architectural approaches.
"""

import asyncio
import traceback
from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.base.hooks import HookContext
from haive.agents.base.pre_post_agent_mixin import (
    create_graded_reflection_agent,
    create_reflection_agent,
)
from haive.agents.multi.agent import MultiAgent
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent


# Structured output models
class TaskAnalysis(BaseModel):
    """Analysis of a complex task."""

    task_summary: str = Field(description="Brief summary of the task")
    complexity_level: str = Field(description="Low/Medium/High complexity")
    key_components: list[str] = Field(description="Main components of the task")
    estimated_effort: str = Field(description="Estimated effort required")
    success_criteria: list[str] = Field(description="Criteria for success")
    potential_challenges: list[str] = Field(description="Potential challenges")


class ResearchFindings(BaseModel):
    """Structured research findings."""

    research_question: str = Field(description="Main research question")
    methodology: str = Field(description="Research approach used")
    key_findings: list[dict[str, str]] = Field(description="Key findings with evidence")
    data_sources: list[str] = Field(description="Sources of information")
    confidence_assessment: str = Field(description="High/Medium/Low confidence")
    limitations: list[str] = Field(description="Research limitations")
    next_steps: list[str] = Field(description="Recommended next steps")


class ProblemAnalysis(BaseModel):
    """Structured problem analysis."""

    problem_definition: str = Field(description="Clear definition of the problem")
    stakeholders: list[str] = Field(description="Key stakeholders affected")
    root_causes: list[str] = Field(description="Identified root causes")
    impact_assessment: dict[str, str] = Field(description="Impact on different areas")
    solution_options: list[dict[str, Any]] = Field(description="Possible solutions")
    recommended_approach: str = Field(description="Recommended solution approach")


# Example tools
@tool
def web_research(topic: str) -> str:
    """Research a topic using web sources."""
    return f"Web research on '{topic}': Found comprehensive information including recent studies, expert opinions, and statistical data."


@tool
def data_analysis(data_description: str) -> str:
    """Analyze data and extract insights."""
    return f"Data analysis of '{data_description}': Identified trends, patterns, and statistical significance with confidence intervals."


@tool
def stakeholder_analysis(context: str) -> str:
    """Analyze stakeholders for a given context."""
    return f"Stakeholder analysis for '{context}': Identified key stakeholders, their interests, influence levels, and potential impact."


# =============================================================================
# PATTERN 1: V3 Architecture - ReactAgent → SimpleAgentV3
# =============================================================================


class ReactToStructuredV3:
    """V3 Pattern: ReactAgent → SimpleAgentV3 with structured output."""

    def __init__(
        self,
        name: str,
        tools: list | None = None,
        structured_output_model: type[BaseModel] = TaskAnalysis,
        reasoning_config: AugLLMConfig = None,
        structuring_config: AugLLMConfig = None,
    ):
        """Init  .

        Args:
            name: [TODO: Add description]
            tools: [TODO: Add description]
            structured_output_model: [TODO: Add description]
            reasoning_config: [TODO: Add description]
            structuring_config: [TODO: Add description]
        """
        self.name = name
        self.structured_output_model = structured_output_model

        # Create ReactAgent for reasoning
        self.reasoning_agent = ReactAgent(
            name=f"{name}_reasoner",
            engine=reasoning_config
            or AugLLMConfig(
                system_message="You are an expert analyst. Use tools to gather information and provide thorough analysis.",
                temperature=0.3,
            ),
            tools=tools or [],
        )

        # Create SimpleAgentV3 for structured output
        self.structuring_agent = SimpleAgent(
            name=f"{name}_structurer",
            engine=structuring_config
            or AugLLMConfig(
                system_message="You are a structured output specialist. Convert analysis into well-formatted structured data.",
                structured_output_model=structured_output_model,
                temperature=0.1,
            ),
            prompt_template=ChatPromptTemplate.from_messages(
                [
                    (
                        "system",
                        "Convert the following analysis into structured format.",
                    ),
                    (
                        "human",
                        """Analysis from reasoning agent:
{reasoning_output}

Convert this into the required structured format. Ensure all fields are properly filled based on the analysis provided.""",
                    ),
                ]
            ),
        )

        # Set up hooks for monitoring
        self._setup_v3_hooks()

    def _setup_v3_hooks(self):
        """Set up hooks for V3 pattern monitoring."""

        @self.reasoning_agent.before_run
        def log_reasoning_start(context: HookContext):
            """Log Reasoning Start.

            Args:
                context: [TODO: Add description]
            """
            pass

        @self.reasoning_agent.after_run
        def log_reasoning_complete(context: HookContext):
            """Log Reasoning Complete.

            Args:
                context: [TODO: Add description]
            """
            pass

        @self.structuring_agent.before_structured_output
        def log_structuring_start(context: HookContext):
            """Log Structuring Start.

            Args:
                context: [TODO: Add description]
            """
            pass

        @self.structuring_agent.after_structured_output
        def log_structuring_complete(context: HookContext):
            """Log Structuring Complete.

            Args:
                context: [TODO: Add description]
            """
            pass

    async def arun(self, input_data: str) -> BaseModel:
        """Execute V3 pattern: ReactAgent → SimpleAgentV3."""
        # Step 1: ReactAgent reasoning
        reasoning_result = await self.reasoning_agent.arun(input_data)

        # Step 2: SimpleAgentV3 structuring
        structured_result = await self.structuring_agent.arun(
            {"reasoning_output": str(reasoning_result)}
        )

        return structured_result


# =============================================================================
# PATTERN 2: V4 Architecture - MultiAgent Composition
# =============================================================================


class ReactToStructuredV4(MultiAgent):
    """V4 Pattern: MultiAgent with ReactAgent → SimpleAgentV3."""

    reasoning_agent: ReactAgent = Field(
        ..., description="Agent for reasoning and tool usage"
    )
    structuring_agent: SimpleAgentV3 = Field(
        ..., description="Agent for structured output"
    )
    structured_output_model: type[BaseModel] = Field(
        ..., description="Output model type"
    )

    def __init__(self, **data):
        """Init  ."""
        # Set up agents for V4 architecture
        if "agents" not in data:
            data["agents"] = [
                data.get("reasoning_agent"),
                data.get("structuring_agent"),
            ]

        if "execution_mode" not in data:
            data["execution_mode"] = "sequential"

        super().__init__(**data)
        self._setup_v4_hooks()

    def _setup_v4_hooks(self):
        """Set up hooks for V4 pattern monitoring."""

        @self.before_run
        def log_v4_start(context: HookContext):
            """Log V4 Start.

            Args:
                context: [TODO: Add description]
            """
            pass

        @self.after_run
        def log_v4_complete(context: HookContext):
            """Log V4 Complete.

            Args:
                context: [TODO: Add description]
            """
            pass

        @self.reasoning_agent.after_run
        def track_reasoning_stage(context: HookContext):
            """Track Reasoning Stage.

            Args:
                context: [TODO: Add description]
            """
            pass

        @self.structuring_agent.after_structured_output
        def track_structuring_stage(context: HookContext):
            """Track Structuring Stage.

            Args:
                context: [TODO: Add description]
            """
            pass

    @classmethod
    def create_analysis_workflow(
        cls,
        name: str = "v4_analysis",
        tools: list | None = None,
        structured_output_model: type[BaseModel] = TaskAnalysis,
    ) -> "ReactToStructuredV4":
        """Create V4 analysis workflow."""
        reasoning_agent = ReactAgent(
            name=f"{name}_reasoner",
            engine=AugLLMConfig(
                system_message="You are an expert analyst. Use available tools for comprehensive analysis.",
                temperature=0.3,
            ),
            tools=tools or [],
        )

        structuring_agent = SimpleAgent(
            name=f"{name}_structurer",
            engine=AugLLMConfig(
                system_message="Convert analysis results into structured format.",
                structured_output_model=structured_output_model,
                temperature=0.1,
            ),
        )

        return cls(
            name=name,
            reasoning_agent=reasoning_agent,
            structuring_agent=structuring_agent,
            structured_output_model=structured_output_model,
        )


# =============================================================================
# PATTERN 3: Enhanced Base Agent with Reflection
# =============================================================================


class ReactWithReflection:
    """Enhanced Base Agent Pattern: ReactAgent → SimpleAgentV3 → ReflectionAgent."""

    def __init__(
        self,
        name: str,
        tools: list | None = None,
        structured_output_model: type[BaseModel] = TaskAnalysis,
        reasoning_config: AugLLMConfig = None,
        structuring_config: AugLLMConfig = None,
    ):
        """Init  .

        Args:
            name: [TODO: Add description]
            tools: [TODO: Add description]
            structured_output_model: [TODO: Add description]
            reasoning_config: [TODO: Add description]
            structuring_config: [TODO: Add description]
        """
        self.name = name
        self.structured_output_model = structured_output_model

        # Create ReactAgent
        self.reasoning_agent = ReactAgent(
            name=f"{name}_reasoner",
            engine=reasoning_config
            or AugLLMConfig(
                system_message="You are a thorough analyst. Use tools and provide detailed reasoning.",
                temperature=0.4,
            ),
            tools=tools or [],
        )

        # Create SimpleAgentV3 with structured output
        base_structuring_agent = SimpleAgent(
            name=f"{name}_structurer",
            engine=structuring_config
            or AugLLMConfig(
                system_message="Convert analysis into structured format with attention to detail.",
                structured_output_model=structured_output_model,
                temperature=0.2,
            ),
        )

        # Add reflection capabilities using factory pattern
        self.structuring_agent = create_reflection_agent(base_structuring_agent)

        self._setup_reflection_hooks()

    def _setup_reflection_hooks(self):
        """Set up hooks for reflection pattern monitoring."""

        @self.reasoning_agent.before_run
        def log_reasoning_with_reflection_start(context: HookContext):
            """Log Reasoning With Reflection Start.

            Args:
                context: [TODO: Add description]
            """
            pass

        @self.reasoning_agent.after_run
        def log_reasoning_with_reflection_complete(context: HookContext):
            """Log Reasoning With Reflection Complete.

            Args:
                context: [TODO: Add description]
            """
            pass

        @self.structuring_agent.before_reflection
        def log_reflection_start(context: HookContext):
            """Log Reflection Start.

            Args:
                context: [TODO: Add description]
            """
            pass

        @self.structuring_agent.after_reflection
        def log_reflection_complete(context: HookContext):
            """Log Reflection Complete.

            Args:
                context: [TODO: Add description]
            """
            pass

    async def arun(self, input_data: str) -> dict[str, Any]:
        """Execute Enhanced Base Agent pattern with reflection."""
        # Step 1: ReactAgent reasoning
        reasoning_result = await self.reasoning_agent.arun(input_data)

        # Step 2: SimpleAgentV3 with reflection for structured output
        structured_result = await self.structuring_agent.arun(
            {"reasoning_output": str(reasoning_result)}
        )

        return structured_result


# =============================================================================
# PATTERN 4: Graded Reflection Pattern
# =============================================================================


class ReactWithGradedReflection:
    """Graded Reflection Pattern: ReactAgent → GradingAgent → SimpleAgentV3 → ReflectionAgent."""

    def __init__(
        self,
        name: str,
        tools: list | None = None,
        structured_output_model: type[BaseModel] = TaskAnalysis,
    ):
        """Init  .

        Args:
            name: [TODO: Add description]
            tools: [TODO: Add description]
            structured_output_model: [TODO: Add description]
        """
        self.name = name
        self.structured_output_model = structured_output_model

        # Create ReactAgent
        self.reasoning_agent = ReactAgent(
            name=f"{name}_reasoner",
            engine=AugLLMConfig(
                system_message="You are an expert analyst. Provide comprehensive analysis using available tools.",
                temperature=0.4,
            ),
            tools=tools or [],
        )

        # Create base structuring agent
        base_structuring_agent = SimpleAgent(
            name=f"{name}_structurer",
            engine=AugLLMConfig(
                system_message="Convert analysis into high-quality structured format.",
                structured_output_model=structured_output_model,
                temperature=0.2,
            ),
        )

        # Add graded reflection capabilities
        self.structuring_agent = create_graded_reflection_agent(base_structuring_agent)

        self._setup_graded_reflection_hooks()

    def _setup_graded_reflection_hooks(self):
        """Set up hooks for graded reflection pattern monitoring."""

        @self.structuring_agent.before_grading
        def log_grading_start(context: HookContext):
            """Log Grading Start.

            Args:
                context: [TODO: Add description]
            """
            pass

        @self.structuring_agent.after_grading
        def log_grading_complete(context: HookContext):
            """Log Grading Complete.

            Args:
                context: [TODO: Add description]
            """
            pass

        @self.structuring_agent.before_reflection
        def log_reflection_with_grade_start(context: HookContext):
            """Log Reflection With Grade Start.

            Args:
                context: [TODO: Add description]
            """
            pass

        @self.structuring_agent.after_reflection
        def log_reflection_with_grade_complete(context: HookContext):
            """Log Reflection With Grade Complete.

            Args:
                context: [TODO: Add description]
            """
            pass

    async def arun(self, input_data: str) -> dict[str, Any]:
        """Execute Graded Reflection pattern."""
        # Step 1: ReactAgent reasoning
        reasoning_result = await self.reasoning_agent.arun(input_data)

        # Step 2: SimpleAgentV3 with graded reflection
        structured_result = await self.structuring_agent.arun(
            {"reasoning_output": str(reasoning_result)}
        )

        return structured_result


# =============================================================================
# FACTORY FUNCTIONS FOR ALL PATTERNS
# =============================================================================


def create_v3_pattern(
    name: str = "react_structured_v3",
    tools: list | None = None,
    structured_output_model: type[BaseModel] = TaskAnalysis,
) -> ReactToStructuredV3:
    """Create V3 pattern: ReactAgent → SimpleAgentV3."""
    return ReactToStructuredV3(
        name=name, tools=tools, structured_output_model=structured_output_model
    )


def create_v4_pattern(
    name: str = "react_structured_v4",
    tools: list | None = None,
    structured_output_model: type[BaseModel] = TaskAnalysis,
) -> ReactToStructuredV4:
    """Create V4 pattern: MultiAgent composition."""
    return ReactToStructuredV4.create_analysis_workflow(
        name=name, tools=tools, structured_output_model=structured_output_model
    )


def create_reflection_pattern(
    name: str = "react_with_reflection",
    tools: list | None = None,
    structured_output_model: type[BaseModel] = TaskAnalysis,
) -> ReactWithReflection:
    """Create Enhanced Base Agent pattern with reflection."""
    return ReactWithReflection(
        name=name, tools=tools, structured_output_model=structured_output_model
    )


def create_graded_reflection_pattern(
    name: str = "react_graded_reflection",
    tools: list | None = None,
    structured_output_model: type[BaseModel] = TaskAnalysis,
) -> ReactWithGradedReflection:
    """Create graded reflection pattern."""
    return ReactWithGradedReflection(
        name=name, tools=tools, structured_output_model=structured_output_model
    )


# =============================================================================
# COMPREHENSIVE EXAMPLES
# =============================================================================


async def example_v3_pattern():
    """Example: V3 Architecture Pattern."""
    workflow = create_v3_pattern(
        name="market_research_v3",
        tools=[web_research, data_analysis],
        structured_output_model=ResearchFindings,
    )

    result = await workflow.arun(
        "Research the impact of AI on small businesses and provide structured findings"
    )

    return result


async def example_v4_pattern():
    """Example: V4 Architecture Pattern."""
    workflow = create_v4_pattern(
        name="problem_analysis_v4",
        tools=[stakeholder_analysis, data_analysis],
        structured_output_model=ProblemAnalysis,
    )

    result = await workflow.arun(
        "Analyze the problem of customer service delays in our company"
    )

    return result


async def example_reflection_pattern():
    """Example: Enhanced Base Agent with Reflection."""
    workflow = create_reflection_pattern(
        name="task_analysis_reflection",
        tools=[web_research, stakeholder_analysis],
        structured_output_model=TaskAnalysis,
    )

    result = await workflow.arun(
        "Analyze the task of implementing a new customer feedback system"
    )

    if isinstance(result, dict) and "processing_stages" in result:
        pass
    return result


async def example_graded_reflection_pattern():
    """Example: Graded Reflection Pattern."""
    workflow = create_graded_reflection_pattern(
        name="comprehensive_analysis",
        tools=[web_research, data_analysis, stakeholder_analysis],
        structured_output_model=ResearchFindings,
    )

    result = await workflow.arun(
        "Conduct comprehensive research on sustainable energy adoption in urban areas"
    )

    if isinstance(result, dict) and "processing_stages" in result:
        pass
    return result


async def main():
    """Run all pattern examples."""
    try:
        # Run all patterns
        await example_v3_pattern()
        await example_v4_pattern()
        await example_reflection_pattern()
        await example_graded_reflection_pattern()

    except Exception:
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
