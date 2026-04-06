# Memory System Design v3

## Principle: Start Simple, Layer Up

### Phase 1: Base Memory Agent (NOW)

A **ReactAgent** with memory tools and automatic conversation summarization.

```
MemoryAgent (ReactAgent)
├── Tools:
│   ├── save_memory(content) → store to Postgres
│   ├── search_memory(query) → vector search from Postgres
│   └── save_knowledge(subject, predicate, object) → KG triple
│
├── Auto-summarize: when token count > threshold
│   ├── Summarize conversation so far (SimpleAgent)
│   ├── Store summary to ("summary", user_id) namespace
│   └── Trim messages to keep context window manageable
│
├── Store: haive.core PostgresStoreWrapper (async)
│   ├── ("user", user_id) → user memories
│   ├── ("kg", user_id) → knowledge triples
│   └── ("summary", user_id) → conversation summaries
│
└── On each turn:
    1. Search store for relevant memories (auto, before LLM)
    2. Inject memories into system message
    3. ReactAgent responds (may call save_memory tool)
    4. Check token count → summarize if over threshold
```

**Files:**
```
memory/
├── agent.py       # MemoryAgent extends ReactAgent
├── models.py      # MemoryItem, KnowledgeTriple, ConversationSummary
├── state.py       # MemoryState (serializable)
├── store.py       # MemoryStore wraps haive.core PostgresStore
├── tools.py       # save_memory, search_memory, save_knowledge tools
└── __init__.py
```

**This gives us:**
- Working memory agent with real persistence (Postgres async)
- Auto-summarization to manage context window
- KG triple storage
- Vector search for recall
- Token counting + conditional summarization

### Phase 2: Extraction Pipeline (LATER)
- Add structured extraction (SimpleAgent → MemoryExtraction)
- Auto-classify memories (MemoryClassificationResult)
- Build KG from conversations (document_modifiers/kg/)

### Phase 3: Smart Retrieval (LATER)
- Query intent analysis
- Multi-strategy search (vector + KG + temporal)
- Result ranking

### Phase 4: Consolidation (LATER)
- Deduplication
- Decay and expiration
- Summary archival

## Phase 1 Implementation Detail

### MemoryAgent Graph

```python
class MemoryAgent(ReactAgent):
    """ReactAgent with persistent memory + auto-summarization."""

    # Config
    store_config: PostgresStoreConfig  # or connection string
    user_id: str
    summarize_threshold: int = 4000  # tokens before auto-summarize

    # Tools (built in model_post_init)
    # - save_memory, search_memory, save_knowledge

    # Graph: same as ReactAgent but with:
    # - Pre-step: search store, inject context
    # - Post-step: check tokens, maybe summarize
```

### Auto-Summarize Flow

```
after each response:
    if count_tokens(messages) > threshold:
        summary = summarizer.run(messages)
        store.put(("summary", user_id), summary)
        messages = [system_msg, summary_msg, last_2_messages]
```

### Store Operations

```python
# Save memory
store.put(("user", user_id), key=uuid, value={"content": "...", "type": "semantic"})

# Search memories
results = store.search(("user", user_id), query="what does user like?", limit=5)

# Save KG triple
store.put(("kg", user_id), key=f"{subj}_{pred}_{obj}", value=triple_dict)

# Get summaries
summaries = store.search(("summary", user_id), query="recent", limit=3)
```
