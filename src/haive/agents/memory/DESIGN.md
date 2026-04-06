# Memory System Design

## Architecture

The memory system is a **graph of haive agents**, NOT a custom LLM pipeline.
Each memory operation is a composable agent using our proven patterns.

### Agents

1. **TriageAgent** (ReactAgent) - Classifies incoming data, decides what to remember
2. **ExtractionAgent** (SimpleAgent + structured output) - Extracts memories, KG triples, preferences
3. **KGBuilder** (SimpleAgent + structured output) - Consolidates knowledge graph
4. **SummarizerAgent** (SimpleAgent) - Summarizes conversations for archival
5. **RetrievalAgent** (ReactAgent + search tools) - Finds relevant memories

### Graph Flow

```
User Query
    ↓
load_memories (search store for context)
    ↓
respond (ReactAgent answers with memory context)
    ↓
extract_memories (SimpleAgent extracts what to remember)
    ↓
build_kg (SimpleAgent extracts knowledge triples)
    ↓
store_memories (persist to PostgresStore async)
    ↓
Response
```

### Memory Tiers

1. **SHORT_TERM** - Thread-scoped, current conversation (namespace: `("thread", thread_id)`)
2. **LONG_TERM** - User-scoped, cross-conversation (namespace: `("user", user_id)`)
3. **KNOWLEDGE** - Workspace-shared facts, KG (namespace: `("knowledge", workspace_id)`)

### Storage

- **haive.core.persistence.store.PostgresStoreWrapper** - Primary store (async)
- Vector search via store embeddings
- KG stored as triples in store items with graph metadata
- Full checkpointing via PostgresCheckpointerConfig (async)

### Key Models

- `MemoryExtraction` - What the extraction agent outputs (summary, facts, triples, type, importance)
- `KnowledgeTriple` - Subject-predicate-object with confidence
- `MemoryItem` - Stored memory with namespace scoping
- `ConversationSummary` - Archived conversation summary
- `MemorySearchResult` - Search result with score

### Improvements Over Langmem

1. **Async Postgres** - Not generic BaseStore, proper connection pooling
2. **KG Construction** - Native knowledge graph support via triples
3. **Agent Composition** - Uses ReactAgent/SimpleAgent, not custom TrustCall
4. **Serializable State** - Everything in state is JSON-serializable
5. **Multi-tier** - Thread/user/workspace scoping
6. **Checkpointing** - Full state recovery via haive-core persistence

### File Structure

```
memory/
├── agent.py          # MemoryAgent (main agent with graph)
├── models.py         # Pydantic models (extraction, triples, items)
├── state.py          # MemoryState (serializable TypedDict)
├── store.py          # Store interface (wraps haive.core PostgresStore)
├── tools.py          # Memory tools (save, search, summarize)
├── prompts.py        # Extraction/summarization prompts
└── __init__.py
```
