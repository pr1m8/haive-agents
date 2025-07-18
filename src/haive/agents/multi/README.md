# Multi-Agent System - Unified Implementation

**Version**: 2.0  
**Status**: Production Ready  
**Implementation**: `clean.py` (Unified)

## Overview

The Multi-Agent system provides a unified, comprehensive solution for coordinating multiple agents in the Haive framework. This single implementation (`clean.py`) replaces all previous multi-agent implementations and supports both simple sequential execution and complex routing patterns.

## Key Features

- **🎯 Unified Implementation**: Single `MultiAgent` class handles all use cases
- **🔄 Flexible Routing**: Supports sequential, parallel, conditional, and custom routing
- **📝 List Initialization**: Natural `MultiAgent([agent1, agent2])` syntax
- **🎛️ Progressive Complexity**: Start simple, add sophistication as needed
- **🧠 Intelligent Routing**: Automatic routing inference via BaseGraph
- **🔧 Custom Routing**: Explicit routing control for complex scenarios
- **📊 Real Component Testing**: 100% no-mocks testing approach
- **🔍 Type Safety**: Full type hints and Pydantic validation

## Quick Start

### Basic Sequential Execution

```python
from haive.agents.multi.clean import MultiAgent
from haive.agents.simple import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig

# Create agents
agent1 = SimpleAgent(name="analyzer", engine=AugLLMConfig())
agent2 = SimpleAgent(name="summarizer", engine=AugLLMConfig())
agent3 = SimpleAgent(name="reporter", engine=AugLLMConfig())

# Create multi-agent (natural list syntax)
multi_agent = MultiAgent(agents=[agent1, agent2, agent3])

# Execute
result = await multi_agent.arun("Process this data")
```

### Conditional Routing

```python
# Create specialized agents
classifier = SimpleAgent(name="classifier", engine=AugLLMConfig())
billing_agent = SimpleAgent(name="billing", engine=AugLLMConfig())
technical_agent = SimpleAgent(name="technical", engine=AugLLMConfig())

# Create multi-agent with entry point
multi_agent = MultiAgent(
    agents=[classifier, billing_agent, technical_agent],
    entry_point="classifier"
)

# Add conditional routing
def route_by_category(state):
    return state.get("category", "general")

multi_agent.add_conditional_routing(
    "classifier",
    route_by_category,
    {
        "billing": "billing",
        "technical": "technical",
        "general": "billing"  # Default
    }
)

# Execute with routing
result = await multi_agent.arun("I have a billing question")
```

### Parallel Processing

```python
# Create processing agents
data_processor = SimpleAgent(name="data_proc", engine=AugLLMConfig())
image_processor = SimpleAgent(name="image_proc", engine=AugLLMConfig())
text_processor = SimpleAgent(name="text_proc", engine=AugLLMConfig())
aggregator = SimpleAgent(name="aggregator", engine=AugLLMConfig())

multi_agent = MultiAgent(agents=[data_processor, image_processor, text_processor, aggregator])

# Run processors in parallel, then aggregate
multi_agent.add_parallel_group(
    ["data_proc", "image_proc", "text_proc"],
    next_agent="aggregator"
)

result = await multi_agent.arun("Process all data types")
```

## Architecture

### Class Hierarchy

```
Agent (Base Class)
└── MultiAgent
    ├── Uses BaseGraph for intelligent routing
    ├── Supports custom routing patterns
    └── Manages MultiAgentState by default
```

### Routing Modes

1. **Intelligent Routing** (Default): Uses BaseGraph to automatically infer execution patterns
2. **Custom Routing**: Explicit routing control when using enhanced methods

### State Management

- **Default**: `MultiAgentState` for message passing and context sharing
- **Customizable**: Any StateSchema can be used
- **Automatic**: Proper field sharing and reducers

## API Reference

### Core Class

```python
class MultiAgent(Agent):
    """Unified multi-agent coordination system."""

    agents: Dict[str, Agent]              # Coordinated agents
    execution_mode: str                   # "infer", "sequential", "parallel", etc.
    entry_point: Optional[str]            # Starting agent
    branches: Dict[str, Dict[str, Any]]   # Routing configuration
```

### Initialization Methods

```python
# List initialization (recommended)
MultiAgent(agents=[agent1, agent2, agent3])

# Dictionary initialization
MultiAgent(agents={"first": agent1, "second": agent2})

# Factory method
MultiAgent.create(
    agents=[agent1, agent2],
    name="workflow",
    execution_mode="sequential"
)
```

### Routing Methods

```python
# Conditional routing with functions
multi_agent.add_conditional_routing(
    source_agent="classifier",
    condition_fn=lambda state: state.get("category"),
    routes={"billing": "billing_agent", "tech": "tech_agent"}
)

# Direct agent-to-agent connections
multi_agent.add_edge("agent1", "agent2")

# Parallel execution groups
multi_agent.add_parallel_group(
    agent_names=["agent1", "agent2"],
    next_agent="aggregator"
)

# Manual sequence ordering
multi_agent.set_sequence(["agent2", "agent1", "agent3"])
```

### Legacy Support

```python
# Legacy branch method (still supported)
multi_agent.add_branch(
    source_agent="classifier",
    condition="if category == 'urgent'",
    target_agents=["urgent_processor"]
)
```

## Usage Patterns

### 1. Content Creation Pipeline

```python
# Research → Write → Optimize → Review
researcher = SimpleAgent(name="researcher", engine=AugLLMConfig())
writer = SimpleAgent(name="writer", engine=AugLLMConfig())
optimizer = SimpleAgent(name="optimizer", engine=AugLLMConfig())
reviewer = SimpleAgent(name="reviewer", engine=AugLLMConfig())

content_pipeline = MultiAgent(agents=[researcher, writer, optimizer, reviewer])
```

### 2. Customer Support Escalation

```python
# Classifier → Specialist → Senior (if needed)
classifier = SimpleAgent(name="classifier", engine=AugLLMConfig())
billing_specialist = SimpleAgent(name="billing", engine=AugLLMConfig())
tech_specialist = SimpleAgent(name="technical", engine=AugLLMConfig())
senior_agent = SimpleAgent(name="senior", engine=AugLLMConfig())

support_system = MultiAgent(
    agents=[classifier, billing_specialist, tech_specialist, senior_agent],
    entry_point="classifier"
)

# Route by ticket type
support_system.add_conditional_routing(
    "classifier",
    lambda state: state.get("ticket_type"),
    {"billing": "billing", "technical": "technical"}
)

# Escalation if needed
support_system.add_conditional_routing(
    "billing",
    lambda state: "senior" if state.get("escalate") else "END",
    {"senior": "senior", "END": "END"}
)
```

### 3. Data Analysis Workflow

```python
# Parallel Analysis → Synthesis
financial_analyst = SimpleAgent(name="financial", engine=AugLLMConfig())
risk_analyst = SimpleAgent(name="risk", engine=AugLLMConfig())
market_analyst = SimpleAgent(name="market", engine=AugLLMConfig())
synthesizer = SimpleAgent(name="synthesizer", engine=AugLLMConfig())

analysis_workflow = MultiAgent(agents=[
    financial_analyst, risk_analyst, market_analyst, synthesizer
])

# Run analysis in parallel, then synthesize
analysis_workflow.add_parallel_group(
    ["financial", "risk", "market"],
    next_agent="synthesizer"
)
```

## Advanced Features

### State Schema Customization

```python
from haive.core.schema import StateSchema
from pydantic import Field

class CustomWorkflowState(StateSchema):
    """Custom state for workflow tracking."""

    workflow_id: str = Field(...)
    priority: int = Field(default=1)
    metadata: Dict[str, Any] = Field(default_factory=dict)

multi_agent = MultiAgent(
    agents=[agent1, agent2],
    state_schema=CustomWorkflowState
)
```

### Dynamic Agent Addition

```python
# Start with basic agents
multi_agent = MultiAgent(agents=[agent1, agent2])

# Add more agents dynamically
new_agent = SimpleAgent(name="new_processor", engine=AugLLMConfig())
multi_agent.agents["new_processor"] = new_agent

# Update routing
multi_agent.add_edge("agent1", "new_processor")
```

### Execution Mode Control

```python
# Automatic inference (default)
multi_agent = MultiAgent(agents=[agent1, agent2], execution_mode="infer")

# Force sequential
multi_agent = MultiAgent(agents=[agent1, agent2], execution_mode="sequential")

# Force parallel
multi_agent = MultiAgent(agents=[agent1, agent2], execution_mode="parallel")
```

## Testing

### Real Component Testing (NO MOCKS)

```python
import pytest
from haive.agents.multi.clean import MultiAgent
from haive.agents.simple import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig

@pytest.mark.asyncio
async def test_real_multiagent_execution():
    """Test with REAL LLM calls."""
    agent1 = SimpleAgent(name="greeter", engine=AugLLMConfig(temperature=0.1))
    agent2 = SimpleAgent(name="responder", engine=AugLLMConfig(temperature=0.1))

    multi_agent = MultiAgent(agents=[agent1, agent2])

    # Real execution
    result = await multi_agent.arun("Hello, process this message")

    assert result is not None
    assert isinstance(result, (str, dict))
```

### Running Tests

```bash
# Run all multi-agent tests
poetry run pytest packages/haive-agents/tests/multi/ -v

# Run specific test file
poetry run pytest packages/haive-agents/tests/multi/test_clean_multiagent.py -v

# Run with coverage
poetry run pytest packages/haive-agents/tests/multi/ --cov=haive.agents.multi --cov-report=html
```

## Migration Guide

### From Legacy Implementations

The unified implementation in `clean.py` provides backward compatibility:

```python
# Old way (still works)
from haive.agents.multi.base import SequentialAgent, ParallelAgent

sequential = SequentialAgent(agents=[agent1, agent2])
parallel = ParallelAgent(agents=[agent1, agent2])

# New way (recommended)
from haive.agents.multi.clean import MultiAgent

sequential = MultiAgent(agents=[agent1, agent2], execution_mode="sequential")
parallel = MultiAgent(agents=[agent1, agent2], execution_mode="parallel")
```

### From Business Examples

Update imports in existing code:

```python
# Old import
from haive.agents.multi.base import MultiAgent, SequentialAgent, ParallelAgent

# New import
from haive.agents.multi.clean import MultiAgent

# Usage remains the same
multi_agent = MultiAgent(agents=[agent1, agent2])
```

## Performance Considerations

### Best Practices

1. **Agent Reuse**: Share agents across multiple MultiAgent instances when possible
2. **State Management**: Use appropriate state schemas for your use case
3. **Routing Efficiency**: Use intelligent routing for simple cases, custom routing for complex scenarios
4. **Resource Management**: Monitor memory usage with large numbers of agents

### Optimization Tips

```python
# Efficient agent creation
config = AugLLMConfig(temperature=0.7)  # Reuse config
agents = [SimpleAgent(name=f"agent_{i}", engine=config) for i in range(5)]

# Batch operations
multi_agent = MultiAgent(agents=agents)
multi_agent.add_parallel_group([f"agent_{i}" for i in range(3)])
```

## Error Handling

### Common Issues

1. **Agent Name Conflicts**: Automatically resolved with suffixes
2. **Missing Agents**: Validation in routing methods
3. **Circular Dependencies**: Detected by BaseGraph
4. **State Schema Conflicts**: Clear error messages

### Debugging

```python
# Enable debug mode
multi_agent = MultiAgent(agents=[agent1, agent2])
graph = multi_agent.build_graph()

# Inspect routing
print(f"Branches: {multi_agent.branches}")
print(f"Execution mode: {multi_agent.execution_mode}")
print(f"Entry point: {multi_agent.entry_point}")
```

## Integration

### With Other Haive Components

```python
# With RAG agents
from haive.agents.rag.base import BaseRAGAgent

rag_agent = BaseRAGAgent(name="knowledge", engine=AugLLMConfig())
simple_agent = SimpleAgent(name="processor", engine=AugLLMConfig())

multi_agent = MultiAgent(agents=[rag_agent, simple_agent])
```

### With Tools

```python
from langchain_core.tools import tool

@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    return str(eval(expression))

# Agents can have tools
agent_with_tools = SimpleAgent(
    name="calculator_agent",
    engine=AugLLMConfig(),
    tools=[calculator]
)

multi_agent = MultiAgent(agents=[agent_with_tools, other_agent])
```

## File Structure

```
haive/agents/multi/
├── clean.py              # ✅ Unified implementation (USE THIS)
├── base.py               # Compatibility layer
├── archive/              # Legacy implementations
├── README.md             # This file
└── examples/
    ├── business_workflows.py
    ├── content_pipeline.py
    └── support_system.py
```

## Future Enhancements

- **Visual Workflow Designer**: GUI for complex routing design
- **Performance Monitoring**: Built-in metrics and profiling
- **Dynamic Scaling**: Auto-scaling based on load
- **Workflow Templates**: Pre-built patterns for common use cases

## Support

- **Documentation**: [Haive Multi-Agent Docs](https://docs.haive.ai/agents/multi)
- **Examples**: See `examples/` directory
- **Tests**: See `tests/multi/` directory
- **Issues**: Report via GitHub issues

---

**Note**: This is the unified implementation that replaces all previous multi-agent approaches. Use `clean.py` for all new development.
