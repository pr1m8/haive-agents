#!/usr/bin/env python3
"""Debug the failing tests to understand the issues."""

import logging
from pathlib import Path
import sys


# Suppress all logging output
logging.getLogger().setLevel(logging.CRITICAL)

# Add the project root to the Python path
project_root = Path(__file__).parent.parent.parent.parent.parent
sys.path.insert(0, str(project_root))

from langchain_core.documents import Document

from haive.agents.document_processing import (
    DocumentProcessingAgent,
    DocumentProcessingConfig,
)
from haive.core.schema.prebuilt.query_state import (
    QueryComplexity,
    QueryIntent,
    QueryState,
    QueryType,
    RetrievalStrategy,
)


def test_advanced_query_state_features():
    """Debug the advanced QueryState features test."""
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

        # Test query management
        query_state.add_refined_query("ML applications in medical diagnosis")
        query_state.add_expanded_query("Deep learning in medical imaging")

        # Test document management
        doc = Document(
            page_content="Machine learning is revolutionizing medical diagnosis.",
            metadata={"source": "medical_journal_1"},
        )

        query_state.add_context_document(doc)
        query_state.add_retrieved_document(doc)

        # Test advanced methods
        query_state.get_all_queries()
        query_state.get_all_documents()

        # Test workflow detection
        query_state.is_multi_query_workflow()
        query_state.requires_structured_output()

        # Test cache key generation
        query_state.create_cache_key()

        # Test processing summary
        query_state.get_processing_summary()

        return True

    except Exception:
        import traceback

        traceback.print_exc()
        return False


def test_integration_workflows():
    """Debug the integration workflows test."""
    try:
        # Create integrated workflow
        config = DocumentProcessingConfig(
            search_enabled=True,
            annotation_enabled=True,
            bulk_processing=True,
            rag_strategy="adaptive",
        )

        agent = DocumentProcessingAgent(config=config, name="integration_test")

        # Create query state for integration
        query_state = QueryState(
            original_query="Comprehensive analysis of AI research",
            query_type=QueryType.RESEARCH,
            retrieval_strategy=RetrievalStrategy.ENSEMBLE,
            multi_query_enabled=True,
        )

        # Add queries
        research_queries = [
            "Latest machine learning breakthroughs",
            "AI applications in healthcare",
        ]

        for query in research_queries:
            query_state.add_refined_query(query)

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

        # Test integration points
        query_state.get_all_queries()
        query_state.get_all_documents()

        # Test agent capabilities
        capabilities = agent.get_capabilities()

        # Verify key capabilities
        required_sections = [
            "document_loading",
            "search_capabilities",
            "processing_pipeline",
        ]
        for section in required_sections:
            if section not in capabilities:
                raise ValueError(f"Missing capability section: {section}")

        return True

    except Exception:
        import traceback

        traceback.print_exc()
        return False


def main():
    """Run debug tests."""
    results = []

    # Test the two failing components
    results.append(test_advanced_query_state_features())
    results.append(test_integration_workflows())

    passed = sum(results)
    total = len(results)

    if passed == total:
        pass
    else:
        pass

    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
