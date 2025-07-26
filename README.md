# Haive Agents - Complete Agent Framework

## 🎯 Quick Start Guide

### Which Agent Should I Use?

| Agent Type      | Default Version | Latest Version          | When to Use                         |
| --------------- | --------------- | ----------------------- | ----------------------------------- |
| **SimpleAgent** | `SimpleAgent`   | `SimpleAgentV3`         | Basic LLM interactions with prompts |
| **ReactAgent**  | `ReactAgent`    | `ReactAgent` (no V2/V3) | Tool use and reasoning loops        |
| **MultiAgent**  | `MultiAgent`    | `EnhancedMultiAgentV4`  | Coordinating multiple agents        |

### Import Examples

```python
# Default versions (stable, widely used)
from haive.agents.simple import SimpleAgent
from haive.agents.react import ReactAgent
from haive.agents.multi import MultiAgent

# Latest versions (enhanced features)
from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
```

## 📚 Agent Types Overview

### SimpleAgent Family

- **Purpose**: Basic LLM-powered agents with prompt templates
- **Key Features**: Prompt engineering, structured output, state management
- **[Detailed Documentation →](src/haive/agents/simple/README.md)**

### ReactAgent

- **Purpose**: Reasoning and tool-using agents
- **Key Features**: ReAct loop, tool integration, multi-step reasoning
- **[Detailed Documentation →](src/haive/agents/react/README.md)**

### MultiAgent Family

- **Purpose**: Orchestrating multiple agents in workflows
- **Key Features**: Sequential/parallel execution, state sharing, complex workflows
- **[Detailed Documentation →](src/haive/agents/multi/README.md)**

## 🚀 Quick Examples

### Basic LLM Agent

```python
from haive.agents.simple import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig

# Create a basic agent
agent = SimpleAgent(
    name="assistant",
    engine=AugLLMConfig(temperature=0.7)
)

# Use it
response = agent.run("Explain quantum computing")
```

### Agent with Tools

```python
from haive.agents.react import ReactAgent
from langchain_core.tools import tool

@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    return str(eval(expression))

# Create agent with tools
agent = ReactAgent(
    name="math_assistant",
    engine=AugLLMConfig(),
    tools=[calculator]
)

# Use it
response = agent.run("What is 25 * 37?")
```

### Multi-Agent Workflow

```python
from haive.agents.multi import MultiAgent
from haive.agents.simple import SimpleAgent

# Create specialized agents
researcher = SimpleAgent(name="researcher")
writer = SimpleAgent(name="writer")

# Coordinate them
team = MultiAgent(
    name="content_team",
    agents={"research": researcher, "write": writer},
    mode="sequential"
)

# Execute workflow
result = team.run("Write a blog post about AI")

## 📖 Detailed Documentation

Each agent family has comprehensive documentation:

1. **[SimpleAgent Documentation](src/haive/agents/simple/README.md)**
   - Version comparison (V1, V2, V3)
   - Prompt engineering patterns
   - Structured output examples

2. **[ReactAgent Documentation](src/haive/agents/react/README.md)**
   - Tool integration guide
   - Reasoning patterns
   - Error handling

3. **[MultiAgent Documentation](src/haive/agents/multi/README.md)**
   - Version comparison (V1-V4)
   - Execution modes
   - State management patterns

## 🏗️ Architecture Patterns

### Agent Hierarchy
```

Agent (base class)
├── SimpleAgent (basic LLM agent)
│ ├── SimpleAgentV2 (+ typed state)
│ └── SimpleAgentV3 (+ enhanced features)
├── ReactAgent (reasoning + tools)
└── MultiAgent (orchestration)
├── SimpleMultiAgent (basic)
├── MultiAgentV2 (+ state management)
├── MultiAgentV3 (+ async)
└── EnhancedMultiAgentV4 (+ all features)

````

### Key Concepts

1. **Engine (AugLLMConfig)**: LLM configuration for all agents
2. **Tools**: Functions that agents can call
3. **State**: Agent memory and context
4. **Orchestration**: Coordinating multiple agents

## 🛠️ Advanced Features

### Structured Output
```python
from pydantic import BaseModel

class AnalysisResult(BaseModel):
    sentiment: str
    confidence: float
    themes: list[str]

agent = SimpleAgent(
    name="analyzer",
    engine=AugLLMConfig(structured_output_model=AnalysisResult)
)
````

### Async Execution

```python
# All agents support async
result = await agent.arun("Process this asynchronously")

# Multi-agent parallel execution
results = await team.arun("Process in parallel", mode="parallel")
```

### State Persistence

```python
# Agents can save/load state
agent.save_state("agent_state.json")
restored_agent = SimpleAgent.load_state("agent_state.json")
```

## 🧪 Testing Agents

```python
# All agents use real LLMs in tests (no mocks)
def test_agent_with_real_llm():
    agent = SimpleAgent(
        name="test",
        engine=AugLLMConfig(temperature=0.1)  # Low for consistency
    )

    result = agent.run("Hello")
    assert isinstance(result, str)
    assert len(result) > 0
```

## 📋 Migration Guide

### Upgrading SimpleAgent

```python
# From default to V3
# Before:
agent = SimpleAgent(name="old")

# After:
from haive.agents.simple.agent_v3 import SimpleAgentV3
agent = SimpleAgentV3(name="new")  # Drop-in replacement
```

### Upgrading MultiAgent

```python
# From default to V4
# Before:
multi = MultiAgent(agents=[agent1, agent2])

# After:
from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
multi = EnhancedMultiAgentV4(
    agents=[agent1, agent2],
    execution_mode="sequential"  # Explicit mode
)
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

### Installation

```bash
# Install with poetry
poetry install

# Install with pip
pip install haive-agents
```

### Running Examples

```bash
# Basic examples
poetry run python examples/simple_agent_example.py
poetry run python examples/react_agent_example.py
poetry run python examples/multi_agent_example.py

# Advanced patterns
poetry run python examples/structured_output_example.py
poetry run python examples/parallel_execution_example.py
```

### Development Setup

```bash
# Install dependencies
poetry install --all-extras

# Run tests
poetry run pytest tests/ -v

# Run specific tests
poetry run pytest tests/simple/ -v
```

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

## 🛡️ Best Practices

### 1. Agent Design

- **Specialized agents** for specific tasks
- **Clear descriptions** for routing decisions
- **Robust error handling** in implementations
- **Appropriate tool selection**

### 2. Configuration

- **Clear system messages** for agent behavior
- **Appropriate model selection** for task complexity
- **Proper state management** for conversations
- **Resource optimization** for cost efficiency

### 3. Testing

- **Real LLM testing** - No mocks
- **Integration tests** - Full workflows
- **Error scenarios** - Edge cases
- **Performance testing** - Response times

## 🔗 Related Documentation

- [Haive Core Documentation](../haive-core/README.md)
- [Tool Integration Guide](../haive-tools/README.md)
- [Agent Patterns](../../project_docs/active/architecture/multi_agent_meta_agent_memory_hub.md)
- [CLAUDE.md](../../CLAUDE.md) - Main development hub

## 🤝 Contributing

When contributing new agents:

1. Follow the version naming convention
2. Maintain backward compatibility
3. Add comprehensive tests (no mocks)
4. Update relevant documentation
5. Add migration notes if needed

## 📈 Version History

### Latest Updates

- **SimpleAgentV3**: Enhanced base agent with hooks, recompilation
- **EnhancedMultiAgentV4**: Full async support, parallel execution
- **ReactAgent**: Stable, no version changes needed

### Version Policy

- Default imports remain stable for backward compatibility
- New features added in versioned classes (V2, V3, etc.)
- Migration guides provided for version upgrades

## 📝 License

MIT License - see [LICENSE](../../../LICENSE) for details.

## 🔗 Resources

- **[API Reference](https://haive.readthedocs.io)**
- **[GitHub Repository](https://github.com/haive/haive)**
- **[Discord Community](https://discord.gg/haive)**
- **[Blog & Tutorials](https://haive.ai/blog)**

For questions, issues, or contributions, please refer to the main project repository or create an issue.
