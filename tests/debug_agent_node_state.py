"""Debug what state is passed to agent nodes."""

import sys


sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")

from langchain_core.messages import HumanMessage

from haive.agents.multi.proper_base import ProperMultiAgent
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.node.agent_node_v3 import create_agent_node_v3


# Create test agents
agent1 = SimpleAgent(
    name="test1",
    engine=AugLLMConfig(system_message="Test agent 1"),
)

# Create multi-agent
multi = ProperMultiAgent(
    name="multi_test", agents={"test1": agent1}, execution_mode="sequential"
)


# Check multi-agent setup

# Create test state
test_state = multi.state_schema(
    messages=[HumanMessage(content="Test")],
    agents=multi.agents,  # Explicitly set agents
)

if hasattr(test_state, "agents"):
    pass

# Test node creation
try:
    node = create_agent_node_v3(agent_name="test1", agent=agent1, name="node_test1")

    # Test node execution
    result = node(test_state)

except Exception:
    import traceback

    traceback.print_exc()
