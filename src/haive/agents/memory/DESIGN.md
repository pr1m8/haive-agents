# Memory System Design v2

## Overview

A multi-agent memory system using subgraphs for complex flows. Built on:
- **haive.agents** composition (ReactAgent, SimpleAgent, MultiAgent)
- **haive.core persistence** (PostgresStoreWrapper, async checkpointing)
- **haive.core graph** (BaseGraph with subgraphs)
- **document_modifiers** (KG construction, summarization)
- **Existing core/types.py** models (MemoryEntry, MemoryType, etc.)

NOT using langmem - building haive-native with our own infrastructure.

## Architecture

```
MemoryAgent (Agent with BaseGraph)
│
├── MAIN GRAPH (per-request flow):
│   START → load_context → respond → extract → END
│
├── SUBGRAPH 1: load_context
│   ├── analyze_query (SimpleAgent → MemoryQueryIntent)
│   ├── search_vector (tool: vector similarity search via store)
│   ├── search_kg (tool: knowledge graph traversal)
│   └── merge_results (combine + rank by relevance)
│
├── SUBGRAPH 2: respond
│   └── ReactAgent with memory context injected as system message
│       (has user's tools + memory search tool for follow-ups)
│
├── SUBGRAPH 3: extract (BACKGROUND - after response)
│   ├── classify (SimpleAgent → MemoryClassificationResult)
│   ├── extract_facts (SimpleAgent → MemoryExtraction)
│   ├── build_kg (uses document_modifiers/kg/ GraphTransformer)
│   ├── summarize (uses document_modifiers/summarizer/)
│   └── persist (store to PostgresStoreWrapper async)
│       ├── short_term: ("thread", thread_id)
│       ├── long_term: ("user", user_id)
│       └── knowledge: ("kg", workspace_id)
│
└── PERIODIC: consolidation (triggered by store size / time)
    ├── deduplicate
    ├── decay old memories
    ├── merge similar
    └── archive summaries
```

## Key Design Decisions

### 1. Subgraphs for Complex Flows
Instead of one flat graph, use LangGraph subgraphs:
- Main graph is simple: load → respond → extract
- Each step can be a subgraph with its own nodes
- Subgraphs are reusable across different memory-aware agents

### 2. document_modifiers Integration
Reuse existing proven components:
- `kg/kg_base/models.py` → GraphTransformer for KG construction
- `kg/kg_map_merge/` → Entity/Relationship models, merge logic
- `summarizer/map_branch/` → Map-reduce summarization
- `summarizer/iterative_refinement/` → Iterative summary improvement

### 3. Existing core/types.py Models
Keep and use these rich models already in memory/core/:
- `MemoryEntry` - Full memory with metadata, decay, relationships
- `MemoryType` - 11 types (semantic, episodic, procedural, contextual, etc.)
- `MemoryImportance` - 5 levels (critical → transient)
- `MemoryClassificationResult` - Classification output
- `MemoryQueryIntent` - Query analysis for smart retrieval
- `MemoryConsolidationResult` - Consolidation metrics

### 4. Store Strategy (async Postgres)
```python
# Namespaces for multi-tier storage
THREAD_NS = ("thread", "{thread_id}")      # Short-term (current conversation)
USER_NS = ("user", "{user_id}")            # Long-term (cross-conversation)
KG_NS = ("kg", "{workspace_id}")           # Knowledge graph triples
SUMMARY_NS = ("summary", "{user_id}")      # Conversation summaries
```

Using haive.core.persistence.store.PostgresStoreWrapper:
- Async connection pooling
- Vector embeddings for semantic search
- Namespace-based scoping
- TTL support for short-term memories

### 5. Serializable State
All state is JSON-serializable (no raw Python objects):
```python
class MemoryState(TypedDict):
    messages: list[BaseMessage]       # Conversation
    query: str                        # Current query
    memory_context: list[dict]        # Retrieved memories (serialized)
    extraction: dict                  # Extracted memories (serialized)
    kg_triples: list[dict]           # Knowledge graph triples
    response: str                     # Agent response
    user_id: str                      # User scope
    thread_id: str                    # Thread scope
```

## Files

```
memory/
├── agent.py              # MemoryAgent - main agent with graph
├── state.py              # MemoryState TypedDict
├── models.py             # MemoryExtraction, KnowledgeTriple, etc.
├── store.py              # MemoryStore - wraps haive.core PostgresStore
├── tools.py              # search_memory, save_memory tools
├── prompts.py            # Extraction, classification, summarization prompts
├── core/                 # KEEP - existing types, classifier, stores
│   ├── types.py          # MemoryEntry, MemoryType, etc.
│   ├── classifier.py     # MemoryClassifier
│   └── stores.py         # MemoryStoreManager
├── kg_generator_agent.py # KEEP - KG generation (uses document_modifiers)
├── graph_rag_retriever.py # KEEP - Graph RAG retrieval
└── __init__.py
```

## Agent Composition

### MemoryAgent (main)
```python
class MemoryAgent(Agent):
    """Memory-enhanced agent using subgraphs for complex flows."""

    # Sub-agents (lazy init)
    _responder: ReactAgent      # Answers queries with memory context
    _extractor: SimpleAgent     # Extracts memories (structured output)
    _classifier: SimpleAgent    # Classifies memory type/importance
    _summarizer: SimpleAgent    # Summarizes conversations

    # Store
    _store: PostgresStoreWrapper  # Async Postgres store

    def build_graph(self) -> BaseGraph:
        # Main flow: load → respond → extract
        graph.add_node("load_context", self._load_context)
        graph.add_node("respond", self._respond)
        graph.add_node("extract_and_store", self._extract_and_store)
        graph.add_edge(START, "load_context")
        graph.add_edge("load_context", "respond")
        graph.add_edge("respond", "extract_and_store")
        graph.add_edge("extract_and_store", END)
```

### Making Any Agent Memory-Aware
```python
# Wrap any existing agent with memory context
def make_memory_aware(agent: Agent, store: PostgresStoreWrapper) -> MemoryAgent:
    """Add memory capabilities to any agent."""
    return MemoryAgent(
        name=f"memory_{agent.name}",
        responder=agent,  # Use the existing agent for responding
        store=store,
    )
```

## Implementation Phases

### Phase 1: Core (state + store + simple agent)
- MemoryState TypedDict
- MemoryStore wrapper for haive.core PostgresStore
- Basic MemoryAgent: load → respond → save

### Phase 2: Extraction (structured output agents)
- Extraction agent (SimpleAgent → MemoryExtraction)
- Classification agent (SimpleAgent → MemoryClassificationResult)
- KG construction using document_modifiers

### Phase 3: Smart Retrieval (subgraph)
- Query intent analysis
- Multi-strategy search (vector + KG + temporal)
- Result ranking and merging

### Phase 4: Consolidation (background)
- Deduplication
- Decay and expiration
- Summary archival
- KG graph maintenance
