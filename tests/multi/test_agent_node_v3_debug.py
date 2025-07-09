"""Debug test for AgentNodeV3 schema validation issues."""

import asyncio
from typing import List

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState
from haive.core.schema.state_schema import StateSchema
from langchain_core.messages import HumanMessage
from pydantic import Field

# Import Agent for model_rebuild
from haive.agents.base.agent import Agent
from haive.agents.simple.agent import SimpleAgent

# Fix forward reference issue
MultiAgentState.model_rebuild()


class PlannerState(StateSchema):
    """State for planner agent."""

    messages: List = Field(default_factory=list)
    plan: str = Field(default="")
    steps: List[str] = Field(default_factory=list)


async def test_debug_schema_validation():
    """Debug schema validation in AgentNodeV3."""

    print("=== Debugging Schema Validation ===\n")

    # Create simple agent
    planner = SimpleAgent(
        name="planner", engine=AugLLMConfig(temperature=0.7), state_schema=PlannerState
    )

    print(f"Created planner agent: {planner.name}")
    print(f"Agent state schema: {planner.state_schema}")
    print(f"Agent state schema name: {planner.state_schema.__name__}")

    # Check schema fields
    print("\nState schema fields:")
    for field_name, field_info in planner.state_schema.model_fields.items():
        print(
            f"  {field_name}: {field_info.annotation} (default: {field_info.default})"
        )

    # Test direct schema instantiation
    print("\n=== Testing Direct Schema Instantiation ===")
    try:
        test_data = {
            "messages": [HumanMessage(content="test")],
            "plan": "test plan",
            "steps": ["step1", "step2"],
        }

        print(f"Test data: {test_data}")

        # Try to instantiate the schema directly
        schema_instance = planner.state_schema(**test_data)
        print(f"✓ Schema instantiation successful: {schema_instance}")

        # Try to dump back to dict
        dumped = schema_instance.model_dump()
        print(f"✓ Schema dump successful: {dumped}")

    except Exception as e:
        print(f"❌ Schema instantiation failed: {e}")
        print(f"Error type: {type(e)}")

        # Check for engine fields
        print("\nChecking for engine fields in schema:")
        for field_name, field_info in planner.state_schema.model_fields.items():
            if hasattr(field_info.annotation, "__origin__"):
                print(f"  {field_name}: {field_info.annotation} (complex type)")
            else:
                print(f"  {field_name}: {field_info.annotation}")

    # Test MultiAgentState
    print("\n=== Testing MultiAgentState ===")
    try:
        state = MultiAgentState(
            agents=[planner], messages=[HumanMessage(content="test message")]
        )

        print(f"✓ MultiAgentState created successfully")
        print(f"Agent count: {state.agent_count}")
        print(f"Agents: {list(state.agents.keys())}")

        # Try to get agent state
        agent_state = state.get_agent_state("planner")
        print(f"Agent state: {agent_state}")

    except Exception as e:
        print(f"❌ MultiAgentState creation failed: {e}")
        print(f"Error type: {type(e)}")

    return True


if __name__ == "__main__":
    result = asyncio.run(test_debug_schema_validation())
    print(f"\n=== Debug complete ===")
