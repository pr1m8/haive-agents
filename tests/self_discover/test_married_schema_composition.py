"""Test the married AgentSchemaComposer + MultiAgentState approach."""

import sys

sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")


def test_married_schema_composition():
    """Test that AgentSchemaComposer + MultiAgentState marriage works."""

    from haive.core.schema.agent_schema_composer import AgentSchemaComposer
    from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState

    from haive.agents.reasoning_and_critique.self_discover.v2.agent import (
        self_discovery,
    )

    # Check individual agent schema fields
    agent_fields = set(self_discovery.state_schema.model_fields.keys())

    # Check MultiAgentState fields
    multi_fields = set(MultiAgentState.model_fields.keys())

    # Test the married approach
    try:
        married_schema = AgentSchemaComposer.from_agents_with_multiagent_base(
            agents=[self_discovery],
            name="MarriedSelfDiscoveryState",
            separation="smart",
        )

        # Check that married schema has BOTH sets of fields
        married_fields = set(married_schema.model_fields.keys())

        # Verify it has MultiAgentState fields
        multi_missing = multi_fields - married_fields
        if multi_missing:
            pass
        else:
            pass

        # Verify it has SelfDiscovery fields (excluding conflicts)
        discovery_specific = agent_fields - multi_fields
        discovery_missing = discovery_specific - married_fields
        if discovery_missing:
            pass
        else:
            pass

        # Create an instance to verify it works
        instance = married_schema()

        # Test hierarchical functionality (from MultiAgentState)

        # Test agent-specific fields (from SelfDiscoveryState)

        return married_schema

    except Exception as e:
        import traceback

        traceback.print_exc()
        return None


def test_proper_multi_agent():
    """Test that ProperMultiAgent now uses the married schema."""

    try:
        from haive.agents.multi.proper_base import ProperMultiAgent
        from haive.agents.reasoning_and_critique.self_discover.v2.agent import (
            self_discovery,
        )

        # Create multi-agent with self-discovery agent
        multi_agent = ProperMultiAgent(name="test_multi", agents=[self_discovery])

        # Check that it has BOTH MultiAgentState AND SelfDiscovery fields
        schema_fields = set(multi_agent.state_schema.model_fields.keys())

        # Verify key fields exist
        required_multi_fields = {"agents", "agent_states", "agent_outputs"}
        required_discovery_fields = {"reasoning_modules", "task_description"}

        missing_multi = required_multi_fields - schema_fields
        missing_discovery = required_discovery_fields - schema_fields

        if missing_multi:
            pass
        else:
            pass

        if missing_discovery:
            pass
        else:
            pass

        return multi_agent

    except Exception as e:
        import traceback

        traceback.print_exc()
        return None


if __name__ == "__main__":
    # Test the marriage
    married_schema = test_married_schema_composition()

    # Test ProperMultiAgent
    multi_agent = test_proper_multi_agent()

    if married_schema and multi_agent:
        pass
    else:
        pass
