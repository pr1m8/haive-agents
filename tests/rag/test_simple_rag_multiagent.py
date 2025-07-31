#!/usr/bin/env python3
"""Test SimpleRAG with REAL components - NO MOCKS."""

import pytest

from haive.agents.rag.simple.simple_rag import SimpleRAG
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.engine.vectorstore import VectorStoreConfig


class TestSimpleRAGMultiAgent:
    """Test SimpleRAG using clean MultiAgent pattern with REAL components."""

    def test_simple_rag_creation(self):
        """Test SimpleRAG can be created with real configs."""
        # Create real configs
        llm_config = AugLLMConfig(temperature=0.1)

        # Note: This would need a real vector store in practice
        # For now, testing the structure
        vector_config = VectorStoreConfig(
            vector_store=None  # Would be real vector store
        )

        # Create SimpleRAG
        rag = SimpleRAG.create(
            retriever_config=vector_config, llm_config=llm_config, name="test_rag"
        )

        # Verify it's a MultiAgent
        from haive.agents.multi.clean import MultiAgent

        assert isinstance(rag, MultiAgent)

        # Verify agents were created
        assert len(rag.agents) == 2
        assert "retriever" in rag.agents
        assert "generator" in rag.agents

        # Verify execution mode
        assert rag.execution_mode == "sequential"

        # Verify name
        assert rag.name == "test_rag"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
