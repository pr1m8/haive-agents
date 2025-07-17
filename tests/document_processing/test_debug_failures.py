#!/usr/bin/env python3
"""Debug the failing tests to understand the issues."""

import logging
import sys
from pathlib import Path

# Suppress all logging output
logging.getLogger().setLevel(logging.CRITICAL)

# Add the project root to the Python path
project_root = Path(__file__).parent.parent.parent.parent.parent
sys.path.insert(0, str(project_root))

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema.prebuilt.query_state import (
    QueryComplexity,
    QueryIntent,
    QueryProcessingConfig,
    QueryState,
    QueryType,
    RetrievalStrategy,
)
from langchain_core.documents import Document

from haive.agents.document_processing import (
    DocumentProcessingAgent,
    DocumentProcessingConfig,
)


def test_advanced_query_state_features():
    """Debug the advanced QueryState features test."""
    print("🔧 Testing Advanced QueryState Features...")

    try:
        # Create comprehensive query state
        query_state = QueryState(
            original_query="Analyze the impact of machine learning on healthcare",
            query_type=QueryType.ANALYTICAL,
            retrieval_strategy=RetrievalStrategy.HYBRID,
            query_complexity=QueryComplexity.EXPERT,
            query_intent=QueryIntent.LEARNING,
            query_expansion_enabled=True,
            query_refinement_enabled=True,
            multi_query_enabled=True,
            structured_query_enabled=True,
            time_weighted_retrieval=True,
        )

        print(f"✓ Query state created: {query_state.original_query}")

        # Test query management
        query_state.add_refined_query("ML applications in medical diagnosis")
        query_state.add_expanded_query("Deep learning in medical imaging")

        print(f"✓ Added queries. Total: {len(query_state.get_all_queries())}")

        # Test document management
        doc = Document(
            page_content="Machine learning is revolutionizing medical diagnosis.",
            metadata={"source": "medical_journal_1"},
        )

        query_state.add_context_document(doc)
        query_state.add_retrieved_document(doc)

        print(f"✓ Added documents. Total: {len(query_state.get_all_documents())}")

        # Test advanced methods
        all_queries = query_state.get_all_queries()
        all_docs = query_state.get_all_documents()

        print(f"✓ All queries: {len(all_queries)}")
        print(f"✓ All documents: {len(all_docs)}")

        # Test workflow detection
        is_multi = query_state.is_multi_query_workflow()
        requires_structured = query_state.requires_structured_output()

        print(f"✓ Multi-query workflow: {is_multi}")
        print(f"✓ Requires structured output: {requires_structured}")

        # Test cache key generation
        cache_key = query_state.create_cache_key()
        print(f"✓ Cache key generated: {cache_key[:8]}...")

        # Test processing summary
        summary = query_state.get_processing_summary()
        print(f"✓ Processing summary: {summary['query_type']}")

        print("✅ Advanced QueryState Features: ALL WORKING")
        return True

    except Exception as e:
        print(f"❌ Advanced QueryState Features FAILED: {e}")
        import traceback

        traceback.print_exc()
        return False


def test_integration_workflows():
    """Debug the integration workflows test."""
    print("\n🔧 Testing Integration Workflows...")

    try:
        # Create integrated workflow
        config = DocumentProcessingConfig(
            search_enabled=True,
            annotation_enabled=True,
            bulk_processing=True,
            rag_strategy="adaptive",
        )

        print("✓ Config created")

        agent = DocumentProcessingAgent(config=config, name="integration_test")
        print("✓ Agent created")

        # Create query state for integration
        query_state = QueryState(
            original_query="Comprehensive analysis of AI research",
            query_type=QueryType.RESEARCH,
            retrieval_strategy=RetrievalStrategy.ENSEMBLE,
            multi_query_enabled=True,
        )

        print("✓ Query state created")

        # Add queries
        research_queries = [
            "Latest machine learning breakthroughs",
            "AI applications in healthcare",
        ]

        for query in research_queries:
            query_state.add_refined_query(query)

        print(f"✓ Added {len(research_queries)} queries")

        # Create sample documents
        research_docs = [
            Document(
                page_content="Recent advances in transformer architectures.",
                metadata={"source": "nlp_research_2024"},
            ),
            Document(
                page_content="Computer vision models achieving human-level performance.",
                metadata={"source": "cv_advances_2024"},
            ),
        ]

        for doc in research_docs:
            query_state.add_context_document(doc)
            query_state.add_retrieved_document(doc)

        print(f"✓ Added {len(research_docs)} documents")

        # Test integration points
        all_queries = query_state.get_all_queries()
        all_docs = query_state.get_all_documents()

        print(f"✓ Total queries: {len(all_queries)}")
        print(f"✓ Total documents: {len(all_docs)}")

        # Test agent capabilities
        capabilities = agent.get_capabilities()
        print("✓ Agent capabilities retrieved")

        # Verify key capabilities
        required_sections = [
            "document_loading",
            "search_capabilities",
            "processing_pipeline",
        ]
        for section in required_sections:
            if section not in capabilities:
                raise ValueError(f"Missing capability section: {section}")

        print("✓ All required capability sections present")

        print("✅ Integration Workflows: ALL WORKING")
        return True

    except Exception as e:
        print(f"❌ Integration Workflows FAILED: {e}")
        import traceback

        traceback.print_exc()
        return False


def main():
    """Run debug tests."""
    print("🚀 Debugging Failed Tests")
    print("=" * 50)

    results = []

    # Test the two failing components
    results.append(test_advanced_query_state_features())
    results.append(test_integration_workflows())

    print("\n" + "=" * 50)
    print("📊 DEBUG SUMMARY")
    print("=" * 50)

    passed = sum(results)
    total = len(results)

    print(f"Passed: {passed}/{total}")
    print(f"Success Rate: {(passed/total*100):.1f}%")

    if passed == total:
        print("✅ All issues resolved!")
    else:
        print("❌ Some issues remain")

    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
