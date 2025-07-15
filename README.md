# Haive Agents - Multi-Agent Architecture Library

## Overview

Haive Agents provides comprehensive multi-agent orchestration capabilities with dynamic supervisor patterns, reactive reasoning agents, and sophisticated coordination mechanisms. The library has been recently reorganized for better maintainability and developer experience.

## 🎯 Core Implementations

### 1. Dynamic Supervisor Agent

**Location**: `/src/haive/agents/dynamic_supervisor/`

Runtime agent management with tool-based execution:

- **Dynamic agent management** - Add/remove agents at runtime
- **Tool-based execution** - Agents execute through tools
- **ReAct integration** - Inherits reasoning capabilities
- **State management** - Maintains agent registry and execution state

```python
from haive.agents.dynamic_supervisor import create_dynamic_supervisor

# Create supervisor
supervisor = create_dynamic_supervisor(name="task_router")

# Add agents
state = supervisor.create_initial_state()
state.add_agent("math", math_agent, "Mathematics expert")
state.add_agent("search", search_agent, "Web search specialist")

# Route tasks
result = await supervisor.arun("Calculate 15 * 23", state=state)
```

### 2. React Agent

**Location**: `/src/haive/agents/react/`

ReAct (Reasoning and Acting) pattern with looping behavior:

- **Reasoning loop** - Continuous reasoning and acting cycle
- **Tool integration** - Seamless tool usage within the loop
- **State management** - Maintains conversation state
- **SimpleAgent extension** - Inherits base functionality

```python
from haive.agents.react import ReactAgent
from haive.core.engine.aug_llm import AugLLMConfig

agent = ReactAgent(
    name="reasoning_agent",
    engine=AugLLMConfig(
        model="gpt-4",
        tools=[calculator_tool],
        system_message="Think step by step."
    )
)

result = await agent.arun("What is 15 * 23 + 7?")
```

### 3. Supervisor Package

**Location**: `/src/haive/agents/supervisor/`

Alternative supervisor implementations:

- **Basic SupervisorAgent** - Traditional supervisor pattern
- **Integrated supervisor** - Multi-agent coordination
- **Registry utilities** - Agent registry management
- **Routing logic** - Task routing and agent selection

## 🗂️ Package Organization

### Source Code Structure

```
src/haive/agents/
├── dynamic_supervisor/     # Main supervisor implementation
├── supervisor/             # Alternative supervisor patterns
├── react/                  # ReAct agent implementation
├── simple/                 # Base SimpleAgent
├── multi/                  # Multi-agent coordination
├── rag/                    # RAG agent implementations
└── ...                     # Other agent types
```

### Testing Structure

```
tests/
├── supervisor/
│   ├── components/         # Component-specific tests
│   ├── experiments/        # Experimental pattern tests
│   └── integration/        # Integration tests
├── react/                  # React agent tests
├── test_dynamic_supervisor/# Dynamic supervisor tests
└── ...
```

### Examples Structure

```
examples/
├── supervisor/
│   ├── basic/              # Basic usage examples
│   ├── advanced/           # Advanced patterns
│   └── patterns/           # Architecture patterns
├── react/                  # React agent examples
└── ...
```

### Documentation Structure

```
docs/
├── supervisor/
│   ├── README.md           # Main supervisor documentation
│   ├── patterns/           # Pattern documentation
│   └── archive/            # Archived implementations
└── ...
```

## 🚀 Quick Start

### Installation

```bash
pip install haive-agents
```

### Basic Multi-Agent Setup

```python
import asyncio
from haive.agents.dynamic_supervisor import create_dynamic_supervisor
from haive.agents.simple import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig

async def main():
    # Create specialized agents
    math_agent = SimpleAgent(
        name="math_agent",
        engine=AugLLMConfig(tools=[calculator_tool])
    )

    search_agent = SimpleAgent(
        name="search_agent",
        engine=AugLLMConfig(tools=[search_tool])
    )

    # Create supervisor
    supervisor = create_dynamic_supervisor(name="coordinator")

    # Add agents
    state = supervisor.create_initial_state()
    state.add_agent("math", math_agent, "Mathematics expert")
    state.add_agent("search", search_agent, "Web search specialist")

    # Route complex task
    result = await supervisor.arun(
        "Find the population of Tokyo and calculate the population density",
        state=state
    )

    print(result)

asyncio.run(main())
```

### Advanced Agent Activation

```python
from haive.agents.dynamic_supervisor import DynamicSupervisorAgent

# Create supervisor with capability-based activation
supervisor = DynamicSupervisorAgent(
    name="adaptive_supervisor",
    engine=supervisor_engine,
    enable_agent_builder=True
)

# Start with minimal agents
state = supervisor.create_initial_state()
state.add_agent("general", general_agent, "General assistant")

# Add specialized agents dynamically based on need
async def handle_request(request):
    # Analyze request capabilities
    if "calculation" in request.lower():
        state.add_agent("math", math_agent, "Mathematics expert")

    if "research" in request.lower():
        state.add_agent("search", search_agent, "Research specialist")

    return await supervisor.arun(request, state=state)
```

## 🏗️ Architecture Patterns

### 1. Tool-Based Agent Execution

```python
@tool
def handoff_to_math_agent(task: str) -> str:
    """Transfer task to math agent."""
    result = await math_agent.arun(task)
    return f"Math result: {result}"
```

### 2. Agent Execution Node Pattern

```python
# Supervisor decides routing
state.agent_route = "math_agent"

# Agent execution node runs selected agent
async def agent_execution_node(state):
    agent = registry.get_active_agent(state.agent_route)
    return await agent.arun(state.current_task)
```

### 3. Dynamic Tool Generation

```python
def generate_handoff_tools(agents):
    tools = []
    for name, agent in agents.items():
        tool = create_handoff_tool(name, agent)
        tools.append(tool)
    return tools
```

## 🧪 Testing Philosophy

### No-Mocks Testing

All tests use real components:

- **Real LLM integrations** - Actual API calls
- **Real agent implementations** - Full agent stack
- **Real state management** - Actual persistence
- **Real tool execution** - Complete workflow

### Test Categories

```bash
# Run all tests
poetry run pytest tests/ -v

# Run specific categories
poetry run pytest tests/supervisor/ -v          # Supervisor tests
poetry run pytest tests/react/ -v              # React agent tests
poetry run pytest tests/supervisor/components/ -v  # Component tests
poetry run pytest tests/supervisor/experiments/ -v # Experimental tests
```

## 📚 Examples and Patterns

### Basic Examples

- **[Basic Supervisor](examples/supervisor/basic/basic_supervisor_example.py)** - Simple multi-agent coordination
- **[React Agent](examples/react/)** - ReAct pattern usage

### Advanced Examples

- **[Dynamic Activation](examples/supervisor/advanced/dynamic_activation_example.py)** - Capability-based agent activation
- **[Multi-Step Workflows](examples/supervisor/advanced/)** - Complex task coordination

### Pattern Examples

- **[Agent Execution Node](examples/supervisor/patterns/agent_execution_node_pattern.py)** - Clean execution pattern
- **[Dynamic Tool Generation](examples/supervisor/patterns/dynamic_tool_generation_pattern.py)** - Tool creation patterns
- **[State Synchronized Tools](examples/supervisor/patterns/state_synchronized_tools_pattern.py)** - State-tool coordination

## 🔧 Development

### Running Examples

```bash
# Basic supervisor example
poetry run python examples/supervisor/basic/basic_supervisor_example.py

# Advanced patterns
poetry run python examples/supervisor/advanced/dynamic_activation_example.py

# Pattern demonstrations
poetry run python examples/supervisor/patterns/agent_execution_node_pattern.py
```

### Development Setup

```bash
# Install dependencies
poetry install

# Run tests
poetry run pytest tests/ -v

# Run specific test suite
poetry run pytest tests/supervisor/ -v
```

## 📖 Documentation

### Core Documentation

- **[Supervisor Documentation](docs/supervisor/README.md)** - Complete supervisor guide
- **[React Agent Documentation](src/haive/agents/react/README.md)** - ReAct pattern guide
- **[Dynamic Supervisor Documentation](src/haive/agents/dynamic_supervisor/README.md)** - Dynamic supervisor details

### Testing Documentation

- **[Test Guide](tests/supervisor/README.md)** - Testing approach and guidelines
- **[No-Mocks Philosophy](docs/supervisor/TEST_GUIDE.md)** - Testing philosophy

### Pattern Documentation

- **[Architecture Patterns](docs/supervisor/patterns/)** - Detailed pattern explanations
- **[Implementation Guide](docs/supervisor/IMPLEMENTATION_PLAN.md)** - Implementation strategy

## 🎯 Common Use Cases

### 1. Task Routing

Route different types of tasks to specialized agents:

```python
# Question answering → General agent
# Calculations → Math agent
# Research → Search agent
# Code generation → Code agent
```

### 2. Multi-Step Workflows

Coordinate complex processes:

```python
# Research → Analysis → Presentation
# Data Collection → Processing → Reporting
# Problem Analysis → Solution Design → Implementation
```

### 3. Resource Management

Optimize resource usage:

```python
# Dynamic activation - Activate agents on demand
# Load balancing - Distribute work across agents
# Cost optimization - Use appropriate models
```

### 4. Error Recovery

Handle failures gracefully:

```python
# Fallback agents - Backup for critical functions
# Retry logic - Automatic retry for failures
# Graceful degradation - Reduced functionality
```

## 🛠️ Best Practices

### 1. Agent Design

- **Specialized agents** for specific tasks
- **Clear descriptions** for routing decisions
- **Robust error handling** in implementations
- **Appropriate tool selection**

### 2. Supervisor Configuration

- **Clear system messages** for routing logic
- **Appropriate model selection** for complexity
- **Proper state management** for multi-turn interactions
- **Resource optimization** for cost efficiency

### 3. State Management

- **Minimal state** for performance
- **Clear state transitions** for debugging
- **Proper state persistence** for long conversations
- **State validation** for correctness

### 4. Error Handling

- **Graceful degradation** when agents fail
- **Retry logic** for transient failures
- **Fallback agents** for critical functions
- **Comprehensive logging** for debugging

## 🔄 Recent Reorganization

The package has been recently reorganized for better maintainability:

### What Was Moved

- **64 test files** moved from source to proper test directories
- **8 valuable examples** extracted from experimental code
- **7 documentation files** organized in docs directory
- **Debug and experimental files** properly archived

### Benefits

- **Clean source code** - No test files in source directories
- **Organized tests** - Tests categorized by purpose
- **Preserved patterns** - Valuable patterns saved as examples
- **Centralized documentation** - All docs in logical locations

### Migration Guide

See **[Reorganization Summary](docs/supervisor/REORGANIZATION_SUMMARY.md)** for complete details.

## 🤝 Contributing

### Adding New Patterns

1. Study existing patterns in `/patterns/` directory
2. Follow established architecture principles
3. Implement comprehensive tests
4. Document the pattern thoroughly
5. Provide usage examples

### Development Guidelines

1. **Use real components** in tests (no mocks)
2. **Follow existing patterns** and conventions
3. **Include comprehensive documentation**
4. **Test thoroughly** before submission
5. **Update cross-references** as needed

## 📈 Roadmap

### Planned Improvements

1. **Enhanced routing** - More sophisticated agent selection
2. **Performance optimization** - Faster state management
3. **Extended patterns** - New architectural patterns
4. **Better monitoring** - Enhanced observability
5. **Improved error handling** - More robust error recovery

### Future Patterns

1. **Hierarchical supervisors** - Multi-level coordination
2. **Federated agents** - Distributed agent management
3. **Adaptive routing** - Learning-based agent selection
4. **Resource-aware scheduling** - Optimize resource usage
5. **Stream processing** - Real-time agent coordination

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Related Projects

- **[Haive Core](../haive-core/)** - Core framework components
- **[Haive Tools](../haive-tools/)** - Tool implementations
- **[Haive Games](../haive-games/)** - Game-playing agents
- **[Haive MCP](../haive-mcp/)** - MCP integration

For questions, issues, or contributions, please refer to the main project repository or create an issue.
