# Working Dynamic Supervisor Implementations Comparison

## Overview

There are 3 working dynamic supervisor implementations in the examples directory. All the 132+ files in src/ are broken.

## 1. Registry-Based Dynamic Supervisor

**File**: `examples/dynamic_supervisor/working_registry_supervisor.py`

### Key Features:

- **AgentRegistry**: Stores inactive agents that can be activated on demand
- **AgentInfo**: Metadata about each agent (name, description, capability, active status)
- **Active/Inactive Management**: Agents can be activated/deactivated
- **Capability Search**: `search_agents_by_capability()` finds matching agents

### State Structure:

```python
class RegistrySupervisorState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    active_agents: Dict[str, AgentInfo]  # Currently active agents
    agent_registry: AgentRegistry  # Registry of all available agents
    next_agent: str
    agent_task: str
    agent_response: str
```

### How it Works:

1. Agents are registered in the AgentRegistry (inactive by default)
2. When a task comes in, supervisor checks active agents first
3. If no active agent matches, searches registry by capability
4. Activates matching agent from registry and adds to active_agents
5. Routes task to the activated agent

### Best For:

- Large pools of specialized agents
- Memory-efficient (agents inactive until needed)
- Agent lifecycle management

## 2. Dynamic Agent Discovery Supervisor

**File**: `examples/dynamic_supervisor/working_dynamic_agent_discovery_supervisor.py`

### Key Features:

- **Dynamic Agent Creation**: Creates new agents at runtime
- **Agent Specifications**: List of agent specs that can be instantiated
- **Discovery Modes**: Different ways to discover agents (component, RAG, MCP, hybrid)
- **AgentCapability**: Rich metadata including specialties and tools

### State Structure:

```python
class DynamicAgentDiscoveryState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    agents: Dict[str, Any]  # Active agent instances
    agent_capabilities: Dict[str, AgentCapability]  # Agent capability registry
    discovered_agents: Set[str]  # Names of discovered agents
    available_agent_specs: List[Dict[str, Any]]  # Specs for agents that can be created
    current_agent: str
    agent_task: str
    agent_response: str
    discovery_attempts: int
```

### How it Works:

1. Starts with agent specifications (templates)
2. When a task requires a new capability, discovers/creates appropriate agent
3. Uses `discover_and_add_agents()` to instantiate from specs
4. Maintains discovered_agents set to track what's been created
5. Can discover agents through multiple modes

### Best For:

- Dynamic environments where agent needs aren't known upfront
- Creating specialized agents on-demand
- Integration with external agent discovery systems

## 3. Static Supervisor with Tool Sync

**File**: `examples/dynamic_supervisor/working_sync_supervisor.py`

### Key Features:

- **Automatic Tool Sync**: `sync_tools_with_agents()` creates handoff tools
- **AgentEntry**: Serializes agents with pickle for storage
- **Dynamic Handoff Tools**: Creates tools for each registered agent
- **Static Agent Set**: Agents are pre-defined, not discovered

### State Structure:

```python
class SupervisorState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    registered_agents: Dict[str, AgentEntry]  # All registered agents
    next_agent: str
    agent_task: str
    agent_response: str
```

### How it Works:

1. Agents are registered upfront with `register_agent()`
2. `sync_tools_with_agents()` creates handoff tools for each agent
3. Supervisor gets these tools automatically
4. When supervisor uses a handoff tool, routes to that agent
5. AgentEntry handles serialization/deserialization

### Best For:

- Fixed set of known agents
- Simple handoff patterns
- When you want supervisor to have explicit tools for each agent

## Key Differences

| Feature          | Registry-Based                   | Discovery-Based               | Tool Sync                     |
| ---------------- | -------------------------------- | ----------------------------- | ----------------------------- |
| Agent Storage    | AgentInfo with metadata          | Direct instances              | Pickled AgentEntry            |
| Agent Creation   | Pre-created, activated on demand | Created from specs at runtime | Pre-created and registered    |
| Discovery        | Capability search in registry    | Multiple discovery modes      | No discovery, all pre-defined |
| Tools            | No automatic tools               | Agent-specific tools          | Auto-generated handoff tools  |
| State Complexity | Medium (registry + active)       | High (specs + capabilities)   | Low (just registered agents)  |
| Memory Usage     | Low (inactive agents)            | Medium (creates as needed)    | High (all agents in memory)   |
| Best Use Case    | Large agent pools                | Unknown agent needs           | Simple fixed workflows        |

## Common Patterns

All three implementations:

1. Use `SimpleAgentV3` and `ReactAgent` as base agent types
2. Implement a supervisor reasoning node that routes tasks
3. Use LangGraph StateGraph for workflow
4. Have similar routing logic (check task, find agent, route)
5. Return results through state updates

## Which to Use?

- **Registry-Based**: When you have many agents but only need a few active at once
- **Discovery-Based**: When you need to create new agent types dynamically
- **Tool Sync**: When you have a fixed set of agents and want simple tool-based routing
