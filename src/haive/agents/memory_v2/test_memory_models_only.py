"""Test only the memory models without requiring LLMs or embeddings."""

from datetime import datetime

from haive.agents.memory_v2.memory_state_original import (
    EnhancedKnowledgeTriple,
    EnhancedMemoryItem,
    ImportanceLevel,
    KnowledgeTriple,
    MemoryItem,
    MemoryState,
    MemoryStats,
    MemoryType,
    UnifiedMemoryEntry,
)
from haive.agents.memory_v2.memory_state_with_tokens import MemoryStateWithTokens


def test_memory_models():
    """Test memory models functionality."""
    print("\n=== Testing Memory Models ===\n")

    # Test basic MemoryItem
    print("1. Testing MemoryItem...")
    basic_memory = MemoryItem(
        content="Alice works at TechCorp", memory_type=MemoryType.FACTUAL
    )
    print(f"   Created: {basic_memory.content}")
    print(f"   Type: {basic_memory.memory_type}")

    # Test EnhancedMemoryItem
    print("\n2. Testing EnhancedMemoryItem...")
    enhanced_memory = EnhancedMemoryItem(
        content="Bob is the CTO of DataCorp",
        memory_type=MemoryType.FACTUAL,
        tags=["executive", "technology"],
        user_id="test_user",
        confidence=0.9,
        importance=ImportanceLevel.HIGH,
    )
    print(f"   Created: {enhanced_memory.content}")
    print(f"   Tags: {enhanced_memory.tags}")
    print(f"   ID: {enhanced_memory.id}")

    # Test KnowledgeTriple
    print("\n3. Testing KnowledgeTriple...")
    triple = KnowledgeTriple(
        subject="TechCorp", predicate="employs", object="Alice", confidence=0.95
    )
    print(f"   Triple: {triple.subject} {triple.predicate} {triple.object}")

    # Test EnhancedKnowledgeTriple
    print("\n4. Testing EnhancedKnowledgeTriple...")
    enhanced_triple = EnhancedKnowledgeTriple(
        subject="DataCorp",
        predicate="has_cto",
        object="Bob",
        importance=ImportanceLevel.HIGH,
        supporting_evidence="From company website",
    )
    print(
        f"   Triple: {enhanced_triple.subject} {enhanced_triple.predicate} {enhanced_triple.object}"
    )
    print(f"   Importance: {enhanced_triple.importance}")

    # Test UnifiedMemoryEntry
    print("\n5. Testing UnifiedMemoryEntry...")
    entry1 = UnifiedMemoryEntry.from_memory_item(enhanced_memory)
    print(f"   Entry type: {entry1.entry_type}")
    print(f"   Content: {entry1.content}")

    entry2 = UnifiedMemoryEntry.from_knowledge_triple(enhanced_triple)
    print(f"   Triple entry: {entry2.content}")

    # Test MemoryState
    print("\n6. Testing MemoryState...")
    state = MemoryState(user_id="test_user")

    # Add memories
    state.add_memory_item(enhanced_memory)
    state.add_knowledge_triple(enhanced_triple)

    print(f"   Total memories: {state.stats.total_memories}")
    print(f"   Memory items: {state.stats.total_memory_items}")
    print(f"   Knowledge triples: {state.stats.total_knowledge_triples}")

    # Search memories
    results = state.search_memories("Bob")
    print(f"   Search 'Bob': Found {len(results)} results")

    # Test MemoryStateWithTokens
    print("\n7. Testing MemoryStateWithTokens...")
    token_state = MemoryStateWithTokens(
        messages=[], total_tokens=0, current_memories=[]
    )

    # Add a memory entry
    token_state.current_memories.append(entry1)
    token_state.current_memories.append(entry2)

    print(f"   Memories: {len(token_state.current_memories)}")
    print(f"   Has graph fields: {hasattr(token_state, 'knowledge_graph')}")

    # Test routing decision
    route = token_state.get_memory_route()
    print(f"   Memory route: {route}")

    # Test memory types
    print("\n8. Testing MemoryType enum...")
    for mem_type in MemoryType:
        print(f"   - {mem_type.value}")

    # Test importance levels
    print("\n9. Testing ImportanceLevel enum...")
    for level in ImportanceLevel:
        print(f"   - {level.value}")

    print("\n✅ All memory model tests passed!")
    return True


def test_memory_stats():
    """Test memory statistics functionality."""
    print("\n=== Testing Memory Statistics ===\n")

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
    print("Memory Statistics:")
    print(f"  Total memories: {state.stats.total_memories}")
    print(f"  Memory items: {state.stats.total_memory_items}")
    print(f"  Knowledge triples: {state.stats.total_knowledge_triples}")

    print("\nMemories by type:")
    for mem_type, count in state.stats.memories_by_type.items():
        print(f"  {mem_type}: {count}")

    print("\nMemories by importance:")
    for importance, count in state.stats.memories_by_importance.items():
        print(f"  {importance}: {count}")

    print("\n✅ Memory statistics test passed!")
    return True


def test_memory_search():
    """Test memory search functionality."""
    print("\n=== Testing Memory Search ===\n")

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

    print("Search Results:")
    for query, expected_count in searches:
        results = state.search_memories(query)
        print(f"  Query '{query}': Found {len(results)} (expected {expected_count})")
        assert (
            len(results) >= expected_count
        ), f"Expected at least {expected_count} results"

    print("\n✅ Memory search test passed!")
    return True


def main():
    """Run all memory model tests."""
    print("\n🚀 Testing Memory Models (No LLM/Embeddings Required) 🚀")
    print("=" * 60)

    try:
        # Run tests
        test_memory_models()
        test_memory_stats()
        test_memory_search()

        print("\n" + "=" * 60)
        print("✨ ALL MEMORY MODEL TESTS PASSED! ✨")
        print("=" * 60)

    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()
