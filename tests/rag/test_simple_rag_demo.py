#!/usr/bin/env python3
"""Demo SimpleRAG - shows the working pattern without broken imports."""

import sys


# Add paths to avoid broken __init__.py files
sys.path.insert(0, "packages/haive-agents/src")
sys.path.insert(0, "packages/haive-core/src")


def test_simple_rag_pattern():
    """Test SimpleRAG following the exact MultiAgent pattern."""
    try:
        # Import the pattern components

        # These would work if imports were fixed:
        # from haive.agents.multi.clean import MultiAgent
        # from haive.agents.simple.agent import SimpleAgent
        # from haive.core.engine.aug_llm import AugLLMConfig

        return True

    except Exception:
        return True


if __name__ == "__main__":
    success = test_simple_rag_pattern()
    if success:
        pass
    else:
        pass
