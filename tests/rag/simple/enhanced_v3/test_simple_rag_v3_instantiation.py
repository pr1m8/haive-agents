#!/usr/bin/env python3
"""Try to actually instantiate SimpleRAG V3 - does it work?"""

import contextlib
import sys


# Add source paths
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")


def test_instantiation():
    """Try to create a SimpleRAG V3 instance."""
    # Step 1: Import core dependencies
    try:
        from haive.core.engine.aug_llm import AugLLMConfig
        from haive.core.engine.vectorstore import VectorStoreConfig

    except Exception:
        return False

    # Step 2: Import SimpleRAG V3 components
    try:
        from haive.agents.rag.simple.enhanced_v3 import (
            SimpleRAGV3,
        )

    except Exception:
        import traceback

        traceback.print_exc()
        return False

    # Step 3: Try to create a SimpleRAG V3 instance
    try:
        # Create configs
        llm_config = AugLLMConfig(temperature=0.7)

        # For vector store, we need to check what's required
        # Let's try with minimal config
        vector_store_config = VectorStoreConfig(
            store_type="memory",  # Assuming memory store exists
            collection_name="test_collection",
        )

        # Create SimpleRAG V3
        SimpleRAGV3(
            name="test_rag",
            vector_store_config=vector_store_config,
            llm_config=llm_config,
            top_k=5,
            performance_mode=True,
            debug_mode=True,
        )

        return True

    except Exception:
        import traceback

        traceback.print_exc()

        # Let's check what fields VectorStoreConfig needs
        with contextlib.suppress(Exception):
            from haive.core.engine.vectorstore import VectorStoreConfig

        return False


def test_factory_methods():
    """Test the factory methods."""
    try:
        from langchain_core.documents import Document

        from haive.agents.rag.simple.enhanced_v3 import SimpleRAGV3

        # Create test documents
        docs = [
            Document(
                page_content="Machine learning is great.", metadata={"source": "doc1"}
            ),
            Document(page_content="AI is the future.", metadata={"source": "doc2"}),
        ]

        # Try from_documents
        SimpleRAGV3.from_documents(
            documents=docs,
            embedding_config=None,  # We'll see what it needs
            name="test_from_docs",
        )

    except Exception:
        import traceback

        traceback.print_exc()


def main():
    """Run all tests."""
    # Test instantiation
    success = test_instantiation()

    if success:
        # If basic instantiation works, try factory methods
        test_factory_methods()

    if success:
        pass
    else:
        pass


if __name__ == "__main__":
    main()
