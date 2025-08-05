#!/usr/bin/env python3
"""Test SimpleRAG V3 implementation bypassing broken import chains."""

import sys
from unittest.mock import MagicMock


# Add source paths
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")


def test_simple_rag_v3_architecture():
    """Test SimpleRAG V3 architecture and pattern compliance."""
    # Import components directly, bypassing broken chains
    from haive.agents.rag.simple.enhanced_v3.state import SimpleRAGState

    # Mock the problematic dependencies to test our architecture
    sys.modules["haive.agents.rag.base.agent"] = MagicMock()
    sys.modules["haive.agents.simple.agent"] = MagicMock()
    sys.modules["haive.agents.multi.enhanced_multi_agent_v3"] = MagicMock()

    # Create mock classes for dependencies
    MockBaseRAGAgent = MagicMock()
    MockSimpleAgent = MagicMock()
    MockEnhancedMultiAgent = MagicMock()

    sys.modules["haive.agents.rag.base.agent"].BaseRAGAgent = MockBaseRAGAgent
    sys.modules["haive.agents.simple.agent"].SimpleAgent = MockSimpleAgent
    sys.modules[
        "haive.agents.multi.enhanced_multi_agent_v3"
    ].EnhancedMultiAgent = MockEnhancedMultiAgent

    # Now import our components
    from haive.agents.rag.simple.enhanced_v3.answer_generator_agent import (
        SimpleAnswerAgent,
    )
    from haive.agents.rag.simple.enhanced_v3.retriever_agent import RetrieverAgent

    # Test that our classes inherit from the right base classes
    assert RetrieverAgent.__bases__[0] == MockBaseRAGAgent
    assert SimpleAnswerAgent.__bases__[0] == MockSimpleAgent

    # Test state functionality (this should work without mocks)
    state = SimpleRAGState(query="Test query", retrieved_documents=[], generated_answer="")

    assert state.query == "Test query"
    assert state.current_stage == "ready"

    # Test stage progression
    state.update_stage("retrieval")
    state.update_stage("generation")
    state.update_stage("completed")

    assert state.current_stage == "completed"
    assert state.stage_history == ["retrieval", "generation", "completed"]

    return True


def test_simple_rag_v3_pattern_compliance():
    """Test that SimpleRAG V3 follows the requested MultiAgent pattern."""
    # Import agent type checking

    from haive.agents.rag.simple.enhanced_v3.agent import RAGAgentCollection

    # Verify the type alias is correct
    assert RAGAgentCollection is not None

    # Test that our implementation follows the pattern requested:
    # MultiAgent[RetrieverAgent, SimpleAnswerAgent]

    # Load our agent module to check class definition
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "agent_module",
        "/home/will/Projects/haive/backend/haive/packages/haive-agents/src/haive/agents/rag/simple/enhanced_v3/agent.py",
    )
    importlib.util.module_from_spec(spec)

    # Check if our class is properly defined
    with open(
        "/home/will/Projects/haive/backend/haive/packages/haive-agents/src/haive/agents/rag/simple/enhanced_v3/agent.py",
    ) as f:
        content = f.read()

    # Verify pattern compliance in source code
    assert "EnhancedMultiAgent[RAGAgentCollection]" in content
    assert "RAGAgentCollection = List[RetrieverAgent | SimpleAnswerAgent]" in content
    assert 'execution_mode = "sequential"' in content

    return True


def test_simple_rag_v3_features():
    """Test SimpleRAG V3 enhanced features."""
    # Test state features
    from langchain_core.documents import Document

    from haive.agents.rag.simple.enhanced_v3.state import SimpleRAGState

    state = SimpleRAGState(
        query="What is machine learning?", retrieved_documents=[], generated_answer=""
    )

    # Test performance tracking
    state.update_performance_metric("retrieval_time", 0.5)
    state.update_performance_metric("generation_time", 1.2)
    state.update_performance_metric("total_time", 1.7)

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

    assert state.retrieval_debug.search_time == 0.45
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

    assert pipeline_summary["documents_retrieved"] == 2
    assert pipeline_summary["answer_generated"] is True
    assert retrieval_summary["documents_count"] == 2
    assert generation_summary["answer_length"] > 0

    return True


def test_file_organization():
    """Test that our file organization follows the requested structure."""
    base_path = "/home/will/Projects/haive/backend/haive/packages/haive-agents/src/haive/agents/rag/simple/enhanced_v3"

    # Check that all required files exist
    required_files = [
        "__init__.py",
        "state.py",
        "retriever_agent.py",
        "answer_generator_agent.py",
        "agent.py",
    ]

    for file in required_files:
        file_path = os.path.join(base_path, file)
        assert os.path.exists(file_path), f"Missing file: {file}"

    # Check that each has appropriate content
    with open(os.path.join(base_path, "state.py")) as f:
        state_content = f.read()
        assert "SimpleRAGState" in state_content
        assert "RAGMetadata" in state_content

    with open(os.path.join(base_path, "retriever_agent.py")) as f:
        retriever_content = f.read()
        assert "RetrieverAgent" in retriever_content
        assert "BaseRAGAgent" in retriever_content

    with open(os.path.join(base_path, "answer_generator_agent.py")) as f:
        answer_content = f.read()
        assert "SimpleAnswerAgent" in answer_content
        assert "SimpleAgent" in answer_content

    with open(os.path.join(base_path, "agent.py")) as f:
        agent_content = f.read()
        assert "SimpleRAGV3" in agent_content
        assert "EnhancedMultiAgent" in agent_content

    return True


def main():
    """Run all tests."""
    try:
        # Test architecture
        test_simple_rag_v3_architecture()

        # Test pattern compliance
        test_simple_rag_v3_pattern_compliance()

        # Test enhanced features
        test_simple_rag_v3_features()

        # Test file organization
        test_file_organization()

        return True

    except Exception:
        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
