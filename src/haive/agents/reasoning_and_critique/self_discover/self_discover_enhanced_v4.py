"""Self-Discover Agent Implementation following LangGraph tutorial pattern.

Based on the official LangGraph Self-Discover tutorial:
https://langchain-ai.github.io/langgraph/tutorials/self-discover/self-discover/

This implementation follows the exact pattern from the tutorial with proper
state management and structured output parsing.
"""

from typing import Any, Dict, Optional, TypedDict

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from haive.agents.simple.agent_v3 import SimpleAgentV3

# ==========================
# State Management - Following LangGraph Tutorial Pattern
# ==========================


class SelfDiscoverState(TypedDict):
    """State for Self-Discover workflow following LangGraph tutorial."""

    reasoning_modules: str
    task_description: str
    selected_modules: Optional[str]
    adapted_modules: Optional[str]
    reasoning_structure: Optional[str]
    answer: Optional[str]


# ==========================
# Structured Output Models - String-based following tutorial pattern
# ==========================


class ModuleSelectionOutput(BaseModel):
    """Output from module selector - string format."""

    selected_modules: str = Field(
        description="Selected reasoning modules as formatted text"
    )


class AdaptedModulesOutput(BaseModel):
    """Output from module adapter - string format."""

    adapted_modules: str = Field(
        description="Adapted reasoning modules as formatted text"
    )


class ReasoningStructureOutput(BaseModel):
    """Output from structure creator - string format."""

    reasoning_structure: str = Field(
        description="Step-by-step reasoning structure as formatted text"
    )


class FinalAnswerOutput(BaseModel):
    """Output from final reasoner - string format."""

    answer: str = Field(description="The final answer to the task")


# ==========================
# Default Reasoning Modules
# ==========================

DEFAULT_REASONING_MODULES = """1. Pattern Recognition - Identify patterns, shapes, and structures
2. Spatial Analysis - Understand spatial relationships and geometry
3. Logical Reasoning - Apply logical thinking and deduction
4. Mathematical Analysis - Use mathematical concepts and calculations
5. Visual Interpretation - Interpret visual information and diagrams
6. Problem Decomposition - Break complex problems into parts
7. Critical Thinking - Evaluate information and assumptions
8. Systems Analysis - Understand systems and relationships
9. Comparative Analysis - Compare and contrast options
10. Hypothesis Testing - Form and test hypotheses"""


# ==========================
# Self-Discover Agents
# ==========================


class SelfDiscoverSelector(SimpleAgentV3):
    """Agent that selects relevant reasoning modules."""

    name: str = Field(default="sd_selector")

    engine: AugLLMConfig = Field(
        default_factory=lambda: AugLLMConfig(
            temperature=0.3,
            max_tokens=1000,
            structured_output_model=ModuleSelectionOutput,
            system_message="You are an expert at selecting appropriate reasoning strategies for tasks.",
        )
    )

    prompt_template: ChatPromptTemplate = Field(
        default_factory=lambda: ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are an expert at selecting appropriate reasoning strategies for tasks.",
                ),
                ("placeholder", "{messages}"),
            ]
        )
    )


class SelfDiscoverAdapter(SimpleAgentV3):
    """Agent that adapts modules to be task-specific."""

    name: str = Field(default="sd_adapter")

    engine: AugLLMConfig = Field(
        default_factory=lambda: AugLLMConfig(
            temperature=0.5,
            max_tokens=1000,
            structured_output_model=AdaptedModulesOutput,
            system_message="You adapt reasoning modules to be specific for the given task.",
        )
    )

    prompt_template: ChatPromptTemplate = Field(
        default_factory=lambda: ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You adapt reasoning modules to be specific for the given task.",
                ),
                ("human", "{messages}"),
            ]
        )
    )


class SelfDiscoverStructurer(SimpleAgentV3):
    """Agent that creates a structured reasoning plan."""

    name: str = Field(default="sd_structurer")

    engine: AugLLMConfig = Field(
        default_factory=lambda: AugLLMConfig(
            temperature=0.3,
            max_tokens=1500,
            structured_output_model=ReasoningStructureOutput,
            system_message="You create detailed step-by-step reasoning plans.",
        )
    )

    prompt_template: ChatPromptTemplate = Field(
        default_factory=lambda: ChatPromptTemplate.from_messages(
            [
                ("system", "You create detailed step-by-step reasoning plans."),
                ("human", "{messages}"),
            ]
        )
    )


class SelfDiscoverExecutor(SimpleAgentV3):
    """Agent that executes the reasoning plan."""

    name: str = Field(default="sd_executor")

    engine: AugLLMConfig = Field(
        default_factory=lambda: AugLLMConfig(
            temperature=0.7,
            max_tokens=2000,
            structured_output_model=FinalAnswerOutput,
            system_message="You execute reasoning plans to solve tasks step by step.",
        )
    )

    prompt_template: ChatPromptTemplate = Field(
        default_factory=lambda: ChatPromptTemplate.from_messages(
            [
                ("system", "You execute reasoning plans to solve tasks step by step."),
                ("human", "{messages}"),
            ]
        )
    )


# ==========================
# Sequential Workflow
# ==========================


async def run_self_discover_workflow(
    task: str, modules: Optional[str] = None
) -> Dict[str, Any]:
    """Run the Self-Discover workflow sequentially.

    Args:
        task: The task to solve
        modules: Optional custom reasoning modules

    Returns:
        Dict containing the final answer and reasoning
    """
    if modules is None:
        modules = DEFAULT_REASONING_MODULES

    # Create agents
    selector = SelfDiscoverSelector()
    adapter = SelfDiscoverAdapter()
    structurer = SelfDiscoverStructurer()
    executor = SelfDiscoverExecutor()

    # Step 1: Select modules
    print("Step 1: Selecting relevant modules...")
    selector_input = {"available_modules": modules, "task_description": task}

    selector_result = await selector.arun(selector_input)

    # Extract and format selected modules
    selected_modules_text = ""
    if isinstance(selector_result, dict) and "selected_modules" in selector_result:
        output = ModuleSelectionOutput(
            selected_modules=selector_result["selected_modules"]
        )
        selected_modules_text = output.format_as_text()
    elif hasattr(selector_result, "selected_modules"):
        selected_modules_text = selector_result.format_as_text()
    else:
        selected_modules_text = str(selector_result)

    # Step 2: Adapt modules
    print("Step 2: Adapting modules to task...")
    adapter_input = {
        "task_description": task,
        "selected_modules": selected_modules_text,
    }

    adapter_result = await adapter.arun(adapter_input)

    # Extract and format adapted modules
    adapted_modules_text = ""
    if isinstance(adapter_result, dict) and "adapted_modules" in adapter_result:
        output = AdaptedModulesOutput(adapted_modules=adapter_result["adapted_modules"])
        adapted_modules_text = output.format_as_text()
    elif hasattr(adapter_result, "adapted_modules"):
        adapted_modules_text = adapter_result.format_as_text()
    else:
        adapted_modules_text = str(adapter_result)

    # Step 3: Create reasoning plan
    print("Step 3: Creating reasoning plan...")
    structurer_input = {
        "task_description": task,
        "adapted_modules": adapted_modules_text,
    }

    structurer_result = await structurer.arun(structurer_input)

    # Extract and format plan
    reasoning_plan_text = ""
    if isinstance(structurer_result, dict) and "steps" in structurer_result:
        output = ReasoningPlanOutput(steps=structurer_result["steps"])
        reasoning_plan_text = output.format_as_text()
    elif hasattr(structurer_result, "steps"):
        reasoning_plan_text = structurer_result.format_as_text()
    else:
        reasoning_plan_text = str(structurer_result)

    # Step 4: Execute plan
    print("Step 4: Executing plan to solve task...")
    executor_input = {
        "task_description": task,
        "reasoning_structure": reasoning_plan_text,
    }

    executor_result = await executor.arun(executor_input)

    # Extract final answer
    if isinstance(executor_result, dict):
        return executor_result
    elif hasattr(executor_result, "answer"):
        return {
            "answer": executor_result.answer,
            "reasoning_process": executor_result.reasoning_process,
            "confidence": executor_result.confidence,
        }
    else:
        return {"answer": str(executor_result)}


# ==========================
# Example Usage
# ==========================

if __name__ == "__main__":
    import asyncio

    async def main():
        """Example of using Self-Discover Enhanced V4."""

        print("=" * 70)
        print("Self-Discover Enhanced V4 - Using Enhanced Base Agent")
        print("=" * 70)

        # Example 1: Shape recognition
        task1 = """Analyze this SVG path and determine what shape it draws:
<path d="M 10,10 L 40,10 L 40,40 L 10,40 Z"/>

The path uses these commands:
- M 10,10 (Move to point 10,10)
- L 40,10 (Line to point 40,10)  
- L 40,40 (Line to point 40,40)
- L 10,40 (Line to point 10,40)
- Z (Close path back to start)

Options: circle, triangle, square, pentagon, hexagon"""

        print(f"\nTask 1: Shape Recognition")
        print("-" * 50)
        print(task1[:100] + "...")
        print("\nRunning Self-Discover workflow...\n")

        result1 = await run_self_discover_workflow(task1)

        print("\n" + "=" * 50)
        print("RESULT:")
        print("=" * 50)
        if "answer" in result1:
            print(f"Answer: {result1['answer']}")
        if "confidence" in result1:
            print(f"Confidence: {result1['confidence']}")
        if "reasoning_process" in result1:
            print(f"\nReasoning:\n{result1['reasoning_process'][:500]}...")

        # Example 2: Problem solving
        print("\n\n" + "=" * 70)
        print("Example 2: Problem Solving")
        print("=" * 70)

        task2 = "How can I improve team productivity in a remote work environment?"

        print(f"\nTask 2: {task2}")
        print("\nRunning Self-Discover workflow...\n")

        result2 = await run_self_discover_workflow(task2)

        print("\n" + "=" * 50)
        print("RESULT:")
        print("=" * 50)
        if "answer" in result2:
            print(f"Answer: {result2['answer'][:500]}...")
        if "confidence" in result2:
            print(f"\nConfidence: {result2['confidence']}")

    asyncio.run(main())
