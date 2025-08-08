# Archived Agent Files

These files were archived during the agent base consolidation on 2025-08-07.

## Why These Were Archived:

- Consolidating multiple agent base classes into ONE base agent
- Removing version suffixes (V2, V3, etc.)
- Simplifying the agent hierarchy

## Original Files:

- agent.py → Replaced by enhanced_agent.py content
- agent_v2.py → Functionality merged into agent.py
- agent_v3.py → Renamed to agent.py (without V3 suffix)

## Migration Guide:

1. `from haive.agents.base.enhanced_agent import Agent` → `from haive.agents.base.agent import Agent`
2. `SimpleAgentV3` → `SimpleAgent`
3. `SimpleAgentV2` → `SimpleAgent`
