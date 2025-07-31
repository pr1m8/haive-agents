"""Test only the memory models without requiring LLMs or embeddings."""

import traceback

from haive.agents.memory_v2.memory_state_original import (
    EnhancedKnowledgeTriple,
    EnhancedMemoryItem,
    ImportanceLevel,
    KnowledgeTriple,
    MemoryItem,
    MemoryState,
    MemoryType,
    UnifiedMemoryEntry,
)
from haive.agents.memory_v2.memory_state_with_tokens import MemoryStateWithTokens


def test_memory_models():
    """Test memory models functionality."""
    # Test basic MemoryItem
    MemoryItem(content="Alice works at TechCorp", memory_type=MemoryType.FACTUAL)

    # Test EnhancedMemoryItem
    enhanced_memory = EnhancedMemoryItem(
        content="Bob is the CTO of DataCorp",
        memory_type=MemoryType.FACTUAL,
        tags=["executive", "technology"],
        user_id="test_user",
        confidence=0.9,
        importance=ImportanceLevel.HIGH,
    )

    # Test KnowledgeTriple
    KnowledgeTriple(
        subject="TechCorp", predicate="employs", object="Alice", confidence=0.95
    )

    # Test EnhancedKnowledgeTriple
    enhanced_triple = EnhancedKnowledgeTriple(
        subject="DataCorp",
        predicate="has_cto",
        object="Bob",
        importance=ImportanceLevel.HIGH,
        supporting_evidence="From company website",
    )

    # Test UnifiedMemoryEntry
    entry1 = UnifiedMemoryEntry.from_memory_item(enhanced_memory)

    entry2 = UnifiedMemoryEntry.from_knowledge_triple(enhanced_triple)

    # Test MemoryState
    state = MemoryState(user_id="test_user")

    # Add memories
    state.add_memory_item(enhanced_memory)
    state.add_knowledge_triple(enhanced_triple)

    # Search memories
    state.search_memories("Bob")

    # Test MemoryStateWithTokens
    token_state = MemoryStateWithTokens(
        messages=[], total_tokens=0, current_memories=[]
    )

    # Add a memory entry
    token_state.current_memories.append(entry1)
    token_state.current_memories.append(entry2)

    # Test routing decision
    token_state.get_memory_route()

    # Test memory types
    for _mem_type in MemoryType:
        pass

    # Test importance levels
    for _level in ImportanceLevel:
        pass

    return True


def test_memory_stats():
    """Test memory statistics functionality."""
    state = MemoryState(user_id="test_user")

    # Add various types of memories
    memories = [
        ("Fact 1", MemoryType.FACTUAL, ImportanceLevel.HIGH),
        ("Fact 2", MemoryType.FACTUAL, ImportanceLevel.MEDIUM),
        ("Conversation 1", MemoryType.CONVERSATIONAL, ImportanceLevel.LOW),
        ("Conversation 2", MemoryType.CONVERSATIONAL, ImportanceLevel.MEDIUM),
        ("Procedure 1", MemoryType.PROCEDURAL, ImportanceLevel.HIGH),
    ]

    for content, mem_type, importance in memories:
        memory = EnhancedMemoryItem(
            content=content, memory_type=mem_type, importance=importance
        )
        state.add_memory_item(memory)

    # Add some triples
    triples = [
        ("Company", "has_employee", "Person1"),
        ("Person1", "knows", "Person2"),
        ("Person2", "works_at", "Company"),
    ]

    for subj, pred, obj in triples:
        triple = EnhancedKnowledgeTriple(
            subject=subj, predicate=pred, object=obj, importance=ImportanceLevel.MEDIUM
        )
        state.add_knowledge_triple(triple)

    # Check stats

    for mem_type, _count in state.stats.memories_by_type.items():
        pass

    for importance, _count in state.stats.memories_by_importance.items():
        pass

    return True


def test_memory_search():
    """Test memory search functionality."""
    state = MemoryState(user_id="test_user")

    # Add searchable content
    test_data = [
        "Alice Johnson is a senior AI researcher at TechCorp",
        "Bob Smith works as the CTO of DataCorp",
        "Carol Williams is a data scientist at AI Labs",
        "TechCorp specializes in machine learning solutions",
        "DataCorp provides cloud infrastructure services",
        "AI Labs focuses on natural language processing",
    ]

    for content in test_data:
        memory = EnhancedMemoryItem(content=content, memory_type=MemoryType.FACTUAL)
        state.add_memory_item(memory)

    # Test searches
    searches = [("Alice", 1), ("Corp", 2), ("AI", 2), ("scientist", 1), ("xyz", 0)]

    for query, expected_count in searches:
        results = state.search_memories(query)
        assert (
            len(results) >= expected_count
        ), f"Expected at least {expected_count} results"

    return True


def main():
    """Run all memory model tests."""
    try:
        # Run tests
        test_memory_models()
        test_memory_stats()
        test_memory_search()

    except Exception:

        traceback.print_exc()


if __name__ == "__main__":
    main()
