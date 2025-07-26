# MultiAgent - Haive Framework

**Multi-agent orchestration and coordination for complex AI workflows**

## 🎯 Quick Start - Which Version to Use?

### ✅ **Default (Recommended)**: MultiAgent (Clean Implementation)

```python
from haive.agents.multi import MultiAgent  # Gets clean, unified implementation
from haive.agents.simple import SimpleAgent
from haive.agents.react import ReactAgent
from haive.core.engine.aug_llm import AugLLMConfig

# Create individual agents
researcher = ReactAgent(
    name="researcher",
    engine=AugLLMConfig(temperature=0.3),
    tools=[web_search, calculator]
)

writer = SimpleAgent(
    name="writer",
    engine=AugLLMConfig(temperature=0.7)
)

editor = SimpleAgent(
    name="editor",
    engine=AugLLMConfig(temperature=0.2)
)

# Natural multi-agent syntax
workflow = MultiAgent([researcher, writer, editor])

# Execute sequential workflow
result = await workflow.arun("Research and write about AI trends")
print(result)
```

### 🚀 **Enhanced (Newer)**: EnhancedMultiAgentV4

```python
from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.simple import SimpleAgent
from haive.agents.react import ReactAgent
from haive.core.engine.aug_llm import AugLLMConfig

# Create enhanced multi-agent with advanced features
workflow = EnhancedMultiAgentV4(
    name="analysis_pipeline",
    agents=[analyzer, processor, formatter],
    execution_mode="sequential",  # sequential, parallel, conditional, manual
    build_mode="auto"  # auto, manual, lazy
)

# Add conditional routing
def check_complexity(state):
    return state.get("complexity_score", 0) > 0.7

workflow.add_conditional_edge(
    from_agent="analyzer",
    condition=check_complexity,
    true_agent="complex_processor",
    false_agent="simple_processor"
)

# Execute with advanced orchestration
result = await workflow.arun({"messages": [{"role": "user", "content": "Analyze complex data"}]})
```

## 📋 Version Comparison

| Feature                 | MultiAgent<br/>(Default Clean)              | EnhancedMultiAgentV4<br/>(Advanced)                                           |
| ----------------------- | ------------------------------------------- | ----------------------------------------------------------------------------- |
| **Import**              | `from haive.agents.multi import MultiAgent` | `from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4` |
| **Base Class**          | Enhanced Agent ✅                           | Enhanced Agent ✅                                                             |
| **Syntax**              | `MultiAgent([agent1, agent2])`              | `EnhancedMultiAgentV4(agents=[...])`                                          |
| **Execution Modes**     | ✅ **Auto-detected**                        | ✅ **Explicit modes**                                                         |
| **Conditional Routing** | ✅ Smart routing                            | ✅ **Rich conditional edges**                                                 |
| **Dynamic Agents**      | ✅ Basic                                    | ✅ **Hot addition with recompilation**                                        |
| **State Management**    | ✅ Unified                                  | ✅ **MultiAgentState with projections**                                       |
| **Build Modes**         | ✅ Auto                                     | ✅ **Auto/Manual/Lazy**                                                       |
| **Graph Control**       | ✅ Simplified                               | ✅ **Full manual control**                                                    |
| **Status**              | **Current Default**                         | **Advanced Features**                                                         |

Advanced multi-agent orchestration system for the Haive framework with enhanced base agent pattern support.

## Overview

MultiAgent provides intuitive multi-agent coordination in Haive. **Default import gets you clean implementation, V4 available for advanced features.**

Both versions leverage the enhanced base agent pattern for seamless integration with the Haive ecosystem.

## 🔧 Installation & Setup

```bash
# Install Haive framework
poetry install

# MultiAgent is included in haive-agents package
from haive.agents.multi import MultiAgent, EnhancedMultiAgentV4
```

## 🎯 Use Cases

### MultiAgent (Default Clean) - For Most Users

- **Sequential workflows**: Research → Analysis → Writing pipelines
- **Simple coordination**: Basic agent orchestration
- **Auto-detection**: Smart routing based on agent types
- **Production ready**: Stable, tested patterns

### EnhancedMultiAgentV4 (Advanced) - For Complex Workflows

- **Complex orchestration**: Conditional routing, parallel execution
- **Dynamic workflows**: Runtime agent addition and modification
- **Advanced state management**: Multi-agent state projections
- **Research & experimentation**: Latest coordination patterns

## Key Features

### Both Versions Include:

- **Enhanced Base Agent Pattern**: Properly extends `Agent` class and implements `build_graph()`
- **Multiple Execution Modes**: Sequential, parallel, conditional orchestration
- **State Management**: Type-safe state handling across agents
- **Dynamic Graph Building**: Automatic graph compilation

### V4 Advanced Features:

- **AgentNodeV3 Integration**: Advanced state projection for clean agent isolation
- **Rich Conditional Routing**: Complex edge conditions via BaseGraph2
- **Hot Agent Addition**: Add agents dynamically with automatic recompilation
- **Manual Graph Control**: Full control over execution flow

## Quick Start

### Basic Sequential Workflow

```python
from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.simple import SimpleAgent
from haive.agents.react import ReactAgent
from haive.core.engine.aug_llm import AugLLMConfig

# Create individual agents
analyzer = ReactAgent(
    name="analyzer",
    engine=AugLLMConfig(),
    tools=[calculator_tool, search_tool]
)

processor = SimpleAgent(
    name="processor",
    engine=AugLLMConfig()
)

formatter = SimpleAgent(
    name="formatter",
    engine=AugLLMConfig()
)

# Create multi-agent workflow
workflow = EnhancedMultiAgentV4(
    name="analysis_pipeline",
    agents=[analyzer, processor, formatter],
    execution_mode="sequential"
)

# Execute workflow
result = await workflow.arun({
    "messages": [{"role": "user", "content": "Analyze market trends"}]
})
```

### Conditional Routing

```python
# Create agents for different complexity levels
simple_processor = SimpleAgent(name="simple", engine=config)
complex_processor = ReactAgent(name="complex", engine=config, tools=[...])
classifier = SimpleAgent(name="classifier", engine=config)

# Create workflow with conditional execution
workflow = EnhancedMultiAgentV4(
    name="adaptive_processor",
    agents=[classifier, simple_processor, complex_processor],
    execution_mode="conditional"
)

# Add conditional routing
def check_complexity(state):
    return state.get("complexity_score", 0) > 0.7

workflow.add_conditional_edge(
    from_agent="classifier",
    condition=check_complexity,
    true_agent="complex",
    false_agent="simple"
)
```

### Manual Graph Building

```python
# Create workflow with manual build mode
workflow = EnhancedMultiAgentV4(
    name="custom_flow",
    agents=[agent1, agent2, agent3],
    execution_mode="manual",
    build_mode="manual"
)

# Build custom execution flow
workflow.add_edge("agent1", "agent2")
workflow.add_edge("agent1", "agent3")  # Parallel branch
workflow.add_edge("agent2", END)
workflow.add_edge("agent3", END)

# Build the graph
workflow.build()
```

## Execution Modes

### Sequential

Agents execute one after another in the order they were added.

```python
workflow = EnhancedMultiAgentV4(
    agents=[step1, step2, step3],
    execution_mode="sequential"
)
# Execution: step1 → step2 → step3
```

### Parallel

All agents execute simultaneously.

```python
workflow = EnhancedMultiAgentV4(
    agents=[analyzer1, analyzer2, analyzer3],
    execution_mode="parallel"
)
# Execution: analyzer1, analyzer2, analyzer3 (all at once)
```

### Conditional

Agents execute based on routing logic.

```python
workflow = EnhancedMultiAgentV4(
    agents=[router, option_a, option_b],
    execution_mode="conditional"
)
workflow.add_conditional_edge("router", condition_fn, "option_a", "option_b")
```

### Manual

You have full control over the graph structure.

```python
workflow = EnhancedMultiAgentV4(
    agents=[...],
    execution_mode="manual"
)
# Add edges manually to create any graph structure
```

## Build Modes

- **auto**: Graph builds immediately on initialization (default)
- **manual**: Must call `build()` explicitly
- **lazy**: Graph builds on first execution

## Advanced Features

### Multi-Way Conditional Routing

```python
def route_by_category(state):
    category = state.get("category", "other")
    return category  # Returns: "sales", "support", "technical", etc.

workflow.add_multi_conditional_edge(
    from_agent="classifier",
    condition=route_by_category,
    routes={
        "sales": "sales_agent",
        "support": "support_agent",
        "technical": "tech_agent"
    },
    default="general_agent"
)
```

### Dynamic Agent Addition

```python
# Start with basic workflow
workflow = EnhancedMultiAgentV4(
    agents=[agent1, agent2],
    build_mode="auto"  # Automatic recompilation
)

# Add new agent dynamically
validator = SimpleAgent(name="validator")
workflow.add_agent(validator)  # Graph automatically rebuilds

# Add edge to include new agent
workflow.add_edge("agent2", "validator")
```

### State Management

EnhancedMultiAgentV4 uses `MultiAgentState` by default, which provides:

- **Agent Isolation**: Each agent gets its own state namespace
- **Shared State**: Common fields like `messages` are accessible to all
- **Type Safety**: State projections maintain type information
- **Direct Updates**: Structured output agents can update specific fields

## API Reference

### Constructor Parameters

- `name` (str): Workflow identifier
- `agents` (List[Agent]): List of agents to coordinate
- `execution_mode` (Literal["sequential", "parallel", "conditional", "manual"]): How agents connect
- `build_mode` (Literal["auto", "manual", "lazy"]): When to build the graph
- `entry_point` (Optional[str]): Starting agent name (defaults to first)
- `state_schema` (type): State schema class (defaults to MultiAgentState)

### Key Methods

- `build()`: Manually build the graph (for manual/lazy modes)
- `add_edge(from_agent, to_agent)`: Add direct connection
- `add_conditional_edge(from_agent, condition, true_agent, false_agent)`: Add conditional routing
- `add_multi_conditional_edge(from_agent, condition, routes, default)`: Add multi-way routing
- `add_agent(agent)`: Dynamically add an agent
- `get_agent(name)`: Retrieve agent by name
- `get_agent_names()`: List all agent names
- `display_info()`: Print workflow configuration

## Best Practices

1. **Use Descriptive Names**: Give agents clear, descriptive names for easier debugging
2. **Start Simple**: Begin with sequential mode and add complexity as needed
3. **Test Incrementally**: Test each agent individually before combining
4. **Handle Errors**: Implement error handling in condition functions
5. **Monitor State**: Use logging to track state changes between agents

## Examples

See the `examples/` directory for complete working examples:

- `multi_agent_v4_react_to_simple.py` - ReactAgent → SimpleAgent sequential pattern with structured output
- `multi_agent_v4_parallel_dynamic.py` - Parallel execution and dynamic agent addition patterns
- `enhanced_multi_agent_v4_example.py` - Basic usage patterns
- `conditional_routing_example.py` - Advanced routing scenarios
- `dynamic_agents_example.py` - Runtime agent management

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are installed with `poetry install`
2. **Circular Dependencies**: Check agent output/input schema compatibility
3. **State Conflicts**: Verify agents aren't overwriting shared state unexpectedly
4. **Build Failures**: Check agent names are unique and valid

### Debug Mode

Enable debug logging to see detailed execution flow:

```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Or use agent debug mode
result = await workflow.arun(input_data, debug=True)
```

## Contributing

Contributions are welcome! Please ensure:

1. All tests pass: `poetry run pytest`
2. Code follows style guide: `poetry run ruff check`
3. Documentation is updated
4. Examples demonstrate new features

## License

MIT License - see LICENSE file for details.
