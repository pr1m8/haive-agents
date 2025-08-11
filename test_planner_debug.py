"""Debug the planner prompt issue."""

import asyncio

from haive.core.engine.aug_llm import AugLLMConfig

from haive.agents.planning_v2.base.models import Plan, Task
from haive.agents.planning_v2.base.planner.prompts import planner_prompt
from haive.agents.simple.agent import SimpleAgent


async def test_planner_debug():
    """Test planner with proper context_section handling."""

    # Check the prompt template structure
    print("1. Checking planner_prompt structure:")
    print(f"   Input variables: {planner_prompt.input_variables}")
    print(f"   Partial variables: {planner_prompt.partial_variables}")
    print(f"   Messages: {len(planner_prompt.messages)}")

    # Create engine with structured output
    config = AugLLMConfig(
        temperature=0.3,
        structured_output_model=Plan[Task],
        prompt_template=planner_prompt,
    )

    print("\n2. Checking AugLLMConfig prompt after format instructions:")
    print(f"   Input variables: {config.prompt_template.input_variables}")
    print(f"   Partial variables: {config.prompt_template.partial_variables}")
    print(f"   Messages: {len(config.prompt_template.messages)}")

    # Create agent
    planner = SimpleAgent(name="debug_planner", engine=config)

    print("\n3. Testing simple execution:")
    try:
        result = await planner.arun({"objective": "Test simple objective"})
        print(
            f"   SUCCESS: Generated {len(result.steps) if hasattr(result, 'steps') else 'unknown'} steps"
        )
    except Exception as e:
        print(f"   ERROR: {e}")

        # Let's try providing the missing context_section explicitly
        print("\n4. Testing with explicit context_section:")
        try:
            result = await planner.arun(
                {
                    "objective": "Test simple objective",
                    "context_section": "",  # Explicitly provide empty context
                }
            )
            print(
                f"   SUCCESS: Generated {len(result.steps) if hasattr(result, 'steps') else 'unknown'} steps"
            )
        except Exception as e2:
            print(f"   STILL ERROR: {e2}")


if __name__ == "__main__":
    asyncio.run(test_planner_debug())
