"""Test AgentSchemaComposer with self-discover agents - DO NOT RUN."""

import sys

sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")

from haive.agents.reasoning_and_critique.self_discover.v2.agent import self_discovery


def test_agent_schema_composer():
    """Test what AgentSchemaComposer should do with agents dict."""
    # Check the agents dict
    agents_dict = self_discovery.agents
    for _name, agent in agents_dict.items():
        if hasattr(agent, "state_schema") and hasattr(
            agent.state_schema, "model_fields"
        ):
            pass
        if hasattr(agent, "engine"):
            pass

    # What AgentSchemaComposer should do:

    # Expected composed fields
    expected_fields = set()
    for _name, agent in agents_dict.items():
        if hasattr(agent, "state_schema") and hasattr(
            agent.state_schema, "model_fields"
        ):
            agent_fields = agent.state_schema.model_fields.keys()
            expected_fields.update(agent_fields)

    # Check current multi-agent state
    multi_state = self_discovery.state_schema
    if hasattr(multi_state, "model_fields"):
        list(multi_state.model_fields.keys())


if __name__ == "__main__":
    test_agent_schema_composer()
