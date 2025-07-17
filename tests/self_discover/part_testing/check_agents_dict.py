"""Check the agents dict structure."""

import sys

sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")

from haive.agents.reasoning_and_critique.self_discover.v2.agent import self_discovery

print("🔍 Checking agents dict structure...")
print(f"Multi-agent name: {self_discovery.name}")
print(f"Number of agents: {len(self_discovery.agents)}")
print(f"Number of engines: {len(self_discovery.engines)}")

print(f"\nAgents dict:")
for agent_name, agent in self_discovery.agents.items():
    print(f"  {agent_name}: {type(agent).__name__}")
    if hasattr(agent, "engine"):
        print(f"    Engine: {type(agent.engine).__name__}")
        print(f"    Engine name: {agent.engine.name}")
    if hasattr(agent, "engines"):
        print(f"    Engines: {len(agent.engines)}")

print(f"\nEngines dict:")
for engine_name, engine in self_discovery.engines.items():
    print(f"  {engine_name}: {type(engine).__name__}")
    if hasattr(engine, "name"):
        print(f"    Name: {engine.name}")

print(f"\nProblem: Should have 4 agents, each with 1 engine = 4 engines total")
print(
    f"Actual: {len(self_discovery.agents)} agents, {len(self_discovery.engines)} engines"
)
