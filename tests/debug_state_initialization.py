"""Debug state initialization for multi-agent."""

import sys

sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")

from haive.core.engine.aug_llm import AugLLMConfig

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


# Check agents dict
for _name, _agent in multi.agents.items():
    pass

# Check state schema

# Check if agents field exists in schema
if "agents" in multi.state_schema.model_fields:
    field_info = multi.state_schema.model_fields["agents"]

# Create initial state
initial_state = multi.get_initial_state()

# Check agents in initial state
if "agents" in initial_state:
    if isinstance(initial_state["agents"], dict):
        pass
else:
    pass

# Create state instance
try:
    state_instance = multi.state_schema(**initial_state)

    # Check agents field in instance
    if hasattr(state_instance, "agents"):
        if isinstance(state_instance.agents, dict):
            pass
    else:
        pass

except Exception:
    import traceback

    traceback.print_exc()
