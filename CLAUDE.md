# CLAUDE.md - Haive Agents Package Guide

**Purpose**: Central guide for working with the haive-agents package
**Version**: 1.0
**Last Updated**: 2025-01-18

## 🎯 Package Overview

Haive Agents provides **truly dynamic agents** capable of self-modification, self-replication, runtime adaptation, and autonomous coordination. This is not just another agent framework - it's a system for building agents that can **modify their own behavior**, **spawn new agents**, and **coordinate complex workflows** in real-time.

**Key Innovation**: Agents that adapt, evolve, and self-organize based on task requirements, without predefined configuration.

## 📁 Directory Structure

```
haive-agents/
├── src/haive/agents/
│   ├── __init__.py              # Main exports and module docstring
│   │
│   ├── simple/                  # Foundation agents
│   │   ├── agent.py             # SimpleAgent - conversation, structured output
│   │   ├── agent_v2.py          # Enhanced SimpleAgent with state management
│   │   ├── agent_v3.py          # Latest SimpleAgent with hooks & recompilation
│   │   └── __init__.py          # Simple agent exports
│   │
│   ├── react/                   # ReAct pattern agents
│   │   ├── agent.py             # ReactAgent - tools, reasoning, planning
│   │   ├── agent_v2.py          # Enhanced ReactAgent with better loops
│   │   ├── agent_v3.py          # Latest ReactAgent with V3 improvements
│   │   └── __init__.py          # React agent exports
│   │
│   ├── multi/                   # Multi-agent coordination
│   │   ├── multi_agent.py       # Basic MultiAgent coordination
│   │   ├── enhanced_multi_agent_v3.py  # Enhanced with generics
│   │   ├── enhanced_multi_agent_v4.py  # Latest with full async support
│   │   └── __init__.py          # Multi-agent exports
│   │
│   ├── agent/                   # Advanced agent capabilities
│   │   ├── dynamic_supervisor.py       # DynamicSupervisorAgent
│   │   ├── self_modifying_agent.py     # Self-modification capabilities
│   │   ├── self_replicating_agent.py   # Self-replication system
│   │   ├── provider_switching_agent.py # Provider hot-swapping
│   │   └── __init__.py          # Advanced agent exports
│   │
│   ├── memory_reorganized/      # 🧠 COMPREHENSIVE MEMORY SYSTEM
│   │   ├── __init__.py          # Memory system exports & architecture docs
│   │   ├── agents/              # Memory-enhanced agents
│   │   │   ├── simple.py        # SimpleMemoryAgent with classification
│   │   │   ├── react.py         # ReactMemoryAgent with context
│   │   │   ├── multi.py         # MultiMemoryAgent coordination
│   │   │   └── ltm.py           # LongTermMemoryAgent with consolidation
│   │   ├── retrieval/           # Advanced retrieval systems
│   │   │   ├── graph_rag_retriever.py      # Graph RAG with Neo4j traversal
│   │   │   └── enhanced_retriever.py       # Multi-factor retrieval scoring
│   │   ├── coordination/        # Memory system coordination
│   │   │   ├── integrated_memory_system.py # Unified memory coordination
│   │   │   └── multi_agent_coordinator.py  # Multi-agent memory sharing
│   │   ├── knowledge/           # Knowledge graph management
│   │   │   └── kg_generator_agent.py       # Automatic graph construction
│   │   ├── core/                # Core memory functionality
│   │   │   ├── classifier.py    # LLM-based memory classification
│   │   │   └── types.py         # 11 memory type definitions
│   │   └── search/              # Search agents
│   │       ├── quick_search/    # Fast semantic search (<10ms)
│   │       └── pro_search/      # Deep relationship search (100-500ms)
│   │
│   └── base/                    # Base classes and mixins
│       ├── agent.py             # Base Agent class
│       ├── mixins/              # Capability mixins
│       │   ├── self_modification.py   # Self-modification mixin
│       │   ├── replication.py         # Replication mixin
│       │   ├── provider_switching.py  # Provider switching mixin
│       │   └── tool_transfer.py       # Tool sharing mixin
│       └── __init__.py          # Base exports
│
├── examples/                    # Organized examples
│   ├── basic/                   # Getting started
│   ├── advanced/                # Complex patterns
│   ├── self_modification/       # Self-modifying examples
│   └── dynamic_supervision/     # Supervisor examples
│
├── tests/                       # Comprehensive tests (NO MOCKS)
│   ├── simple/                  # SimpleAgent tests
│   ├── react/                   # ReactAgent tests
│   ├── multi/                   # Multi-agent tests
│   ├── agent/                   # Advanced agent tests
│   └── integration/             # End-to-end tests
│
└── project_docs/               # Package documentation
    ├── guides/                  # Usage guides
    ├── architecture/            # System design
    ├── patterns/                # Implementation patterns
    └── examples/                # Code examples
```

## 🚀 Quick Start Commands

```bash
# Install package with dependencies
poetry install

# Run basic examples
poetry run python examples/basic/simple_agent_example.py
poetry run python examples/basic/react_agent_example.py
poetry run python examples/basic/multi_agent_example.py

# Run advanced examples
poetry run python examples/advanced/self_organizing_team.py
poetry run python examples/advanced/adaptive_pipeline.py
poetry run python examples/self_modification/evolving_agent.py

# Run dynamic supervision examples
poetry run python examples/dynamic_supervision/supervisor_demo.py
poetry run python examples/dynamic_supervision/hierarchical_system.py
```

## 💻 Common Development Tasks

### 1. Creating a Basic Agent

```python
# In your script or module
from haive.agents.simple import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig

# Simple conversational agent
agent = SimpleAgent(
    name="assistant",
    engine=AugLLMConfig(temperature=0.7)
)

# Execute
result = await agent.arun("Hello, how can you help me?")
```

### 2. Creating a ReAct Agent with Tools

```python
from haive.agents.react import ReactAgent
from langchain_core.tools import tool

@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    return str(eval(expression))

@tool 
def web_search(query: str) -> str:
    """Search the web for information."""
    return f"Search results for: {query}"

# ReAct agent with reasoning and tools
agent = ReactAgent(
    name="research_assistant",
    engine=AugLLMConfig(tools=[calculator, web_search]),
    max_iterations=5
)

result = await agent.arun("What is 15 * 23 and find info about that number?")
```

### 3. Creating Multi-Agent Workflows

```python
from haive.agents.multi import MultiAgent

# Create specialized agents
researcher = ReactAgent(name="researcher", tools=[web_search])
writer = SimpleAgent(name="writer", engine=AugLLMConfig(temperature=0.8))
reviewer = SimpleAgent(name="reviewer", engine=AugLLMConfig(temperature=0.3))

# Coordinate them in a workflow
workflow = MultiAgent(
    name="content_pipeline",
    agents=[researcher, writer, reviewer],
    execution_mode="sequential"
)

result = await workflow.arun("Create a blog post about AI trends")
```

### 4. Dynamic Supervision Pattern

```python
from haive.agents.agent import DynamicSupervisorAgent

# Create supervisor that can spawn agents
supervisor = DynamicSupervisorAgent(
    name="adaptive_coordinator",
    engine=AugLLMConfig(),
    enable_agent_builder=True
)

# Supervisor automatically creates needed agents
result = await supervisor.arun(
    "Analyze this dataset, create visualizations, and write a report"
)
# Creates: DataAnalyst → Visualizer → ReportWriter automatically
```

### 5. Self-Modifying Agent Pattern

```python
from haive.agents.agent import SelfModifyingAgent

class AdaptiveAgent(SelfModifyingAgent):
    """Agent that modifies itself based on performance."""
    
    async def arun(self, input_data):
        # Execute task
        result = await super().arun(input_data)
        
        # Analyze and self-modify if needed
        if self.performance_below_threshold():
            await self.modify_behavior({
                "temperature": 0.1,  # More deterministic
                "system_message": "You are an expert analyst.",
                "tools": self.tools + [additional_tool]
            })
        
        return result

agent = AdaptiveAgent(name="adaptive", engine=AugLLMConfig())
```

### 6. Self-Replicating Agent Pattern

```python
from haive.agents.agent import SelfReplicatingAgent

class ReplicatingAgent(SelfReplicatingAgent):
    async def replicate_for_task(self, task_type: str):
        """Create specialized copies for different tasks."""
        
        if task_type == "analysis":
            return await self.replicate({
                "name": f"{self.name}_analyst",
                "temperature": 0.1,
                "system_message": "You are a data analysis expert.",
                "tools": self.tools + [analysis_tool]
            })
        elif task_type == "creative":
            return await self.replicate({
                "name": f"{self.name}_creative", 
                "temperature": 0.9,
                "system_message": "You are a creative writing expert.",
                "tools": [writing_tool, inspiration_tool]
            })

# Original agent creates specialized versions
agent = ReplicatingAgent(name="base", engine=config)
analyst = await agent.replicate_for_task("analysis")
writer = await agent.replicate_for_task("creative")
```

### 7. Graph-Based Memory System

```python
from haive.agents.memory_reorganized import SimpleMemoryAgent
from haive.agents.memory_reorganized.coordination import IntegratedMemorySystem

# Create memory-enhanced agent with automatic classification
memory_agent = SimpleMemoryAgent(
    name="assistant",
    memory_config={
        "enable_classification": True,
        "store_type": "integrated",  # Graph + Vector + Time
        "neo4j_config": neo4j_config
    }
)

# Store memory with automatic processing
await memory_agent.store_memory("I learned Python at university in 2020")
# -> Classified as EPISODIC + EDUCATION
# -> Entities: ["Python", "university", "2020"]
# -> Graph relationships created

# Retrieve with memory-aware context
results = await memory_agent.retrieve_memories("programming experience")
# -> Multi-factor scoring: similarity + graph + recency + importance
```

### 8. Advanced Graph RAG Retrieval

```python
from haive.agents.memory_reorganized.retrieval import GraphRAGRetriever
from haive.agents.memory_reorganized.knowledge import KGGeneratorAgent

# Setup Graph RAG with knowledge graph
kg_agent = KGGeneratorAgent(neo4j_config=neo4j_config)
retriever = GraphRAGRetriever(
    kg_agent=kg_agent,
    vector_store=chroma_store,
    enable_graph_traversal=True
)

# Query with graph context
result = await retriever.retrieve_memories(
    "What's the relationship between Python and machine learning?"
)

print(f"Memories: {len(result.memories)}")
print(f"Graph nodes explored: {result.graph_nodes_explored}")
print(f"Relationship paths: {len(result.relationship_paths)}")
print(f"Performance: {result.total_time_ms:.1f}ms")
```

## 🧪 Testing

```bash
# Run all tests (NO MOCKS - real LLMs)
poetry run pytest tests/

# Run specific test categories
poetry run pytest tests/simple/ -v          # SimpleAgent tests
poetry run pytest tests/react/ -v           # ReactAgent tests
poetry run pytest tests/multi/ -v           # Multi-agent tests
poetry run pytest tests/agent/ -v           # Advanced agent tests

# Run integration tests
poetry run pytest tests/integration/ -v     # End-to-end tests

# Run with coverage
poetry run pytest --cov=haive.agents
```

## 📝 Documentation

### Building Docs
```bash
# Build package documentation
cd project_docs
poetry run sphinx-build -b html source build

# View locally
python -m http.server 8000 --directory build
```

### Key Documentation Files
- `project_docs/guides/quick-start.md` - Getting started
- `project_docs/architecture/README.md` - System design
- `project_docs/patterns/` - Implementation patterns
- `project_docs/examples/` - Working examples

## 🔧 Common Patterns

### Pattern 1: Foundation Agent (SimpleAgent)
```python
# Basic conversation
agent = SimpleAgent(name="chatbot", engine=AugLLMConfig())

# With structured output
from pydantic import BaseModel, Field

class AnalysisResult(BaseModel):
    sentiment: str = Field(description="positive/negative/neutral")
    confidence: float = Field(ge=0.0, le=1.0)

structured_agent = SimpleAgent(
    name="analyzer",
    engine=AugLLMConfig(structured_output_model=AnalysisResult)
)
```

### Pattern 2: Tool-Enabled Agent (ReactAgent)
```python
# Agent with reasoning and tools
agent = ReactAgent(
    name="assistant",
    engine=AugLLMConfig(tools=[calculator, web_search]),
    max_iterations=3
)
```

### Pattern 3: Multi-Agent Coordination
```python
# Sequential workflow
workflow = MultiAgent(
    name="pipeline",
    agents=[planner, executor, reviewer],
    execution_mode="sequential"
)

# Parallel execution
parallel_workflow = MultiAgent(
    name="analysis",
    agents=[analyzer1, analyzer2, analyzer3],
    execution_mode="parallel"
)

# Conditional routing
conditional_workflow = MultiAgent(
    name="smart_router",
    agents=[classifier, simple_processor, complex_processor],
    execution_mode="conditional"
)

# Add routing logic
conditional_workflow.add_conditional_edge(
    from_agent="classifier",
    condition=lambda state: state.get("complexity") > 0.7,
    true_agent="complex_processor",
    false_agent="simple_processor"
)
```

### Pattern 4: Dynamic Agent Creation
```python
# Supervisor that creates agents on-demand
supervisor = DynamicSupervisorAgent(
    name="meta_coordinator",
    enable_agent_builder=True
)

# Analyzes task and creates appropriate agents
result = await supervisor.arun("Complex multi-step task description")
```

### Pattern 5: Self-Improving Agents
```python
# Agent that evolves based on feedback
class EvolvingAgent(SimpleAgent, SelfModifyingAgent, SelfReplicatingAgent):
    async def evolve_from_feedback(self, feedback: Dict[str, Any]):
        if feedback["accuracy"] < 0.7:
            improved = await self.replicate({
                "temperature": self.engine.temperature * 0.8,
                "system_message": f"{self.engine.system_message}\nFocus on accuracy."
            })
            return improved
        return self
```

### Pattern 6: Provider Switching
```python
from haive.agents.agent import ProviderSwitchingAgent

class AdaptiveAgent(ProviderSwitchingAgent):
    async def optimize_for_task(self, task_complexity: float):
        if task_complexity > 0.8:
            # Use powerful model for complex tasks
            await self.switch_provider({
                "provider": "azure",
                "model": "gpt-4",
                "temperature": 0.1
            })
        else:
            # Use efficient model for simple tasks
            await self.switch_provider({
                "provider": "openai",
                "model": "gpt-3.5-turbo", 
                "temperature": 0.7
            })
```

## 🚨 Important Notes

1. **Dynamic Nature**: The key innovation is **runtime adaptation** - agents modify themselves as needed

2. **No Mocks**: Always test with real LLMs and components, never mock agent behavior

3. **Async First**: All agent operations are async - use `await` properly

4. **Real-Time Recompilation**: Agents automatically rebuild when configuration changes

5. **State Management**: Use proper state schemas for multi-agent coordination

## 🔍 Debugging

```python
# Enable debug logging
import logging
logging.getLogger("haive.agents").setLevel(logging.DEBUG)

# Check agent configuration
agent.validate_configuration()

# Display agent debug info
agent.display_debug_info()

# Monitor multi-agent execution
workflow.enable_execution_monitoring()

# Manually trigger recompilation
await agent.rebuild_graph()
```

## 🎯 Key Files for Different Tasks

### Working on Simple Agents
- `src/haive/agents/simple/agent_v3.py` - Latest SimpleAgent implementation
- `src/haive/agents/simple/__init__.py` - Simple agent exports
- `tests/simple/` - SimpleAgent tests

### Working on ReAct Agents
- `src/haive/agents/react/agent_v3.py` - Latest ReactAgent implementation
- `src/haive/agents/react/__init__.py` - React agent exports
- `tests/react/` - ReactAgent tests

### Working on Multi-Agent Systems
- `src/haive/agents/multi/enhanced_multi_agent_v4.py` - Latest multi-agent implementation
- `src/haive/agents/multi/__init__.py` - Multi-agent exports
- `tests/multi/` - Multi-agent tests

### Working on Advanced Capabilities
- `src/haive/agents/agent/dynamic_supervisor.py` - Dynamic supervision
- `src/haive/agents/agent/self_modifying_agent.py` - Self-modification
- `src/haive/agents/agent/self_replicating_agent.py` - Self-replication
- `tests/agent/` - Advanced agent tests

### Working on Base Classes
- `src/haive/agents/base/agent.py` - Base Agent class
- `src/haive/agents/base/mixins/` - Capability mixins
- `tests/base/` - Base class tests

## 🚀 Next Steps

1. **Enhanced Reasoning**: Integrate Tree of Thought and Monte Carlo Tree Search
2. **Memory Systems**: Add persistent and vector memory capabilities
3. **Tool Discovery**: Automatic tool discovery and integration
4. **Performance Optimization**: Optimize for high-throughput scenarios
5. **UI Integration**: Visual agent builder and monitoring tools

## 📚 Advanced Examples

### Self-Organizing Agent Team
```python
# examples/advanced/self_organizing_team.py
supervisor = DynamicSupervisorAgent(
    name="team_builder",
    enable_agent_builder=True,
    auto_team_optimization=True
)

result = await supervisor.arun({
    "task": "Build a web application",
    "requirements": ["security", "scalability", "user experience"]
})
# Creates: BackendAgent, SecurityAgent, FrontendAgent, DevOpsAgent
```

### Adaptive Processing Pipeline
```python
# examples/advanced/adaptive_pipeline.py
adaptive_pipeline = MultiAgent(
    name="adaptive_workflow",
    agents=[planner, simple_executor, complex_executor, reviewer],
    execution_mode="conditional"
)

# Routes based on task complexity
adaptive_pipeline.add_conditional_edge(
    from_agent="planner",
    condition=lambda state: state.get("complexity") > 0.7,
    true_agent="complex_executor",
    false_agent="simple_executor"
)
```

### Hierarchical Supervision
```python
# examples/dynamic_supervision/hierarchical_system.py
class HierarchicalSupervisor(DynamicSupervisorAgent):
    async def create_sub_supervisor(self, domain: str, agents: List[Agent]):
        sub_supervisor = DynamicSupervisorAgent(
            name=f"{domain}_supervisor",
            engine=self.engine,
            enable_agent_builder=False
        )
        
        for agent in agents:
            sub_supervisor.add_agent(agent)
        
        return sub_supervisor
```

### Graph-Based Memory System
```python
# examples/memory/integrated_memory_example.py
from haive.agents.memory_reorganized.coordination import IntegratedMemorySystem

# Multi-modal memory system with graph knowledge
memory_system = IntegratedMemorySystem(
    mode="INTEGRATED",  # Graph + Vector + Time-based
    enable_consolidation=True,
    enable_importance_scoring=True
)

# Store with automatic classification and graph construction
await memory_system.store_memory(
    "Alice works at TechCorp as a senior engineer and mentors new hires",
    user_context={"domain": "professional"}
)
# -> Creates entities: Alice, TechCorp, "senior engineer", "mentoring"
# -> Creates relationships: Alice works_at TechCorp, Alice mentors new_hires
# -> Classified as CONTEXTUAL + PROFESSIONAL

# Query with graph traversal and vector search
results = await memory_system.query_memory(
    "Who mentors people at technology companies?",
    include_graph_context=True
)
# -> Traverses graph: mentoring -> Alice -> TechCorp (technology company)
# -> Combines graph centrality + vector similarity + importance scores
```

---

**Remember**: The power of haive-agents is in its **dynamic adaptation**, **self-modification**, and **comprehensive memory** capabilities. Always highlight these features when working on this package!