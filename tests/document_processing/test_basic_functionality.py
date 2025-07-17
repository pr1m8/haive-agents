#!/usr/bin/env python3
"""Simple test to verify everything is working correctly."""

import logging
import os
import sys
from pathlib import Path

# Suppress all logging output
logging.getLogger().setLevel(logging.CRITICAL)

# Add the project root to the Python path
project_root = Path(__file__).parent.parent.parent.parent.parent
sys.path.insert(0, str(project_root))

try:
    from haive.core.engine.aug_llm import AugLLMConfig
    from haive.core.schema.prebuilt.query_state import QueryState, QueryType
    from langchain_core.documents import Document

    from haive.agents.document_processing import DocumentProcessingAgent

    print("📋 Testing DocumentProcessingAgent Basic Functionality")
    print("=" * 60)

    # Test 1: Basic agent creation
    print("🔧 Test 1: Basic agent creation...")
    config = AugLLMConfig()
    agent = DocumentProcessingAgent(engine=config)
    assert agent.name == "document_processor"
    print("✅ Basic agent creation: PASSED")

    # Test 2: QueryState functionality
    print("🔧 Test 2: QueryState functionality...")
    query_state = QueryState(original_query="Test query", query_type=QueryType.SIMPLE)

    # Add some queries
    query_state.add_refined_query("Refined test query")
    query_state.add_expanded_query("Expanded test query")

    # Add documents
    doc1 = Document(page_content="Test content 1", metadata={"source": "test1"})
    doc2 = Document(page_content="Test content 2", metadata={"source": "test2"})
    query_state.add_context_document(doc1)
    query_state.add_retrieved_document(doc2)

    # Test methods
    all_queries = query_state.get_all_queries()
    assert len(all_queries) == 3  # original + 2 added

    all_docs = query_state.get_all_documents()
    assert len(all_docs) == 2  # 2 documents added

    summary = query_state.get_processing_summary()
    assert summary["original_query"] == "Test query"
    assert summary["total_queries"] == 3

    print("✅ QueryState functionality: PASSED")

    # Test 3: Agent capabilities
    print("🔧 Test 3: Agent capabilities...")
    capabilities = agent.get_capabilities()
    assert "document_loading" in capabilities
    assert "search_capabilities" in capabilities
    assert "processing_pipeline" in capabilities
    assert "rag_capabilities" in capabilities
    assert "output_features" in capabilities
    print("✅ Agent capabilities: PASSED")

    # Test 4: Configuration validation
    print("🔧 Test 4: Configuration validation...")
    from haive.agents.document_processing import DocumentProcessingConfig

    custom_config = DocumentProcessingConfig(
        search_enabled=True, annotation_enabled=True, rag_strategy="adaptive"
    )

    custom_agent = DocumentProcessingAgent(config=custom_config)
    assert custom_agent.config.search_enabled == True
    assert custom_agent.config.annotation_enabled == True
    assert custom_agent.config.rag_strategy == "adaptive"
    print("✅ Configuration validation: PASSED")

    print("\n" + "=" * 60)
    print("✅ ALL TESTS PASSED!")
    print("📊 Summary:")
    print("  - Basic agent creation: ✅")
    print("  - QueryState functionality: ✅")
    print("  - Agent capabilities: ✅")
    print("  - Configuration validation: ✅")
    print("\n🎉 DocumentProcessingAgent is working correctly!")

except Exception as e:
    print(f"\n❌ Test failed with error: {e}")
    import traceback

    traceback.print_exc()
    sys.exit(1)
