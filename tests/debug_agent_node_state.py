"""Debug what state is passed to agent nodes."""

import sys

sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.node.agent_node_v3 import create_agent_node_v3
from langchain_core.messages import HumanMessage

from haive.agents.multi.proper_base import ProperMultiAgent
from haive.agents.simple.agent import SimpleAgent

# Create test agents
agent1 = SimpleAgent(
    name="test1",
    engine=AugLLMConfig(system_message="Test agent 1"),
)

# Create multi-agent
multi = ProperMultiAgent(
    name="multi_test", agents={"test1": agent1}, execution_mode="sequential"
)

print("=" * 80)
print("AGENT NODE STATE DEBUG")
print("=" * 80)

# Check multi-agent setup
print(f"\n1. Multi-agent agents: {list(multi.agents.keys())}")
print(f"2. State schema: {multi.state_schema.__name__}")
print(
    f"3. State schema has 'agents' field: {'agents' in multi.state_schema.model_fields}"
)

# Create test state
print("\n4. Creating test state...")
test_state = multi.state_schema(
    messages=[HumanMessage(content="Test")],
    agents=multi.agents,  # Explicitly set agents
)

print(f"   - State type: {type(test_state).__name__}")
print(f"   - State has agents attr: {hasattr(test_state, 'agents')}")
if hasattr(test_state, "agents"):
    print(f"   - State.agents type: {type(test_state.agents)}")
    print(
        f"   - State.agents keys: {list(test_state.agents.keys()) if isinstance(test_state.agents, dict) else 'Not a dict'}"
    )

# Test node creation
print("\n5. Creating agent node...")
try:
    node = create_agent_node_v3(agent_name="test1", agent=agent1, name="node_test1")
    print(f"   ✅ Node created: {node.name}")

    # Test node execution
    print("\n6. Testing node execution...")
    result = node(test_state)
    print("   ✅ Node executed successfully"y")
    print(f"   Result type: {type(result)}")

except Exception as e:
    print(f"   ❌ Error: {e}")
    import traceback

    traceback.print_exc()

print("\n" + "=" * 80)
