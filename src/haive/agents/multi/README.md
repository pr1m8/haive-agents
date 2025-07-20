# MultiAgent

Clean multi-agent coordinator for orchestrating multiple agents in different execution patterns.

## Overview

MultiAgent provides three execution modes for coordinating multiple agents:

- **Sequential**: Agents execute one after another, passing results forward
- **Parallel**: All agents execute simultaneously on the same input
- **Conditional**: A coordinator LLM routes to the appropriate agent

## Installation

```bash
poetry add haive-agents
```

## Quick Start

```python
from haive.agents.multi import MultiAgent
from haive.agents.simple import SimpleAgent

# Create individual agents
writer = SimpleAgent(name="writer", temperature=0.9)
editor = SimpleAgent(name="editor", temperature=0.3)

# Sequential pipeline
pipeline = MultiAgent(
    name="content_pipeline",
    agents={"writer": writer, "editor": editor},
    execution_mode="sequence"
)

result = pipeline.run("Write and edit a blog post about AI")
```

## Execution Modes

### Sequential Execution

Agents execute in the order they appear in the dictionary. Each agent receives the output of the previous agent.

```python
# Research → Write → Edit pipeline
researcher = SimpleAgent(name="researcher")
writer = SimpleAgent(name="writer")
editor = SimpleAgent(name="editor")

pipeline = MultiAgent(
    name="article_pipeline",
    agents={
        "research": researcher,
        "write": writer,
        "edit": editor
    },
    execution_mode="sequence"
)

article = pipeline.run("Create an article about quantum computing")
```

### Parallel Execution

All agents execute simultaneously with the same input. Useful for getting multiple perspectives or analyses.

```python
# Multiple analyzers working in parallel
sentiment = SimpleAgent(name="sentiment_analyzer")
keywords = SimpleAgent(name="keyword_extractor")
summary = SimpleAgent(name="summarizer")

analyzer = MultiAgent(
    name="text_analyzer",
    agents={
        "sentiment": sentiment,
        "keywords": keywords,
        "summary": summary
    },
    execution_mode="parallel"
)

results = analyzer.run("Analyze this customer review...")
```

### Conditional Execution

A coordinator LLM decides which agent to use based on the input.

```python
from haive.core.engine.aug_llm import AugLLMConfig

# Specialized agents
coder = SimpleAgent(name="coder", system_message="You are an expert programmer.")
writer = SimpleAgent(name="writer", system_message="You are a creative writer.")
analyst = SimpleAgent(name="analyst", system_message="You are a data analyst.")

# Router with coordinator
router = MultiAgent(
    name="smart_assistant",
    agents={
        "coder": coder,
        "writer": writer,
        "analyst": analyst
    },
    execution_mode="conditional",
    coordinator_config=AugLLMConfig(temperature=0.1)
)

# Coordinator will route to the appropriate agent
result1 = router.run("Write a Python function to sort a list")  # → coder
result2 = router.run("Write a poem about the ocean")  # → writer
result3 = router.run("Analyze these sales figures")  # → analyst
```

## API Reference

### Constructor

```python
MultiAgent(
    name: str = "MultiAgent",
    agents: dict[str, Agent] = {},
    execution_mode: str = "sequence",
    coordinator_config: AugLLMConfig | None = None,
    **kwargs
)
```

### Methods

- `add_agent(name: str, agent: Agent)` - Add an agent to the system
- `remove_agent(name: str)` - Remove an agent
- `get_agent(name: str) -> Agent | None` - Get an agent by name

Plus all methods inherited from base Agent:

- `run(input: str) -> Any` - Synchronous execution
- `arun(input: str) -> Any` - Asynchronous execution
- `stream(input: str) -> Iterator` - Streaming execution
- `astream(input: str) -> AsyncIterator` - Async streaming

## Advanced Examples

### Content Creation Pipeline

```python
# Create a full content creation pipeline
idea_generator = SimpleAgent(
    name="idea_generator",
    temperature=0.9,
    system_message="You generate creative content ideas."
)

outline_creator = SimpleAgent(
    name="outline_creator",
    temperature=0.5,
    system_message="You create detailed content outlines."
)

content_writer = SimpleAgent(
    name="content_writer",
    temperature=0.7,
    system_message="You write engaging content based on outlines."
)

fact_checker = SimpleAgent(
    name="fact_checker",
    temperature=0.1,
    system_message="You verify facts and improve accuracy."
)

pipeline = MultiAgent(
    name="content_factory",
    agents={
        "ideate": idea_generator,
        "outline": outline_creator,
        "write": content_writer,
        "verify": fact_checker
    },
    execution_mode="sequence"
)

article = pipeline.run("Create content about sustainable living")
```

### Multi-Perspective Analysis

```python
# Get different perspectives on the same topic
optimist = SimpleAgent(
    name="optimist",
    system_message="You analyze topics from an optimistic perspective."
)

pessimist = SimpleAgent(
    name="pessimist",
    system_message="You analyze topics from a pessimistic perspective."
)

realist = SimpleAgent(
    name="realist",
    system_message="You analyze topics from a realistic, balanced perspective."
)

analyzer = MultiAgent(
    name="perspective_analyzer",
    agents={
        "optimistic": optimist,
        "pessimistic": pessimist,
        "realistic": realist
    },
    execution_mode="parallel"
)

perspectives = analyzer.run("Analyze the future of AI in healthcare")
```

### Dynamic Agent Management

```python
# Start with base agents
multi = MultiAgent(name="dynamic_system")

# Add agents dynamically
multi.add_agent("translator", SimpleAgent(
    name="translator",
    system_message="You translate text between languages."
))

multi.add_agent("summarizer", SimpleAgent(
    name="summarizer",
    system_message="You create concise summaries."
))

# Remove agents when not needed
multi.remove_agent("translator")

# Check available agents
if multi.get_agent("summarizer"):
    result = multi.run("Summarize this document...")
```

## Best Practices

1. **Sequential Mode**: Order matters! Place agents in logical sequence
2. **Parallel Mode**: Ensure agents are truly independent
3. **Conditional Mode**: Use low temperature (0.1) for coordinator
4. **State Management**: Each agent maintains its own state
5. **Error Handling**: Individual agent failures don't crash the system

## Testing

```bash
poetry run pytest packages/haive-agents/tests/multi/
```

## See Also

- [SimpleAgent](../simple/README.md) - Basic agent implementation
- [SupervisorAgent](../supervisor/README.md) - Advanced routing with reasoning
- [ReactAgent](../react/README.md) - For reasoning loops

## Version History

- v1.0.0: Clean implementation with three execution modes
