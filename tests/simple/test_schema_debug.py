#!/usr/bin/env python3
"""Debug the SimpleAgentV3State schema."""

from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import DeepSeekLLMConfig


def test_schema_fields():
    """Test what fields the schema has."""
    # Create agent
    config = AugLLMConfig(temperature=0.1, max_tokens=50, llm_config=DeepSeekLLMConfig())

    agent = SimpleAgentV3(name="test_agent", engine=config, debug=False)  # Less verbose

    # Check state schema

    # Check schema fields
    if hasattr(agent.state_schema, "model_fields"):
        for _field_name, _field_info in agent.state_schema.model_fields.items():
            pass

    # Check input/output schemas

    # Try to create an instance
    try:
        # Try with empty dict
        agent.state_schema()
    except Exception:
        pass

    try:
        # Try with messages
        from langchain_core.messages import HumanMessage

        agent.state_schema(messages=[HumanMessage(content="test")])
    except Exception:
        pass

    # Check how input is prepared
    test_input = "Hello world"
    agent._prepare_input(test_input)

    return agent


if __name__ == "__main__":
    agent = test_schema_fields()
