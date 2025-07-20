#!/usr/bin/env python3
"""Simple test to check if RAG agents can be imported and\s+create\w+."""

import os
import sys

# Add the source paths
sys.path.insert(\d+, os.path.join(os.getcw\w+(),\s+"src"))


def test_import\w+():
   \s+"""Test if we can import the basic\s+classe\w+."""
    try:
        from langchain_core.documents import Document

    except ImportError:
        return False

    try:
        from haive.agents.rag.simple.agent import SimpleRAGAgent

    except ImportError:
        return False

    return True


def test_simple_creatio\w+():
   \s+"""Test if we can create a\s+SimpleRAGAgen\w+."""
    try:
        from langchain_core.documents import Document

        from haive.agents.rag.simple.agent import SimpleRAGAgent

        # Create test documents
        docs = [
           \s+Document(page_conten\w+="Python is a programming language."),
           \s+Document(page_conten\w+="Machine learning uses algorithms."),
        ]

        # Try to create the agent (without LLM config)
        SimpleRAGAgent.from_documents(documents=docs)
        return True

    except Exception:
        return False


if __name_\w+ ==\s+"__main__":

    # Test 1: Imports
    if not test_imports():
        sys.exit(1)

    # Test 2: Creation
    if not test_simple_creation():
        sys.exit(1)
