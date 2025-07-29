"""Self-Discover Sequential Agent V2 - Proper implementation following CLAUDE.md patterns.

This implementation:
1. Uses SimpleAgentV3 for enhanced features
2. No custom __init__ overrides
3. Uses EnhancedMultiAgentV4 for sequential composition
4. Consolidates Pydantic models to avoid conflicts
5. Follows "no mocks" testing philosophy
"""

from typing import List

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field, field_validator

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.simple.agent_v3 import SimpleAgentV3


# Consolidated Pydantic Models (fixing conflicts)
class SelectedModule(BaseModel):
    """A reasoning module selected for a specific problem."""

    module_number: int = Field(
        description="The module number from the available list (1-20)"
    )
    module_name: str = Field(description="Name or brief description of the module")
    relevance_explanation: str = Field(
        description="Why this module is relevant for the task"
    )
    contribution: str = Field(
        description="How this module will contribute to solving the task"
    )


class ModuleSelectionResult(BaseModel):
    """Result of the module selection stage."""

    task_summary: str = Field(description="Brief summary of the task being analyzed")
    selected_modules: List[SelectedModule] = Field(
        description="List of selected reasoning modules (3-5 modules)"
    )
    selection_rationale: str = Field(
        description="Overall rationale for the module selection"
    )

    @field_validator("selected_modules")
    @classmethod
    def validate_modules(cls, modules: List[SelectedModule]) -> List[SelectedModule]:
        """Ensure we have 3-5 modules."""
        if len(modules) < 3:
            raise ValueError("At least 3 modules must be selected")
        if len(modules) > 5:
            raise ValueError("Maximum 5 modules should be selected")
        return modules

    def format_for_adapter(self) -> str:
        """Format selected modules for the adapter stage."""
        formatted = f"TASK: {self.task_summary}\n\n"
        formatted += "SELECTED MODULES:\n"
        for module in self.selected_modules:
            formatted += f"\n{module.module_number}. {module.module_name}\n"
            formatted += f"   Relevance: {module.relevance_explanation}\n"
            formatted += f"   Contribution: {module.contribution}\n"
        return formatted


class AdaptedModule(BaseModel):
    """An adapted version of a reasoning module for a specific task."""

    module_number: int = Field(description="Original module number")
    module_name: str = Field(description="Original module name")
    adapted_description: str = Field(
        description="Task-specific adaptation of this module"
    )
    application_strategy: str = Field(
        description="Specific strategy for applying this module to the task"
    )


class ModuleAdaptationResult(BaseModel):
    """Result of the module adaptation stage."""

    adapted_modules: List[AdaptedModule] = Field(
        description="List of adapted reasoning modules"
    )

    def format_for_structurer(self) -> str:
        """Format adapted modules for the structurer stage."""
        formatted = "ADAPTED MODULES FOR TASK:\n"
        for module in self.adapted_modules:
            formatted += f"\n{module.module_number}. {module.module_name} (Adapted)\n"
            formatted += f"   Task-Specific: {module.adapted_description}\n"
            formatted += f"   Application: {module.application_strategy}\n"
        return formatted


class ReasoningStep(BaseModel):
    """A step in the reasoning plan."""

    step_number: int = Field(description="Sequential step number")
    description: str = Field(description="What to determine or analyze in this step")
    modules_used: List[int] = Field(
        default_factory=list, description="Module numbers used in this step"
    )
    expected_output: str = Field(description="What this step should produce")


class ReasoningStructure(BaseModel):
    """A structured reasoning plan."""

    steps: List[ReasoningStep] = Field(
        description="Sequential steps in the reasoning plan"
    )

    @field_validator("steps")
    @classmethod
    def validate_steps(cls, steps: List[ReasoningStep]) -> List[ReasoningStep]:
        """Ensure steps are properly numbered."""
        for i, step in enumerate(steps, 1):
            if step.step_number != i:
                raise ValueError(f"Step {i} has incorrect number: {step.step_number}")
        return steps

    def format_for_executor(self) -> str:
        """Format reasoning structure for the executor."""
        formatted = "REASONING PLAN:\n"
        for step in self.steps:
            formatted += f"\nStep {step.step_number}: {step.description}\n"
            if step.modules_used:
                formatted += f"   Using modules: {step.modules_used}\n"
            formatted += f"   Expected output: {step.expected_output}\n"
        return formatted


class ExecutionStep(BaseModel):
    """A completed step in the reasoning process."""

    step_number: int = Field(description="Step number")
    description: str = Field(description="What was analyzed")
    reasoning: str = Field(description="Detailed reasoning for this step")
    conclusion: str = Field(description="Key conclusion from this step")


class ReasoningExecution(BaseModel):
    """Complete reasoning execution with all steps and final answer."""

    completed_steps: List[ExecutionStep] = Field(
        description="List of completed reasoning steps"
    )
    final_answer: str = Field(description="Final answer to the problem")
    confidence_level: str = Field(description="Confidence level: HIGH, MEDIUM, or LOW")
    explanation: str = Field(description="Brief explanation of the final answer")


# Default reasoning modules
DEFAULT_REASONING_MODULES = """1. Critical Thinking: Question assumptions, identify biases, evaluate evidence
2. Systems Analysis: Break down complex systems, identify components and relationships
3. Root Cause Analysis: Identify underlying causes of problems or phenomena
4. Stakeholder Analysis: Identify and understand different perspectives and interests
5. SWOT Analysis: Analyze strengths, weaknesses, opportunities, and threats
6. Cost-Benefit Analysis: Evaluate trade-offs and resource allocation
7. Risk Assessment: Identify and evaluate potential risks and mitigation strategies
8. Design Thinking: User-centered approach to innovation and problem-solving
9. Analogical Reasoning: Draw insights from similar situations or domains
10. Causal Analysis: Understand cause-and-effect relationships
11. Scenario Planning: Consider multiple future possibilities and outcomes
12. Constraint Analysis: Identify limitations and work within boundaries
13. Optimization: Find the best solution within given parameters
14. Pattern Recognition: Identify recurring themes, trends, or structures
15. Hypothesis Testing: Formulate and test explanatory theories
16. Brainstorming: Generate creative ideas and solutions
17. Prioritization: Rank options by importance or impact
18. Process Analysis: Examine workflows and procedures for improvement
19. Competitive Analysis: Understand competitive landscape and positioning
20. Data Analysis: Extract insights from quantitative and qualitative data"""


# Create individual agents using Field defaults (no __init__ override)
def create_selector_agent() -> SimpleAgentV3:
    """Create the selector agent with proper configuration."""
    return SimpleAgentV3(
        name="self_discover_selector",
        engine=AugLLMConfig(
            temperature=0.3,
            max_tokens=1500,
            structured_output_model=ModuleSelectionResult,
            system_message="You are an expert at analyzing tasks and selecting appropriate reasoning strategies.",
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                (
                    "human",
                    """Analyze the following task and select 3-5 reasoning modules that would be most effective.

Available Reasoning Modules:
{available_modules}

Task to Analyze:
{task_description}

Select the most relevant modules and explain your choices.""",
                ),
            ]
        ),
    )


def create_adapter_agent() -> SimpleAgentV3:
    """Create the adapter agent with proper configuration."""
    return SimpleAgentV3(
        name="self_discover_adapter",
        engine=AugLLMConfig(
            temperature=0.5,
            max_tokens=1500,
            structured_output_model=ModuleAdaptationResult,
            system_message="You are an expert at customizing reasoning strategies for specific tasks.",
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                (
                    "human",
                    """Adapt the selected reasoning modules to be specifically tailored for this task.

{selected_modules_formatted}

Create task-specific versions of each module with concrete application strategies.""",
                ),
            ]
        ),
    )


def create_structurer_agent() -> SimpleAgentV3:
    """Create the structurer agent with proper configuration."""
    return SimpleAgentV3(
        name="self_discover_structurer",
        engine=AugLLMConfig(
            temperature=0.3,
            max_tokens=2000,
            structured_output_model=ReasoningStructure,
            system_message="You are an expert at creating step-by-step reasoning plans.",
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                (
                    "human",
                    """Create a detailed step-by-step reasoning plan using the adapted modules.

{adapted_modules_formatted}

Original Task:
{task_description}

Design a comprehensive reasoning plan with clear steps that will lead to solving this task.""",
                ),
            ]
        ),
    )


def create_executor_agent() -> SimpleAgentV3:
    """Create the executor agent with proper configuration."""
    return SimpleAgentV3(
        name="self_discover_executor",
        engine=AugLLMConfig(
            temperature=0.7,
            max_tokens=3000,
            structured_output_model=ReasoningExecution,
            system_message="You are an expert problem solver who follows structured reasoning plans.",
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                (
                    "human",
                    """Execute the following reasoning plan to solve the task.

{reasoning_plan_formatted}

Original Task:
{task_description}

Work through each step carefully and provide your final answer.""",
                ),
            ]
        ),
    )


def create_self_discover_sequential() -> EnhancedMultiAgentV4:
    """Create the complete Self-Discover sequential workflow.

    This follows the proper pattern from CLAUDE.md:
    - Uses EnhancedMultiAgentV4 for composition
    - No custom classes or __init__ overrides
    - Clear sequential execution
    - Proper state handling between agents

    Returns:
        EnhancedMultiAgentV4 configured for Self-Discover workflow
    """
    # Create the four agents
    selector = create_selector_agent()
    adapter = create_adapter_agent()
    structurer = create_structurer_agent()
    executor = create_executor_agent()

    # Compose into sequential workflow
    return EnhancedMultiAgentV4(
        agents=[selector, adapter, structurer, executor],
        execution_mode="sequential",
        name="self_discover_sequential_v2",
    )


# Example usage
if __name__ == "__main__":
    import asyncio

    async def main():
        """Example of using the Self-Discover sequential agent."""
        # Create the agent
        self_discover = create_self_discover_sequential()

        # Example task
        task = """This SVG path element <path d="M 55.57,80.69 L 57.38,65.80 M 57.38,65.80 L 48.90,57.46 M 48.90,57.46 L
45.58,47.78 M 45.58,47.78 L 53.25,36.07 L 66.29,48.90 L 78.69,61.09 L 55.57,80.69"/> draws a:
(A) circle (B) heptagon (C) hexagon (D) kite (E) line (F) octagon (G) pentagon (H) rectangle (I) sector (J) triangle"""

        # Prepare input
        initial_state = {
            "available_modules": DEFAULT_REASONING_MODULES,
            "task_description": task,
            "selected_modules_formatted": "",  # Will be populated by selector
            "adapted_modules_formatted": "",  # Will be populated by adapter
            "reasoning_plan_formatted": "",  # Will be populated by structurer
        }

        # Execute the workflow
        result = await self_discover.arun(initial_state)

        # The result will contain the final execution from all four agents
        print("Self-Discover Result:")
        print(result)

    # Run the example
    asyncio.run(main())
