"""Debug script to trace why planner is getting wrong input."""

import asyncio

from haive.core.engine.aug_llm import AugLLMConfig

from haive.agents.planning_v2.base.models import Plan, Task
from haive.agents.planning_v2.base.planner.models import TaskPlan
from haive.agents.planning_v2.base.planner.prompts import planner_prompt
from haive.agents.simple import SimpleAgent


async def debug_planner_input():
    """Debug what input the planner is receiving."""
    print("=== DEBUG: Planner Input Analysis ===\n")

    # Create engine with Plan[Task]
    engine = AugLLMConfig(temperature=0.3, structured_output_model=Plan[Task])

    # Create planner
    planner = SimpleAgent(
        name="test_planner", engine=engine, prompt_template=planner_prompt
    )

    # Check initial state
    print(f"1. Planner name: {planner.name}")
    print(f"2. Engine structured_output_model: {engine.structured_output_model}")
    print(
        f"3. Agent structured_output_model: {getattr(planner, 'structured_output_model', None)}"
    )
    print(f"4. Prompt template variables: {planner_prompt.input_variables}")
    print(f"5. Prompt template partial variables: {planner_prompt.partial_variables}")

    # Check what the prompt looks like with our input
    input_data = {"objective": "Build a simple REST API for a todo list"}
    print(f"\n6. Input data: {input_data}")

    try:
        # Format the prompt to see what it generates
        formatted = planner_prompt.format(**input_data)
        print(f"\n7. Formatted prompt preview (first 500 chars):\n{formatted[:500]}...")
    except Exception as e:
        print(f"\n7. Error formatting prompt: {e}")

    # Run the agent with debug enabled
    print("\n8. Running agent...\n")
    planner.debug = True  # Enable debug mode

    result = await planner.arun(input_data)

    print(f"\n9. Result type: {type(result)}")
    print(f"10. Result content: {result}")

    return result


if __name__ == "__main__":
    asyncio.run(debug_planner_input())
