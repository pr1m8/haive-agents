"""Check the agents dict structure."""

import sys


sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")

from haive.agents.reasoning_and_critique.self_discover.v2.agent import self_discovery


for _agent_name, agent in self_discovery.agents.items():
    if hasattr(agent, "engine"):
        pass
    if hasattr(agent, "engines"):
        pass

for _engine_name, engine in self_discovery.engines.items():
    if hasattr(engine, "name"):
        pass
