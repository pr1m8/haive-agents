"""Test AgentSchemaComposer with self-discover agents - DO NOT RUN."""

import sys

sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")

from haive.agents.reasoning_and_critique.self_discover.v2.agent import self_discovery


def test_agent_schema_composer():
    """Test what AgentSchemaComposer should do with agents dict."""

    print("🔍 Testing AgentSchemaComposer with agents dict...")

    # Check the agents dict
    agents_dict = self_discovery.agents
    print(f"Agents dict: {len(agents_dict)} agents")
    for name, agent in agents_dict.items():
        print(f"  {name}: {type(agent).__name__}")
        if hasattr(agent, "state_schema"):
            print(f"    State schema: {agent.state_schema.__name__}")
            if hasattr(agent.state_schema, "model_fields"):
                print(f"    Fields: {list(agent.state_schema.model_fields.keys())}")
        if hasattr(agent, "engine"):
            print(f"    Engine: {agent.engine.name}")
        print()

    # What AgentSchemaComposer should do:
    print("🏗️  What AgentSchemaComposer should do:")
    print("1. Take agents dict as input")
    print("2. Get state schema from each agent")
    print("3. Compose fields from all agent state schemas")
    print("4. Create unified MultiAgentState with all fields")
    print("5. Handle field conflicts/namespacing")

    # Expected composed fields
    expected_fields = set()
    for name, agent in agents_dict.items():
        if hasattr(agent, "state_schema") and hasattr(
            agent.state_schema, "model_fields"
        ):
            agent_fields = agent.state_schema.model_fields.keys()
            expected_fields.update(agent_fields)
            print(f"  Agent {name} contributes: {list(agent_fields)}")

    print(f"\nExpected composed fields: {sorted(expected_fields)}")
    print(f"Expected field count: {len(expected_fields)}")

    # Check current multi-agent state
    multi_state = self_discovery.state_schema
    print(f"\nCurrent multi-agent state: {multi_state.__name__}")
    if hasattr(multi_state, "model_fields"):
        current_fields = list(multi_state.model_fields.keys())
        print(f"Current fields: {current_fields}")
        print(f"Current field count: {len(current_fields)}")

    print("\n🎯 Problem: MultiAgentState doesn't have agent-specific fields!")
    print("    Solution: AgentSchemaComposer should compose from agents dict")


if __name__ == "__main__":
    print("⚠️  This is a test script - DO NOT RUN the agent!")
    test_agent_schema_composer()
