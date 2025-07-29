# Haive Agents Examples

This directory contains organized examples demonstrating various Haive agent patterns and capabilities.

## Directory Structure

### `core/` - Core Agent Examples

- **`simple/`** - Basic SimpleAgent examples
  - Basic agent creation and usage
  - Agent with structured output
  - Token tracking and monitoring
- **`react/`** - ReactAgent examples
  - Basic ReAct pattern
  - Dynamic tool discovery
  - Advanced ReAct patterns
- **`multi/`** - Multi-agent examples
  - Sequential multi-agent workflows
  - Parallel agent execution
  - Enhanced multi-agent patterns
- **`base/`** - Base agent patterns
  - Enhanced agent pattern
  - Custom agent implementations

### `advanced/` - Advanced Agent Patterns

- **`rag/`** - Retrieval-Augmented Generation
  - Simple RAG examples
  - Database RAG (SQL, Graph)
  - LLM-based RAG
- **`memory/`** - Memory agents
  - Conversation memory
  - Knowledge graph memory
  - Enhanced memory retrieval
- **`planning/`** - Planning agents
  - Plan-and-execute pattern
  - ReWOO tree planning
  - Hierarchical planning
- **`research/`** - Research agents
  - STORM research pattern
  - Multi-source research
- **`reasoning/`** - Reasoning and critique
  - Self-discover pattern
  - Tree of Thoughts (ToT)
  - Monte Carlo Tree Search (MCTS)
  - Language Agent Tree Search (LATS)
  - Reflexion pattern

### `patterns/` - Design Patterns

- **`composition/`** - Agent composition patterns
  - Agent-as-tool pattern
  - Nested agent structures
  - Chain patterns
- **`workflow/`** - Workflow patterns
  - Sequential workflows
  - Conditional routing
  - Dynamic activation
- **`tools/`** - Tool integration patterns
  - Dynamic tool discovery
  - State-synchronized tools
  - Tool generation patterns
- **`supervisor/`** - Supervisor patterns
  - Basic supervisor pattern
  - Three-node supervisor
  - Enhanced supervisor with choice

### `specialized/` - Specialized Domains

- **`conversation/`** - Conversation agents
  - Collaborative conversation
  - Debate agents
  - Round-robin conversation
  - Social media simulation
- **`document_processing/`** - Document modifiers
  - Summarization (iterative, map-branch)
  - Complex extraction
  - Text normalization (TNT)
- **`knowledge_graph/`** - Knowledge graph agents
  - KG construction
  - KG map-merge pattern
  - Graph analysis

## Running Examples

All examples can be run using poetry:

```bash
# Run a specific example
poetry run python examples/core/simple/basic_agent.py

# Run with environment variables
OPENAI_API_KEY=your_key poetry run python examples/core/react/dynamic_tools.py
```

## Example Categories

### Beginner-Friendly

Start with these examples if you're new to Haive:

1. `core/simple/basic_agent.py` - Simplest agent usage
2. `core/react/basic_react.py` - Basic ReAct pattern
3. `patterns/composition/simple_chain.py` - Simple agent chaining

### Intermediate

Once comfortable with basics:

1. `advanced/rag/simple_rag.py` - RAG implementation
2. `patterns/workflow/sequential_workflow.py` - Multi-agent workflows
3. `advanced/memory/conversation_memory.py` - Memory management

### Advanced

For complex use cases:

1. `advanced/reasoning/self_discover.py` - Advanced reasoning
2. `patterns/supervisor/enhanced_supervisor.py` - Complex orchestration
3. `specialized/knowledge_graph/kg_construction.py` - Graph-based reasoning

## Common Patterns

### 1. Agent Creation

```python
from haive.agents.simple import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig

agent = SimpleAgent(
    name="my_agent",
    engine=AugLLMConfig(temperature=0.7)
)
```

### 2. Tool Integration

```python
from haive.agents.react import ReactAgent
from langchain_core.tools import tool

@tool
def calculator(expression: str) -> float:
    """Calculate mathematical expression."""
    return eval(expression)

agent = ReactAgent(
    name="math_agent",
    engine=AugLLMConfig(),
    tools=[calculator]
)
```

### 3. Multi-Agent Coordination

```python
from haive.agents.multi import EnhancedMultiAgent

multi_agent = EnhancedMultiAgent(
    name="coordinator",
    agents=[agent1, agent2, agent3],
    execution_mode="sequential"
)
```

## Best Practices

1. **No Mocks**: All examples use real components
2. **Error Handling**: Examples include proper error handling
3. **Documentation**: Each example has comprehensive docstrings
4. **Real Use Cases**: Examples demonstrate practical scenarios
5. **Performance**: Examples show monitoring and optimization

## Contributing Examples

When adding new examples:

1. Place in appropriate category directory
2. Use descriptive filenames
3. Include comprehensive docstrings
4. Add run instructions in file header
5. Test with real components (no mocks)
6. Update this README with new example

## Testing Examples

Some examples that are more like tests should be moved to:
`packages/haive-agents/tests/examples/`

These include:

- Unit test-like demonstrations
- Edge case validations
- Performance benchmarks
- Integration test scenarios
