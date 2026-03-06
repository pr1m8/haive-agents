# Multi-Agent Experiments

**Created**: 2025-01-15  
**Purpose**: Explore and refine multi-agent list/sequence patterns

## 🎯 Core Concept

Multi-agent systems should feel like working with a Python list of agents, with natural operations like append, insert, remove, and iteration. The key insight is that **composition and orchestration** matter more than complex state merging or tool management.

## 📊 Key Principles

1. **List-like Interface**: Multi-agent extends `Sequence[Agent]`
2. **Simple State Flow**: Message passing, not complex merging
3. **Tools Stay Local**: Each agent manages its own tools in state/engine
4. **Conditional Routing**: Use BaseGraph's `add_conditional_edges`
5. **Dynamic Recompilation**: Support runtime modifications

## 🧪 Experiments

### 1. Basic List Multi-Agent (`list_multi_agent.py`)

- Pure list interface implementation
- Sequential execution by default
- Simple message passing approach

### 2. Proper Infrastructure Usage (`proper_list_multi_agent.py`) ⭐ **RECOMMENDED**

- Uses `MultiAgentState` for proper state management
- Uses `AgentNodeV3` for agent execution with state projection
- Uses `MetaStateSchema` for single agent embedding
- Proper engine syncing and recompilation tracking
- **This is the correct way to build multi-agent systems**

### 3. Routing Patterns (`routing_patterns.py`)

- Conditional routing with `add_conditional_edges`
- Multi-branch decisions
- Dynamic route modification
- Early exit conditions

### 4. Test Suite (`test_proper_usage.py`)

- Comprehensive tests showing proper usage patterns
- Demonstrates MultiAgentState, MetaStateSchema, AgentNodeV3
- Tool integration examples
- Recompilation tracking tests

## 📝 Design Decisions

### Why Not Complex Tool Management?

Tools are already part of each agent's configuration:

- Agents have `engine.tools`
- Agents have `get_all_tools()` method
- Tools can be in agent state schema
- No need for complex sharing/mapping at multi-agent level

### State Flow Philosophy

Instead of merging schemas:

```python
# Simple message passing
def build_graph(self):
    for i, agent in enumerate(self.agents):
        graph.add_node(f"agent_{i}",
            lambda state: agent.invoke({"messages": state["messages"]})
        )
```

### Recompilation Strategy

When agents are added/removed:

1. Mark for recompile
2. Rebuild graph if auto_recompile=True
3. Track modifications for debugging

## 🚀 Next Steps

1. Implement basic `ListMultiAgent` with clean interface
2. Test conditional routing patterns
3. Experiment with state isolation vs sharing
4. Build real-world examples (research pipeline, QA system)
5. Performance testing with many agents

## 📄 File Structure

```
experiments/
├── README.md                    # This file
├── list_multi_agent.py         # Core list-based implementation
├── routing_patterns.py         # Conditional routing experiments
├── execution_modes.py          # Different execution strategies
├── state_patterns.py           # State management approaches
├── builder_api.py              # Fluent builder interfaces
└── test_experiments.py         # Test cases for all experiments
```

## 💡 Key Insights

1. **Use the existing infrastructure**: MultiAgentState and AgentNodeV3 are there for a reason
2. **State hierarchy matters**: Don't flatten schemas, use proper projection
3. **Tools are local**: Each agent manages its own tools in engine/state
4. **Recompilation is built-in**: MultiAgentState has recompilation tracking
5. **List interface is intuitive**: Natural Python patterns work well

## 🎯 Major Realizations

### We Were Over-engineering Tool Management

- Tools are already in each agent's `engine.tools`
- Agents have `get_all_tools()` method
- No need for complex sharing/mapping at multi-agent level
- Tools are part of agent configuration, not multi-agent orchestration

### The Infrastructure is Already There

- **MultiAgentState**: Proper agent container with isolation
- **AgentNodeV3**: Proper agent execution with state projection
- **MetaStateSchema**: Single agent embedding pattern
- **create_agent_node_v3**: Factory for creating agent nodes

### State Management is Hierarchical

- Each agent has isolated state in `agent_states`
- Shared fields like `messages` are managed at container level
- No schema flattening - agents maintain their own schemas
- Engine syncing happens automatically

### Recompilation is Built-in

- MultiAgentState tracks agents needing recompilation
- RecompileMixin provides standardized recompilation patterns
- Graph rebuilding happens when agents are added/removed
- No need to reinvent recompilation tracking

---

**Note**: These experiments helped us understand the proper patterns. The `proper_list_multi_agent.py` implementation should be the foundation for the real multi-agent system.
