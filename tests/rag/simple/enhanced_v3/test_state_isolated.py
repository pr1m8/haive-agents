#!/usr/bin/env python3
"""Test only the SimpleRAGState implementation in isolation."""

import sys

# Add the source directories to Python path
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")


def test_state_in_complete_isolation():
    """Test direct import of state module only."""
    print("🔍 Testing state module in complete isolation...")

    # Import ONLY the state module directly, not through __init__.py
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "state_module",
        "/home/will/Projects/haive/backend/haive/packages/haive-agents/src/haive/agents/rag/simple/enhanced_v3/state.py",
    )
    state_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(state_module)

    SimpleRAGState = state_module.SimpleRAGState
    RAGMetadata = state_module.RAGMetadata
    RetrievalDebugInfo = state_module.RetrievalDebugInfo
    GenerationDebugInfo = state_module.GenerationDebugInfo

    print("✅ State module imported successfully in isolation")
    return SimpleRAGState, RAGMetadata, RetrievalDebugInfo, GenerationDebugInfo


def test_basic_state_functionality():
    """Test basic state functionality."""
    print("🔍 Testing basic state functionality...")

    SimpleRAGState, RAGMetadata, RetrievalDebugInfo, GenerationDebugInfo = (
        test_state_in_complete_isolation()
    )

    # Import Document separately
    from langchain_core.documents import Document

    # Test basic creation
    state = SimpleRAGState(
        query="What is machine learning?", retrieved_documents=[], generated_answer=""
    )

    print(f"✅ State created with query: '{state.query}'")
    assert state.query == "What is machine learning?"
    assert state.current_stage == "ready"
    assert len(state.stage_history) == 0

    # Test stage tracking
    state.update_stage("retrieval")
    state.update_stage("generation")
    state.update_stage("completed")

    print(f"✅ Stage tracking: {state.stage_history}")
    assert state.current_stage == "completed"
    assert state.stage_history == ["retrieval", "generation", "completed"]

    # Test performance metrics
    state.update_performance_metric("retrieval_time", 0.5)
    state.update_performance_metric("generation_time", 1.2)
    state.update_performance_metric("total_time", 1.7)

    print(f"✅ Performance metrics: {state.performance_metrics}")
    assert state.performance_metrics["total_time"] == 1.7

    # Test debug information
    state.add_retrieval_debug(
        search_time=0.45, total_documents=100, similarity_scores=[0.9, 0.85, 0.8]
    )

    state.add_generation_debug(
        context_length=500,
        generation_time=1.15,
        prompt_tokens=200,
        completion_tokens=50,
    )

    print("✅ Debug information added")
    assert state.retrieval_debug is not None
    assert state.retrieval_debug.search_time == 0.45
    assert state.generation_debug is not None
    assert state.generation_debug.context_length == 500

    # Test with documents
    docs = [
        Document(
            page_content="Machine learning is a subset of AI.",
            metadata={"source": "ml_guide.pdf", "score": 0.9},
        ),
        Document(
            page_content="Neural networks are inspired by biological neurons.",
            metadata={"source": "nn_book.pdf", "score": 0.85},
        ),
    ]

    state.retrieved_documents = docs
    state.generated_answer = "Machine learning is a subset of artificial intelligence."
    state.document_sources = ["ml_guide.pdf", "nn_book.pdf"]

    # Test summaries
    pipeline_summary = state.get_pipeline_summary()
    retrieval_summary = state.get_retrieval_summary()
    generation_summary = state.get_generation_summary()

    print(f"✅ Pipeline summary: {list(pipeline_summary.keys())}")
    print(f"✅ Retrieval summary: {list(retrieval_summary.keys())}")
    print(f"✅ Generation summary: {list(generation_summary.keys())}")

    assert pipeline_summary["documents_retrieved"] == 2
    assert pipeline_summary["answer_generated"] is True
    assert retrieval_summary["documents_count"] == 2
    assert generation_summary["answer_length"] > 0

    return True


def test_rag_metadata():
    """Test RAG metadata model."""
    print("🔍 Testing RAGMetadata...")

    SimpleRAGState, RAGMetadata, RetrievalDebugInfo, GenerationDebugInfo = (
        test_state_in_complete_isolation()
    )

    metadata = RAGMetadata(
        query_analysis={"intent": "factual", "complexity": "medium"},
        retrieval_params={"top_k": 5, "threshold": 0.7},
        timing_info={"retrieval": 0.5, "generation": 1.2},
        quality_scores={"relevance": 0.9, "coherence": 0.85},
    )

    print(f"✅ RAGMetadata created with {len(metadata.model_dump())} fields")
    assert metadata.query_analysis["intent"] == "factual"
    assert metadata.timing_info["retrieval"] == 0.5

    return True


def main():
    """Run all tests."""
    print("🚀 Testing SimpleRAG V3 State in Complete Isolation")
    print("=" * 60)

    try:
        # Test state functionality
        test_basic_state_functionality()
        print()

        # Test metadata
        test_rag_metadata()
        print()

        print("🎉 ALL STATE TESTS PASSED!")
        print("✅ SimpleRAGState is working correctly in isolation")
        print("✅ Enhanced features (performance, debug) are functional")
        print("✅ State tracking and summaries work as expected")
        print("✅ Ready to test full SimpleRAG V3 once import issues are resolved")

    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback

        traceback.print_exc()
        return False

    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
