"""Debug state initialization for multi-agent."""

import sys

sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage

from haive.agents.multi.proper_base import ProperMultiAgent
from haive.agents.simple.agent import SimpleAgent

# Create agents
agent1 = SimpleAgent(
    name="agent1",
    engine=AugLLMConfig(system_message="You are agent 1"),
)

agent2 = SimpleAgent(
    name="agent2",
    engine=AugLLMConfig(system_message="You are agent 2"),
)

# Create multi-agent
multi = ProperMultiAgent(
    name="test_multi", agents=[agent1, agent2], execution_mode="sequential"
)

print("=" * 80)
print("MULTI-AGENT DEBUG")
print("=" * 80)

# Check agents dict
print(f"\n1. Multi-agent agents dict: {list(multi.agents.keys())}")
for name, agent in multi.agents.items():
    print(f"   - {name}: {type(agent).__name__}")

# Check state schema
print(f"\n2. State schema: {multi.state_schema.__name__}")
print(f"   Fields: {list(multi.state_schema.model_fields.keys())[:10]}...")

# Check if agents field exists in schema
if "agents" in multi.state_schema.model_fields:
    field_info = multi.state_schema.model_fields["agents"]
    print(f"\n3. 'agents' field in schema:")
    print(f"   - Type: {field_info.annotation}")
    print(f"   - Default factory: {field_info.default_factory}")

# Create initial state
print("\n4. Creating initial state...")
initial_state = multi.get_initial_state()
print(f"   Initial state keys: {list(initial_state.keys())[:10]}...")

# Check agents in initial state
if "agents" in initial_state:
    print(f"\n5. 'agents' in initial state: {type(initial_state['agents'])}")
    if isinstance(initial_state["agents"], dict):
        print(f"   Agent names: {list(initial_state['agents'].keys())}")
else:
    print("\n5. ❌ 'agents' NOT in initial state!")

# Create state instance
print("\n6. Creating state instance...")
try:
    state_instance = multi.state_schema(**initial_state)
    print(f"   ✅ State instance created: {type(state_instance).__name__}")

    # Check agents field in instance
    if hasattr(state_instance, "agents"):
        print(f"   - state.agents type: {type(state_instance.agents)}")
        if isinstance(state_instance.agents, dict):
            print(f"   - state.agents keys: {list(state_instance.agents.keys())}")
    else:
        print("   ❌ No 'agents' attribute on state instance!")

except Exception as e:
    print(f"   ❌ Error creating state instance: {e}")
    import traceback

    traceback.print_exc()

print("\n" + "=" * 80)
