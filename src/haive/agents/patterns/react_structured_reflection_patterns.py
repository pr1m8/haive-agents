"""Comprehensive ReactAgent → SimpleAgent Patterns with V3, V4, and Enhanced Base Agent.

This demonstrates all variations of ReactAgent → SimpleAgent workflows:
1. V3: ReactAgent → SimpleAgentV3 (structured output)
2. V4: EnhancedMultiAgentV4 composition
3. Enhanced Base: Using enhanced base agent with hooks
4. Reflection: ReactAgent → SimpleAgentV3 → ReflectionAgent
5. Graded Reflection: ReactAgent → GradingAgent → SimpleAgentV3 → ReflectionAgent

Each pattern showcases the generalized hook system and different architectural approaches.
"""

import asyncio
from typing import Any, Dict, List, Type

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.base.hooks import HookContext
from haive.agents.base.pre_post_agent_mixin import (
    create_graded_reflection_agent,
    create_reflection_agent,
)
from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent_v3 import SimpleAgentV3


# Structured output models
class TaskAnalysis(BaseModel):
    """Analysis of a complex task."""

    task_summary: str = Field(description="Brief summary of the task")
    complexity_level: str = Field(description="Low/Medium/High complexity")
    key_components: List[str] = Field(description="Main components of the task")
    estimated_effort: str = Field(description="Estimated effort required")
    success_criteria: List[str] = Field(description="Criteria for success")
    potential_challenges: List[str] = Field(description="Potential challenges")


class ResearchFindings(BaseModel):
    """Structured research findings."""

    research_question: str = Field(description="Main research question")
    methodology: str = Field(description="Research approach used")
    key_findings: List[Dict[str, str]] = Field(description="Key findings with evidence")
    data_sources: List[str] = Field(description="Sources of information")
    confidence_assessment: str = Field(description="High/Medium/Low confidence")
    limitations: List[str] = Field(description="Research limitations")
    next_steps: List[str] = Field(description="Recommended next steps")


class ProblemAnalysis(BaseModel):
    """Structured problem analysis."""

    problem_definition: str = Field(description="Clear definition of the problem")
    stakeholders: List[str] = Field(description="Key stakeholders affected")
    root_causes: List[str] = Field(description="Identified root causes")
    impact_assessment: Dict[str, str] = Field(description="Impact on different areas")
    solution_options: List[Dict[str, Any]] = Field(description="Possible solutions")
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
        tools: List = None,
        structured_output_model: Type[BaseModel] = TaskAnalysis,
        reasoning_config: AugLLMConfig = None,
        structuring_config: AugLLMConfig = None,
    ):
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
        self.structuring_agent = SimpleAgentV3(
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
            print(f"🧠 V3 Reasoning starting: {context.agent_name}")
            print(f"   Tools available: {len(self.reasoning_agent.tools)}")

        @self.reasoning_agent.after_run
        def log_reasoning_complete(context: HookContext):
            print(f"✅ V3 Reasoning completed: {context.agent_name}")

        @self.structuring_agent.before_structured_output
        def log_structuring_start(context: HookContext):
            print(
                f"📊 V3 Structuring starting: {self.structured_output_model.__name__}"
            )

        @self.structuring_agent.after_structured_output
        def log_structuring_complete(context: HookContext):
            print(f"📋 V3 Structuring completed: {context.agent_name}")

    async def arun(self, input_data: str) -> BaseModel:
        """Execute V3 pattern: ReactAgent → SimpleAgentV3."""
        print(f"🎯 V3 Pattern executing: {self.name}")

        # Step 1: ReactAgent reasoning
        reasoning_result = await self.reasoning_agent.arun(input_data)

        # Step 2: SimpleAgentV3 structuring
        structured_result = await self.structuring_agent.arun(
            {"reasoning_output": str(reasoning_result)}
        )

        print(f"✅ V3 Pattern completed: {self.name}")
        return structured_result


# =============================================================================
# PATTERN 2: V4 Architecture - EnhancedMultiAgentV4 Composition
# =============================================================================


class ReactToStructuredV4(EnhancedMultiAgentV4):
    """V4 Pattern: EnhancedMultiAgentV4 with ReactAgent → SimpleAgentV3."""

    reasoning_agent: ReactAgent = Field(
        ..., description="Agent for reasoning and tool usage"
    )
    structuring_agent: SimpleAgentV3 = Field(
        ..., description="Agent for structured output"
    )
    structured_output_model: Type[BaseModel] = Field(
        ..., description="Output model type"
    )

    def __init__(self, **data):
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
            print(f"🎯 V4 MultiAgent pattern starting: {self.name}")
            print(f"   Reasoning agent: {self.reasoning_agent.name}")
            print(f"   Structuring agent: {self.structuring_agent.name}")
            print(f"   Output model: {self.structured_output_model.__name__}")

        @self.after_run
        def log_v4_complete(context: HookContext):
            print(f"✅ V4 MultiAgent pattern completed: {self.name}")

        @self.reasoning_agent.after_run
        def track_reasoning_stage(context: HookContext):
            print(f"🔄 V4 Reasoning stage completed")

        @self.structuring_agent.after_structured_output
        def track_structuring_stage(context: HookContext):
            print(f"📊 V4 Structuring stage completed")

    @classmethod
    def create_analysis_workflow(
        cls,
        name: str = "v4_analysis",
        tools: List = None,
        structured_output_model: Type[BaseModel] = TaskAnalysis,
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

        structuring_agent = SimpleAgentV3(
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
        tools: List = None,
        structured_output_model: Type[BaseModel] = TaskAnalysis,
        reasoning_config: AugLLMConfig = None,
        structuring_config: AugLLMConfig = None,
    ):
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
        base_structuring_agent = SimpleAgentV3(
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
            print(f"🧠 Enhanced Reasoning starting: {context.agent_name}")

        @self.reasoning_agent.after_run
        def log_reasoning_with_reflection_complete(context: HookContext):
            print(f"✅ Enhanced Reasoning completed: {context.agent_name}")

        @self.structuring_agent.before_reflection
        def log_reflection_start(context: HookContext):
            print(f"💭 Reflection starting for structured output")

        @self.structuring_agent.after_reflection
        def log_reflection_complete(context: HookContext):
            print(f"✨ Reflection completed - output improved")

    async def arun(self, input_data: str) -> Dict[str, Any]:
        """Execute Enhanced Base Agent pattern with reflection."""
        print(f"🎯 Enhanced Base Agent + Reflection executing: {self.name}")

        # Step 1: ReactAgent reasoning
        reasoning_result = await self.reasoning_agent.arun(input_data)

        # Step 2: SimpleAgentV3 with reflection for structured output
        structured_result = await self.structuring_agent.arun(
            {"reasoning_output": str(reasoning_result)}
        )

        print(f"✅ Enhanced Base Agent + Reflection completed: {self.name}")
        return structured_result


# =============================================================================
# PATTERN 4: Graded Reflection Pattern
# =============================================================================


class ReactWithGradedReflection:
    """Graded Reflection Pattern: ReactAgent → GradingAgent → SimpleAgentV3 → ReflectionAgent."""

    def __init__(
        self,
        name: str,
        tools: List = None,
        structured_output_model: Type[BaseModel] = TaskAnalysis,
    ):
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
        base_structuring_agent = SimpleAgentV3(
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
            print(f"📊 Grading starting for quality assessment")

        @self.structuring_agent.after_grading
        def log_grading_complete(context: HookContext):
            print(f"📈 Grading completed - quality assessed")

        @self.structuring_agent.before_reflection
        def log_reflection_with_grade_start(context: HookContext):
            print(f"💭 Reflection starting with grade context")

        @self.structuring_agent.after_reflection
        def log_reflection_with_grade_complete(context: HookContext):
            print(f"✨ Graded reflection completed - output enhanced")

    async def arun(self, input_data: str) -> Dict[str, Any]:
        """Execute Graded Reflection pattern."""
        print(f"🎯 Graded Reflection Pattern executing: {self.name}")

        # Step 1: ReactAgent reasoning
        reasoning_result = await self.reasoning_agent.arun(input_data)

        # Step 2: SimpleAgentV3 with graded reflection
        structured_result = await self.structuring_agent.arun(
            {"reasoning_output": str(reasoning_result)}
        )

        print(f"✅ Graded Reflection Pattern completed: {self.name}")
        return structured_result


# =============================================================================
# FACTORY FUNCTIONS FOR ALL PATTERNS
# =============================================================================


def create_v3_pattern(
    name: str = "react_structured_v3",
    tools: List = None,
    structured_output_model: Type[BaseModel] = TaskAnalysis,
) -> ReactToStructuredV3:
    """Create V3 pattern: ReactAgent → SimpleAgentV3."""
    return ReactToStructuredV3(
        name=name, tools=tools, structured_output_model=structured_output_model
    )


def create_v4_pattern(
    name: str = "react_structured_v4",
    tools: List = None,
    structured_output_model: Type[BaseModel] = TaskAnalysis,
) -> ReactToStructuredV4:
    """Create V4 pattern: EnhancedMultiAgentV4 composition."""
    return ReactToStructuredV4.create_analysis_workflow(
        name=name, tools=tools, structured_output_model=structured_output_model
    )


def create_reflection_pattern(
    name: str = "react_with_reflection",
    tools: List = None,
    structured_output_model: Type[BaseModel] = TaskAnalysis,
) -> ReactWithReflection:
    """Create Enhanced Base Agent pattern with reflection."""
    return ReactWithReflection(
        name=name, tools=tools, structured_output_model=structured_output_model
    )


def create_graded_reflection_pattern(
    name: str = "react_graded_reflection",
    tools: List = None,
    structured_output_model: Type[BaseModel] = TaskAnalysis,
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
    print("\n🔧 V3 Architecture Pattern Example")
    print("=" * 50)

    workflow = create_v3_pattern(
        name="market_research_v3",
        tools=[web_research, data_analysis],
        structured_output_model=ResearchFindings,
    )

    result = await workflow.arun(
        "Research the impact of AI on small businesses and provide structured findings"
    )

    print(f"\n📋 V3 Result: {type(result).__name__}")
    return result


async def example_v4_pattern():
    """Example: V4 Architecture Pattern."""
    print("\n🚀 V4 Architecture Pattern Example")
    print("=" * 50)

    workflow = create_v4_pattern(
        name="problem_analysis_v4",
        tools=[stakeholder_analysis, data_analysis],
        structured_output_model=ProblemAnalysis,
    )

    result = await workflow.arun(
        "Analyze the problem of customer service delays in our company"
    )

    print(f"\n📋 V4 Result: {type(result).__name__}")
    return result


async def example_reflection_pattern():
    """Example: Enhanced Base Agent with Reflection."""
    print("\n💭 Enhanced Base Agent + Reflection Pattern Example")
    print("=" * 60)

    workflow = create_reflection_pattern(
        name="task_analysis_reflection",
        tools=[web_research, stakeholder_analysis],
        structured_output_model=TaskAnalysis,
    )

    result = await workflow.arun(
        "Analyze the task of implementing a new customer feedback system"
    )

    print(f"\n📋 Reflection Result: Type: {type(result)}")
    if isinstance(result, dict) and "processing_stages" in result:
        print(f"Processing stages: {result['processing_stages']}")
    return result


async def example_graded_reflection_pattern():
    """Example: Graded Reflection Pattern."""
    print("\n📊 Graded Reflection Pattern Example")
    print("=" * 50)

    workflow = create_graded_reflection_pattern(
        name="comprehensive_analysis",
        tools=[web_research, data_analysis, stakeholder_analysis],
        structured_output_model=ResearchFindings,
    )

    result = await workflow.arun(
        "Conduct comprehensive research on sustainable energy adoption in urban areas"
    )

    print(f"\n📋 Graded Reflection Result: Type: {type(result)}")
    if isinstance(result, dict) and "processing_stages" in result:
        print(f"Processing stages: {result['processing_stages']}")
    return result


async def main():
    """Run all pattern examples."""
    print("🎯 Comprehensive ReactAgent → SimpleAgent Patterns")
    print("Demonstrating V3, V4, Enhanced Base Agent, and Reflection patterns")
    print("=" * 80)

    try:
        # Run all patterns
        await example_v3_pattern()
        await example_v4_pattern()
        await example_reflection_pattern()
        await example_graded_reflection_pattern()

        print("\n🎉 All pattern examples completed successfully!")
        print("Each pattern demonstrates different architectural approaches:")
        print("  • V3: Direct ReactAgent → SimpleAgentV3 composition")
        print("  • V4: EnhancedMultiAgentV4 orchestration")
        print("  • Enhanced Base: Using enhanced base agent with reflection")
        print("  • Graded Reflection: Multi-stage quality improvement")

    except Exception as e:
        print(f"❌ Pattern execution failed: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
