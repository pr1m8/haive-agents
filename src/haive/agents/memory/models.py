"""Memory system Pydantic models for structured extraction and storage.

Inspired by langmem's memory management approach but built on haive.core
store/persistence for async Postgres support.
"""

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class MemoryType(str, Enum):
    """Classification of memory types (inspired by cognitive science + langmem)."""
    EPISODIC = "episodic"       # Events, conversations, experiences
    SEMANTIC = "semantic"       # Facts, concepts, knowledge
    PROCEDURAL = "procedural"   # How-to, processes, skills
    PREFERENCE = "preference"   # User preferences, likes/dislikes


class KnowledgeTriple(BaseModel):
    """A subject-predicate-object knowledge graph triple."""
    subject: str = Field(description="The entity or concept (e.g. 'Python')")
    predicate: str = Field(description="The relationship (e.g. 'was created by')")
    object: str = Field(description="The target entity (e.g. 'Guido van Rossum')")
    confidence: float = Field(default=1.0, ge=0.0, le=1.0)


class MemoryExtraction(BaseModel):
    """Structured extraction from a conversation - what to remember.

    The memory extractor agent outputs this to decide what gets stored.
    Similar to langmem's MemoryStoreManager extraction but using our
    SimpleAgent with structured output.
    """
    summary: str = Field(description="Concise summary of what happened")
    key_facts: list[str] = Field(default_factory=list, description="Important facts to remember")
    knowledge_triples: list[KnowledgeTriple] = Field(
        default_factory=list,
        description="Extracted knowledge graph triples (subject-predicate-object)",
    )
    memory_type: MemoryType = Field(default=MemoryType.EPISODIC, description="Type of memory")
    importance: float = Field(
        default=0.5, ge=0.0, le=1.0,
        description="How important is this (0=trivial, 1=critical). Prioritize surprising or persistent info.",
    )
    user_preferences: list[str] = Field(
        default_factory=list,
        description="User preferences discovered (e.g. 'prefers Python', 'likes concise answers')",
    )
    should_remember: bool = Field(
        default=True,
        description="Whether this interaction contains anything worth remembering",
    )


class MemoryItem(BaseModel):
    """A single memory stored in the system."""
    id: str = Field(default="", description="Unique memory ID")
    content: str = Field(description="The memory content (human-readable)")
    memory_type: MemoryType = Field(default=MemoryType.EPISODIC)
    importance: float = Field(default=0.5)
    metadata: dict[str, Any] = Field(default_factory=dict)
    knowledge_triples: list[KnowledgeTriple] = Field(default_factory=list)
    namespace: str = Field(default="default", description="Store namespace for scoping")


class ConversationSummary(BaseModel):
    """Summary of a conversation for long-term storage."""
    summary: str = Field(description="Concise summary of the conversation")
    topics: list[str] = Field(default_factory=list, description="Topics discussed")
    key_decisions: list[str] = Field(default_factory=list, description="Key decisions made")
    action_items: list[str] = Field(default_factory=list, description="Action items identified")
    entities_mentioned: list[str] = Field(default_factory=list, description="People, orgs, concepts mentioned")


class MemorySearchResult(BaseModel):
    """Result from memory search."""
    content: str
    score: float = 0.0
    memory_type: MemoryType = MemoryType.EPISODIC
    metadata: dict[str, Any] = Field(default_factory=dict)
