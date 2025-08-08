"""Standalone memory models for the reorganized memory system.

This module provides core memory models that are used throughout the memory system,
designed to be standalone without heavy dependencies to avoid circular imports.
"""

from __future__ import annotations

import json
import logging
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Union
from uuid import uuid4

from pydantic import BaseModel, Field, field_validator, model_validator

logger = logging.getLogger(__name__)


class ImportanceLevel(str, Enum):
    """Importance levels for memory items."""

    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    TRIVIAL = "trivial"


class MemoryType(str, Enum):
    """Types of memory for classification."""

    FACTUAL = "factual"
    PROCEDURAL = "procedural"
    EPISODIC = "episodic"
    SEMANTIC = "semantic"
    EMOTIONAL = "emotional"
    CONTEXTUAL = "contextual"


class KnowledgeTriple(BaseModel):
    """Knowledge graph triple structure (subject-predicate-object)."""

    subject: str = Field(..., description="Subject entity")
    predicate: str = Field(..., description="Relationship/predicate")
    object: str = Field(..., description="Object entity")
    confidence: float = Field(
        default=1.0, ge=0.0, le=1.0, description="Confidence score"
    )
    source: Optional[str] = Field(default=None, description="Source of this knowledge")
    timestamp: datetime = Field(
        default_factory=datetime.now, description="When this triple was created"
    )

    def to_string(self) -> str:
        """Convert triple to readable string."""
        return f"{self.subject} {self.predicate} {self.object}"

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for storage."""
        return {
            "subject": self.subject,
            "predicate": self.predicate,
            "object": self.object,
            "confidence": self.confidence,
            "source": self.source,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "KnowledgeTriple":
        """Create from dictionary."""
        if isinstance(data.get("timestamp"), str):
            data["timestamp"] = datetime.fromisoformat(data["timestamp"])
        return cls(**data)


class MemoryItem(BaseModel):
    """Basic memory item with core attributes."""

    id: str = Field(
        default_factory=lambda: str(uuid4()), description="Unique memory ID"
    )
    content: str = Field(..., description="Memory content/text")
    memory_type: MemoryType = Field(
        default=MemoryType.SEMANTIC, description="Type of memory"
    )
    importance: ImportanceLevel = Field(
        default=ImportanceLevel.MEDIUM, description="Importance level"
    )
    timestamp: datetime = Field(
        default_factory=datetime.now, description="When memory was created"
    )
    last_accessed: datetime = Field(
        default_factory=datetime.now, description="Last access time"
    )
    access_count: int = Field(default=0, description="Number of times accessed")
    tags: List[str] = Field(default_factory=list, description="Memory tags")
    metadata: Dict[str, Any] = Field(
        default_factory=dict, description="Additional metadata"
    )

    # Knowledge graph fields
    entities: List[str] = Field(default_factory=list, description="Extracted entities")
    relations: List[KnowledgeTriple] = Field(
        default_factory=list, description="Knowledge relations"
    )

    # Context fields
    context_id: Optional[str] = Field(default=None, description="Context/session ID")
    user_id: Optional[str] = Field(default=None, description="Associated user ID")
    source: Optional[str] = Field(default=None, description="Source of memory")

    @field_validator("content")
    @classmethod
    def validate_content(cls, v: str) -> str:
        """Validate content is not empty."""
        if not v or not v.strip():
            raise ValueError("Memory content cannot be empty")
        return v.strip()

    @field_validator("tags")
    @classmethod
    def validate_tags(cls, v: List[str]) -> List[str]:
        """Validate and normalize tags."""
        return [tag.lower().strip() for tag in v if tag and tag.strip()]

    def update_access(self) -> None:
        """Update access tracking."""
        self.last_accessed = datetime.now()
        self.access_count += 1

    def add_tag(self, tag: str) -> None:
        """Add a tag to the memory."""
        normalized_tag = tag.lower().strip()
        if normalized_tag and normalized_tag not in self.tags:
            self.tags.append(normalized_tag)

    def remove_tag(self, tag: str) -> bool:
        """Remove a tag from the memory."""
        normalized_tag = tag.lower().strip()
        if normalized_tag in self.tags:
            self.tags.remove(normalized_tag)
            return True
        return False

    def add_entity(self, entity: str) -> None:
        """Add an entity to the memory."""
        entity = entity.strip()
        if entity and entity not in self.entities:
            self.entities.append(entity)

    def add_relation(self, relation: KnowledgeTriple) -> None:
        """Add a knowledge relation."""
        if relation not in self.relations:
            self.relations.append(relation)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for storage."""
        return {
            "id": self.id,
            "content": self.content,
            "memory_type": self.memory_type.value,
            "importance": self.importance.value,
            "timestamp": self.timestamp.isoformat(),
            "last_accessed": self.last_accessed.isoformat(),
            "access_count": self.access_count,
            "tags": self.tags,
            "metadata": self.metadata,
            "entities": self.entities,
            "relations": [r.to_dict() for r in self.relations],
            "context_id": self.context_id,
            "user_id": self.user_id,
            "source": self.source,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MemoryItem":
        """Create from dictionary."""
        # Handle datetime conversion
        for field in ["timestamp", "last_accessed"]:
            if isinstance(data.get(field), str):
                data[field] = datetime.fromisoformat(data[field])

        # Handle enum conversion
        if isinstance(data.get("memory_type"), str):
            data["memory_type"] = MemoryType(data["memory_type"])
        if isinstance(data.get("importance"), str):
            data["importance"] = ImportanceLevel(data["importance"])

        # Handle relations conversion
        if "relations" in data and isinstance(data["relations"], list):
            data["relations"] = [
                KnowledgeTriple.from_dict(r) if isinstance(r, dict) else r
                for r in data["relations"]
            ]

        return cls(**data)


class EnhancedMemoryItem(MemoryItem):
    """Enhanced memory item with additional capabilities."""

    # Enhanced scoring and ranking
    relevance_score: float = Field(
        default=0.0, ge=0.0, le=1.0, description="Relevance score"
    )
    quality_score: float = Field(
        default=0.0, ge=0.0, le=1.0, description="Quality score"
    )
    embedding: Optional[List[float]] = Field(
        default=None, description="Vector embedding"
    )

    # Enhanced relationships
    related_memories: List[str] = Field(
        default_factory=list, description="Related memory IDs"
    )
    parent_memory: Optional[str] = Field(default=None, description="Parent memory ID")
    child_memories: List[str] = Field(
        default_factory=list, description="Child memory IDs"
    )

    # Enhanced processing
    processing_status: str = Field(default="raw", description="Processing status")
    extracted_facts: List[str] = Field(
        default_factory=list, description="Extracted facts"
    )
    sentiment: Optional[str] = Field(default=None, description="Sentiment analysis")
    summary: Optional[str] = Field(default=None, description="Memory summary")

    # Enhanced retrieval
    retrieval_contexts: List[str] = Field(
        default_factory=list, description="Contexts where retrieved"
    )
    retrieval_count: int = Field(default=0, description="Number of retrievals")
    last_retrieved: Optional[datetime] = Field(
        default=None, description="Last retrieval time"
    )

    def update_retrieval(self, context: str = "") -> None:
        """Update retrieval tracking."""
        self.last_retrieved = datetime.now()
        self.retrieval_count += 1
        if context and context not in self.retrieval_contexts:
            self.retrieval_contexts.append(context)
        self.update_access()  # Also update base access tracking

    def calculate_composite_score(self) -> float:
        """Calculate composite relevance score."""
        # Weight different factors
        importance_weight = 0.3
        quality_weight = 0.3
        relevance_weight = 0.2
        recency_weight = 0.1
        access_weight = 0.1

        # Convert importance to numeric
        importance_scores = {
            ImportanceLevel.CRITICAL: 1.0,
            ImportanceLevel.HIGH: 0.8,
            ImportanceLevel.MEDIUM: 0.6,
            ImportanceLevel.LOW: 0.4,
            ImportanceLevel.TRIVIAL: 0.2,
        }
        importance_score = importance_scores.get(self.importance, 0.6)

        # Calculate recency score (more recent = higher score)
        if self.timestamp:
            hours_old = (datetime.now() - self.timestamp).total_seconds() / 3600
            recency_score = max(0.0, 1.0 - (hours_old / (24 * 7)))  # Decay over week
        else:
            recency_score = 0.0

        # Calculate access score
        access_score = min(1.0, self.access_count / 10.0)  # Cap at 10 accesses

        # Combine scores
        composite = (
            importance_score * importance_weight
            + self.quality_score * quality_weight
            + self.relevance_score * relevance_weight
            + recency_score * recency_weight
            + access_score * access_weight
        )

        return min(1.0, max(0.0, composite))

    def add_related_memory(self, memory_id: str) -> None:
        """Add a related memory ID."""
        if memory_id and memory_id not in self.related_memories:
            self.related_memories.append(memory_id)

    def set_parent_memory(self, parent_id: str) -> None:
        """Set parent memory ID."""
        self.parent_memory = parent_id

    def add_child_memory(self, child_id: str) -> None:
        """Add a child memory ID."""
        if child_id and child_id not in self.child_memories:
            self.child_memories.append(child_id)

    def extract_fact(self, fact: str) -> None:
        """Add an extracted fact."""
        fact = fact.strip()
        if fact and fact not in self.extracted_facts:
            self.extracted_facts.append(fact)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary including enhanced fields."""
        base_dict = super().to_dict()
        enhanced_dict = {
            "relevance_score": self.relevance_score,
            "quality_score": self.quality_score,
            "embedding": self.embedding,
            "related_memories": self.related_memories,
            "parent_memory": self.parent_memory,
            "child_memories": self.child_memories,
            "processing_status": self.processing_status,
            "extracted_facts": self.extracted_facts,
            "sentiment": self.sentiment,
            "summary": self.summary,
            "retrieval_contexts": self.retrieval_contexts,
            "retrieval_count": self.retrieval_count,
            "last_retrieved": (
                self.last_retrieved.isoformat() if self.last_retrieved else None
            ),
        }
        base_dict.update(enhanced_dict)
        return base_dict

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "EnhancedMemoryItem":
        """Create from dictionary."""
        # Handle last_retrieved datetime conversion
        if isinstance(data.get("last_retrieved"), str):
            data["last_retrieved"] = datetime.fromisoformat(data["last_retrieved"])

        # Use parent class method for base conversion, then create enhanced
        base_data = data.copy()
        return cls(**base_data)

    @classmethod
    def from_memory_item(cls, memory_item: MemoryItem) -> "EnhancedMemoryItem":
        """Create enhanced memory from basic memory item."""
        return cls(**memory_item.model_dump())


# Helper functions for memory operations


def create_memory_item(
    content: str,
    memory_type: MemoryType = MemoryType.SEMANTIC,
    importance: ImportanceLevel = ImportanceLevel.MEDIUM,
    tags: Optional[List[str]] = None,
    context_id: Optional[str] = None,
    user_id: Optional[str] = None,
    source: Optional[str] = None,
    enhanced: bool = False,
) -> Union[MemoryItem, EnhancedMemoryItem]:
    """Create a memory item with the specified parameters."""

    kwargs = {
        "content": content,
        "memory_type": memory_type,
        "importance": importance,
        "tags": tags or [],
        "context_id": context_id,
        "user_id": user_id,
        "source": source,
    }

    if enhanced:
        return EnhancedMemoryItem(**kwargs)
    else:
        return MemoryItem(**kwargs)


def create_knowledge_triple(
    subject: str,
    predicate: str,
    object: str,
    confidence: float = 1.0,
    source: Optional[str] = None,
) -> KnowledgeTriple:
    """Create a knowledge triple."""
    return KnowledgeTriple(
        subject=subject,
        predicate=predicate,
        object=object,
        confidence=confidence,
        source=source,
    )


def merge_memory_items(items: List[MemoryItem]) -> EnhancedMemoryItem:
    """Merge multiple memory items into one enhanced memory item."""
    if not items:
        raise ValueError("Cannot merge empty list of memory items")

    # Use first item as base
    base_item = items[0]

    # Combine content
    combined_content = []
    all_tags = set()
    all_entities = set()
    all_relations = []
    all_facts = []

    for item in items:
        combined_content.append(item.content)
        all_tags.update(item.tags)
        all_entities.update(item.entities)
        all_relations.extend(item.relations)

        if isinstance(item, EnhancedMemoryItem):
            all_facts.extend(item.extracted_facts)

    # Create enhanced memory with merged content
    merged = EnhancedMemoryItem(
        content=" | ".join(combined_content),
        memory_type=base_item.memory_type,
        importance=max(item.importance for item in items),  # Use highest importance
        tags=list(all_tags),
        entities=list(all_entities),
        relations=all_relations,
        extracted_facts=all_facts,
        context_id=base_item.context_id,
        user_id=base_item.user_id,
        source=f"merged_{len(items)}_items",
    )

    # Set related memories to the merged items
    merged.related_memories = [item.id for item in items]

    return merged


# Export all public classes and functions
__all__ = [
    "MemoryItem",
    "EnhancedMemoryItem",
    "KnowledgeTriple",
    "ImportanceLevel",
    "MemoryType",
    "create_memory_item",
    "create_knowledge_triple",
    "merge_memory_items",
]
