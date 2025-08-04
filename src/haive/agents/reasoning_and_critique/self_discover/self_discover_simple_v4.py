"""Self-Discover Simple V4 - Minimal implementation with proper state handling.

This version:
- Uses a single shared state dict
- Each agent updates the state with its output
- No complex state transformations
- Clear, simple flow
"""

import asyncio

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.simple.agent_v3 import SimpleAgentV3


# Simple output models
class ModuleList(BaseModel):
    """Selected modules output."""

    modules: str = Field(description="Selected modules as formatted text")


class AdaptedModules(BaseModel):
    """Adapted modules output."""

    adapted: str = Field(description="Adapted modules as formatted text")


class Plan(BaseModel):
    """Reasoning plan output."""

    plan: str = Field(description="Step-by-step plan as formatted text")


class Solution(BaseModel):
    """Final solution output."""

    answer: str = Field(description="The final answer")
    reasoning: str = Field(description="Reasoning process")


# Default modules (simplified)
MODULES = """1. Pattern Analysis - Identify patterns and structures
2. Logical Reasoning - Apply logic to solve problems
3. Visual/Spatial - Understand spatial relationships
4. Mathematical - Apply mathematical concepts
5. Critical Thinking - Evaluate and analyze
6. Problem Decomposition - Break down complex problems
7. Hypothesis Testing - Test assumptions
8. Comparative Analysis - Compare options
9. Causal Reasoning - Understand cause and effect
10. Systems Thinking - See the big picture"""


def create_agents():
    """Create the four agents for Self-Discover."""
    # 1. Selector - picks relevant modules
    selector = SimpleAgentV3(
        name="selector",
        engine=AugLLMConfig(temperature=0.3, structured_output_model=ModuleList),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "Select 3-5 most relevant reasoning modules for the task."),
                (
                    "human",
                    """Available modules:
{modules}

Task: {task}

Select the most relevant modules and format them clearly."""),
            ]
        ))

    # 2. Adapter - makes modules task-specific
    adapter = SimpleAgentV3(
        name="adapter",
        engine=AugLLMConfig(temperature=0.5, structured_output_model=AdaptedModules),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "Adapt the selected modules to be specific for this task."),
                (
                    "human",
                    """Task: {task}

Selected modules:
{modules}

Adapt each module with specific strategies for this task."""),
            ]
        ))

    # 3. Structurer - creates step-by-step plan
    structurer = SimpleAgentV3(
        name="structurer",
        engine=AugLLMConfig(temperature=0.3, structured_output_model=Plan),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "Create a clear step-by-step plan using the adapted modules."),
                (
                    "human",
                    """Task: {task}

Adapted modules:
{adapted}

Create a numbered step-by-step plan to solve this task."""),
            ]
        ))

    # 4. Executor - follows plan to solve
    executor = SimpleAgentV3(
        name="executor",
        engine=AugLLMConfig(temperature=0.7, structured_output_model=Solution),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "Follow the plan to solve the task."),
                (
                    "human",
                    """Task: {task}

Plan:
{plan}

Execute each step and provide the final answer."""),
            ]
        ))

    return [selector, adapter, structurer, executor]


def create_self_discover_simple():
    """Create the Self-Discover agent."""
    agents = create_agents()

    # Use sequential execution
    multi_agent = EnhancedMultiAgentV4(
        agents=agents, execution_mode="sequential", name="self_discover_simple"
    )

    return multi_agent


async def run_self_discover(task: str, modules: str | None = None):
    """Run Self-Discover on a task.

    Args:
        task: The task to solve
        modules: Optional custom modules (defaults to MODULES)

    Returns:
        Dict with the solution
    """
    if modules is None:
        modules = MODULES

    # Create agent
    agent = create_self_discover_simple()

    # Initial state - all fields that will be used
    state = {
        "task": task,
        "modules": modules,
        "adapted": "",  # Will be filled by adapter
        "plan": "",  # Will be filled by structurer
        "answer": "",  # Will be filled by executor
        "reasoning": "",  # Will be filled by executor
    }

    # Run the workflow
    result = await agent.arun(state)

    return result


# Example usage
if __name__ == "__main__":

    async def main():
        task = """What shape does this SVG path draw?
<path d="M 10,10 L 40,10 L 40,40 L 10,40 Z"/>
Options: circle, square, triangle, pentagon"""

        result = await run_self_discover(task)

        if isinstance(result, dict):
            if "answer" in result:
                pass
            if "reasoning" in result:
                pass
        else:
            pass

    asyncio.run(main())
