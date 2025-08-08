"""Simple debug to trace field naming without pdb."""

import asyncio

from haive.core.engine.aug_llm import AugLLMConfig

from haive.agents.base.structured_output_handler import StructuredOutputHandler
from haive.agents.planning_v2.base.models import Plan, Task
from haive.agents.planning_v2.base.planner.models import TaskPlan
from haive.agents.planning_v2.base.planner.prompts import planner_prompt
from haive.agents.simple import SimpleAgent


def test_field_naming():
    """Test field name generation for different Plan variants."""
    print("=== Field Name Generation Test ===\n")

    # Test 1: Generic Plan[Task]
    generic_plan = Plan[Task]
    handler1 = StructuredOutputHandler(generic_plan)
    print(f"1. Plan[Task]:")
    print(f"   Raw name: {generic_plan.__name__}")
    print(f"   Field name: {handler1.field_name}")
    print(f"   Common fields: {handler1.common_fields[:3]}...")  # First 3 only

    # Test 2: Concrete TaskPlan
    handler2 = StructuredOutputHandler(TaskPlan)
    print(f"\n2. TaskPlan:")
    print(f"   Raw name: {TaskPlan.__name__}")
    print(f"   Field name: {handler2.field_name}")
    print(f"   Common fields: {handler2.common_fields[:3]}...")  # First 3 only

    # Test 3: Base Plan class
    handler3 = StructuredOutputHandler(Plan)
    print(f"\n3. Plan (base):")
    print(f"   Raw name: {Plan.__name__}")
    print(f"   Field name: {handler3.field_name}")
    print(f"   Common fields: {handler3.common_fields[:3]}...")  # First 3 only


async def test_agent_execution():
    """Test what actually gets stored by the agent."""
    print("\n=== Agent Execution Test ===\n")

    # Create agent with Plan[Task]
    engine = AugLLMConfig(temperature=0.3, structured_output_model=Plan[Task])

    planner = SimpleAgent(
        name="test_planner", engine=engine, prompt_template=planner_prompt
    )

    print(f"Agent name: {planner.name}")
    print(f"Engine structured_output_model: {engine.structured_output_model}")
    print(
        f"Agent structured_output_model: {getattr(planner, 'structured_output_model', None)}"
    )

    # Run the agent
    result = await planner.arun(
        {"objective": "Build a simple REST API for a todo list"}
    )

    print(f"\nResult type: {type(result)}")
    print(f"Is dict?: {isinstance(result, dict)}")
    print(f"Is Plan?: {isinstance(result, Plan)}")

    if isinstance(result, dict):
        print(f"Dict keys: {list(result.keys())}")
        # Check for various possible field names
        possible_fields = [
            "plan_result",
            "plan_task_generic_result",
            "taskplan_result",
            "structured_output",
            "output",
            "result",
        ]
        for field in possible_fields:
            if field in result:
                print(f"Found field '{field}': {type(result[field])}")

    return result


if __name__ == "__main__":
    test_field_naming()
    result = asyncio.run(test_agent_execution())
