# Supervisor Comparison: Dynamic Capabilities

## Overview

Haive now has three types of dynamic supervisors, each with different capabilities:

1. **DynamicActivationSupervisor** - Component discovery and activation
2. **Dynamic Agent Tools (via dynamic_agent_tools.py)** - Agent management
3. **DynamicToolDiscoverySupervisor** - Tool discovery and distribution

## Feature Comparison

| Feature               | DynamicActivationSupervisor      | Dynamic Agent Tools  | DynamicToolDiscoverySupervisor |
| --------------------- | -------------------------------- | -------------------- | ------------------------------ |
| **Primary Focus**     | Component activation             | Agent management     | Tool discovery                 |
| **Discovery Type**    | Components (agents, tools, etc.) | N/A (manages agents) | Tools specifically             |
| **Discovery Sources** | ComponentDiscoveryAgent          | N/A                  | RAG, ComponentDiscovery, MCP   |
| **Dynamic Addition**  | Components to registry           | Agents to supervisor | Tools to agents                |
| **State Schema**      | DynamicActivationState           | SupervisorState      | SupervisorState                |
| **MetaStateSchema**   | Yes (wraps components)           | No                   | No (but could be added)        |
| **Factory Methods**   | Yes                              | No (uses tools)      | Yes                            |
| **Tool Distribution** | No                               | No                   | Yes (to agents)                |

## Use Cases

### DynamicActivationSupervisor

```python
# Use when you need to discover and activate various components
supervisor = DynamicActivationSupervisor.create_with_discovery(
    name="component_supervisor",
    document_path="@haive-tools",
    engine=AugLLMConfig()
)

# Discovers and activates components based on task needs
result = await supervisor.arun("Process CSV and create visualization")
```

### Dynamic Agent Tools (Supervisor with Tools)

```python
# Use when you need to dynamically manage agents at runtime
tools = create_agent_management_tools(supervisor)

# Add/remove agents via tool calls
await add_agent_tool.arun(
    agent_descriptor=AgentDescriptor(
        name="new_agent",
        agent_type="ReactAgent",
        capability_description="Handles specific tasks"
    )
)
```

### DynamicToolDiscoverySupervisor

```python
# Use when you need to discover and distribute tools to agents
supervisor = DynamicToolDiscoverySupervisor.create_with_discovery(
    name="tool_supervisor",
    agents={"worker": ReactAgent(...)},
    engine=AugLLMConfig(),
    discovery_mode=ToolDiscoveryMode.HYBRID,
    rag_documents_path="/path/to/tool/docs"
)

# Discovers tools and provides them to appropriate agents
result = await supervisor.arun("Calculate statistics and create report")
```

## Key Differences

### 1. Discovery Scope

- **DynamicActivationSupervisor**: Discovers any type of component (agents, tools, workflows)
- **DynamicToolDiscoverySupervisor**: Focused specifically on tool discovery

### 2. Discovery Methods

- **DynamicActivationSupervisor**: Uses ComponentDiscoveryAgent with documentation
- **DynamicToolDiscoverySupervisor**: Multiple sources (RAG, ComponentDiscovery, MCP)

### 3. Integration Approach

- **DynamicActivationSupervisor**: Wraps components in MetaStateSchema for tracking
- **Dynamic Agent Tools**: Provides tools that modify supervisor's agent registry
- **DynamicToolDiscoverySupervisor**: Registers tools and distributes to agents

### 4. State Management

- **DynamicActivationSupervisor**: Custom DynamicActivationState with registry
- **DynamicToolDiscoverySupervisor**: Standard SupervisorState with tool registry

## When to Use Each

### Use DynamicActivationSupervisor when:

- You need to discover and activate various types of components
- You want MetaStateSchema tracking for all components
- You have documentation-based component discovery needs
- You need capability gap detection and filling

### Use Dynamic Agent Tools when:

- You need to add/remove agents at runtime
- You want tool-based agent management
- You're building adaptive multi-agent systems
- You need fine-grained control over agent lifecycle

### Use DynamicToolDiscoverySupervisor when:

- You need to discover tools from multiple sources
- You want to distribute tools to specific agents
- You have RAG-based tool documentation
- You need MCP framework integration
- You want tool-aware routing decisions

## Example: Combining Approaches

You can combine these approaches for maximum flexibility:

```python
# Create a supervisor with dynamic tool discovery
tool_supervisor = DynamicToolDiscoverySupervisor.create_with_discovery(
    name="main_supervisor",
    agents=initial_agents,
    engine=config,
    discovery_mode=ToolDiscoveryMode.HYBRID
)

# Add agent management tools
agent_tools = create_agent_management_tools(tool_supervisor)
# Now supervisor can both discover tools AND manage agents dynamically

# The supervisor can:
# 1. Discover new tools from documentation/RAG/MCP
# 2. Add/remove agents as needed
# 3. Distribute tools to appropriate agents
# 4. Make routing decisions based on tool availability
```

## Implementation Notes

### DynamicActivationSupervisor

- Uses graph-based workflow with conditional routing
- Implements capability analysis and gap detection
- Maintains component registry with activation tracking
- Provides activation statistics

### DynamicToolDiscoverySupervisor

- Extends BaseSupervisor with tool discovery
- Implements multiple discovery strategies
- Maintains tool registry separate from agent registry
- Provides tool distribution to agents

### Integration Patterns

Both supervisors follow similar patterns:

1. Factory methods for complex initialization
2. Private attributes for internal state
3. Model validators for setup
4. No `__init__` overrides (Pydantic best practice)

## Future Enhancements

### Potential Convergence

Consider creating a unified supervisor that combines:

- Component discovery (from DynamicActivationSupervisor)
- Tool discovery (from DynamicToolDiscoverySupervisor)
- Agent management (from dynamic_agent_tools)
- MetaStateSchema tracking for all entities

### Shared Infrastructure

- Unified discovery interface
- Common registry patterns
- Shared routing logic
- Consistent state management
