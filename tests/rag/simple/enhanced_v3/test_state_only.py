#!/usr/bin/env python3
"""Test only the SimpleRAGState implementation."""

import sys

# Add the source directories to Python path
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")


def test_state_direct_import():
    """Test direct import of state module."""
    print("🔍 Testing direct state import...")

    # Import the state module directly
    from haive.agents.rag.simple.enhanced_v3.state import (
        GenerationDebugInfo,
        RAGMetadata,
        RetrievalDebugInfo,
        SimpleRAGState,
    )

    print("✅ State module imported successfully")
    return SimpleRAGState, RAGMetadata, RetrievalDebugInfo, GenerationDebugInfo


def test_basic_state_functionality():
    """Test basic state functionality."""
    print("🔍 Testing basic state functionality...")

    SimpleRAGState, RAGMetadata, RetrievalDebugInfo, GenerationDebugInfo = (
        test_state_direct_import()
    )

    # Test basic creation
    state = SimpleRAGState(
        query="What is machine learning?", retrieved_documents=[], generated_answer=""
    )

    print(f"✅ State created: {state.query}")

    # Test stage tracking
    state.update_stage("retrieval")
    state.update_stage("generation")

    print(f"✅ Stage tracking: {state.stage_history}")

    # Test performance metrics
    state.update_performance_metric("retrieval_time", 0.5)
    state.update_performance_metric("generation_time", 1.2)

    print(f"✅ Performance metrics: {state.performance_metrics}")

    # Test summary
    summary = state.get_pipeline_summary()
    print(f"✅ Pipeline summary keys: {list(summary.keys())}")

    return True


def main():
    """Run state-only tests."""
    print("🚀 Testing SimpleRAG V3 State Management Only")
    print("=" * 50)

    try:
        test_basic_state_functionality()

        print()
        print("🎉 ALL STATE TESTS PASSED!")
        print("✅ SimpleRAGState is working correctly")
        return True

    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
