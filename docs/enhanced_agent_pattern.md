# Enhanced Agent Pattern Documentation

## Overview

The enhanced agent pattern introduces engine-focused generics to the Haive agent architecture. This pattern provides type safety, clear separation of concerns, and a clean implementation hierarchy.

## Core Concepts

### 1. The Hierarchy

```
Workflow (pure orchestration - no LLM)
└── Agent[EngineT] (Workflow + Engine)
    ├── SimpleAgent = Agent[AugLLMConfig]
    ├── ReactAgent = Agent[AugLLMConfig] + reasoning
    ├── RAGAgent = Agent[RetrieverEngine]
    └── MultiAgent = Agent[AugLLMConfig] + agents: Dict[str, Agent]
```

### 2. Key Insight

**The engine type IS the primary differentiator between agent types.**

- `SimpleAgent` is just `Agent[AugLLMConfig]`
- `RAGAgent` is just `Agent[RetrieverEngine]`
- `ReasoningAgent` is just `Agent[ReasoningEngine]`

## Implementation

### Basic Pattern

```python
from typing import TypeVar, Generic
from haive.core.engine.base import InvokableEngine

# Engine-focused generic
EngineT = TypeVar("EngineT", bound=InvokableEngine)

class Workflow(ABC):
    """Pure orchestration without engine."""
    @abstractmethod
    async def execute(self, input_data: Any) -> Any:
        pass

class Agent(Workflow, Generic[EngineT]):
    """Agent = Workflow + Engine."""
    def __init__(self, name: str, engine: EngineT):
        self.name = name
        self.engine = engine
```

### SimpleAgent Implementation

```python
class SimpleAgent(Agent[AugLLMConfig]):
    """SimpleAgent is just Agent[AugLLMConfig].

    That's it! The entire implementation.
    """
    pass
```

### Type-Safe Engine Access

```python
# SimpleAgent knows its engine is AugLLMConfig
simple = SimpleAgent(name="assistant", engine=AugLLMConfig())
simple.engine.temperature = 0.7  # Type-safe!

# RAGAgent knows its engine is RetrieverEngine
rag = RAGAgent(name="researcher", engine=RetrieverEngine())
docs = await rag.engine.retrieve("query")  # Type-safe!
```

## Benefits

### 1. Type Safety

- Engine type is known at compile time
- IDE autocomplete for engine-specific features
- Prevents passing wrong engine types

### 2. Clean Architecture

- Clear separation: Workflow vs Agent vs MultiAgent
- Engine determines capabilities
- Minimal implementation needed

### 3. Extensibility

- New agent types = new engine types
- Easy to add specialized agents
- Consistent pattern across all agents

## Migration Guide

### From Old Pattern

```python
# Old pattern
class SimpleAgent(Agent):
    def __init__(self, engine: AugLLMConfig = None):
        if engine is None:
            engine = AugLLMConfig()
        super().__init__(engine=engine)
```

### To Enhanced Pattern

```python
# Enhanced pattern
class SimpleAgent(Agent[AugLLMConfig]):
    # That's it! Engine type is in the inheritance
    pass
```

## Examples

### Creating Different Agent Types

```python
# Simple conversational agent
simple = SimpleAgent(
    name="assistant",
    engine=AugLLMConfig(temperature=0.7)
)

# RAG agent with retrieval
rag = RAGAgent(
    name="researcher",
    engine=RetrieverEngine(index="knowledge_base")
)

# Multi-modal agent
multimodal = MultiModalAgent(
    name="vision",
    engine=MultiModalEngine(modalities=["text", "image"])
)
```

### Multi-Agent Coordination

```python
# Coordinator is Agent[AugLLMConfig] because it uses LLM
coordinator = MultiAgent(
    name="coordinator",
    engine=AugLLMConfig(temperature=0.3),
    agents={
        "simple": simple,
        "rag": rag,
        "multimodal": multimodal
    }
)
```

## Best Practices

1. **Let the engine type define the agent**: Don't add complex logic to agent subclasses
2. **Use type annotations**: Always specify `Agent[EngineType]` for clarity
3. **Keep agents minimal**: Most functionality should come from the base Agent class
4. **Engine-specific methods**: Add methods that make sense for the engine type

## Common Patterns

### Convenience Fields

```python
class SimpleAgent(Agent[AugLLMConfig]):
    # Convenience fields that sync to engine
    temperature: float = Field(default=0.7)

    def setup_agent(self):
        # Sync to engine
        self.engine.temperature = self.temperature
```

### Engine-Specific Methods

```python
class RAGAgent(Agent[RetrieverEngine]):
    async def retrieve(self, query: str) -> List[Document]:
        """Available because engine is RetrieverEngine."""
        return await self.engine.retrieve(query)
```

### Type Guards

```python
def process_agent(agent: Agent[Any]):
    if isinstance(agent, Agent[AugLLMConfig]):
        # Type-safe access to AugLLMConfig features
        agent.engine.temperature = 0.5
    elif isinstance(agent, Agent[RetrieverEngine]):
        # Type-safe access to RetrieverEngine features
        docs = agent.engine.retrieve("query")
```

## Future Enhancements

1. **Automatic schema generation** based on engine type
2. **Engine-specific graph building** patterns
3. **Type-safe inter-agent communication**
4. **Engine composition** for multi-capability agents

## Summary

The enhanced agent pattern simplifies agent development by making the engine type the primary generic parameter. This provides:

- **Clarity**: `SimpleAgent = Agent[AugLLMConfig]`
- **Type Safety**: Engine capabilities are type-checked
- **Simplicity**: Minimal code needed for new agents
- **Consistency**: Same pattern for all agent types

The pattern makes it clear that agents are differentiated primarily by their engine type, not by complex inheritance hierarchies or duplicated logic.
