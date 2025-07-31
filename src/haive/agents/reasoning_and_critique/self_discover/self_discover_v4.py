"""Self-Discover V4 - Using SimpleAgentV3 and EnhancedMultiAgentV4.

Clean implementation following CLAUDE.md patterns:
- SimpleAgentV3 for individual agents
- EnhancedMultiAgentV4 for orchestration
- No custom __init__ overrides
- Proper state handling
"""

import asyncio
import traceback
from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.simple.agent_v3 import SimpleAgentV3

# ==========================
# Pydantic Models (Unified)
# ==========================


class SelectedModule(BaseModel):
    """A reasoning module selected for the task."""

    module_number: int = Field(
        description="Module number from the list (1-20)", ge=1, le=20
    )
    module_name: str = Field(description="Name of the reasoning module")
    explanation: str = Field(description="Why this module is relevant")


class ModuleSelection(BaseModel):
    """Result from the selector agent."""

    selected_modules: list[SelectedModule] = Field(
        description="3-5 selected modules", min_length=3, max_length=5
    )

    def to_string(self) -> str:
        """Convert to string for next agent."""
        lines = ["SELECTED MODULES:"]
        for m in self.selected_modules:
            lines.append(f"\n{m.module_number}. {m.module_name}")
            lines.append(f"   Reason: {m.explanation}")
        return "\n".join(lines)


class AdaptedModule(BaseModel):
    """A module adapted for the specific task."""

    module_number: int = Field(description="Original module number")
    adapted_approach: str = Field(description="Task-specific approach")


class AdaptationResult(BaseModel):
    """Result from the adapter agent."""

    adapted_modules: list[AdaptedModule] = Field(description="Adapted modules")

    def to_string(self) -> str:
        """Convert to string for next agent."""
        lines = ["ADAPTED MODULES:"]
        for m in self.adapted_modules:
            lines.append(f"\nModule {m.module_number}:")
            lines.append(f"   {m.adapted_approach}")
        return "\n".join(lines)


class ReasoningStep(BaseModel):
    """A step in the reasoning plan."""

    step: int = Field(description="Step number", ge=1)
    action: str = Field(description="What to do in this step")
    modules: list[int] = Field(description="Module numbers to use")


class ReasoningPlan(BaseModel):
    """Result from the structurer agent."""

    steps: list[ReasoningStep] = Field(description="Reasoning steps")

    def to_string(self) -> str:
        """Convert to string for executor."""
        lines = ["REASONING PLAN:"]
        for s in self.steps:
            lines.append(f"\nStep {s.step}: {s.action}")
            lines.append(f"   Using modules: {s.modules}")
        return "\n".join(lines)


class FinalAnswer(BaseModel):
    """Result from the executor agent."""

    reasoning_process: str = Field(description="Step-by-step reasoning")
    answer: str = Field(description="Final answer")
    confidence: str = Field(
        description="HIGH, MEDIUM, or LOW", pattern="^(HIGH|MEDIUM|LOW)$"
    )


# ==========================
# Default Reasoning Modules
# ==========================

REASONING_MODULES = """1. Critical Thinking: Question assumptions, evaluate evidence
2. Systems Analysis: Break down complex systems and relationships
3. Root Cause Analysis: Identify underlying causes
4. Pattern Recognition: Identify recurring themes and structures
5. Hypothesis Testing: Formulate and test theories
6. Cost-Benefit Analysis: Evaluate trade-offs
7. Risk Assessment: Identify and evaluate risks
8. Design Thinking: User-centered problem solving
9. Analogical Reasoning: Draw insights from similar situations
10. Causal Analysis: Understand cause-effect relationships
11. Scenario Planning: Consider multiple possibilities
12. Constraint Analysis: Identify limitations
13. Optimization: Find best solution within parameters
14. Data Analysis: Extract insights from data
15. Process Analysis: Examine workflows
16. Brainstorming: Generate creative ideas
17. Prioritization: Rank by importance
18. Stakeholder Analysis: Consider perspectives
19. SWOT Analysis: Strengths, weaknesses, opportunities, threats
20. Competitive Analysis: Understand landscape"""


# ==========================
# Agent Creation Functions
# ==========================


def create_selector() -> SimpleAgentV3:
    """Create the module selector agent."""
    return SimpleAgentV3(
        name="selector",
        engine=AugLLMConfig(
            temperature=0.3,
            structured_output_model=ModuleSelection,
            system_message="Select 3-5 reasoning modules most relevant for the task.",
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                (
                    "human",
                    """Available Modules:
{modules}

Task: {task}

Select the most relevant modules and explain why.""",
                ),
            ]
        ),
    )


def create_adapter() -> SimpleAgentV3:
    """Create the module adapter agent."""
    return SimpleAgentV3(
        name="adapter",
        engine=AugLLMConfig(
            temperature=0.5,
            structured_output_model=AdaptationResult,
            system_message="Adapt selected modules to be task-specific.",
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                (
                    "human",
                    """Task: {task}

{selected}

Adapt each module with a specific approach for this task.""",
                ),
            ]
        ),
    )


def create_structurer() -> SimpleAgentV3:
    """Create the plan structurer agent."""
    return SimpleAgentV3(
        name="structurer",
        engine=AugLLMConfig(
            temperature=0.3,
            structured_output_model=ReasoningPlan,
            system_message="Create a step-by-step reasoning plan.",
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                (
                    "human",
                    """Task: {task}

{adapted}

Create a step-by-step plan using these modules.""",
                ),
            ]
        ),
    )


def create_executor() -> SimpleAgentV3:
    """Create the plan executor agent."""
    return SimpleAgentV3(
        name="executor",
        engine=AugLLMConfig(
            temperature=0.7,
            structured_output_model=FinalAnswer,
            system_message="Execute the reasoning plan to solve the task.",
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                (
                    "human",
                    """Task: {task}

{plan}

Execute this plan step-by-step and provide the answer.""",
                ),
            ]
        ),
    )


# ==========================
# Main Self-Discover Agent
# ==========================


class SelfDiscoverV4(EnhancedMultiAgentV4):
    """Self-Discover agent using V4 architecture.

    This is a clean implementation that:
    1. Uses SimpleAgentV3 for all agents
    2. Uses EnhancedMultiAgentV4 for orchestration
    3. Properly handles state between agents
    4. No custom __init__ overrides
    """

    def __init__(self, name: str = "self_discover_v4", **kwargs):
        """Initialize with the four agents in sequence."""
        # Create the agents
        agents = [
            create_selector(),
            create_adapter(),
            create_structurer(),
            create_executor(),
        ]

        # Initialize parent with sequential execution
        super().__init__(
            agents=agents, execution_mode="sequential", name=name, **kwargs
        )

    def prepare_initial_state(
        self, task: str, modules: str | None = None
    ) -> dict[str, Any]:
        """Prepare the initial state for execution.

        Args:
            task: The task to solve
            modules: Optional custom modules (defaults to REASONING_MODULES)

        Returns:
            Dict with initial state for the workflow
        """
        if modules is None:
            modules = REASONING_MODULES

        return {
            "task": task,
            "modules": modules,
            "selected": "",  # Will be filled by selector
            "adapted": "",  # Will be filled by adapter
            "plan": "",  # Will be filled by structurer
            "system_message": "You are a helpful assistant.",
        }

    async def solve(self, task: str, modules: str | None = None) -> FinalAnswer:
        """Convenience method to solve a task.

        Args:
            task: The task to solve
            modules: Optional custom reasoning modules

        Returns:
            FinalAnswer with the solution
        """
        # Prepare state
        state = self.prepare_initial_state(task, modules)

        # Run the workflow
        result = await self.arun(state)

        # Extract final answer
        if isinstance(result, dict) and "answer" in result:
            return FinalAnswer(
                reasoning_process=result.get("reasoning_process", ""),
                answer=result["answer"],
                confidence=result.get("confidence", "MEDIUM"),
            )

        # Try to parse the result
        return result


# ==========================
# Convenience Functions
# ==========================


def create_self_discover_v4() -> SelfDiscoverV4:
    """Create a ready-to-use Self-Discover V4 agent."""
    return SelfDiscoverV4()


# ==========================
# Example Usage
# ==========================

if __name__ == "__main__":

    async def main():
        """Example of using Self-Discover V4."""
        # Create agent
        agent = create_self_discover_v4()

        # Example task
        task = """Analyze this SVG path and determine what shape it draws:
<path d="M 55.57,80.69 L 57.38,65.80 M 57.38,65.80 L 48.90,57.46 M 48.90,57.46 L
45.58,47.78 M 45.58,47.78 L 53.25,36.07 L 66.29,48.90 L 78.69,61.09 L 55.57,80.69"/>

Options: (A) circle (B) heptagon (C) hexagon (D) kite (E) line (F) octagon
(G) pentagon (H) rectangle (I) sector (J) triangle"""

        try:
            # Solve the task
            await agent.solve(task)

        except Exception:

            traceback.print_exc()

    asyncio.run(main())
