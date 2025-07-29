"""Self-Discover Working V4 - A working implementation that properly handles agents.

This version creates a working self-discover implementation using the patterns
that are known to work in the codebase.
"""

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from haive.agents.multi import MultiAgent  # Use the default MultiAgent
from haive.agents.simple import SimpleAgent  # Use the default SimpleAgent


# Output models for structured responses
class ModuleSelection(BaseModel):
    """Output from selector agent."""

    modules: str = Field(description="Selected modules formatted as text")


class AdaptedModules(BaseModel):
    """Output from adapter agent."""

    adapted: str = Field(description="Adapted modules formatted as text")


class ReasoningPlan(BaseModel):
    """Output from structurer agent."""

    plan: str = Field(description="Step-by-step plan formatted as text")


class FinalAnswer(BaseModel):
    """Output from executor agent."""

    answer: str = Field(description="The final answer to the task")
    explanation: str = Field(description="Brief explanation of the answer")


# Default reasoning modules
DEFAULT_MODULES = """1. Pattern Recognition - Identify patterns and structures
2. Logical Reasoning - Apply logical thinking
3. Spatial Analysis - Understand spatial relationships
4. Mathematical Thinking - Apply mathematical concepts
5. Critical Analysis - Evaluate and analyze information
6. Problem Decomposition - Break down complex problems
7. Hypothesis Testing - Test assumptions
8. Comparative Analysis - Compare different options
9. Causal Reasoning - Understand cause and effect
10. Systems Thinking - See the whole picture"""


def create_self_discover_agents():
    """Create the four agents for Self-Discover workflow."""

    # 1. Module Selector Agent
    selector = SimpleAgent(
        name="module_selector",
        engine=AugLLMConfig(
            temperature=0.3,
            structured_output_model=ModuleSelection,
            system_message="You select the most relevant reasoning modules for solving tasks.",
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                (
                    "human",
                    """Available reasoning modules:
{modules}

Task to solve: {task}

Select 3-5 most relevant modules for this task and explain your choices.""",
                ),
            ]
        ),
    )

    # 2. Module Adapter Agent
    adapter = SimpleAgent(
        name="module_adapter",
        engine=AugLLMConfig(
            temperature=0.5,
            structured_output_model=AdaptedModules,
            system_message="You adapt reasoning modules to be specific for the given task.",
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                (
                    "human",
                    """Task: {task}

Selected modules:
{modules}

Adapt each module with specific strategies for solving this particular task.""",
                ),
            ]
        ),
    )

    # 3. Plan Structurer Agent
    structurer = SimpleAgent(
        name="plan_structurer",
        engine=AugLLMConfig(
            temperature=0.3,
            structured_output_model=ReasoningPlan,
            system_message="You create structured step-by-step plans for problem solving.",
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                (
                    "human",
                    """Task: {task}

Adapted modules:
{adapted}

Create a clear, numbered step-by-step plan using these modules to solve the task.""",
                ),
            ]
        ),
    )

    # 4. Plan Executor Agent
    executor = SimpleAgent(
        name="plan_executor",
        engine=AugLLMConfig(
            temperature=0.7,
            structured_output_model=FinalAnswer,
            system_message="You execute reasoning plans to solve tasks.",
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                (
                    "human",
                    """Task: {task}

Reasoning plan:
{plan}

Follow the plan step by step to solve the task. Provide a clear answer.""",
                ),
            ]
        ),
    )

    return {
        "module_selector": selector,
        "module_adapter": adapter,
        "plan_structurer": structurer,
        "plan_executor": executor,
    }


def create_self_discover_workflow():
    """Create the Self-Discover multi-agent workflow."""
    agents = create_self_discover_agents()

    # Create MultiAgent with sequential execution
    # Using dict format which is known to work
    workflow = MultiAgent(name="self_discover_workflow", agents=agents)

    return workflow


async def solve_with_self_discover(task: str, modules: str = None):
    """Solve a task using Self-Discover workflow.

    Args:
        task: The task to solve
        modules: Optional custom reasoning modules

    Returns:
        The final answer
    """
    if modules is None:
        modules = DEFAULT_MODULES

    # Create the workflow
    workflow = create_self_discover_workflow()

    # Prepare initial state
    initial_state = {
        "task": task,
        "modules": modules,
        "adapted": "",
        "plan": "",
        "system_message": "You are a helpful assistant.",
    }

    # Run the workflow
    try:
        result = await workflow.arun(initial_state)

        # Extract the answer
        if isinstance(result, dict):
            return result
        else:
            return {"answer": str(result)}

    except Exception as e:
        return {"error": str(e)}


# Example usage
if __name__ == "__main__":
    import asyncio

    async def main():
        """Example of using Self-Discover workflow."""

        # Test case 1: Shape recognition
        print("=" * 60)
        print("Self-Discover Working V4 - Shape Recognition")
        print("=" * 60)

        task1 = """What shape does this SVG path draw?
<path d="M 10,10 L 50,10 L 50,50 L 10,50 Z"/>
The path starts at (10,10), goes to (50,10), then to (50,50), then to (10,50), and closes.
Options: circle, triangle, square, pentagon, hexagon"""

        print(f"\nTask: {task1}")
        print("\nRunning Self-Discover workflow...")

        result1 = await solve_with_self_discover(task1)

        print("\nResult:")
        if "answer" in result1:
            print(f"Answer: {result1['answer']}")
        if "explanation" in result1:
            print(f"Explanation: {result1['explanation']}")
        if "error" in result1:
            print(f"Error: {result1['error']}")

        # Test case 2: Problem solving
        print("\n" + "=" * 60)
        print("Self-Discover Working V4 - Problem Solving")
        print("=" * 60)

        task2 = "How can I reduce plastic waste in my daily life?"

        print(f"\nTask: {task2}")
        print("\nRunning Self-Discover workflow...")

        result2 = await solve_with_self_discover(task2)

        print("\nResult:")
        if "answer" in result2:
            print(f"Answer: {result2['answer'][:300]}...")
        if "error" in result2:
            print(f"Error: {result2['error']}")

    asyncio.run(main())
