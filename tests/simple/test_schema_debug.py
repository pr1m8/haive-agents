#!/usr/bin/env python3
"""Debug the SimpleAgentV3State schema."""

import asyncio
import json

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import DeepSeekLLMConfig

from haive.agents.simple.agent_v3 import SimpleAgentV3


def test_schema_fields():
    """Test what fields the schema has."""
    print("\n" + "=" * 60)
    print("DEBUG: SimpleAgentV3State Schema Fields")
    print("=" * 60)

    # Create agent
    config = AugLLMConfig(
        temperature=0.1, max_tokens=50, llm_config=DeepSeekLLMConfig()
    )

    agent = SimpleAgentV3(name="test_agent", engine=config, debug=False)  # Less verbose

    # Check state schema
    print(f"\nState schema: {agent.state_schema}")
    print(f"Schema name: {agent.state_schema.__name__}")

    # Check schema fields
    if hasattr(agent.state_schema, "model_fields"):
        print("\nSchema fields:")
        for field_name, field_info in agent.state_schema.model_fields.items():
            print(f"  - {field_name}: {field_info.annotation}")

    # Check input/output schemas
    print(f"\nInput schema: {agent.input_schema}")
    print(f"Output schema: {agent.output_schema}")

    # Try to create an instance
    print("\nTrying to create state instance...")
    try:
        # Try with empty dict
        state1 = agent.state_schema()
        print("✅ Created with empty dict")
        print(f"   Fields: {list(state1.model_dump().keys())}")
    except Exception as e:
        print(f"❌ Failed with empty dict: {e}")

    try:
        # Try with messages
        from langchain_core.messages import HumanMessage

        state2 = agent.state_schema(messages=[HumanMessage(content="test")])
        print("✅ Created with messages")
    except Exception as e:
        print(f"❌ Failed with messages: {e}")

    # Check how input is prepared
    print("\nChecking input preparation...")
    test_input = "Hello world"
    prepared = agent._prepare_input(test_input)
    print(f"Input type: {type(prepared)}")
    print(f"Prepared input: {prepared}")

    return agent


if __name__ == "__main__":
    agent = test_schema_fields()
