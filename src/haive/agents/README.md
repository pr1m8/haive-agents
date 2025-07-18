# 🤖 Haive Agents

**Comprehensive collection of 80+ intelligent AI agents for every use case**

[![Documentation](https://img.shields.io/badge/docs-available-blue)](https://haive.readthedocs.io/en/latest/api/agents/index.html)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.12+-blue)](https://python.org)

## 🎯 Overview

The Haive Agents package provides the most comprehensive collection of pre-built AI agents, from simple conversational agents to advanced multi-agent systems with planning, reasoning, and memory capabilities.

### 🚀 Quick Start

```python
from haive.agents.simple import SimpleAgent
from haive.agents.react import ReactAgent
from haive.core.engine.aug_llm import AugLLMConfig

# Simple conversational agent
simple_agent = SimpleAgent(
    name="assistant",
    engine=AugLLMConfig(temperature=0.7)
)
result = simple_agent.run("Hello! How can I help you today?")

# ReAct agent with tools
from haive.tools.math import Calculator

react_agent = ReactAgent(
    name="calculator_agent",
    engine=AugLLMConfig(),
    tools=[Calculator()]
)
result = react_agent.run("What's 15 * 23 + 47?")
```

## 📋 Agent Categories

### 🔧 **Core Agents** - Foundation Building Blocks

Essential agents for basic AI interactions and tool usage.

| Agent                                           | Purpose                | Use Cases                     |
| ----------------------------------------------- | ---------------------- | ----------------------------- |
| **[SimpleAgent](simple/)**                      | Basic LLM interactions | Chat, Q&A, text generation    |
| **[ReactAgent](react/)**                        | Tool-enabled reasoning | Math, search, API calls       |
| **[StructuredOutputAgent](structured_output/)** | Type-safe outputs      | Data extraction, form filling |

```python
# Core agents examples
from haive.agents.simple import SimpleAgent
from haive.agents.react import ReactAgent

# Basic conversation
agent = SimpleAgent(name="chat")
response = agent.run("Explain quantum computing")

# Tool-enabled reasoning
react = ReactAgent(name="helper", tools=[web_search, calculator])
result = react.run("Find the current population of Tokyo and calculate growth rate")
```

### 🧠 **RAG Agents** - Knowledge-Powered Intelligence

**20+ specialized retrieval-augmented generation agents** for knowledge-intensive tasks.

#### 📚 Basic RAG

| Agent                             | Capability              | Best For               |
| --------------------------------- | ----------------------- | ---------------------- |
| **[SimpleRAGAgent](rag/simple/)** | Basic retrieve-generate | Document Q&A           |
| **[BaseRAGAgent](rag/base/)**     | Foundation RAG pattern  | Custom RAG development |

#### 🎯 Advanced RAG Strategies

| Agent                                              | Innovation                       | Use Cases               |
| -------------------------------------------------- | -------------------------------- | ----------------------- |
| **[AdaptiveRAGAgent](rag/adaptive_rag/)**          | Dynamic strategy selection       | Complex knowledge tasks |
| **[HyDERAGAgent](rag/hyde/)**                      | Hypothetical document generation | Open-ended research     |
| **[MultiStrategyRAGAgent](rag/multi_strategy/)**   | Multiple retrieval strategies    | Comprehensive analysis  |
| **[SelfReflectiveRAGAgent](rag/self_reflective/)** | Self-improving retrieval         | Learning from mistakes  |

#### 🔍 Specialized RAG

| Agent                                    | Specialization            | Domain              |
| ---------------------------------------- | ------------------------- | ------------------- |
| **[GraphDatabaseRAGAgent](rag/db_rag/)** | Knowledge graphs          | Connected data      |
| **[SQLRAGAgent](rag/db_rag/)**           | Database queries          | Structured data     |
| **[FLARERAGAgent](rag/flare/)**          | Forward-looking retrieval | Predictive analysis |

```python
# RAG agents examples
from haive.agents.rag.adaptive_rag import AdaptiveRAGAgent
from haive.agents.rag.hyde import HyDERAGAgent

# Adaptive RAG for complex queries
rag_agent = AdaptiveRAGAgent(
    name="research_assistant",
    retriever=your_retriever,
    strategy="adaptive"
)

# HyDE for hypothetical document generation
hyde_agent = HyDERAGAgent(
    name="hypothesis_researcher",
    retriever=your_retriever
)
result = hyde_agent.run("What are the implications of quantum internet?")
```

### 💬 **Conversation Agents** - Multi-Turn Interactions

Specialized agents for structured conversations and collaborative interactions.

| Agent                                                 | Pattern                  | Best For                      |
| ----------------------------------------------------- | ------------------------ | ----------------------------- |
| **[DebateAgent](conversation/debate/)**               | Structured argumentation | Decision making, analysis     |
| **[CollaborativeAgent](conversation/collaberative/)** | Team problem-solving     | Group projects, brainstorming |
| **[RoundRobinAgent](conversation/round_robin/)**      | Sequential participation | Workshops, panels             |
| **[SocialMediaAgent](conversation/social_media/)**    | Social content creation  | Marketing, engagement         |

```python
# Conversation agents examples
from haive.agents.conversation.debate import DebateAgent
from haive.agents.conversation.collaberative import CollaborativeAgent

# Structured debate
debate = DebateAgent(
    name="policy_debate",
    participants=["advocate", "critic", "moderator"]
)

# Collaborative problem solving
collab = CollaborativeAgent(
    name="team_brainstorm",
    collaboration_style="consensus"
)
```

### 🎯 **Planning & Reasoning** - Strategic Intelligence

Advanced agents with planning, reasoning, and strategic thinking capabilities.

#### 📋 Planning Agents

| Agent                                                 | Approach                      | Strengths              |
| ----------------------------------------------------- | ----------------------------- | ---------------------- |
| **[PlanAndExecuteAgent](planning/plan_and_execute/)** | Plan→Execute cycles           | Complex task breakdown |
| **[LLMCompilerAgent](planning/llm_compiler/)**        | Code-based planning           | Programming tasks      |
| **[ReWOOAgent](planning/rewoo/)**                     | Reasoning without observation | Efficient planning     |

#### 🧠 Reasoning Agents

| Agent                                                          | Method                   | Applications               |
| -------------------------------------------------------------- | ------------------------ | -------------------------- |
| **[TreeOfThoughtsAgent](reasoning_and_critique/tot/)**         | Branching exploration    | Creative problem solving   |
| **[SelfDiscoverAgent](reasoning_and_critique/self_discover/)** | Self-discovery reasoning | Learning new domains       |
| **[MCTSAgent](reasoning_and_critique/mcts/)**                  | Monte Carlo search       | Game playing, optimization |
| **[ReflectionAgent](reasoning_and_critique/reflection/)**      | Self-reflection          | Iterative improvement      |

```python
# Planning and reasoning examples
from haive.agents.planning.plan_and_execute import PlanAndExecuteAgent
from haive.agents.reasoning_and_critique.tot import TreeOfThoughtsAgent

# Strategic planning
planner = PlanAndExecuteAgent(
    name="project_planner",
    planning_depth=3
)

# Creative reasoning
tot_agent = TreeOfThoughtsAgent(
    name="creative_thinker",
    branching_factor=3,
    max_depth=5
)
```

### 🔬 **Research Agents** - Investigation & Discovery

Specialized agents for research, investigation, and knowledge discovery.

| Agent                                       | Focus               | Capabilities                       |
| ------------------------------------------- | ------------------- | ---------------------------------- |
| **[PersonResearchAgent](research/person/)** | Individual research | Background, expertise, connections |
| **[STORMAgent](research/storm/)**           | Structured research | Multi-perspective analysis         |
| **[ComponentDiscoveryAgent](discovery/)**   | System discovery    | Architecture analysis              |

```python
# Research agents examples
from haive.agents.research.person import PersonResearchAgent
from haive.agents.research.storm import STORMAgent

# Person research
researcher = PersonResearchAgent(
    name="background_checker",
    sources=["linkedin", "google", "academic"]
)

# Structured research methodology
storm = STORMAgent(
    name="topic_researcher",
    perspectives=["technical", "business", "social"]
)
```

### 📄 **Document Processing** - Content Intelligence

Agents specialized in document analysis, processing, and transformation.

#### 📁 Document Loaders

| Agent                                                  | Source Type      | Capabilities                  |
| ------------------------------------------------------ | ---------------- | ----------------------------- |
| **[FileLoaderAgent](document_loader/file/)**           | Local files      | PDF, Word, text processing    |
| **[WebLoaderAgent](document_loader/web/)**             | Web content      | Scraping, parsing, extraction |
| **[DirectoryLoaderAgent](document_loader/directory/)** | File collections | Batch processing              |

#### ✨ Document Processors

| Agent                                                                | Function              | Output               |
| -------------------------------------------------------------------- | --------------------- | -------------------- |
| **[SummarizerAgent](document_modifiers/summarizer/)**                | Content summarization | Structured summaries |
| **[ComplexExtractionAgent](document_modifiers/complex_extraction/)** | Data extraction       | Structured data      |
| **[KnowledgeGraphAgent](document_modifiers/kg/)**                    | Graph generation      | Connected knowledge  |

```python
# Document processing examples
from haive.agents.document_loader.file import FileLoaderAgent
from haive.agents.document_modifiers.summarizer import SummarizerAgent

# Load and process documents
loader = FileLoaderAgent(
    name="doc_loader",
    file_types=["pdf", "docx", "txt"]
)

# Summarize content
summarizer = SummarizerAgent(
    name="content_summarizer",
    summary_style="executive"
)
```

### 🤝 **Multi-Agent Systems** - Collaborative Intelligence

Orchestration and coordination of multiple agents working together.

| Agent                                     | Pattern              | Coordination        |
| ----------------------------------------- | -------------------- | ------------------- |
| **[MultiAgent](multi/)**                  | Core coordination    | Agent orchestration |
| **[SequentialAgent](multi/sequential/)**  | Sequential execution | Pipeline processing |
| **[DynamicSupervisorAgent](supervisor/)** | Dynamic management   | Adaptive routing    |

```python
# Multi-agent examples
from haive.agents.multi import MultiAgent
from haive.agents.multi.sequential import SequentialAgent

# Multi-agent coordination
multi_agent = MultiAgent(
    name="research_team",
    agents={
        "researcher": research_agent,
        "analyst": analysis_agent,
        "writer": writing_agent
    }
)

# Sequential pipeline
pipeline = SequentialAgent(
    name="content_pipeline",
    agents=[loader, processor, summarizer, writer]
)
```

### 🧠 **Memory & Learning** - Persistent Intelligence

Agents with long-term memory, learning capabilities, and knowledge management.

| Agent                                        | Memory Type          | Persistence     |
| -------------------------------------------- | -------------------- | --------------- |
| **[LongTermMemoryAgent](long_term_memory/)** | Episodic + semantic  | Vector stores   |
| **[MemoryAgent](memory/)**                   | Working memory       | Session-based   |
| **[KnowledgeGraphGeneratorAgent](memory/)**  | Structured knowledge | Graph databases |

```python
# Memory agents examples
from haive.agents.long_term_memory import LongTermMemoryAgent
from haive.agents.memory import MemoryAgent

# Long-term memory
ltm_agent = LongTermMemoryAgent(
    name="learning_assistant",
    memory_store=vector_store,
    retention_strategy="importance"
)

# Working memory
memory_agent = MemoryAgent(
    name="context_aware",
    memory_window=10
)
```

### 🛠️ **Specialized Agents** - Domain Experts

Purpose-built agents for specific domains and use cases.

| Agent                                          | Domain               | Specialization            |
| ---------------------------------------------- | -------------------- | ------------------------- |
| **[TaskAnalysisAgent](task_analysis/)**        | Task management      | Decomposition, planning   |
| **[SelfHealingCodeAgent](self_healing_code/)** | Software engineering | Code repair, optimization |
| **[WikiWriterAgent](wiki_writer/)**            | Content creation     | Wikipedia-style articles  |

```python
# Specialized agents examples
from haive.agents.task_analysis import TaskAnalysisAgent
from haive.agents.self_healing_code import SelfHealingCodeAgent

# Task breakdown
task_agent = TaskAnalysisAgent(
    name="project_analyzer",
    decomposition_strategy="hierarchical"
)

# Code improvement
code_agent = SelfHealingCodeAgent(
    name="code_doctor",
    languages=["python", "javascript"]
)
```

## 🏗️ Agent Architecture

### Base Classes

All agents inherit from a robust foundation:

```python
from haive.agents.base import Agent, GenericAgent
from haive.core.engine.aug_llm import AugLLMConfig

# Generic type-safe agent
class CustomAgent(GenericAgent[InputType, OutputType, StateType]):
    def __init__(self, name: str, engine: AugLLMConfig):
        super().__init__(name=name, engine=engine)
```

### Mixins & Extensions

Agents support modular capabilities through mixins:

- **ExecutionMixin**: Async execution patterns
- **PersistenceMixin**: State persistence
- **HooksMixin**: Lifecycle hooks
- **StateMixin**: State management

## 📖 Documentation Structure

### Quick References

- **[Agent Showcase](../../../docs/source/agents/index.rst)** - Visual agent gallery
- **[API Reference](../../../docs/source/api/agents/index.rst)** - Complete API docs
- **[Examples Gallery](examples/)** - Code examples for each agent

### Deep Dives

- **[RAG Agents Guide](rag/README.md)** - Comprehensive RAG documentation
- **[Multi-Agent Patterns](multi/README.md)** - Coordination strategies
- **[Planning Agents](planning/README.md)** - Strategic reasoning patterns

## 🚀 Getting Started

### 1. Choose Your Agent Type

```python
# For basic chat/Q&A
from haive.agents.simple import SimpleAgent

# For tool-enabled tasks
from haive.agents.react import ReactAgent

# For knowledge-intensive work
from haive.agents.rag.adaptive_rag import AdaptiveRAGAgent

# For complex reasoning
from haive.agents.planning.plan_and_execute import PlanAndExecuteAgent
```

### 2. Configure Your Engine

```python
from haive.core.engine.aug_llm import AugLLMConfig

# Basic configuration
config = AugLLMConfig(
    temperature=0.7,
    max_tokens=1000
)

# Advanced configuration
config = AugLLMConfig(
    temperature=0.1,  # Low for consistency
    max_tokens=2000,
    system_message="You are an expert research assistant."
)
```

### 3. Run Your Agent

```python
# Simple execution
agent = SimpleAgent(name="assistant", engine=config)
result = agent.run("Your query here")

# Async execution
result = await agent.arun("Your query here")

# With structured output
from pydantic import BaseModel

class Response(BaseModel):
    answer: str
    confidence: float

result = agent.run("Query", structured_output_model=Response)
```

## 🔧 Advanced Usage

### Custom Agent Development

```python
from haive.agents.base import Agent
from haive.core.engine.aug_llm import AugLLMConfig

class CustomAgent(Agent):
    def __init__(self, name: str, engine: AugLLMConfig, custom_param: str):
        super().__init__(name=name, engine=engine)
        self.custom_param = custom_param

    def process(self, input_data: str) -> str:
        # Custom processing logic
        enhanced_input = f"{self.custom_param}: {input_data}"
        return self.engine.invoke(enhanced_input)
```

### Agent Composition

```python
# Combine multiple agents
from haive.agents.multi import MultiAgent

research_team = MultiAgent(
    name="research_team",
    agents={
        "researcher": PersonResearchAgent(...),
        "analyst": SummarizerAgent(...),
        "writer": WikiWriterAgent(...)
    },
    coordination_strategy="sequential"
)

result = research_team.run("Research topic: Quantum Computing")
```

## 📊 Performance & Monitoring

### Built-in Metrics

All agents support performance monitoring:

```python
agent = SimpleAgent(name="monitored", engine=config)
result = agent.run("Test query", enable_metrics=True)

print(f"Execution time: {result.metrics.execution_time}")
print(f"Token usage: {result.metrics.token_count}")
print(f"Cost: ${result.metrics.estimated_cost}")
```

### State Persistence

Agents automatically save state for resumption:

```python
agent = ReactAgent(name="persistent", engine=config)
agent.run("Start complex task...")

# Later - agent resumes from saved state
agent = ReactAgent(name="persistent", engine=config)
agent.run("Continue task...")  # Remembers previous context
```

## 🤝 Contributing

We welcome contributions! Each agent directory contains:

- **README.md** - Agent-specific documentation
- **agent.py** - Main implementation
- **config.py** - Configuration schemas
- **state.py** - State management
- **examples/** - Usage examples

### Adding New Agents

1. Create agent directory under appropriate category
2. Implement core agent class extending base
3. Add configuration and state schemas
4. Write comprehensive README and examples
5. Add to this index

## 📚 See Also

- **[Haive Core](../../../core/)** - Foundation framework
- **[Haive Tools](../../../tools/)** - Agent tools and utilities
- **[Haive Games](../../../games/)** - Game-playing agents
- **[API Documentation](https://haive.readthedocs.io)** - Complete reference

---

_🤖 **80+ AI agents ready to power your applications** - From simple chat to complex multi-agent systems, Haive Agents provides the building blocks for intelligent automation._
