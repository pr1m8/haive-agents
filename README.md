# haive-agents

[![PyPI version](https://img.shields.io/pypi/v/haive-agents.svg)](https://pypi.org/project/haive-agents/)
[![Python Versions](https://img.shields.io/pypi/pyversions/haive-agents.svg)](https://pypi.org/project/haive-agents/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/pr1m8/haive-agents/actions/workflows/ci.yml/badge.svg)](https://github.com/pr1m8/haive-agents/actions/workflows/ci.yml)
[![Docs](https://github.com/pr1m8/haive-agents/actions/workflows/docs.yml/badge.svg)](https://pr1m8.github.io/haive-agents/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/haive-agents.svg)](https://pypi.org/project/haive-agents/)

**Production-ready agent implementations for the Haive framework** — SimpleAgent, ReactAgent, MultiAgent, MemoryAgent, RAG variants, and more.

53+ working agent implementations covering conversation, planning, reasoning, RAG, memory, research, and multi-agent coordination.

## Installation

```bash
pip install haive-agents
```

## Features

### 🤖 Foundation Agents
- **SimpleAgent** — conversation + structured output
- **ReactAgent** — reasoning loops with tool execution
- **MultiAgent** — sequential, parallel, and conditional composition
- **DynamicSupervisor** — runtime agent management with handoffs

### 🧠 Memory & Knowledge
- **MemoryAgent** — persistent memory + KG extraction + auto-summarize
- **LongTermMemoryAgent** — vector-store backed memory
- Neo4j integration with Cypher queries
- PostgreSQL store support

### 📚 RAG (22+ variants)
Adaptive, Agentic Router, Dynamic, FLARE, Fusion, HyDE, Self-Reflective, Self-Route, Speculative, Step-Back, Query Planning, Query Decomposition, Memory-Aware, GraphDB-RAG, SQL-RAG, and more.

### 🔬 Reasoning & Critique
- **Reflexion** — draft → reflect → revise loop
- **LATS** — language agent tree search with UCB1
- **Reflection** — generate + improve loop
- **Tree of Thoughts**, **Self-Discover**

### 📋 Planning
- **PlanAndExecuteAgent** — Planner → Executor → Replanner
- **LLMCompilerAgent** — DAG-based parallel task execution
- **ReWOOAgent** — Reasoning Without Observation

### 🔍 Research
- **ResearchAgent** — Perplexity-style 3-stage research
- **DeepResearchAgent** — 5-stage with shared findings store
- Tavily search + dynamic RAG tools

### 💬 Conversation
6 conversation patterns: Base, Collaborative, Debate, Directed, Round Robin, Social Media

## Quick Start

```python
from haive.agents.simple.agent import SimpleAgent
from haive.agents.react.agent import ReactAgent
from haive.agents.multi.agent import MultiAgent
from haive.agents.memory import create_memory_agent
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.tools import tool

# 1. Simple conversation agent
writer = SimpleAgent(
    name="writer",
    engine=AugLLMConfig(temperature=0.8, system_message="You are a writer."),
)

# 2. Tool-using agent
@tool
def search(query: str) -> str:
    """Search the web."""
    return f"Results for {query}"

researcher = ReactAgent(
    name="researcher",
    engine=AugLLMConfig(tools=[search], system_message="Use search tool."),
    max_iterations=3,
)

# 3. Compose them
pipeline = MultiAgent(
    name="research_pipeline",
    agents=[researcher, writer],
    execution_mode="sequential",
)
result = pipeline.run("Write about quantum computing")

# 4. Memory agent with KG extraction
memory = create_memory_agent(
    name="assistant",
    user_id="user123",
    connection_string="postgresql://haive:haive@localhost/haive",
)
memory.run("My name is Alice and I work at DeepMind on RL.")
memory.run("What do you know about me?")  # Recalls + queries KG
```

## Documentation

📖 **Full documentation:** https://pr1m8.github.io/haive-agents/

## Related Packages

| Package | Description |
|---------|-------------|
| [haive-core](https://pypi.org/project/haive-core/) | Foundation: engines, graphs, schemas |
| [haive-tools](https://pypi.org/project/haive-tools/) | Tool implementations |
| [haive-games](https://pypi.org/project/haive-games/) | LLM-powered game agents |
| [haive-mcp](https://pypi.org/project/haive-mcp/) | MCP integration |

## License

MIT © [pr1m8](https://github.com/pr1m8)
