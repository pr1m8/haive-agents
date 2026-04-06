"""Memory Agent - ReactAgent with persistent memory, KG extraction, and auto-summarization.

Phase 1: Memory tools (save/search/KG) + auto-context + auto-summarize
Phase 2: KG extraction from conversations + context-length pre-hook
         Optional integration with document_modifiers (summarizer, KG extraction)

Uses haive.core store for persistence, NOT langmem.
Supports InMemoryStore (dev) and PostgresStore (production).
"""

import logging
import uuid
from typing import Any

from langchain_core.messages import AIMessage, HumanMessage
from pydantic import BaseModel, ConfigDict, Field, PrivateAttr

from haive.agents.react.agent import ReactAgent
from haive.core.engine.aug_llm import AugLLMConfig

from .tools import create_memory_tools

logger = logging.getLogger(__name__)

MEMORY_SYSTEM_PROMPT = """You are a helpful assistant with long-term memory.

You have access to memory tools:
- save_memory: Save important facts about the user for future conversations
- search_memory: Search for relevant memories from past conversations
- save_knowledge: Save structured facts (subject-predicate-object triples)
- search_knowledge: Search knowledge graph triples for structured facts

Guidelines:
- Proactively save information when you learn something about the user
- Search memories when the user references past conversations or preferences
- Use save_knowledge for structured facts (who works where, what relates to what)
- Use save_memory for broader context and preferences

{memory_context}"""


# ---- Structured output models for extraction ----

class ExtractedTriple(BaseModel):
    """A single knowledge graph triple extracted from conversation."""
    subject: str = Field(description="The entity or concept")
    predicate: str = Field(description="The relationship or property")
    object: str = Field(description="The target entity or value")


class ConversationExtraction(BaseModel):
    """Structured extraction from a conversation turn."""
    summary: str = Field(description="One-sentence summary of this exchange")
    key_facts: list[str] = Field(default_factory=list, description="Important facts to remember")
    triples: list[ExtractedTriple] = Field(default_factory=list, description="Knowledge graph triples")
    should_save: bool = Field(default=True, description="Whether this contains info worth saving")


# ---- Store helpers ----

def _create_postgres_store(connection_string: str) -> Any:
    """Create a PostgresStore from a connection string."""
    try:
        from haive.core.persistence.store.factory import StoreFactory
        from haive.core.persistence.store.types import StoreConfig, StoreType

        config = StoreConfig(
            type=StoreType.POSTGRES_SYNC,
            connection_params={"connection_string": connection_string},
            setup_on_init=True,
        )
        store = StoreFactory.create(config)
        logger.info("MemoryAgent: using PostgresStore via haive.core")
        return store
    except ImportError:
        logger.warning("haive.core persistence not available, trying langgraph directly")

    try:
        from langgraph.store.postgres import PostgresStore
        store = PostgresStore(conn_string=connection_string)
        store.setup()
        logger.info("MemoryAgent: using langgraph PostgresStore directly")
        return store
    except ImportError:
        raise ImportError(
            "PostgreSQL store requires 'langgraph-checkpoint-postgres'. "
            "Install with: pip install langgraph-checkpoint-postgres"
        )


def _resolve_store(store: Any = None, connection_string: str | None = None) -> Any:
    """Resolve store from explicit store, connection string, or default InMemory."""
    if store is not None:
        return store
    if connection_string:
        return _create_postgres_store(connection_string)
    from langgraph.store.memory import InMemoryStore
    logger.info("MemoryAgent: using InMemoryStore (set store= or connection_string= for production)")
    return InMemoryStore()


# ---- MemoryAgent ----

class MemoryAgent(ReactAgent):
    """ReactAgent with persistent memory, KG extraction, and auto-summarization.

    Features:
    1. Memory tools bound to a store (save/search memories + KG triples)
    2. Auto-context: searches store for relevant memories before each response
    3. Auto-summarize: when context length exceeds threshold, summarize and store
    4. KG extraction: extracts knowledge triples from conversations (post-response)
    5. Integration points for document_modifiers (summarizer, KG pipelines)

    Store options:
    - Pass store= directly (any LangGraph BaseStore)
    - Pass connection_string= for PostgreSQL (preferred for production)
    - Default: InMemoryStore (dev only)
    """

    # ---- Config ----
    user_id: str = Field(default="default", description="User ID for memory scoping")
    summarize_threshold: int = Field(default=4000, description="Token count before auto-summarize")
    auto_context: bool = Field(default=True, description="Auto-search store for context before responding")
    auto_save: bool = Field(default=True, description="Auto-save conversation summaries")
    auto_extract_kg: bool = Field(default=True, description="Auto-extract KG triples from conversations")

    # ---- Store (runtime, not serialized) ----
    _store: Any = PrivateAttr(default=None)
    _summarizer: Any = PrivateAttr(default=None)
    _extractor: Any = PrivateAttr(default=None)

    model_config = ConfigDict(arbitrary_types_allowed=True)

    # ---- Memory context loading (pre-hook) ----

    def _load_memory_context(self, query: str) -> str:
        """Search store for relevant memories and KG triples, format as context."""
        if not self.auto_context or not self._store:
            return ""

        context_parts = []

        # Search user memories
        try:
            user_ns = ("user", self.user_id)
            results = self._store.search(user_ns, query=query, limit=5)
            if results:
                memories = []
                for item in results:
                    val = item.value if hasattr(item, "value") else item
                    content = val.get("content", str(val)) if isinstance(val, dict) else str(val)
                    memories.append(f"- {content}")
                if memories:
                    context_parts.append("Memories:\n" + "\n".join(memories))
        except Exception as e:
            logger.warning(f"Failed to load memories: {e}")

        # Search KG triples
        try:
            kg_ns = ("kg", self.user_id)
            kg_results = self._store.search(kg_ns, query=query, limit=5)
            if kg_results:
                triples = []
                for item in kg_results:
                    val = item.value if hasattr(item, "value") else item
                    if isinstance(val, dict) and val.get("type") == "kg_triple":
                        triples.append(f"- {val['subject']} {val['predicate']} {val['object']}")
                if triples:
                    context_parts.append("Known facts:\n" + "\n".join(triples))
        except Exception as e:
            logger.warning(f"Failed to load KG triples: {e}")

        # Search summaries
        try:
            summary_ns = ("summary", self.user_id)
            sum_results = self._store.search(summary_ns, query=query, limit=2)
            if sum_results:
                summaries = []
                for item in sum_results:
                    val = item.value if hasattr(item, "value") else item
                    content = val.get("content", str(val)) if isinstance(val, dict) else str(val)
                    summaries.append(f"- {content}")
                if summaries:
                    context_parts.append("Previous conversation summaries:\n" + "\n".join(summaries))
        except Exception as e:
            logger.warning(f"Failed to load summaries: {e}")

        if context_parts:
            return "Relevant context from past conversations:\n\n" + "\n\n".join(context_parts)
        return ""

    # ---- Token counting ----

    def _count_tokens(self, messages: list) -> int:
        """Approximate token count from messages."""
        total = 0
        for msg in messages:
            content = msg.content if hasattr(msg, "content") else str(msg)
            total += len(content) // 4  # ~4 chars per token
        return total

    # ---- Auto-summarization (post-hook on context length) ----

    def _summarize_conversation(self, messages: list) -> str:
        """Summarize conversation using a SimpleAgent."""
        if self._summarizer is None:
            from haive.agents.simple.agent import SimpleAgent
            self._summarizer = SimpleAgent(
                name=f"{self.name}_summarizer",
                engine=AugLLMConfig(
                    temperature=0.2,
                    system_message=(
                        "Summarize this conversation concisely. Include:\n"
                        "- Key facts learned about the user\n"
                        "- Decisions made\n"
                        "- User preferences expressed\n"
                        "- Important context for future conversations"
                    ),
                ),
            )

        conv_text = "\n".join(
            f"{'User' if isinstance(m, HumanMessage) else 'Assistant'}: {m.content[:300]}"
            for m in messages if hasattr(m, "content") and m.content
        )

        try:
            result = self._summarizer.run(f"Summarize:\n\n{conv_text}")
            if hasattr(result, "messages") and result.messages:
                return result.messages[-1].content
        except Exception as e:
            logger.warning(f"Summarization failed: {e}")

        return f"Conversation with {len(messages)} messages."

    # ---- KG extraction (post-hook) ----

    def _extract_and_store_kg(self, messages: list) -> None:
        """Extract KG triples from conversation and store them.

        Uses a SimpleAgent with structured output to extract triples,
        then stores them via the store's put() API.
        """
        if not self.auto_extract_kg or not self._store:
            return

        # Build conversation text from last exchange (not entire history)
        recent = [m for m in messages[-4:] if hasattr(m, "content") and m.content]
        if not recent:
            return

        conv_text = "\n".join(
            f"{'User' if isinstance(m, HumanMessage) else 'Assistant'}: {m.content[:300]}"
            for m in recent
        )

        if self._extractor is None:
            from haive.agents.simple.agent import SimpleAgent
            self._extractor = SimpleAgent(
                name=f"{self.name}_extractor",
                engine=AugLLMConfig(
                    temperature=0.1,
                    system_message=(
                        "Extract structured information from this conversation.\n"
                        "Identify knowledge graph triples (subject-predicate-object facts).\n"
                        "Focus on facts about the user, their preferences, relationships, and context.\n"
                        "Only extract if there is genuinely useful information to save."
                    ),
                ),
            )

        try:
            result = self._extractor.run(
                f"Extract triples from this conversation:\n\n{conv_text}\n\n"
                "Respond with JSON: {\"triples\": [{\"subject\": \"...\", \"predicate\": \"...\", \"object\": \"...\"}], \"should_save\": true/false}"
            )

            # Parse the extraction result
            response_text = ""
            if hasattr(result, "messages") and result.messages:
                response_text = result.messages[-1].content
            elif isinstance(result, str):
                response_text = result

            if not response_text:
                return

            # Try to parse JSON from response
            import json
            # Find JSON in response (may be wrapped in markdown)
            json_start = response_text.find("{")
            json_end = response_text.rfind("}") + 1
            if json_start >= 0 and json_end > json_start:
                extraction = json.loads(response_text[json_start:json_end])
                if not extraction.get("should_save", True):
                    return

                kg_ns = ("kg", self.user_id)
                for triple in extraction.get("triples", []):
                    subj = triple.get("subject", "")
                    pred = triple.get("predicate", "")
                    obj = triple.get("object", "")
                    if subj and pred and obj:
                        key = f"{subj}_{pred}_{obj}".replace(" ", "_")[:100]
                        self._store.put(
                            kg_ns, key,
                            {"subject": subj, "predicate": pred, "object": obj, "type": "kg_triple"},
                        )
                        logger.info(f"KG extracted: {subj} {pred} {obj}")

        except json.JSONDecodeError:
            logger.debug("KG extraction: no valid JSON in response")
        except Exception as e:
            logger.warning(f"KG extraction failed: {e}")

    # ---- Main run loop ----

    def run(self, input_data: str | dict | Any = None, debug: bool | None = None, **kwargs) -> Any:
        """Run with memory: load context -> respond -> extract KG -> maybe summarize.

        Flow:
        1. Pre-hook: Load memory context (memories + KG triples + summaries)
        2. Execute: ReactAgent responds (may call memory tools)
        3. Post-hook: Extract KG triples from conversation
        4. Post-hook: Auto-summarize if context length exceeds threshold
        """
        # Extract query for memory search
        if isinstance(input_data, str):
            query = input_data
        elif isinstance(input_data, dict):
            query = input_data.get("query", "")
            if not query and input_data.get("messages"):
                msgs = input_data["messages"]
                if msgs:
                    last = msgs[-1]
                    query = last.content if hasattr(last, "content") else str(last)
        else:
            query = str(input_data) if input_data else ""

        # ---- PRE-HOOK: Load memory context ----
        memory_ctx = self._load_memory_context(query)
        if memory_ctx and self.engine:
            self.engine.system_message = MEMORY_SYSTEM_PROMPT.format(memory_context=memory_ctx)

        # ---- EXECUTE: ReactAgent ----
        kwargs.pop("debug", None)
        result = super().run(input_data, debug=debug, **kwargs)

        # ---- POST-HOOKS ----
        if hasattr(result, "messages") and result.messages:
            token_count = self._count_tokens(result.messages)

            # Post-hook 1: KG extraction (lightweight, runs on recent messages)
            try:
                self._extract_and_store_kg(result.messages)
            except Exception as e:
                logger.warning(f"KG extraction post-hook failed: {e}")

            # Post-hook 2: Auto-summarize if context length exceeded
            if token_count > self.summarize_threshold and self.auto_save:
                try:
                    summary = self._summarize_conversation(result.messages)
                    summary_ns = ("summary", self.user_id)
                    self._store.put(
                        summary_ns,
                        str(uuid.uuid4()),
                        {"content": summary, "type": "conversation_summary"},
                    )
                    logger.info(f"Auto-summarized conversation ({token_count} tokens)")
                except Exception as e:
                    logger.warning(f"Failed to save summary: {e}")

        return result

    def get_store(self) -> Any:
        """Get the underlying store for direct access."""
        return self._store

    # ---- Advanced: Document-level KG extraction ----

    def extract_kg_from_document(self, text: str, allowed_nodes: list[str] | None = None) -> list[dict]:
        """Extract KG triples from a document using GraphTransformer.

        Uses haive.agents.document_modifiers.kg for full document-level
        knowledge graph extraction (more thorough than conversation extraction).

        Args:
            text: Document text to extract from
            allowed_nodes: Optional list of entity types to extract

        Returns:
            List of extracted triples as dicts
        """
        try:
            from langchain_core.documents import Document
            from haive.agents.document_modifiers.kg.kg_base.models import GraphTransformer

            transformer = GraphTransformer()
            docs = [Document(page_content=text)]
            graphs = transformer.transform_documents(
                documents=docs,
                allowed_nodes=allowed_nodes or [],
                strict_mode=False,
            )

            triples = []
            kg_ns = ("kg", self.user_id)
            for graph in graphs:
                for rel in graph.relationships:
                    triple = {
                        "subject": rel.source.id,
                        "predicate": rel.type,
                        "object": rel.target.id,
                    }
                    triples.append(triple)
                    # Also store in the store
                    key = f"{triple['subject']}_{triple['predicate']}_{triple['object']}".replace(" ", "_")[:100]
                    self._store.put(
                        kg_ns, key,
                        {**triple, "type": "kg_triple", "source": "document_extraction"},
                    )

            logger.info(f"Extracted {len(triples)} triples from document")
            return triples

        except ImportError as e:
            logger.warning(f"GraphTransformer not available: {e}")
            return []
        except Exception as e:
            logger.warning(f"Document KG extraction failed: {e}")
            return []


def create_memory_agent(
    name: str = "memory_agent",
    store: Any = None,
    connection_string: str | None = None,
    extra_tools: list | None = None,
    user_id: str = "default",
    auto_extract_kg: bool = True,
    summarize_threshold: int = 4000,
    **kwargs,
) -> MemoryAgent:
    """Factory for creating a memory agent with store + memory tools pre-wired.

    This is the recommended way to create a MemoryAgent. It resolves the store,
    creates memory tools, and passes them into the engine so ReactAgent's
    tool routing works correctly.

    Args:
        name: Agent name
        store: Direct store instance (takes precedence over connection_string)
        connection_string: PostgreSQL connection string for production
        extra_tools: Additional tools beyond memory tools
        user_id: User ID for memory scoping
        auto_extract_kg: Enable automatic KG triple extraction from conversations
        summarize_threshold: Token count threshold for auto-summarization
        **kwargs: Additional MemoryAgent/ReactAgent kwargs
    """
    # Resolve store
    resolved_store = _resolve_store(store, connection_string)

    # Create memory tools bound to this store + user
    memory_tools = create_memory_tools(resolved_store, user_id)

    # Combine with any extra user tools
    all_tools = list(extra_tools or []) + memory_tools

    # Build engine with tools included (so ReactAgent routing works)
    engine_kwargs = {"temperature": 0.7}
    if "engine" in kwargs:
        provided_engine = kwargs.pop("engine")
        if isinstance(provided_engine, AugLLMConfig):
            engine_kwargs["temperature"] = provided_engine.temperature
            if provided_engine.system_message:
                engine_kwargs["system_message"] = provided_engine.system_message
            if provided_engine.tools:
                all_tools = list(provided_engine.tools) + all_tools
    if "system_message" not in engine_kwargs:
        engine_kwargs["system_message"] = MEMORY_SYSTEM_PROMPT.format(memory_context="")

    engine = AugLLMConfig(tools=all_tools, **engine_kwargs)

    agent = MemoryAgent(
        name=name,
        user_id=user_id,
        engine=engine,
        auto_extract_kg=auto_extract_kg,
        summarize_threshold=summarize_threshold,
        **kwargs,
    )
    agent._store = resolved_store
    return agent
