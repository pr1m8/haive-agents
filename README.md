# haive-agents

[![PyPI version](https://img.shields.io/pypi/v/haive-agents.svg)](https://pypi.org/project/haive-agents/)
[![Python Versions](https://img.shields.io/pypi/pyversions/haive-agents.svg)](https://pypi.org/project/haive-agents/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/pr1m8/haive-agents/actions/workflows/ci.yml/badge.svg)](https://github.com/pr1m8/haive-agents/actions/workflows/ci.yml)
[![Docs](https://github.com/pr1m8/haive-agents/actions/workflows/docs.yml/badge.svg)](https://pr1m8.github.io/haive-agents/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/haive-agents.svg)](https://pypi.org/project/haive-agents/)

**Production-ready agent implementations for the Haive framework.**

53+ working agent implementations covering conversation, planning, reasoning, RAG, memory, research, and multi-agent coordination — built on `haive-core` and ready for production. Every agent is verified end-to-end with real LLM calls (no mocks).

---

## Why haive-agents?

Building production agents from scratch on LangGraph is hard. You need to:

- Roll your own state schemas with the right fields for tool execution
- Implement reasoning loops with iteration tracking and convergence checks
- Handle structured output validation, tool routing, and error recovery
- Wire up memory, persistence, and KG extraction
- Compose agents into pipelines without losing type safety

`haive-agents` gives you all of this as a library. Each agent is a `pydantic.BaseModel` you can configure, compose, and extend. Agents follow a consistent pattern: configure with `AugLLMConfig`, run with `agent.run(input)`, get back structured output.

---

## Foundation Agents

### SimpleAgent — Conversation + Structured Output

The base agent. Single LLM call, optional structured output, no tools. Use this for chatbots, formatters, classifiers, and any task that doesn't need tool execution.

```python
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig

writer = SimpleAgent(
    name="writer",
    engine=AugLLMConfig(
        temperature=0.8,
        system_message="You are a creative writer.",
    ),
)

result = writer.run("Write a haiku about quantum computing.")
print(result.messages[-1].content)
```

**Graph:** `START → agent_node → END`

**Use cases:** Conversational chatbots, structured data extraction, content generation, classification, summarization.

### ReactAgent — Reasoning Loops with Tools

Implements the ReAct pattern: reason → act → observe → repeat. The agent decides which tools to call, sees the results, and continues reasoning until it has an answer or hits the iteration limit.

```python
from haive.agents.react.agent import ReactAgent
from langchain_core.tools import tool

@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    return str(eval(expression, {"__builtins__": {}}))

@tool
def web_search(query: str) -> str:
    """Search the web."""
    return f"Results for: {query}"

researcher = ReactAgent(
    name="researcher",
    engine=AugLLMConfig(
        tools=[calculator, web_search],
        system_message="Use tools to answer questions. Reason step by step.",
    ),
    max_iterations=5,
)

result = researcher.run("What is the population density of Tokyo?")
```

**Graph:** `START → agent_node → [tool_calls?] → tool_node → agent_node → ... → END`

**Use cases:** Research, math, web scraping, multi-step problem solving, anything that needs tools.

### MultiAgent — Compose Agents

Compose multiple agents into pipelines: sequential, parallel, or conditional. Each child agent can be a different type (Simple, React, Memory, etc.). Engines are passed through automatically so child tools work.

```python
from haive.agents.multi.agent import MultiAgent

# Sequential: each agent sees output of previous
pipeline = MultiAgent(
    name="research_pipeline",
    agents=[researcher, analyzer, writer],
    execution_mode="sequential",
)

# Parallel: all run concurrently, results merged
parallel = MultiAgent(
    name="multi_perspective",
    agents=[technical_analyst, business_analyst, security_analyst],
    execution_mode="parallel",
)

# Conditional: route based on state
router = MultiAgent(
    name="router",
    agents=[classifier, simple_handler, complex_handler],
    execution_mode="conditional",
)
```

**Use cases:** Research pipelines, multi-perspective analysis, content workflows, fan-out/fan-in patterns.

### DynamicSupervisor — Runtime Agent Management

A `ReactAgent` with handoff tools that can dynamically delegate to other agents. Add agents at runtime, remove them, or create new ones from system messages.

```python
from haive.agents.dynamic_supervisor.agent import DynamicSupervisor

supervisor = DynamicSupervisor(
    name="team_lead",
    engine=AugLLMConfig(system_message="You coordinate a team."),
)

# Add agents at any time
supervisor.add_agent(math_agent, description="Handles math problems")
supervisor.add_agent(writer_agent, description="Writes content")

# Or create one on the fly
supervisor.create_agent(
    name="translator",
    system_message="You translate between languages.",
    description="Handles translation tasks",
)

# Supervisor decides who handles each request
result = supervisor.run("Translate 'hello world' to French")
```

**Use cases:** Customer service routing, dynamic task delegation, agent marketplaces, runtime adaptation.

---

## MemoryAgent — Persistent Memory + Knowledge Graphs

The most sophisticated agent in the framework. A `ReactAgent` extended with:

1. **Persistent memory** — saves facts about users in a store (PostgreSQL or in-memory)
2. **Auto-context loading** — searches memory before each response, injects relevant facts
3. **KG extraction** — automatically extracts subject-predicate-object triples from conversations
4. **Auto-summarization** — summarizes long conversations to manage context length
5. **Neo4j integration** — optional graph database for Cypher queries on the KG

```python
from haive.agents.memory import create_memory_agent

# Dev mode (in-memory)
agent = create_memory_agent(name="assistant", user_id="alice")

# Production (PostgreSQL with pgvector)
agent = create_memory_agent(
    name="assistant",
    user_id="alice",
    connection_string="postgresql://haive:haive@localhost/haive",
)

# With Neo4j knowledge graph
agent = create_memory_agent(
    name="assistant",
    user_id="alice",
    connection_string="postgresql://haive:haive@localhost/haive",
    neo4j_config=True,  # Uses NEO4J_URI/USER/PASSWORD env vars
)

# Have a conversation — agent remembers and extracts KG
agent.run("My name is Alice. I work at DeepMind on reinforcement learning.")
# → Saves memory: "Alice works at DeepMind"
# → Extracts triples: (Alice)-[works_at]->(DeepMind), (Alice)-[focuses_on]->(RL)
# → Stores in PostgreSQL + syncs to Neo4j

agent.run("I also use PyTorch and JAX.")
# → Saves memory + new triples

agent.run("What do you know about me?")
# → Pre-hook: searches memories + KG triples + summaries
# → Injects context into system message
# → LLM responds with full recall
```

**Memory tools available to the LLM:**
- `save_memory(content, importance)` — save a fact
- `search_memory(query)` — search past memories
- `save_knowledge(subject, predicate, object_)` — save a KG triple
- `search_knowledge(query)` — search KG triples
- `query_knowledge_graph(question)` — Cypher query (when Neo4j connected)

**Document-level KG extraction:**

```python
# Extract KG from a document using GraphTransformer
triples = agent.extract_kg_from_document(
    "Marie Curie was born in Warsaw, Poland in 1867. She won two Nobel prizes.",
    allowed_nodes=["Person", "Location", "Award"],
)
# → [{subject: "Marie Curie", predicate: "born_in", object: "Warsaw"}, ...]
```

**Use cases:** Personal assistants, customer support with history, research assistants, anything that needs long-term memory.

---

## RAG Agents — 22+ Variants

Every meaningful RAG variant from the literature, implemented and ready to use:

| Agent | Pattern | Best For |
|-------|---------|----------|
| **BaseRAGAgent** | Simple retrieve → generate | Baseline RAG |
| **AdaptiveRAGAgent** | Routes by query complexity | Mixed query types |
| **AgenticRAGAgent** | ReactAgent with retrieval tools | Multi-step research |
| **DynamicRAGAgent** | Multi-source dynamic retrieval | Varied data sources |
| **FLARERAGAgent** | Forward-Looking Active REtrieval | Long-form generation |
| **RAGFusionAgent** | Reciprocal rank fusion | Better recall |
| **HyDERAGAgent** | Hypothetical document embeddings | Better semantic search |
| **SelfReflectiveRAGAgent** | Generate → grade → regenerate | Hallucination control |
| **SelfRouteRAGAgent** | Query-aware route selection | Mixed strategies |
| **SpeculativeRAGAgent** | Hypothesis + parallel verification | Speed + accuracy |
| **StepBackRAGAgent** | Abstract query → retrieve → answer | Complex reasoning |
| **QueryPlanningRAGAgent** | Query planning + multi-hop | Hierarchical questions |
| **QueryDecomposerAgent** | Decompose into sub-queries | Compound questions |
| **MemoryAwareRAGAgent** | RAG + memory context | Personalized RAG |
| **GraphDBRAGAgent** | NL → Cypher → Neo4j | Graph-based knowledge |
| **SQLRAGAgent** | NL → SQL → database | Structured data |

```python
from haive.agents.rag.adaptive.agent import AdaptiveRAGAgent
from langchain_core.documents import Document

docs = [Document(page_content="...") for _ in range(100)]

agent = AdaptiveRAGAgent.from_documents(
    documents=docs,
    llm_config=AugLLMConfig(),
    max_query_complexity="complex",
)

result = agent.run("What are the key insights from the documents?")
```

---

## Reasoning & Critique Agents

Implementations of recent reasoning paper algorithms:

### Reflexion — Draft → Reflect → Revise

```python
from haive.agents.reasoning_and_critique.reflexion.agent import ReflexionAgent

agent = ReflexionAgent(
    name="reflexive",
    engine=AugLLMConfig(),
    max_revisions=3,
)
result = agent.run("Solve this complex problem...")
# → Draft → Reflect on draft → Revise → Loop until quality threshold
```

### LATS — Language Agent Tree Search

Tree search with UCB1 selection, simulation, backprop, and reflection-based scoring.

```python
from haive.agents.reasoning_and_critique.lats.agent import LATSAgent

agent = LATSAgent(
    name="lats",
    engine=AugLLMConfig(tools=[search]),
    max_depth=4,
    n_samples=3,
)
```

Other reasoning agents: `ReflectionAgent`, `LogicReasoningAgent`, `ToTAgent` (Tree of Thoughts), `SelfDiscoverAgent`.

---

## Planning Agents

### PlanAndExecuteAgent — Planner → Executor → Replanner

```python
from haive.agents.planning.plan_and_execute import PlanAndExecuteAgent

agent = PlanAndExecuteAgent.create(
    tools=[calculator, web_search],
    name="planner",
)
result = agent.run("Research AI safety and write a 3-paragraph summary.")
```

### LLMCompilerAgent — DAG-based Parallel Execution

Plans tasks as a DAG, executes independent tasks in parallel, joins results, replans if needed.

```python
from haive.agents.planning.llm_compiler.agent import LLMCompilerAgent

agent = LLMCompilerAgent(
    name="dag_executor",
    engine=AugLLMConfig(tools=[search, calc]),
)
```

### ReWOO — Reasoning Without Observation

Plans all steps upfront, executes them all, then synthesizes. Only 2 LLM calls for the planning + synthesis (intermediate steps don't require LLM reasoning).

```python
from haive.agents.planning.rewoo.agent import ReWOOAgent

agent = ReWOOAgent(name="rewoo", engine=AugLLMConfig(tools=[...]))
```

---

## Research Agents

### ResearchAgent — Perplexity-Style 3-Stage

`QueryAnalyzer → Researcher (search + RAG) → Synthesizer`

```python
from haive.agents.research import create_research_agent

agent = create_research_agent(
    name="research",
    max_search_iterations=8,
    # Tavily auto-detected if TAVILY_API_KEY set, else mock
)
result = agent.run("What are the latest advances in quantum computing?")
```

### DeepResearchAgent — 5-Stage Pipeline

`Planner → Researcher → Analyzer → FactChecker → Writer`

Shared `ResearchStore` across agents so the analyzer can retrieve what the researcher found.

```python
from haive.agents.research import create_deep_research_agent

agent = create_deep_research_agent(
    name="deep",
    include_fact_check=True,
    max_search_iterations=10,
)
result = agent.run("Compare React vs Vue.js for 2025 web development")
```

---

## Conversation Agents

Six conversation patterns:

| Agent | Description |
|-------|-------------|
| **BaseConversationAgent** | Foundation for all conversation types |
| **CollaborativeConversation** | Agents collaborate on a goal |
| **DebateConversation** | Structured debate with positions |
| **DirectedConversation** | Moderator-directed flow |
| **RoundRobinConversation** | Sequential turn-taking |
| **SocialMediaConversation** | Social media simulation with personalities |

```python
from haive.agents.conversation.debate.agent import DebateConversation

debate = DebateConversation(
    name="ai_safety_debate",
    engine=AugLLMConfig(),
    topic="Should AI development be paused?",
    n_rounds=3,
)
result = debate.run("Begin debate")
```

---

## Trace Utility — Pretty-Print Any Agent

Strip the noisy LangGraph debug output and see clean agent execution:

```python
from haive.agents.utils.trace import run_traced

result = run_traced(agent, "Tell me about quantum computing", save_to="traces/")
# → Rich-formatted tree showing user message, AI response, tool calls,
#   tool results, timing, token usage, store contents
```

---

## Installation

```bash
pip install haive-agents
```

For specific extras:

```bash
pip install haive-agents[memory]    # MemoryAgent + Neo4j support
pip install haive-agents[rag]       # RAG dependencies
pip install haive-agents[research]  # Tavily + research deps
```

---

## Quick Start

```python
from haive.agents.simple.agent import SimpleAgent
from haive.agents.react.agent import ReactAgent
from haive.agents.multi.agent import MultiAgent
from haive.agents.memory import create_memory_agent
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.tools import tool

# 1. Simple LLM agent
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

# 3. Compose into pipeline
pipeline = MultiAgent(
    name="research_pipeline",
    agents=[researcher, writer],
    execution_mode="sequential",
)
result = pipeline.run("Write an article about quantum computing")

# 4. Add persistent memory
memory_agent = create_memory_agent(
    name="assistant",
    user_id="user123",
    connection_string="postgresql://haive:haive@localhost/haive",
)
memory_agent.run("My name is Alice and I work at DeepMind on RL.")
memory_agent.run("What do you know about me?")  # Recalls everything
```

---

## Documentation

📖 **Full documentation:** https://pr1m8.github.io/haive-agents/

---

## Related Packages

| Package | Description |
|---------|-------------|
| [haive-core](https://pypi.org/project/haive-core/) | Foundation: engines, graphs, schemas |
| [haive-tools](https://pypi.org/project/haive-tools/) | Tool implementations |
| [haive-games](https://pypi.org/project/haive-games/) | LLM-powered game agents |
| [haive-mcp](https://pypi.org/project/haive-mcp/) | Dynamic MCP integration |

---

## License

MIT © [pr1m8](https://github.com/pr1m8)
