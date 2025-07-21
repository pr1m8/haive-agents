#!/usr/bin/env python3
"""Try to actually instantiate SimpleRAG V3 - does it work?"""

import os
import sys

# Add source paths
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")


def test_instantiation():
    """Try to create a SimpleRAG V3 instance."""
    print("🚀 Testing SimpleRAG V3 Instantiation")
    print("=" * 50)

    # Step 1: Import core dependencies
    print("\n1️⃣ Testing core imports...")
    try:
        from haive.core.engine.aug_llm import AugLLMConfig
        from haive.core.engine.vectorstore import VectorStoreConfig
        from langchain_core.documents import Document

        print("✅ Core imports successful")
    except Exception as e:
        print(f"❌ Core import failed: {e}")
        return False

    # Step 2: Import SimpleRAG V3 components
    print("\n2️⃣ Testing SimpleRAG V3 imports...")
    try:
        from haive.agents.rag.simple.enhanced_v3 import (
            RetrieverAgent,
            SimpleAnswerAgent,
            SimpleRAGState,
            SimpleRAGV3,
        )

        print("✅ SimpleRAG V3 imports successful!")
        print(f"   - SimpleRAGV3: {SimpleRAGV3}")
        print(f"   - RetrieverAgent: {RetrieverAgent}")
        print(f"   - SimpleAnswerAgent: {SimpleAnswerAgent}")
        print(f"   - SimpleRAGState: {SimpleRAGState}")
    except Exception as e:
        print(f"❌ SimpleRAG V3 import failed: {e}")
        import traceback

        traceback.print_exc()
        return False

    # Step 3: Try to create a SimpleRAG V3 instance
    print("\n3️⃣ Testing SimpleRAG V3 instantiation...")
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
        rag = SimpleRAGV3(
            name="test_rag",
            vector_store_config=vector_store_config,
            llm_config=llm_config,
            top_k=5,
            performance_mode=True,
            debug_mode=True,
        )

        print("✅ SimpleRAG V3 created successfully!")
        print(f"   - Name: {rag.name}")
        print(f"   - Execution mode: {rag.execution_mode}")
        print(
            f"   - Agents: {len(rag.agents) if hasattr(rag, 'agents') else 'Not set'}"
        )

        return True

    except Exception as e:
        print(f"❌ SimpleRAG V3 instantiation failed: {e}")
        import traceback

        traceback.print_exc()

        # Let's check what fields VectorStoreConfig needs
        print("\n🔍 Checking VectorStoreConfig requirements...")
        try:
            from haive.core.engine.vectorstore import VectorStoreConfig

            print(f"VectorStoreConfig fields: {VectorStoreConfig.model_fields.keys()}")
        except:
            pass

        return False


def test_factory_methods():
    """Test the factory methods."""
    print("\n4️⃣ Testing factory methods...")

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
        print("\n   Testing from_documents...")
        rag = SimpleRAGV3.from_documents(
            documents=docs,
            embedding_config=None,  # We'll see what it needs
            name="test_from_docs",
        )
        print("✅ from_documents works!")

    except Exception as e:
        print(f"❌ Factory method failed: {e}")
        import traceback

        traceback.print_exc()


def main():
    """Run all tests."""
    # Test instantiation
    success = test_instantiation()

    if success:
        # If basic instantiation works, try factory methods
        test_factory_methods()

    print("\n" + "=" * 50)
    if success:
        print("🎉 SimpleRAG V3 CAN be instantiated!")
        print("✅ The implementation works!")
    else:
        print("❌ SimpleRAG V3 cannot be instantiated yet")
        print("🔧 Need to fix remaining import/config issues")


if __name__ == "__main__":
    main()
