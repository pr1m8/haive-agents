# Enhanced Agent Pattern Refactoring Plan

## Overview

This document outlines the refactoring plan to migrate all agents to use the enhanced `Agent[EngineT]` pattern.

## Core Principle

Each agent type is defined by its engine type:

- **SimpleAgent** = `Agent[AugLLMConfig]`
- **ReactAgent** = `Agent[AugLLMConfig]` + reasoning loop
- **RAGAgent** = `Agent[RetrieverEngine]`
- **MultiAgent** = `Agent[AugLLMConfig]` + agents field

## Refactoring Order

### Phase 1: Core Agents (Immediate)

1. **SimpleAgent** ✅ (example created)
2. **ReactAgent**
3. **SupervisorAgent**
4. **DynamicSupervisor**

### Phase 2: Multi-Agent Patterns

5. **SequentialAgent**
6. **ParallelAgent**
7. **SimpleMultiAgent**

### Phase 3: RAG Agents

8. **BaseRAGAgent**
9. **SimpleRAGAgent**
10. **ConversationRAGAgent**
11. **DocumentRAGAgent**

## Implementation Strategy

### 1. SimpleAgent ✅

```python
class SimpleAgent(Agent[AugLLMConfig]):
    """SimpleAgent is just Agent[AugLLMConfig]."""
    pass
```

### 2. ReactAgent

```python
class ReactAgent(Agent[AugLLMConfig]):
    """ReactAgent with reasoning loop."""

    max_iterations: int = Field(default=10)

    def build_graph(self) -> BaseGraph:
        # Add reasoning loop to graph
        pass
```

### 3. SupervisorAgent

```python
class SupervisorAgent(Agent[AugLLMConfig]):
    """Supervisor that coordinates workers."""

    workers: Dict[str, Agent[Any]] = Field(default_factory=dict)

    def add_worker(self, name: str, agent: Agent[Any]) -> None:
        self.workers[name] = agent
```

### 4. DynamicSupervisor

```python
class DynamicSupervisor(SupervisorAgent):
    """Supervisor with dynamic worker management."""

    max_workers: int = Field(default=5)

    def can_add_worker(self) -> bool:
        return len(self.workers) < self.max_workers
```

### 5. Sequential/Parallel Agents

```python
class SequentialAgent(Agent[AugLLMConfig]):
    """Execute agents in sequence."""

    agents: List[Agent[Any]] = Field(default_factory=list)

    async def execute_sequence(self, input_data: Any) -> Any:
        result = input_data
        for agent in self.agents:
            result = await agent.arun(result)
        return result

class ParallelAgent(Agent[AugLLMConfig]):
    """Execute agents in parallel."""

    agents: List[Agent[Any]] = Field(default_factory=list)

    async def execute_parallel(self, input_data: Any) -> List[Any]:
        import asyncio
        tasks = [agent.arun(input_data) for agent in self.agents]
        return await asyncio.gather(*tasks)
```

### 6. RAG Agents

```python
# Define RetrieverEngine type
class RetrieverEngine(InvokableEngine):
    """Engine with retrieval capabilities."""
    retriever: Any

class BaseRAGAgent(Agent[RetrieverEngine]):
    """Base RAG agent with retrieval."""

    async def retrieve(self, query: str) -> List[Document]:
        return await self.engine.retriever.aretrieve(query)

class SimpleRAGAgent(BaseRAGAgent):
    """Simple RAG implementation."""
    pass
```

## Migration Steps

For each agent:

1. **Update inheritance**: Change from `Agent` to `Agent[EngineType]`
2. **Remove engine validation**: Engine type is enforced by generics
3. **Simplify initialization**: Remove complex engine setup
4. **Add engine-specific methods**: Based on engine capabilities
5. **Update tests**: Ensure type safety is tested
6. **Update documentation**: Add type annotations

## Type Definitions

```python
# Engine types to define
EngineT = TypeVar("EngineT", bound=InvokableEngine)
AugLLMConfig = Engine  # Standard LLM engine
RetrieverEngine = Engine  # Engine with retrieval
PlannerEngine = Engine  # Engine with planning capabilities
ReasoningEngine = Engine  # Engine with reasoning loop
```

## Benefits After Refactoring

1. **Type Safety**: Each agent knows its engine type
2. **Clean Code**: Minimal implementations
3. **Consistency**: Same pattern everywhere
4. **Extensibility**: Easy to add new agent types
5. **Documentation**: Types are self-documenting

## Testing Strategy

```python
# Type-safe testing
def test_simple_agent():
    agent = SimpleAgent(name="test", engine=AugLLMConfig())
    assert isinstance(agent.engine, AugLLMConfig)

def test_rag_agent():
    agent = BaseRAGAgent(name="rag", engine=RetrieverEngine())
    assert hasattr(agent, "retrieve")  # Method available due to engine type
```

## Timeline

- **Day 1**: SimpleAgent, ReactAgent ✅
- **Day 2**: Supervisor agents
- **Day 3**: Multi-agent patterns
- **Day 4**: RAG agents
- **Day 5**: Testing and documentation
